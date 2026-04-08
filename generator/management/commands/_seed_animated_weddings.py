"""5 animated wedding templates using pure CSS @keyframes.

These work in the live preview AND can be exported as GIFs via the
'Download GIF' button in the editor.
"""

ANIMATED_SAMPLE = {
    'bride': 'Ananya',
    'groom': 'Arjun',
    'date': 'Saturday, 14th February 2026',
    'time': '6:00 PM onwards',
    'venue': 'The Leela Palace,\nMG Road, Bangalore',
    'message': 'Together with their families, we joyfully invite you to celebrate our union.',
    'rsvp': '+91 98765 43210',
}

ANIMATED_WEDDINGS = [
    # ===== 1. Floating Petals =====
    {'title': '🎬 Floating Petals Romance', 'religion': 'animated',
     'desc': 'Animated wedding card with falling rose petals and fade-in names. (Exportable as GIF)',
     'css': """
.aw1{width:560px;height:720px;position:relative;background:linear-gradient(180deg,#fff5f7 0%,#fce4ec 100%);overflow:hidden;font-family:Georgia,serif;color:#880e4f;border:1px solid #f8bbd0;box-shadow:0 30px 70px rgba(236,64,122,.25)}
.aw1 .petal{position:absolute;font-size:24px;animation:petalFall 6s linear infinite;color:#ec407a;opacity:.8}
.aw1 .petal:nth-child(1){left:10%;animation-delay:0s;animation-duration:7s}
.aw1 .petal:nth-child(2){left:25%;animation-delay:1s;animation-duration:6s;font-size:18px}
.aw1 .petal:nth-child(3){left:45%;animation-delay:2s;animation-duration:8s}
.aw1 .petal:nth-child(4){left:65%;animation-delay:.5s;animation-duration:7s;font-size:22px}
.aw1 .petal:nth-child(5){left:85%;animation-delay:1.5s;animation-duration:6s}
.aw1 .petal:nth-child(6){left:35%;animation-delay:3s;animation-duration:7s;font-size:20px}
.aw1 .petal:nth-child(7){left:75%;animation-delay:2.5s;animation-duration:8s}
@keyframes petalFall{0%{top:-30px;transform:rotate(0deg)}100%{top:760px;transform:rotate(360deg)}}
.aw1 .content{position:relative;text-align:center;padding:80px 40px 40px;z-index:2}
.aw1 .label{font-size:11px;letter-spacing:6px;color:#ad1457;text-transform:uppercase;margin-bottom:14px;animation:fadeInUp 1s ease both}
.aw1 .ico{font-size:50px;animation:floatY 3s ease-in-out infinite;display:inline-block}
.aw1 h1{font-size:54px;margin:14px 0 6px;color:#880e4f;font-style:italic;font-weight:500;animation:fadeInUp 1s ease .3s both}
.aw1 .amp{font-size:38px;color:#ec407a;margin:6px 0;animation:scalePulse 2s ease-in-out infinite}
.aw1 h1.groom{animation:fadeInUp 1s ease .6s both}
.aw1 .msg{font-size:14px;font-style:italic;color:#ad1457;margin:18px 30px;line-height:1.7;animation:fadeInUp 1s ease .9s both}
.aw1 .info{margin-top:24px;padding-top:18px;border-top:1px solid #f8bbd0;font-size:14px;line-height:1.8;color:#880e4f;animation:fadeInUp 1s ease 1.2s both}
.aw1 .info strong{color:#ec407a;display:block;font-size:16px}
@keyframes fadeInUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
@keyframes floatY{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
@keyframes scalePulse{0%,100%{transform:scale(1)}50%{transform:scale(1.15)}}
""",
     'html': '<div class="aw1"><div class="petal">🌸</div><div class="petal">🌹</div><div class="petal">🌸</div><div class="petal">🌺</div><div class="petal">🌸</div><div class="petal">🌹</div><div class="petal">🌺</div><div class="content"><div class="label">SAVE THE DATE</div><div class="ico">💕</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1 class="groom">{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div></div>'},

    # ===== 2. Sparkling Stars Royal =====
    {'title': '🎬 Sparkling Stars Royal', 'religion': 'animated',
     'desc': 'Animated royal navy card with twinkling stars and shimmer effects.',
     'css': """
.aw2{width:560px;height:720px;position:relative;background:linear-gradient(135deg,#0f1c3f,#1a2a52);overflow:hidden;font-family:Georgia,serif;color:#fff;border:1px solid #d4af37;box-shadow:0 30px 70px rgba(15,28,63,.5)}
.aw2 .star{position:absolute;color:#d4af37;font-size:14px;animation:twinkle 1.5s ease-in-out infinite}
.aw2 .star:nth-child(1){top:10%;left:15%;animation-delay:0s}
.aw2 .star:nth-child(2){top:18%;left:80%;animation-delay:.3s;font-size:20px}
.aw2 .star:nth-child(3){top:30%;left:30%;animation-delay:.6s}
.aw2 .star:nth-child(4){top:25%;left:60%;animation-delay:.9s;font-size:16px}
.aw2 .star:nth-child(5){top:50%;left:10%;animation-delay:.4s}
.aw2 .star:nth-child(6){top:55%;left:88%;animation-delay:.7s;font-size:18px}
.aw2 .star:nth-child(7){top:75%;left:20%;animation-delay:1s}
.aw2 .star:nth-child(8){top:80%;left:75%;animation-delay:.2s;font-size:22px}
.aw2 .star:nth-child(9){top:88%;left:45%;animation-delay:.5s}
@keyframes twinkle{0%,100%{opacity:.3;transform:scale(1)}50%{opacity:1;transform:scale(1.3)}}
.aw2 .content{position:relative;text-align:center;padding:80px 40px 40px;z-index:2}
.aw2 .label{font-size:11px;letter-spacing:8px;color:#d4af37;text-transform:uppercase;margin-bottom:14px;animation:slideDown 1s ease both}
.aw2 .ico{font-size:50px;color:#d4af37;animation:rotateSlow 8s linear infinite;display:inline-block}
.aw2 h1{font-size:54px;margin:14px 0 6px;color:#fff;font-style:italic;font-weight:500;animation:slideRight 1s ease .3s both;text-shadow:0 0 20px rgba(212,175,55,.4)}
.aw2 .amp{font-size:36px;color:#d4af37;margin:6px 0;animation:goldGlow 2s ease-in-out infinite}
.aw2 h1.groom{animation:slideLeft 1s ease .6s both}
.aw2 .msg{font-size:14px;font-style:italic;color:#cbd5e1;margin:18px 30px;line-height:1.7;animation:fadeIn 1.5s ease 1s both}
.aw2 .info{margin-top:24px;padding-top:18px;border-top:1px solid #d4af37;font-size:14px;line-height:1.8;color:#cbd5e1;animation:fadeIn 1.5s ease 1.3s both}
.aw2 .info strong{color:#d4af37;display:block;font-size:16px}
@keyframes slideDown{from{opacity:0;transform:translateY(-20px)}to{opacity:1;transform:translateY(0)}}
@keyframes slideRight{from{opacity:0;transform:translateX(-30px)}to{opacity:1;transform:translateX(0)}}
@keyframes slideLeft{from{opacity:0;transform:translateX(30px)}to{opacity:1;transform:translateX(0)}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes goldGlow{0%,100%{text-shadow:0 0 8px #d4af37}50%{text-shadow:0 0 25px #d4af37,0 0 40px #d4af37}}
@keyframes rotateSlow{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
""",
     'html': '<div class="aw2"><div class="star">✦</div><div class="star">✦</div><div class="star">✦</div><div class="star">✦</div><div class="star">✦</div><div class="star">✦</div><div class="star">✦</div><div class="star">✦</div><div class="star">✦</div><div class="content"><div class="label">— SAVE THE DATE —</div><div class="ico">✦</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1 class="groom">{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div></div>'},

    # ===== 3. Pulsing Hearts =====
    {'title': '🎬 Pulsing Hearts Bloom', 'religion': 'animated',
     'desc': 'Soft pink card with pulsing hearts and blooming names animation.',
     'css': """
.aw3{width:560px;height:720px;position:relative;background:radial-gradient(circle at 30% 20%,#fff5f7,#fce4ec 70%);overflow:hidden;font-family:Georgia,serif;color:#880e4f;border:3px double #ec407a;box-shadow:0 30px 70px rgba(236,64,122,.3)}
.aw3 .heart{position:absolute;font-size:30px;color:#ec407a;animation:heartBeat 2s ease-in-out infinite,floatRise 8s ease-in infinite;opacity:.6}
.aw3 .heart:nth-child(1){left:8%;bottom:0;animation-delay:0s}
.aw3 .heart:nth-child(2){left:25%;bottom:0;animation-delay:1.5s;font-size:20px}
.aw3 .heart:nth-child(3){left:50%;bottom:0;animation-delay:3s;font-size:24px}
.aw3 .heart:nth-child(4){left:75%;bottom:0;animation-delay:.8s;font-size:18px}
.aw3 .heart:nth-child(5){left:90%;bottom:0;animation-delay:2.2s;font-size:22px}
@keyframes heartBeat{0%,100%{transform:scale(1)}50%{transform:scale(1.2)}}
@keyframes floatRise{0%{bottom:-30px;opacity:0}10%{opacity:.6}90%{opacity:.6}100%{bottom:760px;opacity:0}}
.aw3 .content{position:relative;text-align:center;padding:80px 40px 40px;z-index:2}
.aw3 .label{font-size:11px;letter-spacing:6px;color:#ad1457;text-transform:uppercase;margin-bottom:14px;animation:fadeBlur 1.2s ease both}
.aw3 .ico{font-size:60px;color:#ec407a;animation:hugeBeat 1.5s ease-in-out infinite;display:inline-block}
.aw3 h1{font-size:56px;margin:14px 0 6px;color:#880e4f;font-style:italic;font-weight:500;animation:bloom 1.2s cubic-bezier(.34,1.56,.64,1) .3s both}
.aw3 .amp{font-size:40px;color:#ec407a;margin:6px 0;animation:hugeBeat 1.5s ease-in-out infinite}
.aw3 h1.groom{animation:bloom 1.2s cubic-bezier(.34,1.56,.64,1) .6s both}
.aw3 .msg{font-size:14px;font-style:italic;color:#ad1457;margin:18px 30px;line-height:1.7;animation:fadeBlur 1.5s ease 1s both}
.aw3 .info{margin-top:24px;padding-top:18px;border-top:1px solid #ec407a;font-size:14px;line-height:1.8;color:#880e4f;animation:fadeBlur 1.5s ease 1.3s both}
.aw3 .info strong{color:#ec407a;display:block;font-size:16px}
@keyframes fadeBlur{from{opacity:0;filter:blur(8px)}to{opacity:1;filter:blur(0)}}
@keyframes bloom{0%{opacity:0;transform:scale(.5)}60%{transform:scale(1.1)}100%{opacity:1;transform:scale(1)}}
@keyframes hugeBeat{0%,100%{transform:scale(1)}50%{transform:scale(1.25)}}
""",
     'html': '<div class="aw3"><div class="heart">❤</div><div class="heart">💕</div><div class="heart">❤</div><div class="heart">💖</div><div class="heart">❤</div><div class="content"><div class="label">— OUR SPECIAL DAY —</div><div class="ico">❤</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1 class="groom">{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div></div>'},

    # ===== 4. Rotating Mandala Hindu =====
    {'title': '🎬 Rotating Mandala Hindu', 'religion': 'animated',
     'desc': 'Hindu wedding with slowly rotating mandala border and fade-in blessings.',
     'css': """
.aw4{width:560px;height:720px;position:relative;background:linear-gradient(135deg,#fffaf0,#fff8e1);overflow:hidden;font-family:Georgia,serif;color:#7a4f1d;border:6px double #c9a227;box-shadow:0 30px 70px rgba(122,0,25,.3)}
.aw4 .mandala{position:absolute;color:#c9a227;font-size:80px;opacity:.15;animation:rotateForever 30s linear infinite}
.aw4 .mandala.tl{top:-20px;left:-20px}
.aw4 .mandala.tr{top:-20px;right:-20px;animation-direction:reverse}
.aw4 .mandala.bl{bottom:-20px;left:-20px;animation-direction:reverse}
.aw4 .mandala.br{bottom:-20px;right:-20px}
@keyframes rotateForever{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
.aw4 .content{position:relative;text-align:center;padding:80px 40px 40px;z-index:2}
.aw4 .ico{font-size:50px;color:#bf360c;animation:diyaBob 2s ease-in-out infinite;display:inline-block}
.aw4 .label{font-size:13px;letter-spacing:6px;color:#bf360c;text-transform:uppercase;margin:10px 0;font-weight:bold;animation:fadeInUp 1s ease .2s both}
.aw4 .blessing{font-size:14px;color:#7a4f1d;font-style:italic;margin:14px 30px;line-height:1.7;animation:fadeInUp 1s ease .4s both}
.aw4 h1{font-size:54px;margin:14px 0 6px;color:#bf360c;font-style:italic;font-weight:500;animation:slideInBlur 1.2s ease .6s both}
.aw4 .amp{font-size:36px;color:#c9a227;margin:6px 0;animation:goldShine 2s ease-in-out infinite}
.aw4 h1.groom{animation:slideInBlur 1.2s ease .9s both}
.aw4 .msg{font-size:14px;font-style:italic;color:#5d4037;margin:18px 30px;line-height:1.7;animation:fadeInUp 1s ease 1.2s both}
.aw4 .info{margin-top:18px;padding-top:14px;border-top:1px solid #c9a227;font-size:14px;line-height:1.8;color:#5d4037;animation:fadeInUp 1s ease 1.5s both}
.aw4 .info strong{color:#bf360c;display:block;font-size:16px}
@keyframes diyaBob{0%,100%{transform:translateY(0) rotate(-3deg)}50%{transform:translateY(-6px) rotate(3deg)}}
@keyframes fadeInUp{from{opacity:0;transform:translateY(15px)}to{opacity:1;transform:translateY(0)}}
@keyframes slideInBlur{from{opacity:0;filter:blur(10px);transform:translateY(20px)}to{opacity:1;filter:blur(0);transform:translateY(0)}}
@keyframes goldShine{0%,100%{text-shadow:0 0 4px #c9a227}50%{text-shadow:0 0 16px #c9a227,0 0 28px #c9a227}}
""",
     'html': '<div class="aw4"><div class="mandala tl">❀</div><div class="mandala tr">❀</div><div class="mandala bl">❀</div><div class="mandala br">❀</div><div class="content"><div class="ico">🕉</div><div class="label">शुभ विवाह</div><div class="blessing">|| श्री गणेशाय नमः ||<br>With the blessings of our elders</div><h1>{{ bride }}</h1><div class="amp">~ WEDS ~</div><h1 class="groom">{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div></div>'},

    # ===== 5. Fireworks Celebration =====
    {'title': '🎬 Fireworks Celebration', 'religion': 'animated',
     'desc': 'Grand celebration card with bursting fireworks animation.',
     'css': """
.aw5{width:560px;height:720px;position:relative;background:linear-gradient(180deg,#1a1a2e,#16213e 50%,#0f3460);overflow:hidden;font-family:Georgia,serif;color:#fff;border:2px solid #f5c842;box-shadow:0 30px 70px rgba(0,0,0,.6)}
.aw5 .fw{position:absolute;font-size:34px;animation:burst 2.5s ease-out infinite;opacity:0}
.aw5 .fw:nth-child(1){top:15%;left:20%;animation-delay:0s}
.aw5 .fw:nth-child(2){top:10%;left:60%;animation-delay:.6s}
.aw5 .fw:nth-child(3){top:25%;left:80%;animation-delay:1.2s}
.aw5 .fw:nth-child(4){top:20%;left:10%;animation-delay:1.8s}
.aw5 .fw:nth-child(5){top:30%;left:50%;animation-delay:2.2s}
@keyframes burst{0%{opacity:0;transform:scale(0)}30%{opacity:1;transform:scale(1)}80%{opacity:.8;transform:scale(1.4)}100%{opacity:0;transform:scale(1.6)}}
.aw5 .content{position:relative;text-align:center;padding:90px 40px 40px;z-index:2}
.aw5 .label{font-size:11px;letter-spacing:8px;color:#f5c842;text-transform:uppercase;margin-bottom:14px;animation:slideDown 1s ease both}
.aw5 .ico{font-size:50px;animation:swing 2s ease-in-out infinite;display:inline-block}
.aw5 h1{font-size:54px;margin:14px 0 6px;color:#fff;font-style:italic;font-weight:500;animation:zoomIn 1.2s cubic-bezier(.34,1.56,.64,1) .3s both;text-shadow:0 0 20px rgba(245,200,66,.5)}
.aw5 .amp{font-size:38px;color:#f5c842;margin:6px 0;animation:rainbow 3s linear infinite}
.aw5 h1.groom{animation:zoomIn 1.2s cubic-bezier(.34,1.56,.64,1) .6s both}
.aw5 .msg{font-size:14px;font-style:italic;color:#cbd5e1;margin:18px 30px;line-height:1.7;animation:fadeIn 1.5s ease 1s both}
.aw5 .info{margin-top:20px;padding-top:14px;border-top:1px solid #f5c842;font-size:14px;line-height:1.8;color:#fff;animation:fadeIn 1.5s ease 1.3s both}
.aw5 .info strong{color:#f5c842;display:block;font-size:16px}
@keyframes slideDown{from{opacity:0;transform:translateY(-20px)}to{opacity:1;transform:translateY(0)}}
@keyframes swing{0%,100%{transform:rotate(-15deg)}50%{transform:rotate(15deg)}}
@keyframes zoomIn{0%{opacity:0;transform:scale(.3)}60%{transform:scale(1.1)}100%{opacity:1;transform:scale(1)}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes rainbow{0%{color:#f5c842}25%{color:#ff6b9d}50%{color:#a78bfa}75%{color:#60a5fa}100%{color:#f5c842}}
""",
     'html': '<div class="aw5"><div class="fw">🎆</div><div class="fw">✨</div><div class="fw">🎇</div><div class="fw">💥</div><div class="fw">🎆</div><div class="content"><div class="label">— GRAND CELEBRATION —</div><div class="ico">🎉</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1 class="groom">{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div></div>'},
]
