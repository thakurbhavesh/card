"""Auto-populate SEO + discovery fields for every Template.

Computes:
- slug (URL-friendly from title)
- meta_title, meta_description, keywords
- tags (badges): new, hot, premium, animated, indian, editor_pick, free
- color_tags (dominant CSS colors)
- sub_category (hindu/muslim/diwali/holi/...)
- style_tags (modern/vintage/minimal/bold/...)
- is_premium, is_animated, is_featured

Idempotent — safe to run anytime. Heavy work happens once and is cached in DB,
so runtime queries stay fast.
"""
import re
from datetime import timedelta
from collections import Counter
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.text import slugify
from generator.models import Template


# Map common color names + hex prefixes → tag color
COLOR_NAME_MAP = {
    'red': '#dc2626', 'pink': '#ec4899', 'rose': '#f43f5e',
    'orange': '#f97316', 'amber': '#f59e0b', 'yellow': '#fbbf24',
    'green': '#10b981', 'emerald': '#10b981', 'teal': '#14b8a6',
    'cyan': '#06b6d4', 'sky': '#0ea5e9', 'blue': '#3b82f6',
    'indigo': '#6366f1', 'violet': '#8b5cf6', 'purple': '#a855f7',
    'fuchsia': '#d946ef', 'gold': '#d4af37', 'maroon': '#7f1d1d',
    'navy': '#1e3a8a', 'black': '#0a0a0a', 'white': '#fafafa',
    'cream': '#fef9c3', 'gray': '#737373', 'silver': '#cbd5e1',
    'brown': '#78350f', 'burgundy': '#7f1d1d',
}


def hex_to_color_name(hex_code):
    """Map a hex color to nearest named color (8 buckets)."""
    if not hex_code or len(hex_code) < 4:
        return None
    h = hex_code.lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    if len(h) != 6:
        return None
    try:
        r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    except ValueError:
        return None
    # Bucket by HSL/dominant channel
    mx, mn = max(r, g, b), min(r, g, b)
    light = (mx + mn) / 2
    if mx - mn < 25:
        if light < 60: return 'black'
        if light > 220: return 'white'
        return 'gray'
    if r > 200 and g < 100 and b < 100: return 'red'
    if r > 200 and g > 100 and b > 150 and b < 220: return 'pink'
    if r > 200 and g > 130 and b < 100: return 'orange'
    if r > 200 and g > 180 and b < 100: return 'gold'
    if r > 200 and g > 200 and b < 150: return 'yellow'
    if g > 180 and r < 150 and b < 150: return 'green'
    if g > 150 and b > 150 and r < 100: return 'teal'
    if b > 200 and r < 130: return 'blue'
    if r > 150 and b > 200 and g < 130: return 'purple'
    if r > 100 and g < 80 and b < 80: return 'maroon'
    if light < 80 and (r > b or g > b): return 'brown'
    return None


def extract_colors(css):
    """Get top 3 dominant color names from CSS hex codes."""
    if not css:
        return []
    hex_codes = re.findall(r'#[0-9a-fA-F]{3,8}\b', css)
    name_codes = re.findall(r'\b(red|pink|orange|yellow|green|teal|cyan|blue|indigo|purple|gold|maroon|navy|black|white|brown|burgundy)\b', css.lower())
    counter = Counter()
    for h in hex_codes:
        name = hex_to_color_name(h)
        if name:
            counter[name] += 1
    for n in name_codes:
        counter[n] += 1
    return [c for c, _ in counter.most_common(3)]


# Sub-category detection by title keywords
SUBCAT_RULES = [
    # weddings
    ('hindu', ['hindu', 'mandap', 'lotus', 'ganesh', 'om', 'maroon', 'sangeet', 'haldi', 'mehendi']),
    ('muslim', ['muslim', 'nikah', 'islamic', 'pakistani', 'bismillah', 'crescent', 'eid']),
    ('christian', ['christian', 'church', 'cross', 'baptism']),
    ('sikh', ['sikh', 'anand karaj', 'khanda', 'punjabi', 'gurdwara']),
    ('tamil', ['tamil', 'south indian', 'kerala']),
    ('telugu', ['telugu', 'andhra']),
    ('marathi', ['marathi', 'maharashtra']),
    ('bengali', ['bengali', 'kolkata']),
    ('gujarati', ['gujarati', 'gujarat']),
    # festivals
    ('diwali', ['diwali', 'deepavali', 'diya']),
    ('holi', ['holi']),
    ('navratri', ['navratri', 'garba']),
    ('eid', ['eid', 'ramadan']),
    ('christmas', ['christmas', 'xmas']),
    ('lohri', ['lohri']),
    ('pongal', ['pongal']),
    ('onam', ['onam']),
    ('janmashtami', ['janmashtami', 'krishna']),
    ('ganesh', ['ganesh chaturthi', 'ganpati']),
    ('raksha', ['raksha bandhan', 'rakhi']),
    ('karva', ['karva chauth']),
]


