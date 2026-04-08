"""Seed the database with 15+ professional templates per category."""
from django.core.management.base import BaseCommand
from generator.models import Template
from . import _seed_extra as ex
from . import _seed_extra2 as ex2
from . import _seed_weddings_religious as wedrel
from . import _seed_animated_weddings as wedanim
from . import _seed_ultra_premium as ultra
from . import _seed_canva_inspired as canva
from . import _seed_canva_categories as canvacat
from . import _seed_distinct_all as distinct
from . import _seed_resumes_pro as respro
from . import _seed_premium as prem


# ============================================================
# SHARED FIELD SCHEMAS — reused across templates of same type
# ============================================================

RESUME_FIELDS = [
    {'name': 'name', 'label': 'Full Name', 'type': 'text'},
    {'name': 'title', 'label': 'Job Title', 'type': 'text'},
    {'name': 'email', 'label': 'Email', 'type': 'email'},
    {'name': 'phone', 'label': 'Phone', 'type': 'text'},
    {'name': 'location', 'label': 'Location', 'type': 'text'},
    {'name': 'summary', 'label': 'Professional Summary', 'type': 'textarea', 'ai': True},
    {'name': 'experience', 'label': 'Experience', 'type': 'textarea', 'ai': True},
    {'name': 'education', 'label': 'Education', 'type': 'textarea'},
    {'name': 'skills', 'label': 'Skills (comma separated)', 'type': 'text'},
]

RESUME_SAMPLES = [
    {'name': 'Aarav Sharma', 'title': 'Senior Software Engineer', 'email': 'aarav@example.com',
     'phone': '+91 98765 43210', 'location': 'Bangalore, India',
     'summary': 'Results-driven engineer with 6+ years building scalable web systems.',
     'experience': 'Acme Corp — Senior Engineer (2021–Present)\nBuilt microservices serving 2M users.\n\nXYZ Labs — Engineer (2018–2021)\nLed migration to Kubernetes.',
     'education': 'B.Tech Computer Science, IIT Delhi (2018)',
     'skills': 'Python, Django, React, AWS, PostgreSQL, Docker'},
    {'name': 'Priya Verma', 'title': 'Marketing Manager', 'email': 'priya@example.com',
     'phone': '+91 90000 11111', 'location': 'Mumbai, India',
     'summary': 'Award-winning marketer specializing in brand storytelling and digital growth.',
     'experience': 'BrandWorks — Marketing Manager (2020–Present)\nLed campaigns reaching 5M+ users.',
     'education': 'MBA, IIM Bangalore (2019)',
     'skills': 'SEO, Content Strategy, Analytics, Branding, Adobe Suite'},
    {'name': 'Rohan Mehta', 'title': 'Product Designer', 'email': 'rohan@example.com',
     'phone': '+91 99887 76655', 'location': 'Pune, India',
     'summary': 'UI/UX designer focused on crafting intuitive, beautiful digital experiences.',
     'experience': 'Pixelcraft — Lead Designer (2022–Present)\nDesigned 12 mobile apps with 4.8★ ratings.',
     'education': 'B.Des, NID Ahmedabad (2020)',
     'skills': 'Figma, Sketch, Prototyping, UX Research, Design Systems'},
]

INVOICE_FIELDS = [
    {'name': 'company', 'label': 'Your Company', 'type': 'text'},
    {'name': 'company_address', 'label': 'Your Address', 'type': 'textarea'},
    {'name': 'client', 'label': 'Client Name', 'type': 'text'},
    {'name': 'client_address', 'label': 'Client Address', 'type': 'textarea'},
    {'name': 'invoice_no', 'label': 'Invoice #', 'type': 'text'},
    {'name': 'date', 'label': 'Date', 'type': 'date'},
    {'name': 'items', 'label': 'Line Items', 'type': 'items',
     'item_fields': [
         {'name': 'desc',  'label': 'Description', 'placeholder': 'Item or service'},
         {'name': 'qty',   'label': 'Qty',         'placeholder': '1'},
         {'name': 'price', 'label': 'Unit Price',  'placeholder': '0'},
     ]},
    {'name': 'notes', 'label': 'Notes', 'type': 'textarea'},
]

INVOICE_SAMPLE = {
    'company': 'Pixel Studio Pvt Ltd',
    'company_address': '12 MG Road, Bangalore, India',
    'client': 'Acme Industries',
    'client_address': '88 Market Street, Mumbai, India',
    'invoice_no': 'INV-2026-001',
    'date': '2026-04-07',
    'items': [
        {'desc': 'Website Design & Development', 'qty': '1',  'price': '45000'},
        {'desc': 'Logo & Brand Identity',         'qty': '1',  'price': '15000'},
        {'desc': 'Hosting (12 months)',           'qty': '12', 'price': '500'},
        {'desc': 'SEO Setup',                     'qty': '1',  'price': '8000'},
    ],
    'notes': 'Payment due within 15 days. Thank you for your business!',
}

CARD_FIELDS = [
    {'name': 'name', 'label': 'Full Name', 'type': 'text'},
    {'name': 'title', 'label': 'Job Title', 'type': 'text'},
    {'name': 'company', 'label': 'Company', 'type': 'text'},
    {'name': 'email', 'label': 'Email', 'type': 'email'},
    {'name': 'phone', 'label': 'Phone', 'type': 'text'},
    {'name': 'website', 'label': 'Website', 'type': 'text'},
    {'name': 'address', 'label': 'Address', 'type': 'text'},
]

CARD_SAMPLES = [
    {'name': 'Rahul Mehta', 'title': 'Founder & CEO', 'company': 'NovaTech Labs',
     'email': 'rahul@novatech.io', 'phone': '+91 99887 76655', 'website': 'novatech.io',
     'address': 'Bangalore, India'},
    {'name': 'Anjali Kapoor', 'title': 'Interior Designer', 'company': 'Studio Aanya',
     'email': 'hello@studioaanya.com', 'phone': '+91 98700 12345', 'website': 'studioaanya.com',
     'address': 'Delhi, India'},
    {'name': 'Dr. Sameer Khan', 'title': 'Cardiologist', 'company': 'HeartCare Clinic',
     'email': 'dr.sameer@heartcare.in', 'phone': '+91 91234 56789', 'website': 'heartcare.in',
     'address': 'Mumbai, India'},
]

SOCIAL_FIELDS = [
    {'name': 'headline', 'label': 'Headline', 'type': 'text', 'ai': True},
    {'name': 'body', 'label': 'Body Text', 'type': 'textarea', 'ai': True},
    {'name': 'cta', 'label': 'Call to Action', 'type': 'text'},
    {'name': 'handle', 'label': 'Your Handle', 'type': 'text'},
]

SOCIAL_SAMPLES = [
    {'headline': 'Big Summer Sale', 'body': 'Up to 50% off on all collections. Limited time only!',
     'cta': 'Shop Now', 'handle': '@yourbrand'},
    {'headline': 'New Product Launch', 'body': 'Introducing our latest innovation — built for you.',
     'cta': 'Learn More', 'handle': '@yourbrand'},
    {'headline': 'Behind the Scenes', 'body': 'A peek into how we create magic, every single day.',
     'cta': 'Follow Us', 'handle': '@yourbrand'},
]

WEDDING_FIELDS = [
    {'name': 'bride', 'label': 'Bride Name', 'type': 'text'},
    {'name': 'groom', 'label': 'Groom Name', 'type': 'text'},
    {'name': 'date', 'label': 'Wedding Date', 'type': 'text'},
    {'name': 'time', 'label': 'Time', 'type': 'text'},
    {'name': 'venue', 'label': 'Venue', 'type': 'textarea'},
    {'name': 'message', 'label': 'Personal Message', 'type': 'textarea', 'ai': True},
    {'name': 'rsvp', 'label': 'RSVP Contact', 'type': 'text'},
]

WEDDING_SAMPLES = [
    {'bride': 'Ananya', 'groom': 'Arjun', 'date': 'Saturday, 14th February 2026', 'time': '6:00 PM onwards',
     'venue': 'The Leela Palace,\nMG Road, Bangalore',
     'message': 'Together with their families, request the honour of your presence.',
     'rsvp': '+91 98765 43210'},
    {'bride': 'Sophia', 'groom': 'Daniel', 'date': '15.06.2026', 'time': '4:00 PM',
     'venue': 'Sunset Beach Resort, Goa',
     'message': "We're getting married and we'd love for you to be part of our day.",
     'rsvp': '+91 90000 11111'},
    {'bride': 'Priya', 'groom': 'Vikram', 'date': '22nd November 2026', 'time': '7:00 PM',
     'venue': 'Umaid Bhawan Palace, Jodhpur',
     'message': 'With the blessings of our elders, we invite you to our union.',
     'rsvp': '+91 91234 56789'},
]


def R(idx=0): return dict(RESUME_SAMPLES[idx % len(RESUME_SAMPLES)])
def C(idx=0): return dict(CARD_SAMPLES[idx % len(CARD_SAMPLES)])
def S(idx=0): return dict(SOCIAL_SAMPLES[idx % len(SOCIAL_SAMPLES)])
def W(idx=0): return dict(WEDDING_SAMPLES[idx % len(WEDDING_SAMPLES)])
def I(): return dict(INVOICE_SAMPLE)


