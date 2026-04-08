"""Extra template definitions: 8 new categories x 15 templates each."""

# ============================================================
# SHARED FIELD SCHEMAS
# ============================================================

CERTIFICATE_FIELDS = [
    {'name': 'recipient', 'label': 'Recipient Name', 'type': 'text'},
    {'name': 'course', 'label': 'Course / Achievement', 'type': 'text'},
    {'name': 'date', 'label': 'Date', 'type': 'text'},
    {'name': 'organization', 'label': 'Organization', 'type': 'text'},
    {'name': 'signer', 'label': 'Signed By', 'type': 'text'},
    {'name': 'title', 'label': 'Signer Title', 'type': 'text'},
    {'name': 'description', 'label': 'Description', 'type': 'textarea', 'ai': True},
]
CERT_SAMPLE = {
    'recipient': 'Aarav Sharma', 'course': 'Advanced Python Programming',
    'date': '7th April 2026', 'organization': 'TechAcademy',
    'signer': 'Dr. Priya Verma', 'title': 'Director of Education',
    'description': 'For successfully completing the course with distinction.',
}

COVER_FIELDS = [
    {'name': 'name', 'label': 'Your Name', 'type': 'text'},
    {'name': 'email', 'label': 'Email', 'type': 'email'},
    {'name': 'phone', 'label': 'Phone', 'type': 'text'},
    {'name': 'date', 'label': 'Date', 'type': 'text'},
    {'name': 'company', 'label': 'Company', 'type': 'text'},
    {'name': 'position', 'label': 'Position', 'type': 'text'},
    {'name': 'hiring_manager', 'label': 'Hiring Manager', 'type': 'text'},
    {'name': 'body', 'label': 'Letter Body', 'type': 'textarea', 'ai': True},
]
COVER_SAMPLE = {
    'name': 'Aarav Sharma', 'email': 'aarav@example.com', 'phone': '+91 98765 43210',
    'date': '7 April 2026', 'company': 'Acme Corp', 'position': 'Senior Engineer',
    'hiring_manager': 'Ms. Patel',
    'body': 'I am writing to express my strong interest in the Senior Engineer role at Acme Corp. With 6+ years building scalable systems, I am confident I can contribute meaningfully to your team.\n\nIn my current role, I led a migration that reduced infrastructure costs by 40% and mentored 5 junior engineers. I am excited by Acme\'s mission and would love the opportunity to discuss how I can add value.\n\nThank you for considering my application.',
}

BIRTHDAY_FIELDS = [
    {'name': 'name', 'label': 'Birthday Person', 'type': 'text'},
    {'name': 'age', 'label': 'Age', 'type': 'text'},
    {'name': 'date', 'label': 'Party Date', 'type': 'text'},
    {'name': 'time', 'label': 'Time', 'type': 'text'},
    {'name': 'venue', 'label': 'Venue', 'type': 'text'},
    {'name': 'message', 'label': 'Message', 'type': 'textarea', 'ai': True},
    {'name': 'rsvp', 'label': 'RSVP', 'type': 'text'},
]
BIRTHDAY_SAMPLE = {
    'name': 'Riya', 'age': '7', 'date': 'Saturday, 12th April 2026', 'time': '4:00 PM',
    'venue': 'Sunshine Play Park', 'message': "Come join us for cake, games and lots of fun!",
    'rsvp': '+91 98765 43210',
}

FESTIVAL_FIELDS = [
    {'name': 'festival', 'label': 'Festival Name', 'type': 'text'},
    {'name': 'greeting', 'label': 'Greeting', 'type': 'text', 'ai': True},
    {'name': 'message', 'label': 'Message', 'type': 'textarea', 'ai': True},
    {'name': 'sender', 'label': 'From', 'type': 'text'},
]
FESTIVAL_SAMPLES = [
    {'festival': 'Happy Diwali', 'greeting': 'May this Diwali light up your life',
     'message': 'Wishing you and your family prosperity, happiness and joy this festival of lights.',
     'sender': 'The Sharma Family'},
    {'festival': 'Happy Holi', 'greeting': 'Let the colors of joy fill your life',
     'message': 'May this Holi paint your life with happiness, love and laughter.',
     'sender': 'Team Pagecraft'},
    {'festival': 'Merry Christmas', 'greeting': 'May your days be merry and bright',
     'message': 'Wishing you a Christmas filled with warmth, love and wonderful memories.',
     'sender': 'Your Friends'},
    {'festival': 'Happy Onam', 'greeting': 'Wishing you joy, peace & a bountiful Onam',
     'message': 'May King Mahabali bless your home with happiness and prosperity. Onashamsakal!',
     'sender': 'The Nair Family'},
    {'festival': 'Happy Pongal', 'greeting': 'May the harvest bring abundance to your life',
     'message': 'Wishing you a joyous Pongal filled with sweetness, prosperity and family love. Pongalo Pongal!',
     'sender': 'The Iyer Family'},
    {'festival': 'Karva Chauth Mubarak', 'greeting': 'A day of love, devotion and togetherness',
     'message': 'May the moonlight of Karva Chauth bless your bond with everlasting love and happiness.',
     'sender': 'With Love'},
    {'festival': 'Happy Lohri', 'greeting': 'Warmth, joy and prosperity to you',
     'message': 'May the Lohri bonfire warm your heart and burn away all sorrows. Sundar mundriye!',
     'sender': 'The Singh Family'},
    {'festival': 'Happy Bihu', 'greeting': 'Joy of harvest, music and dance to you',
     'message': 'May the spirit of Bihu fill your home with happiness, prosperity and the sweet melody of dhol.',
     'sender': 'The Borah Family'},
    {'festival': 'Krishna Janmashtami', 'greeting': 'May Lord Krishna bless your home',
     'message': 'On this divine night of Janmashtami, may the blessings of Bal Gopal fill your life with love and joy.',
     'sender': 'Hari Bol'},
]

FLYER_FIELDS = [
    {'name': 'title', 'label': 'Headline', 'type': 'text', 'ai': True},
    {'name': 'subtitle', 'label': 'Subtitle', 'type': 'text'},
    {'name': 'body', 'label': 'Body', 'type': 'textarea', 'ai': True},
    {'name': 'date', 'label': 'Date / When', 'type': 'text'},
    {'name': 'venue', 'label': 'Venue', 'type': 'text'},
    {'name': 'contact', 'label': 'Contact', 'type': 'text'},
]
FLYER_SAMPLE = {
    'title': 'GRAND OPENING', 'subtitle': 'You are invited',
    'body': 'Join us for an unforgettable evening of food, music and celebration. Free entry for all.',
    'date': '20th April 2026 · 6PM', 'venue': 'Main Street, Bangalore',
    'contact': '+91 98765 43210',
}

MENU_FIELDS = [
    {'name': 'restaurant', 'label': 'Restaurant Name', 'type': 'text'},
    {'name': 'tagline', 'label': 'Tagline', 'type': 'text'},
    {'name': 'items', 'label': 'Menu Items', 'type': 'items',
     'item_fields': [
         {'name': 'name', 'label': 'Dish Name', 'placeholder': 'e.g. Butter Chicken'},
         {'name': 'desc', 'label': 'Description', 'placeholder': 'Optional', 'optional': True},
         {'name': 'price', 'label': 'Price', 'placeholder': '₹350'},
     ]},
]
MENU_SAMPLE = {
    'restaurant': 'Spice Garden', 'tagline': 'Authentic Indian Cuisine',
    'items': [
        {'name': 'Butter Chicken', 'desc': 'Creamy tomato curry with tender chicken', 'price': '₹350'},
        {'name': 'Paneer Tikka', 'desc': 'Char-grilled cottage cheese with spices', 'price': '₹280'},
        {'name': 'Dal Makhani', 'desc': 'Slow-cooked black lentils in butter', 'price': '₹240'},
        {'name': 'Garlic Naan', 'desc': 'Fresh tandoor bread with garlic', 'price': '₹60'},
        {'name': 'Biryani Hyderabadi', 'desc': 'Aromatic basmati rice with spices', 'price': '₹380'},
        {'name': 'Gulab Jamun', 'desc': 'Soft milk dumplings in rose syrup', 'price': '₹120'},
    ],
}

