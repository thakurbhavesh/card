"""Extra templates part 2: Festivals, Flyers, Menus, Tickets, Vouchers."""

# ============================================================
# FESTIVAL CARDS (15)
# ============================================================
FESTIVALS = [
    {'title': 'Diwali Lamps', 'desc': 'Traditional Diwali greeting card.',
     'css': ".fs1{width:520px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#ff6f00,#ffb300);color:#fff;text-align:center;font-family:Georgia,serif;border-radius:18px;box-shadow:0 24px 60px rgba(255,111,0,.4)}.fs1 .ico{font-size:60px}.fs1 h1{font-size:46px;margin:14px 0;font-style:italic;text-shadow:2px 2px 0 rgba(0,0,0,.2)}.fs1 .greet{font-size:18px;margin:14px 0}.fs1 .msg{font-size:14px;line-height:1.7;margin:14px 30px;font-style:italic}.fs1 .from{margin-top:18px;border-top:1px solid rgba(255,255,255,.4);padding-top:14px;font-size:14px}",
     'html': '<div class="fs1"><div class="ico">🪔 ✨ 🪔</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Holi Splash', 'desc': 'Colorful Holi greeting.',
     'css': ".fs2{width:520px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#ff1744,#f50057,#aa00ff,#2962ff,#00c853);color:#fff;text-align:center;font-family:'Segoe UI',sans-serif;border-radius:18px;box-shadow:0 24px 60px rgba(0,0,0,.3)}.fs2 .ico{font-size:54px}.fs2 h1{font-size:46px;margin:14px 0;font-weight:900;text-shadow:3px 3px 0 rgba(0,0,0,.25)}.fs2 .greet{font-size:18px;margin:14px 0}.fs2 .msg{font-size:14px;line-height:1.7;margin:14px 30px}.fs2 .from{margin-top:18px;font-size:14px}",
     'html': '<div class="fs2"><div class="ico">🎨 🌈 🎨</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Christmas Snow', 'desc': 'Traditional Christmas card.',
     'css': ".fs3{width:520px;margin:30px auto;padding:50px 40px;background:#1b5e20;color:#fff;text-align:center;font-family:Georgia,serif;border:6px solid #f5c842;border-radius:14px}.fs3 .ico{font-size:54px;color:#fff}.fs3 h1{font-size:42px;margin:14px 0;color:#f5c842;font-style:italic}.fs3 .greet{font-size:17px;margin:14px 0}.fs3 .msg{font-size:14px;line-height:1.7;margin:14px 30px}.fs3 .from{margin-top:18px;border-top:1px solid #f5c842;padding-top:14px;font-size:14px}",
     'html': '<div class="fs3"><div class="ico">🎄 ❄ 🎁</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'New Year Sparkle', 'desc': 'Glittery new year greeting.',
     'css': ".fs4{width:520px;margin:30px auto;padding:50px 40px;background:#000;color:#f5c842;text-align:center;font-family:'Segoe UI',sans-serif;border:2px solid #f5c842;outline:6px solid #000;outline-offset:-12px}.fs4 .ico{font-size:54px}.fs4 h1{font-size:54px;margin:14px 0;font-weight:900;color:#fff;letter-spacing:3px}.fs4 .greet{font-size:17px;color:#f5c842;margin:14px 0;letter-spacing:2px}.fs4 .msg{font-size:14px;line-height:1.7;margin:14px 30px;color:#fff}.fs4 .from{margin-top:18px;font-size:14px;color:#f5c842}",
     'html': '<div class="fs4"><div class="ico">🎆 ✨ 🎆</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Eid Mubarak', 'desc': 'Elegant Eid greeting card.',
     'css': ".fs5{width:520px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#1a237e,#3949ab);color:#fff;text-align:center;font-family:Georgia,serif;border:3px solid #f5c842;border-radius:14px}.fs5 .ico{font-size:54px;color:#f5c842}.fs5 h1{font-size:44px;margin:14px 0;font-style:italic;color:#f5c842}.fs5 .greet{font-size:17px;margin:14px 0}.fs5 .msg{font-size:14px;line-height:1.7;margin:14px 30px}.fs5 .from{margin-top:18px;border-top:1px solid #f5c842;padding-top:14px;font-size:14px}",
     'html': '<div class="fs5"><div class="ico">🌙 ✨ 🕌</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Raksha Bandhan', 'desc': 'Sister-brother festival card.',
     'css': ".fs6{width:520px;margin:30px auto;padding:50px 40px;background:#fff0f5;color:#880e4f;text-align:center;font-family:Georgia,serif;border:4px double #ec407a;border-radius:14px}.fs6 .ico{font-size:54px}.fs6 h1{font-size:42px;margin:14px 0;font-style:italic;color:#ad1457}.fs6 .greet{font-size:17px;color:#ad1457;margin:14px 0}.fs6 .msg{font-size:14px;line-height:1.7;margin:14px 30px;color:#5d4037}.fs6 .from{margin-top:18px;border-top:1px solid #ec407a;padding-top:14px;font-size:14px}",
     'html': '<div class="fs6"><div class="ico">🎀 ❤ 🎀</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Navratri Garba', 'desc': 'Dance festival greeting.',
     'css': ".fs7{width:520px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#e91e63,#ff5722,#ff9800);color:#fff;text-align:center;font-family:Georgia,serif;border-radius:18px;box-shadow:0 24px 60px rgba(233,30,99,.4)}.fs7 .ico{font-size:54px}.fs7 h1{font-size:42px;margin:14px 0;font-style:italic}.fs7 .greet{font-size:17px;margin:14px 0}.fs7 .msg{font-size:14px;line-height:1.7;margin:14px 30px}.fs7 .from{margin-top:18px;font-size:14px}",
     'html': '<div class="fs7"><div class="ico">💃 🪘 💃</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Ganesh Chaturthi', 'desc': 'Lord Ganesha greeting.',
     'css': ".fs8{width:520px;margin:30px auto;padding:50px 40px;background:#fff8e1;color:#bf360c;text-align:center;font-family:Georgia,serif;border:6px solid #ff6f00;border-radius:14px}.fs8 .ico{font-size:54px}.fs8 h1{font-size:42px;margin:14px 0;font-style:italic;color:#bf360c}.fs8 .greet{font-size:17px;color:#e65100;margin:14px 0}.fs8 .msg{font-size:14px;line-height:1.7;margin:14px 30px;color:#5d4037}.fs8 .from{margin-top:18px;border-top:1px solid #ff6f00;padding-top:14px;font-size:14px}",
     'html': '<div class="fs8"><div class="ico">🐘 🌺 🐘</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Pongal Harvest', 'desc': 'South Indian harvest festival.',
     'css': ".fs9{width:520px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#fff176,#ffd54f);color:#3e2723;text-align:center;font-family:Georgia,serif;border:6px solid #ff8f00;border-radius:14px}.fs9 .ico{font-size:54px}.fs9 h1{font-size:42px;margin:14px 0;font-style:italic;color:#bf360c}.fs9 .greet{font-size:17px;margin:14px 0;color:#e65100}.fs9 .msg{font-size:14px;line-height:1.7;margin:14px 30px}.fs9 .from{margin-top:18px;border-top:1px solid #ff8f00;padding-top:14px;font-size:14px}",
     'html': '<div class="fs9"><div class="ico">🌾 🍚 🌾</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Republic Day', 'desc': 'Patriotic Republic Day card.',
     'css': ".fs10{width:520px;margin:30px auto;padding:50px 40px;background:#fff;color:#000;text-align:center;font-family:Georgia,serif;border-top:14px solid #ff9933;border-bottom:14px solid #138808;box-shadow:0 24px 60px rgba(0,0,0,.15)}.fs10 .ico{font-size:54px;color:#000080}.fs10 h1{font-size:42px;margin:14px 0;color:#000080;font-style:italic}.fs10 .greet{font-size:17px;margin:14px 0;color:#ff9933}.fs10 .msg{font-size:14px;line-height:1.7;margin:14px 30px;color:#333}.fs10 .from{margin-top:18px;font-size:14px}",
     'html': '<div class="fs10"><div class="ico">🇮🇳</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Valentine Hearts', 'desc': 'Romantic Valentine card.',
     'css': ".fs11{width:520px;margin:30px auto;padding:50px 40px;background:#fff0f5;color:#880e4f;text-align:center;font-family:Georgia,serif;border:4px solid #e91e63;border-radius:18px}.fs11 .ico{font-size:50px;color:#e91e63}.fs11 h1{font-size:42px;margin:14px 0;font-style:italic;color:#ad1457}.fs11 .greet{font-size:17px;margin:14px 0;color:#ec407a}.fs11 .msg{font-size:14px;line-height:1.7;margin:14px 30px;font-style:italic}.fs11 .from{margin-top:18px;border-top:1px solid #ec407a;padding-top:14px;font-size:14px}",
     'html': '<div class="fs11"><div class="ico">❤ ❤ ❤</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Mother\'s Day', 'desc': 'Sweet Mother\'s Day card.',
     'css': ".fs12{width:520px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#fad0c4,#ffd1ff);color:#4a148c;text-align:center;font-family:Georgia,serif;border-radius:18px}.fs12 .ico{font-size:50px;color:#e91e63}.fs12 h1{font-size:42px;margin:14px 0;font-style:italic;color:#880e4f}.fs12 .greet{font-size:17px;margin:14px 0;color:#ad1457}.fs12 .msg{font-size:14px;line-height:1.7;margin:14px 30px;color:#5d4037}.fs12 .from{margin-top:18px;font-size:14px}",
     'html': '<div class="fs12"><div class="ico">💐 ❤ 💐</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Father\'s Day', 'desc': 'Manly Father\'s Day card.',
     'css': ".fs13{width:520px;margin:30px auto;padding:50px 40px;background:#37474f;color:#fff;text-align:center;font-family:Georgia,serif;border:4px solid #ffc107;border-radius:14px}.fs13 .ico{font-size:50px;color:#ffc107}.fs13 h1{font-size:42px;margin:14px 0;color:#ffc107;font-style:italic}.fs13 .greet{font-size:17px;margin:14px 0}.fs13 .msg{font-size:14px;line-height:1.7;margin:14px 30px}.fs13 .from{margin-top:18px;border-top:1px solid #ffc107;padding-top:14px;font-size:14px}",
     'html': '<div class="fs13"><div class="ico">👔 ❤ 👔</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Easter Joy', 'desc': 'Pastel Easter card.',
     'css': ".fs14{width:520px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#fff9c4,#c5e1a5);color:#3e2723;text-align:center;font-family:Georgia,serif;border-radius:18px;border:4px dashed #66bb6a}.fs14 .ico{font-size:54px}.fs14 h1{font-size:42px;margin:14px 0;font-style:italic;color:#33691e}.fs14 .greet{font-size:17px;margin:14px 0;color:#558b2f}.fs14 .msg{font-size:14px;line-height:1.7;margin:14px 30px}.fs14 .from{margin-top:18px;font-size:14px}",
     'html': '<div class="fs14"><div class="ico">🐰 🥚 🐰</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Thanksgiving Warm', 'desc': 'Warm autumn thanksgiving card.',
     'css': ".fs15{width:520px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#ff8f00,#bf360c);color:#fff;text-align:center;font-family:Georgia,serif;border-radius:14px;border:4px solid #ffd54f}.fs15 .ico{font-size:54px}.fs15 h1{font-size:42px;margin:14px 0;font-style:italic;color:#ffd54f}.fs15 .greet{font-size:17px;margin:14px 0}.fs15 .msg{font-size:14px;line-height:1.7;margin:14px 30px}.fs15 .from{margin-top:18px;border-top:1px solid #ffd54f;padding-top:14px;font-size:14px}",
     'html': '<div class="fs15"><div class="ico">🦃 🍁 🌽</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    # ========== Indian regional festivals ==========
    {'title': 'Onam Pookalam Kerala', 'desc': 'Kerala Onam with pookalam flowers.',
     'css': ".fs16{width:520px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#fff8e1,#fff3e0);color:#bf360c;text-align:center;font-family:Georgia,serif;border:6px solid #ff6f00;border-radius:14px}.fs16 .ico{font-size:50px}.fs16 h1{font-size:44px;margin:14px 0;font-style:italic;color:#bf360c}.fs16 .greet{font-size:17px;color:#e65100;margin:10px 0}.fs16 .msg{font-size:14px;line-height:1.7;margin:14px 30px;color:#5d4037}.fs16 .from{margin-top:18px;border-top:2px solid #ff6f00;padding-top:14px;font-size:14px}",
     'html': '<div class="fs16"><div class="ico">🌸 🪷 🌺</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Pongal Harvest Tamil', 'desc': 'South Indian Pongal harvest card.',
     'css': ".fs17{width:520px;margin:30px auto;padding:50px 40px;background:linear-gradient(180deg,#fff176,#ffd54f);color:#3e2723;text-align:center;font-family:Georgia,serif;border:8px solid #bf360c}.fs17 .ico{font-size:54px}.fs17 h1{font-size:44px;margin:14px 0;color:#bf360c;font-weight:bold}.fs17 .greet{font-size:17px;color:#5d4037;margin:10px 0}.fs17 .msg{font-size:14px;line-height:1.7;margin:14px 30px}.fs17 .from{margin-top:18px;border-top:2px solid #bf360c;padding-top:14px;font-size:14px;color:#bf360c}",
     'html': '<div class="fs17"><div class="ico">🌾 🍚 🐄</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Karva Chauth Romance', 'desc': 'Romantic Karva Chauth card.',
     'css': ".fs18{width:520px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#ad1457,#880e4f);color:#fff;text-align:center;font-family:Georgia,serif;border:3px double #f5c842;border-radius:14px;box-shadow:0 24px 60px rgba(173,20,87,.4)}.fs18 .ico{font-size:50px;color:#f5c842}.fs18 h1{font-size:42px;margin:14px 0;font-style:italic;color:#f5c842}.fs18 .greet{font-size:17px;margin:10px 0;color:#fce4ec}.fs18 .msg{font-size:14px;line-height:1.7;margin:14px 30px;color:#fce4ec}.fs18 .from{margin-top:18px;border-top:1px solid #f5c842;padding-top:14px;font-size:14px}",
     'html': '<div class="fs18"><div class="ico">🌙 ❤ 🌙</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Lohri Bonfire Punjabi', 'desc': 'Punjabi Lohri bonfire card.',
     'css': ".fs19{width:520px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#bf360c,#ff6f00);color:#fff;text-align:center;font-family:Georgia,serif;border:6px solid #ffd54f;border-radius:14px}.fs19 .ico{font-size:54px}.fs19 h1{font-size:44px;margin:14px 0;font-style:italic;color:#ffd54f}.fs19 .greet{font-size:17px;margin:10px 0;font-weight:bold}.fs19 .msg{font-size:14px;line-height:1.7;margin:14px 30px}.fs19 .from{margin-top:18px;border-top:2px solid #ffd54f;padding-top:14px;font-size:14px;color:#ffd54f}",
     'html': '<div class="fs19"><div class="ico">🔥 🥜 🪘</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Bihu Assam Joy', 'desc': 'Assamese Bihu festival card.',
     'css': ".fs20{width:520px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#ffeb3b,#fdd835);color:#3e2723;text-align:center;font-family:Georgia,serif;border:6px solid #c62828;border-radius:14px}.fs20 .ico{font-size:50px}.fs20 h1{font-size:44px;margin:14px 0;color:#c62828;font-style:italic}.fs20 .greet{font-size:17px;color:#bf360c;margin:10px 0;font-weight:bold}.fs20 .msg{font-size:14px;line-height:1.7;margin:14px 30px;color:#5d4037}.fs20 .from{margin-top:18px;border-top:2px solid #c62828;padding-top:14px;font-size:14px}",
     'html': '<div class="fs20"><div class="ico">💃 🪘 🌾</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— {{ sender }}</div></div>'},

    {'title': 'Janmashtami Krishna', 'desc': 'Lord Krishna Janmashtami card.',
     'css': ".fs21{width:520px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#1a237e,#3949ab);color:#fff;text-align:center;font-family:Georgia,serif;border:4px solid #ffd54f;border-radius:14px;box-shadow:0 24px 60px rgba(26,35,126,.4)}.fs21 .ico{font-size:54px;color:#ffd54f}.fs21 h1{font-size:42px;margin:14px 0;font-style:italic;color:#ffd54f}.fs21 .greet{font-size:17px;margin:10px 0;color:#bbdefb}.fs21 .msg{font-size:14px;line-height:1.7;margin:14px 30px;color:#e3f2fd}.fs21 .from{margin-top:18px;border-top:1px solid #ffd54f;padding-top:14px;font-size:14px;color:#ffd54f}",
     'html': '<div class="fs21"><div class="ico">🦚 🪈 🪔</div><h1>{{ festival }}</h1><div class="greet">{{ greeting }}</div><div class="msg">{{ message }}</div><div class="from">— Hari Bol! {{ sender }}</div></div>'},
]


# ============================================================
# FLYERS / POSTERS (15)
# ============================================================
FLYERS = [
    {'title': 'Bold Sale', 'desc': 'Massive bold sale flyer.',
     'css': ".fl1{width:480px;margin:30px auto;padding:40px;background:#e53935;color:#fff;text-align:center;font-family:'Segoe UI',sans-serif;border:4px dashed #fff;box-shadow:0 24px 60px rgba(229,57,53,.4)}.fl1 h1{font-size:60px;margin:0;font-weight:900;letter-spacing:2px}.fl1 .sub{font-size:20px;margin:8px 0 18px;font-weight:600}.fl1 .body{font-size:14px;line-height:1.6;margin:14px 20px}.fl1 .info{margin-top:18px;background:#fff;color:#e53935;padding:14px;font-weight:bold;border-radius:8px}",
     'html': '<div class="fl1"><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div><div class="body">{{ body }}</div><div class="info">{{ date }}<br>{{ venue }}<br>{{ contact }}</div></div>'},

    {'title': 'Modern Event', 'desc': 'Sleek event poster.',
     'css': ".fl2{width:480px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;text-align:center;font-family:'Segoe UI',sans-serif;border-radius:14px;box-shadow:0 24px 60px rgba(102,126,234,.4)}.fl2 h1{font-size:48px;margin:0;font-weight:900}.fl2 .sub{font-size:18px;margin:8px 0 18px;opacity:.9}.fl2 .body{font-size:14px;line-height:1.6;margin:14px 20px}.fl2 .info{margin-top:18px;background:rgba(0,0,0,.2);padding:14px;border-radius:10px;font-size:14px}",
     'html': '<div class="fl2"><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div><div class="body">{{ body }}</div><div class="info">{{ date }}<br>{{ venue }}<br>{{ contact }}</div></div>'},

    {'title': 'Minimal Black', 'desc': 'Clean minimal poster.',
     'css': ".fl3{width:480px;margin:30px auto;padding:60px 40px;background:#fff;color:#000;text-align:center;font-family:'Helvetica',sans-serif;border:2px solid #000}.fl3 h1{font-size:54px;margin:0;letter-spacing:3px;font-weight:900}.fl3 .sub{font-size:13px;letter-spacing:6px;text-transform:uppercase;margin:14px 0 30px;color:#666}.fl3 .body{font-size:14px;line-height:1.7;margin:14px 30px;color:#444}.fl3 .info{margin-top:24px;border-top:2px solid #000;padding-top:14px;font-size:13px;letter-spacing:1px}",
     'html': '<div class="fl3"><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div><div class="body">{{ body }}</div><div class="info">{{ date }}<br>{{ venue }} · {{ contact }}</div></div>'},

    {'title': 'Music Concert', 'desc': 'Vibrant music event poster.',
     'css': ".fl4{width:480px;margin:30px auto;padding:50px 40px;background:#000;color:#fff;text-align:center;font-family:'Segoe UI',sans-serif;border:3px solid #ff00ff;box-shadow:0 0 40px rgba(255,0,255,.3)}.fl4 h1{font-size:54px;margin:0;color:#ff00ff;text-shadow:0 0 20px #ff00ff;font-weight:900}.fl4 .sub{font-size:18px;color:#00ffea;margin:8px 0 18px;letter-spacing:3px}.fl4 .body{font-size:14px;line-height:1.6;margin:14px 20px;color:#ddd}.fl4 .info{margin-top:18px;font-size:14px;color:#ffd600}",
     'html': '<div class="fl4"><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div><div class="body">{{ body }}</div><div class="info">{{ date }}<br>{{ venue }}<br>{{ contact }}</div></div>'},

    {'title': 'Workshop', 'desc': 'Educational workshop flyer.',
     'css': ".fl5{width:480px;margin:30px auto;padding:50px 40px;background:#fff;color:#222;text-align:center;font-family:'Segoe UI',sans-serif;border-top:14px solid #1976d2;box-shadow:0 24px 60px rgba(25,118,210,.2)}.fl5 h1{font-size:42px;margin:0;color:#0d47a1}.fl5 .sub{color:#1976d2;font-size:14px;letter-spacing:4px;text-transform:uppercase;margin:8px 0 24px}.fl5 .body{font-size:14px;line-height:1.7;margin:14px 20px;color:#444}.fl5 .info{margin-top:18px;background:#e3f2fd;padding:14px;border-radius:8px;font-size:14px;color:#0d47a1}",
     'html': '<div class="fl5"><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div><div class="body">{{ body }}</div><div class="info">{{ date }}<br>{{ venue }}<br>{{ contact }}</div></div>'},

    {'title': 'Yoga Wellness', 'desc': 'Calm wellness flyer.',
     'css': ".fl6{width:480px;margin:30px auto;padding:50px 40px;background:#f1f8e9;color:#33691e;text-align:center;font-family:Georgia,serif;border:4px solid #558b2f;border-radius:18px}.fl6 .ico{font-size:46px}.fl6 h1{font-size:42px;margin:8px 0;font-style:italic;color:#1b5e20}.fl6 .sub{color:#558b2f;font-size:15px;margin:6px 0 20px}.fl6 .body{font-size:14px;line-height:1.7;margin:14px 30px}.fl6 .info{margin-top:18px;border-top:1px solid #558b2f;padding-top:14px;font-size:14px}",
     'html': '<div class="fl6"><div class="ico">🧘‍♀️</div><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div><div class="body">{{ body }}</div><div class="info">{{ date }}<br>{{ venue }}<br>{{ contact }}</div></div>'},

    {'title': 'Food Festival', 'desc': 'Tasty food event poster.',
     'css': ".fl7{width:480px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#ff6f00,#bf360c);color:#fff;text-align:center;font-family:Georgia,serif;border-radius:14px;box-shadow:0 24px 60px rgba(191,54,12,.4)}.fl7 .ico{font-size:50px}.fl7 h1{font-size:46px;margin:8px 0;font-weight:900;font-style:italic}.fl7 .sub{font-size:16px;opacity:.95;margin:6px 0 18px}.fl7 .body{font-size:14px;line-height:1.7;margin:14px 30px}.fl7 .info{margin-top:18px;background:rgba(0,0,0,.2);padding:14px;border-radius:8px;font-size:14px}",
     'html': '<div class="fl7"><div class="ico">🍕 🍔 🌮</div><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div><div class="body">{{ body }}</div><div class="info">{{ date }}<br>{{ venue }}<br>{{ contact }}</div></div>'},

    {'title': 'Fitness Gym', 'desc': 'High-energy gym flyer.',
     'css': ".fl8{width:480px;margin:30px auto;padding:50px 40px;background:#212121;color:#fff;text-align:center;font-family:'Segoe UI',sans-serif;border:4px solid #ffd600;border-radius:14px}.fl8 .ico{font-size:46px;color:#ffd600}.fl8 h1{font-size:46px;margin:6px 0;color:#ffd600;font-weight:900;letter-spacing:2px}.fl8 .sub{font-size:16px;letter-spacing:4px;text-transform:uppercase;margin:6px 0 18px}.fl8 .body{font-size:14px;line-height:1.7;margin:14px 30px;color:#ddd}.fl8 .info{margin-top:18px;background:#ffd600;color:#212121;padding:14px;border-radius:8px;font-weight:bold}",
     'html': '<div class="fl8"><div class="ico">💪</div><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div><div class="body">{{ body }}</div><div class="info">{{ date }}<br>{{ venue }}<br>{{ contact }}</div></div>'},

    {'title': 'Real Estate Open House', 'desc': 'Property listing poster.',
     'css': ".fl9{width:480px;margin:30px auto;padding:50px 40px;background:#fff;color:#222;text-align:center;font-family:'Segoe UI',sans-serif;border-bottom:14px solid #ffc107;box-shadow:0 24px 60px rgba(0,0,0,.15)}.fl9 .ico{font-size:46px}.fl9 h1{font-size:42px;margin:8px 0;color:#37474f;font-weight:900}.fl9 .sub{color:#546e7a;font-size:15px;letter-spacing:3px;text-transform:uppercase;margin:6px 0 20px}.fl9 .body{font-size:14px;line-height:1.7;margin:14px 30px;color:#555}.fl9 .info{margin-top:18px;background:#37474f;color:#ffc107;padding:14px;border-radius:8px}",
     'html': '<div class="fl9"><div class="ico">🏠</div><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div><div class="body">{{ body }}</div><div class="info">{{ date }}<br>{{ venue }}<br>{{ contact }}</div></div>'},

    {'title': 'Charity Event', 'desc': 'Cause-driven charity flyer.',
     'css': ".fl10{width:480px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#11998e,#38ef7d);color:#fff;text-align:center;font-family:Georgia,serif;border-radius:18px;box-shadow:0 24px 60px rgba(17,153,142,.4)}.fl10 .ico{font-size:46px}.fl10 h1{font-size:42px;margin:8px 0;font-style:italic;font-weight:900}.fl10 .sub{font-size:15px;margin:6px 0 18px;opacity:.95}.fl10 .body{font-size:14px;line-height:1.7;margin:14px 30px}.fl10 .info{margin-top:18px;background:rgba(0,0,0,.2);padding:14px;border-radius:8px}",
     'html': '<div class="fl10"><div class="ico">❤</div><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div><div class="body">{{ body }}</div><div class="info">{{ date }}<br>{{ venue }}<br>{{ contact }}</div></div>'},

    {'title': 'Garage Sale', 'desc': 'Friendly garage sale poster.',
     'css': ".fl11{width:480px;margin:30px auto;padding:50px 40px;background:#fff8e1;color:#3e2723;text-align:center;font-family:'Comic Sans MS','Segoe UI',sans-serif;border:6px dashed #f57f17;border-radius:14px}.fl11 .ico{font-size:46px}.fl11 h1{font-size:46px;margin:8px 0;color:#bf360c;font-weight:900}.fl11 .sub{color:#e65100;font-size:16px;margin:6px 0 18px}.fl11 .body{font-size:14px;line-height:1.7;margin:14px 30px}.fl11 .info{margin-top:18px;font-size:14px}",
     'html': '<div class="fl11"><div class="ico">🏷</div><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div><div class="body">{{ body }}</div><div class="info">{{ date }}<br>{{ venue }}<br>{{ contact }}</div></div>'},

    {'title': 'Art Exhibition', 'desc': 'Gallery art exhibit flyer.',
     'css': ".fl12{width:480px;margin:30px auto;padding:60px 40px;background:#fff;color:#222;text-align:center;font-family:'Playfair Display',Georgia,serif;border:1px solid #000;outline:6px solid #fff;outline-offset:-12px;box-shadow:0 24px 60px rgba(0,0,0,.15)}.fl12 .small{font-size:11px;letter-spacing:6px;color:#666;text-transform:uppercase}.fl12 h1{font-size:48px;margin:14px 0;font-style:italic}.fl12 .sub{font-size:14px;color:#666;margin:6px 0 24px;font-style:italic}.fl12 .body{font-size:14px;line-height:1.7;margin:14px 30px;color:#555}.fl12 .info{margin-top:18px;border-top:1px solid #000;padding-top:14px;font-size:13px}",
     'html': '<div class="fl12"><div class="small">YOU\'RE INVITED</div><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div><div class="body">{{ body }}</div><div class="info">{{ date }}<br>{{ venue }} · {{ contact }}</div></div>'},

    {'title': 'Tech Conference', 'desc': 'Modern tech event poster.',
     'css': ".fl13{width:480px;margin:30px auto;padding:50px 40px;background:#0d1117;color:#c9d1d9;text-align:center;font-family:'Segoe UI',sans-serif;border:1px solid #30363d}.fl13 .ico{font-size:34px;color:#58a6ff;letter-spacing:8px}.fl13 h1{font-size:46px;margin:14px 0 0;color:#58a6ff;font-weight:900}.fl13 .sub{color:#7ee787;font-size:14px;letter-spacing:4px;text-transform:uppercase;margin:6px 0 24px}.fl13 .body{font-size:14px;line-height:1.7;margin:14px 30px;color:#8b949e}.fl13 .info{margin-top:18px;background:#161b22;padding:14px;border-radius:6px;border:1px solid #30363d;color:#fff}",
     'html': '<div class="fl13"><div class="ico">◆ ◆ ◆</div><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div><div class="body">{{ body }}</div><div class="info">{{ date }}<br>{{ venue }}<br>{{ contact }}</div></div>'},

    {'title': 'Beauty Salon', 'desc': 'Elegant beauty service flyer.',
     'css': ".fl14{width:480px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#fce4ec,#f8bbd0);color:#880e4f;text-align:center;font-family:Georgia,serif;border:2px solid #ec407a;border-radius:18px}.fl14 .ico{font-size:46px}.fl14 h1{font-size:42px;margin:8px 0;font-style:italic;color:#ad1457}.fl14 .sub{color:#ec407a;font-size:15px;letter-spacing:3px;text-transform:uppercase;margin:6px 0 18px}.fl14 .body{font-size:14px;line-height:1.7;margin:14px 30px;color:#5d4037}.fl14 .info{margin-top:18px;background:#fff;padding:14px;border-radius:10px}",
     'html': '<div class="fl14"><div class="ico">💄</div><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div><div class="body">{{ body }}</div><div class="info">{{ date }}<br>{{ venue }}<br>{{ contact }}</div></div>'},

    {'title': 'Discount 50%', 'desc': 'Big discount offer flyer.',
     'css': ".fl15{width:480px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#ffd600,#ff6f00);color:#212121;text-align:center;font-family:'Segoe UI',sans-serif;border-radius:18px;box-shadow:0 24px 60px rgba(255,111,0,.4)}.fl15 .big{font-size:90px;font-weight:900;line-height:1;text-shadow:4px 4px 0 rgba(255,255,255,.3)}.fl15 h1{font-size:36px;margin:8px 0 0;font-weight:900}.fl15 .sub{font-size:16px;margin:8px 0 18px}.fl15 .body{font-size:14px;line-height:1.7;margin:14px 30px}.fl15 .info{margin-top:18px;background:#212121;color:#ffd600;padding:14px;border-radius:8px;font-weight:bold}",
     'html': '<div class="fl15"><div class="big">50%</div><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div><div class="body">{{ body }}</div><div class="info">{{ date }}<br>{{ venue }}<br>{{ contact }}</div></div>'},
]


# ============================================================
# MENU CARDS (15)
# ============================================================
MENUS = [
    {'title': 'Classic Restaurant', 'desc': 'Traditional restaurant menu.',
     'css': ".mn1{width:480px;margin:30px auto;padding:40px;background:#fffaf3;color:#3e2723;font-family:Georgia,serif;border:6px double #6d4c41;text-align:center}.mn1 h1{font-size:38px;margin:0;font-style:italic;color:#5d4037}.mn1 .tag{font-size:13px;letter-spacing:3px;color:#8d6e63;text-transform:uppercase;margin:6px 0 24px}.mn1 .item{display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px dashed #8d6e63;font-size:15px;text-align:left}.mn1 .item .name{flex:1}.mn1 .item .price{font-weight:bold;color:#5d4037}",
     'html': '<div class="mn1"><h1>{{ restaurant }}</h1><div class="tag">{{ tagline }}</div>{% for it in items %}<div class="item"><span>{{ it.name }}{% if it.desc %} <em style="font-weight:normal;opacity:.7;font-size:.85em">— {{ it.desc }}</em>{% endif %}</span><span class="price">{{ it.price }}</span></div>{% endfor %}</div>'},

    {'title': 'Modern Cafe', 'desc': 'Sleek modern cafe menu.',
     'css': ".mn2{width:480px;margin:30px auto;padding:40px;background:#fff;color:#222;font-family:'Segoe UI',sans-serif;border-top:8px solid #00897b;border-bottom:8px solid #00897b}.mn2 h1{font-size:36px;margin:0;color:#004d40;text-align:center}.mn2 .tag{text-align:center;color:#00897b;font-size:13px;letter-spacing:3px;text-transform:uppercase;margin:6px 0 24px}.mn2 .item{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #e0f2f1;font-size:15px}.mn2 .price{color:#00897b;font-weight:bold}",
     'html': '<div class="mn2"><h1>{{ restaurant }}</h1><div class="tag">{{ tagline }}</div>{% for it in items %}<div class="item"><span>{{ it.name }}{% if it.desc %} <em style="font-weight:normal;opacity:.7;font-size:.85em">— {{ it.desc }}</em>{% endif %}</span><span class="price">{{ it.price }}</span></div>{% endfor %}</div>'},

    {'title': 'Dark Bistro', 'desc': 'Moody dark bistro menu.',
     'css': ".mn3{width:480px;margin:30px auto;padding:40px;background:#1a1a1a;color:#f5c842;font-family:'Playfair Display',Georgia,serif;border:1px solid #f5c842}.mn3 h1{font-size:38px;margin:0;text-align:center;font-style:italic;color:#fff}.mn3 .tag{text-align:center;font-size:12px;letter-spacing:5px;text-transform:uppercase;margin:6px 0 24px}.mn3 .item{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #333;font-size:15px;color:#ddd}.mn3 .item .price{color:#f5c842;font-weight:bold}",
     'html': '<div class="mn3"><h1>{{ restaurant }}</h1><div class="tag">{{ tagline }}</div>{% for it in items %}<div class="item"><span>{{ it.name }}{% if it.desc %} <em style="font-weight:normal;opacity:.7;font-size:.85em">— {{ it.desc }}</em>{% endif %}</span><span class="price">{{ it.price }}</span></div>{% endfor %}</div>'},

    {'title': 'Italian Trattoria', 'desc': 'Italian restaurant menu.',
     'css': ".mn4{width:480px;margin:30px auto;padding:40px;background:#fff;color:#3e2723;font-family:Georgia,serif;border:4px double #c62828;text-align:center}.mn4 h1{font-size:38px;margin:0;font-style:italic;color:#b71c1c}.mn4 .tag{font-size:13px;color:#388e3c;margin:6px 0 24px;font-style:italic}.mn4 .item{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #ffcdd2;font-size:15px;text-align:left}.mn4 .price{color:#b71c1c;font-weight:bold}",
     'html': '<div class="mn4"><h1>{{ restaurant }}</h1><div class="tag">{{ tagline }}</div>{% for it in items %}<div class="item"><span>{{ it.name }}{% if it.desc %} <em style="font-weight:normal;opacity:.7;font-size:.85em">— {{ it.desc }}</em>{% endif %}</span><span class="price">{{ it.price }}</span></div>{% endfor %}</div>'},

    {'title': 'Vintage Diner', 'desc': 'Retro American diner menu.',
     'css': ".mn5{width:480px;margin:30px auto;padding:40px;background:#fff8e1;color:#5d4037;font-family:'Comic Sans MS','Segoe UI',sans-serif;border:6px dashed #ff8f00;text-align:center}.mn5 h1{font-size:38px;margin:0;color:#bf360c;font-weight:bold}.mn5 .tag{font-size:14px;color:#e65100;margin:6px 0 24px}.mn5 .item{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px dashed #ff8f00;font-size:15px;text-align:left}.mn5 .price{font-weight:bold;color:#bf360c}",
     'html': '<div class="mn5"><h1>{{ restaurant }}</h1><div class="tag">{{ tagline }}</div>{% for it in items %}<div class="item"><span>{{ it.name }}{% if it.desc %} <em style="font-weight:normal;opacity:.7;font-size:.85em">— {{ it.desc }}</em>{% endif %}</span><span class="price">{{ it.price }}</span></div>{% endfor %}</div>'},

    {'title': 'Coffee Shop', 'desc': 'Cozy coffee shop menu.',
     'css': ".mn6{width:480px;margin:30px auto;padding:40px;background:#efebe9;color:#3e2723;font-family:Georgia,serif;border-radius:14px;text-align:center}.mn6 h1{font-size:38px;margin:0;font-style:italic;color:#4e342e}.mn6 .tag{font-size:13px;color:#8d6e63;margin:6px 0 24px;letter-spacing:2px}.mn6 .item{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #d7ccc8;font-size:15px;text-align:left}.mn6 .price{font-weight:bold;color:#4e342e}",
     'html': '<div class="mn6"><h1>☕ {{ restaurant }}</h1><div class="tag">{{ tagline }}</div>{% for it in items %}<div class="item"><span>{{ it.name }}{% if it.desc %} <em style="font-weight:normal;opacity:.7;font-size:.85em">— {{ it.desc }}</em>{% endif %}</span><span class="price">{{ it.price }}</span></div>{% endfor %}</div>'},

    {'title': 'Sushi Bar', 'desc': 'Japanese sushi menu.',
     'css': ".mn7{width:480px;margin:30px auto;padding:40px;background:#fff;color:#222;font-family:Georgia,serif;border:2px solid #d32f2f;text-align:center}.mn7 h1{font-size:38px;margin:0;color:#b71c1c}.mn7 .tag{font-size:13px;color:#666;margin:6px 0 24px;letter-spacing:3px}.mn7 .item{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #ffcdd2;font-size:15px;text-align:left}.mn7 .price{font-weight:bold;color:#b71c1c}",
     'html': '<div class="mn7"><h1>🍣 {{ restaurant }}</h1><div class="tag">{{ tagline }}</div>{% for it in items %}<div class="item"><span>{{ it.name }}{% if it.desc %} <em style="font-weight:normal;opacity:.7;font-size:.85em">— {{ it.desc }}</em>{% endif %}</span><span class="price">{{ it.price }}</span></div>{% endfor %}</div>'},

    {'title': 'Pizza Joint', 'desc': 'Casual pizza place menu.',
     'css': ".mn8{width:480px;margin:30px auto;padding:40px;background:#fff;color:#222;font-family:'Segoe UI',sans-serif;border-top:14px solid #c62828;border-bottom:14px solid #2e7d32;text-align:center}.mn8 h1{font-size:38px;margin:0;color:#c62828;font-weight:900}.mn8 .tag{color:#2e7d32;font-size:13px;letter-spacing:3px;text-transform:uppercase;margin:6px 0 24px}.mn8 .item{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px dashed #ccc;font-size:15px;text-align:left}.mn8 .price{font-weight:bold;color:#c62828}",
     'html': '<div class="mn8"><h1>🍕 {{ restaurant }}</h1><div class="tag">{{ tagline }}</div>{% for it in items %}<div class="item"><span>{{ it.name }}{% if it.desc %} <em style="font-weight:normal;opacity:.7;font-size:.85em">— {{ it.desc }}</em>{% endif %}</span><span class="price">{{ it.price }}</span></div>{% endfor %}</div>'},

    {'title': 'Indian Dhaba', 'desc': 'Authentic Indian dhaba menu.',
     'css': ".mn9{width:480px;margin:30px auto;padding:40px;background:linear-gradient(135deg,#fff8e1,#ffe0b2);color:#3e2723;font-family:Georgia,serif;border:4px solid #bf360c;border-radius:14px;text-align:center}.mn9 h1{font-size:38px;margin:0;color:#bf360c;font-weight:bold}.mn9 .tag{font-size:14px;color:#e65100;margin:6px 0 24px;font-style:italic}.mn9 .item{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px dotted #bf360c;font-size:15px;text-align:left}.mn9 .price{font-weight:bold;color:#bf360c}",
     'html': '<div class="mn9"><h1>{{ restaurant }}</h1><div class="tag">{{ tagline }}</div>{% for it in items %}<div class="item"><span>{{ it.name }}{% if it.desc %} <em style="font-weight:normal;opacity:.7;font-size:.85em">— {{ it.desc }}</em>{% endif %}</span><span class="price">{{ it.price }}</span></div>{% endfor %}</div>'},

    {'title': 'Healthy Bowl', 'desc': 'Fresh healthy food menu.',
     'css': ".mn10{width:480px;margin:30px auto;padding:40px;background:#f1f8e9;color:#1b5e20;font-family:'Segoe UI',sans-serif;border-radius:18px;text-align:center}.mn10 h1{font-size:36px;margin:0;color:#33691e}.mn10 .tag{color:#558b2f;font-size:13px;letter-spacing:3px;text-transform:uppercase;margin:6px 0 24px}.mn10 .item{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #c5e1a5;font-size:15px;text-align:left}.mn10 .price{font-weight:bold;color:#558b2f}",
     'html': '<div class="mn10"><h1>🥗 {{ restaurant }}</h1><div class="tag">{{ tagline }}</div>{% for it in items %}<div class="item"><span>{{ it.name }}{% if it.desc %} <em style="font-weight:normal;opacity:.7;font-size:.85em">— {{ it.desc }}</em>{% endif %}</span><span class="price">{{ it.price }}</span></div>{% endfor %}</div>'},

    {'title': 'Ice Cream Parlor', 'desc': 'Sweet ice cream menu.',
     'css': ".mn11{width:480px;margin:30px auto;padding:40px;background:linear-gradient(135deg,#fce4ec,#f8bbd0);color:#880e4f;font-family:'Comic Sans MS','Segoe UI',sans-serif;border-radius:18px;text-align:center}.mn11 h1{font-size:38px;margin:0;color:#ad1457}.mn11 .tag{color:#ec407a;font-size:14px;margin:6px 0 24px}.mn11 .item{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px dashed #ec407a;font-size:15px;text-align:left}.mn11 .price{font-weight:bold;color:#ad1457}",
     'html': '<div class="mn11"><h1>🍦 {{ restaurant }}</h1><div class="tag">{{ tagline }}</div>{% for it in items %}<div class="item"><span>{{ it.name }}{% if it.desc %} <em style="font-weight:normal;opacity:.7;font-size:.85em">— {{ it.desc }}</em>{% endif %}</span><span class="price">{{ it.price }}</span></div>{% endfor %}</div>'},

    {'title': 'Bar & Drinks', 'desc': 'Stylish bar drinks menu.',
     'css': ".mn12{width:480px;margin:30px auto;padding:40px;background:#0d1117;color:#fff;font-family:'Playfair Display',Georgia,serif;border-top:4px solid #c9a227;border-bottom:4px solid #c9a227;text-align:center}.mn12 h1{font-size:38px;margin:0;font-style:italic;color:#c9a227}.mn12 .tag{font-size:12px;letter-spacing:5px;color:#999;text-transform:uppercase;margin:6px 0 24px}.mn12 .item{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #333;font-size:15px;text-align:left}.mn12 .price{color:#c9a227;font-weight:bold}",
     'html': '<div class="mn12"><h1>{{ restaurant }}</h1><div class="tag">{{ tagline }}</div>{% for it in items %}<div class="item"><span>{{ it.name }}{% if it.desc %} <em style="font-weight:normal;opacity:.7;font-size:.85em">— {{ it.desc }}</em>{% endif %}</span><span class="price">{{ it.price }}</span></div>{% endfor %}</div>'},

    {'title': 'French Bistro', 'desc': 'Elegant French bistro menu.',
     'css': ".mn13{width:480px;margin:30px auto;padding:40px;background:#fff;color:#3e2723;font-family:Georgia,serif;border:1px solid #000;outline:4px solid #fff;outline-offset:-8px;text-align:center}.mn13 h1{font-size:38px;margin:0;font-style:italic}.mn13 .tag{font-size:12px;letter-spacing:5px;color:#666;margin:6px 0 24px}.mn13 .item{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #ddd;font-size:15px;text-align:left}.mn13 .price{font-weight:bold}",
     'html': '<div class="mn13"><h1>{{ restaurant }}</h1><div class="tag">{{ tagline }}</div>{% for it in items %}<div class="item"><span>{{ it.name }}{% if it.desc %} <em style="font-weight:normal;opacity:.7;font-size:.85em">— {{ it.desc }}</em>{% endif %}</span><span class="price">{{ it.price }}</span></div>{% endfor %}</div>'},

    {'title': 'Burger Shack', 'desc': 'Casual burger joint menu.',
     'css': ".mn14{width:480px;margin:30px auto;padding:40px;background:#fff8e1;color:#3e2723;font-family:'Segoe UI',sans-serif;border:6px solid #ff6f00;border-radius:14px;text-align:center}.mn14 h1{font-size:38px;margin:0;color:#bf360c;font-weight:900}.mn14 .tag{color:#e65100;font-size:14px;margin:6px 0 24px;letter-spacing:2px}.mn14 .item{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px dashed #ff6f00;font-size:15px;text-align:left}.mn14 .price{font-weight:bold;color:#bf360c}",
     'html': '<div class="mn14"><h1>🍔 {{ restaurant }}</h1><div class="tag">{{ tagline }}</div>{% for it in items %}<div class="item"><span>{{ it.name }}{% if it.desc %} <em style="font-weight:normal;opacity:.7;font-size:.85em">— {{ it.desc }}</em>{% endif %}</span><span class="price">{{ it.price }}</span></div>{% endfor %}</div>'},

    {'title': 'Bakery Sweet', 'desc': 'Cute bakery menu.',
     'css': ".mn15{width:480px;margin:30px auto;padding:40px;background:#fff0f5;color:#5d4037;font-family:Georgia,serif;border:4px solid #ec407a;border-radius:18px;text-align:center}.mn15 h1{font-size:38px;margin:0;color:#ad1457;font-style:italic}.mn15 .tag{color:#ec407a;font-size:13px;letter-spacing:2px;margin:6px 0 24px}.mn15 .item{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px dashed #ec407a;font-size:15px;text-align:left}.mn15 .price{font-weight:bold;color:#ad1457}",
     'html': '<div class="mn15"><h1>🧁 {{ restaurant }}</h1><div class="tag">{{ tagline }}</div>{% for it in items %}<div class="item"><span>{{ it.name }}{% if it.desc %} <em style="font-weight:normal;opacity:.7;font-size:.85em">— {{ it.desc }}</em>{% endif %}</span><span class="price">{{ it.price }}</span></div>{% endfor %}</div>'},
]


# ============================================================
# EVENT TICKETS (15)
# ============================================================
TICKETS = [
    {'title': 'Concert Stub', 'desc': 'Classic concert ticket stub.',
     'css': ".tk1{width:540px;margin:30px auto;background:#fff;color:#222;font-family:'Segoe UI',sans-serif;display:flex;border:2px dashed #1976d2;border-radius:10px;overflow:hidden}.tk1 .left{flex:1;padding:24px;border-right:2px dashed #1976d2}.tk1 .right{width:130px;background:#0d47a1;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:14px;text-align:center}.tk1 h1{margin:0;font-size:24px;color:#0d47a1}.tk1 .info{margin-top:12px;font-size:13px;line-height:1.7;color:#444}.tk1 .label{font-size:10px;letter-spacing:2px}.tk1 .num{font-size:28px;font-weight:900;margin:6px 0}",
     'html': '<div class="tk1"><div class="left"><h1>{{ event }}</h1><div class="info">📅 {{ date }}<br>🕐 {{ time }}<br>📍 {{ venue }}<br>💺 Seat: {{ seat }}</div></div><div class="right"><div class="label">ADMIT ONE</div><div class="num">{{ price }}</div><div class="label">{{ ticket_no }}</div></div></div>'},

    {'title': 'Dark Concert', 'desc': 'Dark moody concert ticket.',
     'css': ".tk2{width:540px;margin:30px auto;background:#000;color:#fff;font-family:'Segoe UI',sans-serif;display:flex;border:2px solid #ff00ff;box-shadow:0 0 30px rgba(255,0,255,.3)}.tk2 .left{flex:1;padding:24px;border-right:2px dashed #ff00ff}.tk2 .right{width:130px;background:#ff00ff;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:14px;text-align:center}.tk2 h1{margin:0;font-size:24px;color:#ff00ff}.tk2 .info{margin-top:12px;font-size:13px;line-height:1.7;color:#ddd}.tk2 .label{font-size:10px;letter-spacing:2px;color:#fff}.tk2 .num{font-size:28px;font-weight:900;margin:6px 0;color:#fff}",
     'html': '<div class="tk2"><div class="left"><h1>{{ event }}</h1><div class="info">📅 {{ date }}<br>🕐 {{ time }}<br>📍 {{ venue }}<br>💺 {{ seat }}</div></div><div class="right"><div class="label">VIP PASS</div><div class="num">{{ price }}</div><div class="label">{{ ticket_no }}</div></div></div>'},

    {'title': 'Festival Pass', 'desc': 'Colorful festival pass.',
     'css': ".tk3{width:540px;margin:30px auto;padding:24px;background:linear-gradient(135deg,#ee0979,#ff6a00);color:#fff;font-family:'Segoe UI',sans-serif;border-radius:14px;box-shadow:0 24px 60px rgba(238,9,121,.4)}.tk3 h1{margin:0;font-size:30px;font-weight:900}.tk3 .sub{font-size:13px;opacity:.9;margin:4px 0 14px}.tk3 .info{display:flex;justify-content:space-between;background:rgba(0,0,0,.2);padding:14px;border-radius:8px;font-size:13px}",
     'html': '<div class="tk3"><h1>{{ event }}</h1><div class="sub">FESTIVAL PASS</div><div class="info"><div>{{ date }}<br>{{ time }}<br>{{ venue }}</div><div style="text-align:right">{{ price }}<br>{{ seat }}<br>#{{ ticket_no }}</div></div></div>'},

    {'title': 'Sports Match', 'desc': 'Sports event ticket.',
     'css': ".tk4{width:540px;margin:30px auto;background:#fff;color:#222;font-family:'Segoe UI',sans-serif;display:flex;border:3px solid #ff6f00}.tk4 .left{flex:1;padding:24px;border-right:3px dashed #ff6f00}.tk4 .right{width:130px;background:#ff6f00;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}.tk4 h1{margin:0;font-size:24px;color:#bf360c;font-weight:900}.tk4 .info{margin-top:12px;font-size:13px;line-height:1.7;color:#444}.tk4 .label{font-size:10px;letter-spacing:2px}.tk4 .num{font-size:28px;font-weight:900;margin:6px 0}",
     'html': '<div class="tk4"><div class="left"><h1>{{ event }}</h1><div class="info">📅 {{ date }}<br>🕐 {{ time }}<br>📍 {{ venue }}</div></div><div class="right"><div class="label">SEAT</div><div class="num">{{ seat }}</div><div class="label">{{ price }}</div></div></div>'},

    {'title': 'Theater Show', 'desc': 'Elegant theater ticket.',
     'css': ".tk5{width:540px;margin:30px auto;background:#fff8e1;color:#3e2723;font-family:Georgia,serif;display:flex;border:2px solid #c9a227}.tk5 .left{flex:1;padding:24px;border-right:2px dashed #c9a227}.tk5 .right{width:130px;background:#c9a227;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}.tk5 h1{margin:0;font-size:24px;color:#5d4037;font-style:italic}.tk5 .info{margin-top:12px;font-size:13px;line-height:1.7}.tk5 .label{font-size:10px;letter-spacing:2px}.tk5 .num{font-size:24px;margin:6px 0}",
     'html': '<div class="tk5"><div class="left"><h1>{{ event }}</h1><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>Seat: {{ seat }}</div></div><div class="right"><div class="label">ADMIT</div><div class="num">{{ price }}</div><div class="label">#{{ ticket_no }}</div></div></div>'},

    {'title': 'Movie Stub', 'desc': 'Cinema movie ticket.',
     'css': ".tk6{width:540px;margin:30px auto;background:#212121;color:#fff;font-family:'Segoe UI',sans-serif;display:flex;border:2px solid #ffd600}.tk6 .left{flex:1;padding:24px;border-right:2px dashed #ffd600}.tk6 .right{width:130px;background:#ffd600;color:#212121;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}.tk6 h1{margin:0;font-size:24px;color:#ffd600;font-weight:900}.tk6 .info{margin-top:12px;font-size:13px;line-height:1.7;color:#ccc}.tk6 .label{font-size:10px;letter-spacing:2px;font-weight:bold}.tk6 .num{font-size:28px;font-weight:900;margin:6px 0}",
     'html': '<div class="tk6"><div class="left"><h1>🎬 {{ event }}</h1><div class="info">{{ date }}<br>{{ time }}<br>{{ venue }}</div></div><div class="right"><div class="label">SEAT</div><div class="num">{{ seat }}</div><div class="label">{{ price }}</div></div></div>'},

    {'title': 'Workshop Pass', 'desc': 'Workshop access pass.',
     'css': ".tk7{width:540px;margin:30px auto;padding:24px;background:#fff;color:#222;font-family:'Segoe UI',sans-serif;border-left:8px solid #00897b;box-shadow:0 16px 40px rgba(0,137,123,.2)}.tk7 h1{margin:0;font-size:26px;color:#004d40}.tk7 .sub{color:#00897b;font-size:13px;letter-spacing:3px;text-transform:uppercase;margin:4px 0 14px}.tk7 .info{display:flex;justify-content:space-between;font-size:13px}.tk7 .info strong{color:#00897b}",
     'html': '<div class="tk7"><h1>{{ event }}</h1><div class="sub">WORKSHOP PASS</div><div class="info"><div><strong>Date:</strong> {{ date }}<br><strong>Time:</strong> {{ time }}<br><strong>Venue:</strong> {{ venue }}</div><div style="text-align:right"><strong>Seat:</strong> {{ seat }}<br><strong>Price:</strong> {{ price }}<br><strong>#</strong> {{ ticket_no }}</div></div></div>'},

    {'title': 'Boarding Pass', 'desc': 'Airline-style ticket.',
     'css': ".tk8{width:540px;margin:30px auto;background:#fff;color:#222;font-family:'Segoe UI',sans-serif;display:flex;border:1px solid #ddd;box-shadow:0 16px 40px rgba(0,0,0,.1)}.tk8 .left{flex:1;padding:20px;border-right:2px dashed #ccc}.tk8 .right{width:140px;padding:20px;background:#0d47a1;color:#fff;text-align:center}.tk8 h1{margin:0;font-size:22px;color:#0d47a1}.tk8 .left .label{font-size:9px;letter-spacing:2px;color:#666;text-transform:uppercase;margin-top:10px}.tk8 .right .label{font-size:9px;letter-spacing:2px;text-transform:uppercase}.tk8 .right .big{font-size:24px;margin:6px 0;font-weight:bold}",
     'html': '<div class="tk8"><div class="left"><h1>{{ event }}</h1><div class="label">DATE</div><div>{{ date }} · {{ time }}</div><div class="label">VENUE</div><div>{{ venue }}</div></div><div class="right"><div class="label">SEAT</div><div class="big">{{ seat }}</div><div class="label">PRICE</div><div>{{ price }}</div></div></div>'},

    {'title': 'Comedy Night', 'desc': 'Fun comedy show ticket.',
     'css': ".tk9{width:540px;margin:30px auto;padding:24px;background:linear-gradient(135deg,#f093fb,#f5576c);color:#fff;font-family:'Segoe UI',sans-serif;border-radius:14px;box-shadow:0 24px 60px rgba(245,87,108,.4)}.tk9 h1{margin:0;font-size:28px;font-weight:900}.tk9 .sub{font-size:13px;opacity:.9;margin:4px 0 14px}.tk9 .info{background:rgba(0,0,0,.2);padding:14px;border-radius:10px;font-size:13px;line-height:1.7}",
     'html': '<div class="tk9"><h1>🎤 {{ event }}</h1><div class="sub">STAND-UP COMEDY</div><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>Seat: {{ seat }} · {{ price }}<br>#{{ ticket_no }}</div></div>'},

    {'title': 'Conference Badge', 'desc': 'Professional conference badge.',
     'css': ".tk10{width:380px;margin:30px auto;padding:30px;background:#fff;color:#222;font-family:'Segoe UI',sans-serif;border:2px solid #1976d2;border-radius:14px;text-align:center;box-shadow:0 16px 40px rgba(25,118,210,.2)}.tk10 .label{font-size:11px;letter-spacing:3px;color:#1976d2;text-transform:uppercase}.tk10 h1{font-size:24px;margin:8px 0;color:#0d47a1}.tk10 .info{margin-top:14px;font-size:13px;color:#666;line-height:1.7}",
     'html': '<div class="tk10"><div class="label">ATTENDEE BADGE</div><h1>{{ event }}</h1><div class="info">{{ date }}<br>{{ venue }}<br>Seat: {{ seat }}<br><strong>{{ ticket_no }}</strong></div></div>'},

    {'title': 'VIP Gold', 'desc': 'Premium VIP pass.',
     'css': ".tk11{width:540px;margin:30px auto;background:#000;color:#f5c842;font-family:'Playfair Display',Georgia,serif;display:flex;border:2px solid #f5c842}.tk11 .left{flex:1;padding:24px;border-right:2px dashed #f5c842}.tk11 .right{width:130px;background:#f5c842;color:#000;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}.tk11 h1{margin:0;font-size:24px;font-style:italic;color:#fff}.tk11 .info{margin-top:12px;font-size:13px;line-height:1.7;color:#ddd}.tk11 .label{font-size:10px;letter-spacing:3px;font-weight:bold}.tk11 .num{font-size:24px;font-weight:900;margin:6px 0}",
     'html': '<div class="tk11"><div class="left"><h1>{{ event }}</h1><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>{{ seat }}</div></div><div class="right"><div class="label">VIP</div><div class="num">{{ price }}</div><div class="label">GOLD</div></div></div>'},

    {'title': 'Train Style', 'desc': 'Train ticket inspired design.',
     'css': ".tk12{width:540px;margin:30px auto;background:#fff8e1;color:#3e2723;font-family:'Courier New',monospace;display:flex;border:2px solid #6d4c41}.tk12 .left{flex:1;padding:20px;border-right:2px dashed #6d4c41}.tk12 .right{width:130px;padding:20px;background:#6d4c41;color:#fff;text-align:center}.tk12 h1{margin:0;font-size:20px;color:#5d4037}.tk12 .info{margin-top:12px;font-size:12px;line-height:1.6}.tk12 .num{font-size:24px;font-weight:bold;margin:8px 0}",
     'html': '<div class="tk12"><div class="left"><h1>{{ event }}</h1><div class="info">DEPART: {{ date }}<br>TIME: {{ time }}<br>FROM: {{ venue }}<br>SEAT: {{ seat }}</div></div><div class="right">FARE<div class="num">{{ price }}</div>{{ ticket_no }}</div></div>'},

    {'title': 'Holographic', 'desc': 'Futuristic holographic ticket.',
     'css': ".tk13{width:540px;margin:30px auto;padding:24px;background:linear-gradient(135deg,#0093E9,#80D0C7);color:#fff;font-family:'Segoe UI',sans-serif;border-radius:14px;box-shadow:0 24px 60px rgba(0,147,233,.4)}.tk13 h1{margin:0;font-size:28px;font-weight:900;text-shadow:2px 2px 0 rgba(0,0,0,.2)}.tk13 .sub{font-size:13px;opacity:.9;margin:4px 0 14px}.tk13 .info{background:rgba(0,0,0,.2);padding:14px;border-radius:10px;font-size:13px;line-height:1.7;display:flex;justify-content:space-between}",
     'html': '<div class="tk13"><h1>{{ event }}</h1><div class="sub">DIGITAL TICKET</div><div class="info"><div>{{ date }}<br>{{ time }}<br>{{ venue }}</div><div style="text-align:right">{{ seat }}<br>{{ price }}<br>{{ ticket_no }}</div></div></div>'},

    {'title': 'Vintage Carnival', 'desc': 'Old-school carnival ticket.',
     'css': ".tk14{width:540px;margin:30px auto;background:#fff;color:#3e2723;font-family:Georgia,serif;display:flex;border:6px double #c62828}.tk14 .left{flex:1;padding:24px;border-right:6px double #c62828}.tk14 .right{width:130px;background:#c62828;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}.tk14 h1{margin:0;font-size:24px;color:#b71c1c;font-style:italic}.tk14 .info{margin-top:12px;font-size:13px;line-height:1.7}.tk14 .label{font-size:10px;letter-spacing:3px}.tk14 .num{font-size:26px;font-weight:bold;margin:6px 0}",
     'html': '<div class="tk14"><div class="left"><h1>🎪 {{ event }}</h1><div class="info">{{ date }} · {{ time }}<br>{{ venue }}<br>{{ seat }}</div></div><div class="right"><div class="label">ADMIT ONE</div><div class="num">{{ price }}</div><div class="label">{{ ticket_no }}</div></div></div>'},

    {'title': 'Modern Minimal', 'desc': 'Clean modern ticket.',
     'css': ".tk15{width:540px;margin:30px auto;padding:24px;background:#fff;color:#222;font-family:'Helvetica',sans-serif;border:1px solid #000}.tk15 h1{margin:0;font-size:26px;letter-spacing:1px}.tk15 .sub{font-size:11px;letter-spacing:5px;color:#666;text-transform:uppercase;margin:6px 0 18px}.tk15 .info{display:flex;justify-content:space-between;font-size:13px;border-top:1px solid #000;padding-top:14px}",
     'html': '<div class="tk15"><h1>{{ event }}</h1><div class="sub">EVENT TICKET</div><div class="info"><div>{{ date }}<br>{{ time }}<br>{{ venue }}</div><div style="text-align:right">SEAT {{ seat }}<br>{{ price }}<br>#{{ ticket_no }}</div></div></div>'},
]


# ============================================================
# GIFT VOUCHERS (15)
# ============================================================
VOUCHERS = [
    {'title': 'Modern Gold', 'desc': 'Elegant gold gift voucher.',
     'css': ".vc1{width:540px;margin:30px auto;padding:40px;background:linear-gradient(135deg,#1a1a1a,#3a3a3a);color:#f5c842;font-family:'Playfair Display',Georgia,serif;border:2px solid #f5c842;text-align:center;border-radius:14px}.vc1 .small{font-size:11px;letter-spacing:6px;color:#f5c842}.vc1 h1{font-size:36px;margin:8px 0;font-style:italic;color:#fff}.vc1 .amt{font-size:60px;font-weight:900;color:#f5c842;margin:14px 0}.vc1 .brand{font-size:18px;color:#fff;margin:6px 0}.vc1 .msg{font-size:13px;font-style:italic;color:#ccc;margin:14px 30px}.vc1 .info{margin-top:18px;font-size:12px;color:#999}",
     'html': '<div class="vc1"><div class="small">GIFT VOUCHER</div><h1>{{ brand }}</h1><div class="amt">{{ amount }}</div><div class="msg">{{ message }}</div><div class="info">Code: <strong>{{ code }}</strong> · Expires: {{ expiry }}</div></div>'},

    {'title': 'Pink Romance', 'desc': 'Sweet pink gift voucher.',
     'css': ".vc2{width:540px;margin:30px auto;padding:40px;background:linear-gradient(135deg,#fce4ec,#f8bbd0);color:#880e4f;font-family:Georgia,serif;border:3px solid #ec407a;text-align:center;border-radius:18px}.vc2 .small{font-size:11px;letter-spacing:6px;color:#ec407a}.vc2 h1{font-size:34px;margin:8px 0;font-style:italic;color:#ad1457}.vc2 .amt{font-size:60px;font-weight:bold;color:#e91e63;margin:14px 0}.vc2 .msg{font-size:13px;margin:14px 30px;color:#5d4037;font-style:italic}.vc2 .info{margin-top:18px;font-size:12px;color:#ad1457}",
     'html': '<div class="vc2"><div class="small">A GIFT FOR YOU</div><h1>{{ brand }}</h1><div class="amt">{{ amount }}</div><div class="msg">{{ message }}</div><div class="info">Code: <strong>{{ code }}</strong> · Expires: {{ expiry }}</div></div>'},

    {'title': 'Birthday Gift', 'desc': 'Birthday-themed voucher.',
     'css': ".vc3{width:540px;margin:30px auto;padding:40px;background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;font-family:'Segoe UI',sans-serif;border-radius:18px;text-align:center;box-shadow:0 24px 60px rgba(102,126,234,.4)}.vc3 .ico{font-size:46px}.vc3 h1{font-size:32px;margin:8px 0;font-weight:900}.vc3 .amt{font-size:70px;font-weight:900;margin:6px 0;text-shadow:3px 3px 0 rgba(0,0,0,.2)}.vc3 .msg{font-size:13px;margin:14px 30px;opacity:.95}.vc3 .info{margin-top:18px;background:rgba(0,0,0,.2);padding:12px;border-radius:8px;font-size:12px}",
     'html': '<div class="vc3"><div class="ico">🎂 🎁 🎉</div><h1>{{ brand }}</h1><div class="amt">{{ amount }}</div><div class="msg">{{ message }}</div><div class="info">Code: <strong>{{ code }}</strong> · Expires {{ expiry }}</div></div>'},

    {'title': 'Christmas Cheer', 'desc': 'Festive Christmas voucher.',
     'css': ".vc4{width:540px;margin:30px auto;padding:40px;background:#1b5e20;color:#fff;font-family:Georgia,serif;border:6px solid #f5c842;border-radius:14px;text-align:center}.vc4 .ico{font-size:46px}.vc4 h1{font-size:32px;margin:8px 0;color:#f5c842;font-style:italic}.vc4 .amt{font-size:60px;font-weight:bold;color:#f5c842;margin:6px 0}.vc4 .msg{font-size:13px;margin:14px 30px}.vc4 .info{margin-top:18px;border-top:1px solid #f5c842;padding-top:14px;font-size:12px}",
     'html': '<div class="vc4"><div class="ico">🎄 🎁 ❄</div><h1>{{ brand }}</h1><div class="amt">{{ amount }}</div><div class="msg">{{ message }}</div><div class="info">Code: <strong>{{ code }}</strong> · Valid till {{ expiry }}</div></div>'},

    {'title': 'Minimal Black', 'desc': 'Clean monochrome voucher.',
     'css': ".vc5{width:540px;margin:30px auto;padding:50px 40px;background:#fff;color:#000;font-family:'Helvetica',sans-serif;border:2px solid #000;text-align:center}.vc5 .small{font-size:11px;letter-spacing:8px}.vc5 h1{font-size:30px;margin:14px 0;letter-spacing:2px}.vc5 .amt{font-size:70px;font-weight:900;margin:14px 0}.vc5 .msg{font-size:13px;color:#666;margin:14px 30px;font-style:italic}.vc5 .info{margin-top:18px;font-size:11px;letter-spacing:2px;border-top:1px solid #000;padding-top:14px}",
     'html': '<div class="vc5"><div class="small">GIFT CARD</div><h1>{{ brand }}</h1><div class="amt">{{ amount }}</div><div class="msg">{{ message }}</div><div class="info">CODE: {{ code }} · EXP: {{ expiry }}</div></div>'},

    {'title': 'Spa Wellness', 'desc': 'Relaxing spa voucher.',
     'css': ".vc6{width:540px;margin:30px auto;padding:40px;background:linear-gradient(135deg,#a8edea,#fed6e3);color:#37474f;font-family:Georgia,serif;border-radius:18px;text-align:center}.vc6 .ico{font-size:46px}.vc6 h1{font-size:32px;margin:8px 0;font-style:italic}.vc6 .amt{font-size:60px;font-weight:bold;color:#00897b;margin:6px 0}.vc6 .msg{font-size:13px;margin:14px 30px;font-style:italic}.vc6 .info{margin-top:18px;font-size:12px;color:#666}",
     'html': '<div class="vc6"><div class="ico">🌿 ✨</div><h1>{{ brand }}</h1><div class="amt">{{ amount }}</div><div class="msg">{{ message }}</div><div class="info">Code: <strong>{{ code }}</strong> · Expires {{ expiry }}</div></div>'},

    {'title': 'Coffee Shop', 'desc': 'Coffee shop gift card.',
     'css': ".vc7{width:540px;margin:30px auto;padding:40px;background:#efebe9;color:#3e2723;font-family:Georgia,serif;border:4px solid #6d4c41;border-radius:14px;text-align:center}.vc7 .ico{font-size:46px}.vc7 h1{font-size:32px;margin:8px 0;font-style:italic;color:#4e342e}.vc7 .amt{font-size:60px;font-weight:bold;color:#6d4c41;margin:6px 0}.vc7 .msg{font-size:13px;margin:14px 30px}.vc7 .info{margin-top:18px;border-top:1px solid #6d4c41;padding-top:14px;font-size:12px}",
     'html': '<div class="vc7"><div class="ico">☕</div><h1>{{ brand }}</h1><div class="amt">{{ amount }}</div><div class="msg">{{ message }}</div><div class="info">Code: <strong>{{ code }}</strong> · Valid till {{ expiry }}</div></div>'},

    {'title': 'Vibrant Sale', 'desc': 'Bright sale-style voucher.',
     'css': ".vc8{width:540px;margin:30px auto;padding:40px;background:linear-gradient(135deg,#ff6f00,#bf360c);color:#fff;font-family:'Segoe UI',sans-serif;border-radius:18px;text-align:center;box-shadow:0 24px 60px rgba(191,54,12,.4)}.vc8 h1{font-size:34px;margin:8px 0;font-weight:900}.vc8 .amt{font-size:80px;font-weight:900;margin:6px 0;text-shadow:3px 3px 0 rgba(0,0,0,.2)}.vc8 .msg{font-size:13px;margin:14px 30px;opacity:.95}.vc8 .info{margin-top:18px;background:rgba(0,0,0,.2);padding:12px;border-radius:8px}",
     'html': '<div class="vc8"><h1>{{ brand }}</h1><div class="amt">{{ amount }}</div><div class="msg">{{ message }}</div><div class="info">Code: <strong>{{ code }}</strong> · Expires {{ expiry }}</div></div>'},

    {'title': 'Restaurant Dining', 'desc': 'Fine dining voucher.',
     'css': ".vc9{width:540px;margin:30px auto;padding:40px;background:#fff;color:#222;font-family:'Playfair Display',Georgia,serif;border-top:6px solid #c62828;border-bottom:6px solid #c62828;text-align:center}.vc9 .small{font-size:11px;letter-spacing:5px;color:#c62828}.vc9 h1{font-size:32px;margin:8px 0;font-style:italic}.vc9 .amt{font-size:60px;font-weight:bold;color:#c62828;margin:6px 0}.vc9 .msg{font-size:13px;margin:14px 30px;font-style:italic;color:#666}.vc9 .info{margin-top:18px;font-size:12px;color:#666}",
     'html': '<div class="vc9"><div class="small">DINING VOUCHER</div><h1>{{ brand }}</h1><div class="amt">{{ amount }}</div><div class="msg">{{ message }}</div><div class="info">Code: <strong>{{ code }}</strong> · Expires {{ expiry }}</div></div>'},

    {'title': 'Tech Store', 'desc': 'Modern tech store voucher.',
     'css': ".vc10{width:540px;margin:30px auto;padding:40px;background:#0d1117;color:#c9d1d9;font-family:'Segoe UI',sans-serif;border:1px solid #30363d;text-align:center}.vc10 .small{font-size:11px;letter-spacing:5px;color:#58a6ff}.vc10 h1{font-size:32px;margin:8px 0;color:#58a6ff}.vc10 .amt{font-size:60px;font-weight:900;color:#7ee787;margin:6px 0}.vc10 .msg{font-size:13px;margin:14px 30px;color:#8b949e}.vc10 .info{margin-top:18px;background:#161b22;border:1px solid #30363d;padding:12px;border-radius:6px;font-size:12px;color:#fff}",
     'html': '<div class="vc10"><div class="small">DIGITAL GIFT CARD</div><h1>{{ brand }}</h1><div class="amt">{{ amount }}</div><div class="msg">{{ message }}</div><div class="info">CODE: <strong>{{ code }}</strong> · EXP: {{ expiry }}</div></div>'},

    {'title': 'Beauty Salon', 'desc': 'Beauty service voucher.',
     'css': ".vc11{width:540px;margin:30px auto;padding:40px;background:#fff0f5;color:#880e4f;font-family:Georgia,serif;border:3px solid #ec407a;border-radius:18px;text-align:center}.vc11 .ico{font-size:40px;color:#ec407a}.vc11 h1{font-size:32px;margin:8px 0;font-style:italic;color:#ad1457}.vc11 .amt{font-size:60px;font-weight:bold;color:#e91e63;margin:6px 0}.vc11 .msg{font-size:13px;margin:14px 30px;color:#5d4037;font-style:italic}.vc11 .info{margin-top:18px;font-size:12px}",
     'html': '<div class="vc11"><div class="ico">💄</div><h1>{{ brand }}</h1><div class="amt">{{ amount }}</div><div class="msg">{{ message }}</div><div class="info">Code: <strong>{{ code }}</strong> · Valid till {{ expiry }}</div></div>'},

    {'title': 'Fashion Store', 'desc': 'Trendy fashion voucher.',
     'css': ".vc12{width:540px;margin:30px auto;padding:40px;background:#fff;color:#222;font-family:'Segoe UI',sans-serif;border:2px solid #000;text-align:center;position:relative}.vc12::before{content:'';position:absolute;top:0;left:0;right:0;height:8px;background:linear-gradient(90deg,#000,#666,#000)}.vc12 .small{font-size:11px;letter-spacing:6px;text-transform:uppercase}.vc12 h1{font-size:36px;margin:14px 0;font-weight:900}.vc12 .amt{font-size:70px;font-weight:900;margin:6px 0}.vc12 .msg{font-size:13px;margin:14px 30px;color:#666}.vc12 .info{margin-top:18px;font-size:12px}",
     'html': '<div class="vc12"><div class="small">FASHION VOUCHER</div><h1>{{ brand }}</h1><div class="amt">{{ amount }}</div><div class="msg">{{ message }}</div><div class="info">Code: <strong>{{ code }}</strong> · Expires {{ expiry }}</div></div>'},

    {'title': 'Travel Voucher', 'desc': 'Adventure travel voucher.',
     'css': ".vc13{width:540px;margin:30px auto;padding:40px;background:linear-gradient(135deg,#0093E9,#80D0C7);color:#fff;font-family:'Segoe UI',sans-serif;border-radius:18px;text-align:center;box-shadow:0 24px 60px rgba(0,147,233,.4)}.vc13 .ico{font-size:46px}.vc13 h1{font-size:32px;margin:8px 0;font-weight:900}.vc13 .amt{font-size:70px;font-weight:900;margin:6px 0;text-shadow:3px 3px 0 rgba(0,0,0,.2)}.vc13 .msg{font-size:13px;margin:14px 30px;opacity:.95}.vc13 .info{margin-top:18px;background:rgba(0,0,0,.2);padding:12px;border-radius:8px;font-size:12px}",
     'html': '<div class="vc13"><div class="ico">✈ 🌍</div><h1>{{ brand }}</h1><div class="amt">{{ amount }}</div><div class="msg">{{ message }}</div><div class="info">Code: <strong>{{ code }}</strong> · Valid till {{ expiry }}</div></div>'},

    {'title': 'Floral Soft', 'desc': 'Soft floral voucher.',
     'css': ".vc14{width:540px;margin:30px auto;padding:40px;background:#fffaf3;color:#5d4037;font-family:Georgia,serif;border:1px solid #d7ccc8;text-align:center;box-shadow:0 24px 60px rgba(0,0,0,.1)}.vc14 .ico{font-size:30px;color:#a1887f}.vc14 h1{font-size:32px;margin:8px 0;font-style:italic;color:#4e342e}.vc14 .amt{font-size:60px;font-weight:bold;color:#8d6e63;margin:6px 0}.vc14 .msg{font-size:13px;margin:14px 30px;font-style:italic}.vc14 .info{margin-top:18px;border-top:1px solid #d7ccc8;padding-top:14px;font-size:12px}",
     'html': '<div class="vc14"><div class="ico">❀ ❀ ❀</div><h1>{{ brand }}</h1><div class="amt">{{ amount }}</div><div class="msg">{{ message }}</div><div class="info">Code: <strong>{{ code }}</strong> · Expires {{ expiry }}</div></div>'},

    {'title': 'Bold Yellow', 'desc': 'Eye-catching yellow voucher.',
     'css': ".vc15{width:540px;margin:30px auto;padding:40px;background:#ffd600;color:#212121;font-family:'Segoe UI',sans-serif;border:4px dashed #212121;text-align:center}.vc15 .small{font-size:11px;letter-spacing:5px}.vc15 h1{font-size:34px;margin:8px 0;font-weight:900}.vc15 .amt{font-size:80px;font-weight:900;margin:6px 0}.vc15 .msg{font-size:13px;margin:14px 30px;font-style:italic}.vc15 .info{margin-top:18px;background:#212121;color:#ffd600;padding:12px;border-radius:8px;font-size:12px}",
     'html': '<div class="vc15"><div class="small">GIFT VOUCHER</div><h1>{{ brand }}</h1><div class="amt">{{ amount }}</div><div class="msg">{{ message }}</div><div class="info">Code: <strong>{{ code }}</strong> · Expires {{ expiry }}</div></div>'},
]
