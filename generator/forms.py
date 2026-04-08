"""Custom forms for Pagecraft — enhanced signup with full profile fields."""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile


COUNTRY_CHOICES = [
    ('India', 'India'), ('United States', 'United States'), ('United Kingdom', 'United Kingdom'),
    ('Canada', 'Canada'), ('Australia', 'Australia'), ('Singapore', 'Singapore'),
    ('UAE', 'UAE'), ('Germany', 'Germany'), ('France', 'France'), ('Other', 'Other'),
]

REFERRAL_CHOICES = [
    ('', 'Select an option'),
    ('google', 'Google search'),
    ('social', 'Social media (Instagram/Twitter/LinkedIn)'),
    ('youtube', 'YouTube'),
    ('friend', 'Friend / colleague'),
    ('blog', 'Blog / article'),
    ('ad', 'Advertisement'),
    ('other', 'Other'),
]


class EnhancedSignupForm(UserCreationForm):
    """Signup form with full profile fields. Validates email uniqueness too."""
    full_name = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Aarav Sharma',
            'autocomplete': 'name',
        }),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'you@example.com',
            'autocomplete': 'email',
        }),
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '+91 98765 43210',
            'autocomplete': 'tel',
        }),
    )
    country = forms.ChoiceField(
        choices=COUNTRY_CHOICES,
        initial='India',
        required=False,
    )
    city = forms.CharField(
        max_length=80,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Bangalore'}),
    )
    profession = forms.ChoiceField(
        choices=[('', 'Select...')] + UserProfile.PROFESSION_CHOICES,
        required=False,
    )
    use_case = forms.ChoiceField(
        choices=[('', 'Select...')] + UserProfile.USE_CASE_CHOICES,
        required=False,
        label="What will you use Pagecraft for?",
    )
    referral_source = forms.ChoiceField(
        choices=REFERRAL_CHOICES,
        required=False,
        label="How did you hear about us?",
    )
    newsletter_opt_in = forms.BooleanField(
        required=False,
        initial=True,
        label="Send me product updates and tips",
    )
    marketing_opt_in = forms.BooleanField(
        required=False,
        initial=False,
        label="I'd like to receive special offers and promotions",
    )
    terms_accept = forms.BooleanField(
        required=True,
        label="I agree to the Terms of Service and Privacy Policy",
        error_messages={'required': 'You must accept the Terms to create an account.'},
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Friendlier placeholders
        self.fields['username'].widget.attrs.update({
            'placeholder': 'aarav.sharma',
            'autocomplete': 'username',
        })
        self.fields['username'].help_text = 'Letters, digits and @/./+/-/_ only.'
        self.fields['password1'].widget.attrs.update({
            'placeholder': '••••••••',
            'autocomplete': 'new-password',
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': '••••••••',
            'autocomplete': 'new-password',
        })

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if email and User.objects.filter(email__iexact=email).exists():
            raise ValidationError("An account with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        # Split full name into first/last for User model compatibility
        full = self.cleaned_data.get('full_name', '').strip()
        if full:
            parts = full.split(' ', 1)
            user.first_name = parts[0]
            user.last_name = parts[1] if len(parts) > 1 else ''
        if commit:
            user.save()
            # Create extended profile
            import secrets
            UserProfile.objects.update_or_create(
                user=user,
                defaults={
                    'full_name': full,
                    'phone': self.cleaned_data.get('phone', ''),
                    'country': self.cleaned_data.get('country', '') or 'India',
                    'city': self.cleaned_data.get('city', ''),
                    'profession': self.cleaned_data.get('profession', ''),
                    'use_case': self.cleaned_data.get('use_case', ''),
                    'referral_source': self.cleaned_data.get('referral_source', ''),
                    'newsletter_opt_in': self.cleaned_data.get('newsletter_opt_in', True),
                    'marketing_opt_in': self.cleaned_data.get('marketing_opt_in', False),
                    'verification_token': secrets.token_urlsafe(32),
                },
            )
        return user
