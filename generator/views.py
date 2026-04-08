from django.shortcuts import render, get_object_or_404, redirect
from django.template import Template as DjangoTemplate, Context
from django.http import HttpResponse, JsonResponse
from django.db import models
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
import json
import secrets
from datetime import datetime, timedelta

from .models import Template, GeneratedDocument, Subscription, BrandKit, get_user_plan
from .serializers import TemplateSerializer, GeneratedDocumentSerializer
from .ai_service import enhance_text, translate_dict, generate_image
from collections import defaultdict
import time

# Simple in-memory rate limiter (per-IP)
_RATE_BUCKET = defaultdict(list)
def _rate_limit(request, key, max_calls, window_sec):
    """Return True if allowed, False if rate-limited."""
    ip = request.META.get('REMOTE_ADDR', 'unknown')
    bucket_key = f'{key}:{ip}'
    now = time.time()
    bucket = _RATE_BUCKET[bucket_key]
    # Drop old entries
    _RATE_BUCKET[bucket_key] = [t for t in bucket if now - t < window_sec]
    if len(_RATE_BUCKET[bucket_key]) >= max_calls:
        return False
    _RATE_BUCKET[bucket_key].append(now)
    return True


CATEGORIES = [
    {'key': 'resume',       'label': 'Resumes',         'icon': '📄', 'desc': 'Land your dream job with AI-crafted resumes.'},
    {'key': 'cover_letter', 'label': 'Cover Letters',   'icon': '✉️', 'desc': 'Pair your resume with a winning letter.'},
    {'key': 'invoice',      'label': 'Invoices',        'icon': '🧾', 'desc': 'Professional invoices in seconds.'},
    {'key': 'voucher',      'label': 'Gift Vouchers',   'icon': '🎁', 'desc': 'Reward customers with stylish vouchers.'},
    {'key': 'card',         'label': 'Visiting Cards',  'icon': '💳', 'desc': 'Memorable business cards that pop.'},
    {'key': 'certificate',  'label': 'Certificates',    'icon': '🏆', 'desc': 'Award-winning certificates of achievement.'},
    {'key': 'social',       'label': 'Social Posts',    'icon': '📱', 'desc': 'Eye-catching posts for every platform.'},
    {'key': 'flyer',        'label': 'Flyers & Posters','icon': '📋', 'desc': 'Promote events, sales and services.'},
    {'key': 'wedding',      'label': 'Wedding Invites', 'icon': '💍', 'desc': 'Elegant wedding invitations to cherish.'},
    {'key': 'birthday',     'label': 'Birthday Invites','icon': '🎂', 'desc': 'Fun party invites for every age.'},
    {'key': 'festival',     'label': 'Festival Cards',  'icon': '🪔', 'desc': 'Diwali, Holi, Christmas & more.'},
    {'key': 'menu',         'label': 'Menu Cards',      'icon': '🍽️', 'desc': 'Beautiful menus for cafes & restaurants.'},
    {'key': 'ticket',       'label': 'Event Tickets',   'icon': '🎫', 'desc': 'Tickets for shows, concerts & workshops.'},
]


# ---------- HTML Pages ----------

# ============== DATE-AWARE FESTIVAL HERO ==============
# Each festival: (month, day_start, day_end, name, sub_category_key, icon, palette)
FESTIVAL_CALENDAR = [
    (1, 1, 5,    'Happy New Year',     'new year',     '🎆', '#312e81'),
    (1, 13, 17,  'Lohri & Pongal',     'lohri',        '🔥', '#dc2626'),
    (1, 25, 28,  'Republic Day',       'republic',     '🇮🇳', '#1e40af'),
    (2, 12, 16,  'Valentine\'s Day',   'valentine',    '❤️', '#dc2626'),
    (3, 5, 18,   'Holi · Festival of Colours', 'holi', '🎨', '#ec4899'),
    (3, 28, 31,  'Eid Mubarak',        'eid',          '☪',  '#064e3b'),
    (4, 13, 17,  'Tamil New Year · Vishu', 'pongal',   '🌾', '#f59e0b'),
    (5, 8, 12,   'Mother\'s Day',      'mother',       '💐', '#ec4899'),
    (6, 14, 17,  'Father\'s Day',      'father',       '👔', '#1e40af'),
    (8, 14, 19,  'Raksha Bandhan',     'raksha',       '🎀', '#dc2626'),
    (8, 14, 16,  'Independence Day',   'independence', '🇮🇳', '#15803d'),
    (8, 24, 28,  'Janmashtami',        'janmashtami',  '🦚', '#0891b2'),
    (9, 5, 9,    'Ganesh Chaturthi',   'ganesh',       '🐘', '#f59e0b'),
    (9, 22, 30,  'Onam',               'onam',         '🌸', '#15803d'),
    (10, 1, 12,  'Navratri · Garba',   'navratri',     '💃', '#dc2626'),
    (10, 13, 14, 'Dussehra',           'dussehra',     '🏹', '#dc2626'),
    (10, 31, 31, 'Halloween',          'halloween',    '🎃', '#7c2d12'),
    (11, 1, 5,   'Karva Chauth',       'karva',        '🌙', '#9d174d'),
    (11, 1, 14,  'Diwali · Festival of Lights', 'diwali', '🪔', '#b45309'),
    (11, 25, 30, 'Thanksgiving',       'thanksgiving', '🦃', '#9a3412'),
    (12, 20, 31, 'Merry Christmas',    'christmas',    '🎄', '#15803d'),
]


def get_active_festival():
    """Return the festival happening now or upcoming within 14 days."""
    from datetime import date, timedelta
    today = date.today()
    for month, ds, de, name, key, icon, color in FESTIVAL_CALENDAR:
        try:
            start = date(today.year, month, ds)
            end = date(today.year, month, de)
        except ValueError:
            continue
        # Active if today within range
        if start <= today <= end:
            return {'name': name, 'key': key, 'icon': icon, 'color': color, 'days_until': 0, 'active': True}
        # Upcoming within 14 days
        days_until = (start - today).days
        if 0 < days_until <= 14:
            return {'name': name, 'key': key, 'icon': icon, 'color': color, 'days_until': days_until, 'active': False}
    return None


def home(request):
    from django.db.models import Count
    counts = dict(Template.objects.values_list('category').annotate(n=Count('id')))
    cats = [{**c, 'count': counts.get(c['key'], 0)} for c in CATEGORIES]
    total = sum(counts.values())

    # Most popular templates by usage (document count) — top 6
    popular = list(
        Template.objects.annotate(usage=Count('documents'))
        .order_by('-usage', '?')[:6]
    )
    popular_items = [{
        'tpl': t,
        'preview_html': render_template_html(t, t.sample_data or {}, use_cache=True),
    } for t in popular]

    # Date-aware festival hero — only show if templates actually exist for this festival
    festival = get_active_festival()
    festival_templates = []
    if festival:
        ftemplates = list(
            Template.objects.filter(sub_category=festival['key']).order_by('?')[:6]
        )
        if ftemplates:
            festival_templates = [{
                'tpl': t,
                'preview_html': render_template_html(t, t.sample_data or {}, use_cache=True),
            } for t in ftemplates]
        else:
            # No templates for this festival yet — hide the banner entirely
            festival = None

    return render(request, 'home.html', {
        'categories': cats,
        'total_templates': total,
        'popular_items': popular_items,
        'festival': festival,
        'festival_templates': festival_templates,
    })