TICKET_FIELDS = [
    {'name': 'event', 'label': 'Event Name', 'type': 'text'},
    {'name': 'date', 'label': 'Date', 'type': 'text'},
    {'name': 'time', 'label': 'Time', 'type': 'text'},
    {'name': 'venue', 'label': 'Venue', 'type': 'text'},
    {'name': 'seat', 'label': 'Seat', 'type': 'text'},
    {'name': 'price', 'label': 'Price', 'type': 'text'},
    {'name': 'ticket_no', 'label': 'Ticket #', 'type': 'text'},
]
TICKET_SAMPLE = {
    'event': 'Indie Music Night', 'date': '15 April 2026', 'time': '8:00 PM',
    'venue': 'Hard Rock Cafe, Bangalore', 'seat': 'A-12', 'price': '₹999',
    'ticket_no': 'TKT-20260415-001',
}

VOUCHER_FIELDS = [
    {'name': 'brand', 'label': 'Brand Name', 'type': 'text'},
    {'name': 'amount', 'label': 'Voucher Amount', 'type': 'text'},
    {'name': 'code', 'label': 'Code', 'type': 'text'},
    {'name': 'expiry', 'label': 'Expiry', 'type': 'text'},
    {'name': 'message', 'label': 'Message', 'type': 'textarea', 'ai': True},
]
VOUCHER_SAMPLE = {
    'brand': 'Pagecraft Store', 'amount': '₹1000', 'code': 'GIFT2026',
    'expiry': '31 Dec 2026', 'message': 'A little something special — enjoy!',
}