# ============================================================
# RESUME TEMPLATES (15)
# ============================================================
RESUMES = [
    {'title': 'Modern Minimal', 'desc': 'Clean single-column with blue accent bar.',
     'css': ".r1{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:40px;background:#fff;color:#222}.r1 h1{font-size:34px;margin:0;color:#0d47a1;border-left:6px solid #1976d2;padding-left:14px}.r1 .role{color:#555;font-size:18px;margin:6px 0 4px 20px}.r1 .ct{margin:4px 0 24px 20px;color:#666;font-size:14px}.r1 h2{color:#1976d2;border-bottom:2px solid #e3f2fd;padding-bottom:4px;margin-top:24px;font-size:18px}.r1 pre{white-space:pre-wrap;font-family:inherit;line-height:1.55;margin:8px 0}.r1 .sk span{display:inline-block;background:#e3f2fd;color:#0d47a1;padding:5px 12px;border-radius:20px;margin:4px 4px 0 0;font-size:13px}",
     'html': '<div class="r1"><h1>{{ name }}</h1><div class="role">{{ title }}</div><div class="ct">{{ email }} • {{ phone }} • {{ location }}</div><h2>Summary</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><div class="sk">{% for s in skills_list %}<span>{{ s }}</span>{% endfor %}</div></div>'},

    {'title': 'Classic Professional', 'desc': 'Traditional serif with double-line header.',
     'css': ".r2{font-family:Georgia,serif;max-width:780px;margin:0 auto;padding:40px;background:#fff;color:#1a1a1a}.r2 header{text-align:center;border-bottom:3px double #333;padding-bottom:14px;margin-bottom:18px}.r2 h1{margin:0;font-size:32px;letter-spacing:2px}.r2 .meta{font-style:italic;color:#555;margin-top:6px}.r2 h2{font-size:17px;text-transform:uppercase;letter-spacing:2px;border-bottom:1px solid #ccc;margin-top:20px}.r2 pre{font-family:inherit;white-space:pre-wrap;line-height:1.6;margin:8px 0}",
     'html': '<div class="r2"><header><h1>{{ name }}</h1><div class="meta">{{ title }} • {{ email }} • {{ phone }} • {{ location }}</div></header><h2>Profile</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><pre>{{ skills }}</pre></div>'},

    {'title': 'Tech Developer Dark', 'desc': 'Code-inspired dark theme for engineers.',
     'css': ".r3{font-family:'Consolas',monospace;max-width:780px;margin:0 auto;padding:40px;background:#0d1117;color:#c9d1d9}.r3 h1{font-size:32px;color:#58a6ff;margin:0}.r3 .role{color:#7ee787;margin:6px 0}.r3 .ct{color:#8b949e;font-size:13px;margin-bottom:20px}.r3 h2{color:#f78166;border-bottom:1px solid #30363d;padding-bottom:4px;font-size:16px;margin-top:22px}.r3 h2::before{content:'> ';color:#7ee787}.r3 pre{white-space:pre-wrap;font-family:inherit;line-height:1.6;color:#c9d1d9}.r3 .sk span{display:inline-block;background:#161b22;color:#58a6ff;border:1px solid #30363d;padding:4px 10px;border-radius:4px;margin:3px;font-size:12px}",
     'html': '<div class="r3"><h1>{{ name }}</h1><div class="role">{{ title }}</div><div class="ct">{{ email }} | {{ phone }} | {{ location }}</div><h2>about</h2><pre>{{ summary }}</pre><h2>experience</h2><pre>{{ experience }}</pre><h2>education</h2><pre>{{ education }}</pre><h2>skills</h2><div class="sk">{% for s in skills_list %}<span>{{ s }}</span>{% endfor %}</div></div>'},

    {'title': 'Executive Black & Gold', 'desc': 'Luxurious resume for senior executives.',
     'css': ".r4{font-family:'Playfair Display',Georgia,serif;max-width:780px;margin:0 auto;padding:50px;background:#fff;color:#111;border-top:8px solid #c9a227}.r4 h1{font-size:38px;margin:0;letter-spacing:2px}.r4 .role{color:#c9a227;letter-spacing:4px;text-transform:uppercase;font-size:14px;margin:8px 0}.r4 .ct{font-size:13px;color:#666;border-bottom:1px solid #eee;padding-bottom:14px;margin-bottom:18px}.r4 h2{font-size:18px;letter-spacing:3px;text-transform:uppercase;color:#c9a227;margin-top:22px}.r4 pre{font-family:'Segoe UI',sans-serif;white-space:pre-wrap;line-height:1.7;color:#333}",
     'html': '<div class="r4"><h1>{{ name }}</h1><div class="role">{{ title }}</div><div class="ct">{{ email }} · {{ phone }} · {{ location }}</div><h2>Executive Summary</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Core Competencies</h2><pre>{{ skills }}</pre></div>'},

    {'title': 'Creative Two-Column', 'desc': 'Sidebar layout with colored panel.',
     'css': ".r5{display:flex;font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;background:#fff;min-height:600px}.r5 .side{width:35%;background:#2c3e50;color:#ecf0f1;padding:30px 20px}.r5 .side h1{font-size:24px;margin:0 0 4px}.r5 .side .role{color:#3498db;font-size:13px;margin-bottom:18px}.r5 .side h3{font-size:13px;letter-spacing:2px;text-transform:uppercase;color:#3498db;margin-top:18px;border-bottom:1px solid #34495e;padding-bottom:4px}.r5 .side p{font-size:12px;line-height:1.6;color:#bdc3c7}.r5 .main{flex:1;padding:30px}.r5 .main h2{color:#2c3e50;border-bottom:3px solid #3498db;padding-bottom:4px;font-size:16px}.r5 .main pre{font-family:inherit;white-space:pre-wrap;font-size:13px;line-height:1.6;color:#444}",
     'html': '<div class="r5"><div class="side"><h1>{{ name }}</h1><div class="role">{{ title }}</div><h3>Contact</h3><p>{{ email }}<br>{{ phone }}<br>{{ location }}</p><h3>Skills</h3><p>{{ skills }}</p><h3>Education</h3><p>{{ education }}</p></div><div class="main"><h2>About Me</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre></div></div>'},

    {'title': 'Designer Portfolio', 'desc': 'Vibrant gradient header for creatives.',
     'css': ".r6{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;background:#fff}.r6 .top{background:linear-gradient(135deg,#f093fb 0%,#f5576c 100%);color:#fff;padding:40px}.r6 .top h1{font-size:36px;margin:0}.r6 .top .role{font-size:16px;opacity:.9;margin-top:6px}.r6 .top .ct{margin-top:14px;font-size:13px;opacity:.85}.r6 .body{padding:30px 40px}.r6 h2{color:#f5576c;font-size:18px;margin-top:18px;border-left:4px solid #f093fb;padding-left:10px}.r6 pre{font-family:inherit;white-space:pre-wrap;line-height:1.6;color:#444}",
     'html': '<div class="r6"><div class="top"><h1>{{ name }}</h1><div class="role">{{ title }}</div><div class="ct">{{ email }} · {{ phone }} · {{ location }}</div></div><div class="body"><h2>About</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><pre>{{ skills }}</pre></div></div>'},

    {'title': 'Academic CV', 'desc': 'Formal CV layout for academia.',
     'css': ".r7{font-family:'Times New Roman',serif;max-width:780px;margin:0 auto;padding:50px;background:#fff;color:#000}.r7 h1{text-align:center;margin:0;font-size:28px}.r7 .ct{text-align:center;font-size:13px;margin:6px 0 20px}.r7 h2{font-size:15px;text-transform:uppercase;letter-spacing:1px;border-bottom:1px solid #000;margin-top:18px}.r7 pre{font-family:inherit;white-space:pre-wrap;line-height:1.5;font-size:14px}",
     'html': '<div class="r7"><h1>{{ name }}</h1><div class="ct">{{ title }}<br>{{ email }} | {{ phone }} | {{ location }}</div><h2>Research Statement</h2><pre>{{ summary }}</pre><h2>Academic Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Areas of Expertise</h2><pre>{{ skills }}</pre></div>'},

    {'title': 'Fresh Graduate', 'desc': 'Friendly modern resume for new grads.',
     'css': ".r8{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:40px;background:#fff;color:#333}.r8 h1{font-size:32px;margin:0;color:#00897b}.r8 .role{color:#666;margin:4px 0}.r8 .ct{background:#e0f2f1;padding:10px 16px;border-radius:8px;font-size:13px;color:#00695c;margin:14px 0}.r8 h2{color:#00897b;font-size:17px;margin-top:20px}.r8 h2::before{content:'◆ ';color:#26a69a}.r8 pre{font-family:inherit;white-space:pre-wrap;line-height:1.6}",
     'html': '<div class="r8"><h1>{{ name }}</h1><div class="role">{{ title }}</div><div class="ct">📧 {{ email }} &nbsp; 📱 {{ phone }} &nbsp; 📍 {{ location }}</div><h2>Hello!</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><pre>{{ skills }}</pre></div>'},

    {'title': 'Marketing Pro', 'desc': 'Bold and confident for marketers.',
     'css': ".r9{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;background:#fff}.r9 .top{background:#e91e63;color:#fff;padding:40px;text-align:center}.r9 .top h1{margin:0;font-size:42px;font-weight:800}.r9 .top .role{font-size:16px;letter-spacing:4px;text-transform:uppercase;margin-top:8px;opacity:.95}.r9 .body{padding:30px 40px}.r9 .ct{text-align:center;color:#666;font-size:13px;margin-bottom:20px}.r9 h2{color:#e91e63;font-size:18px;text-transform:uppercase;letter-spacing:2px;border-bottom:2px solid #fce4ec;padding-bottom:4px}.r9 pre{font-family:inherit;white-space:pre-wrap;line-height:1.6;color:#444}",
     'html': '<div class="r9"><div class="top"><h1>{{ name }}</h1><div class="role">{{ title }}</div></div><div class="body"><div class="ct">{{ email }} • {{ phone }} • {{ location }}</div><h2>Profile</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><pre>{{ skills }}</pre></div></div>'},

    {'title': 'Healthcare Clean', 'desc': 'Trustworthy teal design for medical pros.',
     'css': ".r10{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:40px;background:#fff;border-top:6px solid #00acc1}.r10 h1{font-size:32px;margin:0;color:#006064}.r10 .role{color:#00acc1;font-size:17px;margin:4px 0}.r10 .ct{color:#666;font-size:13px;margin-bottom:18px}.r10 h2{color:#006064;background:#e0f7fa;padding:6px 12px;border-radius:4px;font-size:16px;margin-top:18px}.r10 pre{font-family:inherit;white-space:pre-wrap;line-height:1.6;padding:0 12px}",
     'html': '<div class="r10"><h1>{{ name }}</h1><div class="role">{{ title }}</div><div class="ct">{{ email }} | {{ phone }} | {{ location }}</div><h2>Professional Summary</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><pre>{{ skills }}</pre></div>'},

    {'title': 'Sales Champion', 'desc': 'Energetic red theme to close deals.',
     'css': ".r11{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:40px;background:#fff}.r11 h1{font-size:34px;margin:0;color:#c62828;border-bottom:4px solid #c62828;padding-bottom:8px}.r11 .role{color:#666;margin:8px 0}.r11 .ct{font-size:13px;color:#888;margin-bottom:18px}.r11 h2{color:#fff;background:#c62828;padding:6px 14px;font-size:15px;letter-spacing:2px;text-transform:uppercase;display:inline-block;margin-top:20px}.r11 pre{font-family:inherit;white-space:pre-wrap;line-height:1.6;color:#333}",
     'html': '<div class="r11"><h1>{{ name }}</h1><div class="role">{{ title }}</div><div class="ct">{{ email }} • {{ phone }} • {{ location }}</div><h2>Profile</h2><pre>{{ summary }}</pre><h2>Track Record</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><pre>{{ skills }}</pre></div>'},

    {'title': 'Educator Warm', 'desc': 'Warm earthy tones for teachers.',
     'css': ".r12{font-family:Georgia,serif;max-width:780px;margin:0 auto;padding:40px;background:#fffaf3;color:#3e2723}.r12 h1{font-size:32px;margin:0;color:#5d4037}.r12 .role{color:#8d6e63;font-style:italic;margin:6px 0}.r12 .ct{color:#795548;font-size:13px;margin-bottom:18px}.r12 h2{color:#5d4037;border-bottom:2px dotted #8d6e63;font-size:17px;margin-top:20px}.r12 pre{font-family:'Segoe UI',sans-serif;white-space:pre-wrap;line-height:1.7;color:#4e342e}",
     'html': '<div class="r12"><h1>{{ name }}</h1><div class="role">{{ title }}</div><div class="ct">{{ email }} · {{ phone }} · {{ location }}</div><h2>Teaching Philosophy</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><pre>{{ skills }}</pre></div>'},

    {'title': 'Finance Navy', 'desc': 'Polished navy resume for finance pros.',
     'css': ".r13{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;background:#fff}.r13 .top{background:#0d47a1;color:#fff;padding:34px 40px}.r13 .top h1{margin:0;font-size:32px}.r13 .top .role{margin-top:4px;color:#bbdefb}.r13 .top .ct{margin-top:10px;font-size:13px;color:#e3f2fd}.r13 .body{padding:30px 40px}.r13 h2{color:#0d47a1;font-size:16px;letter-spacing:1px;text-transform:uppercase;border-bottom:1px solid #0d47a1;padding-bottom:4px;margin-top:18px}.r13 pre{font-family:inherit;white-space:pre-wrap;line-height:1.6;color:#333}",
     'html': '<div class="r13"><div class="top"><h1>{{ name }}</h1><div class="role">{{ title }}</div><div class="ct">{{ email }} | {{ phone }} | {{ location }}</div></div><div class="body"><h2>Summary</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><pre>{{ skills }}</pre></div></div>'},

    {'title': 'Compact One-Page', 'desc': 'Dense layout that fits on one page.',
     'css': ".r14{font-family:'Helvetica',Arial,sans-serif;max-width:780px;margin:0 auto;padding:30px;background:#fff;font-size:13px}.r14 .hd{display:flex;justify-content:space-between;align-items:end;border-bottom:2px solid #333;padding-bottom:8px}.r14 h1{margin:0;font-size:26px}.r14 .ct{font-size:11px;color:#666;text-align:right}.r14 h2{font-size:13px;text-transform:uppercase;letter-spacing:1px;color:#333;margin:14px 0 4px;border-bottom:1px solid #ddd;padding-bottom:2px}.r14 pre{font-family:inherit;white-space:pre-wrap;line-height:1.45;margin:4px 0;font-size:12px}",
     'html': '<div class="r14"><div class="hd"><div><h1>{{ name }}</h1><div>{{ title }}</div></div><div class="ct">{{ email }}<br>{{ phone }}<br>{{ location }}</div></div><h2>Summary</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><pre>{{ skills }}</pre></div>'},

    {'title': 'Bold Header Resume', 'desc': 'Giant name banner across the top.',
     'css': ".r15{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;background:#fff}.r15 .ban{background:#212121;color:#fff;padding:50px 40px;text-align:center}.r15 .ban h1{margin:0;font-size:54px;font-weight:900;letter-spacing:4px}.r15 .ban .role{color:#ffd54f;letter-spacing:6px;font-size:14px;text-transform:uppercase;margin-top:8px}.r15 .body{padding:30px 40px}.r15 .ct{text-align:center;color:#666;font-size:13px;margin-bottom:20px}.r15 h2{color:#212121;font-size:18px;border-left:5px solid #ffd54f;padding-left:10px;margin-top:18px}.r15 pre{font-family:inherit;white-space:pre-wrap;line-height:1.6;color:#444}",
     'html': '<div class="r15"><div class="ban"><h1>{{ name }}</h1><div class="role">{{ title }}</div></div><div class="body"><div class="ct">{{ email }} · {{ phone }} · {{ location }}</div><h2>About</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><pre>{{ skills }}</pre></div></div>'},
]