def _detect_subcategory(tpl):
    """Detect a sub-category for a template based on title + description.
    Returns (sort_order, key, label, icon)."""
    text = (tpl.title + ' ' + tpl.description).lower()
    cat = tpl.category

    # ===== WEDDING sub-categories =====
    if cat == 'wedding':
        if '🎬' in tpl.title or 'animated' in text:
            return (0, 'animated', 'Animated', '🎬')
        if '✦' in tpl.title:
            return (1, 'premium', 'Premium Designs', '⭐')
        if 'hindu' in text or 'mandap' in text or 'lotus' in text or 'ganesh' in text or 'royal maroon' in text or 'royal purple' in text or 'saffron' in text:
            return (2, 'hindu', 'Hindu Wedding', '🕉')
        if 'muslim' in text or 'nikah' in text or 'islamic' in text or 'samira' in text or 'pakistani' in text or 'bismillah' in text:
            return (3, 'muslim', 'Muslim / Islamic', '☪')
        if 'christian' in text or 'church' in text:
            return (4, 'christian', 'Christian Wedding', '✝')
        if 'sikh' in text or 'anand karaj' in text or 'khanda' in text or 'punjabi' in text:
            return (5, 'sikh', 'Sikh / Punjabi', '☬')
        if 'tamil' in text or 'south indian' in text:
            return (6, 'tamil', 'Tamil Wedding', '🛕')
        if 'telugu' in text:
            return (6, 'telugu', 'Telugu Wedding', '🛕')
        if 'marathi' in text:
            return (7, 'marathi', 'Marathi Wedding', '🪔')
        if 'bengali' in text:
            return (7, 'bengali', 'Bengali Wedding', '🐚')
        if 'gujarati' in text:
            return (7, 'gujarati', 'Gujarati Wedding', '🪔')
        if 'mehendi' in text:
            return (8, 'mehendi', 'Mehendi Ceremony', '🌿')
        if 'sangeet' in text:
            return (8, 'sangeet', 'Sangeet Night', '💃')
        if 'haldi' in text:
            return (8, 'haldi', 'Haldi Ceremony', '🌼')
        if 'baraat' in text:
            return (8, 'baraat', 'Baraat Procession', '🐎')
        return (9, 'modern', 'Modern & Classic', '✨')

    # ===== FESTIVAL sub-categories =====
    if cat == 'festival':
        if 'diwali' in text:
            return (0, 'diwali', 'Diwali', '🪔')
        if 'holi' in text:
            return (1, 'holi', 'Holi', '🎨')
        if 'christmas' in text:
            return (2, 'christmas', 'Christmas', '🎄')
        if 'eid' in text:
            return (3, 'eid', 'Eid', '🌙')
        if 'onam' in text:
            return (4, 'onam', 'Onam', '🌸')
        if 'pongal' in text:
            return (4, 'pongal', 'Pongal', '🌾')
        if 'lohri' in text:
            return (4, 'lohri', 'Lohri', '🔥')
        if 'bihu' in text:
            return (4, 'bihu', 'Bihu', '💃')
        if 'janmashtami' in text or 'krishna' in text:
            return (4, 'janmashtami', 'Janmashtami', '🦚')
        if 'karva chauth' in text:
            return (4, 'karva', 'Karva Chauth', '🌙')
        if 'navratri' in text or 'garba' in text:
            return (4, 'navratri', 'Navratri', '💃')
        if 'ganesh' in text:
            return (4, 'ganesh', 'Ganesh Chaturthi', '🐘')
        if 'raksha' in text or 'bandhan' in text:
            return (4, 'raksha', 'Raksha Bandhan', '🎀')
        if 'republic' in text:
            return (5, 'republic', 'Republic Day', '🇮🇳')
        if 'valentine' in text:
            return (6, 'valentine', 'Valentine\'s Day', '❤')
        if 'mother' in text:
            return (6, 'mother', 'Mother\'s Day', '💐')
        if 'father' in text:
            return (6, 'father', 'Father\'s Day', '👔')
        if 'easter' in text:
            return (6, 'easter', 'Easter', '🐰')
        if 'thanksgiving' in text:
            return (6, 'thanksgiving', 'Thanksgiving', '🦃')
        if 'new year' in text:
            return (6, 'newyear', 'New Year', '🎆')
        return (9, 'other', 'Other Festivals', '✨')

    # ===== RESUME sub-categories =====
    if cat == 'resume':
        if '✦' in tpl.title:
            return (0, 'premium', 'Premium Designs', '⭐')
        if 'tech' in text or 'developer' in text or 'mono' in text:
            return (1, 'tech', 'Tech / Developer', '💻')
        if 'executive' in text or 'finance' in text or 'corporate' in text:
            return (2, 'executive', 'Executive / Finance', '💼')
        if 'creative' in text or 'designer' in text or 'pink' in text:
            return (3, 'creative', 'Creative / Designer', '🎨')
        if 'classic' in text or 'professional' in text or 'serif' in text:
            return (4, 'classic', 'Classic / Professional', '📜')
        if 'modern' in text or 'minimal' in text or 'fresh' in text or 'compact' in text:
            return (5, 'modern', 'Modern / Minimal', '✨')
        if 'academic' in text or 'educator' in text or 'graduate' in text:
            return (6, 'academic', 'Academic / Education', '🎓')
        if 'healthcare' in text or 'medical' in text:
            return (7, 'healthcare', 'Healthcare / Medical', '⚕')
        if 'sales' in text or 'marketing' in text:
            return (8, 'sales', 'Sales / Marketing', '📈')
        return (9, 'other', 'Other Styles', '📄')

    return (0, 'all', 'All', '✨')


CATEGORY_FAQS = {
    'resume': [
        ("Are these resume templates really free?", "Yes — all 56 resume templates are 100% free. No credit card, no signup. Just pick one, fill in your details and download as PDF."),
        ("Will the AI write my resume for me?", "Pagecraft's built-in AI can improve your bullet points, generate professional summaries, suggest action verbs and translate to 10 languages — all with one click."),
        ("Can I use these for ATS systems?", "Yes — most templates use clean, parseable HTML structure. Choose minimal/modern templates for the best ATS compatibility."),
        ("Can I edit fonts and colors?", "Absolutely. Pro users can apply a Brand Kit (logo, colors, fonts) to any template instantly."),
    ],
    'wedding': [
        ("Do you have Indian wedding card templates?", "Yes — 70+ Indian wedding templates including Hindu, Muslim, Sikh, Christian, Tamil, Telugu, Marathi, Bengali, Gujarati and Punjabi styles."),
        ("Can I share the invitation digitally?", "Yes — every saved invitation gets a public share link. Send via WhatsApp, email or SMS. No app needed for guests."),
        ("Are animated wedding cards available?", "Yes! Some templates use CSS animations and can be exported as animated GIFs for WhatsApp sharing."),
        ("Can I print these as physical cards?", "Yes — download as high-resolution PDF and print at any local press. All templates are print-ready."),
    ],
    'invoice': [
        ("Do these invoice templates support GST?", "Yes — all invoice templates support adding GST/VAT line items, tax breakdowns and total calculations."),
        ("Can I save my company branding?", "Pro users can save a Brand Kit (logo, colors, address) and apply it to any invoice with one click."),
        ("Can I send invoices directly from Pagecraft?", "You can download as PDF or share via public link. Email/print integration is on our roadmap."),
        ("Is there a limit to how many invoices I can create?", "Free plan: 5 downloads/month. Pro plan: unlimited."),
    ],
    'festival': [
        ("Which festivals are covered?", "Diwali, Holi, Navratri, Eid, Christmas, Lohri, Pongal, Onam, Janmashtami, Ganesh Chaturthi, Raksha Bandhan, Karva Chauth, New Year and more."),
        ("Can I send festival cards on WhatsApp?", "Yes — download as PNG/JPG or share via public link. Optimized for WhatsApp sharing."),
        ("Are messages in regional languages?", "AI can translate any festival greeting to Hindi, Tamil, Telugu, Marathi, Bengali and 5 more languages instantly."),
        ("Can I add my own message?", "Yes — every template has editable text fields. Type your own greeting or let AI write one."),
    ],
    'card': [
        ("Are visiting cards print-ready?", "Yes — all 40 business card templates are designed at standard print dimensions and download as high-resolution PDF."),
        ("Can I add a QR code to my card?", "Yes — Pagecraft auto-generates QR codes for your phone, website or vCard."),
        ("Can I use my logo?", "Yes — upload your logo or save it in your Brand Kit (Pro feature)."),
    ],
    'birthday': [
        ("Do you have kids birthday templates?", "Yes — playful, colorful templates designed for kids birthdays with cartoon themes, balloons and rainbow palettes."),
        ("Can I include party details and RSVP?", "Yes — all birthday templates include fields for date, time, venue and RSVP contact."),
        ("Can I share via WhatsApp?", "Yes — one-click share creates a public link, or download as PNG to send directly."),
    ],
}


