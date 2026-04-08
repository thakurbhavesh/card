"""Canva-inspired premium templates for Birthday, Resume, Cover Letter.
Each design is visually DISTINCT — different palettes, layouts, decorative styles.
Marked with 🎨 prefix.
"""

# ============================================================
# BIRTHDAY — 6 DISTINCT CANVA-INSPIRED DESIGNS
# ============================================================
CANVA_BIRTHDAYS = [
    # 1. Kids Rainbow Confetti
    {'title': '🎨 Rainbow Kids Confetti', 'desc': 'Bright rainbow with falling confetti and cartoon balloons.',
     'css': """
.cb1{width:480px;margin:30px auto;background:linear-gradient(135deg,#fef3c7 0%,#fce7f3 50%,#dbeafe 100%);color:#7c2d12;padding:0;font-family:'Comic Sans MS','Segoe UI',sans-serif;text-align:center;border:6px dashed #ec4899;border-radius:24px;box-shadow:0 30px 70px rgba(236,72,153,.4);position:relative;overflow:hidden}
.cb1::before{content:'🎉 🎊 ⭐ 🎈 ✨ 🎉 🎊 ⭐ 🎈 ✨';position:absolute;top:8px;left:0;right:0;font-size:18px;letter-spacing:6px;opacity:.4}
.cb1::after{content:'⭐ ✨ 🎊 🎉 ⭐ ✨ 🎊 🎉';position:absolute;bottom:8px;left:0;right:0;font-size:18px;letter-spacing:6px;opacity:.4}
.cb1 .body{padding:50px 30px 50px;position:relative}
.cb1 .balloons{font-size:60px;line-height:1;letter-spacing:6px}
.cb1 h1{font-size:44px;color:#ec4899;margin:14px 0 6px;text-shadow:3px 3px 0 #fff,5px 5px 0 rgba(236,72,153,.3);font-weight:900;-webkit-text-stroke:2px #fff}
.cb1 .age-circle{width:130px;height:130px;border-radius:50%;background:linear-gradient(135deg,#fbbf24,#f59e0b);color:#fff;display:flex;align-items:center;justify-content:center;font-size:74px;font-weight:900;margin:14px auto;box-shadow:0 14px 30px rgba(245,158,11,.4),inset 0 -8px 20px rgba(0,0,0,.15);border:6px solid #fff;text-shadow:2px 2px 0 rgba(0,0,0,.2)}
.cb1 .name{font-size:36px;color:#7c2d12;font-weight:900;margin:10px 0;text-shadow:2px 2px 0 #fff}
.cb1 .info{margin-top:18px;background:#fff;border:3px dashed #ec4899;border-radius:14px;padding:14px;font-size:14px;line-height:1.7;color:#7c2d12;font-weight:700}
""",
     'html': '<div class="cb1"><div class="body"><div class="balloons">🎈 🎂 🎈</div><h1>BIRTHDAY PARTY!</h1><div class="age-circle">{{ age }}</div><div class="name">{{ name }}</div><div class="info">📅 {{ date }} · {{ time }}<br>📍 {{ venue }}<br>📞 {{ rsvp }}</div></div></div>'},

    # 2. Elegant Black & Gold Adult
    {'title': '🎨 Elegant Black Gold Soiree', 'desc': 'Sophisticated black & gold milestone birthday.',
     'css': """
.cb2{width:480px;margin:30px auto;background:radial-gradient(ellipse at top,#1c1917 0%,#0a0a0a 100%);color:#fff;padding:60px 40px;font-family:'Playfair Display',Georgia,serif;text-align:center;border:1px solid #d4af37;outline:6px solid #0a0a0a;outline-offset:-12px;box-shadow:0 40px 80px rgba(0,0,0,.6),inset 0 0 80px rgba(212,175,55,.05);position:relative}
.cb2::before{content:'';position:absolute;inset:14px;border:1px solid rgba(212,175,55,.4);pointer-events:none}
.cb2 .ornament{font-size:24px;color:#d4af37;letter-spacing:14px}
.cb2 .small{font-family:'Inter',sans-serif;font-size:11px;letter-spacing:8px;color:#d4af37;text-transform:uppercase;font-weight:700;margin:14px 0}
.cb2 h1{font-size:42px;margin:14px 0 6px;color:#fff;font-style:italic;font-weight:300;letter-spacing:3px}
.cb2 .age{font-size:120px;color:#d4af37;font-weight:200;line-height:.9;margin:10px 0;text-shadow:0 4px 30px rgba(212,175,55,.4)}
.cb2 .name{font-family:'Cormorant Garamond',serif;font-size:32px;color:#d4af37;font-style:italic;margin:14px 0;font-weight:500}
.cb2 .msg{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:15px;color:#a3a3a3;margin:14px 30px;line-height:1.7}
.cb2 .info{font-family:'Inter',sans-serif;margin-top:18px;padding-top:14px;border-top:1px solid #d4af37;font-size:12px;color:#cbcbcb;line-height:1.9;letter-spacing:1px}
""",
     'html': '<div class="cb2"><div class="ornament">❦ ❦ ❦</div><div class="small">— A PRIVATE CELEBRATION —</div><h1>Birthday</h1><div class="age">{{ age }}</div><div class="name">{{ name }}</div><div class="msg">{{ message }}</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>RSVP: {{ rsvp }}</div></div>'},

    # 3. Watercolor Floral Sweet
    {'title': '🎨 Watercolor Pink Floral', 'desc': 'Soft watercolor pink with floral splashes.',
     'css': """
.cb3{width:480px;margin:30px auto;background:linear-gradient(135deg,#fce7f3 0%,#fdf2f8 50%,#fef3c7 100%);color:#9d174d;padding:50px 40px;font-family:'Cormorant Garamond',Georgia,serif;text-align:center;box-shadow:0 30px 70px rgba(236,72,153,.3);position:relative;overflow:hidden}
.cb3::before{content:'';position:absolute;top:-80px;right:-80px;width:280px;height:280px;background:radial-gradient(circle,rgba(244,114,182,.4),transparent 70%);border-radius:50%;filter:blur(40px)}
.cb3::after{content:'';position:absolute;bottom:-80px;left:-80px;width:280px;height:280px;background:radial-gradient(circle,rgba(251,191,36,.4),transparent 70%);border-radius:50%;filter:blur(40px)}
.cb3 .content{position:relative}
.cb3 .florals{font-size:36px;letter-spacing:14px;color:#ec4899}
.cb3 .small{font-family:'Inter',sans-serif;font-size:10px;letter-spacing:8px;color:#9d174d;text-transform:uppercase;font-weight:700;margin:14px 0 8px}
.cb3 h1{font-size:48px;margin:8px 0;color:#9d174d;font-style:italic;font-weight:500;letter-spacing:1px}
.cb3 .name{font-size:54px;color:#831843;font-style:italic;font-weight:600;margin:14px 0;line-height:1}
.cb3 .age{font-family:'Inter',sans-serif;font-size:18px;color:#ec4899;letter-spacing:6px;font-weight:700;text-transform:uppercase}
.cb3 .msg{font-style:italic;font-size:14px;color:#9d174d;margin:14px 30px;line-height:1.7}
.cb3 .info{font-family:'Inter',sans-serif;margin-top:18px;padding-top:14px;border-top:1px solid rgba(236,72,153,.4);font-size:13px;line-height:1.8;color:#9d174d}
""",
     'html': '<div class="cb3"><div class="content"><div class="florals">✿ ❀ ✿</div><div class="small">— SAVE THE DATE —</div><h1>Birthday Wishes</h1><div class="name">{{ name }}</div><div class="age">turns {{ age }}</div><div class="msg">{{ message }}</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }} · RSVP: {{ rsvp }}</div></div></div>'},

    # 4. Neon Cyberpunk Party
    {'title': '🎨 Neon Cyberpunk Glow', 'desc': 'Electric neon glow with cyberpunk vibes.',
     'css': """
.cb4{width:480px;margin:30px auto;background:#0a0a0a;color:#00ffff;padding:50px 30px;font-family:'Inter','Segoe UI',sans-serif;text-align:center;border:3px solid #00ffff;border-radius:8px;box-shadow:0 0 50px rgba(0,255,255,.5),0 0 100px rgba(255,0,255,.3),inset 0 0 30px rgba(0,255,255,.1);position:relative;overflow:hidden}
.cb4::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,255,255,.03) 2px,rgba(0,255,255,.03) 4px);pointer-events:none}
.cb4 .label{font-size:11px;letter-spacing:8px;color:#ff00ff;text-shadow:0 0 10px #ff00ff;text-transform:uppercase;font-weight:700;margin-bottom:14px;font-family:'Consolas',monospace}
.cb4 h1{font-size:48px;margin:8px 0;color:#fff;text-shadow:0 0 20px #00ffff,0 0 40px #00ffff,0 0 60px #00ffff;font-weight:900;letter-spacing:4px;font-family:'Consolas',monospace}
.cb4 .age{font-size:130px;color:#ff00ff;font-weight:900;line-height:1;margin:10px 0;text-shadow:0 0 30px #ff00ff,0 0 60px #ff00ff;font-family:'Consolas',monospace}
.cb4 .name{font-size:30px;color:#00ffff;text-shadow:0 0 14px #00ffff;font-weight:700;margin:8px 0;font-family:'Consolas',monospace}
.cb4 .msg{font-size:13px;color:#a3a3a3;margin:14px 30px;line-height:1.7;font-style:italic}
.cb4 .info{margin-top:18px;padding-top:14px;border-top:1px solid #00ffff;font-size:12px;color:#fff;line-height:1.9;font-family:'Consolas',monospace;letter-spacing:1px}
.cb4 .info b{color:#ff00ff;text-shadow:0 0 10px #ff00ff}
""",
     'html': '<div class="cb4"><div class="label">// NEON.PARTY</div><h1>BIRTHDAY</h1><div class="age">{{ age }}</div><div class="name">{{ name|upper }}</div><div class="msg">{{ message }}</div><div class="info"><b>WHEN:</b> {{ date }} · {{ time }}<br><b>WHERE:</b> {{ venue }}<br><b>RSVP:</b> {{ rsvp }}</div></div>'},

    # 5. Pastel Boho Dreamy
    {'title': '🎨 Pastel Boho Dreamy', 'desc': 'Soft pastel boho with feathers and dreamy vibes.',
     'css': """
.cb5{width:480px;margin:30px auto;background:linear-gradient(160deg,#fef3c7 0%,#fce7f3 30%,#dbeafe 60%,#e0e7ff 100%);color:#6b21a8;padding:50px 40px;font-family:Georgia,serif;text-align:center;border-radius:200px 16px 200px 16px;box-shadow:0 30px 70px rgba(107,33,168,.3);position:relative}
.cb5::before{content:'';position:absolute;inset:14px;border:1px dashed rgba(107,33,168,.3);border-radius:188px 8px 188px 8px;pointer-events:none}
.cb5 .feather{font-size:36px;color:#a855f7;letter-spacing:14px;line-height:1}
.cb5 .small{font-family:'Inter',sans-serif;font-size:10px;letter-spacing:8px;color:#7c3aed;text-transform:uppercase;font-weight:700;margin:14px 0}
.cb5 h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:42px;margin:8px 0;color:#581c87;font-style:italic;font-weight:600}
.cb5 .age-row{display:flex;align-items:baseline;justify-content:center;gap:14px;margin:14px 0}
.cb5 .age-row .age{font-family:'Playfair Display',serif;font-size:90px;color:#a855f7;font-weight:300;line-height:1}
.cb5 .age-row .label{font-family:'Inter',sans-serif;font-size:11px;color:#7c3aed;letter-spacing:4px;text-transform:uppercase;font-weight:700;writing-mode:vertical-lr;transform:rotate(180deg)}
.cb5 .name{font-family:'Cormorant Garamond',serif;font-size:30px;color:#581c87;font-style:italic;margin:8px 0;font-weight:600}
.cb5 .msg{font-style:italic;font-size:13px;color:#6b21a8;margin:14px 30px;line-height:1.7}
.cb5 .info{font-family:'Inter',sans-serif;margin-top:18px;padding-top:14px;border-top:1px dashed rgba(107,33,168,.4);font-size:13px;color:#6b21a8;line-height:1.8}
""",
     'html': '<div class="cb5"><div class="feather">🪶 ✨ 🪶</div><div class="small">— BOHO BIRTHDAY —</div><h1>Celebrate</h1><div class="age-row"><span class="label">YEARS</span><span class="age">{{ age }}</span></div><div class="name">{{ name }}</div><div class="msg">{{ message }}</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }} · {{ rsvp }}</div></div>'},

    # 6. Tropical Beach Party
    {'title': '🎨 Tropical Beach Party', 'desc': 'Tropical beach with palm leaves and ocean blues.',
     'css': """
.cb6{width:480px;margin:30px auto;background:linear-gradient(180deg,#fef3c7 0%,#fde047 20%,#06b6d4 60%,#0e7490 100%);color:#fff;padding:50px 30px;font-family:'Inter',sans-serif;text-align:center;border:6px solid #fff;border-radius:16px;box-shadow:0 30px 70px rgba(14,116,144,.5);position:relative;overflow:hidden}
.cb6::before{content:'🌴 🌺 🥥 🌴 🌺 🥥';position:absolute;top:14px;left:0;right:0;font-size:20px;letter-spacing:6px;opacity:.5}
.cb6 .palm{font-size:50px;letter-spacing:6px;line-height:1;margin-top:20px;text-shadow:2px 2px 8px rgba(0,0,0,.3)}
.cb6 .small{font-family:'Inter',sans-serif;font-size:11px;letter-spacing:8px;color:#fff;text-transform:uppercase;font-weight:700;margin:14px 0;background:#0e7490;padding:6px 18px;display:inline-block;border-radius:20px;box-shadow:0 4px 12px rgba(0,0,0,.3)}
.cb6 h1{font-family:'Playfair Display',serif;font-size:46px;margin:14px 0 6px;color:#fff;font-style:italic;font-weight:600;text-shadow:3px 3px 0 #0e7490,5px 5px 12px rgba(0,0,0,.3)}
.cb6 .age{font-size:90px;color:#fff;font-weight:900;line-height:.9;text-shadow:4px 4px 0 #0e7490,6px 6px 12px rgba(0,0,0,.4);margin:10px 0}
.cb6 .name{font-family:'Playfair Display',serif;font-size:30px;color:#fff;font-style:italic;font-weight:600;margin:8px 0;text-shadow:2px 2px 0 #0e7490}
.cb6 .info{margin-top:18px;background:rgba(255,255,255,.95);color:#0e7490;padding:14px;border-radius:14px;font-size:13px;line-height:1.7;font-weight:600;box-shadow:0 8px 20px rgba(0,0,0,.2)}
.cb6 .info b{color:#bf360c}
""",
     'html': '<div class="cb6"><div class="palm">🌴 🥥 🌴</div><div class="small">BEACH BIRTHDAY BASH</div><h1>{{ name }}</h1><div class="age">{{ age }}</div><div class="msg" style="font-style:italic;font-size:13px;margin:10px 30px;text-shadow:1px 1px 4px rgba(0,0,0,.3)">{{ message }}</div><div class="info"><b>📅</b> {{ date }} · {{ time }}<br><b>📍</b> {{ venue }}<br><b>📞</b> {{ rsvp }}</div></div>'},
]