# ============================================================
# INVOICE TEMPLATES (15)
# ============================================================
INVOICES = [
    {'title': 'Standard Teal', 'desc': 'Professional invoice with itemised table.',
     'css': ".i1{font-family:Arial,sans-serif;max-width:780px;margin:0 auto;padding:40px;background:#fff;color:#222}.i1 .top{display:flex;justify-content:space-between;border-bottom:4px solid #00897b;padding-bottom:14px}.i1 h1{color:#00897b;margin:0;font-size:30px}.i1 table{width:100%;border-collapse:collapse;margin-top:24px}.i1 th{background:#00897b;color:#fff;padding:10px;text-align:left}.i1 td{padding:10px;border-bottom:1px solid #eee}.i1 .total{text-align:right;font-size:20px;font-weight:bold;margin-top:14px;color:#00695c}.i1 .notes{margin-top:18px;color:#555;font-size:13px;border-top:1px dashed #ccc;padding-top:10px}",
     'html': '<div class="i1"><div class="top"><div><h1>INVOICE</h1><div>{{ company }}</div><div style="font-size:12px;color:#666">{{ company_address }}</div></div><div style="text-align:right"><strong>{{ invoice_no }}</strong><br>{{ date }}<br><br><em>Bill To:</em><br>{{ client }}</div></div><table><tr><th>Description</th><th>Qty</th><th>Price</th><th>Amount</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="total">Total: ₹{{ total }}</div><div class="notes">{{ notes }}</div></div>'},

    {'title': 'Modern Purple', 'desc': 'Vibrant purple modern invoice.',
     'css': ".i2{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:40px;background:#fff;color:#222}.i2 .hd{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;padding:24px;border-radius:8px}.i2 .hd h1{margin:0;font-size:32px;letter-spacing:2px}.i2 .hd p{margin:4px 0;font-size:13px;opacity:.9}.i2 .meta{display:flex;justify-content:space-between;margin:20px 0}.i2 .meta div{font-size:13px}.i2 table{width:100%;border-collapse:collapse}.i2 th{background:#f3e5f5;color:#4a148c;padding:10px;text-align:left}.i2 td{padding:10px;border-bottom:1px solid #eee}.i2 .total{text-align:right;font-size:22px;color:#4a148c;margin-top:14px;font-weight:bold}.i2 .notes{margin-top:14px;font-size:13px;color:#666}",
     'html': '<div class="i2"><div class="hd"><h1>INVOICE</h1><p>{{ company }} · {{ company_address }}</p></div><div class="meta"><div><strong>Bill To:</strong><br>{{ client }}<br>{{ client_address }}</div><div style="text-align:right"><strong>{{ invoice_no }}</strong><br>{{ date }}</div></div><table><tr><th>Item</th><th>Qty</th><th>Price</th><th>Total</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="total">₹{{ total }}</div><div class="notes">{{ notes }}</div></div>'},

    {'title': 'Minimal Black', 'desc': 'Stripped-down black & white invoice.',
     'css': ".i3{font-family:'Helvetica',sans-serif;max-width:780px;margin:0 auto;padding:50px;background:#fff;color:#000}.i3 h1{font-size:42px;margin:0;letter-spacing:6px;font-weight:300}.i3 .meta{display:flex;justify-content:space-between;margin:30px 0;font-size:13px}.i3 table{width:100%;border-top:2px solid #000;border-bottom:2px solid #000}.i3 th{padding:12px 8px;text-align:left;font-size:11px;letter-spacing:2px;text-transform:uppercase;border-bottom:1px solid #ccc}.i3 td{padding:14px 8px}.i3 .total{text-align:right;font-size:24px;margin-top:14px;letter-spacing:2px}",
     'html': '<div class="i3"><h1>INVOICE</h1><div class="meta"><div>{{ company }}<br>{{ company_address }}</div><div style="text-align:right">{{ invoice_no }}<br>{{ date }}</div></div><div><strong>BILL TO</strong><br>{{ client }}<br>{{ client_address }}</div><table><tr><th>Description</th><th>Qty</th><th>Price</th><th>Amount</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="total">TOTAL ₹{{ total }}</div><div style="margin-top:14px;font-size:12px;color:#666">{{ notes }}</div></div>'},

    {'title': 'Corporate Blue', 'desc': 'Classic corporate invoice with navy header.',
     'css': ".i4{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;background:#fff}.i4 .top{background:#0d47a1;color:#fff;padding:30px 40px;display:flex;justify-content:space-between}.i4 .top h1{margin:0;font-size:30px}.i4 .body{padding:30px 40px}.i4 .meta{display:flex;justify-content:space-between;margin-bottom:20px;font-size:13px}.i4 table{width:100%;border-collapse:collapse}.i4 th{background:#e3f2fd;padding:10px;text-align:left;color:#0d47a1}.i4 td{padding:10px;border-bottom:1px solid #eee}.i4 .total{text-align:right;background:#0d47a1;color:#fff;padding:12px;font-size:20px;margin-top:10px}",
     'html': '<div class="i4"><div class="top"><div><h1>INVOICE</h1><div>{{ company }}</div></div><div style="text-align:right">{{ invoice_no }}<br>{{ date }}</div></div><div class="body"><div class="meta"><div><strong>From</strong><br>{{ company_address }}</div><div><strong>Bill To</strong><br>{{ client }}<br>{{ client_address }}</div></div><table><tr><th>Description</th><th>Qty</th><th>Price</th><th>Total</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="total">Grand Total: ₹{{ total }}</div><div style="margin-top:14px;font-size:13px;color:#666">{{ notes }}</div></div></div>'},

    {'title': 'Freelancer Pink', 'desc': 'Friendly soft-pink invoice for freelancers.',
     'css': ".i5{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:40px;background:#fff5f7}.i5 h1{color:#d81b60;font-size:36px;margin:0}.i5 .sub{color:#ad1457;font-size:13px}.i5 .meta{display:flex;justify-content:space-between;margin:24px 0;background:#fff;padding:16px;border-radius:8px}.i5 table{width:100%;background:#fff;border-radius:8px;overflow:hidden;border-collapse:collapse}.i5 th{background:#f8bbd0;color:#880e4f;padding:10px;text-align:left}.i5 td{padding:10px;border-bottom:1px solid #fce4ec}.i5 .total{text-align:right;font-size:22px;color:#d81b60;margin-top:14px;font-weight:bold}",
     'html': '<div class="i5"><h1>Invoice ✨</h1><div class="sub">{{ company }} · {{ company_address }}</div><div class="meta"><div><strong>To:</strong><br>{{ client }}<br>{{ client_address }}</div><div style="text-align:right">{{ invoice_no }}<br>{{ date }}</div></div><table><tr><th>Item</th><th>Qty</th><th>Price</th><th>Total</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="total">Total: ₹{{ total }}</div><div style="margin-top:14px;font-size:13px;color:#666">{{ notes }}</div></div>'},

    {'title': 'Creative Agency', 'desc': 'Bold orange invoice for design agencies.',
     'css': ".i6{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:40px;background:#fff}.i6 .top{border-bottom:6px solid #ff6f00;padding-bottom:14px;margin-bottom:20px}.i6 h1{color:#ff6f00;font-size:48px;margin:0;font-weight:900}.i6 .meta{display:flex;justify-content:space-between;font-size:13px;margin-bottom:20px}.i6 table{width:100%;border-collapse:collapse}.i6 th{background:#212121;color:#ff6f00;padding:12px;text-align:left;letter-spacing:1px;text-transform:uppercase;font-size:12px}.i6 td{padding:12px;border-bottom:1px solid #eee}.i6 .total{text-align:right;font-size:24px;color:#ff6f00;margin-top:14px;font-weight:bold}",
     'html': '<div class="i6"><div class="top"><h1>INVOICE</h1></div><div class="meta"><div>{{ company }}<br>{{ company_address }}</div><div style="text-align:right">{{ invoice_no }}<br>{{ date }}</div></div><div><strong>Client:</strong> {{ client }} — {{ client_address }}</div><table><tr><th>Service</th><th>Qty</th><th>Rate</th><th>Total</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="total">TOTAL ₹{{ total }}</div><div style="margin-top:14px;font-size:13px;color:#666">{{ notes }}</div></div>'},

    {'title': 'Service Provider', 'desc': 'Clean green invoice for service businesses.',
     'css': ".i7{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:40px;background:#fff;border-left:8px solid #2e7d32}.i7 h1{color:#2e7d32;font-size:32px;margin:0}.i7 .sub{color:#666;font-size:13px}.i7 .meta{display:flex;justify-content:space-between;margin:24px 0;font-size:13px}.i7 table{width:100%;border-collapse:collapse}.i7 th{background:#e8f5e9;color:#2e7d32;padding:10px;text-align:left}.i7 td{padding:10px;border-bottom:1px solid #eee}.i7 .total{text-align:right;font-size:22px;color:#2e7d32;margin-top:14px;font-weight:bold}",
     'html': '<div class="i7"><h1>INVOICE</h1><div class="sub">{{ company }} · {{ company_address }}</div><div class="meta"><div><strong>Bill To</strong><br>{{ client }}<br>{{ client_address }}</div><div style="text-align:right">{{ invoice_no }}<br>{{ date }}</div></div><table><tr><th>Service</th><th>Qty</th><th>Price</th><th>Total</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="total">Total: ₹{{ total }}</div><div style="margin-top:14px;font-size:13px;color:#666">{{ notes }}</div></div>'},

    {'title': 'Consultant Slate', 'desc': 'Professional slate gray for consultants.',
     'css': ".i8{font-family:Georgia,serif;max-width:780px;margin:0 auto;padding:40px;background:#fff;color:#37474f}.i8 h1{font-size:34px;margin:0;letter-spacing:3px;border-bottom:2px solid #37474f;padding-bottom:8px}.i8 .meta{display:flex;justify-content:space-between;margin:24px 0;font-size:13px}.i8 table{width:100%;border-collapse:collapse}.i8 th{background:#37474f;color:#fff;padding:10px;text-align:left}.i8 td{padding:10px;border-bottom:1px solid #cfd8dc}.i8 .total{text-align:right;font-size:22px;margin-top:14px;font-weight:bold;color:#37474f}",
     'html': '<div class="i8"><h1>INVOICE</h1><div class="meta"><div>{{ company }}<br>{{ company_address }}</div><div style="text-align:right">{{ invoice_no }}<br>{{ date }}</div></div><div><strong>Client:</strong> {{ client }}, {{ client_address }}</div><table><tr><th>Description</th><th>Qty</th><th>Rate</th><th>Total</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="total">Total Due: ₹{{ total }}</div><div style="margin-top:14px;font-size:13px;color:#666">{{ notes }}</div></div>'},

    {'title': 'E-commerce Receipt', 'desc': 'Order-style receipt for online stores.',
     'css': ".i9{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:40px;background:#fff}.i9 .logo{text-align:center;margin-bottom:14px}.i9 .logo h1{color:#ff5722;margin:0;font-size:28px}.i9 .order{background:#fff3e0;border-radius:8px;padding:16px;text-align:center;margin-bottom:18px}.i9 table{width:100%;border-collapse:collapse}.i9 th{padding:10px;text-align:left;border-bottom:2px solid #ff5722;color:#bf360c}.i9 td{padding:10px;border-bottom:1px solid #ffe0b2}.i9 .total{background:#ff5722;color:#fff;padding:14px;text-align:right;font-size:20px;margin-top:14px;border-radius:6px}",
     'html': '<div class="i9"><div class="logo"><h1>{{ company }}</h1><div style="font-size:12px;color:#666">Order Receipt</div></div><div class="order">Order <strong>{{ invoice_no }}</strong> · {{ date }}<br>Customer: {{ client }}</div><table><tr><th>Product</th><th>Qty</th><th>Price</th><th>Total</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="total">Paid: ₹{{ total }}</div><div style="margin-top:14px;font-size:13px;color:#666;text-align:center">{{ notes }}</div></div>'},

    {'title': 'Restaurant Bill', 'desc': 'Bill format for cafes and restaurants.',
     'css': ".i10{font-family:'Courier New',monospace;max-width:480px;margin:0 auto;padding:30px;background:#fff;border:2px dashed #333}.i10 h1{text-align:center;margin:0;font-size:24px}.i10 .sub{text-align:center;font-size:12px;color:#666;margin-bottom:14px}.i10 hr{border:none;border-top:1px dashed #999;margin:10px 0}.i10 table{width:100%;font-size:13px}.i10 td{padding:4px 0}.i10 .total{font-size:18px;text-align:right;margin-top:10px;font-weight:bold;border-top:2px solid #000;padding-top:8px}",
     'html': '<div class="i10"><h1>{{ company }}</h1><div class="sub">{{ company_address }}</div><hr><div style="font-size:12px">Bill #{{ invoice_no }} · {{ date }}<br>Customer: {{ client }}</div><hr><table>{% for it in items %}<tr><td>{{ it.desc }} x{{ it.qty }}</td><td style="text-align:right">₹{{ it.total }}</td></tr>{% endfor %}</table><div class="total">TOTAL: ₹{{ total }}</div><hr><div style="text-align:center;font-size:11px;color:#666">{{ notes }}<br>** Thank you, visit again! **</div></div>'},

    {'title': 'Medical Invoice', 'desc': 'Calm clinical invoice for healthcare.',
     'css': ".i11{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:40px;background:#fff;border-top:6px solid #00acc1}.i11 h1{color:#006064;font-size:30px;margin:0}.i11 .sub{color:#00838f;font-size:13px}.i11 .meta{display:flex;justify-content:space-between;margin:20px 0;font-size:13px}.i11 table{width:100%;border-collapse:collapse}.i11 th{background:#e0f7fa;color:#006064;padding:10px;text-align:left}.i11 td{padding:10px;border-bottom:1px solid #b2ebf2}.i11 .total{text-align:right;color:#006064;font-size:22px;margin-top:14px;font-weight:bold}",
     'html': '<div class="i11"><h1>{{ company }}</h1><div class="sub">{{ company_address }}</div><div class="meta"><div><strong>Patient:</strong><br>{{ client }}<br>{{ client_address }}</div><div style="text-align:right">Bill #{{ invoice_no }}<br>{{ date }}</div></div><table><tr><th>Service / Test</th><th>Qty</th><th>Rate</th><th>Amount</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="total">Amount Due: ₹{{ total }}</div><div style="margin-top:14px;font-size:13px;color:#666">{{ notes }}</div></div>'},

    {'title': 'Legal Invoice', 'desc': 'Formal legal services invoice.',
     'css': ".i12{font-family:'Times New Roman',serif;max-width:780px;margin:0 auto;padding:50px;background:#fff;border:1px solid #000}.i12 h1{text-align:center;margin:0;font-size:26px;letter-spacing:4px;border-bottom:2px solid #000;padding-bottom:10px}.i12 .meta{display:flex;justify-content:space-between;margin:20px 0;font-size:14px}.i12 table{width:100%;border:1px solid #000;border-collapse:collapse}.i12 th,.i12 td{border:1px solid #000;padding:10px;text-align:left}.i12 th{background:#f5f5f5}.i12 .total{text-align:right;font-size:18px;margin-top:14px;font-weight:bold}",
     'html': '<div class="i12"><h1>INVOICE</h1><div class="meta"><div><strong>{{ company }}</strong><br>{{ company_address }}</div><div style="text-align:right">No. {{ invoice_no }}<br>Date: {{ date }}</div></div><div><strong>To:</strong> {{ client }}, {{ client_address }}</div><br><table><tr><th>Matter / Service</th><th>Hours</th><th>Rate</th><th>Amount</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="total">Total Payable: ₹{{ total }}</div><div style="margin-top:14px;font-size:13px;font-style:italic">{{ notes }}</div></div>'},

    {'title': 'Construction', 'desc': 'Heavy-duty invoice for contractors.',
     'css': ".i13{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;background:#fff}.i13 .top{background:#f57f17;color:#fff;padding:30px 40px;border-bottom:6px solid #212121}.i13 .top h1{margin:0;font-size:34px;letter-spacing:2px}.i13 .body{padding:30px 40px}.i13 .meta{display:flex;justify-content:space-between;margin-bottom:20px;font-size:13px}.i13 table{width:100%;border-collapse:collapse}.i13 th{background:#212121;color:#f57f17;padding:12px;text-align:left;text-transform:uppercase;font-size:12px}.i13 td{padding:12px;border-bottom:1px solid #eee}.i13 .total{background:#212121;color:#f57f17;padding:14px;text-align:right;font-size:22px;margin-top:14px}",
     'html': '<div class="i13"><div class="top"><h1>INVOICE</h1><div>{{ company }}</div></div><div class="body"><div class="meta"><div>{{ company_address }}</div><div style="text-align:right">{{ invoice_no }}<br>{{ date }}</div></div><div><strong>Project For:</strong> {{ client }}, {{ client_address }}</div><table><tr><th>Work Description</th><th>Qty</th><th>Rate</th><th>Total</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="total">TOTAL ₹{{ total }}</div><div style="margin-top:14px;font-size:13px;color:#666">{{ notes }}</div></div></div>'},

    {'title': 'Tech Company', 'desc': 'SaaS-style sleek invoice.',
     'css': ".i14{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:40px;background:#fafafa}.i14 .card{background:#fff;border-radius:12px;padding:32px;box-shadow:0 4px 20px rgba(0,0,0,.06)}.i14 h1{color:#3f51b5;font-size:30px;margin:0}.i14 .meta{display:flex;justify-content:space-between;margin:20px 0;font-size:13px}.i14 table{width:100%;border-collapse:collapse}.i14 th{padding:10px;text-align:left;color:#3f51b5;border-bottom:2px solid #3f51b5}.i14 td{padding:10px;border-bottom:1px solid #eee}.i14 .total{text-align:right;color:#3f51b5;font-size:24px;margin-top:14px;font-weight:bold}",
     'html': '<div class="i14"><div class="card"><h1>Invoice</h1><div class="meta"><div>{{ company }}<br>{{ company_address }}</div><div style="text-align:right">{{ invoice_no }}<br>{{ date }}</div></div><div><strong>Bill To:</strong> {{ client }} — {{ client_address }}</div><table><tr><th>Description</th><th>Qty</th><th>Price</th><th>Amount</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="total">₹{{ total }}</div><div style="margin-top:14px;font-size:13px;color:#666">{{ notes }}</div></div></div>'},

    {'title': 'Bold Header Invoice', 'desc': 'Massive INVOICE banner across the top.',
     'css': ".i15{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;background:#fff}.i15 .ban{background:#000;color:#ffd600;padding:30px 40px;text-align:center}.i15 .ban h1{margin:0;font-size:60px;font-weight:900;letter-spacing:8px}.i15 .body{padding:30px 40px}.i15 .meta{display:flex;justify-content:space-between;font-size:13px;margin-bottom:20px}.i15 table{width:100%;border-collapse:collapse}.i15 th{background:#ffd600;color:#000;padding:10px;text-align:left}.i15 td{padding:10px;border-bottom:1px solid #eee}.i15 .total{background:#000;color:#ffd600;text-align:right;padding:14px;font-size:22px;margin-top:14px}",
     'html': '<div class="i15"><div class="ban"><h1>INVOICE</h1></div><div class="body"><div class="meta"><div>{{ company }}<br>{{ company_address }}</div><div style="text-align:right">{{ invoice_no }}<br>{{ date }}</div></div><div><strong>To:</strong> {{ client }} — {{ client_address }}</div><table><tr><th>Item</th><th>Qty</th><th>Rate</th><th>Total</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="total">TOTAL ₹{{ total }}</div><div style="margin-top:14px;font-size:13px;color:#666">{{ notes }}</div></div></div>'},
]