# ============================================================
# CERTIFICATES (15)
# ============================================================
CERTIFICATES = [
    {'title': 'Classic Gold Border', 'desc': 'Traditional certificate with ornate gold border.',
     'css': ".ce1{width:780px;margin:30px auto;padding:60px;background:#fffaf0;color:#3e2723;text-align:center;font-family:Georgia,serif;border:12px double #c9a227;box-shadow:0 30px 70px rgba(0,0,0,.15)}.ce1 h1{font-size:48px;margin:0;color:#7a4f2b;letter-spacing:6px}.ce1 .sub{font-size:14px;letter-spacing:4px;color:#a8825c;margin:10px 0 30px;text-transform:uppercase}.ce1 .pres{font-size:13px;letter-spacing:2px;color:#666;margin:20px 0 14px}.ce1 .name{font-size:42px;font-style:italic;color:#5d4037;border-bottom:2px solid #c9a227;display:inline-block;padding:0 30px 10px;margin:10px 0}.ce1 .desc{font-size:14px;line-height:1.7;margin:18px 60px;color:#5d4037}.ce1 .course{font-size:22px;font-weight:bold;color:#7a4f2b;margin:14px 0}.ce1 .footer{display:flex;justify-content:space-between;margin-top:50px;font-size:12px;color:#666}.ce1 .footer div{border-top:1px solid #c9a227;padding-top:6px;width:160px}",
     'html': '<div class="ce1"><h1>CERTIFICATE</h1><div class="sub">of Achievement</div><div class="pres">This is to certify that</div><div class="name">{{ recipient }}</div><div class="desc">{{ description }}</div><div class="course">{{ course }}</div><div class="footer"><div>{{ date }}</div><div>{{ signer }}<br><em>{{ title }}</em></div></div></div>'},

    {'title': 'Modern Blue', 'desc': 'Clean modern certificate with blue accents.',
     'css': ".ce2{width:780px;margin:30px auto;padding:60px;background:#fff;text-align:center;font-family:'Segoe UI',sans-serif;border-top:14px solid #1976d2;border-bottom:14px solid #1976d2;box-shadow:0 24px 60px rgba(25,118,210,.2)}.ce2 h1{font-size:42px;margin:0;color:#0d47a1;letter-spacing:4px;font-weight:300}.ce2 .sub{color:#1976d2;letter-spacing:8px;font-size:13px;margin:6px 0 30px}.ce2 .pres{color:#666;font-size:14px;margin:18px 0}.ce2 .name{font-size:40px;color:#0d47a1;font-weight:800;margin:10px 0}.ce2 .desc{font-size:14px;color:#444;line-height:1.7;margin:18px 60px}.ce2 .course{font-size:20px;color:#1976d2;font-weight:bold;margin:14px 0}.ce2 .footer{display:flex;justify-content:space-between;margin-top:40px;font-size:12px;color:#666}.ce2 .footer div{border-top:2px solid #1976d2;padding-top:6px;width:160px}",
     'html': '<div class="ce2"><h1>CERTIFICATE</h1><div class="sub">OF COMPLETION</div><div class="pres">This certificate is proudly presented to</div><div class="name">{{ recipient }}</div><div class="desc">{{ description }}</div><div class="course">{{ course }}</div><div class="footer"><div>{{ date }}</div><div>{{ signer }}<br>{{ title }}</div></div></div>'},

    {'title': 'Elegant Purple', 'desc': 'Royal purple certificate with gold seal.',
     'css': ".ce3{width:780px;margin:30px auto;padding:60px;background:#f3e5f5;text-align:center;font-family:Georgia,serif;border:6px solid #6a1b9a;box-shadow:0 24px 60px rgba(106,27,154,.2)}.ce3 h1{font-size:46px;margin:0;color:#4a148c;letter-spacing:3px}.ce3 .sub{font-size:13px;letter-spacing:6px;color:#6a1b9a;margin:8px 0 28px}.ce3 .pres{color:#666;font-size:14px}.ce3 .name{font-size:42px;color:#4a148c;font-style:italic;margin:14px 0;border-bottom:2px solid #6a1b9a;display:inline-block;padding:0 24px 8px}.ce3 .desc{font-size:14px;line-height:1.7;margin:18px 60px;color:#555}.ce3 .course{font-size:22px;color:#6a1b9a;font-weight:bold}.ce3 .footer{display:flex;justify-content:space-between;margin-top:40px;font-size:12px;color:#666}.ce3 .footer div{border-top:1px solid #6a1b9a;padding-top:6px;width:160px}",
     'html': '<div class="ce3"><h1>CERTIFICATE</h1><div class="sub">OF EXCELLENCE</div><div class="pres">awarded to</div><div class="name">{{ recipient }}</div><div class="desc">{{ description }}</div><div class="course">{{ course }}</div><div class="footer"><div>{{ date }}</div><div>{{ signer }}<br>{{ title }}</div></div></div>'},

    {'title': 'Minimal Black', 'desc': 'Clean black & white minimalist certificate.',
     'css': ".ce4{width:780px;margin:30px auto;padding:70px;background:#fff;text-align:center;font-family:'Helvetica',sans-serif;border:2px solid #000}.ce4 h1{font-size:54px;margin:0;letter-spacing:10px;font-weight:300}.ce4 .sub{font-size:11px;letter-spacing:8px;margin:14px 0 36px;color:#666}.ce4 .pres{font-size:13px;color:#999;letter-spacing:2px;text-transform:uppercase}.ce4 .name{font-size:42px;margin:14px 0;font-weight:300;letter-spacing:2px}.ce4 .line{width:100px;height:1px;background:#000;margin:24px auto}.ce4 .desc{font-size:13px;color:#666;line-height:1.7;margin:18px 80px;font-style:italic}.ce4 .course{font-size:22px;font-weight:bold;margin:14px 0}.ce4 .footer{display:flex;justify-content:space-between;margin-top:50px;font-size:11px;color:#666;letter-spacing:1px}.ce4 .footer div{border-top:1px solid #000;padding-top:6px;width:160px}",
     'html': '<div class="ce4"><h1>CERTIFICATE</h1><div class="sub">OF ACHIEVEMENT</div><div class="pres">PRESENTED TO</div><div class="name">{{ recipient }}</div><div class="line"></div><div class="desc">{{ description }}</div><div class="course">{{ course }}</div><div class="footer"><div>{{ date }}</div><div>{{ signer }}<br>{{ title }}</div></div></div>'},

    {'title': 'Green Botanical', 'desc': 'Fresh green certificate with leaf accents.',
     'css': ".ce5{width:780px;margin:30px auto;padding:60px;background:#f1f8e9;text-align:center;font-family:Georgia,serif;border:4px solid #558b2f;border-radius:12px}.ce5 .ico{font-size:36px;color:#558b2f}.ce5 h1{font-size:46px;margin:10px 0 0;color:#33691e;letter-spacing:3px}.ce5 .sub{font-size:13px;letter-spacing:6px;color:#558b2f;margin:8px 0 28px}.ce5 .pres{color:#666;font-size:14px}.ce5 .name{font-size:40px;color:#33691e;font-style:italic;margin:14px 0}.ce5 .desc{font-size:14px;line-height:1.7;margin:18px 60px;color:#555}.ce5 .course{font-size:22px;color:#558b2f;font-weight:bold}.ce5 .footer{display:flex;justify-content:space-between;margin-top:40px;font-size:12px}.ce5 .footer div{border-top:1px solid #558b2f;padding-top:6px;width:160px}",
     'html': '<div class="ce5"><div class="ico">🌿</div><h1>CERTIFICATE</h1><div class="sub">OF MERIT</div><div class="pres">presented to</div><div class="name">{{ recipient }}</div><div class="desc">{{ description }}</div><div class="course">{{ course }}</div><div class="footer"><div>{{ date }}</div><div>{{ signer }}<br>{{ title }}</div></div></div>'},

    {'title': 'Red Honor', 'desc': 'Bold red certificate of honor.',
     'css': ".ce6{width:780px;margin:30px auto;padding:60px;background:#fff;text-align:center;font-family:Georgia,serif;border:8px solid #c62828;box-shadow:0 24px 60px rgba(198,40,40,.2)}.ce6 h1{font-size:48px;margin:0;color:#b71c1c;letter-spacing:4px}.ce6 .sub{font-size:14px;letter-spacing:5px;color:#c62828;margin:8px 0 28px}.ce6 .pres{color:#666;font-size:14px}.ce6 .name{font-size:42px;color:#b71c1c;font-style:italic;margin:14px 0;border-bottom:3px double #c62828;display:inline-block;padding:0 30px 10px}.ce6 .desc{font-size:14px;line-height:1.7;margin:18px 60px;color:#555}.ce6 .course{font-size:22px;color:#c62828;font-weight:bold}.ce6 .footer{display:flex;justify-content:space-between;margin-top:40px;font-size:12px}.ce6 .footer div{border-top:1px solid #c62828;padding-top:6px;width:160px}",
     'html': '<div class="ce6"><h1>CERTIFICATE</h1><div class="sub">OF HONOR</div><div class="pres">awarded to</div><div class="name">{{ recipient }}</div><div class="desc">{{ description }}</div><div class="course">{{ course }}</div><div class="footer"><div>{{ date }}</div><div>{{ signer }}<br>{{ title }}</div></div></div>'},

    {'title': 'Tech Achievement', 'desc': 'Modern tech-style achievement cert.',
     'css': ".ce7{width:780px;margin:30px auto;padding:50px;background:#0d1117;color:#c9d1d9;text-align:center;font-family:'Segoe UI',sans-serif;border:1px solid #30363d;box-shadow:0 24px 60px rgba(0,0,0,.4)}.ce7 .ico{color:#58a6ff;font-size:30px;letter-spacing:14px}.ce7 h1{font-size:42px;margin:14px 0 0;color:#58a6ff;letter-spacing:4px;font-weight:300}.ce7 .sub{font-size:12px;letter-spacing:8px;color:#7ee787;margin:8px 0 30px}.ce7 .pres{color:#8b949e;font-size:13px}.ce7 .name{font-size:38px;color:#fff;margin:14px 0;font-weight:600}.ce7 .desc{font-size:13px;line-height:1.7;margin:18px 60px;color:#8b949e}.ce7 .course{font-size:20px;color:#f78166;font-weight:bold;background:#161b22;padding:8px 20px;border-radius:6px;display:inline-block;margin:14px 0;border:1px solid #30363d}.ce7 .footer{display:flex;justify-content:space-between;margin-top:40px;font-size:11px;color:#8b949e}.ce7 .footer div{border-top:1px solid #30363d;padding-top:6px;width:160px}",
     'html': '<div class="ce7"><div class="ico">◆ ◆ ◆</div><h1>CERTIFICATE</h1><div class="sub">PROOF OF SKILL</div><div class="pres">issued to</div><div class="name">{{ recipient }}</div><div class="desc">{{ description }}</div><div class="course">{{ course }}</div><div class="footer"><div>{{ date }}</div><div>{{ signer }} · {{ title }}</div></div></div>'},

    {'title': 'Kids Achievement', 'desc': 'Colorful playful kids certificate.',
     'css': ".ce8{width:780px;margin:30px auto;padding:50px;background:linear-gradient(135deg,#fff9c4,#fff176);text-align:center;font-family:'Comic Sans MS','Segoe UI',sans-serif;border:6px dashed #f57f17;border-radius:20px;color:#3e2723}.ce8 .ico{font-size:40px}.ce8 h1{font-size:44px;margin:10px 0;color:#e65100;letter-spacing:2px}.ce8 .sub{color:#f57f17;font-size:14px;margin:0 0 24px}.ce8 .pres{font-size:14px;color:#5d4037}.ce8 .name{font-size:38px;color:#bf360c;margin:10px 0;font-weight:bold}.ce8 .desc{font-size:14px;margin:14px 60px;line-height:1.6}.ce8 .course{font-size:22px;color:#e65100;font-weight:bold;margin:10px 0}.ce8 .footer{display:flex;justify-content:space-between;margin-top:30px;font-size:12px}.ce8 .footer div{border-top:2px dashed #f57f17;padding-top:6px;width:160px}",
     'html': '<div class="ce8"><div class="ico">🌟 🏆 🌟</div><h1>SUPER STAR!</h1><div class="sub">Certificate of Awesomeness</div><div class="pres">This goes to</div><div class="name">{{ recipient }}</div><div class="desc">{{ description }}</div><div class="course">{{ course }}</div><div class="footer"><div>{{ date }}</div><div>{{ signer }}</div></div></div>'},

    {'title': 'Sports Trophy', 'desc': 'Energetic sports victory certificate.',
     'css': ".ce9{width:780px;margin:30px auto;padding:60px;background:#fff;text-align:center;font-family:'Segoe UI',sans-serif;border-top:14px solid #ff6f00;border-bottom:14px solid #212121}.ce9 .ico{font-size:36px;color:#ff6f00}.ce9 h1{font-size:48px;margin:6px 0 0;color:#212121;letter-spacing:4px;font-weight:900}.ce9 .sub{color:#ff6f00;font-size:14px;letter-spacing:6px;margin:6px 0 28px}.ce9 .pres{color:#666;font-size:14px}.ce9 .name{font-size:42px;color:#212121;margin:14px 0;font-weight:800}.ce9 .desc{font-size:14px;line-height:1.7;margin:14px 60px;color:#555}.ce9 .course{font-size:22px;color:#ff6f00;font-weight:bold}.ce9 .footer{display:flex;justify-content:space-between;margin-top:40px;font-size:12px}.ce9 .footer div{border-top:2px solid #ff6f00;padding-top:6px;width:160px}",
     'html': '<div class="ce9"><div class="ico">🏆</div><h1>CHAMPION</h1><div class="sub">CERTIFICATE OF VICTORY</div><div class="pres">awarded to</div><div class="name">{{ recipient }}</div><div class="desc">{{ description }}</div><div class="course">{{ course }}</div><div class="footer"><div>{{ date }}</div><div>{{ signer }}<br>{{ title }}</div></div></div>'},

    {'title': 'Academic Diploma', 'desc': 'Formal academic diploma style.',
     'css': ".ce10{width:780px;margin:30px auto;padding:70px;background:#fefefe;text-align:center;font-family:'Times New Roman',serif;border:1px solid #000;outline:6px double #000;outline-offset:-14px}.ce10 .ico{font-size:30px}.ce10 h1{font-size:38px;margin:14px 0 0;letter-spacing:6px}.ce10 .sub{font-size:13px;letter-spacing:5px;margin:6px 0 30px}.ce10 .pres{font-style:italic;color:#444;font-size:15px}.ce10 .name{font-size:42px;font-style:italic;margin:14px 0}.ce10 .desc{font-size:14px;line-height:1.7;margin:18px 60px;font-style:italic;color:#555}.ce10 .course{font-size:24px;margin:14px 0;font-weight:bold}.ce10 .footer{display:flex;justify-content:space-between;margin-top:50px;font-size:12px}.ce10 .footer div{border-top:1px solid #000;padding-top:6px;width:160px;font-style:italic}",
     'html': '<div class="ce10"><div class="ico">⚜</div><h1>DIPLOMA</h1><div class="sub">CONFERRED UPON</div><div class="pres">By the authority of the institution</div><div class="name">{{ recipient }}</div><div class="desc">{{ description }}</div><div class="course">{{ course }}</div><div class="footer"><div>{{ date }}</div><div>{{ signer }}<br>{{ title }}</div></div></div>'},

    {'title': 'Pink Floral', 'desc': 'Soft pink floral certificate.',
     'css': ".ce11{width:780px;margin:30px auto;padding:60px;background:#fff0f5;text-align:center;font-family:Georgia,serif;border:4px solid #ec407a;border-radius:14px}.ce11 .ico{font-size:30px;color:#ec407a}.ce11 h1{font-size:44px;margin:10px 0 0;color:#880e4f;font-style:italic}.ce11 .sub{font-size:13px;letter-spacing:5px;color:#ad1457;margin:6px 0 28px}.ce11 .pres{font-size:14px;color:#666}.ce11 .name{font-size:42px;color:#880e4f;font-style:italic;margin:14px 0}.ce11 .desc{font-size:14px;line-height:1.7;margin:18px 60px;color:#555}.ce11 .course{font-size:22px;color:#ec407a;font-weight:bold}.ce11 .footer{display:flex;justify-content:space-between;margin-top:40px;font-size:12px}.ce11 .footer div{border-top:1px solid #ec407a;padding-top:6px;width:160px}",
     'html': '<div class="ce11"><div class="ico">❀ ❀ ❀</div><h1>Certificate</h1><div class="sub">OF APPRECIATION</div><div class="pres">presented to</div><div class="name">{{ recipient }}</div><div class="desc">{{ description }}</div><div class="course">{{ course }}</div><div class="footer"><div>{{ date }}</div><div>{{ signer }}</div></div></div>'},

    {'title': 'Corporate Award', 'desc': 'Professional corporate award certificate.',
     'css': ".ce12{width:780px;margin:30px auto;padding:60px;background:#fff;text-align:center;font-family:'Segoe UI',sans-serif;border:1px solid #ddd;box-shadow:0 30px 70px rgba(0,0,0,.1);position:relative}.ce12::before{content:'';position:absolute;top:0;left:0;right:0;height:8px;background:linear-gradient(90deg,#0d47a1,#1976d2,#0d47a1)}.ce12 h1{font-size:42px;margin:14px 0 0;color:#0d47a1;letter-spacing:3px;font-weight:300}.ce12 .sub{font-size:12px;letter-spacing:8px;color:#1976d2;margin:6px 0 30px}.ce12 .pres{color:#666;font-size:13px;letter-spacing:2px;text-transform:uppercase}.ce12 .name{font-size:40px;color:#0d47a1;margin:14px 0;font-weight:600}.ce12 .desc{font-size:14px;line-height:1.7;margin:14px 60px;color:#555}.ce12 .course{font-size:20px;color:#1976d2;font-weight:bold;background:#e3f2fd;display:inline-block;padding:6px 18px;border-radius:4px;margin:14px 0}.ce12 .footer{display:flex;justify-content:space-between;margin-top:40px;font-size:12px}.ce12 .footer div{border-top:1px solid #0d47a1;padding-top:6px;width:160px}",
     'html': '<div class="ce12"><h1>EMPLOYEE OF THE MONTH</h1><div class="sub">CORPORATE EXCELLENCE</div><div class="pres">PROUDLY AWARDED TO</div><div class="name">{{ recipient }}</div><div class="desc">{{ description }}</div><div class="course">{{ course }}</div><div class="footer"><div>{{ date }}</div><div>{{ signer }}<br>{{ title }}</div></div></div>'},

    {'title': 'Vintage Scroll', 'desc': 'Old-world parchment scroll style.',
     'css': ".ce13{width:780px;margin:30px auto;padding:60px;background:#f5e6c8;color:#3e2723;text-align:center;font-family:Georgia,serif;border:8px solid #6d4c41;box-shadow:0 24px 60px rgba(109,76,65,.3)}.ce13 .ico{font-size:30px;color:#6d4c41;letter-spacing:8px}.ce13 h1{font-size:46px;margin:10px 0 0;color:#4e342e;letter-spacing:4px}.ce13 .sub{font-size:13px;letter-spacing:5px;color:#6d4c41;margin:6px 0 28px}.ce13 .pres{font-style:italic;color:#5d4037}.ce13 .name{font-size:42px;font-style:italic;color:#4e342e;margin:14px 0}.ce13 .desc{font-size:14px;line-height:1.7;margin:18px 60px;color:#5d4037;font-style:italic}.ce13 .course{font-size:22px;color:#6d4c41;font-weight:bold}.ce13 .footer{display:flex;justify-content:space-between;margin-top:40px;font-size:12px}.ce13 .footer div{border-top:1px solid #6d4c41;padding-top:6px;width:160px}",
     'html': '<div class="ce13"><div class="ico">⚔</div><h1>CERTIFICATE</h1><div class="sub">OF DISTINCTION</div><div class="pres">Be it known that</div><div class="name">{{ recipient }}</div><div class="desc">{{ description }}</div><div class="course">{{ course }}</div><div class="footer"><div>{{ date }}</div><div>{{ signer }}</div></div></div>'},

    {'title': 'Teal Modern', 'desc': 'Fresh teal certificate design.',
     'css': ".ce14{width:780px;margin:30px auto;padding:60px;background:#fff;text-align:center;font-family:'Segoe UI',sans-serif;border-left:14px solid #00897b;border-right:14px solid #00897b;box-shadow:0 24px 60px rgba(0,137,123,.2)}.ce14 h1{font-size:46px;margin:0;color:#004d40;letter-spacing:4px;font-weight:300}.ce14 .sub{font-size:12px;letter-spacing:8px;color:#00897b;margin:6px 0 30px}.ce14 .pres{color:#666;font-size:14px}.ce14 .name{font-size:42px;color:#004d40;font-weight:bold;margin:14px 0}.ce14 .desc{font-size:14px;line-height:1.7;margin:14px 60px;color:#555}.ce14 .course{font-size:22px;color:#00897b;font-style:italic}.ce14 .footer{display:flex;justify-content:space-between;margin-top:40px;font-size:12px}.ce14 .footer div{border-top:1px solid #00897b;padding-top:6px;width:160px}",
     'html': '<div class="ce14"><h1>CERTIFICATE</h1><div class="sub">OF PARTICIPATION</div><div class="pres">This certificate is awarded to</div><div class="name">{{ recipient }}</div><div class="desc">{{ description }}</div><div class="course">{{ course }}</div><div class="footer"><div>{{ date }}</div><div>{{ signer }}<br>{{ title }}</div></div></div>'},

    {'title': 'Bold Yellow Ribbon', 'desc': 'Eye-catching yellow ribbon design.',
     'css': ".ce15{width:780px;margin:30px auto;padding:60px;background:#fffde7;text-align:center;font-family:'Segoe UI',sans-serif;border:6px solid #f9a825;border-radius:8px;box-shadow:0 24px 60px rgba(249,168,37,.3)}.ce15 .ico{font-size:34px;color:#f57f17}.ce15 h1{font-size:48px;margin:8px 0 0;color:#f57f17;letter-spacing:3px;font-weight:900}.ce15 .sub{font-size:13px;letter-spacing:6px;color:#f9a825;margin:6px 0 28px}.ce15 .pres{color:#666;font-size:14px}.ce15 .name{font-size:42px;color:#bf360c;margin:14px 0;font-weight:bold}.ce15 .desc{font-size:14px;line-height:1.7;margin:14px 60px;color:#5d4037}.ce15 .course{font-size:22px;color:#f57f17;font-weight:bold}.ce15 .footer{display:flex;justify-content:space-between;margin-top:40px;font-size:12px}.ce15 .footer div{border-top:2px solid #f9a825;padding-top:6px;width:160px}",
     'html': '<div class="ce15"><div class="ico">🎖</div><h1>OUTSTANDING</h1><div class="sub">ACHIEVEMENT AWARD</div><div class="pres">presented to</div><div class="name">{{ recipient }}</div><div class="desc">{{ description }}</div><div class="course">{{ course }}</div><div class="footer"><div>{{ date }}</div><div>{{ signer }}</div></div></div>'},
]


