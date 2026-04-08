"""AI service — wraps Google Gemini for text enhancement & translation."""
from django.conf import settings


def _get_model():
    try:
        import google.generativeai as genai
    except ImportError:
        return None
    if not settings.GEMINI_API_KEY or settings.GEMINI_API_KEY == 'your-gemini-key-here':
        return None
    try:
        genai.configure(api_key=settings.GEMINI_API_KEY)
        return genai.GenerativeModel(settings.GEMINI_MODEL)
    except Exception:
        return None


PROMPTS = {
    'improve': "You are a professional editor. Rewrite the following text to be clearer, "
               "more impactful and professional. Keep the same meaning. Return ONLY the rewritten text, no preamble.",
    'summarize': "Summarize the following into a crisp 2-3 sentence professional summary. "
                 "Return ONLY the summary.",
    'autofill': "Generate professional sample content for a '{field}' field on a {category}. "
                "Return ONLY the content, no preamble or explanation.",
    'resume_bullets': "Convert the following job description into 3-4 concise, impact-driven "
                      "resume bullet points starting with strong action verbs. Return as plain bullets, no preamble.",
    'translate': "Translate the following text into {language}. Preserve formatting and meaning. "
                 "Return ONLY the translation, no preamble or notes.",
}


def enhance_text(text: str, mode: str = 'improve', context: dict | None = None) -> dict:
    """Run an AI enhancement via Gemini. Falls back to a local heuristic if no key."""
    context = context or {}
    model = _get_model()

    if not model:
        return {'result': _fallback(text, mode, context), 'source': 'fallback'}

    if mode == 'autofill':
        prompt = PROMPTS['autofill'].format(
            field=context.get('field', 'text'),
            category=context.get('category', 'document'),
        ) + f"\n\nContext: {context}"
    elif mode == 'translate':
        prompt = PROMPTS['translate'].format(
            language=context.get('language', 'English'),
        ) + f"\n\nText:\n{text}"
    else:
        prompt = PROMPTS.get(mode, PROMPTS['improve']) + f"\n\nText:\n{text}"

    try:
        resp = model.generate_content(prompt)
        return {'result': (resp.text or '').strip(), 'source': 'gemini'}
    except Exception as exc:
        return {'result': _fallback(text, mode, context), 'source': 'fallback', 'error': str(exc)}


def translate_dict(data: dict, language: str) -> dict:
    """Translate every string value in a data dict to target language.

    Uses the free `deep-translator` package (no API key, no Gemini call).
    Falls back silently if the package is missing or the network is down.
    """
    out = dict(data)
    if language.lower() in ('en', 'english'):
        return out

    try:
        from deep_translator import GoogleTranslator
    except ImportError:
        return out

    # Map our language names/codes to deep-translator's ISO codes
    lang_map = {
        'english': 'en', 'hindi': 'hi', 'spanish': 'es', 'french': 'fr',
        'german': 'de', 'chinese (simplified)': 'zh-CN', 'chinese': 'zh-CN',
        'arabic': 'ar', 'russian': 'ru', 'portuguese': 'pt', 'japanese': 'ja',
    }
    target = lang_map.get(language.lower(), language.lower())

    try:
        translator = GoogleTranslator(source='auto', target=target)
        for k, v in data.items():
            if isinstance(v, str) and v.strip():
                try:
                    out[k] = translator.translate(v)
                except Exception:
                    out[k] = v  # keep original on per-item failure
    except Exception:
        pass
    return out


# Cache discovered image-capable models for the lifetime of the process
_IMAGE_MODELS_CACHE = None


def _discover_image_models():
    """Ask Gemini API which models exist & which can output images.

    Returns a prioritized list of model names. Cached after first call.
    """
    global _IMAGE_MODELS_CACHE
    if _IMAGE_MODELS_CACHE is not None:
        return _IMAGE_MODELS_CACHE

    try:
        import google.generativeai as genai
    except ImportError:
        _IMAGE_MODELS_CACHE = []
        return _IMAGE_MODELS_CACHE

    try:
        genai.configure(api_key=settings.GEMINI_API_KEY)
        models = list(genai.list_models())
    except Exception:
        _IMAGE_MODELS_CACHE = []
        return _IMAGE_MODELS_CACHE

    candidates = []
    for m in models:
        name = getattr(m, 'name', '') or ''  # e.g. "models/gemini-2.5-flash-image"
        short = name.split('/')[-1]
        methods = list(getattr(m, 'supported_generation_methods', []) or [])
        if 'generateContent' not in methods:
            continue
        # Look for image-capable models by name heuristic
        if 'image' in short.lower() or 'banana' in short.lower():
            candidates.append(short)

    # Prioritise: nano-banana > newest version > "image" in name > stable > preview
    def priority(n):
        score = 0
        if 'nano-banana' in n: score += 1000
        if '3.1' in n: score += 500
        elif '3.0' in n or n.startswith('gemini-3'): score += 400
        elif '2.5' in n: score += 300
        elif '2.0' in n: score += 200
        if 'pro' in n: score += 50
        if 'image' in n: score += 20
        if 'exp' in n: score -= 10
        return -score  # negative so sorted ascending = highest first
    candidates.sort(key=priority)
    _IMAGE_MODELS_CACHE = candidates
    return candidates