def detect_sub_category(title, desc):
    text = f"{title} {desc}".lower()
    for sub, kws in SUBCAT_RULES:
        if any(k in text for k in kws):
            return sub
    return ''


# Style detection
STYLE_RULES = [
    ('minimal', ['minimal', 'minimalist', 'clean', 'simple', 'modern']),
    ('vintage', ['vintage', 'classic', 'retro', 'old', 'antique']),
    ('elegant', ['elegant', 'royal', 'luxury', 'premium', 'gold']),
    ('bold', ['bold', 'big', 'massive', 'mega', 'striking']),
    ('playful', ['fun', 'kids', 'playful', 'cute', 'cartoon', 'rainbow']),
    ('dark', ['dark', 'black', 'neon', 'cyberpunk', 'midnight']),
    ('floral', ['floral', 'flower', 'rose', 'botanical', 'leaf']),
    ('geometric', ['geometric', 'shapes', 'block', 'grid']),
]


def detect_styles(title, desc):
    text = f"{title} {desc}".lower()
    found = []
    for style, kws in STYLE_RULES:
        if any(k in text for k in kws):
            found.append(style)
    return found[:3]


# Tag detection
INDIAN_KEYWORDS = ['hindu', 'muslim', 'sikh', 'christian', 'tamil', 'telugu', 'marathi',
                   'bengali', 'gujarati', 'punjabi', 'diwali', 'holi', 'eid', 'navratri',
                   'lohri', 'pongal', 'onam', 'karva', 'raksha', 'ganesh', 'janmashtami',
                   'krishna', 'mandap', 'sangeet', 'haldi', 'mehendi', 'baraat', 'rangoli',
                   'indian', 'india', 'maa', 'bhai', 'didi']


def is_indian(title, desc):
    text = f"{title} {desc}".lower()
    return any(k in text for k in INDIAN_KEYWORDS)


def is_animated_template(title, css):
    if '🎬' in title or 'animated' in title.lower():
        return True
    if css and ('@keyframes' in css or 'animation:' in css):
        return True
    return False


def is_premium_template(title, desc):
    if '✦' in title or '💎' in title or '⭐' in title:
        return True
    if 'premium' in desc.lower() or 'ultra' in desc.lower() or 'luxury' in desc.lower():
        return True
    return False


# SEO templates
META_TITLE_FMT = "{title} — Free {category} Template | Pagecraft"
META_DESC_FMT = "{desc} Edit online for free, no signup needed. Download as PDF, PNG or JPG. {extra}"

CATEGORY_KEYWORDS = {
    'resume': 'resume template, cv template, free resume, professional resume, job resume',
    'cover_letter': 'cover letter template, free cover letter, job application letter',
    'invoice': 'invoice template, free invoice, billing template, gst invoice',
    'voucher': 'gift voucher template, gift card template, coupon template',
    'card': 'business card template, visiting card, free visiting card',
    'certificate': 'certificate template, achievement certificate, award certificate',
    'social': 'social media template, instagram post, facebook post, free social',
    'flyer': 'flyer template, poster template, free flyer, event poster',
    'wedding': 'wedding invitation, wedding card, indian wedding card, free wedding invite',
    'birthday': 'birthday invitation, birthday card, kids birthday',
    'festival': 'festival card, greeting card, diwali card, holi card',
    'menu': 'restaurant menu template, food menu, cafe menu',
    'ticket': 'event ticket template, concert ticket, conference badge',
}