# ============================================================
# RESUME — 6 DISTINCT CANVA-INSPIRED DESIGNS
# ============================================================
CANVA_RESUMES = [
    # 1. Gradient Header Modern
    {'title': '🎨 Gradient Sunset Modern', 'desc': 'Bold sunset gradient header with split layout.',
     'css': """
.cr1{font-family:'Inter',sans-serif;max-width:780px;margin:0 auto;background:#fff;padding:0;box-shadow:0 30px 70px rgba(236,72,153,.25);border-radius:14px;overflow:hidden}
.cr1 .top{background:linear-gradient(135deg,#fbbf24 0%,#f97316 50%,#ec4899 100%);color:#fff;padding:50px 50px 70px;position:relative;clip-path:polygon(0 0,100% 0,100% 88%,0 100%)}
.cr1 .top h1{font-family:'Playfair Display',serif;font-size:54px;margin:0;font-weight:700;letter-spacing:-1px;text-shadow:0 4px 20px rgba(0,0,0,.2)}
.cr1 .top .role{font-size:14px;color:#fff;letter-spacing:5px;text-transform:uppercase;margin:8px 0 14px;font-weight:600;opacity:.95}
.cr1 .top .ct{font-size:12px;color:#fff;opacity:.95;letter-spacing:.5px}
.cr1 .body{padding:40px 50px}
.cr1 h2{font-family:'Playfair Display',serif;font-size:24px;color:#0a0a0a;margin-top:24px;font-weight:700;display:inline-block;position:relative}
.cr1 h2::after{content:'';display:block;width:48px;height:4px;background:linear-gradient(90deg,#fbbf24,#ec4899);margin-top:6px;border-radius:2px}
.cr1 pre{font-family:inherit;white-space:pre-wrap;font-size:13px;line-height:1.8;color:#475569;margin:14px 0}
""",
     'html': '<div class="cr1"><div class="top"><h1>{{ name }}</h1><div class="role">{{ title }}</div><div class="ct">{{ email }} &nbsp;·&nbsp; {{ phone }} &nbsp;·&nbsp; {{ location }}</div></div><div class="body"><h2>About</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><pre>{{ skills }}</pre></div></div>'},

    # 2. Vertical Timeline Creative
    {'title': '🎨 Vertical Timeline Pro', 'desc': 'Creative timeline layout with circular date markers.',
     'css': """
.cr2{font-family:'Inter',sans-serif;max-width:780px;margin:0 auto;background:#fafafa;padding:50px 50px;color:#0f172a;box-shadow:0 30px 70px rgba(0,0,0,.15);border-left:8px solid #6366f1}
.cr2 .top{display:flex;align-items:center;gap:24px;margin-bottom:30px;padding-bottom:24px;border-bottom:2px solid #e2e8f0}
.cr2 .avatar{width:80px;height:80px;border-radius:50%;background:linear-gradient(135deg,#6366f1,#a855f7);color:#fff;display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:900;box-shadow:0 8px 20px rgba(99,102,241,.4);flex-shrink:0}
.cr2 .top-info h1{font-family:'Playfair Display',serif;font-size:38px;margin:0;color:#0f172a;font-weight:700;line-height:1}
.cr2 .top-info .role{font-size:13px;color:#6366f1;letter-spacing:3px;text-transform:uppercase;margin:6px 0;font-weight:700}
.cr2 .top-info .ct{font-size:11px;color:#64748b;letter-spacing:.5px}
.cr2 h2{font-size:13px;letter-spacing:5px;text-transform:uppercase;color:#6366f1;margin-top:24px;font-weight:700;position:relative;padding-left:24px}
.cr2 h2::before{content:'';position:absolute;left:0;top:50%;transform:translateY(-50%);width:14px;height:14px;border-radius:50%;background:linear-gradient(135deg,#6366f1,#a855f7);box-shadow:0 0 0 4px rgba(99,102,241,.2)}
.cr2 pre{font-family:inherit;white-space:pre-wrap;font-size:13px;line-height:1.8;color:#475569;margin:10px 0 0 24px;border-left:2px dashed #cbd5e1;padding-left:14px}
""",
     'html': '<div class="cr2"><div class="top"><div class="avatar">{{ name|first }}</div><div class="top-info"><h1>{{ name }}</h1><div class="role">{{ title }}</div><div class="ct">{{ email }} · {{ phone }} · {{ location }}</div></div></div><h2>Profile</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><pre>{{ skills }}</pre></div>'},

    # 3. Two-Column Photo Sidebar
    {'title': '🎨 Photo Sidebar Creative', 'desc': 'Two-column with colorful sidebar and skill badges.',
     'css': """
.cr3{display:flex;font-family:'Inter',sans-serif;max-width:780px;margin:0 auto;background:#fff;min-height:760px;box-shadow:0 30px 70px rgba(34,197,94,.2)}
.cr3 .side{width:34%;background:linear-gradient(180deg,#16a34a 0%,#15803d 100%);color:#fff;padding:50px 28px;text-align:center}
.cr3 .photo{width:140px;height:140px;border-radius:50%;background:#fff;border:6px solid #fff;box-shadow:0 14px 30px rgba(0,0,0,.3);margin:0 auto 18px;display:flex;align-items:center;justify-content:center;font-size:54px;color:#16a34a;font-weight:900;font-family:'Playfair Display',serif}
.cr3 .side h1{font-family:'Playfair Display',serif;font-size:26px;margin:0 0 6px;font-weight:700;letter-spacing:.5px}
.cr3 .side .role{font-size:11px;color:#bbf7d0;letter-spacing:3px;text-transform:uppercase;margin-bottom:24px;font-weight:600}
.cr3 .side h3{font-size:11px;letter-spacing:3px;color:#fff;text-transform:uppercase;margin-top:22px;border-bottom:2px solid rgba(255,255,255,.3);padding-bottom:6px;text-align:left;font-weight:700}
.cr3 .side p{font-size:11px;color:#dcfce7;line-height:1.7;margin:8px 0;text-align:left}
.cr3 .side .skill-tags{display:flex;flex-wrap:wrap;gap:4px;margin-top:8px}
.cr3 .side .skill-tags span{background:rgba(255,255,255,.2);padding:3px 8px;border-radius:10px;font-size:9px;font-weight:600}
.cr3 .main{flex:1;padding:50px 38px}
.cr3 .main h2{font-family:'Playfair Display',serif;font-size:22px;color:#15803d;margin-top:22px;font-style:italic;font-weight:700}
.cr3 .main h2::before{content:'❯ ';color:#16a34a}
.cr3 .main pre{font-family:inherit;white-space:pre-wrap;font-size:13px;line-height:1.8;color:#475569;margin:10px 0}
""",
     'html': '<div class="cr3"><div class="side"><div class="photo">{{ name|first }}</div><h1>{{ name }}</h1><div class="role">{{ title }}</div><h3>Contact</h3><p>{{ email }}<br>{{ phone }}<br>{{ location }}</p><h3>Education</h3><p>{{ education }}</p><h3>Skills</h3><div class="skill-tags">{% for s in skills_list %}<span>{{ s }}</span>{% endfor %}</div></div><div class="main"><h2>About Me</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre></div></div>'},

    # 4. Magazine Editorial Bold
    {'title': '🎨 Magazine Editorial Bold', 'desc': 'Magazine-cover with massive serif and pull-quote.',
     'css': """
.cr4{font-family:'Inter',sans-serif;max-width:780px;margin:0 auto;background:#fff;padding:0;box-shadow:0 30px 70px rgba(0,0,0,.2);border:1px solid #0a0a0a}
.cr4 .top{padding:40px 50px 30px;border-bottom:6px double #0a0a0a;background:#fafafa}
.cr4 .magazine-bar{display:flex;justify-content:space-between;font-size:9px;letter-spacing:5px;text-transform:uppercase;color:#737373;font-weight:700;margin-bottom:14px}
.cr4 .top h1{font-family:'Playfair Display',serif;font-size:84px;margin:0;color:#0a0a0a;font-weight:900;letter-spacing:-4px;line-height:.85}
.cr4 .top .role{font-family:'Cormorant Garamond',serif;font-size:28px;font-style:italic;color:#dc2626;margin:8px 0 14px;font-weight:500}
.cr4 .top .ct{font-size:11px;color:#525252;letter-spacing:1px;border-top:1px solid #0a0a0a;padding-top:12px}
.cr4 .body{padding:40px 50px}
.cr4 .quote{font-family:'Cormorant Garamond',serif;font-size:24px;font-style:italic;color:#0a0a0a;line-height:1.4;margin:0 0 30px;padding:0 20px;text-align:center;position:relative}
.cr4 .quote::before,.cr4 .quote::after{font-size:60px;color:#dc2626;font-weight:900;line-height:0;position:relative;top:18px}
.cr4 .quote::before{content:'"';margin-right:8px}
.cr4 .quote::after{content:'"';margin-left:8px}
.cr4 h2{font-family:'Playfair Display',serif;font-size:14px;letter-spacing:5px;text-transform:uppercase;color:#0a0a0a;margin-top:28px;font-weight:900;border-bottom:2px solid #dc2626;padding-bottom:6px;display:inline-block}
.cr4 pre{font-family:inherit;white-space:pre-wrap;font-size:13px;line-height:1.8;color:#404040;margin:12px 0}
""",
     'html': '<div class="cr4"><div class="top"><div class="magazine-bar"><span>RESUME · VOL 01</span><span>2026</span></div><h1>{{ name }}</h1><div class="role">— {{ title }}</div><div class="ct">{{ email }} &nbsp;·&nbsp; {{ phone }} &nbsp;·&nbsp; {{ location }}</div></div><div class="body"><div class="quote">{{ summary }}</div><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><pre>{{ skills }}</pre></div></div>'},

    # 5. Architect Dark Modern
    {'title': '🎨 Architect Dark Geometric', 'desc': 'Dark geometric architectural with cyan accents.',
     'css': """
.cr5{font-family:'Inter',sans-serif;max-width:780px;margin:0 auto;background:#0f172a;color:#f1f5f9;padding:50px 50px;box-shadow:0 30px 70px rgba(0,0,0,.5);border:1px solid #1e293b;position:relative;overflow:hidden}
.cr5::before{content:'';position:absolute;top:0;right:0;width:200px;height:200px;background:linear-gradient(135deg,#06b6d4,transparent);clip-path:polygon(100% 0,0 0,100% 100%);opacity:.3}
.cr5 .top{position:relative;z-index:2}
.cr5 .label{font-family:'Consolas',monospace;font-size:11px;color:#06b6d4;letter-spacing:3px;text-transform:uppercase}
.cr5 h1{font-size:54px;margin:8px 0 4px;color:#fff;font-weight:200;letter-spacing:-1px;line-height:1}
.cr5 .role{font-size:13px;color:#06b6d4;letter-spacing:5px;text-transform:uppercase;margin:8px 0 24px;font-weight:600}
.cr5 .ct-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;font-size:11px;border:1px solid #334155;padding:14px;margin-bottom:24px;background:rgba(6,182,212,.05)}
.cr5 .ct-grid b{color:#06b6d4;display:block;font-size:9px;letter-spacing:2px;text-transform:uppercase;margin-bottom:4px}
.cr5 .ct-grid span{color:#cbd5e1}
.cr5 h2{font-size:13px;letter-spacing:5px;text-transform:uppercase;color:#06b6d4;margin-top:24px;font-weight:700;border-left:3px solid #06b6d4;padding-left:14px}
.cr5 pre{font-family:inherit;white-space:pre-wrap;font-size:13px;line-height:1.8;color:#cbd5e1;margin:10px 0 0 17px}
""",
     'html': '<div class="cr5"><div class="top"><div class="label">// RESUME.001</div><h1>{{ name }}</h1><div class="role">{{ title }}</div></div><div class="ct-grid"><div><b>Email</b><span>{{ email }}</span></div><div><b>Phone</b><span>{{ phone }}</span></div><div><b>Location</b><span>{{ location }}</span></div></div><h2>Profile</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><pre>{{ skills }}</pre></div>'},

    # 6. Pastel Boho Natural
    {'title': '🎨 Pastel Boho Natural', 'desc': 'Soft pastel boho with handwritten touch.',
     'css': """
.cr6{font-family:'Inter',sans-serif;max-width:780px;margin:0 auto;background:linear-gradient(180deg,#fef3c7 0%,#fff 30%);padding:60px 50px;color:#78350f;box-shadow:0 30px 70px rgba(217,119,6,.2);border:1px solid #fde68a}
.cr6 .top{text-align:center;margin-bottom:30px;padding-bottom:24px;border-bottom:2px dashed #f59e0b}
.cr6 .leaf{font-size:30px;color:#16a34a;letter-spacing:14px}
.cr6 h1{font-family:'Cormorant Garamond',serif;font-size:48px;margin:8px 0 4px;color:#78350f;font-weight:700;font-style:italic;letter-spacing:1px}
.cr6 .role{font-family:'Cormorant Garamond',serif;font-size:18px;color:#d97706;font-style:italic;margin:6px 0 12px}
.cr6 .ct{font-size:11px;color:#92400e;letter-spacing:1px}
.cr6 h2{font-family:'Cormorant Garamond',serif;font-size:24px;color:#78350f;margin-top:24px;font-style:italic;font-weight:700}
.cr6 h2::before{content:'❀ ';color:#d97706}
.cr6 pre{font-family:inherit;white-space:pre-wrap;font-size:13px;line-height:1.8;color:#5a3a0a;margin:10px 0}
""",
     'html': '<div class="cr6"><div class="top"><div class="leaf">🌿 ❀ 🌿</div><h1>{{ name }}</h1><div class="role">{{ title }}</div><div class="ct">{{ email }} · {{ phone }} · {{ location }}</div></div><h2>About Me</h2><pre>{{ summary }}</pre><h2>Experience</h2><pre>{{ experience }}</pre><h2>Education</h2><pre>{{ education }}</pre><h2>Skills</h2><pre>{{ skills }}</pre></div>'},
]