def get_category_faqs(category):
    """Returns FAQ list for a category, with sensible defaults."""
    return CATEGORY_FAQS.get(category, [
        (f"Are these {category} templates free?", "Yes, all templates are free to use. No signup required."),
        ("Can I edit them?", "Yes — every template is fully editable. Type your own content and customize."),
        ("Can I download as PDF?", "Yes — export as PDF, PNG, JPG or animated GIF."),
        ("Do I need to sign up?", "No — start creating immediately. Sign up only if you want to save your work."),
    ])


def category_view(request, category):
    from django.db.models import Count
    templates = list(Template.objects.filter(category=category).order_by('title'))
    label = dict(Template.CATEGORY_CHOICES).get(category, category.title())
    items = [{'tpl': tpl, 'preview_html': render_template_html(tpl, tpl.sample_data or {}, use_cache=True)}
             for tpl in templates]
    cat_meta = next((c for c in CATEGORIES if c['key'] == category), None)
    counts = dict(Template.objects.values_list('category').annotate(n=Count('id')))
    all_cats = [{**c, 'count': counts.get(c['key'], 0)} for c in CATEGORIES]

    # Build sub-groups for categories that have them (wedding/festival/resume)
    subgroups = []
    if category in ('wedding', 'festival', 'resume'):
        groups_dict = {}
        for it in items:
            sort_order, key, label2, icon = _detect_subcategory(it['tpl'])
            if key not in groups_dict:
                groups_dict[key] = {'sort': sort_order, 'key': key, 'label': label2, 'icon': icon, 'items': []}
            groups_dict[key]['items'].append(it)
        subgroups = sorted(groups_dict.values(), key=lambda g: (g['sort'], g['label']))

    return render(request, 'category.html', {
        'items': items, 'category': category, 'category_label': label,
        'category_meta': cat_meta, 'all_categories': all_cats,
        'subgroups': subgroups,
        'faqs': get_category_faqs(category),
        'total_count': len(templates),
    })


def editor_view(request, template_id):
    tpl = get_object_or_404(Template, pk=template_id)

    # Track view (atomic, no lock — single UPDATE) — non-blocking
    Template.objects.filter(pk=tpl.pk).update(view_count=models.F('view_count') + 1)

    # Smart related templates: prefer same sub_category, then same category
    related_qs = Template.objects.filter(category=tpl.category).exclude(pk=tpl.pk)
    if tpl.sub_category:
        same_sub = list(related_qs.filter(sub_category=tpl.sub_category).order_by('?')[:6])
        if len(same_sub) < 6:
            extra = list(related_qs.exclude(sub_category=tpl.sub_category).order_by('?')[:6 - len(same_sub)])
            related = same_sub + extra
        else:
            related = same_sub
    else:
        related = list(related_qs.order_by('?')[:6])
    related_items = [{
        'tpl': r,
        'preview_html': render_template_html(r, r.sample_data or {}, use_cache=True),
    } for r in related]

    # Prev / Next within same category (alphabetical by id)
    same_cat = list(Template.objects.filter(category=tpl.category).order_by('id').values_list('id', flat=True))
    cur_idx = same_cat.index(tpl.id) if tpl.id in same_cat else 0
    prev_id = same_cat[cur_idx - 1] if cur_idx > 0 else same_cat[-1]
    next_id = same_cat[cur_idx + 1] if cur_idx < len(same_cat) - 1 else same_cat[0]

    sub = get_user_plan(request.user)
    has_no_watermark = bool(sub and sub.has_feature('no_watermark'))
    return render(request, 'editor.html', {
        'template': tpl,
        'template_json': json.dumps(TemplateSerializer(tpl).data),
        'related_items': related_items,
        'prev_id': prev_id,
        'next_id': next_id,
        'category_position': f'{cur_idx + 1} / {len(same_cat)}',
        'share_url_absolute': request.build_absolute_uri(),
        'has_no_watermark': has_no_watermark,
    })


@login_required
def documents_view(request):
    docs = GeneratedDocument.objects.select_related('template').filter(user=request.user)[:50]
    return render(request, 'documents.html', {'documents': docs})


# ---------- Template Clone (Duplicate) ----------


def template_clone_view(request, template_id):
    """Duplicate an existing template into a new editable copy."""
    src = get_object_or_404(Template, pk=template_id)
    tpl = Template.objects.create(
        title=src.title + ' (copy)',
        category=src.category,
        description=src.description,
        html_layout=src.html_layout,
        css_layout=src.css_layout,
        fields_schema=src.fields_schema,
        sample_data=src.sample_data,
    )
    from django.shortcuts import redirect
    return redirect('editor', template_id=tpl.id)


def robots_txt(request):
    text = "User-agent: *\nAllow: /\nDisallow: /admin/\nDisallow: /api/\nSitemap: " + request.build_absolute_uri('/sitemap.xml')
    return HttpResponse(text, content_type='text/plain')


