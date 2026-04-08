"""Email helpers for Pagecraft.

All emails route through Django's send_mail using the EMAIL_BACKEND configured
in settings (console for dev, SMTP for production via .env).
"""
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import logging

logger = logging.getLogger(__name__)


def _send(subject, html_body, to_email, text_body=None, fail_silently=True):
    """Internal helper that sends both HTML and plain text versions."""
    if not to_email:
        return False
    if not text_body:
        text_body = strip_tags(html_body)
    try:
        msg = EmailMultiAlternatives(
            subject=subject,
            body=text_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[to_email],
            reply_to=[settings.SUPPORT_EMAIL],
        )
        msg.attach_alternative(html_body, 'text/html')
        msg.send(fail_silently=fail_silently)
        return True
    except Exception as e:
        logger.error(f"Email send failed to {to_email}: {e}")
        if not fail_silently:
            raise
        return False


def send_welcome_email(user, profile=None):
    """Send a welcome email after signup."""
    name = (profile.full_name if profile else user.first_name) or user.username
    site_url = getattr(settings, 'SITE_URL', 'http://127.0.0.1:8000')
    html = f"""\
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Welcome to Pagecraft</title></head>
<body style="margin:0;padding:0;background:#f8fafc;font-family:-apple-system,Segoe UI,Roboto,sans-serif;color:#0f172a">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr><td align="center" style="padding:40px 20px">
      <table role="presentation" width="560" cellpadding="0" cellspacing="0" border="0" style="max-width:560px;background:#fff;border:1px solid #e5e9f2;border-radius:14px;overflow:hidden">
        <!-- Header with blue gradient -->
        <tr><td style="background:linear-gradient(135deg,#0052FF 0%,#001A66 100%);padding:40px;text-align:center;color:#fff">
          <div style="font-family:Georgia,serif;font-style:italic;font-size:32px;font-weight:700;letter-spacing:-0.5px">✦ Pagecraft</div>
          <div style="font-size:13px;letter-spacing:.15em;text-transform:uppercase;opacity:.85;margin-top:6px">Welcome aboard</div>
        </td></tr>
        <!-- Body -->
        <tr><td style="padding:40px">
          <h1 style="margin:0 0 14px;font-size:28px;letter-spacing:-0.5px">Hey {name}, welcome! 👋</h1>
          <p style="margin:0 0 20px;font-size:16px;line-height:1.6;color:#475569">
            You just joined <strong style="color:#0052FF">2,000+ creators</strong> using Pagecraft to design beautiful resumes,
            invoices, wedding invites, certificates and more — powered by AI.
          </p>
          <!-- Quick links -->
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:24px 0">
            <tr><td style="padding:14px;background:#f0f5ff;border-left:4px solid #0052FF;border-radius:8px">
              <div style="font-weight:700;font-size:14px;margin-bottom:4px">📚 496+ premium templates</div>
              <div style="font-size:13px;color:#475569">All free. Hand-crafted. Indian wedding/festival included.</div>
            </td></tr>
            <tr><td style="height:8px"></td></tr>
            <tr><td style="padding:14px;background:#f0f5ff;border-left:4px solid #0052FF;border-radius:8px">
              <div style="font-weight:700;font-size:14px;margin-bottom:4px">🤖 AI text + image generation</div>
              <div style="font-size:13px;color:#475569">Let Gemini write your bullet points, translate to 10 languages.</div>
            </td></tr>
            <tr><td style="height:8px"></td></tr>
            <tr><td style="padding:14px;background:#f0f5ff;border-left:4px solid #0052FF;border-radius:8px">
              <div style="font-weight:700;font-size:14px;margin-bottom:4px">📥 Export to PDF, PNG, JPG, GIF</div>
              <div style="font-size:13px;color:#475569">One click. No watermark with Pro.</div>
            </td></tr>
          </table>
          <!-- CTA button -->
          <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:30px auto"><tr>
            <td style="background:#0052FF;border-radius:10px;box-shadow:0 4px 12px rgba(0,82,255,.3)">
              <a href="{site_url}/" style="display:inline-block;padding:14px 32px;color:#fff;text-decoration:none;font-weight:700;font-size:15px">Start Creating →</a>
            </td>
          </tr></table>
          <p style="margin:24px 0 0;font-size:13px;color:#94a3b8;text-align:center">
            Need help? Reply to this email or visit our <a href="{site_url}/faq/" style="color:#0052FF">FAQ</a>.
          </p>
        </td></tr>
        <!-- Footer -->
        <tr><td style="background:#fafbff;padding:20px;text-align:center;border-top:1px solid #e5e9f2">
          <div style="font-size:11px;color:#94a3b8;letter-spacing:.05em">
            ✦ Pagecraft · Built with care in India 🇮🇳<br>
            <a href="{site_url}/profile/" style="color:#94a3b8;text-decoration:none">Manage preferences</a> ·
            <a href="{site_url}/contact/" style="color:#94a3b8;text-decoration:none">Contact us</a>
          </div>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>
"""
    return _send(
        subject=f"Welcome to Pagecraft, {name}! 🎉",
        html_body=html,
        to_email=user.email,
    )


