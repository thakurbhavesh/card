from django.db import models


class Template(models.Model):
    CATEGORY_CHOICES = [
        ('resume', 'Resume'),
        ('invoice', 'Invoice'),
        ('card', 'Visiting Card'),
        ('social', 'Social Media Post'),
        ('wedding', 'Wedding Invitation'),
        ('certificate', 'Certificate'),
        ('cover_letter', 'Cover Letter'),
        ('birthday', 'Birthday Invitation'),
        ('festival', 'Festival Card'),
        ('flyer', 'Flyer / Poster'),
        ('menu', 'Menu Card'),
        ('ticket', 'Event Ticket'),
        ('voucher', 'Gift Voucher'),
    ]

    title = models.CharField(max_length=120, db_index=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, db_index=True)
    description = models.TextField(blank=True)
    html_layout = models.TextField(help_text="Django template HTML with {{ variables }}")
    css_layout = models.TextField(blank=True)
    preview_image = models.ImageField(upload_to='previews/', blank=True, null=True)
    sample_data = models.JSONField(default=dict, help_text="Demo data for example mode")
    fields_schema = models.JSONField(default=list, help_text="List of {name,label,type} for dynamic forms")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # ========== SEO + DISCOVERY ==========
    slug = models.SlugField(max_length=160, blank=True, db_index=True)
    meta_title = models.CharField(max_length=180, blank=True)
    meta_description = models.CharField(max_length=320, blank=True)
    keywords = models.CharField(max_length=400, blank=True, help_text="Comma-separated SEO keywords")
    tags = models.JSONField(default=list, blank=True, help_text="badges: new, hot, trending, animated, indian, premium, free, editor_pick")
    color_tags = models.JSONField(default=list, blank=True, help_text="dominant colors detected from CSS")
    sub_category = models.CharField(max_length=40, blank=True, db_index=True, help_text="hindu, muslim, diwali, holi, etc.")
    language_tags = models.JSONField(default=list, blank=True)
    style_tags = models.JSONField(default=list, blank=True, help_text="modern, vintage, minimal, bold, elegant, etc.")
    view_count = models.PositiveIntegerField(default=0, db_index=True)
    download_count = models.PositiveIntegerField(default=0, db_index=True)
    is_premium = models.BooleanField(default=False, db_index=True)
    is_animated = models.BooleanField(default=False, db_index=True)
    is_featured = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ['category', 'title']
        indexes = [
            models.Index(fields=['category', 'is_featured']),
            models.Index(fields=['category', '-download_count']),
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return f"{self.get_category_display()} — {self.title}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('editor', args=[self.id])

    def has_tag(self, tag):
        return tag in (self.tags or [])


class GeneratedDocument(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE, related_name='documents')
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='documents')
    title = models.CharField(max_length=200, blank=True)
    data = models.JSONField(default=dict)
    rendered_html = models.TextField(blank=True)
    share_token = models.CharField(max_length=32, blank=True, db_index=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.title or f"Document #{self.pk}"


class BrandKit(models.Model):
    """One brand kit per user — stores logo, colors, fonts.
    Used by 'Apply Brand' to instantly skin any template."""
    FONT_CHOICES = [
        ('Inter', 'Inter (Modern Sans)'),
        ('Playfair Display', 'Playfair Display (Elegant Serif)'),
        ('Cormorant Garamond', 'Cormorant Garamond (Classic Serif)'),
        ('Poppins', 'Poppins (Friendly Sans)'),
        ('Montserrat', 'Montserrat (Bold Sans)'),
        ('Roboto', 'Roboto (Clean Sans)'),
        ('Lora', 'Lora (Editorial Serif)'),
        ('Oswald', 'Oswald (Strong Display)'),
    ]
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='brand_kit')
    brand_name = models.CharField(max_length=100, blank=True)
    tagline = models.CharField(max_length=200, blank=True)
    logo = models.TextField(blank=True, help_text="Base64 data URL of logo image")
    primary_color = models.CharField(max_length=20, default='#6366f1')
    secondary_color = models.CharField(max_length=20, default='#a855f7')
    accent_color = models.CharField(max_length=20, default='#ec4899')
    text_color = models.CharField(max_length=20, default='#0f172a')
    background_color = models.CharField(max_length=20, default='#ffffff')
    heading_font = models.CharField(max_length=60, choices=FONT_CHOICES, default='Inter')
    body_font = models.CharField(max_length=60, choices=FONT_CHOICES, default='Inter')
    website = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s brand kit"