# ============================================================
# VISITING CARD TEMPLATES (15)
# ============================================================
CARDS = [
    {'title': 'Modern Dark Stripe', 'desc': 'Sleek dark card with cyan accent stripe.',
     'css': ".c1{width:380px;height:220px;background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);color:#fff;border-radius:14px;padding:24px;font-family:'Segoe UI',sans-serif;margin:30px auto;box-shadow:0 18px 40px rgba(0,0,0,.25);position:relative;overflow:hidden}.c1::before{content:'';position:absolute;top:0;left:0;width:6px;height:100%;background:#00e5ff}.c1 h2{margin:0 0 4px 0;font-size:24px}.c1 .role{color:#80deea;font-size:14px;margin-bottom:14px}.c1 .company{font-weight:bold;font-size:16px}.c1 .ct{font-size:12px;line-height:1.7;margin-top:14px;color:#cfd8dc}",
     'html': '<div class="c1"><h2>{{ name }}</h2><div class="role">{{ title }}</div><div class="company">{{ company }}</div><div class="ct">📧 {{ email }}<br>📱 {{ phone }}<br>🌐 {{ website }}</div></div>'},

    {'title': 'Elegant Light Gold', 'desc': 'Minimalist white card with gold accents.',
     'css': ".c2{width:380px;height:220px;background:#fff;color:#1a1a1a;border:1px solid #eee;border-top:5px solid #c9a227;border-radius:8px;padding:28px;margin:30px auto;font-family:Georgia,serif;box-shadow:0 12px 30px rgba(0,0,0,.08)}.c2 h2{margin:0;font-size:24px}.c2 .role{color:#c9a227;letter-spacing:2px;font-size:12px;text-transform:uppercase;margin:6px 0 18px}.c2 .info{font-size:13px;line-height:1.7;color:#555}",
     'html': '<div class="c2"><h2>{{ name }}</h2><div class="role">{{ title }} • {{ company }}</div><div class="info">{{ email }}<br>{{ phone }}<br>{{ website }}</div></div>'},

    {'title': 'Gradient Sunset', 'desc': 'Vibrant gradient card with bold name.',
     'css': ".c3{width:380px;height:220px;background:linear-gradient(135deg,#ff6a00,#ee0979);color:#fff;border-radius:16px;padding:26px;font-family:'Segoe UI',sans-serif;margin:30px auto;box-shadow:0 20px 50px rgba(238,9,121,.35)}.c3 h2{margin:0;font-size:26px;font-weight:800}.c3 .role{margin:4px 0 16px;font-size:13px;opacity:.9}.c3 .ct{font-size:12px;line-height:1.7}",
     'html': '<div class="c3"><h2>{{ name }}</h2><div class="role">{{ title }} · {{ company }}</div><div class="ct">{{ email }}<br>{{ phone }}<br>{{ website }}</div></div>'},

    {'title': 'Pure Minimal', 'desc': 'Ultra-clean white card with thin border.',
     'css': ".c4{width:380px;height:220px;background:#fff;color:#000;border:1px solid #000;padding:30px;font-family:'Helvetica',sans-serif;margin:30px auto}.c4 h2{margin:0;font-size:22px;letter-spacing:1px}.c4 .role{font-size:11px;letter-spacing:3px;text-transform:uppercase;color:#888;margin:6px 0 24px}.c4 .ct{font-size:11px;line-height:1.8;color:#555}",
     'html': '<div class="c4"><h2>{{ name }}</h2><div class="role">{{ title }} — {{ company }}</div><div class="ct">{{ email }}<br>{{ phone }}<br>{{ website }}<br>{{ address }}</div></div>'},

    {'title': 'Bold Red Power', 'desc': 'Confident red card with white text.',
     'css': ".c5{width:380px;height:220px;background:#c62828;color:#fff;border-radius:10px;padding:26px;font-family:'Segoe UI',sans-serif;margin:30px auto;box-shadow:0 16px 36px rgba(198,40,40,.3);position:relative}.c5::after{content:'';position:absolute;bottom:0;right:0;width:80px;height:80px;background:#fff;opacity:.1;border-radius:50%;transform:translate(30px,30px)}.c5 h2{margin:0;font-size:26px}.c5 .role{margin:6px 0 18px;font-size:13px;opacity:.85}.c5 .ct{font-size:12px;line-height:1.7}",
     'html': '<div class="c5"><h2>{{ name }}</h2><div class="role">{{ title }} · {{ company }}</div><div class="ct">{{ email }}<br>{{ phone }}<br>{{ website }}</div></div>'},

    {'title': 'Tech Blue Circuit', 'desc': 'Tech-inspired blue card.',
     'css': ".c6{width:380px;height:220px;background:#1565c0;color:#fff;padding:26px;font-family:'Consolas',monospace;margin:30px auto;border-radius:8px;border-left:6px solid #00e5ff;box-shadow:0 14px 36px rgba(21,101,192,.3)}.c6 h2{margin:0;font-size:22px;font-family:'Segoe UI',sans-serif}.c6 .role{color:#80deea;font-size:13px;margin:4px 0 18px}.c6 .ct{font-size:12px;line-height:1.7}",
     'html': '<div class="c6"><h2>{{ name }}</h2><div class="role">// {{ title }} @ {{ company }}</div><div class="ct">{{ email }}<br>{{ phone }}<br>{{ website }}</div></div>'},

    {'title': 'Nature Green Leaf', 'desc': 'Earthy green for eco-friendly brands.',
     'css': ".c7{width:380px;height:220px;background:linear-gradient(135deg,#2e7d32,#66bb6a);color:#fff;border-radius:14px;padding:26px;font-family:'Segoe UI',sans-serif;margin:30px auto;box-shadow:0 16px 36px rgba(46,125,50,.3)}.c7 h2{margin:0;font-size:24px}.c7 .role{margin:4px 0 16px;font-size:13px;opacity:.9}.c7 .ct{font-size:12px;line-height:1.7}",
     'html': '<div class="c7"><h2>🌿 {{ name }}</h2><div class="role">{{ title }} · {{ company }}</div><div class="ct">{{ email }}<br>{{ phone }}<br>{{ website }}</div></div>'},

    {'title': 'Photographer Black', 'desc': 'Pure black card for photographers.',
     'css': ".c8{width:380px;height:220px;background:#000;color:#fff;padding:30px;font-family:'Helvetica',sans-serif;margin:30px auto;border:2px solid #fff;outline:1px solid #000;outline-offset:-8px}.c8 h2{margin:0;font-size:22px;letter-spacing:2px}.c8 .role{font-size:10px;letter-spacing:4px;text-transform:uppercase;color:#999;margin:6px 0 24px}.c8 .ct{font-size:11px;line-height:1.8;color:#ccc}",
     'html': '<div class="c8"><h2>{{ name }}</h2><div class="role">{{ title }} · {{ company }}</div><div class="ct">{{ email }}<br>{{ phone }}<br>{{ website }}</div></div>'},

    {'title': 'Luxury Black & Gold', 'desc': 'Premium black card with gold borders.',
     'css': ".c9{width:380px;height:220px;background:#1a1a1a;color:#f5c842;padding:30px;font-family:'Playfair Display',Georgia,serif;margin:30px auto;border:2px solid #f5c842;border-radius:6px;box-shadow:0 20px 50px rgba(0,0,0,.4)}.c9 h2{margin:0;font-size:26px;color:#fff}.c9 .role{font-size:11px;letter-spacing:4px;text-transform:uppercase;margin:6px 0 22px}.c9 .ct{font-size:12px;line-height:1.7;color:#ccc;font-family:'Segoe UI',sans-serif}",
     'html': '<div class="c9"><h2>{{ name }}</h2><div class="role">{{ title }} · {{ company }}</div><div class="ct">{{ email }}<br>{{ phone }}<br>{{ website }}</div></div>'},

    {'title': 'Geometric Modern', 'desc': 'Trendy geometric shapes background.',
     'css': ".c10{width:380px;height:220px;background:#fff;color:#222;padding:26px;font-family:'Segoe UI',sans-serif;margin:30px auto;position:relative;overflow:hidden;border-radius:10px;box-shadow:0 12px 30px rgba(0,0,0,.1)}.c10::before{content:'';position:absolute;top:-40px;right:-40px;width:140px;height:140px;background:#7c4dff;border-radius:50%}.c10::after{content:'';position:absolute;bottom:-30px;left:-30px;width:100px;height:100px;background:#ffea00;border-radius:50%}.c10 .inner{position:relative;z-index:2}.c10 h2{margin:0;font-size:24px}.c10 .role{margin:4px 0 16px;color:#7c4dff;font-size:13px;font-weight:600}.c10 .ct{font-size:12px;line-height:1.7;color:#555}",
     'html': '<div class="c10"><div class="inner"><h2>{{ name }}</h2><div class="role">{{ title }} · {{ company }}</div><div class="ct">{{ email }}<br>{{ phone }}<br>{{ website }}</div></div></div>'},

    {'title': 'Vintage Cream', 'desc': 'Retro-style cream card with serif.',
     'css': ".c11{width:380px;height:220px;background:#f5e6c8;color:#3e2723;padding:28px;font-family:Georgia,serif;margin:30px auto;border:3px double #8d6e63;box-shadow:0 14px 30px rgba(141,110,99,.3)}.c11 h2{margin:0;font-size:24px;color:#5d4037}.c11 .role{font-style:italic;color:#8d6e63;margin:6px 0 18px;font-size:13px}.c11 .ct{font-size:12px;line-height:1.7}",
     'html': '<div class="c11"><h2>{{ name }}</h2><div class="role">{{ title }} · {{ company }}</div><div class="ct">{{ email }}<br>{{ phone }}<br>{{ website }}</div></div>'},

    {'title': 'Corporate Navy', 'desc': 'Trustworthy navy corporate card.',
     'css': ".c12{width:380px;height:220px;background:#fff;color:#0d47a1;padding:0;font-family:'Segoe UI',sans-serif;margin:30px auto;border-radius:8px;overflow:hidden;box-shadow:0 14px 30px rgba(13,71,161,.2);display:flex}.c12 .l{width:120px;background:#0d47a1;color:#fff;display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:bold}.c12 .r{flex:1;padding:24px}.c12 h2{margin:0;font-size:22px}.c12 .role{color:#1976d2;font-size:13px;margin:4px 0 14px}.c12 .ct{font-size:12px;color:#555;line-height:1.7}",
     'html': '<div class="c12"><div class="l">{{ name|first }}</div><div class="r"><h2>{{ name }}</h2><div class="role">{{ title }} · {{ company }}</div><div class="ct">{{ email }}<br>{{ phone }}<br>{{ website }}</div></div></div>'},

    {'title': 'Artist Watercolor', 'desc': 'Soft pastel artist card.',
     'css': ".c13{width:380px;height:220px;background:linear-gradient(135deg,#a8edea,#fed6e3);color:#4a148c;padding:26px;font-family:Georgia,serif;margin:30px auto;border-radius:14px;box-shadow:0 14px 36px rgba(168,237,234,.5)}.c13 h2{margin:0;font-size:26px;font-style:italic}.c13 .role{margin:4px 0 16px;font-size:13px;color:#6a1b9a}.c13 .ct{font-size:12px;line-height:1.7;color:#4a148c}",
     'html': '<div class="c13"><h2>{{ name }}</h2><div class="role">{{ title }} · {{ company }}</div><div class="ct">{{ email }}<br>{{ phone }}<br>{{ website }}</div></div>'},

    {'title': 'Doctor Clinical', 'desc': 'Clean medical professional card.',
     'css': ".c14{width:380px;height:220px;background:#fff;color:#006064;padding:0;font-family:'Segoe UI',sans-serif;margin:30px auto;border-radius:10px;overflow:hidden;box-shadow:0 12px 30px rgba(0,96,100,.2);border-top:8px solid #00acc1}.c14 .body{padding:24px}.c14 h2{margin:0;font-size:24px}.c14 .role{color:#00acc1;font-size:13px;margin:4px 0 16px;font-weight:600}.c14 .ct{font-size:12px;line-height:1.7;color:#555}",
     'html': '<div class="c14"><div class="body"><h2>{{ name }}</h2><div class="role">{{ title }} · {{ company }}</div><div class="ct">{{ email }}<br>{{ phone }}<br>{{ website }}<br>{{ address }}</div></div></div>'},

    {'title': 'Real Estate Premium', 'desc': 'Premium card for realtors.',
     'css': ".c15{width:380px;height:220px;background:linear-gradient(135deg,#37474f,#546e7a);color:#fff;padding:26px;font-family:'Segoe UI',sans-serif;margin:30px auto;border-radius:10px;border-bottom:5px solid #ffc107;box-shadow:0 16px 36px rgba(55,71,79,.3)}.c15 h2{margin:0;font-size:24px}.c15 .role{margin:6px 0 16px;color:#ffc107;font-size:13px;text-transform:uppercase;letter-spacing:2px}.c15 .ct{font-size:12px;line-height:1.7;color:#cfd8dc}",
     'html': '<div class="c15"><h2>🏠 {{ name }}</h2><div class="role">{{ title }} · {{ company }}</div><div class="ct">{{ email }}<br>{{ phone }}<br>{{ website }}</div></div>'},
]