def sitemap_xml(request):
    """Full sitemap with all 496+ templates, priority + lastmod.
    Cached for 1 hour to avoid hitting DB on every Googlebot fetch."""
    from django.core.cache import cache
    cached = cache.get('sitemap_xml_v2')
    if cached:
        return HttpResponse(cached, content_type='application/xml')

    base = request.build_absolute_uri('/').rstrip('/')
    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

    def url(loc, priority='0.5', changefreq='weekly', lastmod=None):
        bits = [f'<loc>{loc}</loc>',
                f'<changefreq>{changefreq}</changefreq>',
                f'<priority>{priority}</priority>']
        if lastmod:
            bits.append(f'<lastmod>{lastmod.strftime("%Y-%m-%d")}</lastmod>')
        return '<url>' + ''.join(bits) + '</url>'

    # 1. Static high-priority pages
    parts.append(url(f'{base}/', '1.0', 'daily'))
    parts.append(url(f'{base}/templates/', '0.9', 'daily'))
    parts.append(url(f'{base}/ai-template/', '0.8', 'weekly'))
    parts.append(url(f'{base}/pricing/', '0.7', 'monthly'))
    parts.append(url(f'{base}/features/', '0.6', 'monthly'))
    parts.append(url(f'{base}/compare/', '0.6', 'monthly'))
    parts.append(url(f'{base}/about/', '0.4', 'monthly'))
    parts.append(url(f'{base}/faq/', '0.5', 'monthly'))
    parts.append(url(f'{base}/contact/', '0.4', 'monthly'))

    # 2. All categories (high priority — landing pages)
    for c in CATEGORIES:
        parts.append(url(f'{base}/category/{c["key"]}/', '0.9', 'weekly'))

    # 3. ALL templates (single optimized query, only fields needed)
    template_qs = Template.objects.only('id', 'updated_at', 'created_at', 'is_premium', 'is_featured', 'download_count')
    for tpl in template_qs.iterator(chunk_size=200):
        priority = '0.8' if tpl.is_featured else ('0.7' if tpl.is_premium else '0.6')
        if tpl.download_count > 50:
            priority = '0.85'
        lastmod = tpl.updated_at or tpl.created_at
        parts.append(url(f'{base}/editor/{tpl.id}/', priority, 'monthly', lastmod))

    parts.append('</urlset>')
    xml = ''.join(parts)
    cache.set('sitemap_xml_v2', xml, 3600)  # 1 hour cache
    return HttpResponse(xml, content_type='application/xml')


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def custom_500(request):
    return render(request, '500.html', status=500)


FILTER_COLORS = ['blue', 'red', 'pink', 'green', 'orange', 'gold', 'purple', 'teal', 'maroon', 'black', 'white']
FILTER_TAGS = [
    ('new', '🆕 New'),
    ('hot', '🔥 Hot'),
    ('trending', '📈 Trending'),
    ('animated', '🎬 Animated'),
    ('indian', '🇮🇳 Indian'),
    ('premium', '⭐ Premium'),
    ('free', '🎁 Free'),
]


def all_templates_view(request):
    """Browse templates GROUPED BY CATEGORY with smart filtering: search, color, tag, sort."""
    from django.db.models import Count, Q

    q = (request.GET.get('q') or '').strip()
    selected_cat = request.GET.get('category', '')
    color_filter = (request.GET.get('color') or '').strip().lower()
    tag_filter = (request.GET.get('tag') or '').strip().lower()
    sort = (request.GET.get('sort') or '').strip()

    counts = dict(Template.objects.values_list('category').annotate(n=Count('id')))
    cat_chips = [{**c, 'count': counts.get(c['key'], 0)} for c in CATEGORIES]

    base_qs = Template.objects.all()
    if q:
        base_qs = base_qs.filter(
            Q(title__icontains=q) | Q(description__icontains=q) | Q(keywords__icontains=q)
        )
    if color_filter:
        base_qs = base_qs.filter(color_tags__contains=[color_filter])
    if tag_filter:
        base_qs = base_qs.filter(tags__contains=[tag_filter])

    # Sort options
    if sort == 'newest':
        base_qs = base_qs.order_by('-created_at')
    elif sort == 'popular':
        base_qs = base_qs.order_by('-download_count', '-view_count')
    elif sort == 'trending':
        base_qs = base_qs.order_by('-view_count')

    has_filters = bool(q or color_filter or tag_filter or sort)

    # When filtered to one category OR any filter active, show ALL matching. Else 8 per category.
    if selected_cat or has_filters:
        if selected_cat:
            cats_to_show = [c for c in CATEGORIES if c['key'] == selected_cat]
        else:
            cats_to_show = CATEGORIES
        per_cat_limit = 1000
    else:
        cats_to_show = CATEGORIES
        per_cat_limit = 8

    groups = []
    total_displayed = 0
    for c in cats_to_show:
        cat_list = list(base_qs.filter(category=c['key'])[:per_cat_limit])
        if not cat_list:
            continue
        items = [{
            'tpl': tpl,
            'preview_html': render_template_html(tpl, tpl.sample_data or {}, use_cache=True),
        } for tpl in cat_list]
        total_displayed += len(items)
        groups.append({
            'key': c['key'],
            'label': c['label'],
            'icon': c['icon'],
            'desc': c['desc'],
            'count': counts.get(c['key'], 0),
            'items': items,
            'show_view_all': counts.get(c['key'], 0) > per_cat_limit,
        })

    return render(request, 'all_templates.html', {
        'groups': groups,
        'cat_chips': cat_chips,
        'query': q,
        'selected_cat': selected_cat,
        'color_filter': color_filter,
        'tag_filter': tag_filter,
        'sort': sort,
        'has_filters': has_filters,
        'filter_colors': FILTER_COLORS,
        'filter_tags': FILTER_TAGS,
        'total_results': total_displayed,
        'total_all': sum(counts.values()),
    })


# ---------- Compare: same content across multiple templates ----------

def compare_templates_view(request, category):
    """Show all templates of a category rendered with the SAME (sample or user) data."""
    templates = list(Template.objects.filter(category=category))
    label = dict(Template.CATEGORY_CHOICES).get(category, category.title())
    # Use first template's sample data as the shared dataset
    base_data = templates[0].sample_data if templates else {}
    items = [{'tpl': t, 'preview_html': render_template_html(t, base_data)}
             for t in templates]
    return render(request, 'compare_templates.html', {
        'items': items, 'category': category, 'category_label': label,
        'base_data_json': json.dumps(base_data),
    })


# ---------- Static / Business Pages ----------

def about_view(request):
    return render(request, 'pages/about.html')

def features_view(request):
    total = Template.objects.count()
    return render(request, 'pages/features.html', {'total_templates': total})

def pricing_view(request):
    total = Template.objects.count()
    return render(request, 'pages/pricing.html', {'total_templates': total})

def contact_view(request):
    from .emails import send_contact_form_email
    sent = False
    if request.method == 'POST':
        name = (request.POST.get('name') or '').strip()
        email = (request.POST.get('email') or '').strip()
        message = (request.POST.get('message') or '').strip()
        if name and email and message:
            send_contact_form_email(name, email, message)
            sent = True
    return render(request, 'pages/contact.html', {'sent': sent})

def faq_view(request):
    faqs = [
        ('Is Pagecraft free to use?', 'Yes! Our Starter plan is free forever and includes all template categories.'),
        ('Do I need a Gemini API key?', 'No. The app works without one — AI features fall back to a smart local heuristic. Add your free Gemini key in .env for full power.'),
        ('Can I export to PDF?', 'Yes — every template supports one-click PDF export. PDFs are generated client-side for privacy and reliability.'),
        ('How many languages are supported?', 'Pagecraft supports 10 languages: English, Hindi, Spanish, French, German, Chinese, Arabic, Russian, Portuguese, and Japanese.'),
        ('Can I see the same content in multiple templates?', 'Yes! Use the "Compare Templates" feature on any category page to see the same content rendered across all templates.'),
        ('Can I save and re-edit my documents?', 'Absolutely. Every saved document is stored and editable from "My Documents".'),
        ('Are there templates for Indian weddings?', 'Yes — we ship 15 wedding invitation designs including a Royal Indian style.'),
        ('Can I add my own templates?', 'Yes, via the Django admin. Templates are stored in the database with HTML/CSS layouts.'),
    ]
    return render(request, 'pages/faq.html', {'faqs': faqs})