class Subscription(models.Model):
    PLAN_CHOICES = [
        ('starter', 'Starter'),
        ('pro', 'Pro'),
        ('lifetime', 'Lifetime'),
        ('business', 'Business'),
    ]
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='subscription')
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES, default='starter')
    card_last4 = models.CharField(max_length=4, blank=True)
    download_count = models.PositiveIntegerField(default=0)
    ai_call_count = models.PositiveIntegerField(default=0)
    activated_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    # Plan limits — used by views to enforce gates.
    # Strategy: very generous free tier (more than Canva's free), Pro adds power features,
    # Lifetime is one-time payment (huge differentiator vs subscription tools).
    PLAN_LIMITS = {
        'starter':  {
            'downloads': None,           # unlimited downloads (with watermark)
            'saved_docs': 20,            # 20 saved drafts
            'ai_per_day': 30,            # 30 AI calls/day
            'features': set(),
        },
        'pro':      {
            'downloads': None,
            'saved_docs': None,          # unlimited
            'ai_per_day': None,          # unlimited
            'features': {'brand_kit', 'ai_template', 'gif_export', 'bulk_export', 'no_watermark', 'priority_ai', 'commercial_use'},
        },
        'lifetime': {
            'downloads': None,
            'saved_docs': None,
            'ai_per_day': None,
            'features': {'brand_kit', 'ai_template', 'gif_export', 'bulk_export', 'no_watermark', 'priority_ai', 'commercial_use', 'lifetime'},
        },
        'business': {
            'downloads': None,
            'saved_docs': None,
            'ai_per_day': None,
            'features': {'brand_kit', 'ai_template', 'gif_export', 'bulk_export', 'no_watermark', 'priority_ai', 'commercial_use', 'team', 'api', 'webhooks', 'white_label'},
        },
    }

    def limit(self, key):
        return self.PLAN_LIMITS.get(self.plan, {}).get(key)

    def has_feature(self, name):
        return name in self.PLAN_LIMITS.get(self.plan, {}).get('features', set())

    def can_download(self):
        limit = self.limit('downloads')
        return limit is None or self.download_count < limit

    def downloads_remaining(self):
        limit = self.limit('downloads')
        if limit is None:
            return None  # unlimited
        return max(0, limit - self.download_count)

    def __str__(self):
        return f"{self.user.username} — {self.get_plan_display()}"


def get_user_plan(user):
    """Helper: returns Subscription for any auth user, creating Starter if missing."""
    if not user or not user.is_authenticated:
        return None
    sub, _ = Subscription.objects.get_or_create(user=user, defaults={'plan': 'starter'})
    return sub


class UserProfile(models.Model):
    """Extended user profile — captured at signup for personalization & marketing."""
    USE_CASE_CHOICES = [
        ('personal',  'Personal use'),
        ('freelance', 'Freelancer / solo'),
        ('business',  'Business / startup'),
        ('agency',    'Agency / studio'),
        ('student',   'Student'),
        ('teacher',   'Teacher / educator'),
        ('ngo',       'NGO / non-profit'),
        ('other',     'Other'),
    ]
    PROFESSION_CHOICES = [
        ('designer',     'Designer'),
        ('developer',    'Developer'),
        ('marketer',     'Marketer'),
        ('entrepreneur', 'Entrepreneur'),
        ('manager',      'Manager'),
        ('hr',           'HR / Recruiter'),
        ('teacher',      'Teacher'),
        ('student',      'Student'),
        ('other',        'Other'),
    ]
    LANGUAGE_CHOICES = [
        ('en', 'English'), ('hi', 'हिन्दी'), ('es', 'Español'), ('fr', 'Français'),
        ('de', 'Deutsch'), ('zh', '中文'), ('ar', 'العربية'), ('ru', 'Русский'),
        ('pt', 'Português'), ('ja', '日本語'),
    ]
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=80, blank=True, default='India')
    city = models.CharField(max_length=80, blank=True)
    profession = models.CharField(max_length=20, choices=PROFESSION_CHOICES, blank=True)
    use_case = models.CharField(max_length=20, choices=USE_CASE_CHOICES, blank=True)
    company = models.CharField(max_length=120, blank=True)
    website = models.CharField(max_length=200, blank=True)
    preferred_language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, default='en')
    referral_source = models.CharField(max_length=80, blank=True, help_text="How did they hear about us?")
    newsletter_opt_in = models.BooleanField(default=True)
    marketing_opt_in = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=64, blank=True)
    avatar_url = models.CharField(max_length=400, blank=True)
    bio = models.TextField(blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} profile"

    @property
    def display_name(self):
        return self.full_name or self.user.get_full_name() or self.user.username


def get_or_create_profile(user):
    """Helper to fetch/create UserProfile for any user."""
    if not user or not user.is_authenticated:
        return None
    profile, _ = UserProfile.objects.get_or_create(user=user)
    return profile