# ============================================================
# SOCIAL POST TEMPLATES (15)
# ============================================================
SOCIALS = [
    {'title': 'Sunset Quote', 'desc': 'Inspirational gradient quote post.',
     'css': ".s1{width:440px;height:440px;background:linear-gradient(135deg,#ee0979,#ff6a00);color:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:40px;text-align:center;font-family:'Segoe UI',sans-serif;margin:30px auto;border-radius:18px;box-shadow:0 20px 50px rgba(0,0,0,.2)}.s1 h2{font-size:32px;margin:0 0 14px}.s1 .body{font-size:18px;line-height:1.5;margin-bottom:20px;font-style:italic}.s1 .cta{background:#fff;color:#ee0979;padding:10px 24px;border-radius:30px;font-weight:bold}.s1 .h{position:absolute;bottom:30px;font-size:12px;letter-spacing:2px;opacity:.85}",
     'html': '<div class="s1"><h2>{{ headline }}</h2><div class="body">"{{ body }}"</div><div class="cta">{{ cta }}</div><div class="h">{{ handle }}</div></div>'},

    {'title': 'Sale Promotion', 'desc': 'Bold red sale announcement post.',
     'css': ".s2{width:440px;height:440px;background:#e53935;color:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:40px;text-align:center;font-family:'Segoe UI',sans-serif;margin:30px auto;border-radius:14px;border:4px dashed #fff;box-shadow:0 20px 50px rgba(229,57,53,.4)}.s2 h2{font-size:42px;margin:0;font-weight:900;text-transform:uppercase}.s2 .body{font-size:20px;margin:14px 0;font-weight:600}.s2 .cta{background:#fff;color:#e53935;padding:12px 30px;border-radius:6px;font-weight:bold;font-size:16px;margin-top:10px}.s2 .h{margin-top:24px;font-size:12px;opacity:.85}",
     'html': '<div class="s2"><h2>{{ headline }}</h2><div class="body">{{ body }}</div><div class="cta">{{ cta }}</div><div class="h">{{ handle }}</div></div>'},

    {'title': 'Event Announcement', 'desc': 'Classy event invitation post.',
     'css': ".s3{width:440px;height:440px;background:#1a237e;color:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:40px;text-align:center;font-family:Georgia,serif;margin:30px auto;border:3px solid #ffd54f}.s3 .label{font-size:11px;letter-spacing:6px;color:#ffd54f;margin-bottom:14px}.s3 h2{font-size:36px;margin:0;font-style:italic}.s3 .body{font-size:16px;margin:20px 0;line-height:1.5}.s3 .cta{border:2px solid #ffd54f;color:#ffd54f;padding:10px 26px;letter-spacing:2px;text-transform:uppercase;font-size:13px}.s3 .h{margin-top:20px;font-size:11px;letter-spacing:3px;opacity:.7}",
     'html': '<div class="s3"><div class="label">YOU\'RE INVITED</div><h2>{{ headline }}</h2><div class="body">{{ body }}</div><div class="cta">{{ cta }}</div><div class="h">{{ handle }}</div></div>'},

    {'title': 'Tip Card', 'desc': 'Helpful tip post with green accent.',
     'css': ".s4{width:440px;height:440px;background:#fff;color:#1b5e20;display:flex;flex-direction:column;justify-content:center;padding:50px;font-family:'Segoe UI',sans-serif;margin:30px auto;border-radius:18px;border-left:10px solid #43a047;box-shadow:0 20px 50px rgba(0,0,0,.1)}.s4 .label{font-size:13px;color:#43a047;font-weight:bold;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px}.s4 h2{font-size:32px;margin:0 0 18px;color:#1b5e20}.s4 .body{font-size:16px;line-height:1.6;color:#444}.s4 .h{margin-top:24px;color:#43a047;font-size:13px;font-weight:bold}",
     'html': '<div class="s4"><div class="label">💡 PRO TIP</div><h2>{{ headline }}</h2><div class="body">{{ body }}</div><div class="h">{{ handle }} · {{ cta }}</div></div>'},

    {'title': 'Motivational Dark', 'desc': 'Dark motivational quote post.',
     'css': ".s5{width:440px;height:440px;background:#000;color:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:50px;text-align:center;font-family:'Helvetica',sans-serif;margin:30px auto}.s5 h2{font-size:36px;margin:0 0 20px;font-weight:900;line-height:1.2}.s5 .body{font-size:16px;color:#999;line-height:1.6;font-style:italic}.s5 .line{width:60px;height:3px;background:#ffd600;margin:24px auto}.s5 .h{font-size:11px;letter-spacing:4px;color:#ffd600}",
     'html': '<div class="s5"><h2>{{ headline }}</h2><div class="body">{{ body }}</div><div class="line"></div><div class="h">{{ handle }}</div></div>'},

    {'title': 'Product Launch', 'desc': 'Sleek product reveal post.',
     'css': ".s6{width:440px;height:440px;background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;display:flex;flex-direction:column;justify-content:center;padding:50px;font-family:'Segoe UI',sans-serif;margin:30px auto;border-radius:18px;box-shadow:0 24px 60px rgba(102,126,234,.4)}.s6 .label{font-size:11px;letter-spacing:5px;opacity:.85;margin-bottom:14px}.s6 h2{font-size:38px;margin:0 0 16px;font-weight:800}.s6 .body{font-size:15px;line-height:1.6;opacity:.95}.s6 .cta{background:#fff;color:#667eea;padding:12px 26px;border-radius:30px;font-weight:bold;display:inline-block;margin-top:20px;width:fit-content}.s6 .h{margin-top:auto;padding-top:16px;font-size:11px;opacity:.7;letter-spacing:2px}",
     'html': '<div class="s6"><div class="label">NEW LAUNCH ✨</div><h2>{{ headline }}</h2><div class="body">{{ body }}</div><div class="cta">{{ cta }}</div><div class="h">{{ handle }}</div></div>'},

    {'title': 'Birthday Wish', 'desc': 'Cheerful colorful birthday post.',
     'css': ".s7{width:440px;height:440px;background:linear-gradient(135deg,#f6d365,#fda085);color:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:40px;text-align:center;font-family:'Segoe UI',sans-serif;margin:30px auto;border-radius:18px;box-shadow:0 20px 50px rgba(253,160,133,.4)}.s7 .emoji{font-size:60px;margin-bottom:14px}.s7 h2{font-size:36px;margin:0;font-weight:800;text-shadow:2px 2px 0 rgba(0,0,0,.1)}.s7 .body{font-size:16px;margin:14px 30px;line-height:1.6}.s7 .h{margin-top:18px;font-size:12px;opacity:.9}",
     'html': '<div class="s7"><div class="emoji">🎉</div><h2>{{ headline }}</h2><div class="body">{{ body }}</div><div class="h">{{ handle }}</div></div>'},

    {'title': 'Story Cover', 'desc': '9:16 vertical story cover.',
     'css': ".s8{width:300px;height:530px;background:linear-gradient(180deg,#ff9a8b,#ff6a88,#ff99ac);color:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:30px;text-align:center;font-family:'Segoe UI',sans-serif;margin:20px auto;border-radius:18px;box-shadow:0 18px 40px rgba(0,0,0,.2)}.s8 h2{font-size:32px;margin:0 0 16px;font-weight:800}.s8 .body{font-size:14px;line-height:1.6;margin-bottom:20px}.s8 .cta{background:#fff;color:#ff6a88;padding:10px 22px;border-radius:30px;font-weight:bold;font-size:13px}.s8 .h{position:absolute;bottom:20px;font-size:11px;letter-spacing:2px;opacity:.85}",
     'html': '<div class="s8"><h2>{{ headline }}</h2><div class="body">{{ body }}</div><div class="cta">{{ cta }}</div><div class="h">{{ handle }}</div></div>'},

    {'title': 'Listicle Top 5', 'desc': 'Numbered list-style post.',
     'css': ".s9{width:440px;height:440px;background:#fff;color:#222;padding:40px;font-family:'Segoe UI',sans-serif;margin:30px auto;border-radius:14px;border-top:8px solid #ff5722;box-shadow:0 18px 40px rgba(0,0,0,.1)}.s9 .num{font-size:60px;font-weight:900;color:#ff5722;line-height:1}.s9 h2{font-size:28px;margin:8px 0 16px;font-weight:800}.s9 .body{font-size:15px;line-height:1.6;color:#444}.s9 .h{margin-top:auto;color:#ff5722;font-size:12px;font-weight:bold}",
     'html': '<div class="s9"><div class="num">#1</div><h2>{{ headline }}</h2><div class="body">{{ body }}</div><div class="h">{{ handle }} · {{ cta }}</div></div>'},

    {'title': 'Q&A Card', 'desc': 'Question & answer style post.',
     'css': ".s10{width:440px;height:440px;background:#263238;color:#fff;padding:40px;font-family:'Segoe UI',sans-serif;margin:30px auto;border-radius:14px;display:flex;flex-direction:column;justify-content:center}.s10 .q{color:#4fc3f7;font-size:13px;letter-spacing:3px;text-transform:uppercase;margin-bottom:10px}.s10 h2{font-size:28px;margin:0 0 22px;line-height:1.3}.s10 .a{color:#80cbc4;font-size:13px;letter-spacing:3px;text-transform:uppercase;margin-bottom:10px}.s10 .body{font-size:15px;line-height:1.6;color:#cfd8dc}.s10 .h{margin-top:auto;font-size:11px;letter-spacing:2px;color:#78909c}",
     'html': '<div class="s10"><div class="q">QUESTION</div><h2>{{ headline }}</h2><div class="a">ANSWER</div><div class="body">{{ body }}</div><div class="h">{{ handle }}</div></div>'},

    {'title': 'Behind the Scenes', 'desc': 'Casual BTS-style post.',
     'css': ".s11{width:440px;height:440px;background:#fff8e1;color:#3e2723;padding:40px;font-family:Georgia,serif;margin:30px auto;border-radius:14px;border:2px dashed #ff8f00}.s11 .label{background:#ff8f00;color:#fff;padding:4px 12px;border-radius:20px;font-size:11px;letter-spacing:2px;display:inline-block;margin-bottom:14px}.s11 h2{font-size:32px;margin:0 0 14px;font-style:italic}.s11 .body{font-size:15px;line-height:1.7}.s11 .h{margin-top:20px;color:#ff8f00;font-weight:bold;font-size:13px}",
     'html': '<div class="s11"><div class="label">BEHIND THE SCENES</div><h2>{{ headline }}</h2><div class="body">{{ body }}</div><div class="h">{{ handle }}</div></div>'},

    {'title': 'Testimonial Star', 'desc': '5-star review showcase post.',
     'css': ".s12{width:440px;height:440px;background:#fff;color:#222;padding:40px;font-family:'Segoe UI',sans-serif;margin:30px auto;border-radius:18px;border-bottom:8px solid #ffc107;display:flex;flex-direction:column;justify-content:center;box-shadow:0 18px 40px rgba(0,0,0,.1)}.s12 .stars{color:#ffc107;font-size:32px;margin-bottom:14px}.s12 h2{font-size:24px;margin:0 0 14px;font-style:italic;color:#444;line-height:1.4}.s12 .body{font-size:14px;color:#666;line-height:1.6}.s12 .h{margin-top:18px;font-weight:bold;color:#222}",
     'html': '<div class="s12"><div class="stars">★★★★★</div><h2>"{{ headline }}"</h2><div class="body">{{ body }}</div><div class="h">— {{ handle }}</div></div>'},

    {'title': 'Coming Soon', 'desc': 'Hype-building teaser post.',
     'css': ".s13{width:440px;height:440px;background:#000;color:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:40px;text-align:center;font-family:'Segoe UI',sans-serif;margin:30px auto;border-radius:14px;position:relative;overflow:hidden}.s13::before{content:'';position:absolute;width:300px;height:300px;background:radial-gradient(circle,#f5576c,transparent);top:50%;left:50%;transform:translate(-50%,-50%);opacity:.3}.s13 .label{font-size:11px;letter-spacing:8px;color:#f5576c;margin-bottom:14px;position:relative}.s13 h2{font-size:48px;margin:0;font-weight:900;letter-spacing:2px;position:relative}.s13 .body{font-size:14px;margin-top:18px;color:#aaa;position:relative}.s13 .h{position:absolute;bottom:24px;font-size:11px;letter-spacing:3px;color:#f5576c}",
     'html': '<div class="s13"><div class="label">COMING SOON</div><h2>{{ headline }}</h2><div class="body">{{ body }}</div><div class="h">{{ handle }}</div></div>'},

    {'title': 'Discount Banner', 'desc': 'Eye-catching discount percentage.',
     'css': ".s14{width:440px;height:440px;background:linear-gradient(135deg,#11998e,#38ef7d);color:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:40px;text-align:center;font-family:'Segoe UI',sans-serif;margin:30px auto;border-radius:18px;box-shadow:0 24px 60px rgba(17,153,142,.4)}.s14 .big{font-size:90px;font-weight:900;line-height:1;text-shadow:4px 4px 0 rgba(0,0,0,.15)}.s14 h2{font-size:30px;margin:10px 0 14px;font-weight:800}.s14 .body{font-size:14px;opacity:.95}.s14 .cta{background:#fff;color:#11998e;padding:12px 28px;border-radius:30px;font-weight:bold;margin-top:18px}.s14 .h{margin-top:14px;font-size:11px;opacity:.85}",
     'html': '<div class="s14"><div class="big">50%</div><h2>{{ headline }}</h2><div class="body">{{ body }}</div><div class="cta">{{ cta }}</div><div class="h">{{ handle }}</div></div>'},

    {'title': 'Polaroid Photo', 'desc': 'Polaroid-style photo frame post.',
     'css': ".s15{width:440px;height:440px;background:#f5f5f5;display:flex;justify-content:center;align-items:center;font-family:'Caveat',cursive;margin:30px auto;border-radius:14px}.s15 .frame{background:#fff;padding:20px 20px 60px;box-shadow:0 14px 30px rgba(0,0,0,.2);transform:rotate(-3deg);width:300px;text-align:center;position:relative}.s15 .img{width:100%;height:240px;background:linear-gradient(135deg,#fbc2eb,#a6c1ee);border-radius:4px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:60px;font-family:'Segoe UI',sans-serif}.s15 h2{font-family:'Segoe UI',sans-serif;font-size:18px;margin:14px 0 4px;color:#222}.s15 .body{font-family:'Segoe UI',sans-serif;font-size:11px;color:#666}.s15 .h{position:absolute;bottom:16px;left:0;right:0;font-size:14px;color:#777;font-style:italic;font-family:Georgia,serif}",
     'html': '<div class="s15"><div class="frame"><div class="img">📷</div><h2>{{ headline }}</h2><div class="body">{{ body }}</div><div class="h">~ {{ handle }} ~</div></div></div>'},
]