def compare_view(request):
    """Pagecraft vs competitors comparison page.
    Honest labeling: ✓ Free / ⭐ Pro / ⭐ Pro+ / ⚠ Limited / ✗ None.
    """
    total = Template.objects.count()
    groups = [
        {
            'title': 'Pricing & Plans',
            'icon': '💸',
            'rows': [
                {'feature': 'Cheapest paid plan (per month)', 'pagecraft': '₹149', 'canva': '₹500', 'adobe': '₹830', 'word': '₹489', 'highlight': True},
                {'feature': 'Yearly cost (full features)', 'pagecraft': '₹1,188', 'canva': '₹6,000', 'adobe': '₹9,960', 'word': '₹5,868', 'highlight': True},
                {'feature': 'Lifetime option (one-time)', 'pagecraft': '✓ ₹1,999', 'canva': '✗', 'adobe': '✗', 'word': '✗', 'highlight': True},
                {'feature': 'Free forever plan', 'pagecraft': '✓', 'canva': '⚠ Limited', 'adobe': '⚠ Trial', 'word': '✗'},
                {'feature': 'Number of free templates', 'pagecraft': f'{total}+ all unlocked', 'canva': '⚠ Few', 'adobe': '⚠ Few', 'word': '~50'},
                {'feature': '30-day money-back guarantee', 'pagecraft': '✓', 'canva': '⚠ 7 days', 'adobe': '⚠ 14 days', 'word': '✗'},
                {'feature': 'Open source / self-hostable', 'pagecraft': '✓', 'canva': '✗', 'adobe': '✗', 'word': '✗'},
            ]
        },
        {
            'title': 'AI Superpowers',
            'icon': '🤖',
            'rows': [
                {'feature': 'AI text enhancement', 'pagecraft': '✓ Free (30/day)', 'canva': '⭐ Pro only', 'adobe': '⭐ Pro only', 'word': '✗', 'highlight': True},
                {'feature': 'AI Template Generator (Gemini)', 'pagecraft': '⭐ Pro · ₹149', 'canva': '⭐ Pro · ₹500', 'adobe': '⭐ Pro · ₹830', 'word': '✗', 'highlight': True},
                {'feature': 'AI image generation', 'pagecraft': '⭐ Pro · ₹149', 'canva': '⭐ Pro · ₹500', 'adobe': '⭐ Pro · ₹830', 'word': '✗'},
                {'feature': '10-language AI translation', 'pagecraft': '✓ Free', 'canva': '✗', 'adobe': '✗', 'word': '⚠ Manual'},
                {'feature': 'Surprise Me (random + AI fill)', 'pagecraft': '✓ Free', 'canva': '✗', 'adobe': '✗', 'word': '✗'},
            ]
        },
        {
            'title': 'Made for India',
            'icon': '🇮🇳',
            'rows': [
                {'feature': 'Hindu / Muslim / Christian / Sikh wedding cards', 'pagecraft': '✓ Free 70+', 'canva': '⚠ Few', 'adobe': '✗', 'word': '✗', 'highlight': True},
                {'feature': 'Regional weddings (Tamil/Telugu/Marathi/Punjabi/Bengali)', 'pagecraft': '✓ Free', 'canva': '✗', 'adobe': '✗', 'word': '✗'},
                {'feature': 'Ceremony cards (Mehendi/Sangeet/Haldi/Baraat)', 'pagecraft': '✓ Free', 'canva': '✗', 'adobe': '✗', 'word': '✗'},
                {'feature': 'Festival cards (Diwali/Holi/Lohri/Pongal/Onam etc.)', 'pagecraft': '✓ Free 36', 'canva': '⚠ Few', 'adobe': '✗', 'word': '✗'},
                {'feature': 'Date-aware festival hero', 'pagecraft': '✓ Auto', 'canva': '✗', 'adobe': '✗', 'word': '✗'},
                {'feature': 'Hindi UI auto-suggestion', 'pagecraft': '✓ Smart', 'canva': '✗', 'adobe': '✗', 'word': '⚠ Manual'},
                {'feature': 'WhatsApp direct share', 'pagecraft': '✓ Free', 'canva': '⚠ Link only', 'adobe': '✗', 'word': '✗'},
                {'feature': 'UPI / Indian payment methods', 'pagecraft': '✓ All', 'canva': '⚠ Card only', 'adobe': '⚠ Card only', 'word': '✓'},
            ]
        },
        {
            'title': 'Editor & Workflow',
            'icon': '⚡',
            'rows': [
                {'feature': 'Live preview (desktop/tablet/mobile)', 'pagecraft': '✓ Free', 'canva': '✓', 'adobe': '✓', 'word': '⚠ Limited'},
                {'feature': 'Compare same content across N templates', 'pagecraft': '✓ Free Unique!', 'canva': '✗', 'adobe': '✗', 'word': '✗', 'highlight': True},
                {'feature': 'Similar templates sidebar (smart match)', 'pagecraft': '✓ Free', 'canva': '✗', 'adobe': '✗', 'word': '✗'},
                {'feature': 'Smart badges (NEW / HOT / INDIAN)', 'pagecraft': '✓ Free', 'canva': '⚠ Few', 'adobe': '✗', 'word': '✗'},
                {'feature': 'Auto-save (every keystroke)', 'pagecraft': '✓ Free', 'canva': '✓', 'adobe': '✓', 'word': '✓'},
                {'feature': 'Undo / Redo 50 steps', 'pagecraft': '✓ Free', 'canva': '✓', 'adobe': '✓', 'word': '✓'},
                {'feature': 'Command palette (Ctrl+K)', 'pagecraft': '✓ Free', 'canva': '✗', 'adobe': '✗', 'word': '✗'},
                {'feature': 'Dark mode', 'pagecraft': '✓ Free', 'canva': '✓', 'adobe': '⚠ Limited', 'word': '✓'},
            ]
        },
        {
            'title': 'Export & Sharing',
            'icon': '📥',
            'rows': [
                {'feature': 'PDF / PNG / JPG export', 'pagecraft': '✓ Free', 'canva': '⚠ PNG paid', 'adobe': '✓', 'word': 'PDF only'},
                {'feature': 'No watermark', 'pagecraft': '⭐ Pro · ₹149', 'canva': '⭐ Pro · ₹500', 'adobe': '⭐ Pro · ₹830', 'word': '✓'},
                {'feature': 'Animated GIF export', 'pagecraft': '⭐ Pro · ₹149', 'canva': '⭐ Pro · ₹500', 'adobe': '✗', 'word': '✗'},
                {'feature': 'Bulk export (ZIP)', 'pagecraft': '⭐ Pro · ₹149', 'canva': '⭐ Pro · ₹500', 'adobe': '⭐ Pro · ₹830', 'word': '✗'},
                {'feature': 'Public share links', 'pagecraft': '✓ Free', 'canva': '✓', 'adobe': '✓', 'word': '⚠ Limited'},
                {'feature': 'Email share', 'pagecraft': '✓ Free', 'canva': '⚠ Link', 'adobe': '⚠ Link', 'word': '✓'},
                {'feature': 'Print optimized', 'pagecraft': '✓ Free', 'canva': '✓', 'adobe': '✓', 'word': '✓'},
                {'feature': 'Commercial use license', 'pagecraft': '⭐ Pro included', 'canva': '⭐ Pro extra', 'adobe': '⭐ Pro extra', 'word': '⚠ Limited'},
            ]
        },
        {
            'title': 'Brand & Personalization',
            'icon': '🎨',
            'rows': [
                {'feature': 'Brand Kit (logo + colors + fonts)', 'pagecraft': '⭐ Pro · ₹149', 'canva': '⭐ Pro · ₹500', 'adobe': '⭐ Pro · ₹830', 'word': '✗', 'highlight': True},
                {'feature': 'Apply brand to any template', 'pagecraft': '⭐ 1-click', 'canva': '⭐ 1-click', 'adobe': '⭐ 1-click', 'word': '✗'},
                {'feature': 'Save unlimited brand presets', 'pagecraft': '⭐ Pro', 'canva': '⭐ Pro', 'adobe': '⭐ Pro', 'word': '✗'},
                {'feature': 'Multiple paper sizes (A4/A3/Letter)', 'pagecraft': '✓ Free', 'canva': '⚠ Some Pro', 'adobe': '✓', 'word': '✓'},
            ]
        },
        {
            'title': 'Discovery & SEO',
            'icon': '🔍',
            'rows': [
                {'feature': 'Per-template SEO landing pages', 'pagecraft': '✓ All', 'canva': '⚠ Some', 'adobe': '✗', 'word': '✗', 'highlight': True},
                {'feature': 'JSON-LD schema (Google rich snippets)', 'pagecraft': '✓', 'canva': '⚠ Some', 'adobe': '✗', 'word': '✗'},
                {'feature': 'Full sitemap.xml with priority', 'pagecraft': '✓', 'canva': '✓', 'adobe': '✓', 'word': '✗'},
                {'feature': 'Search by color, tag, language', 'pagecraft': '✓ Free', 'canva': '⚠ Color only', 'adobe': '⚠ Limited', 'word': '✗'},
                {'feature': 'Category FAQ schema', 'pagecraft': '✓', 'canva': '✗', 'adobe': '✗', 'word': '✗'},
            ]
        },
        {
            'title': 'Mobile & Account',
            'icon': '📱',
            'rows': [
                {'feature': 'PWA install (offline-capable)', 'pagecraft': '✓ Free', 'canva': '✓', 'adobe': '⚠ Limited', 'word': '✗'},
                {'feature': 'Native mobile sticky bar', 'pagecraft': '✓ Free', 'canva': '✓', 'adobe': '⚠ Limited', 'word': '⚠ Limited'},
                {'feature': 'My Documents library', 'pagecraft': '✓ Free', 'canva': '✓', 'adobe': '✓', 'word': '✓'},
                {'feature': 'Achievements / gamification', 'pagecraft': '✓ 8 badges', 'canva': '✗', 'adobe': '✗', 'word': '✗'},
                {'feature': 'Analytics dashboard', 'pagecraft': '✓ Free', 'canva': '⭐ Pro', 'adobe': '⭐ Pro', 'word': '✗'},
            ]
        },
    ]
    return render(request, 'pages/compare.html', {'groups': groups, 'total_templates': total})


