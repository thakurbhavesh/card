"""6 Canva-inspired Indian wedding templates.
Recreations of popular Canva designs with authentic Hindu ornamental style.
Marked with 🎨 prefix.
"""

CANVA_SAMPLES = {
    'hindu_red': {
        'bride': 'Priya', 'groom': 'Arjun',
        'bride_parents': 'Mr. & Mrs. Sharma', 'groom_parents': 'Mr. & Mrs. Kapoor',
        'date': 'Sunday, 22nd November 2026', 'time': '7:00 PM onwards',
        'venue': 'Umaid Bhawan Palace,\nJodhpur, Rajasthan',
        'blessing': '|| श्री गणेशाय नमः ||',
        'message': 'Together with their families, request the honour of your presence at the wedding ceremony of their beloved children.',
        'rsvp': '+91 98765 43210',
    },
    'sangeet': {
        'bride': 'Priya', 'groom': 'Arjun',
        'bride_parents': '', 'groom_parents': '',
        'date': 'Saturday, 21st November 2026', 'time': '7:00 PM onwards',
        'venue': 'The Grand Ballroom,\nLeela Palace, Delhi',
        'blessing': 'Sangeet Night',
        'message': 'A night of music, dance and celebration. Join us as we groove to celebrate the upcoming union!',
        'rsvp': '+91 98765 43210',
    },
    'haldi': {
        'bride': 'Priya', 'groom': 'Arjun',
        'bride_parents': '', 'groom_parents': '',
        'date': 'Sunday, 22nd November 2026', 'time': '10:00 AM',
        'venue': 'Sharma Residence,\nGreen Park, Delhi',
        'blessing': 'Haldi Ceremony',
        'message': 'You are warmly invited to the auspicious Haldi ceremony — please wear yellow!',
        'rsvp': '+91 98765 43210',
    },
    'green': {
        'bride': 'Krisha', 'groom': 'Rohan',
        'bride_parents': 'Mr. & Mrs. Patel', 'groom_parents': 'Mr. & Mrs. Mehta',
        'date': 'Friday, 14th February 2026', 'time': '6:00 PM',
        'venue': 'The Oberoi,\nMumbai',
        'blessing': '|| ॐ श्री गणेशाय नमः ||',
        'message': 'Together with their families, joyfully invite you to bless their union.',
        'rsvp': '+91 98765 43210',
    },
}