def send_verification_email(user, profile):
    """Send email verification link (optional flow)."""
    site_url = getattr(settings, 'SITE_URL', 'http://127.0.0.1:8000')
    verify_url = f"{site_url}/verify/{profile.verification_token}/"
    name = profile.full_name or user.username
    html = f"""\
<!DOCTYPE html>
<html><body style="font-family:-apple-system,sans-serif;background:#f8fafc;padding:40px">
  <table style="max-width:520px;margin:0 auto;background:#fff;border-radius:14px;border:1px solid #e5e9f2;padding:36px">
    <tr><td>
      <h2 style="margin:0 0 14px;color:#0f172a">Verify your email, {name}</h2>
      <p style="color:#475569;line-height:1.6">Click the button below to verify your Pagecraft account. This link expires in 24 hours.</p>
      <p style="margin:24px 0">
        <a href="{verify_url}" style="display:inline-block;background:#0052FF;color:#fff;padding:14px 32px;border-radius:10px;text-decoration:none;font-weight:700">Verify Email</a>
      </p>
      <p style="font-size:12px;color:#94a3b8">If the button doesn't work, copy this link: {verify_url}</p>
    </td></tr>
  </table>
</body></html>
"""
    return _send(
        subject="Verify your Pagecraft email",
        html_body=html,
        to_email=user.email,
    )


def send_password_reset_email(user, reset_url):
    """Sent when user requests a password reset."""
    name = user.first_name or user.username
    html = f"""\
<!DOCTYPE html>
<html><body style="font-family:-apple-system,sans-serif;background:#f8fafc;padding:40px">
  <table style="max-width:520px;margin:0 auto;background:#fff;border-radius:14px;border:1px solid #e5e9f2;padding:36px">
    <tr><td>
      <h2 style="margin:0 0 14px">Reset your Pagecraft password</h2>
      <p style="color:#475569;line-height:1.6">Hi {name}, click the button below to reset your password. This link expires in 1 hour.</p>
      <p style="margin:24px 0">
        <a href="{reset_url}" style="display:inline-block;background:#0052FF;color:#fff;padding:14px 32px;border-radius:10px;text-decoration:none;font-weight:700">Reset Password</a>
      </p>
      <p style="font-size:12px;color:#94a3b8">If you didn't request this, ignore this email — your password will stay the same.</p>
    </td></tr>
  </table>
</body></html>
"""
    return _send(
        subject="Reset your Pagecraft password",
        html_body=html,
        to_email=user.email,
    )


def send_contact_form_email(name, email, message):
    """Forward a contact form submission to support."""
    support = getattr(settings, 'SUPPORT_EMAIL', 'support@pagecraft.app')
    html = f"""\
<html><body style="font-family:sans-serif">
  <h3>New contact form submission</h3>
  <p><strong>From:</strong> {name} &lt;{email}&gt;</p>
  <p><strong>Message:</strong></p>
  <div style="background:#f8fafc;padding:14px;border-left:4px solid #0052FF">{message}</div>
</body></html>
"""
    try:
        send_mail(
            subject=f"[Pagecraft Contact] {name}",
            message=f"From: {name} <{email}>\n\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[support],
            html_message=html,
            fail_silently=True,
        )
        return True
    except Exception as e:
        logger.error(f"Contact email failed: {e}")
        return False