# ---------- API: Templates ----------

class TemplateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    def get_queryset(self):
        from django.db.models import Q
        qs = super().get_queryset()
        cat = self.request.query_params.get('category')
        if cat:
            qs = qs.filter(category=cat)
        q = self.request.query_params.get('q') or self.request.query_params.get('search')
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(category__icontains=q) | Q(keywords__icontains=q))
        # Tag filter
        tag = self.request.query_params.get('tag')
        if tag:
            qs = qs.filter(tags__contains=[tag])
        # Color filter
        color = self.request.query_params.get('color')
        if color:
            qs = qs.filter(color_tags__contains=[color])
        # Random
        if self.request.query_params.get('random'):
            qs = qs.order_by('?')
        return qs

    @action(detail=True, methods=['post'])
    def render(self, request, pk=None):
        tpl = self.get_object()
        data = request.data.get('data') or tpl.sample_data or {}
        html = render_template_html(tpl, data)
        return Response({'html': html})


# ---------- API: Documents ----------

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = GeneratedDocument.objects.all()
    serializer_class = GeneratedDocumentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(user=self.request.user)
        return qs.none()

    def create(self, request, *args, **kwargs):
        # Login required to save documents
        if not request.user.is_authenticated:
            return Response({
                'error': 'login_required',
                'message': 'Please log in to save documents.',
                'login_url': '/login/',
            }, status=401)
        # Free tier limit: 5 saved documents max
        sub = get_user_plan(request.user)
        limit = sub.limit('saved_docs') if sub else 5
        if limit is not None:
            current = GeneratedDocument.objects.filter(user=request.user).count()
            if current >= limit:
                return Response({
                    'error': 'limit_reached',
                    'message': f'Free plan allows only {limit} saved documents. Upgrade to Pro for unlimited.',
                    'upgrade_url': '/pricing/',
                }, status=403)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        tpl = serializer.validated_data['template']
        data = serializer.validated_data.get('data', {})
        rendered = render_template_html(tpl, data)
        serializer.save(rendered_html=rendered, user=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.instance
        tpl = serializer.validated_data.get('template', instance.template)
        data = serializer.validated_data.get('data', instance.data)
        rendered = render_template_html(tpl, data)
        serializer.save(rendered_html=rendered)


# ---------- API: AI ----------

@api_view(['POST'])
def ai_enhance(request):
    if not _rate_limit(request, 'ai_enhance', max_calls=30, window_sec=60):
        return Response({'error': 'Too many requests. Slow down.', 'source': 'ratelimit'}, status=429)
    text = request.data.get('text', '')
    mode = request.data.get('mode', 'improve')
    context = request.data.get('context', {})
    return Response(enhance_text(text, mode=mode, context=context))


LANGUAGE_NAMES = {
    'en': 'English', 'hi': 'Hindi', 'es': 'Spanish', 'fr': 'French',
    'de': 'German', 'zh': 'Chinese (Simplified)', 'ar': 'Arabic',
    'ru': 'Russian', 'pt': 'Portuguese', 'ja': 'Japanese',
}

# ====================================================================
# USER AUTH
# ====================================================================

def signup_view(request):
    from .forms import EnhancedSignupForm
    from .emails import send_welcome_email
    from .models import get_or_create_profile
    if request.method == 'POST':
        form = EnhancedSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Auto-create Subscription (Starter)
            get_user_plan(user)
            # Fetch the profile and send welcome email (non-blocking, fail-silent)
            profile = get_or_create_profile(user)
            try:
                send_welcome_email(user, profile)
            except Exception:
                pass
            messages.success(request, f'Welcome to Pagecraft, {profile.display_name}!')
            return redirect('home')
    else:
        form = EnhancedSignupForm()
    return render(request, 'auth/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(request.GET.get('next', 'home'))
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def _require_pro(request, feature_name):
    """Helper: returns redirect response if user lacks pro feature, else None."""
    sub = get_user_plan(request.user)
    if sub and sub.has_feature(feature_name):
        return None
    messages.error(request, f'⭐ {feature_name.replace("_", " ").title()} is a Pro feature. Upgrade to unlock!')
    return redirect('pricing')


@login_required
def brand_kit_view(request):
    """Brand Kit page — upload logo, pick colors & fonts. PRO ONLY."""
    gate = _require_pro(request, 'brand_kit')
    if gate: return gate
    kit, _ = BrandKit.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        kit.brand_name = request.POST.get('brand_name', '').strip()
        kit.tagline = request.POST.get('tagline', '').strip()
        kit.primary_color = request.POST.get('primary_color', '#6366f1')
        kit.secondary_color = request.POST.get('secondary_color', '#a855f7')
        kit.accent_color = request.POST.get('accent_color', '#ec4899')
        kit.text_color = request.POST.get('text_color', '#0f172a')
        kit.background_color = request.POST.get('background_color', '#ffffff')
        kit.heading_font = request.POST.get('heading_font', 'Inter')
        kit.body_font = request.POST.get('body_font', 'Inter')
        kit.website = request.POST.get('website', '').strip()
        kit.email = request.POST.get('email', '').strip()
        kit.phone = request.POST.get('phone', '').strip()
        # Logo can be passed as base64 data URL via JS
        logo_data = request.POST.get('logo', '').strip()
        if logo_data:
            kit.logo = logo_data
        elif request.POST.get('clear_logo'):
            kit.logo = ''
        kit.save()
        messages.success(request, 'Brand kit saved!')
        return redirect('brand_kit')
    return render(request, 'brand_kit.html', {'kit': kit, 'fonts': BrandKit.FONT_CHOICES})


@api_view(['GET'])
def brand_kit_api(request):
    """Return current user's brand kit as JSON for the editor."""
    if not request.user.is_authenticated:
        return Response({'error': 'login_required'}, status=401)
    kit = BrandKit.objects.filter(user=request.user).first()
    if not kit:
        return Response({'has_kit': False})
    return Response({
        'has_kit': True,
        'brand_name': kit.brand_name,
        'tagline': kit.tagline,
        'logo': kit.logo,
        'primary_color': kit.primary_color,
        'secondary_color': kit.secondary_color,
        'accent_color': kit.accent_color,
        'text_color': kit.text_color,
        'background_color': kit.background_color,
        'heading_font': kit.heading_font,
        'body_font': kit.body_font,
        'website': kit.website,
        'email': kit.email,
        'phone': kit.phone,
    })


@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'profile':
            user.first_name = request.POST.get('first_name', '').strip()
            user.last_name = request.POST.get('last_name', '').strip()
            user.email = request.POST.get('email', '').strip()
            user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        elif action == 'password':
            old = request.POST.get('old_password', '')
            new = request.POST.get('new_password', '')
            new2 = request.POST.get('new_password2', '')
            if not user.check_password(old):
                messages.error(request, 'Current password is incorrect.')
            elif new != new2:
                messages.error(request, 'New passwords do not match.')
            elif len(new) < 6:
                messages.error(request, 'Password must be at least 6 characters.')
            else:
                user.set_password(new)
                user.save()
                login(request, user)
                messages.success(request, 'Password changed successfully!')
            return redirect('profile')
        elif action == 'delete':
            user.delete()
            messages.success(request, 'Account deleted.')
            return redirect('home')

    # ===== Comprehensive activity data =====
    from django.db.models import Count
    from datetime import datetime

    sub = get_user_plan(user)  # auto-creates Starter sub if missing
    has_brand_kit = BrandKit.objects.filter(user=user).exists()

    docs_qs = GeneratedDocument.objects.filter(user=user).select_related('template')
    doc_count = docs_qs.count()
    recent_docs = docs_qs.order_by('-updated_at')[:8]

    # Top category by usage
    top_cat_data = (docs_qs.values('template__category')
                    .annotate(n=Count('id')).order_by('-n').first())
    top_cat = None
    if top_cat_data:
        top_cat = {
            'key': top_cat_data['template__category'],
            'label': dict(Template.CATEGORY_CHOICES).get(top_cat_data['template__category'], top_cat_data['template__category']),
            'count': top_cat_data['n'],
        }

    # Days active since signup
    days_active = (datetime.now().date() - user.date_joined.date()).days if user.date_joined else 0

    # Plan limits & usage
    download_limit = sub.limit('downloads') if sub else 5
    download_used = sub.download_count if sub else 0
    download_pct = int((download_used / download_limit) * 100) if download_limit else 0

    saved_limit = sub.limit('saved_docs') if sub else 5
    saved_used = doc_count
    saved_pct = int((saved_used / saved_limit) * 100) if saved_limit else 0

    return render(request, 'auth/profile.html', {
        'user_obj': user,
        'subscription': sub,
        'has_brand_kit': has_brand_kit,
        'doc_count': doc_count,
        'recent_docs': recent_docs,
        'top_cat': top_cat,
        'days_active': days_active,
        'download_limit': download_limit,
        'download_used': download_used,
        'download_pct': min(download_pct, 100),
        'saved_limit': saved_limit,
        'saved_used': saved_used,
        'saved_pct': min(saved_pct, 100),
    })


# ====================================================================
# MOCK PAYMENT / CHECKOUT
# ====================================================================

PLANS = {
    'pro':      {'name': 'Pro',      'price': 149,  'desc': 'Unlimited everything · No watermark · Brand Kit · Priority AI'},
    'lifetime': {'name': 'Lifetime', 'price': 1999, 'desc': 'Pay once, use forever · All Pro features · Lifetime updates'},
    'business': {'name': 'Business', 'price': 499,  'desc': '5 team seats · API access · White-label · Webhooks'},
}

@login_required
def checkout_view(request, plan):
    plan_data = PLANS.get(plan)
    if not plan_data:
        return redirect('pricing')

    if request.method == 'POST':
        # Mock payment validation
        card = (request.POST.get('card_number') or '').replace(' ', '')
        cvv = request.POST.get('cvv') or ''
        name = request.POST.get('name') or ''
        if len(card) >= 13 and len(cvv) >= 3 and name:
            # Save subscription if logged in
            if request.user.is_authenticated:
                # Lifetime never expires; others expire after 30 days
                expires = None if plan == 'lifetime' else datetime.now() + timedelta(days=30)
                Subscription.objects.update_or_create(
                    user=request.user,
                    defaults={
                        'plan': plan,
                        'card_last4': card[-4:],
                        'expires_at': expires,
                    },
                )
            return render(request, 'checkout_success.html', {
                'plan': plan_data, 'plan_key': plan,
                'card_last4': card[-4:],
                'invoice_id': 'PC-' + secrets.token_hex(4).upper(),
            })
        return render(request, 'checkout.html', {
            'plan': plan_data, 'plan_key': plan,
            'error': 'Please fill all card details correctly (16-digit number, 3-digit CVV).',
        })

    return render(request, 'checkout.html', {'plan': plan_data, 'plan_key': plan})


# ====================================================================
# PUBLIC SHARE
# ====================================================================

def share_doc_view(request, token):
    doc = get_object_or_404(GeneratedDocument, share_token=token, is_public=True)
    return render(request, 'share.html', {'doc': doc})


@api_view(['POST'])
def make_doc_public(request, doc_id):
    doc = get_object_or_404(GeneratedDocument, pk=doc_id)
    if not doc.share_token:
        doc.share_token = secrets.token_urlsafe(16)
    doc.is_public = True
    doc.save()
    share_url = request.build_absolute_uri(f'/share/{doc.share_token}/')
    return Response({'share_url': share_url, 'token': doc.share_token})


# ====================================================================
# ANALYTICS DASHBOARD
# ====================================================================

@login_required
def analytics_view(request):
    from django.db.models import Count
    cat_counts = list(Template.objects.values('category').annotate(n=Count('id')).order_by('-n'))
    cat_labels = dict(Template.CATEGORY_CHOICES)
    for c in cat_counts:
        c['label'] = cat_labels.get(c['category'], c['category'])
    total_templates = Template.objects.count()
    total_docs = GeneratedDocument.objects.count()
    total_users = 0
    try:
        from django.contrib.auth.models import User
        total_users = User.objects.count()
    except Exception:
        pass
    recent_docs = GeneratedDocument.objects.order_by('-created_at')[:8]

    # Top template (most documents)
    top_templates = list(
        Template.objects.annotate(usage=Count('documents'))
        .filter(usage__gt=0).order_by('-usage')[:5]
    )

    return render(request, 'analytics.html', {
        'cat_counts': cat_counts,
        'total_templates': total_templates,
        'total_docs': total_docs,
        'total_users': total_users,
        'recent_docs': recent_docs,
        'top_templates': top_templates,
    })


# ====================================================================
# AI TEMPLATE GENERATOR
# ====================================================================

def ai_template_view(request):
    if request.user.is_authenticated:
        gate = _require_pro(request, 'ai_template')
        if gate: return gate
    return render(request, 'ai_template.html')


@api_view(['POST'])
def ai_generate_template(request):
    """Use Gemini to generate a complete HTML+CSS template from a prompt."""
    if not _rate_limit(request, 'ai_template', max_calls=5, window_sec=300):
        return Response({'error': 'rate_limit',
                         'message': 'Maximum 5 AI templates per 5 minutes.'}, status=429)
    prompt = (request.data.get('prompt') or '').strip()
    category = request.data.get('category', 'card')
    if not prompt:
        return Response({'error': 'Empty prompt'}, status=400)

    from .ai_service import _get_model
    model = _get_model()
    if not model:
        return Response({
            'error': 'Gemini API key not configured',
            'message': 'Add GEMINI_API_KEY to .env to use AI template generation.'
        }, status=500)

    full_prompt = f"""Generate a complete document template as JSON.

User wants: {prompt}
Category: {category}

Return ONLY valid JSON in this exact format (no markdown, no code fences, no preamble):
{{
  "title": "Short template title",
  "description": "One-line description",
  "html": "<div class=\\"my-tpl\\">...</div>",
  "css": ".my-tpl{{...}}",
  "fields": [{{"name": "field1", "label": "Field 1", "type": "text"}}],
  "sample": {{"field1": "Sample value"}}
}}

Rules:
- Use a unique CSS class prefix (e.g. .ai-tpl-X) so styles don't clash
- HTML uses Django-style {{{{ field_name }}}} placeholders
- Make it visually impressive: gradients, premium typography, generous spacing
- Use Google Fonts already loaded: Inter, Playfair Display, Cormorant Garamond
- 3-6 fields covering the essential content
- Include rich sample data that demonstrates the design
- Width should be around 560px for invitations, 780px for documents
"""

    try:
        resp = model.generate_content(full_prompt)
        text = (resp.text or '').strip()
        # Strip code fences if Gemini added them
        if text.startswith('```'):
            text = text.split('```')[1] if '```' in text[3:] else text[3:]
            if text.startswith('json'):
                text = text[4:]
            text = text.strip().rstrip('`').strip()
        data = json.loads(text)
        # Save as a custom template
        tpl = Template.objects.create(
            title='🤖 ' + (data.get('title') or 'AI Template'),
            category=category,
            description='AI generated · ' + (data.get('description') or prompt[:80]),
            html_layout=data.get('html', ''),
            css_layout=data.get('css', ''),
            fields_schema=data.get('fields', []),
            sample_data=data.get('sample', {}),
        )
        return Response({'success': True, 'template_id': tpl.id, 'title': tpl.title})
    except Exception as exc:
        return Response({'error': 'generation_failed', 'message': str(exc)}, status=500)


# ====================================================================
# BULK EXPORT
# ====================================================================

@login_required
def bulk_export_view(request):
    gate = _require_pro(request, 'bulk_export')
    if gate: return gate
    docs = GeneratedDocument.objects.filter(user=request.user)[:50]
    return render(request, 'bulk_export.html', {'documents': docs})


# ====================================================================
# AI ENDPOINTS (existing)
# ====================================================================

@api_view(['POST'])
def check_download(request):
    """Called by editor BEFORE downloading. Enforces login + plan limits.
    Increments download_count on success."""
    if not request.user.is_authenticated:
        return Response({
            'allowed': False,
            'reason': 'login_required',
            'message': 'Please log in to download.',
            'login_url': '/login/?next=' + request.META.get('HTTP_REFERER', '/'),
        }, status=401)

    sub = get_user_plan(request.user)
    fmt = request.data.get('format', 'pdf')  # pdf / png / jpg / gif

    # GIF export is Pro+ only
    if fmt == 'gif' and not sub.has_feature('gif_export'):
        return Response({
            'allowed': False,
            'reason': 'pro_required',
            'feature': 'GIF export',
            'message': '🎬 Animated GIF export is a Pro feature. Upgrade to unlock!',
            'upgrade_url': '/pricing/',
        }, status=403)

    # Free tier download limit
    if not sub.can_download():
        return Response({
            'allowed': False,
            'reason': 'limit_reached',
            'plan': sub.plan,
            'limit': sub.limit('downloads'),
            'used': sub.download_count,
            'message': f'Free plan limit reached ({sub.limit("downloads")} downloads). Upgrade to Pro for unlimited downloads.',
            'upgrade_url': '/pricing/',
        }, status=403)

    # OK — increment counter
    sub.download_count += 1
    sub.save(update_fields=['download_count'])

    return Response({
        'allowed': True,
        'plan': sub.plan,
        'used': sub.download_count,
        'remaining': sub.downloads_remaining(),
        'unlimited': sub.downloads_remaining() is None,
    })


@api_view(['POST'])
def ai_image(request):
    """Generate an image with Gemini 2.5 Flash Image (Nano Banana)."""
    if not _rate_limit(request, 'ai_image', max_calls=10, window_sec=60):
        return Response({'error': 'rate_limit',
                         'message': 'Too many image requests. Please wait 60 seconds.',
                         'retry_after': 60}, status=429)
    prompt = (request.data.get('prompt') or '').strip()
    style = request.data.get('style', '')
    if not prompt:
        return Response({'error': 'Empty prompt'}, status=400)
    result = generate_image(prompt, style=style)
    return Response(result)


@api_view(['POST'])
def ai_translate(request):
    """Translate a data dict into target language using Gemini."""
    data = request.data.get('data', {})
    lang_code = request.data.get('language', 'en')
    language = LANGUAGE_NAMES.get(lang_code, lang_code)
    translated = translate_dict(data, language)
    return Response({'data': translated, 'language': language})


# ---------- Helpers ----------

def render_template_html(tpl: Template, data: dict, use_cache: bool = False) -> str:
    """Render the stored html_layout with given context, wrapping with the template CSS.

    If use_cache=True (for sample/preview rendering), result is cached for 1 hour
    keyed by template id + sample_data hash.
    """
    if use_cache:
        from django.core.cache import cache
        import hashlib
        key = f'tpl_render_{tpl.id}_{hashlib.md5(repr(data).encode()).hexdigest()}'
        cached = cache.get(key)
        if cached is not None:
            return cached
    try:
        django_tpl = DjangoTemplate(tpl.html_layout)
        body = django_tpl.render(Context(data))
    except Exception as exc:
        body = f"<p style='color:red;'>Render error: {exc}</p>"
    result = f"<style>{tpl.css_layout}</style>{body}"
    if use_cache:
        from django.core.cache import cache
        cache.set(key, result, 3600)
    return result