def generate_image(prompt: str, style: str = '') -> dict:
    """Generate an image using whatever Gemini image model is available.

    The model is auto-discovered from the API — no hardcoded names.

    Returns:
        {'image': 'data:image/png;base64,...', 'source': 'gemini', 'model': '...'}
        or {'error': '...'} on failure.
    """
    try:
        import google.generativeai as genai
    except ImportError:
        return {'error': 'google-generativeai package not installed'}

    if not settings.GEMINI_API_KEY or settings.GEMINI_API_KEY == 'your-gemini-key-here':
        return {'error': 'Gemini API key not configured in .env'}

    full_prompt = prompt.strip()
    if style:
        full_prompt = f"{full_prompt}. Style: {style}."

    try:
        genai.configure(api_key=settings.GEMINI_API_KEY)
    except Exception as exc:
        return {'error': f'configure failed: {exc}'}

    model_candidates = _discover_image_models()
    if not model_candidates:
        return {'error': 'No image-capable Gemini model found for this API key. '
                         'Try regenerating your key at https://aistudio.google.com/apikey'}

    import re
    last_error = None
    last_retry_after = None
    quota_hit = False
    for model_name in model_candidates:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(full_prompt)
            for cand in (response.candidates or []):
                content = getattr(cand, 'content', None)
                for part in (getattr(content, 'parts', None) or []):
                    inline = getattr(part, 'inline_data', None)
                    if inline and getattr(inline, 'data', None):
                        import base64
                        data = inline.data
                        if isinstance(data, str):
                            b64 = data
                        else:
                            b64 = base64.b64encode(data).decode('utf-8')
                        mime = getattr(inline, 'mime_type', None) or 'image/png'
                        return {
                            'image': f'data:{mime};base64,{b64}',
                            'source': 'gemini',
                            'model': model_name,
                        }
            last_error = f'{model_name}: no image returned'
        except Exception as exc:
            err_str = str(exc)
            # Detect 429 / quota errors so we can show a friendlier message
            if '429' in err_str or 'quota' in err_str.lower() or 'exceeded' in err_str.lower():
                quota_hit = True
                m = re.search(r'retry[_ ]delay[^\d]*(\d+)', err_str, re.I) or \
                    re.search(r'retry in (\d+(?:\.\d+)?)', err_str, re.I)
                if m:
                    try:
                        last_retry_after = int(float(m.group(1)))
                    except (ValueError, IndexError):
                        pass
            last_error = f'{model_name}: {exc}'
            continue

    if quota_hit:
        return {
            'error': 'rate_limit',
            'message': 'Free tier quota reached for image generation. Please wait and try again.',
            'retry_after': last_retry_after or 60,
            'tried': model_candidates,
        }

    return {
        'error': 'failed',
        'message': f'Tried {len(model_candidates)} model(s), none returned an image.',
        'detail': last_error,
        'tried': model_candidates,
    }


def _fallback(text: str, mode: str, context: dict) -> str:
    """Local heuristic when Gemini is unavailable — keeps the UI usable."""
    text = (text or '').strip()
    if mode == 'summarize':
        sentences = [s.strip() for s in text.replace('\n', ' ').split('.') if s.strip()]
        return '. '.join(sentences[:2]) + ('.' if sentences else '')
    if mode == 'autofill':
        field = context.get('field', 'field')
        samples = {
            'name': 'Aarav Sharma',
            'email': 'aarav.sharma@example.com',
            'phone': '+91 98765 43210',
            'title': 'Senior Software Engineer',
            'company': 'Acme Technologies Pvt Ltd',
            'summary': 'Results-driven professional with 5+ years of experience delivering scalable solutions and leading cross-functional teams to success.',
            'address': '221B Baker Street, Mumbai, India',
        }
        return samples.get(field.lower(), f'Sample {field}')
    if mode == 'resume_bullets':
        return ('• Led key initiatives that improved efficiency by 30%\n'
                '• Collaborated with cross-functional teams to deliver projects on time\n'
                '• Mentored junior team members and improved team velocity')
    if mode == 'translate':
        return text  # No fallback translation
    if not text:
        return 'Please provide some text to enhance.'
    return text[0].upper() + text[1:] + (' — refined for clarity and impact.' if len(text) < 200 else '')