CANVA_WEDDINGS = [
    # ===== 1. Generic Hindu — Red/Orange/Yellow Ornamental =====
    {'title': '🎨 Hindu Ornamental Red Gold', 'sample': 'hindu_red',
     'desc': 'Traditional red, orange & gold ornamental Hindu wedding (Canva-inspired).',
     'css': """
.cv1{width:560px;margin:30px auto;background:linear-gradient(180deg,#fff8e7 0%,#fef3c7 100%);color:#7a0019;padding:0;font-family:Georgia,serif;text-align:center;border:8px solid #c62828;box-shadow:0 30px 70px rgba(122,0,25,.4);position:relative;overflow:hidden}
.cv1::before{content:'';position:absolute;inset:8px;border:2px solid #f5c842;pointer-events:none}
.cv1::after{content:'';position:absolute;inset:14px;border:1px dashed #c62828;pointer-events:none;opacity:.5}
.cv1 .top-orn{padding:30px 30px 12px;font-size:34px;color:#c62828;letter-spacing:14px;line-height:1}
.cv1 .ganesh{font-size:48px;color:#bf360c;margin:6px 0}
.cv1 .blessing{font-family:'Cormorant Garamond',Georgia,serif;font-size:18px;color:#bf360c;font-weight:700;font-style:italic;margin:8px 0;letter-spacing:1px}
.cv1 .small{font-size:11px;letter-spacing:8px;color:#c62828;text-transform:uppercase;font-weight:700;margin:14px 0 8px;font-family:'Inter',sans-serif}
.cv1 .body{padding:0 40px 20px}
.cv1 .parents{font-size:13px;color:#bf360c;margin:8px 0;font-style:italic;font-weight:600}
.cv1 h1{font-family:'Playfair Display',Georgia,serif;font-size:46px;margin:10px 0 4px;color:#7a0019;font-style:italic;font-weight:700}
.cv1 .weds{font-size:20px;color:#bf360c;letter-spacing:8px;margin:8px 0;font-weight:700;font-family:'Inter',sans-serif}
.cv1 .msg{font-style:italic;font-size:13px;color:#7a4f1d;margin:14px 30px;line-height:1.7}
.cv1 .info-box{margin:16px 30px 0;padding:14px;background:rgba(245,200,66,.2);border:1px dashed #c62828;border-radius:8px}
.cv1 .info-box strong{color:#bf360c;display:block;font-size:16px;font-family:'Playfair Display',serif;font-style:italic}
.cv1 .info-box .det{font-family:'Inter',sans-serif;font-size:13px;color:#7a4f1d;line-height:1.7;margin-top:4px}
.cv1 .bottom-orn{padding:14px 30px 24px;font-size:30px;color:#c62828;letter-spacing:14px}
.cv1 .corner-tl,.cv1 .corner-tr,.cv1 .corner-bl,.cv1 .corner-br{position:absolute;font-size:30px;color:#bf360c;opacity:.7}
.cv1 .corner-tl{top:18px;left:18px}.cv1 .corner-tr{top:18px;right:18px}
.cv1 .corner-bl{bottom:18px;left:18px}.cv1 .corner-br{bottom:18px;right:18px}
""",
     'html': '<div class="cv1"><div class="corner-tl">❀</div><div class="corner-tr">❀</div><div class="corner-bl">❀</div><div class="corner-br">❀</div><div class="top-orn">🪔 ✦ 🪔</div><div class="ganesh">🕉</div><div class="blessing">{{ blessing }}</div><div class="small">— SHUBH VIVAH —</div><div class="body"><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">~ WEDS ~</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info-box"><strong>{{ date }}</strong><div class="det">{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div></div><div class="bottom-orn">🌺 ✦ 🌺</div></div>'},

    # ===== 2. Sangeet — Dark Red/Pink/Yellow Ornamental =====
    {'title': '🎨 Sangeet Pink Ornamental', 'sample': 'sangeet',
     'desc': 'Dark red, pink & yellow ornamental Sangeet ceremony (Canva-inspired).',
     'css': """
.cv2{width:560px;margin:30px auto;background:linear-gradient(135deg,#fce4ec 0%,#fff8e1 50%,#fce4ec 100%);color:#880e4f;padding:0;font-family:Georgia,serif;text-align:center;border:8px solid #ad1457;box-shadow:0 30px 70px rgba(173,20,87,.4);position:relative;overflow:hidden}
.cv2::before{content:'';position:absolute;inset:8px;border:2px solid #f5c842;pointer-events:none}
.cv2 .top{padding:30px 40px 12px;background:linear-gradient(180deg,rgba(173,20,87,.1),transparent)}
.cv2 .musical{font-size:36px;color:#ad1457;letter-spacing:10px}
.cv2 .label{font-family:'Inter',sans-serif;font-size:11px;letter-spacing:8px;color:#ad1457;text-transform:uppercase;font-weight:700;margin:8px 0}
.cv2 .blessing{font-family:'Playfair Display',Georgia,serif;font-size:42px;margin:14px 0 6px;color:#880e4f;font-style:italic;font-weight:700}
.cv2 .body{padding:0 40px 24px}
.cv2 h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:46px;margin:10px 0 4px;color:#880e4f;font-style:italic;font-weight:600}
.cv2 .amp{font-size:32px;color:#f59e0b;margin:6px 0;font-style:italic;font-family:'Playfair Display',serif}
.cv2 .msg{font-style:italic;font-size:14px;color:#ad1457;margin:14px 30px;line-height:1.7}
.cv2 .info{margin-top:18px;padding-top:14px;border-top:2px dashed #ad1457;font-family:'Inter',sans-serif;font-size:14px;line-height:1.8;color:#880e4f}
.cv2 .info strong{color:#880e4f;display:block;font-size:18px;font-family:'Playfair Display',serif;font-style:italic;font-weight:600}
.cv2 .bottom{padding:14px 30px 24px;font-size:28px;color:#ad1457;letter-spacing:10px}
.cv2 .corner{position:absolute;font-size:28px;color:#f59e0b;opacity:.6}
.cv2 .ctl{top:18px;left:18px}.cv2 .ctr{top:18px;right:18px}
.cv2 .cbl{bottom:18px;left:18px}.cv2 .cbr{bottom:18px;right:18px}
""",
     'html': '<div class="cv2"><div class="corner ctl">✿</div><div class="corner ctr">✿</div><div class="corner cbl">✿</div><div class="corner cbr">✿</div><div class="top"><div class="musical">🎵 💃 🎵</div><div class="label">— A NIGHT OF MUSIC & DANCE —</div></div><div class="body"><div class="blessing">{{ blessing }}</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div><div class="bottom">🪘 ✦ 🪘</div></div>'},

    # ===== 3. Red & Yellow Illustrated Indian (with couple illustration) =====
    {'title': '🎨 Indian Couple Red Yellow', 'sample': 'hindu_red',
     'desc': 'Red & yellow with illustrated bride-groom couple, classic Hindu style (Canva-inspired).',
     'css': """
.cv3{width:560px;margin:30px auto;background:radial-gradient(ellipse at top,#fff8e1 0%,#fef3c7 60%,#fde68a 100%);color:#7a0019;padding:0;font-family:Georgia,serif;text-align:center;border:1px solid #c62828;box-shadow:0 30px 70px rgba(122,0,25,.35);position:relative;overflow:hidden}
.cv3 .arch{position:relative;padding:30px 40px 18px;background:linear-gradient(180deg,#c62828 0%,#bf360c 100%);color:#fff8e1;border-bottom:6px solid #f5c842;border-radius:0 0 280px 280px / 0 0 60px 60px}
.cv3 .arch .ico{font-size:42px;color:#f5c842;line-height:1}
.cv3 .arch .label{font-family:'Inter',sans-serif;font-size:11px;letter-spacing:8px;color:#f5c842;text-transform:uppercase;font-weight:700;margin-top:8px}
.cv3 .arch .blessing{font-family:'Playfair Display',Georgia,serif;font-size:24px;color:#fff8e1;font-style:italic;margin-top:6px;font-weight:600}
.cv3 .body{padding:24px 40px 20px}
.cv3 .parents{font-size:13px;color:#bf360c;margin:6px 0;font-style:italic;font-weight:600}
.cv3 h1{font-family:'Playfair Display',Georgia,serif;font-size:48px;margin:8px 0 4px;color:#7a0019;font-style:italic;font-weight:700}
.cv3 .weds{font-size:18px;color:#bf360c;letter-spacing:8px;margin:6px 0;font-weight:700;font-family:'Inter',sans-serif}
.cv3 .couple{font-size:64px;margin:14px 0;line-height:1}
.cv3 .msg{font-style:italic;font-size:13px;color:#7a4f1d;margin:14px 30px;line-height:1.7}
.cv3 .info{margin-top:14px;padding:14px 20px;background:#fff8e1;border:2px solid #c62828;border-radius:8px;font-family:'Inter',sans-serif;font-size:13px;line-height:1.8;color:#7a0019}
.cv3 .info strong{color:#bf360c;display:block;font-size:16px;font-family:'Playfair Display',serif;font-style:italic}
.cv3 .bottom-pattern{padding:14px 0 20px;font-size:24px;color:#c62828;letter-spacing:10px;background:linear-gradient(180deg,transparent,rgba(245,200,66,.2))}
""",
     'html': '<div class="cv3"><div class="arch"><div class="ico">🕉</div><div class="label">— SHUBH VIVAH —</div><div class="blessing">{{ blessing }}</div></div><div class="body"><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">~ WEDS ~</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="couple">👰🏽‍♀️ 🤵🏽‍♂️</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div><div class="bottom-pattern">🌺 ✦ 🪷 ✦ 🌺</div></div>'},

    # ===== 4. Red & Yellow Traditional Illustrative =====
    {'title': '🎨 Traditional Maroon Yellow', 'sample': 'hindu_red',
     'desc': 'Maroon & yellow traditional illustrative Indian wedding (Canva-inspired).',
     'css': """
.cv4{width:560px;margin:30px auto;background:#fef3c7;color:#7a0019;padding:0;font-family:Georgia,serif;text-align:center;border:6px solid #7a0019;box-shadow:0 30px 70px rgba(122,0,25,.4);position:relative;overflow:hidden}
.cv4::before{content:'';position:absolute;top:6px;left:6px;right:6px;bottom:6px;border:2px solid #f5c842;pointer-events:none}
.cv4::after{content:'';position:absolute;top:14px;left:14px;right:14px;bottom:14px;border:1px solid #7a0019;pointer-events:none;opacity:.4}
.cv4 .header{padding:34px 30px 12px;background:linear-gradient(180deg,#7a0019 0%,#a51c30 100%);color:#fff8e1;margin:14px 14px 0;position:relative;border:1px solid #f5c842}
.cv4 .header::after{content:'';position:absolute;left:0;right:0;bottom:0;height:3px;background:linear-gradient(90deg,#f5c842,#fef3c7,#f5c842)}
.cv4 .header .ico{font-size:36px;color:#f5c842}
.cv4 .header .label{font-family:'Inter',sans-serif;font-size:11px;letter-spacing:8px;color:#f5c842;text-transform:uppercase;font-weight:700;margin-top:6px}
.cv4 .header .blessing{font-family:'Playfair Display',Georgia,serif;font-size:22px;color:#fff8e1;font-style:italic;margin-top:8px;font-weight:600}
.cv4 .body{padding:24px 40px 12px}
.cv4 .parents{font-size:13px;color:#7a0019;margin:6px 0;font-style:italic;font-weight:600}
.cv4 h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:48px;margin:10px 0 4px;color:#7a0019;font-style:italic;font-weight:700}
.cv4 .weds{font-size:20px;color:#bf360c;letter-spacing:6px;margin:8px 0;font-weight:700;font-family:'Inter',sans-serif}
.cv4 .msg{font-style:italic;font-size:13px;color:#7a4f1d;margin:14px 30px;line-height:1.7}
.cv4 .footer{padding:14px 30px 24px;background:linear-gradient(0deg,rgba(122,0,25,.1),transparent)}
.cv4 .info{margin-top:8px;font-family:'Inter',sans-serif;font-size:13px;line-height:1.8;color:#7a0019}
.cv4 .info strong{color:#7a0019;display:block;font-size:16px;font-family:'Playfair Display',serif;font-style:italic;font-weight:700}
.cv4 .deco{font-size:24px;color:#bf360c;letter-spacing:14px;margin:14px 0 8px}
""",
     'html': '<div class="cv4"><div class="header"><div class="ico">🕉</div><div class="label">— TRADITIONAL HINDU WEDDING —</div><div class="blessing">{{ blessing }}</div></div><div class="body"><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">— WEDS —</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div></div><div class="footer"><div class="deco">❦ ❦ ❦</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div></div>'},

    # ===== 5. Green & Gold Illustrated Greeting =====
    {'title': '🎨 Green Gold Botanical', 'sample': 'green',
     'desc': 'Green & gold illustrated botanical wedding greeting (Canva-inspired).',
     'css': """
.cv5{width:560px;margin:30px auto;background:linear-gradient(180deg,#f0fdf4 0%,#dcfce7 100%);color:#14532d;padding:0;font-family:Georgia,serif;text-align:center;border:6px solid #166534;box-shadow:0 30px 70px rgba(22,101,52,.35);position:relative;overflow:hidden}
.cv5::before{content:'';position:absolute;inset:6px;border:2px solid #d4af37;pointer-events:none}
.cv5 .top{padding:30px 30px 12px}
.cv5 .leaves{font-size:36px;color:#166534;letter-spacing:10px}
.cv5 .ganesh{font-size:42px;color:#d4af37;margin:8px 0}
.cv5 .blessing{font-family:'Cormorant Garamond',Georgia,serif;font-size:18px;color:#166534;font-weight:700;font-style:italic;margin:8px 0}
.cv5 .label{font-family:'Inter',sans-serif;font-size:11px;letter-spacing:8px;color:#d4af37;text-transform:uppercase;font-weight:700;margin:8px 0;background:#166534;padding:6px 16px;display:inline-block;border-radius:20px}
.cv5 .body{padding:8px 40px 24px}
.cv5 .parents{font-size:13px;color:#166534;margin:6px 0;font-style:italic;font-weight:600}
.cv5 h1{font-family:'Playfair Display',Georgia,serif;font-size:48px;margin:10px 0 4px;color:#14532d;font-style:italic;font-weight:700}
.cv5 .amp{font-size:36px;color:#d4af37;margin:6px 0;font-style:italic;font-family:'Cormorant Garamond',serif}
.cv5 .msg{font-style:italic;font-size:13px;color:#166534;margin:14px 30px;line-height:1.7}
.cv5 .info{margin:14px 30px 0;padding:14px;background:#fff;border:2px solid #d4af37;border-radius:8px;font-family:'Inter',sans-serif;font-size:13px;line-height:1.8;color:#14532d}
.cv5 .info strong{color:#166534;display:block;font-size:16px;font-family:'Playfair Display',serif;font-style:italic}
.cv5 .bottom-leaves{padding:14px 0 20px;font-size:30px;color:#166534;letter-spacing:14px}
.cv5 .corner{position:absolute;font-size:28px;color:#d4af37;opacity:.7}
.cv5 .ctl{top:14px;left:14px;transform:rotate(-30deg)}
.cv5 .ctr{top:14px;right:14px;transform:rotate(30deg)}
.cv5 .cbl{bottom:14px;left:14px;transform:rotate(-150deg)}
.cv5 .cbr{bottom:14px;right:14px;transform:rotate(150deg)}
""",
     'html': '<div class="cv5"><div class="corner ctl">🌿</div><div class="corner ctr">🌿</div><div class="corner cbl">🌿</div><div class="corner cbr">🌿</div><div class="top"><div class="leaves">🍃 🌿 🍃</div><div class="ganesh">🕉</div><div class="blessing">{{ blessing }}</div><div class="label">SAVE THE DATE</div></div><div class="body"><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div><div class="bottom-leaves">🌿 ✦ 🌿</div></div>'},

    # ===== 6. Haldi Ceremony — Yellow/Red/Orange Ornamental =====
    {'title': '🎨 Haldi Ceremony Bright Yellow', 'sample': 'haldi',
     'desc': 'Bright yellow Haldi ceremony with red ornaments (Canva-inspired).',
     'css': """
.cv6{width:560px;margin:30px auto;background:linear-gradient(180deg,#fef3c7 0%,#fde68a 50%,#fcd34d 100%);color:#7c2d12;padding:0;font-family:Georgia,serif;text-align:center;border:8px solid #f59e0b;box-shadow:0 30px 70px rgba(245,158,11,.5);position:relative;overflow:hidden}
.cv6::before{content:'';position:absolute;inset:8px;border:2px dashed #c62828;pointer-events:none;border-radius:4px}
.cv6 .top{padding:30px 30px 14px}
.cv6 .flowers{font-size:38px;color:#c62828;letter-spacing:10px}
.cv6 .haldi-ico{font-size:50px;margin:10px 0;line-height:1}
.cv6 .blessing{font-family:'Playfair Display',Georgia,serif;font-size:38px;margin:8px 0;color:#7c2d12;font-style:italic;font-weight:700}
.cv6 .label{font-family:'Inter',sans-serif;font-size:11px;letter-spacing:8px;color:#fff;text-transform:uppercase;font-weight:700;margin:8px 0;background:#c62828;padding:8px 22px;display:inline-block;border-radius:20px;box-shadow:0 4px 12px rgba(198,40,40,.4)}
.cv6 .body{padding:8px 40px 20px}
.cv6 h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:46px;margin:10px 0 4px;color:#7c2d12;font-style:italic;font-weight:700}
.cv6 .amp{font-size:32px;color:#c62828;margin:6px 0;font-style:italic;font-family:'Playfair Display',serif}
.cv6 .msg{font-style:italic;font-size:13px;color:#7c2d12;margin:14px 30px;line-height:1.7;font-weight:500}
.cv6 .dress{display:inline-block;padding:6px 18px;background:#7c2d12;color:#fcd34d;font-family:'Inter',sans-serif;font-size:11px;letter-spacing:3px;text-transform:uppercase;font-weight:700;border-radius:4px;margin:10px 0}
.cv6 .info{margin-top:12px;padding:14px 20px;background:rgba(255,255,255,.6);backdrop-filter:blur(4px);border:2px solid #c62828;border-radius:8px;font-family:'Inter',sans-serif;font-size:13px;line-height:1.8;color:#7c2d12}
.cv6 .info strong{color:#c62828;display:block;font-size:16px;font-family:'Playfair Display',serif;font-style:italic}
.cv6 .bottom{padding:14px 30px 22px;font-size:32px;letter-spacing:10px}
""",
     'html': '<div class="cv6"><div class="top"><div class="flowers">🌼 🌻 🌼</div><div class="haldi-ico">✨</div><div class="blessing">{{ blessing }}</div><div class="label">🌼 HALDI CEREMONY 🌼</div></div><div class="body"><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="dress">DRESS CODE: YELLOW</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div><div class="bottom">🌼 ✦ 🌼</div></div>'},
]