def build_seo(t, badges, sub_cat, colors, styles):
    """Compute meta_title, meta_description, keywords for one template."""
    cat = t.get_category_display()
    title = re.sub(r'^[🎨🎬✦💎⭐🪔☪✝☬🛕🌿🌼🐎✨]+\s*', '', t.title).strip()
    extras = []
    if 'indian' in badges: extras.append("Perfect for Indian audiences.")
    if 'animated' in badges: extras.append("Animated GIF export available.")
    if sub_cat: extras.append(f"Style: {sub_cat.title()}.")
    extra = ' '.join(extras)

    meta_title = META_TITLE_FMT.format(title=title, category=cat)[:180]
    meta_desc = META_DESC_FMT.format(desc=(t.description or title)[:160], extra=extra)[:320]
    kw_parts = [title.lower(), cat.lower(), CATEGORY_KEYWORDS.get(t.category, '')]
    kw_parts += badges + colors + styles
    if sub_cat: kw_parts.append(sub_cat)
    keywords = ', '.join(filter(None, dict.fromkeys(kw_parts)))[:400]
    return meta_title, meta_desc, keywords


class Command(BaseCommand):
    help = "Populate SEO + discovery fields for all templates."

    def add_arguments(self, parser):
        parser.add_argument('--force', action='store_true', help='Recompute even if fields exist')

    def handle(self, *args, **options):
        force = options.get('force', False)
        recent_cutoff = timezone.now() - timedelta(days=14)
        all_tpl = Template.objects.all()
        total = all_tpl.count()
        self.stdout.write(f"Processing {total} templates...")

        # Used for "hot" badge — top 5% by download count
        download_threshold = 0
        downloads = list(Template.objects.values_list('download_count', flat=True).order_by('-download_count'))
        if downloads:
            download_threshold = downloads[max(0, total // 20)]

        # Used for "trending" — top viewed
        views = list(Template.objects.values_list('view_count', flat=True).order_by('-view_count'))
        view_threshold = views[max(0, total // 10)] if views else 0

        updated = 0
        bulk = []
        for t in all_tpl.iterator():
            # Skip if already has SEO data and not --force
            if not force and t.meta_title and t.slug:
                continue

            # Slug — unique by appending id if collision
            base_slug = slugify(re.sub(r'[^\w\s-]', '', t.title))[:140] or f"template-{t.id}"
            slug = f"{base_slug}-{t.id}"

            # Detect badges/tags
            badges = []
            if t.created_at and t.created_at >= recent_cutoff:
                badges.append('new')
            if t.download_count >= download_threshold and t.download_count > 0:
                badges.append('hot')
            if t.view_count >= view_threshold and t.view_count > 0:
                badges.append('trending')

            animated = is_animated_template(t.title, t.css_layout)
            if animated: badges.append('animated')

            premium = is_premium_template(t.title, t.description)
            if premium:
                badges.append('premium')
            else:
                badges.append('free')

            indian = is_indian(t.title, t.description)
            if indian: badges.append('indian')

            sub_cat = detect_sub_category(t.title, t.description)
            colors = extract_colors(t.css_layout)
            styles = detect_styles(t.title, t.description)

            meta_title, meta_desc, keywords = build_seo(t, badges, sub_cat, colors, styles)

            t.slug = slug
            t.meta_title = meta_title
            t.meta_description = meta_desc
            t.keywords = keywords
            t.tags = badges
            t.color_tags = colors
            t.sub_category = sub_cat
            t.style_tags = styles
            t.is_premium = premium
            t.is_animated = animated
            t.is_featured = 'editor_pick' in badges or t.is_featured
            bulk.append(t)
            updated += 1

            if len(bulk) >= 100:
                Template.objects.bulk_update(bulk, [
                    'slug', 'meta_title', 'meta_description', 'keywords',
                    'tags', 'color_tags', 'sub_category', 'style_tags',
                    'is_premium', 'is_animated', 'is_featured',
                ])
                bulk = []

        if bulk:
            Template.objects.bulk_update(bulk, [
                'slug', 'meta_title', 'meta_description', 'keywords',
                'tags', 'color_tags', 'sub_category', 'style_tags',
                'is_premium', 'is_animated', 'is_featured',
            ])

        self.stdout.write(self.style.SUCCESS(f"Updated SEO data for {updated} templates."))

        # Show counts by tag
        from collections import Counter
        all_tags = Counter()
        for tags in Template.objects.values_list('tags', flat=True):
            for tag in (tags or []):
                all_tags[tag] += 1
        self.stdout.write("\nTag distribution:")
        for tag, count in all_tags.most_common():
            self.stdout.write(f"  {tag:12} {count}")

        all_colors = Counter()
        for colors in Template.objects.values_list('color_tags', flat=True):
            for c in (colors or []):
                all_colors[c] += 1
        self.stdout.write("\nColor distribution:")
        for c, n in all_colors.most_common(10):
            self.stdout.write(f"  {c:12} {n}")