# ============================================================
# COVER LETTERS (15)
# ============================================================
COVERS = [
    {'title': 'Modern Minimal', 'desc': 'Clean modern cover letter.',
     'css': ".cl1{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:50px;background:#fff;color:#333;line-height:1.7}.cl1 .top{border-left:5px solid #1976d2;padding-left:14px;margin-bottom:30px}.cl1 h1{font-size:30px;margin:0;color:#0d47a1}.cl1 .ct{color:#666;font-size:13px;margin-top:4px}.cl1 .date{margin:20px 0;font-size:14px;color:#666}.cl1 .to{margin-bottom:20px}.cl1 .body{font-size:15px}.cl1 .sign{margin-top:30px}",
     'html': '<div class="cl1"><div class="top"><h1>{{ name }}</h1><div class="ct">{{ email }} · {{ phone }}</div></div><div class="date">{{ date }}</div><div class="to"><strong>{{ hiring_manager }}</strong><br>{{ company }}</div><div>Re: <strong>{{ position }}</strong></div><br><div class="body">Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}</div><div class="sign">Sincerely,<br><br><strong>{{ name }}</strong></div></div>'},

    {'title': 'Classic Serif', 'desc': 'Traditional serif cover letter.',
     'css': ".cl2{font-family:Georgia,serif;max-width:780px;margin:0 auto;padding:50px;background:#fff;color:#222;line-height:1.7}.cl2 header{text-align:center;border-bottom:2px solid #333;padding-bottom:14px}.cl2 h1{margin:0;font-size:30px}.cl2 .ct{font-size:13px;color:#666;margin-top:4px}.cl2 .date{margin:24px 0;font-size:14px}.cl2 .body{font-size:15px;margin-top:14px}.cl2 .sign{margin-top:30px}",
     'html': '<div class="cl2"><header><h1>{{ name }}</h1><div class="ct">{{ email }} · {{ phone }}</div></header><div class="date">{{ date }}</div><div><strong>{{ hiring_manager }}</strong><br>{{ company }}</div><br><div>Re: <em>{{ position }}</em></div><div class="body">Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}</div><div class="sign">Yours sincerely,<br><br><em>{{ name }}</em></div></div>'},

    {'title': 'Bold Header', 'desc': 'Cover letter with bold header banner.',
     'css': ".cl3{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;background:#fff;color:#333;line-height:1.7}.cl3 .ban{background:#212121;color:#fff;padding:30px 50px}.cl3 .ban h1{margin:0;font-size:32px;letter-spacing:2px}.cl3 .ban .ct{font-size:13px;color:#ffd54f;margin-top:6px}.cl3 .body{padding:30px 50px}.cl3 .body .date{font-size:14px;color:#666;margin-bottom:14px}",
     'html': '<div class="cl3"><div class="ban"><h1>{{ name }}</h1><div class="ct">{{ email }} · {{ phone }}</div></div><div class="body"><div class="date">{{ date }}</div><div><strong>{{ hiring_manager }}</strong><br>{{ company }}</div><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Sincerely,<br><br><strong>{{ name }}</strong></div></div>'},

    {'title': 'Creative Pink', 'desc': 'Pink accent creative cover letter.',
     'css': ".cl4{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:50px;background:#fff;color:#333;line-height:1.7;border-top:8px solid #e91e63}.cl4 h1{font-size:30px;margin:0;color:#ad1457}.cl4 .ct{color:#888;font-size:13px}.cl4 .date{color:#888;margin:20px 0}",
     'html': '<div class="cl4"><h1>{{ name }}</h1><div class="ct">{{ email }} · {{ phone }}</div><div class="date">{{ date }}</div><div><strong>{{ hiring_manager }}</strong><br>{{ company }}</div><br><strong>Re: {{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Warm regards,<br><br><strong>{{ name }}</strong></div>'},

    {'title': 'Tech Dark', 'desc': 'Developer-style dark cover letter.',
     'css': ".cl5{font-family:'Consolas',monospace;max-width:780px;margin:0 auto;padding:50px;background:#0d1117;color:#c9d1d9;line-height:1.7}.cl5 h1{color:#58a6ff;font-size:28px;margin:0}.cl5 .ct{color:#7ee787;font-size:13px}.cl5 .date{color:#8b949e;margin:20px 0}.cl5 strong{color:#fff}",
     'html': '<div class="cl5"><h1>{{ name }}</h1><div class="ct">{{ email }} | {{ phone }}</div><div class="date">// {{ date }}</div><div><strong>{{ hiring_manager }}</strong><br>{{ company }}</div><br><strong>Re: {{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Best,<br><br><strong>{{ name }}</strong></div>'},

    {'title': 'Executive Gold', 'desc': 'Premium gold accent letter.',
     'css': ".cl6{font-family:'Playfair Display',Georgia,serif;max-width:780px;margin:0 auto;padding:50px;background:#fff;color:#222;line-height:1.7;border-top:8px solid #c9a227}.cl6 h1{font-size:34px;margin:0;letter-spacing:2px}.cl6 .ct{color:#c9a227;font-size:13px;letter-spacing:2px;text-transform:uppercase}.cl6 .date{margin:20px 0;font-size:14px}",
     'html': '<div class="cl6"><h1>{{ name }}</h1><div class="ct">{{ email }} · {{ phone }}</div><div class="date">{{ date }}</div><div><strong>{{ hiring_manager }}</strong><br>{{ company }}</div><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Respectfully,<br><br><strong>{{ name }}</strong></div>'},

    {'title': 'Two-Column', 'desc': 'Sidebar contact + letter body.',
     'css': ".cl7{display:flex;font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;background:#fff;line-height:1.7}.cl7 .side{width:220px;background:#2c3e50;color:#ecf0f1;padding:30px 20px}.cl7 .side h1{font-size:22px;margin:0}.cl7 .side .ct{font-size:12px;color:#bdc3c7;margin-top:14px;line-height:1.6}.cl7 .main{flex:1;padding:30px;color:#333;font-size:14px}",
     'html': '<div class="cl7"><div class="side"><h1>{{ name }}</h1><div class="ct">{{ email }}<br>{{ phone }}</div></div><div class="main">{{ date }}<br><br><strong>{{ hiring_manager }}</strong><br>{{ company }}<br><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Sincerely,<br><br><strong>{{ name }}</strong></div></div>'},

    {'title': 'Green Fresh', 'desc': 'Fresh green clean letter.',
     'css': ".cl8{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:50px;background:#fff;color:#333;line-height:1.7;border-left:8px solid #2e7d32}.cl8 h1{font-size:30px;margin:0;color:#1b5e20}.cl8 .ct{color:#666;font-size:13px}.cl8 .date{margin:20px 0;color:#888}",
     'html': '<div class="cl8"><h1>{{ name }}</h1><div class="ct">{{ email }} · {{ phone }}</div><div class="date">{{ date }}</div><div><strong>{{ hiring_manager }}</strong><br>{{ company }}</div><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Best regards,<br><br><strong>{{ name }}</strong></div>'},

    {'title': 'Orange Energetic', 'desc': 'Energetic orange-themed letter.',
     'css': ".cl9{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;background:#fff;color:#333;line-height:1.7}.cl9 .top{background:#ff6f00;color:#fff;padding:30px 50px}.cl9 .top h1{margin:0;font-size:30px}.cl9 .top .ct{font-size:13px;opacity:.95}.cl9 .body{padding:30px 50px}",
     'html': '<div class="cl9"><div class="top"><h1>{{ name }}</h1><div class="ct">{{ email }} · {{ phone }}</div></div><div class="body">{{ date }}<br><br><strong>{{ hiring_manager }}</strong><br>{{ company }}<br><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Cheers,<br><br><strong>{{ name }}</strong></div></div>'},

    {'title': 'Slate Professional', 'desc': 'Slate gray professional style.',
     'css': ".cl10{font-family:Georgia,serif;max-width:780px;margin:0 auto;padding:50px;background:#fff;color:#37474f;line-height:1.7;border:2px solid #37474f}.cl10 h1{font-size:30px;margin:0;letter-spacing:2px}.cl10 .ct{color:#666;font-size:13px}.cl10 .date{margin:20px 0}",
     'html': '<div class="cl10"><h1>{{ name }}</h1><div class="ct">{{ email }} · {{ phone }}</div><div class="date">{{ date }}</div><div><strong>{{ hiring_manager }}</strong><br>{{ company }}</div><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Sincerely,<br><br><strong>{{ name }}</strong></div>'},

    {'title': 'Blue Corporate', 'desc': 'Trustworthy blue corporate letter.',
     'css': ".cl11{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;background:#fff;color:#333;line-height:1.7}.cl11 .top{background:#0d47a1;color:#fff;padding:24px 50px}.cl11 .top h1{margin:0;font-size:28px}.cl11 .top .ct{color:#bbdefb;font-size:13px;margin-top:4px}.cl11 .body{padding:30px 50px}",
     'html': '<div class="cl11"><div class="top"><h1>{{ name }}</h1><div class="ct">{{ email }} · {{ phone }}</div></div><div class="body">{{ date }}<br><br><strong>{{ hiring_manager }}</strong><br>{{ company }}<br><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Sincerely,<br><br><strong>{{ name }}</strong></div></div>'},

    {'title': 'Compact', 'desc': 'Dense one-page compact letter.',
     'css': ".cl12{font-family:'Helvetica',sans-serif;max-width:780px;margin:0 auto;padding:40px;background:#fff;color:#222;font-size:13px;line-height:1.6}.cl12 .hd{display:flex;justify-content:space-between;border-bottom:1px solid #333;padding-bottom:8px}.cl12 h1{margin:0;font-size:24px}.cl12 .ct{font-size:11px;color:#666;text-align:right}",
     'html': '<div class="cl12"><div class="hd"><h1>{{ name }}</h1><div class="ct">{{ email }}<br>{{ phone }}</div></div><br>{{ date }}<br><br><strong>{{ hiring_manager }}</strong>, {{ company }}<br><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Sincerely,<br><br><strong>{{ name }}</strong></div>'},

    {'title': 'Designer Gradient', 'desc': 'Creative gradient header letter.',
     'css': ".cl13{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;background:#fff;color:#333;line-height:1.7}.cl13 .top{background:linear-gradient(135deg,#f093fb,#f5576c);color:#fff;padding:30px 50px}.cl13 .top h1{margin:0;font-size:32px}.cl13 .top .ct{font-size:13px;opacity:.95}.cl13 .body{padding:30px 50px}",
     'html': '<div class="cl13"><div class="top"><h1>{{ name }}</h1><div class="ct">{{ email }} · {{ phone }}</div></div><div class="body">{{ date }}<br><br><strong>{{ hiring_manager }}</strong>, {{ company }}<br><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Warmly,<br><br><strong>{{ name }}</strong></div></div>'},

    {'title': 'Healthcare Teal', 'desc': 'Calm teal medical-style letter.',
     'css': ".cl14{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:50px;background:#fff;color:#333;line-height:1.7;border-top:6px solid #00acc1}.cl14 h1{font-size:30px;margin:0;color:#006064}.cl14 .ct{color:#666;font-size:13px}.cl14 .date{color:#888;margin:20px 0}",
     'html': '<div class="cl14"><h1>{{ name }}</h1><div class="ct">{{ email }} · {{ phone }}</div><div class="date">{{ date }}</div><div><strong>{{ hiring_manager }}</strong><br>{{ company }}</div><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Sincerely,<br><br><strong>{{ name }}</strong></div>'},

    {'title': 'Yellow Bold', 'desc': 'Bold yellow accent cover letter.',
     'css': ".cl15{font-family:'Segoe UI',sans-serif;max-width:780px;margin:0 auto;padding:50px;background:#fff;color:#222;line-height:1.7;border-left:14px solid #ffd600}.cl15 h1{font-size:34px;margin:0}.cl15 .ct{color:#666;font-size:13px}.cl15 .date{margin:20px 0;color:#888}",
     'html': '<div class="cl15"><h1>{{ name }}</h1><div class="ct">{{ email }} · {{ phone }}</div><div class="date">{{ date }}</div><div><strong>{{ hiring_manager }}</strong><br>{{ company }}</div><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Best,<br><br><strong>{{ name }}</strong></div>'},
]