# ============================================================
# COVER LETTER — 6 DISTINCT CANVA-INSPIRED DESIGNS
# ============================================================
CANVA_COVERS = [
    # 1. Gradient Banner Modern
    {'title': '🎨 Gradient Banner Modern', 'desc': 'Bold gradient banner header.',
     'css': """
.ccl1{font-family:'Inter',sans-serif;max-width:780px;margin:0 auto;background:#fff;padding:0;box-shadow:0 30px 70px rgba(99,102,241,.25);line-height:1.8}
.ccl1 .top{background:linear-gradient(135deg,#6366f1 0%,#a855f7 50%,#ec4899 100%);color:#fff;padding:36px 50px;clip-path:polygon(0 0,100% 0,100% 90%,0 100%)}
.ccl1 .top h1{font-family:'Playfair Display',serif;font-size:38px;margin:0;font-weight:700;letter-spacing:-.5px}
.ccl1 .top .ct{font-size:12px;color:#fff;opacity:.95;margin-top:6px}
.ccl1 .body{padding:30px 50px;color:#404040;font-size:14px}
.ccl1 .body strong{color:#0a0a0a}
.ccl1 .date{color:#a855f7;font-weight:700;font-size:13px;margin-bottom:14px;letter-spacing:1px}
""",
     'html': '<div class="ccl1"><div class="top"><h1>{{ name }}</h1><div class="ct">{{ email }} · {{ phone }}</div></div><div class="body"><div class="date">{{ date }}</div><strong>{{ hiring_manager }}</strong><br>{{ company }}<br><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Sincerely,<br><br><strong>{{ name }}</strong></div></div>'},

    # 2. Side Bar Initial
    {'title': '🎨 Initial Sidebar Modern', 'desc': 'Side initial badge with clean letter body.',
     'css': """
.ccl2{display:flex;font-family:'Inter',sans-serif;max-width:780px;margin:0 auto;background:#fff;min-height:760px;box-shadow:0 30px 70px rgba(15,23,42,.2)}
.ccl2 .side{width:30%;background:#0f172a;color:#fff;padding:50px 24px;text-align:center;display:flex;flex-direction:column;justify-content:flex-start}
.ccl2 .initial{width:90px;height:90px;border-radius:50%;background:linear-gradient(135deg,#fbbf24,#f59e0b);color:#0f172a;display:flex;align-items:center;justify-content:center;font-family:'Playfair Display',serif;font-size:42px;font-weight:900;margin:0 auto 18px;box-shadow:0 8px 20px rgba(251,191,36,.4)}
.ccl2 .side h1{font-family:'Playfair Display',serif;font-size:24px;margin:0;font-weight:700}
.ccl2 .side .ct{font-size:11px;color:#94a3b8;margin-top:14px;line-height:1.7;letter-spacing:.5px}
.ccl2 .body{flex:1;padding:50px 38px;font-size:14px;line-height:1.85;color:#404040}
.ccl2 .body strong{color:#0f172a}
.ccl2 .body .date{color:#f59e0b;font-weight:700;margin-bottom:14px}
""",
     'html': '<div class="ccl2"><div class="side"><div class="initial">{{ name|first }}</div><h1>{{ name }}</h1><div class="ct">{{ email }}<br>{{ phone }}</div></div><div class="body"><div class="date">{{ date }}</div><strong>{{ hiring_manager }}</strong><br>{{ company }}<br><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Sincerely,<br><br><strong>{{ name }}</strong></div></div>'},

    # 3. Editorial Magazine Bold
    {'title': '🎨 Editorial Magazine Bold', 'desc': 'Magazine-style with massive serif name.',
     'css': """
.ccl3{font-family:'Inter',sans-serif;max-width:780px;margin:0 auto;background:#fff;padding:0;box-shadow:0 30px 70px rgba(0,0,0,.2);border:1px solid #0a0a0a;line-height:1.85}
.ccl3 .top{padding:40px 50px 24px;background:#fafafa;border-bottom:6px double #0a0a0a}
.ccl3 .magazine-bar{display:flex;justify-content:space-between;font-size:9px;letter-spacing:5px;text-transform:uppercase;color:#737373;font-weight:700;margin-bottom:8px}
.ccl3 h1{font-family:'Playfair Display',serif;font-size:54px;margin:0;color:#0a0a0a;font-weight:900;letter-spacing:-2px;line-height:.95}
.ccl3 .ct{font-size:11px;color:#525252;letter-spacing:1px;margin-top:8px}
.ccl3 .body{padding:30px 50px;color:#404040;font-size:14px}
.ccl3 .body strong{color:#0a0a0a;font-weight:700}
.ccl3 .body .date{color:#dc2626;font-weight:700;font-style:italic;font-family:'Cormorant Garamond',serif;font-size:18px;margin-bottom:14px}
.ccl3 .body .re{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:18px;color:#dc2626;border-left:3px solid #dc2626;padding-left:14px;margin:14px 0}
""",
     'html': '<div class="ccl3"><div class="top"><div class="magazine-bar"><span>COVER LETTER</span><span>VOL 01 · 2026</span></div><h1>{{ name }}</h1><div class="ct">{{ email }} &nbsp;·&nbsp; {{ phone }}</div></div><div class="body"><div class="date">{{ date }}</div><strong>{{ hiring_manager }}</strong><br>{{ company }}<br><div class="re">Re: {{ position }}</div>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Sincerely,<br><br><strong>{{ name }}</strong></div></div>'},

    # 4. Pastel Soft Feminine
    {'title': '🎨 Pastel Pink Soft', 'desc': 'Soft pastel pink with elegant script.',
     'css': """
.ccl4{font-family:'Inter',sans-serif;max-width:780px;margin:0 auto;background:linear-gradient(135deg,#fdf2f8 0%,#fff 60%);padding:50px 50px;color:#831843;box-shadow:0 30px 70px rgba(236,72,153,.25);line-height:1.85;border:1px solid #fbcfe8}
.ccl4 .top{text-align:center;padding-bottom:24px;border-bottom:2px dashed #ec4899;margin-bottom:24px}
.ccl4 .ornament{font-size:24px;color:#ec4899;letter-spacing:14px}
.ccl4 h1{font-family:'Playfair Display',serif;font-size:42px;margin:8px 0 4px;color:#9d174d;font-weight:600;font-style:italic}
.ccl4 .ct{font-size:11px;color:#9d174d;letter-spacing:1px;font-family:'Inter',sans-serif}
.ccl4 .body{font-size:14px;color:#7e22ce;font-family:'Inter',sans-serif}
.ccl4 .body strong{color:#831843;font-weight:700}
.ccl4 .date{font-family:'Cormorant Garamond',serif;font-size:18px;font-style:italic;color:#ec4899;margin-bottom:14px}
""",
     'html': '<div class="ccl4"><div class="top"><div class="ornament">❀ ✿ ❀</div><h1>{{ name }}</h1><div class="ct">{{ email }} · {{ phone }}</div></div><div class="body"><div class="date">{{ date }}</div><strong>{{ hiring_manager }}</strong><br>{{ company }}<br><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Warmly,<br><br><strong>{{ name }}</strong></div></div>'},

    # 5. Tech Dark Terminal
    {'title': '🎨 Tech Terminal Dark', 'desc': 'Dark terminal style with monospace and cyan.',
     'css': """
.ccl5{font-family:'Inter',sans-serif;max-width:780px;margin:0 auto;background:#0f172a;padding:50px 50px;color:#cbd5e1;box-shadow:0 30px 70px rgba(0,0,0,.5);line-height:1.85;border:1px solid #1e293b;position:relative}
.ccl5::before{content:'';position:absolute;top:14px;left:14px;width:12px;height:12px;border-radius:50%;background:#ef4444;box-shadow:18px 0 0 #f59e0b,36px 0 0 #10b981}
.ccl5 .label{font-family:'Consolas',monospace;font-size:11px;color:#06b6d4;letter-spacing:2px;margin-top:18px;text-transform:uppercase}
.ccl5 h1{font-size:42px;margin:6px 0;color:#fff;font-weight:200;letter-spacing:-1px;line-height:1}
.ccl5 .ct{font-family:'Consolas',monospace;font-size:11px;color:#06b6d4;margin:8px 0 18px;border-top:1px solid #334155;border-bottom:1px solid #334155;padding:10px 0}
.ccl5 .body{font-size:13px;color:#cbd5e1}
.ccl5 .body strong{color:#06b6d4;font-weight:700}
.ccl5 .body .date{font-family:'Consolas',monospace;color:#06b6d4;margin-bottom:14px}
""",
     'html': '<div class="ccl5"><div class="label">// COVER_LETTER.md</div><h1>{{ name }}</h1><div class="ct">{{ email }} | {{ phone }}</div><div class="body"><div class="date">// {{ date }}</div><strong>{{ hiring_manager }}</strong><br>{{ company }}<br><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Best,<br><br><strong>{{ name }}</strong></div></div>'},

    # 6. Bold Color Block
    {'title': '🎨 Color Block Bold', 'desc': 'Bold color block with diagonal split.',
     'css': """
.ccl6{font-family:'Inter',sans-serif;max-width:780px;margin:0 auto;background:#fff;padding:0;box-shadow:0 30px 70px rgba(220,38,38,.25);line-height:1.85;position:relative;overflow:hidden}
.ccl6::before{content:'';position:absolute;top:0;left:0;width:200px;height:100%;background:#dc2626;clip-path:polygon(0 0,100% 0,60% 100%,0 100%);z-index:0}
.ccl6 .top{position:relative;z-index:2;padding:50px 50px 24px;display:flex;align-items:center;gap:24px}
.ccl6 .badge{width:80px;height:80px;border-radius:50%;background:#fff;color:#dc2626;display:flex;align-items:center;justify-content:center;font-family:'Playfair Display',serif;font-size:38px;font-weight:900;box-shadow:0 8px 20px rgba(0,0,0,.3);flex-shrink:0;border:4px solid #fff}
.ccl6 .top-info h1{font-family:'Playfair Display',serif;font-size:36px;margin:0;color:#fff;font-weight:900;line-height:1}
.ccl6 .top-info .ct{font-size:11px;color:#fef2f2;letter-spacing:1px;margin-top:6px}
.ccl6 .body{padding:30px 50px;color:#404040;font-size:14px;position:relative;z-index:2;background:#fff}
.ccl6 .body strong{color:#dc2626}
.ccl6 .body .date{color:#dc2626;font-weight:700;margin-bottom:14px;letter-spacing:1px}
""",
     'html': '<div class="ccl6"><div class="top"><div class="badge">{{ name|first }}</div><div class="top-info"><h1>{{ name }}</h1><div class="ct">{{ email }} · {{ phone }}</div></div></div><div class="body"><div class="date">{{ date }}</div><strong>{{ hiring_manager }}</strong><br>{{ company }}<br><br>Re: <strong>{{ position }}</strong><br><br>Dear {{ hiring_manager }},<br><br>{{ body|linebreaksbr }}<br><br>Sincerely,<br><br><strong>{{ name }}</strong></div></div>'},
]