# ============================================================
# WEDDING INVITATION TEMPLATES (15)
# ============================================================
WEDDINGS = [
    {'title': 'Floral Romance', 'desc': 'Soft floral with elegant serif.',
     'css': ".w1{width:560px;margin:30px auto;padding:50px 40px;background:#fffaf5;border:1px solid #e8d8c4;font-family:Georgia,serif;color:#5a3e2b;text-align:center;box-shadow:0 25px 60px rgba(90,62,43,.18)}.w1::before,.w1::after{content:'❀';font-size:34px;color:#d9a679;display:block;margin:6px 0}.w1 .small{font-size:13px;letter-spacing:6px;text-transform:uppercase;color:#a8825c}.w1 h1{font-size:46px;margin:14px 0;font-style:italic;color:#7a4f2b}.w1 .amp{font-size:38px;color:#d9a679;margin:6px 0}.w1 .msg{font-size:14px;font-style:italic;line-height:1.7;margin:18px 30px;color:#7a5a40}.w1 .info{margin-top:20px;padding-top:18px;border-top:1px solid #e8d8c4;font-size:14px;line-height:1.8}.w1 .info strong{display:block;color:#7a4f2b;font-size:18px;margin-bottom:4px}.w1 .rsvp{margin-top:18px;font-size:12px;letter-spacing:3px;color:#a8825c}",
     'html': '<div class="w1"><div class="small">Save the Date</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br><em>{{ venue|linebreaksbr }}</em></div><div class="rsvp">RSVP · {{ rsvp }}</div></div>'},

    {'title': 'Modern Minimal Wedding', 'desc': 'Clean black border, bold typography.',
     'css': ".w2{width:520px;margin:30px auto;padding:60px 40px;background:#fff;border:2px solid #1a1a1a;font-family:'Helvetica',Arial,sans-serif;color:#1a1a1a;text-align:center}.w2 .label{font-size:11px;letter-spacing:8px;color:#888;margin-bottom:30px}.w2 h1{font-size:54px;margin:0;letter-spacing:6px;font-weight:300}.w2 .and{font-size:18px;font-style:italic;margin:14px 0;color:#888}.w2 .line{width:60px;height:1px;background:#1a1a1a;margin:30px auto}.w2 .date{font-size:20px;letter-spacing:8px;margin:20px 0}.w2 .venue{font-size:13px;letter-spacing:2px;color:#666;text-transform:uppercase}.w2 .msg{font-size:13px;line-height:1.7;margin-top:24px;color:#555;font-style:italic}",
     'html': '<div class="w2"><div class="label">YOU ARE INVITED</div><h1>{{ bride }}</h1><div class="and">and</div><h1>{{ groom }}</h1><div class="line"></div><div class="date">{{ date }}</div><div class="venue">{{ venue }}</div><div class="msg">{{ message }}</div></div>'},

    {'title': 'Royal Indian', 'desc': 'Maroon & gold traditional invite.',
     'css': ".w3{width:560px;margin:30px auto;padding:50px;background:linear-gradient(135deg,#7a0019,#a51c30);color:#fff8e1;font-family:Georgia,serif;text-align:center;border:3px double #f5c842;box-shadow:0 30px 70px rgba(122,0,25,.4)}.w3::before{content:'❈ ❈ ❈';display:block;color:#f5c842;font-size:18px;letter-spacing:14px;margin-bottom:20px}.w3 .blessing{font-style:italic;font-size:15px;color:#f5c842;line-height:1.7;margin-bottom:24px}.w3 h1{font-size:52px;margin:18px 0 8px;color:#fff8e1;font-style:italic;font-weight:400}.w3 .weds{font-size:20px;color:#f5c842;letter-spacing:8px;margin:14px 0}.w3 .info{margin-top:28px;padding-top:20px;border-top:1px solid #f5c84266;font-size:15px;line-height:1.8}.w3 .info strong{color:#f5c842;font-size:18px}",
     'html': '<div class="w3"><div class="blessing">{{ message }}</div><h1>{{ bride }}</h1><div class="weds">WEDS</div><h1>{{ groom }}</h1><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br><br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Beach Sunset', 'desc': 'Tropical beach theme invite.',
     'css': ".w4{width:560px;margin:30px auto;padding:50px;background:linear-gradient(180deg,#fceabb 0%,#f8b500 100%);color:#5d4037;text-align:center;font-family:Georgia,serif;border-radius:20px;box-shadow:0 30px 70px rgba(248,181,0,.3)}.w4 .ico{font-size:50px;margin-bottom:10px}.w4 .small{font-size:12px;letter-spacing:5px;color:#bf360c;text-transform:uppercase}.w4 h1{font-size:44px;margin:14px 0;color:#3e2723;font-style:italic}.w4 .amp{font-size:30px;color:#bf360c}.w4 .msg{font-style:italic;font-size:14px;line-height:1.7;margin:18px 20px}.w4 .info{margin-top:18px;padding-top:18px;border-top:1px dashed #bf360c;font-size:14px}",
     'html': '<div class="w4"><div class="ico">🌊 🌴</div><div class="small">Beach Wedding</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong> · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Rustic Country', 'desc': 'Wood texture rustic wedding invite.',
     'css': ".w5{width:560px;margin:30px auto;padding:50px;background:#f4e4c1;color:#3e2723;text-align:center;font-family:Georgia,serif;border:8px solid #6d4c41;box-shadow:0 24px 50px rgba(109,76,65,.3)}.w5 .small{font-family:'Caveat',cursive;font-size:24px;color:#6d4c41}.w5 h1{font-size:48px;margin:10px 0;color:#3e2723;font-style:italic}.w5 .amp{font-family:'Caveat',cursive;font-size:46px;color:#8d6e63}.w5 .msg{font-size:14px;line-height:1.7;margin:18px 20px;font-style:italic}.w5 .info{margin-top:18px;padding-top:18px;border-top:2px dotted #6d4c41;font-size:14px;line-height:1.8}",
     'html': '<div class="w5"><div class="small">together with their families</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong><br>{{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Vintage Lace', 'desc': 'Delicate vintage lace style.',
     'css': ".w6{width:540px;margin:30px auto;padding:50px;background:#fdf6f0;color:#5d4037;font-family:Georgia,serif;text-align:center;border:1px solid #d7ccc8;position:relative;box-shadow:0 20px 50px rgba(0,0,0,.1)}.w6::before,.w6::after{content:'✥';font-size:30px;color:#bcaaa4;display:block;margin:8px 0}.w6 h1{font-size:42px;margin:14px 0;font-style:italic;color:#4e342e}.w6 .amp{font-size:34px;color:#a1887f}.w6 .small{font-size:12px;letter-spacing:5px;color:#8d6e63;text-transform:uppercase}.w6 .msg{font-size:13px;font-style:italic;line-height:1.8;margin:18px 30px;color:#6d4c41}.w6 .info{font-size:14px;line-height:1.8;border-top:1px solid #d7ccc8;padding-top:18px;margin-top:18px}",
     'html': '<div class="w6"><div class="small">Save the Date</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong> · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Botanical Green', 'desc': 'Fresh green botanical garden invite.',
     'css': ".w7{width:560px;margin:30px auto;padding:50px;background:#f1f8e9;color:#1b5e20;font-family:Georgia,serif;text-align:center;border-top:6px solid #558b2f;border-bottom:6px solid #558b2f;box-shadow:0 20px 50px rgba(85,139,47,.2)}.w7 .ico{font-size:40px;color:#558b2f}.w7 h1{font-size:46px;margin:14px 0;color:#33691e;font-style:italic}.w7 .amp{font-size:34px;color:#7cb342}.w7 .small{font-size:12px;letter-spacing:4px;color:#558b2f;text-transform:uppercase}.w7 .msg{font-size:14px;font-style:italic;line-height:1.7;margin:18px 30px}.w7 .info{margin-top:18px;padding-top:18px;border-top:1px solid #c5e1a5;font-size:14px;line-height:1.8}",
     'html': '<div class="w7"><div class="ico">🌿</div><div class="small">A Garden Wedding</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong> · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Geometric Modern Wedding', 'desc': 'Trendy geometric shapes design.',
     'css': ".w8{width:540px;margin:30px auto;padding:50px;background:#fff;color:#222;font-family:'Segoe UI',sans-serif;text-align:center;position:relative;overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,.12)}.w8::before{content:'';position:absolute;top:0;left:0;width:160px;height:160px;background:#ec407a;clip-path:polygon(0 0,100% 0,0 100%)}.w8::after{content:'';position:absolute;bottom:0;right:0;width:160px;height:160px;background:#5e35b1;clip-path:polygon(100% 0,100% 100%,0 100%)}.w8 .inner{position:relative;z-index:2}.w8 .small{font-size:11px;letter-spacing:6px;color:#888;text-transform:uppercase;margin-bottom:14px}.w8 h1{font-size:42px;margin:6px 0;font-weight:300;letter-spacing:3px}.w8 .amp{font-size:24px;color:#ec407a;margin:8px 0}.w8 .msg{font-size:13px;font-style:italic;color:#666;line-height:1.7;margin:18px 40px}.w8 .info{font-size:14px;line-height:1.8;margin-top:18px}",
     'html': '<div class="w8"><div class="inner"><div class="small">SAVE THE DATE</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong> · {{ time }}<br>{{ venue }}</div></div></div>'},

    {'title': 'Watercolor Pastel', 'desc': 'Dreamy pastel watercolor invite.',
     'css': ".w9{width:560px;margin:30px auto;padding:50px;background:linear-gradient(135deg,#fbc2eb,#a6c1ee);color:#4a148c;text-align:center;font-family:Georgia,serif;border-radius:14px;box-shadow:0 24px 60px rgba(166,193,238,.5)}.w9 h1{font-size:48px;margin:14px 0;font-style:italic;color:#311b92}.w9 .amp{font-size:36px;color:#6a1b9a}.w9 .small{font-size:12px;letter-spacing:5px;text-transform:uppercase;color:#6a1b9a}.w9 .msg{font-size:14px;font-style:italic;line-height:1.7;margin:18px 30px}.w9 .info{margin-top:18px;padding-top:18px;border-top:1px solid rgba(74,20,140,.2);font-size:14px;line-height:1.8}",
     'html': '<div class="w9"><div class="small">Save the Date</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong> · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Black Tie Formal', 'desc': 'Elegant black tie formal invite.',
     'css': ".w10{width:540px;margin:30px auto;padding:60px 40px;background:#000;color:#fff;text-align:center;font-family:'Playfair Display',Georgia,serif;border:1px solid #c9a227;outline:3px solid #000;outline-offset:-12px}.w10 .small{font-size:11px;letter-spacing:8px;color:#c9a227;text-transform:uppercase;margin-bottom:24px}.w10 h1{font-size:48px;margin:10px 0;font-style:italic;font-weight:400}.w10 .amp{font-size:30px;color:#c9a227;margin:8px 0}.w10 .line{width:80px;height:1px;background:#c9a227;margin:24px auto}.w10 .msg{font-size:13px;font-style:italic;color:#bbb;line-height:1.7;margin:0 30px}.w10 .info{margin-top:24px;font-size:14px;line-height:1.8;color:#ddd}.w10 .info strong{color:#c9a227}",
     'html': '<div class="w10"><div class="small">REQUEST THE PLEASURE OF YOUR COMPANY</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="line"></div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong><br>{{ time }} · {{ venue }}</div></div>'},

    {'title': 'Bohemian Earthy', 'desc': 'Boho earth-tones with feathers.',
     'css': ".w11{width:560px;margin:30px auto;padding:50px;background:#efebe9;color:#3e2723;text-align:center;font-family:Georgia,serif;border:double 4px #8d6e63}.w11 .ico{font-size:30px;color:#a1887f;margin-bottom:6px}.w11 h1{font-size:46px;margin:10px 0;font-style:italic;color:#4e342e}.w11 .amp{font-size:32px;color:#8d6e63}.w11 .small{font-size:12px;letter-spacing:5px;text-transform:uppercase;color:#6d4c41}.w11 .msg{font-size:14px;font-style:italic;line-height:1.7;margin:18px 30px;color:#5d4037}.w11 .info{margin-top:18px;padding-top:18px;border-top:1px solid #a1887f;font-size:14px;line-height:1.8}",
     'html': '<div class="w11"><div class="ico">✺ ✺ ✺</div><div class="small">Two Souls, One Heart</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong><br>{{ time }} · {{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Tropical Paradise', 'desc': 'Vibrant tropical leaves design.',
     'css': ".w12{width:560px;margin:30px auto;padding:50px;background:#fff;color:#1b5e20;text-align:center;font-family:Georgia,serif;border:6px solid #2e7d32;border-radius:20px;box-shadow:0 24px 60px rgba(46,125,50,.25);position:relative}.w12::before{content:'🌺 🌴 🌺';display:block;font-size:30px;margin-bottom:10px}.w12 h1{font-size:46px;margin:14px 0;color:#1b5e20;font-style:italic}.w12 .amp{font-size:32px;color:#e91e63}.w12 .small{font-size:11px;letter-spacing:5px;color:#2e7d32;text-transform:uppercase}.w12 .msg{font-size:14px;font-style:italic;line-height:1.7;margin:18px 30px;color:#33691e}.w12 .info{margin-top:18px;padding-top:18px;border-top:2px solid #c5e1a5;font-size:14px;line-height:1.8}",
     'html': '<div class="w12"><div class="small">Tropical Wedding</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong> · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Winter Wonderland', 'desc': 'Icy blue winter wedding invite.',
     'css': ".w13{width:560px;margin:30px auto;padding:50px;background:linear-gradient(135deg,#e0f7fa,#b3e5fc);color:#01579b;text-align:center;font-family:Georgia,serif;border:2px solid #4fc3f7;border-radius:14px;box-shadow:0 24px 60px rgba(79,195,247,.3)}.w13 .ico{font-size:36px;color:#0277bd}.w13 h1{font-size:46px;margin:14px 0;color:#01579b;font-style:italic}.w13 .amp{font-size:32px;color:#0288d1}.w13 .small{font-size:11px;letter-spacing:5px;color:#0277bd;text-transform:uppercase}.w13 .msg{font-size:14px;font-style:italic;line-height:1.7;margin:18px 30px}.w13 .info{margin-top:18px;padding-top:18px;border-top:1px solid #4fc3f7;font-size:14px;line-height:1.8}",
     'html': '<div class="w13"><div class="ico">❄ ❄ ❄</div><div class="small">A Winter Wedding</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong> · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Art Deco Gold', 'desc': '1920s art deco golden invite.',
     'css': ".w14{width:540px;margin:30px auto;padding:60px 40px;background:#1c1c1c;color:#f5c842;text-align:center;font-family:'Playfair Display',Georgia,serif;border:4px double #f5c842;box-shadow:0 30px 70px rgba(0,0,0,.5)}.w14 .ico{font-size:24px;letter-spacing:8px;margin-bottom:14px}.w14 .small{font-size:11px;letter-spacing:8px;text-transform:uppercase}.w14 h1{font-size:48px;margin:14px 0;font-style:italic;color:#fff;letter-spacing:2px}.w14 .amp{font-size:32px;margin:8px 0}.w14 .msg{font-size:13px;font-style:italic;color:#ddd;line-height:1.7;margin:18px 30px}.w14 .info{margin-top:18px;padding-top:18px;border-top:1px solid #f5c842;font-size:14px;line-height:1.8;color:#fff}.w14 .info strong{color:#f5c842}",
     'html': '<div class="w14"><div class="ico">◆ ◆ ◆</div><div class="small">The Honour of Your Presence</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong><br>{{ time }} · {{ venue }}</div></div>'},

    {'title': 'Pastel Dreams', 'desc': 'Soft pastel pink dreamy invite.',
     'css': ".w15{width:560px;margin:30px auto;padding:50px;background:#fff0f5;color:#880e4f;text-align:center;font-family:Georgia,serif;border:1px solid #f8bbd0;border-radius:18px;box-shadow:0 24px 60px rgba(244,143,177,.3)}.w15 .ico{font-size:30px;color:#ec407a}.w15 h1{font-size:46px;margin:14px 0;color:#880e4f;font-style:italic}.w15 .amp{font-size:32px;color:#ec407a}.w15 .small{font-size:11px;letter-spacing:5px;color:#ad1457;text-transform:uppercase}.w15 .msg{font-size:14px;font-style:italic;line-height:1.7;margin:18px 30px;color:#ad1457}.w15 .info{margin-top:18px;padding-top:18px;border-top:1px solid #f8bbd0;font-size:14px;line-height:1.8}",
     'html': '<div class="w15"><div class="ico">♡ ♡ ♡</div><div class="small">Together Forever</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong> · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},
]


# ============================================================
# FESTIVAL SAMPLE PICKER — match title keyword to correct sample
# ============================================================
# Each entry: (keyword, festival_name, greeting, message, sender)
_FESTIVAL_DATA = [
    ('diwali',      'Happy Diwali',         'May this Diwali light up your life',                'Wishing you and your family prosperity, happiness and joy this festival of lights.', 'The Sharma Family'),
    ('holi',        'Happy Holi',           'Let the colors of joy fill your life',              'May this Holi paint your life with happiness, love and laughter.', 'Team Pagecraft'),
    ('christmas',   'Merry Christmas',      'May your days be merry and bright',                 'Wishing you a Christmas filled with warmth, love and wonderful memories.', 'Your Friends'),
    ('onam',        'Happy Onam',           'Wishing you joy, peace & a bountiful Onam',         'May King Mahabali bless your home with happiness and prosperity. Onashamsakal!', 'The Nair Family'),
    ('pongal',      'Happy Pongal',         'May the harvest bring abundance to your life',      'Wishing you a joyous Pongal filled with sweetness, prosperity and family love. Pongalo Pongal!', 'The Iyer Family'),
    ('karva',       'Karva Chauth Mubarak', 'A day of love, devotion and togetherness',          'May the moonlight of Karva Chauth bless your bond with everlasting love and happiness.', 'With Love'),
    ('lohri',       'Happy Lohri',          'Warmth, joy and prosperity to you',                 'May the Lohri bonfire warm your heart and burn away all sorrows. Sundar mundriye ho!', 'The Singh Family'),
    ('bihu',        'Happy Bihu',           'Joy of harvest, music and dance to you',            'May the spirit of Bihu fill your home with happiness, prosperity and the sweet melody of dhol.', 'The Borah Family'),
    ('janmashtami', 'Krishna Janmashtami',  'May Lord Krishna bless your home',                  'On this divine night of Janmashtami, may the blessings of Bal Gopal fill your life with love and joy.', 'Hari Bol'),
    ('krishna',     'Krishna Janmashtami',  'May Lord Krishna bless your home',                  'On this divine night of Janmashtami, may the blessings of Bal Gopal fill your life with love and joy.', 'Hari Bol'),
    ('navratri',    'Happy Navratri',       'May Maa Durga bless you with strength',             'Wishing you nine nights of joy, devotion and divine blessings. Jai Mata Di!', 'The Mehta Family'),
    ('garba',       'Happy Navratri',       'Let\'s dance the night away',                       'May the rhythm of Garba fill your nights with energy, joy and divine grace.', 'The Patel Family'),
    ('dussehra',    'Happy Dussehra',       'Victory of good over evil',                         'May this Dussehra burn away all your worries and bring victory in every walk of life.', 'The Verma Family'),
    ('eid',         'Eid Mubarak',          'Wishing you peace and blessings',                   'May this Eid bring boundless joy, peace and prosperity to your home. Eid Mubarak!', 'The Khan Family'),
    ('ganesh',      'Ganesh Chaturthi',     'Ganpati Bappa Morya!',                              'May Lord Ganesha remove all obstacles and shower his blessings upon you and your family.', 'The Joshi Family'),
    ('raksha',      'Happy Raksha Bandhan', 'A bond beyond words',                               'May this Raksha Bandhan strengthen the beautiful bond of love between brothers and sisters.', 'With Love'),
    ('bandhan',     'Happy Raksha Bandhan', 'A bond beyond words',                               'May this Raksha Bandhan strengthen the beautiful bond of love between brothers and sisters.', 'With Love'),
    ('republic',    'Happy Republic Day',   'Proud to be Indian',                                'Saluting the spirit of our great nation. Jai Hind! Vande Mataram!', 'Team Pagecraft'),
    ('independence','Happy Independence Day','Celebrate freedom',                                 'On this 15th August, let us honour our freedom fighters and salute the tricolour. Jai Hind!', 'Team Pagecraft'),
    ('valentine',   'Happy Valentine\'s Day','You are my forever',                               'Every moment with you feels like a beautiful dream. Happy Valentine\'s Day, my love!', 'With Love'),
    ('mother',      'Happy Mother\'s Day',  'Thank you, Mom',                                    'For all the love, care and sacrifices — you are the reason I am who I am today. Love you, Mom!', 'With Love'),
    ('father',      'Happy Father\'s Day',  'My hero, my dad',                                   'Thank you for being my strength, my guide and my biggest inspiration. Love you, Dad!', 'With Love'),
    ('easter',      'Happy Easter',         'New beginnings, new hope',                          'May this Easter bring you joy, peace and renewed faith. Wishing you and your family blessings.', 'Your Friends'),
    ('new year',    'Happy New Year',       'Cheers to new beginnings',                          'May the coming year be filled with happiness, success and unforgettable moments. Happy New Year!', 'Team Pagecraft'),
    ('thanksgiving','Happy Thanksgiving',   'Grateful for you',                                  'Wishing you a day filled with love, laughter and lots of delicious food. Happy Thanksgiving!', 'Your Friends'),
    ('halloween',   'Happy Halloween',      'Tricks, treats & spooky vibes',                     'Wishing you a fang-tastic night full of treats, scares and unforgettable fun!', 'Your Friends'),
]

def pick_festival_sample(title):
    """Match a festival template title to the correct sample data."""
    t = (title or '').lower()
    for kw, festival, greeting, message, sender in _FESTIVAL_DATA:
        if kw in t:
            return {'festival': festival, 'greeting': greeting, 'message': message, 'sender': sender}
    # Fallback — use Diwali as a safe default
    kw, festival, greeting, message, sender = _FESTIVAL_DATA[0]
    return {'festival': festival, 'greeting': greeting, 'message': message, 'sender': sender}


# ============================================================
# BUILD ALL TEMPLATES
# ============================================================

def build_templates():
    out = []
    for i, t in enumerate(RESUMES):
        out.append({
            'title': t['title'], 'category': 'resume', 'description': t['desc'],
            'fields_schema': RESUME_FIELDS, 'sample_data': R(i),
            'css_layout': t['css'], 'html_layout': t['html'],
        })
    for t in INVOICES:
        out.append({
            'title': t['title'], 'category': 'invoice', 'description': t['desc'],
            'fields_schema': INVOICE_FIELDS, 'sample_data': I(),
            'css_layout': t['css'], 'html_layout': t['html'],
        })
    for i, t in enumerate(CARDS):
        out.append({
            'title': t['title'], 'category': 'card', 'description': t['desc'],
            'fields_schema': CARD_FIELDS, 'sample_data': C(i),
            'css_layout': t['css'], 'html_layout': t['html'],
        })
    for i, t in enumerate(SOCIALS):
        out.append({
            'title': t['title'], 'category': 'social', 'description': t['desc'],
            'fields_schema': SOCIAL_FIELDS, 'sample_data': S(i),
            'css_layout': t['css'], 'html_layout': t['html'],
        })
    for i, t in enumerate(WEDDINGS):
        out.append({
            'title': t['title'], 'category': 'wedding', 'description': t['desc'],
            'fields_schema': WEDDING_FIELDS, 'sample_data': W(i),
            'css_layout': t['css'], 'html_layout': t['html'],
        })

    # ---- Extra categories from _seed_extra & _seed_extra2 ----
    extras = [
        ('certificate',  ex.CERTIFICATES, ex.CERTIFICATE_FIELDS, ex.CERT_SAMPLE),
        ('cover_letter', ex.COVERS,       ex.COVER_FIELDS,       ex.COVER_SAMPLE),
        ('birthday',     ex.BIRTHDAYS,    ex.BIRTHDAY_FIELDS,    ex.BIRTHDAY_SAMPLE),
        ('flyer',        ex2.FLYERS,      ex.FLYER_FIELDS,       ex.FLYER_SAMPLE),
        ('menu',         ex2.MENUS,       ex.MENU_FIELDS,        ex.MENU_SAMPLE),
        ('ticket',       ex2.TICKETS,     ex.TICKET_FIELDS,      ex.TICKET_SAMPLE),
        ('voucher',      ex2.VOUCHERS,    ex.VOUCHER_FIELDS,     ex.VOUCHER_SAMPLE),
    ]
    for cat, lst, fields, sample in extras:
        for t in lst:
            out.append({
                'title': t['title'], 'category': cat, 'description': t['desc'],
                'fields_schema': fields, 'sample_data': dict(sample),
                'css_layout': t['css'], 'html_layout': t['html'],
            })
    # 15 additional pro resumes (with photo, sidebar, skill bars etc.)
    for i, t in enumerate(respro.RESUMES_PRO):
        out.append({
            'title': t['title'], 'category': 'resume', 'description': t['desc'],
            'fields_schema': RESUME_FIELDS, 'sample_data': R(i),
            'css_layout': t['css'], 'html_layout': t['html'],
        })

    # Canva-inspired distinct templates for Birthday / Resume / Cover Letter
    for i, t in enumerate(canvacat.CANVA_BIRTHDAYS):
        out.append({
            'title': t['title'], 'category': 'birthday', 'description': t['desc'],
            'fields_schema': ex.BIRTHDAY_FIELDS, 'sample_data': dict(ex.BIRTHDAY_SAMPLE),
            'css_layout': t['css'], 'html_layout': t['html'],
        })
    for i, t in enumerate(canvacat.CANVA_RESUMES):
        out.append({
            'title': t['title'], 'category': 'resume', 'description': t['desc'],
            'fields_schema': RESUME_FIELDS, 'sample_data': R(i),
            'css_layout': t['css'], 'html_layout': t['html'],
        })
    for i, t in enumerate(canvacat.CANVA_COVERS):
        out.append({
            'title': t['title'], 'category': 'cover_letter', 'description': t['desc'],
            'fields_schema': ex.COVER_FIELDS, 'sample_data': dict(ex.COVER_SAMPLE),
            'css_layout': t['css'], 'html_layout': t['html'],
        })

    # Distinct best 5 templates per remaining category
    distinct_map = [
        ('invoice',     distinct.INVOICES,     INVOICE_FIELDS,           lambda i: dict(INVOICE_SAMPLE)),
        ('voucher',     distinct.VOUCHERS,     ex.VOUCHER_FIELDS,        lambda i: dict(ex.VOUCHER_SAMPLE)),
        ('card',        distinct.CARDS,        CARD_FIELDS,              lambda i: dict(CARD_SAMPLES[i % len(CARD_SAMPLES)])),
        ('certificate', distinct.CERTIFICATES, ex.CERTIFICATE_FIELDS,    lambda i: dict(ex.CERT_SAMPLE)),
        ('social',      distinct.SOCIALS,      SOCIAL_FIELDS,            lambda i: dict(SOCIAL_SAMPLES[i % len(SOCIAL_SAMPLES)])),
        ('flyer',       distinct.FLYERS,       ex.FLYER_FIELDS,          lambda i: dict(ex.FLYER_SAMPLE)),
        ('festival',    distinct.FESTIVALS,    ex.FESTIVAL_FIELDS,       None),  # sample picked by title
        ('menu',        distinct.MENUS,        ex.MENU_FIELDS,           lambda i: dict(ex.MENU_SAMPLE)),
        ('ticket',      distinct.TICKETS,      ex.TICKET_FIELDS,         lambda i: dict(ex.TICKET_SAMPLE)),
    ]
    for cat, lst, fields, sample_fn in distinct_map:
        for i, t in enumerate(lst):
            sample = pick_festival_sample(t['title']) if cat == 'festival' else sample_fn(i)
            out.append({
                'title': t['title'], 'category': cat, 'description': t['desc'],
                'fields_schema': fields, 'sample_data': sample,
                'css_layout': t['css'], 'html_layout': t['html'],
            })

    # Canva-inspired Indian wedding templates
    for t in canva.CANVA_WEDDINGS:
        out.append({
            'title': t['title'], 'category': 'wedding', 'description': t['desc'],
            'fields_schema': WEDDING_FIELDS,
            'sample_data': dict(canva.CANVA_SAMPLES.get(t['sample'], canva.CANVA_SAMPLES['hindu_red'])),
            'css_layout': t['css'], 'html_layout': t['html'],
        })

    # Animated wedding templates (CSS @keyframes — exportable as GIF)
    for t in wedanim.ANIMATED_WEDDINGS:
        out.append({
            'title': t['title'], 'category': 'wedding', 'description': t['desc'],
            'fields_schema': WEDDING_FIELDS,
            'sample_data': dict(wedanim.ANIMATED_SAMPLE),
            'css_layout': t['css'], 'html_layout': t['html'],
        })

    # Religious / regional wedding templates
    for t in wedrel.WEDDINGS_RELIGIOUS:
        if t.get('multi'):
            fields = wedrel.WEDDING_FIELDS_MULTI
            sample = dict(wedrel.GUJARATI_SAMPLE)
        else:
            fields = wedrel.WEDDING_FIELDS_PRO
            sample = dict(wedrel.SAMPLES.get(t['religion'], wedrel.SAMPLES['hindu']))
        out.append({
            'title': t['title'], 'category': 'wedding', 'description': t['desc'],
            'fields_schema': fields, 'sample_data': sample,
            'css_layout': t['css'], 'html_layout': t['html'],
        })

    # ========== ULTRA PREMIUM 💎 (50 luxury templates) ==========
    ultra_map = [
        ('wedding',     ultra.ULTRA_WEDDINGS,     WEDDING_FIELDS, lambda i: W(i)),
        ('resume',      ultra.ULTRA_RESUMES,      RESUME_FIELDS,  lambda i: R(i)),
        ('invoice',     ultra.ULTRA_INVOICES,     INVOICE_FIELDS, lambda i: I()),
        ('card',        ultra.ULTRA_CARDS,        CARD_FIELDS,    lambda i: C(i)),
        ('certificate', ultra.ULTRA_CERTIFICATES, ex.CERTIFICATE_FIELDS, lambda i: dict(ex.CERT_SAMPLE)),
    ]
    for cat, lst, fields, sample_fn in ultra_map:
        for i, t in enumerate(lst):
            out.append({
                'title': t['title'],
                'category': cat,
                'description': '💎 ULTRA PREMIUM · ' + t['desc'],
                'fields_schema': fields,
                'sample_data': sample_fn(i),
                'css_layout': t['css'], 'html_layout': t['html'],
            })

    # ========== PREMIUM (130 templates: 10 per category) ==========
    premium_map = [
        ('resume',       prem.PREMIUM_RESUMES,      RESUME_FIELDS,        lambda i: R(i)),
        ('cover_letter', prem.PREMIUM_COVERS,       ex.COVER_FIELDS,      lambda i: dict(ex.COVER_SAMPLE)),
        ('invoice',      prem.PREMIUM_INVOICES,     INVOICE_FIELDS,       lambda i: I()),
        ('voucher',      prem.PREMIUM_VOUCHERS,     ex.VOUCHER_FIELDS,    lambda i: dict(ex.VOUCHER_SAMPLE)),
        ('card',         prem.PREMIUM_CARDS,        CARD_FIELDS,          lambda i: C(i)),
        ('certificate',  prem.PREMIUM_CERTIFICATES, ex.CERTIFICATE_FIELDS, lambda i: dict(ex.CERT_SAMPLE)),
        ('social',       prem.PREMIUM_SOCIALS,      SOCIAL_FIELDS,        lambda i: S(i)),
        ('flyer',        prem.PREMIUM_FLYERS,       ex.FLYER_FIELDS,      lambda i: dict(ex.FLYER_SAMPLE)),
        ('wedding',      prem.PREMIUM_WEDDINGS,     WEDDING_FIELDS,       lambda i: W(i)),
        ('birthday',     prem.PREMIUM_BIRTHDAYS,    ex.BIRTHDAY_FIELDS,   lambda i: dict(ex.BIRTHDAY_SAMPLE)),
        ('festival',     prem.PREMIUM_FESTIVALS,    ex.FESTIVAL_FIELDS,   lambda i: dict(ex.FESTIVAL_SAMPLES[i % len(ex.FESTIVAL_SAMPLES)])),
        ('menu',         prem.PREMIUM_MENUS,        ex.MENU_FIELDS,       lambda i: dict(ex.MENU_SAMPLE)),
        ('ticket',       prem.PREMIUM_TICKETS,      ex.TICKET_FIELDS,     lambda i: dict(ex.TICKET_SAMPLE)),
    ]
    for cat, lst, fields, sample_fn in premium_map:
        for i, t in enumerate(lst):
            sample = pick_festival_sample(t['title']) if cat == 'festival' else sample_fn(i)
            out.append({
                'title': '✦ ' + t['title'],
                'category': cat,
                'description': '⭐ PREMIUM · ' + t['desc'],
                'fields_schema': fields,
                'sample_data': sample,
                'css_layout': t['css'], 'html_layout': t['html'],
            })

    # Festivals — match sample data by title keyword
    for i, t in enumerate(ex2.FESTIVALS):
        out.append({
            'title': t['title'], 'category': 'festival', 'description': t['desc'],
            'fields_schema': ex.FESTIVAL_FIELDS,
            'sample_data': pick_festival_sample(t['title']),
            'css_layout': t['css'], 'html_layout': t['html'],
        })
    return out


class Command(BaseCommand):
    help = "Seed 15+ professional templates per category."

    def handle(self, *args, **options):
        # Wipe old templates so re-seed always reflects latest designs
        Template.objects.all().delete()
        templates = build_templates()
        for data in templates:
            Template.objects.create(**data)
        from collections import Counter
        counts = Counter(t['category'] for t in templates)
        self.stdout.write(self.style.SUCCESS(
            f"Seeded {len(templates)} templates across {len(counts)} categories: "
            + ', '.join(f"{k}={v}" for k, v in sorted(counts.items()))
        ))
        # Auto-populate SEO/discovery fields after seeding
        from django.core.management import call_command
        call_command('populate_seo', '--force')