# ============================================================
# BIRTHDAY INVITATIONS (15)
# ============================================================
BIRTHDAYS = [
    {'title': 'Kids Rainbow', 'desc': 'Colorful rainbow kids birthday.',
     'css': ".bd1{width:480px;margin:30px auto;padding:40px;background:linear-gradient(135deg,#ff9a9e,#fad0c4,#fbc2eb,#a18cd1);color:#fff;text-align:center;font-family:'Comic Sans MS','Segoe UI',sans-serif;border-radius:24px;box-shadow:0 24px 60px rgba(0,0,0,.2)}.bd1 .ico{font-size:50px}.bd1 h1{font-size:38px;margin:10px 0;text-shadow:2px 2px 0 rgba(0,0,0,.15)}.bd1 .age{font-size:80px;font-weight:900;margin:10px 0;line-height:1}.bd1 .name{font-size:32px;margin:6px 0}.bd1 .info{margin-top:18px;font-size:15px;line-height:1.7}.bd1 .msg{margin:14px 20px;font-size:13px;font-style:italic}",
     'html': '<div class="bd1"><div class="ico">🎂🎉🎈</div><h1>Birthday Party!</h1><div class="age">{{ age }}</div><div class="name">{{ name }} turns {{ age }}!</div><div class="msg">{{ message }}</div><div class="info">{{ date }}<br>{{ time }}<br>{{ venue }}<br><strong>RSVP:</strong> {{ rsvp }}</div></div>'},

    {'title': 'Sweet Pink', 'desc': 'Sweet pink birthday for girls.',
     'css': ".bd2{width:480px;margin:30px auto;padding:40px;background:#fff0f5;color:#880e4f;text-align:center;font-family:Georgia,serif;border:4px dashed #ec407a;border-radius:18px}.bd2 .ico{font-size:40px}.bd2 h1{font-size:40px;margin:10px 0;font-style:italic}.bd2 .name{font-size:32px;color:#ad1457;margin:8px 0;font-weight:bold}.bd2 .age{font-size:60px;color:#ec407a;font-weight:900}.bd2 .msg{font-size:13px;margin:14px 30px;font-style:italic}.bd2 .info{margin-top:18px;font-size:14px;line-height:1.7;border-top:1px solid #ec407a;padding-top:14px}",
     'html': '<div class="bd2"><div class="ico">🎀 ♡ 🎀</div><h1>Birthday Bash</h1><div class="name">{{ name }}</div><div class="age">turns {{ age }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong> · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Cool Boys Blue', 'desc': 'Cool blue birthday for boys.',
     'css': ".bd3{width:480px;margin:30px auto;padding:40px;background:linear-gradient(135deg,#1976d2,#42a5f5);color:#fff;text-align:center;font-family:'Segoe UI',sans-serif;border-radius:18px;box-shadow:0 24px 60px rgba(25,118,210,.4)}.bd3 .ico{font-size:50px}.bd3 h1{font-size:42px;margin:10px 0;font-weight:900;text-shadow:2px 2px 0 rgba(0,0,0,.2)}.bd3 .age{font-size:90px;font-weight:900;line-height:1}.bd3 .name{font-size:24px;margin:6px 0}.bd3 .info{margin-top:18px;font-size:15px;line-height:1.7;background:rgba(0,0,0,.15);padding:14px;border-radius:10px}",
     'html': '<div class="bd3"><div class="ico">⚽ 🎮 🎂</div><h1>BIRTHDAY BLAST!</h1><div class="age">{{ age }}</div><div class="name">{{ name }} is turning {{ age }}!</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Elegant Adult', 'desc': 'Sophisticated adult birthday invite.',
     'css': ".bd4{width:480px;margin:30px auto;padding:50px 40px;background:#fff;color:#222;text-align:center;font-family:'Playfair Display',Georgia,serif;border:1px solid #c9a227;outline:3px solid #fff;outline-offset:-10px;box-shadow:0 24px 60px rgba(0,0,0,.15)}.bd4 .small{font-size:11px;letter-spacing:6px;color:#c9a227;text-transform:uppercase}.bd4 h1{font-size:38px;margin:14px 0;font-style:italic}.bd4 .name{font-size:42px;margin:6px 0;color:#c9a227}.bd4 .msg{font-size:13px;font-style:italic;color:#666;margin:14px 20px}.bd4 .info{margin-top:18px;padding-top:14px;border-top:1px solid #c9a227;font-size:14px;line-height:1.7}",
     'html': '<div class="bd4"><div class="small">PLEASE JOIN US FOR</div><h1>A Birthday Celebration</h1><div class="name">{{ name }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong> · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Tropical Party', 'desc': 'Tropical theme birthday.',
     'css': ".bd5{width:480px;margin:30px auto;padding:40px;background:linear-gradient(135deg,#11998e,#38ef7d);color:#fff;text-align:center;font-family:'Segoe UI',sans-serif;border-radius:18px;box-shadow:0 24px 60px rgba(17,153,142,.4)}.bd5 .ico{font-size:46px}.bd5 h1{font-size:38px;margin:10px 0;font-weight:900}.bd5 .name{font-size:30px;margin:6px 0}.bd5 .age{font-size:60px;font-weight:900}.bd5 .info{margin-top:18px;font-size:15px;line-height:1.7;background:rgba(0,0,0,.15);padding:14px;border-radius:10px}",
     'html': '<div class="bd5"><div class="ico">🌺 🍹 🌴</div><h1>Tropical Birthday</h1><div class="name">{{ name }}</div><div class="age">{{ age }}</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Unicorn Magic', 'desc': 'Magical unicorn birthday.',
     'css': ".bd6{width:480px;margin:30px auto;padding:40px;background:linear-gradient(135deg,#fbc2eb,#a6c1ee);color:#4a148c;text-align:center;font-family:Georgia,serif;border-radius:24px;box-shadow:0 24px 60px rgba(166,193,238,.5)}.bd6 .ico{font-size:50px}.bd6 h1{font-size:38px;margin:8px 0;font-style:italic}.bd6 .name{font-size:34px;color:#6a1b9a;margin:6px 0;font-weight:bold}.bd6 .age{font-size:60px;color:#ec407a}.bd6 .info{margin-top:18px;font-size:14px;line-height:1.7}",
     'html': '<div class="bd6"><div class="ico">🦄 ✨ 🌈</div><h1>Magical Birthday</h1><div class="name">{{ name }}</div><div class="age">turns {{ age }}</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Surprise Party', 'desc': 'Surprise party invite.',
     'css': ".bd7{width:480px;margin:30px auto;padding:40px;background:#212121;color:#ffd600;text-align:center;font-family:'Segoe UI',sans-serif;border:4px solid #ffd600;border-radius:14px}.bd7 .small{font-size:11px;letter-spacing:6px;color:#ffd600}.bd7 h1{font-size:48px;margin:8px 0;font-weight:900;color:#fff}.bd7 .name{font-size:30px;margin:6px 0}.bd7 .msg{color:#fff;font-style:italic;margin:14px 20px;font-size:13px}.bd7 .info{margin-top:18px;font-size:14px;line-height:1.7;color:#fff}",
     'html': '<div class="bd7"><div class="small">SHHH... ITS A</div><h1>SURPRISE!</h1><div class="name">For {{ name }}\'s {{ age }}th</div><div class="msg">{{ message }}</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Watercolor Pastel', 'desc': 'Soft watercolor pastel birthday.',
     'css': ".bd8{width:480px;margin:30px auto;padding:40px;background:linear-gradient(135deg,#fad0c4,#ffd1ff);color:#4a148c;text-align:center;font-family:Georgia,serif;border-radius:18px}.bd8 h1{font-size:38px;margin:14px 0;font-style:italic}.bd8 .name{font-size:34px;color:#880e4f;margin:6px 0}.bd8 .age{font-size:54px;color:#ec407a;font-weight:bold}.bd8 .info{margin-top:18px;font-size:14px;line-height:1.7;border-top:1px solid #ec407a;padding-top:14px}",
     'html': '<div class="bd8"><h1>Birthday Wishes</h1><div class="name">{{ name }}</div><div class="age">{{ age }}</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Confetti Pop', 'desc': 'Confetti explosion birthday.',
     'css': ".bd9{width:480px;margin:30px auto;padding:40px;background:#fff;color:#222;text-align:center;font-family:'Segoe UI',sans-serif;border-radius:18px;border:6px dotted #e91e63;box-shadow:0 24px 60px rgba(233,30,99,.2)}.bd9 .ico{font-size:46px}.bd9 h1{font-size:42px;margin:8px 0;color:#ad1457;font-weight:900}.bd9 .name{font-size:30px;color:#222;margin:6px 0}.bd9 .age{font-size:60px;color:#e91e63;font-weight:900}.bd9 .info{margin-top:18px;font-size:14px;line-height:1.7;background:#fce4ec;padding:14px;border-radius:10px}",
     'html': '<div class="bd9"><div class="ico">🎊 🎉 🎊</div><h1>Lets Celebrate!</h1><div class="name">{{ name }}</div><div class="age">{{ age }}</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Vintage Floral', 'desc': 'Vintage floral birthday invite.',
     'css': ".bd10{width:480px;margin:30px auto;padding:50px 40px;background:#fffaf3;color:#5d4037;text-align:center;font-family:Georgia,serif;border:1px solid #d7ccc8;box-shadow:0 24px 60px rgba(0,0,0,.1)}.bd10 .ico{font-size:30px;color:#8d6e63}.bd10 h1{font-size:36px;font-style:italic;margin:8px 0}.bd10 .name{font-size:34px;color:#4e342e;margin:6px 0}.bd10 .age{font-size:50px;color:#8d6e63;font-weight:bold}.bd10 .info{margin-top:18px;font-size:14px;line-height:1.7;border-top:1px solid #d7ccc8;padding-top:14px}",
     'html': '<div class="bd10"><div class="ico">❀ ❀ ❀</div><h1>Birthday Tea Party</h1><div class="name">{{ name }}</div><div class="age">{{ age }}</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Glow Neon', 'desc': 'Neon glow party invite.',
     'css': ".bd11{width:480px;margin:30px auto;padding:40px;background:#000;color:#00ffea;text-align:center;font-family:'Segoe UI',sans-serif;border:3px solid #00ffea;border-radius:14px;box-shadow:0 0 40px #00ffea}.bd11 h1{font-size:44px;margin:8px 0;color:#fff;text-shadow:0 0 14px #00ffea;font-weight:900}.bd11 .name{font-size:30px;color:#ff00ff;text-shadow:0 0 10px #ff00ff;margin:6px 0}.bd11 .age{font-size:60px;color:#00ffea;text-shadow:0 0 14px #00ffea}.bd11 .info{margin-top:18px;font-size:14px;line-height:1.7;color:#fff}",
     'html': '<div class="bd11"><h1>NEON PARTY</h1><div class="name">{{ name }}</div><div class="age">{{ age }}</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Safari Adventure', 'desc': 'Wild safari themed birthday.',
     'css': ".bd12{width:480px;margin:30px auto;padding:40px;background:#fff8e1;color:#5d4037;text-align:center;font-family:Georgia,serif;border:6px solid #ff8f00;border-radius:14px}.bd12 .ico{font-size:50px}.bd12 h1{font-size:38px;color:#bf360c;margin:8px 0;font-weight:bold}.bd12 .name{font-size:30px;color:#5d4037;margin:6px 0}.bd12 .age{font-size:54px;color:#ff8f00;font-weight:bold}.bd12 .info{margin-top:18px;font-size:14px;line-height:1.7}",
     'html': '<div class="bd12"><div class="ico">🦁 🐘 🦓</div><h1>Safari Birthday</h1><div class="name">{{ name }}</div><div class="age">{{ age }}</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Princess Crown', 'desc': 'Royal princess birthday.',
     'css': ".bd13{width:480px;margin:30px auto;padding:40px;background:linear-gradient(135deg,#fce4ec,#f8bbd0);color:#880e4f;text-align:center;font-family:Georgia,serif;border:4px solid #f5c842;border-radius:18px}.bd13 .ico{font-size:46px}.bd13 h1{font-size:38px;margin:8px 0;font-style:italic;color:#ad1457}.bd13 .name{font-size:32px;color:#880e4f;margin:6px 0;font-weight:bold}.bd13 .age{font-size:54px;color:#f5c842;font-weight:bold}.bd13 .info{margin-top:18px;font-size:14px;line-height:1.7}",
     'html': '<div class="bd13"><div class="ico">👑 ✨ 👑</div><h1>Princess Party</h1><div class="name">{{ name }}</div><div class="age">{{ age }}</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Black & Gold', 'desc': 'Sleek black & gold milestone.',
     'css': ".bd14{width:480px;margin:30px auto;padding:50px 40px;background:#000;color:#f5c842;text-align:center;font-family:'Playfair Display',Georgia,serif;border:2px solid #f5c842;outline:6px solid #000;outline-offset:-10px}.bd14 .small{font-size:11px;letter-spacing:6px;color:#f5c842}.bd14 h1{font-size:42px;margin:14px 0;color:#fff;font-style:italic}.bd14 .age{font-size:80px;font-weight:900;color:#f5c842;line-height:1}.bd14 .name{font-size:24px;color:#fff;margin:6px 0}.bd14 .info{margin-top:18px;padding-top:14px;border-top:1px solid #f5c842;font-size:14px;line-height:1.7;color:#fff}",
     'html': '<div class="bd14"><div class="small">CELEBRATING</div><h1>Birthday</h1><div class="age">{{ age }}</div><div class="name">{{ name }}</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Balloon Burst', 'desc': 'Bright balloon celebration.',
     'css': ".bd15{width:480px;margin:30px auto;padding:40px;background:#fff;color:#222;text-align:center;font-family:'Segoe UI',sans-serif;border-radius:18px;box-shadow:0 24px 60px rgba(0,0,0,.15)}.bd15 .ico{font-size:50px}.bd15 h1{font-size:38px;margin:8px 0;color:#e91e63;font-weight:900}.bd15 .name{font-size:30px;margin:6px 0}.bd15 .age{font-size:60px;color:#1976d2;font-weight:900}.bd15 .info{margin-top:18px;font-size:14px;line-height:1.7;background:#fce4ec;padding:14px;border-radius:10px}",
     'html': '<div class="bd15"><div class="ico">🎈 🎈 🎈</div><h1>Birthday Party</h1><div class="name">{{ name }}</div><div class="age">{{ age }}</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},
]
