"""5 distinct best templates per category — Invoice, Voucher, Card, Certificate,
Social, Flyer, Festival, Menu, Ticket, Wedding. Each with totally unique CSS class
prefix + color palette + layout so no two look alike."""

# ============================================================
# INVOICES (5)
# ============================================================
INVOICES = [
{'title': '🎨 Modern Gradient Header', 'desc': 'Bold purple→pink gradient banner with split totals.',
 'css': """.di1{font-family:'Inter',sans-serif;background:#fff;padding:0;border-radius:18px;overflow:hidden;box-shadow:0 24px 60px rgba(124,58,237,.18)}
.di1-h{background:linear-gradient(135deg,#7c3aed 0%,#ec4899 100%);color:#fff;padding:42px 44px;display:flex;justify-content:space-between;align-items:flex-start}
.di1-h h1{margin:0;font-size:46px;font-weight:900;letter-spacing:-1px}
.di1-h .lbl{opacity:.85;font-size:11px;text-transform:uppercase;letter-spacing:2px;margin-bottom:6px}
.di1-h .v{font-size:18px;font-weight:700}
.di1-b{padding:36px 44px}
.di1-row{display:flex;justify-content:space-between;gap:30px;margin-bottom:28px}
.di1-row h4{margin:0 0 6px;font-size:10px;text-transform:uppercase;color:#7c3aed;letter-spacing:1.5px}
.di1-row p{margin:0;color:#1f2937;line-height:1.6}
.di1 table{width:100%;border-collapse:collapse;margin:18px 0}
.di1 th{background:#f5f3ff;color:#5b21b6;font-size:11px;text-transform:uppercase;letter-spacing:1px;padding:14px;text-align:left}
.di1 th:last-child,.di1 td:last-child{text-align:right}
.di1 td{padding:14px;border-bottom:1px solid #f3f4f6;color:#374151}
.di1-tot{display:flex;justify-content:flex-end;margin-top:10px}
.di1-tot div{background:linear-gradient(135deg,#7c3aed,#ec4899);color:#fff;padding:18px 32px;border-radius:14px;font-weight:900;font-size:22px}
.di1-n{margin-top:24px;padding:16px;background:#fef3c7;border-left:4px solid #f59e0b;border-radius:8px;color:#78350f;font-size:13px}""",
 'html': """<div class="di1"><div class="di1-h"><div><div class="lbl">Invoice</div><h1>{{ invoice_no }}</h1></div><div style="text-align:right"><div class="lbl">Date</div><div class="v">{{ date }}</div></div></div><div class="di1-b"><div class="di1-row"><div><h4>From</h4><p><strong>{{ company }}</strong><br>{{ company_address|linebreaksbr }}</p></div><div style="text-align:right"><h4>Bill To</h4><p><strong>{{ client }}</strong><br>{{ client_address|linebreaksbr }}</p></div></div><table><tr><th>Description</th><th>Qty</th><th>Price</th><th>Total</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="di1-tot"><div>TOTAL ₹{{ grand_total }}</div></div><div class="di1-n">{{ notes }}</div></div></div>"""},

{'title': '🎨 Minimal Black Border Pro', 'desc': 'Clean monochrome with thick black border accent.',
 'css': """.di2{font-family:'Helvetica Neue',sans-serif;background:#fff;padding:50px;border:3px solid #000;color:#000}
.di2-top{display:flex;justify-content:space-between;align-items:flex-start;border-bottom:3px solid #000;padding-bottom:24px;margin-bottom:30px}
.di2-top h1{margin:0;font-size:64px;font-weight:900;letter-spacing:-3px;line-height:.9}
.di2-top .meta{text-align:right;font-size:12px;line-height:1.8}
.di2-top .meta strong{display:block;font-size:18px;letter-spacing:1px}
.di2-cols{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-bottom:30px}
.di2-cols div{padding:18px;background:#000;color:#fff}
.di2-cols h4{margin:0 0 8px;font-size:10px;letter-spacing:2px;opacity:.7}
.di2-cols p{margin:0;font-size:14px;line-height:1.6}
.di2 table{width:100%;border-collapse:collapse}
.di2 th{background:#000;color:#fff;padding:14px;text-align:left;font-size:11px;letter-spacing:1.5px;text-transform:uppercase}
.di2 th:last-child,.di2 td:last-child{text-align:right}
.di2 td{padding:14px;border-bottom:1px solid #000}
.di2-tot{display:flex;justify-content:space-between;align-items:center;margin-top:24px;padding:24px;background:#000;color:#fff}
.di2-tot span{font-size:12px;letter-spacing:2px;text-transform:uppercase}
.di2-tot strong{font-size:32px;font-weight:900}
.di2-n{margin-top:24px;font-size:12px;line-height:1.7;border-top:1px dashed #000;padding-top:18px}""",
 'html': """<div class="di2"><div class="di2-top"><h1>INVOICE</h1><div class="meta"><strong>{{ invoice_no }}</strong>{{ date }}</div></div><div class="di2-cols"><div><h4>FROM</h4><p><strong>{{ company }}</strong><br>{{ company_address|linebreaksbr }}</p></div><div><h4>BILL TO</h4><p><strong>{{ client }}</strong><br>{{ client_address|linebreaksbr }}</p></div></div><table><tr><th>Item</th><th>Qty</th><th>Price</th><th>Total</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="di2-tot"><span>Amount Due</span><strong>₹{{ grand_total }}</strong></div><div class="di2-n">{{ notes }}</div></div>"""},

{'title': '🎨 Corporate Navy Stripes', 'desc': 'Navy professional with side stripes and clean grid.',
 'css': """.di3{font-family:'Inter',sans-serif;background:#fff;display:grid;grid-template-columns:14px 1fr;border-radius:14px;overflow:hidden;box-shadow:0 18px 48px rgba(15,23,42,.12)}
.di3-side{background:linear-gradient(180deg,#0f172a 0%,#1e40af 50%,#0ea5e9 100%)}
.di3-main{padding:42px 44px}
.di3-h{display:flex;justify-content:space-between;border-bottom:2px solid #0f172a;padding-bottom:22px;margin-bottom:24px}
.di3-h h1{margin:0;font-size:38px;color:#0f172a;font-weight:800;letter-spacing:-.5px}
.di3-h .sub{color:#64748b;font-size:13px;margin-top:4px}
.di3-h .meta{text-align:right}
.di3-h .meta div{font-size:11px;color:#64748b;text-transform:uppercase;letter-spacing:1px}
.di3-h .meta strong{font-size:18px;color:#0f172a}
.di3-grid{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:28px}
.di3-grid .box{padding:18px;background:#f8fafc;border-left:3px solid #0ea5e9;border-radius:6px}
.di3-grid h4{margin:0 0 6px;font-size:11px;color:#0ea5e9;text-transform:uppercase;letter-spacing:1.5px}
.di3-grid p{margin:0;font-size:14px;color:#1e293b;line-height:1.6}
.di3 table{width:100%;border-collapse:collapse}
.di3 th{background:#0f172a;color:#fff;padding:14px 12px;font-size:11px;text-transform:uppercase;letter-spacing:1px;text-align:left}
.di3 th:last-child,.di3 td:last-child{text-align:right}
.di3 td{padding:14px 12px;border-bottom:1px solid #e2e8f0;color:#334155}
.di3 tr:nth-child(even) td{background:#f8fafc}
.di3-tot{margin-top:18px;display:flex;justify-content:flex-end}
.di3-tot div{background:#0f172a;color:#fff;padding:14px 28px;border-radius:8px;font-weight:800;font-size:20px}
.di3-tot div span{color:#0ea5e9;margin-right:10px;font-size:12px}
.di3-n{margin-top:20px;padding:14px;background:#eff6ff;color:#1e40af;font-size:12px;border-radius:8px}""",
 'html': """<div class="di3"><div class="di3-side"></div><div class="di3-main"><div class="di3-h"><div><h1>INVOICE</h1><div class="sub">{{ company }}</div></div><div class="meta"><div># Invoice</div><strong>{{ invoice_no }}</strong><div style="margin-top:6px">Date</div><strong>{{ date }}</strong></div></div><div class="di3-grid"><div class="box"><h4>From</h4><p><strong>{{ company }}</strong><br>{{ company_address|linebreaksbr }}</p></div><div class="box"><h4>To</h4><p><strong>{{ client }}</strong><br>{{ client_address|linebreaksbr }}</p></div></div><table><tr><th>Service</th><th>Qty</th><th>Rate</th><th>Total</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="di3-tot"><div><span>TOTAL</span>₹{{ grand_total }}</div></div><div class="di3-n">{{ notes }}</div></div></div>"""},

{'title': '🎨 Creative Pink Bold Shapes', 'desc': 'Playful pink with abstract circles and bold type.',
 'css': """.di4{font-family:'Inter',sans-serif;background:#fff5f7;padding:44px;border-radius:24px;position:relative;overflow:hidden}
.di4::before{content:'';position:absolute;top:-80px;right:-80px;width:240px;height:240px;background:#ec4899;border-radius:50%;opacity:.18}
.di4::after{content:'';position:absolute;bottom:-60px;left:-60px;width:180px;height:180px;background:#f97316;border-radius:50%;opacity:.15}
.di4-h{position:relative;z-index:2;display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:30px}
.di4-h h1{margin:0;font-size:54px;font-weight:900;color:#831843;letter-spacing:-2px;line-height:.95}
.di4-h h1 span{display:block;color:#ec4899;font-size:22px;font-weight:700;margin-top:6px;letter-spacing:0}
.di4-h .badge{background:#ec4899;color:#fff;padding:14px 24px;border-radius:30px;font-weight:800;font-size:14px;box-shadow:0 8px 24px rgba(236,72,153,.4)}
.di4-info{position:relative;z-index:2;display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:24px}
.di4-info .c{background:#fff;padding:20px;border-radius:16px;box-shadow:0 6px 20px rgba(0,0,0,.05)}
.di4-info h4{margin:0 0 6px;color:#ec4899;font-size:11px;text-transform:uppercase;letter-spacing:1.5px}
.di4-info p{margin:0;color:#1f2937;font-size:14px;line-height:1.6}
.di4-info p strong{color:#831843;font-size:16px}
.di4-tbl{position:relative;z-index:2;background:#fff;border-radius:18px;padding:8px;box-shadow:0 8px 28px rgba(0,0,0,.06)}
.di4 table{width:100%;border-collapse:collapse}
.di4 th{padding:14px 16px;color:#831843;text-align:left;font-size:11px;text-transform:uppercase;letter-spacing:1.5px;border-bottom:2px solid #fce7f3}
.di4 th:last-child,.di4 td:last-child{text-align:right}
.di4 td{padding:14px 16px;color:#374151;border-bottom:1px dashed #fce7f3}
.di4-tot{position:relative;z-index:2;margin-top:20px;display:flex;justify-content:flex-end;align-items:center;gap:14px}
.di4-tot span{color:#ec4899;font-weight:700;text-transform:uppercase;font-size:12px;letter-spacing:1.5px}
.di4-tot strong{background:linear-gradient(135deg,#ec4899,#f97316);color:#fff;padding:18px 30px;border-radius:50px;font-size:24px;font-weight:900;box-shadow:0 10px 28px rgba(236,72,153,.4)}
.di4-n{position:relative;z-index:2;margin-top:18px;text-align:center;color:#9f1239;font-style:italic;font-size:13px}""",
 'html': """<div class="di4"><div class="di4-h"><h1>INVOICE<span>{{ company }}</span></h1><div class="badge">#{{ invoice_no }}</div></div><div class="di4-info"><div class="c"><h4>Bill To</h4><p><strong>{{ client }}</strong><br>{{ client_address|linebreaksbr }}</p></div><div class="c"><h4>Date</h4><p><strong>{{ date }}</strong></p></div></div><div class="di4-tbl"><table><tr><th>Item</th><th>Qty</th><th>Price</th><th>Total</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table></div><div class="di4-tot"><span>Total Due</span><strong>₹{{ grand_total }}</strong></div><div class="di4-n">{{ notes }}</div></div>"""},

{'title': '🎨 Dark Mode Neon Premium', 'desc': 'Dark slate background with electric cyan accents.',
 'css': """.di5{font-family:'JetBrains Mono','Inter',sans-serif;background:#0a0e27;padding:44px;border-radius:18px;color:#cbd5e1;border:1px solid #1e293b;box-shadow:0 24px 60px rgba(0,0,0,.4)}
.di5-h{display:flex;justify-content:space-between;align-items:flex-start;border-bottom:1px solid #1e293b;padding-bottom:24px;margin-bottom:28px}
.di5-h h1{margin:0;font-size:42px;color:#22d3ee;font-weight:900;letter-spacing:-1px;text-shadow:0 0 20px rgba(34,211,238,.4)}
.di5-h .pill{background:rgba(34,211,238,.1);color:#22d3ee;padding:8px 18px;border-radius:30px;font-size:12px;border:1px solid rgba(34,211,238,.3);font-weight:700}
.di5-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:26px}
.di5-grid div{background:rgba(34,211,238,.04);padding:18px;border-radius:10px;border-left:3px solid #22d3ee}
.di5-grid h4{margin:0 0 6px;color:#22d3ee;font-size:10px;letter-spacing:2px;text-transform:uppercase}
.di5-grid p{margin:0;color:#e2e8f0;font-size:13px;line-height:1.6}
.di5-grid p strong{color:#fff}
.di5 table{width:100%;border-collapse:collapse;background:rgba(0,0,0,.3);border-radius:10px;overflow:hidden}
.di5 th{background:rgba(34,211,238,.15);color:#22d3ee;padding:14px;text-align:left;font-size:11px;text-transform:uppercase;letter-spacing:1.5px}
.di5 th:last-child,.di5 td:last-child{text-align:right}
.di5 td{padding:14px;border-bottom:1px solid #1e293b;color:#cbd5e1}
.di5 tr:hover td{background:rgba(34,211,238,.05);color:#fff}
.di5-tot{margin-top:24px;padding:22px;background:linear-gradient(90deg,rgba(34,211,238,.1),rgba(34,211,238,.02));border:1px solid rgba(34,211,238,.3);border-radius:12px;display:flex;justify-content:space-between;align-items:center}
.di5-tot span{color:#94a3b8;font-size:12px;text-transform:uppercase;letter-spacing:2px}
.di5-tot strong{color:#22d3ee;font-size:32px;font-weight:900;text-shadow:0 0 24px rgba(34,211,238,.5)}
.di5-n{margin-top:18px;padding:14px;background:rgba(248,113,113,.05);border-left:3px solid #f87171;border-radius:6px;color:#fca5a5;font-size:12px}""",
 'html': """<div class="di5"><div class="di5-h"><h1>// INVOICE</h1><div class="pill">#{{ invoice_no }} · {{ date }}</div></div><div class="di5-grid"><div><h4>~/from</h4><p><strong>{{ company }}</strong><br>{{ company_address|linebreaksbr }}</p></div><div><h4>~/billTo</h4><p><strong>{{ client }}</strong><br>{{ client_address|linebreaksbr }}</p></div></div><table><tr><th>Service</th><th>Qty</th><th>Rate</th><th>Total</th></tr>{% for it in items %}<tr><td>{{ it.desc }}</td><td>{{ it.qty }}</td><td>₹{{ it.price }}</td><td>₹{{ it.total }}</td></tr>{% endfor %}</table><div class="di5-tot"><span>$ amount_due</span><strong>₹{{ grand_total }}</strong></div><div class="di5-n">// {{ notes }}</div></div>"""},
]

# ============================================================
# VOUCHERS (5)
# ============================================================
VOUCHERS = [
{'title': '🎨 Luxury Black Gold Foil', 'desc': 'Premium black with gold foil borders and serif elegance.',
 'css': """.dv1{font-family:'Playfair Display',serif;background:#0a0a0a;color:#f5d68a;padding:50px;border:2px solid #d4af37;border-radius:14px;text-align:center;position:relative}
.dv1::before,.dv1::after{content:'';position:absolute;left:14px;right:14px;height:1px;background:linear-gradient(90deg,transparent,#d4af37,transparent)}
.dv1::before{top:14px}.dv1::after{bottom:14px}
.dv1-brand{font-size:14px;letter-spacing:8px;text-transform:uppercase;margin-bottom:18px;color:#d4af37}
.dv1-title{font-size:54px;font-weight:900;letter-spacing:-1px;margin:10px 0;background:linear-gradient(180deg,#fde68a,#d4af37);-webkit-background-clip:text;background-clip:text;color:transparent}
.dv1-amt{font-size:88px;font-weight:900;color:#d4af37;line-height:1;margin:14px 0;text-shadow:0 4px 24px rgba(212,175,55,.3)}
.dv1-msg{font-style:italic;color:#fef3c7;margin:18px auto;max-width:340px;line-height:1.6;font-size:15px}
.dv1-code{display:inline-block;margin-top:18px;padding:14px 28px;background:rgba(212,175,55,.1);border:1px dashed #d4af37;border-radius:8px;font-family:monospace;color:#fde68a;letter-spacing:3px;font-size:18px}
.dv1-exp{margin-top:14px;font-size:12px;letter-spacing:2px;color:#d4af37;text-transform:uppercase}""",
 'html': """<div class="dv1"><div class="dv1-brand">{{ brand }}</div><div class="dv1-title">Gift Voucher</div><div class="dv1-amt">{{ amount }}</div><div class="dv1-msg">{{ message }}</div><div class="dv1-code">{{ code }}</div><div class="dv1-exp">Valid until {{ expiry }}</div></div>"""},

{'title': '🎨 Festive Red Celebration', 'desc': 'Vibrant red with gold ornaments — diwali gift style.',
 'css': """.dv2{font-family:'Inter',sans-serif;background:linear-gradient(135deg,#dc2626 0%,#991b1b 100%);color:#fff;padding:48px;border-radius:18px;text-align:center;position:relative;overflow:hidden;box-shadow:0 24px 60px rgba(220,38,38,.3)}
.dv2::before{content:'✦';position:absolute;top:20px;left:30px;font-size:40px;color:#fbbf24;opacity:.6}
.dv2::after{content:'✦';position:absolute;bottom:20px;right:30px;font-size:40px;color:#fbbf24;opacity:.6}
.dv2-ornament{font-size:32px;color:#fbbf24;margin-bottom:10px;letter-spacing:14px}
.dv2-brand{text-transform:uppercase;letter-spacing:4px;font-size:14px;color:#fde68a;font-weight:700}
.dv2-title{font-size:38px;font-weight:900;margin:14px 0;color:#fff}
.dv2-amt{display:inline-block;background:#fbbf24;color:#7f1d1d;padding:24px 50px;border-radius:14px;font-size:60px;font-weight:900;margin:14px 0;box-shadow:0 12px 30px rgba(251,191,36,.4),inset 0 -4px 0 rgba(0,0,0,.15)}
.dv2-msg{max-width:340px;margin:18px auto;color:#fef3c7;line-height:1.6;font-size:14px}
.dv2-code{display:flex;justify-content:center;align-items:center;gap:14px;margin-top:18px;padding:14px;background:rgba(0,0,0,.3);border-radius:10px}
.dv2-code span{font-family:monospace;color:#fbbf24;letter-spacing:3px;font-size:18px;font-weight:800}
.dv2-exp{margin-top:14px;font-size:11px;text-transform:uppercase;letter-spacing:2px;opacity:.85}""",
 'html': """<div class="dv2"><div class="dv2-ornament">✦ ❋ ✦</div><div class="dv2-brand">{{ brand }}</div><div class="dv2-title">Gift Voucher</div><div class="dv2-amt">{{ amount }}</div><div class="dv2-msg">{{ message }}</div><div class="dv2-code"><span>CODE: {{ code }}</span></div><div class="dv2-exp">Valid until {{ expiry }}</div></div>"""},

{'title': '🎨 Pastel Birthday Soft', 'desc': 'Soft pastel pink with rounded shapes and balloons.',
 'css': """.dv3{font-family:'Inter',sans-serif;background:linear-gradient(160deg,#fce7f3 0%,#ddd6fe 100%);padding:48px;border-radius:30px;text-align:center;color:#831843;position:relative;overflow:hidden}
.dv3::before{content:'🎈';position:absolute;top:18px;left:24px;font-size:42px}
.dv3::after{content:'🎁';position:absolute;top:18px;right:24px;font-size:42px}
.dv3-brand{font-size:13px;letter-spacing:3px;color:#9d174d;font-weight:700;text-transform:uppercase;margin-top:20px}
.dv3-title{font-size:46px;font-weight:900;color:#831843;margin:14px 0;letter-spacing:-1px}
.dv3-amt{display:inline-block;background:#fff;color:#ec4899;padding:24px 60px;border-radius:30px;font-size:64px;font-weight:900;margin:18px 0;box-shadow:0 14px 40px rgba(236,72,153,.2);border:3px dashed #fbcfe8}
.dv3-msg{max-width:360px;margin:14px auto;color:#9d174d;font-size:15px;line-height:1.6;font-style:italic}
.dv3-code{display:inline-block;margin-top:14px;padding:12px 26px;background:#fff;border-radius:30px;color:#ec4899;font-family:monospace;font-weight:800;letter-spacing:2px;font-size:16px;box-shadow:0 6px 18px rgba(0,0,0,.06)}
.dv3-exp{margin-top:16px;font-size:11px;color:#9d174d;text-transform:uppercase;letter-spacing:2px}""",
 'html': """<div class="dv3"><div class="dv3-brand">{{ brand }}</div><div class="dv3-title">Happy Gifting!</div><div class="dv3-amt">{{ amount }}</div><div class="dv3-msg">{{ message }}</div><div class="dv3-code">{{ code }}</div><div class="dv3-exp">Expires {{ expiry }}</div></div>"""},

{'title': '🎨 Tech Cyan Modern', 'desc': 'Modern tech cyan gradient with QR code style block.',
 'css': """.dv4{font-family:'Inter',sans-serif;background:#0f172a;padding:0;border-radius:20px;overflow:hidden;display:grid;grid-template-columns:1.6fr 1fr;color:#fff;box-shadow:0 24px 60px rgba(6,182,212,.25)}
.dv4-l{background:linear-gradient(135deg,#0891b2 0%,#3b82f6 100%);padding:40px;position:relative}
.dv4-l::after{content:'';position:absolute;top:-40px;right:-40px;width:160px;height:160px;background:rgba(255,255,255,.08);border-radius:50%}
.dv4-l h4{margin:0;font-size:11px;letter-spacing:3px;text-transform:uppercase;opacity:.85}
.dv4-l h1{margin:14px 0 4px;font-size:42px;font-weight:900;letter-spacing:-1px}
.dv4-l p{margin:0;font-size:15px;opacity:.9;line-height:1.6}
.dv4-l .amt{margin-top:24px;font-size:72px;font-weight:900;line-height:1}
.dv4-r{background:#0f172a;padding:40px 30px;display:flex;flex-direction:column;justify-content:space-between;border-left:2px dashed rgba(255,255,255,.15)}
.dv4-r .qr{width:120px;height:120px;background:repeating-conic-gradient(#fff 0 25%,#0f172a 0 50%) 50%/24px 24px;border-radius:8px;margin:0 auto;border:6px solid #fff}
.dv4-r .code{margin-top:18px;text-align:center;font-family:monospace;color:#22d3ee;font-size:14px;letter-spacing:2px;font-weight:800}
.dv4-r .exp{text-align:center;font-size:10px;color:#64748b;text-transform:uppercase;letter-spacing:1.5px;margin-top:10px}""",
 'html': """<div class="dv4"><div class="dv4-l"><h4>{{ brand }}</h4><h1>Gift Card</h1><p>{{ message }}</p><div class="amt">{{ amount }}</div></div><div class="dv4-r"><div class="qr"></div><div class="code">{{ code }}</div><div class="exp">Valid until {{ expiry }}</div></div></div>"""},

{'title': '🎨 Vintage Coupon Cream', 'desc': 'Old-school coupon with dashed borders and stamp.',
 'css': """.dv5{font-family:'Georgia',serif;background:#fef9c3;padding:0;border-radius:6px;border:3px dashed #78350f;display:grid;grid-template-columns:1fr 140px;color:#78350f;position:relative}
.dv5-main{padding:34px 36px;border-right:3px dashed #78350f}
.dv5-brand{font-size:11px;letter-spacing:3px;text-transform:uppercase;font-weight:700}
.dv5-title{font-size:32px;font-weight:900;font-style:italic;margin:8px 0;color:#451a03}
.dv5-msg{font-size:13px;line-height:1.6;color:#78350f;margin:10px 0;max-width:280px}
.dv5-code{display:inline-block;margin-top:8px;padding:8px 16px;background:#78350f;color:#fef9c3;font-family:monospace;letter-spacing:2px;border-radius:4px;font-size:13px}
.dv5-side{display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px}
.dv5-side .amt{font-size:42px;font-weight:900;line-height:1;color:#451a03}
.dv5-side .lbl{font-size:9px;letter-spacing:2px;text-transform:uppercase;margin-top:4px}
.dv5-side .stamp{margin-top:14px;border:2px solid #b91c1c;color:#b91c1c;padding:6px 12px;border-radius:4px;font-size:9px;letter-spacing:1.5px;text-transform:uppercase;transform:rotate(-8deg);font-weight:800}""",
 'html': """<div class="dv5"><div class="dv5-main"><div class="dv5-brand">{{ brand }}</div><div class="dv5-title">Discount Coupon</div><div class="dv5-msg">{{ message }}</div><div class="dv5-code">USE: {{ code }}</div></div><div class="dv5-side"><div class="amt">{{ amount }}</div><div class="lbl">OFF</div><div class="stamp">Exp {{ expiry }}</div></div></div>"""},
]

# ============================================================
# CARDS / VISITING CARDS (5)
# ============================================================
CARDS = [
{'title': '🎨 Minimalist White Premium', 'desc': 'Ultra-clean white with subtle thin line accents.',
 'css': """.dc1{font-family:'Inter',sans-serif;background:#fff;padding:40px;border-radius:8px;box-shadow:0 18px 50px rgba(0,0,0,.08);border-top:4px solid #000;color:#0a0a0a}
.dc1-name{font-size:32px;font-weight:200;letter-spacing:-1px;margin:0;line-height:1}
.dc1-name strong{font-weight:800}
.dc1-title{font-size:11px;text-transform:uppercase;letter-spacing:3px;color:#737373;margin-top:8px}
.dc1-line{width:50px;height:1px;background:#000;margin:16px 0}
.dc1-info{font-size:12px;color:#404040;line-height:1.9}
.dc1-info div::before{content:'';display:inline-block;width:10px;height:1px;background:#737373;margin-right:8px;vertical-align:middle}
.dc1-co{margin-top:14px;font-size:10px;text-transform:uppercase;letter-spacing:2.5px;color:#737373}""",
 'html': """<div class="dc1"><h2 class="dc1-name">{{ name }}</h2><div class="dc1-title">{{ title }}</div><div class="dc1-line"></div><div class="dc1-info"><div>{{ phone }}</div><div>{{ email }}</div><div>{{ website }}</div><div>{{ address }}</div></div><div class="dc1-co">{{ company }}</div></div>"""},

{'title': '🎨 Bold Gradient Tech', 'desc': 'Vibrant gradient with bold sans and modern tech feel.',
 'css': """.dc2{font-family:'Inter',sans-serif;background:linear-gradient(135deg,#6366f1 0%,#a855f7 50%,#ec4899 100%);padding:40px;border-radius:18px;color:#fff;position:relative;overflow:hidden;box-shadow:0 24px 60px rgba(99,102,241,.35)}
.dc2::before{content:'';position:absolute;top:-60px;right:-60px;width:200px;height:200px;background:rgba(255,255,255,.1);border-radius:50%}
.dc2::after{content:'';position:absolute;bottom:-80px;left:-80px;width:240px;height:240px;background:rgba(255,255,255,.06);border-radius:50%}
.dc2-name{position:relative;font-size:34px;font-weight:900;margin:0;letter-spacing:-1px;line-height:1.05}
.dc2-title{position:relative;font-size:13px;font-weight:600;margin-top:6px;opacity:.92}
.dc2-co{position:relative;font-size:11px;text-transform:uppercase;letter-spacing:2px;margin-top:14px;background:rgba(255,255,255,.18);display:inline-block;padding:5px 12px;border-radius:20px;backdrop-filter:blur(8px)}
.dc2-info{position:relative;margin-top:24px;font-size:12px;line-height:1.8}
.dc2-info div{display:flex;align-items:center;gap:8px}
.dc2-info span{display:inline-block;width:6px;height:6px;background:#fff;border-radius:50%}""",
 'html': """<div class="dc2"><h2 class="dc2-name">{{ name }}</h2><div class="dc2-title">{{ title }}</div><div class="dc2-co">{{ company }}</div><div class="dc2-info"><div><span></span>{{ phone }}</div><div><span></span>{{ email }}</div><div><span></span>{{ website }}</div><div><span></span>{{ address }}</div></div></div>"""},

{'title': '🎨 Dark Luxury Gold', 'desc': 'Black background with elegant gold typography.',
 'css': """.dc3{font-family:'Playfair Display',serif;background:#0a0a0a;padding:42px;border-radius:10px;color:#d4af37;border:1px solid #d4af37;position:relative}
.dc3::before{content:'';position:absolute;top:14px;left:14px;right:14px;bottom:14px;border:1px solid rgba(212,175,55,.3);pointer-events:none;border-radius:6px}
.dc3-mono{position:absolute;top:30px;right:30px;width:46px;height:46px;border:1px solid #d4af37;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:900;color:#d4af37}
.dc3-name{font-size:32px;font-weight:900;margin:0;color:#fde68a;letter-spacing:-.5px;font-style:italic}
.dc3-title{font-family:'Inter',sans-serif;font-size:10px;text-transform:uppercase;letter-spacing:3px;color:#d4af37;margin-top:4px}
.dc3-divider{width:60px;height:2px;background:#d4af37;margin:14px 0 16px}
.dc3-info{font-family:'Inter',sans-serif;font-size:11px;line-height:1.9;color:#fef3c7}
.dc3-info div::before{content:'•';color:#d4af37;margin-right:8px;font-weight:900}
.dc3-co{position:absolute;bottom:30px;right:30px;font-family:'Inter',sans-serif;font-size:9px;text-transform:uppercase;letter-spacing:2.5px;color:#d4af37}""",
 'html': """<div class="dc3"><div class="dc3-mono">{{ name|first }}</div><h2 class="dc3-name">{{ name }}</h2><div class="dc3-title">{{ title }}</div><div class="dc3-divider"></div><div class="dc3-info"><div>{{ phone }}</div><div>{{ email }}</div><div>{{ website }}</div><div>{{ address }}</div></div><div class="dc3-co">{{ company }}</div></div>"""},

{'title': '🎨 Watercolor Creative', 'desc': 'Soft pastel watercolor with handwritten artistic feel.',
 'css': """.dc4{font-family:'Inter',sans-serif;background:linear-gradient(135deg,#fef3c7 0%,#fed7aa 40%,#fecaca 100%);padding:40px;border-radius:20px;color:#7c2d12;position:relative;overflow:hidden;box-shadow:0 18px 50px rgba(251,146,60,.2)}
.dc4::before{content:'';position:absolute;top:-40px;right:-40px;width:160px;height:160px;background:radial-gradient(circle,#fbbf24,transparent 70%);opacity:.5;border-radius:50%}
.dc4::after{content:'';position:absolute;bottom:-50px;left:-50px;width:180px;height:180px;background:radial-gradient(circle,#fb7185,transparent 70%);opacity:.4;border-radius:50%}
.dc4-name{position:relative;font-family:'Caveat','cursive';font-size:42px;font-weight:700;color:#7c2d12;margin:0;line-height:.95}
.dc4-title{position:relative;font-size:13px;font-weight:600;color:#9a3412;margin-top:6px;font-style:italic}
.dc4-co{position:relative;font-size:11px;text-transform:uppercase;letter-spacing:2px;color:#9a3412;margin-top:8px;font-weight:700}
.dc4-info{position:relative;margin-top:20px;font-size:12px;line-height:1.8;color:#7c2d12}
.dc4-info div::before{content:'~';color:#ea580c;font-weight:900;margin-right:8px}""",
 'html': """<div class="dc4"><h2 class="dc4-name">{{ name }}</h2><div class="dc4-title">{{ title }}</div><div class="dc4-co">{{ company }}</div><div class="dc4-info"><div>{{ phone }}</div><div>{{ email }}</div><div>{{ website }}</div><div>{{ address }}</div></div></div>"""},

{'title': '🎨 Geometric Color Block', 'desc': 'Bold color blocks with geometric shapes and modern grid.',
 'css': """.dc5{font-family:'Inter',sans-serif;background:#fff;padding:0;border-radius:14px;overflow:hidden;display:grid;grid-template-columns:120px 1fr;box-shadow:0 18px 50px rgba(0,0,0,.1);min-height:200px}
.dc5-l{background:#10b981;display:flex;flex-direction:column;justify-content:space-between;padding:24px 20px;color:#fff;position:relative}
.dc5-l::after{content:'';position:absolute;bottom:0;left:0;right:0;height:40%;background:#0f172a;clip-path:polygon(0 30%,100% 0,100% 100%,0 100%)}
.dc5-l .mono{position:relative;z-index:2;font-size:48px;font-weight:900;line-height:1}
.dc5-l .co{position:relative;z-index:2;font-size:9px;text-transform:uppercase;letter-spacing:1.5px;writing-mode:vertical-rl;transform:rotate(180deg);align-self:flex-end;font-weight:800}
.dc5-r{padding:30px 32px;color:#0f172a}
.dc5-r .name{font-size:28px;font-weight:900;margin:0;letter-spacing:-.5px}
.dc5-r .title{font-size:11px;text-transform:uppercase;letter-spacing:2px;color:#10b981;font-weight:700;margin-top:4px}
.dc5-r .bar{width:40px;height:3px;background:#10b981;margin:14px 0 12px}
.dc5-r .info{font-size:11px;line-height:1.85;color:#475569}
.dc5-r .info strong{color:#0f172a;display:inline-block;width:54px;text-transform:uppercase;font-size:9px;letter-spacing:1.5px;color:#10b981}""",
 'html': """<div class="dc5"><div class="dc5-l"><div class="mono">{{ name|first }}</div><div class="co">{{ company }}</div></div><div class="dc5-r"><h2 class="name">{{ name }}</h2><div class="title">{{ title }}</div><div class="bar"></div><div class="info"><div><strong>tel</strong>{{ phone }}</div><div><strong>mail</strong>{{ email }}</div><div><strong>web</strong>{{ website }}</div><div><strong>loc</strong>{{ address }}</div></div></div></div>"""},
]

# ============================================================
# CERTIFICATES (5)
# ============================================================
CERTIFICATES = [
{'title': '🎨 Classic Gold Border Elegance', 'desc': 'Traditional ornate gold border with serif script.',
 'css': """.dcr1{font-family:'Playfair Display',serif;background:#fffbeb;padding:60px 50px;border:14px double #d4af37;text-align:center;color:#78350f;position:relative}
.dcr1::before{content:'';position:absolute;top:30px;left:30px;right:30px;bottom:30px;border:1px solid #d4af37;pointer-events:none}
.dcr1 .org{font-size:13px;letter-spacing:5px;text-transform:uppercase;color:#92400e;font-weight:700}
.dcr1 .ttl{font-size:54px;font-weight:900;color:#451a03;margin:14px 0 8px;font-style:italic;letter-spacing:-1px}
.dcr1 .sub{font-size:14px;color:#78350f;letter-spacing:3px;text-transform:uppercase}
.dcr1 .ribbon{display:inline-block;margin:18px 0;padding:6px 30px;background:#d4af37;color:#fff;font-size:11px;letter-spacing:2px;text-transform:uppercase;font-weight:800;clip-path:polygon(8% 0,92% 0,100% 50%,92% 100%,8% 100%,0 50%)}
.dcr1 .name{font-size:48px;font-weight:900;color:#7c2d12;margin:14px 0 4px;font-style:italic;font-family:'Great Vibes','Playfair Display',serif}
.dcr1 .desc{max-width:480px;margin:14px auto;color:#78350f;font-size:14px;line-height:1.7;font-family:'Inter',sans-serif}
.dcr1 .desc strong{color:#451a03;font-style:italic}
.dcr1 .footer{display:flex;justify-content:space-between;margin-top:30px;padding:0 30px;font-family:'Inter',sans-serif}
.dcr1 .footer div{text-align:center;flex:1}
.dcr1 .footer .line{width:140px;height:1px;background:#92400e;margin:0 auto 6px}
.dcr1 .footer strong{font-size:13px;color:#451a03}
.dcr1 .footer span{display:block;font-size:10px;text-transform:uppercase;letter-spacing:1.5px;color:#92400e}""",
 'html': """<div class="dcr1"><div class="org">{{ organization }}</div><div class="ttl">Certificate</div><div class="sub">of Achievement</div><div class="ribbon">★ Awarded To ★</div><div class="name">{{ recipient }}</div><div class="desc">For successful completion of <strong>{{ course }}</strong>. {{ description }}</div><div class="footer"><div><div class="line"></div><strong>{{ signer }}</strong><span>{{ title }}</span></div><div><div class="line"></div><strong>{{ date }}</strong><span>Date</span></div></div></div>"""},

{'title': '🎨 Modern Gradient Achievement', 'desc': 'Bold blue gradient with modern sans and clean lines.',
 'css': """.dcr2{font-family:'Inter',sans-serif;background:#fff;padding:0;border-radius:18px;overflow:hidden;box-shadow:0 24px 60px rgba(59,130,246,.18)}
.dcr2-h{background:linear-gradient(135deg,#1e40af 0%,#3b82f6 50%,#06b6d4 100%);padding:50px 40px 70px;text-align:center;color:#fff;position:relative;clip-path:polygon(0 0,100% 0,100% 88%,50% 100%,0 88%)}
.dcr2-h .org{font-size:11px;letter-spacing:4px;text-transform:uppercase;opacity:.85;font-weight:700}
.dcr2-h h1{margin:14px 0 6px;font-size:46px;font-weight:900;letter-spacing:-1px}
.dcr2-h .sub{font-size:12px;text-transform:uppercase;letter-spacing:3px;opacity:.85}
.dcr2-b{padding:40px 50px 36px;text-align:center}
.dcr2-b .ack{font-size:12px;text-transform:uppercase;letter-spacing:2.5px;color:#3b82f6;font-weight:700}
.dcr2-b .name{font-size:48px;font-weight:900;color:#0f172a;margin:8px 0;letter-spacing:-1.5px}
.dcr2-b .underline{width:80px;height:3px;background:#3b82f6;margin:10px auto}
.dcr2-b .desc{max-width:460px;margin:14px auto;color:#475569;font-size:13px;line-height:1.7}
.dcr2-b .desc strong{color:#1e40af}
.dcr2-f{display:flex;justify-content:space-between;margin-top:30px;padding:0 60px}
.dcr2-f div{text-align:center;flex:1}
.dcr2-f .line{width:160px;height:2px;background:#1e40af;margin:0 auto 8px}
.dcr2-f strong{display:block;color:#0f172a;font-size:14px}
.dcr2-f span{font-size:10px;text-transform:uppercase;letter-spacing:1.5px;color:#64748b}
.dcr2-seal{position:absolute;top:50%;right:40px;transform:translateY(-50%);width:80px;height:80px;border:3px solid #fff;border-radius:50%;background:rgba(255,255,255,.15);display:flex;align-items:center;justify-content:center;font-size:34px;backdrop-filter:blur(8px)}""",
 'html': """<div class="dcr2"><div class="dcr2-h"><div class="org">{{ organization }}</div><h1>Certificate of Excellence</h1><div class="sub">Issued by {{ organization }}</div><div class="dcr2-seal">★</div></div><div class="dcr2-b"><div class="ack">This Certificate is Proudly Presented To</div><div class="name">{{ recipient }}</div><div class="underline"></div><div class="desc">For outstanding achievement in <strong>{{ course }}</strong>. {{ description }}</div><div class="dcr2-f"><div><div class="line"></div><strong>{{ signer }}</strong><span>{{ title }}</span></div><div><div class="line"></div><strong>{{ date }}</strong><span>Date Issued</span></div></div></div></div>"""},

{'title': '🎨 Minimal Modern Award', 'desc': 'Ultra-clean monochrome with thin geometric accents.',
 'css': """.dcr3{font-family:'Inter',sans-serif;background:#fafafa;padding:60px 50px;border:1px solid #e5e5e5;text-align:center;color:#0a0a0a;position:relative}
.dcr3::before{content:'';position:absolute;top:30px;left:50%;transform:translateX(-50%);width:60px;height:60px;border:2px solid #0a0a0a;border-radius:50%}
.dcr3::after{content:'★';position:absolute;top:42px;left:50%;transform:translateX(-50%);font-size:28px;color:#0a0a0a}
.dcr3 .org{margin-top:120px;font-size:11px;letter-spacing:5px;text-transform:uppercase;color:#737373;font-weight:600}
.dcr3 .ttl{font-size:42px;font-weight:200;color:#0a0a0a;margin:14px 0 4px;letter-spacing:-1px}
.dcr3 .ttl strong{font-weight:900}
.dcr3 .sub{font-size:11px;text-transform:uppercase;letter-spacing:3px;color:#737373}
.dcr3 .divider{width:60px;height:1px;background:#0a0a0a;margin:24px auto}
.dcr3 .ack{font-size:11px;text-transform:uppercase;letter-spacing:2px;color:#737373}
.dcr3 .name{font-size:38px;font-weight:900;margin:10px 0;letter-spacing:-1px}
.dcr3 .desc{max-width:440px;margin:14px auto;color:#404040;font-size:13px;line-height:1.8}
.dcr3 .desc strong{color:#0a0a0a}
.dcr3 .footer{display:flex;justify-content:space-between;margin-top:36px;padding:0 30px}
.dcr3 .footer div{text-align:center;flex:1}
.dcr3 .footer .line{width:130px;height:1px;background:#0a0a0a;margin:0 auto 6px}
.dcr3 .footer strong{font-size:13px}
.dcr3 .footer span{display:block;font-size:9px;text-transform:uppercase;letter-spacing:2px;color:#737373}""",
 'html': """<div class="dcr3"><div class="org">{{ organization }}</div><div class="ttl">Certi<strong>ficate</strong></div><div class="sub">of Achievement</div><div class="divider"></div><div class="ack">Awarded to</div><div class="name">{{ recipient }}</div><div class="desc">In recognition of completing <strong>{{ course }}</strong>. {{ description }}</div><div class="footer"><div><div class="line"></div><strong>{{ signer }}</strong><span>{{ title }}</span></div><div><div class="line"></div><strong>{{ date }}</strong><span>Date</span></div></div></div>"""},

{'title': '🎨 Vintage Royal Burgundy', 'desc': 'Royal burgundy with vintage ornaments and crown motif.',
 'css': """.dcr4{font-family:'Playfair Display',serif;background:linear-gradient(180deg,#fef3e2 0%,#fde68a 100%);padding:50px;border:6px solid #7f1d1d;text-align:center;color:#7f1d1d;position:relative}
.dcr4::before{content:'';position:absolute;top:14px;left:14px;right:14px;bottom:14px;border:2px dashed #7f1d1d;pointer-events:none}
.dcr4 .crown{font-size:46px;color:#7f1d1d;line-height:1}
.dcr4 .org{font-size:12px;letter-spacing:4px;text-transform:uppercase;font-weight:700;margin-top:6px}
.dcr4 .ttl{font-size:50px;font-weight:900;font-style:italic;color:#450a0a;margin:8px 0 4px;letter-spacing:-1px}
.dcr4 .sub{font-size:13px;text-transform:uppercase;letter-spacing:3px}
.dcr4 .scroll{display:inline-block;margin:18px auto;padding:8px 36px;background:#7f1d1d;color:#fef3e2;font-size:11px;letter-spacing:2px;text-transform:uppercase;font-weight:800;clip-path:polygon(8% 0,92% 0,100% 50%,92% 100%,8% 100%,0 50%)}
.dcr4 .name{font-family:'Great Vibes','Playfair Display',cursive;font-size:54px;color:#450a0a;margin:6px 0;font-weight:700}
.dcr4 .desc{font-family:'Inter',sans-serif;max-width:460px;margin:12px auto;font-size:13px;line-height:1.7;color:#7f1d1d}
.dcr4 .desc em{font-style:italic;color:#450a0a;font-weight:700}
.dcr4 .footer{display:flex;justify-content:space-between;margin-top:24px;padding:0 30px;font-family:'Inter',sans-serif}
.dcr4 .footer div{flex:1;text-align:center}
.dcr4 .footer .line{width:140px;height:1px;background:#7f1d1d;margin:0 auto 6px}
.dcr4 .footer strong{font-size:13px;color:#450a0a;font-style:italic}
.dcr4 .footer span{display:block;font-size:9px;text-transform:uppercase;letter-spacing:1.5px}""",
 'html': """<div class="dcr4"><div class="crown">♛</div><div class="org">{{ organization }}</div><div class="ttl">Certificate</div><div class="sub">of Distinction</div><div class="scroll">Awarded To</div><div class="name">{{ recipient }}</div><div class="desc">In honor of mastery in <em>{{ course }}</em>. {{ description }}</div><div class="footer"><div><div class="line"></div><strong>{{ signer }}</strong><span>{{ title }}</span></div><div><div class="line"></div><strong>{{ date }}</strong><span>Issued</span></div></div></div>"""},

{'title': '🎨 Bold Geometric Modern', 'desc': 'Bold color blocks with geometric shapes and chunky serif.',
 'css': """.dcr5{font-family:'Inter',sans-serif;background:#fff;padding:0;border-radius:14px;overflow:hidden;display:grid;grid-template-columns:1fr 200px;color:#0f172a;box-shadow:0 24px 60px rgba(0,0,0,.12)}
.dcr5-main{padding:50px 40px}
.dcr5-main .org{font-size:11px;letter-spacing:3px;text-transform:uppercase;color:#10b981;font-weight:800}
.dcr5-main h1{font-family:'Playfair Display',serif;font-size:48px;font-weight:900;color:#0f172a;margin:8px 0;letter-spacing:-1.5px;line-height:.95}
.dcr5-main .sub{font-size:12px;text-transform:uppercase;letter-spacing:2px;color:#64748b}
.dcr5-main .divider{width:60px;height:4px;background:#10b981;margin:20px 0}
.dcr5-main .ack{font-size:11px;text-transform:uppercase;letter-spacing:2px;color:#64748b}
.dcr5-main .name{font-size:38px;font-weight:900;color:#0f172a;margin:6px 0;letter-spacing:-1px}
.dcr5-main .desc{font-size:13px;color:#475569;line-height:1.7;max-width:380px;margin:10px 0}
.dcr5-main .desc strong{color:#10b981}
.dcr5-main .footer{display:flex;gap:40px;margin-top:24px}
.dcr5-main .footer div .line{width:120px;height:2px;background:#0f172a;margin-bottom:6px}
.dcr5-main .footer strong{display:block;font-size:13px}
.dcr5-main .footer span{font-size:9px;text-transform:uppercase;letter-spacing:1.5px;color:#64748b}
.dcr5-side{background:linear-gradient(180deg,#10b981 0%,#059669 100%);display:flex;flex-direction:column;justify-content:center;align-items:center;color:#fff;padding:30px 20px;text-align:center;position:relative}
.dcr5-side::before{content:'';position:absolute;top:0;left:0;right:0;height:80px;background:#0f172a;clip-path:polygon(0 0,100% 0,100% 60%,0 100%)}
.dcr5-side .star{position:relative;z-index:2;font-size:80px;line-height:1;color:#fde68a;margin-top:30px}
.dcr5-side .lbl{font-size:11px;text-transform:uppercase;letter-spacing:2px;margin-top:12px;font-weight:700;opacity:.95}
.dcr5-side .yr{font-family:'Playfair Display',serif;font-size:42px;font-weight:900;margin-top:8px;line-height:1}""",
 'html': """<div class="dcr5"><div class="dcr5-main"><div class="org">{{ organization }}</div><h1>CERTIFICATE</h1><div class="sub">of Achievement</div><div class="divider"></div><div class="ack">Presented To</div><div class="name">{{ recipient }}</div><div class="desc">For outstanding performance in <strong>{{ course }}</strong>. {{ description }}</div><div class="footer"><div><div class="line"></div><strong>{{ signer }}</strong><span>{{ title }}</span></div><div><div class="line"></div><strong>{{ date }}</strong><span>Date</span></div></div></div><div class="dcr5-side"><div class="star">★</div><div class="lbl">Excellence</div><div class="yr">2026</div></div></div>"""},
]

# ============================================================
# SOCIAL POSTS (5)
# ============================================================
SOCIALS = [
{'title': '🎨 Bold Type Quote Post', 'desc': 'Massive bold type quote on solid color background.',
 'css': """.ds1{font-family:'Inter',sans-serif;background:#fbbf24;padding:60px 50px;color:#0f172a;text-align:center;border-radius:14px;aspect-ratio:1;display:flex;flex-direction:column;justify-content:center;position:relative;overflow:hidden}
.ds1::before{content:'"';position:absolute;top:-20px;left:30px;font-family:'Playfair Display',serif;font-size:200px;color:rgba(15,23,42,.08);line-height:1}
.ds1 h1{font-size:64px;font-weight:900;letter-spacing:-2px;line-height:1;margin:0;position:relative}
.ds1 p{font-size:18px;font-weight:600;margin:24px 0 0;line-height:1.4;position:relative}
.ds1 .cta{margin-top:30px;display:inline-block;padding:14px 30px;background:#0f172a;color:#fbbf24;font-weight:800;border-radius:50px;align-self:center;font-size:14px;letter-spacing:1px;text-transform:uppercase}
.ds1 .handle{margin-top:24px;font-size:13px;font-weight:700;letter-spacing:1px;position:relative}""",
 'html': """<div class="ds1"><h1>{{ headline }}</h1><p>{{ body }}</p><div class="cta">{{ cta }}</div><div class="handle">{{ handle }}</div></div>"""},

{'title': '🎨 Gradient Sunset Vibe', 'desc': 'Vibrant pink-orange gradient with modern type stack.',
 'css': """.ds2{font-family:'Inter',sans-serif;background:linear-gradient(135deg,#f97316 0%,#ec4899 50%,#a855f7 100%);padding:60px 40px;color:#fff;text-align:center;border-radius:18px;aspect-ratio:1;display:flex;flex-direction:column;justify-content:center;position:relative;overflow:hidden}
.ds2::before{content:'';position:absolute;top:-50%;right:-30%;width:140%;height:140%;background:radial-gradient(circle,rgba(255,255,255,.18),transparent 40%)}
.ds2 .tag{position:relative;display:inline-block;background:rgba(255,255,255,.18);padding:6px 18px;border-radius:30px;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;align-self:center;backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.25)}
.ds2 h1{position:relative;font-size:56px;font-weight:900;letter-spacing:-2px;margin:18px 0 12px;line-height:1;text-shadow:0 4px 24px rgba(0,0,0,.2)}
.ds2 p{position:relative;font-size:17px;line-height:1.5;margin:0 auto;max-width:400px;opacity:.95}
.ds2 .cta{position:relative;margin-top:26px;align-self:center;background:#fff;color:#a855f7;padding:14px 30px;border-radius:50px;font-weight:800;font-size:14px;letter-spacing:1px;text-transform:uppercase;box-shadow:0 12px 28px rgba(0,0,0,.18)}
.ds2 .handle{position:relative;margin-top:20px;font-size:12px;opacity:.9;letter-spacing:1px}""",
 'html': """<div class="ds2"><div class="tag">✨ New</div><h1>{{ headline }}</h1><p>{{ body }}</p><div class="cta">{{ cta }}</div><div class="handle">{{ handle }}</div></div>"""},

{'title': '🎨 Minimal Sale Announcement', 'desc': 'Clean white with bold black sale type and minimal layout.',
 'css': """.ds3{font-family:'Inter',sans-serif;background:#fff;padding:50px 40px;color:#0a0a0a;border-radius:14px;aspect-ratio:1;display:flex;flex-direction:column;justify-content:space-between;border:3px solid #0a0a0a;position:relative}
.ds3 .top{font-size:11px;letter-spacing:4px;text-transform:uppercase;font-weight:700;color:#0a0a0a;border-bottom:1px solid #0a0a0a;padding-bottom:14px}
.ds3 .top span{float:right}
.ds3 .mid{padding:20px 0}
.ds3 h1{font-size:96px;font-weight:900;letter-spacing:-5px;line-height:.85;margin:0;color:#0a0a0a}
.ds3 h1 span{display:block;color:#dc2626}
.ds3 p{font-size:14px;line-height:1.5;color:#404040;margin:14px 0 0;max-width:280px}
.ds3 .bot{display:flex;justify-content:space-between;align-items:center;border-top:1px solid #0a0a0a;padding-top:14px}
.ds3 .cta{background:#0a0a0a;color:#fff;padding:14px 26px;font-weight:800;font-size:13px;letter-spacing:2px;text-transform:uppercase}
.ds3 .handle{font-size:11px;letter-spacing:2px;text-transform:uppercase;font-weight:700}""",
 'html': """<div class="ds3"><div class="top">Limited Time Only<span>2026</span></div><div class="mid"><h1>{{ headline }}<span>50% OFF</span></h1><p>{{ body }}</p></div><div class="bot"><div class="cta">{{ cta }}</div><div class="handle">{{ handle }}</div></div></div>"""},

{'title': '🎨 Neon Aesthetic Glow', 'desc': 'Dark with neon pink/cyan glow and retro aesthetic.',
 'css': """.ds4{font-family:'Inter',sans-serif;background:#0a0014;padding:50px 40px;color:#fff;text-align:center;border-radius:14px;aspect-ratio:1;display:flex;flex-direction:column;justify-content:center;position:relative;overflow:hidden;border:2px solid rgba(236,72,153,.4);box-shadow:0 0 60px rgba(236,72,153,.3),inset 0 0 60px rgba(34,211,238,.1)}
.ds4::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(180deg,transparent 0,transparent 3px,rgba(236,72,153,.04) 3px,rgba(236,72,153,.04) 4px);pointer-events:none}
.ds4 .tag{position:relative;color:#22d3ee;font-size:12px;letter-spacing:6px;text-transform:uppercase;font-weight:800;text-shadow:0 0 14px #22d3ee}
.ds4 h1{position:relative;font-size:62px;font-weight:900;color:#ec4899;margin:18px 0 14px;letter-spacing:-2px;line-height:.95;text-shadow:0 0 24px #ec4899,0 0 50px rgba(236,72,153,.5)}
.ds4 p{position:relative;color:#e2e8f0;font-size:15px;line-height:1.5;max-width:380px;margin:0 auto;opacity:.9}
.ds4 .cta{position:relative;margin-top:26px;align-self:center;background:transparent;color:#22d3ee;padding:14px 28px;border:2px solid #22d3ee;border-radius:6px;font-weight:800;font-size:13px;letter-spacing:2px;text-transform:uppercase;text-shadow:0 0 14px #22d3ee;box-shadow:0 0 20px rgba(34,211,238,.4)}
.ds4 .handle{position:relative;margin-top:18px;color:#f472b6;font-size:12px;letter-spacing:2px;font-weight:700}""",
 'html': """<div class="ds4"><div class="tag">// 2026</div><h1>{{ headline }}</h1><p>{{ body }}</p><div class="cta">▸ {{ cta }}</div><div class="handle">{{ handle }}</div></div>"""},

{'title': '🎨 Pastel Lifestyle Soft', 'desc': 'Soft pastel with serif title and lifestyle elegance.',
 'css': """.ds5{font-family:'Inter',sans-serif;background:linear-gradient(160deg,#fef3c7 0%,#fce7f3 60%,#ddd6fe 100%);padding:50px 40px;color:#831843;text-align:center;border-radius:18px;aspect-ratio:1;display:flex;flex-direction:column;justify-content:center;position:relative;overflow:hidden;box-shadow:0 18px 50px rgba(236,72,153,.15)}
.ds5::before{content:'❀';position:absolute;top:24px;left:30px;font-size:36px;color:#f9a8d4;opacity:.7}
.ds5::after{content:'❀';position:absolute;bottom:24px;right:30px;font-size:36px;color:#c4b5fd;opacity:.7}
.ds5 .tag{font-family:'Caveat',cursive;font-size:24px;color:#9d174d;font-weight:700}
.ds5 h1{font-family:'Playfair Display',serif;font-size:56px;font-weight:900;color:#831843;margin:8px 0 14px;letter-spacing:-1.5px;line-height:1;font-style:italic}
.ds5 p{font-size:15px;color:#9d174d;line-height:1.6;max-width:380px;margin:0 auto;font-style:italic}
.ds5 .cta{margin-top:26px;align-self:center;background:#831843;color:#fef3c7;padding:14px 30px;border-radius:50px;font-weight:700;font-size:13px;letter-spacing:1.5px;text-transform:uppercase}
.ds5 .handle{margin-top:18px;color:#9d174d;font-size:12px;letter-spacing:1.5px}""",
 'html': """<div class="ds5"><div class="tag">~ lovely ~</div><h1>{{ headline }}</h1><p>{{ body }}</p><div class="cta">{{ cta }}</div><div class="handle">{{ handle }}</div></div>"""},
]

# ============================================================
# FLYERS (5)
# ============================================================
FLYERS = [
{'title': '🎨 Bold Event Gradient', 'desc': 'Massive bold type with vibrant gradient header.',
 'css': """.df1{font-family:'Inter',sans-serif;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 24px 60px rgba(168,85,247,.18)}
.df1-h{background:linear-gradient(135deg,#a855f7 0%,#ec4899 50%,#f59e0b 100%);padding:50px 40px;color:#fff;position:relative;overflow:hidden}
.df1-h::before{content:'';position:absolute;top:-50px;right:-50px;width:200px;height:200px;background:rgba(255,255,255,.12);border-radius:50%}
.df1-h .tag{position:relative;display:inline-block;background:rgba(255,255,255,.2);padding:6px 16px;border-radius:30px;font-size:11px;letter-spacing:2px;text-transform:uppercase;font-weight:800;backdrop-filter:blur(8px)}
.df1-h h1{position:relative;font-size:64px;font-weight:900;letter-spacing:-2px;line-height:.95;margin:14px 0 6px}
.df1-h .sub{position:relative;font-size:18px;font-weight:600;opacity:.95}
.df1-b{padding:36px 40px}
.df1-b p{font-size:15px;line-height:1.7;color:#475569;margin:0 0 24px}
.df1-info{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:24px}
.df1-info div{padding:18px;background:#faf5ff;border-left:4px solid #a855f7;border-radius:8px}
.df1-info h4{margin:0 0 4px;font-size:10px;text-transform:uppercase;letter-spacing:1.5px;color:#a855f7;font-weight:800}
.df1-info p{margin:0;color:#0f172a;font-weight:700;font-size:15px}
.df1-cta{background:linear-gradient(135deg,#a855f7,#ec4899);color:#fff;padding:18px;text-align:center;border-radius:50px;font-weight:800;font-size:15px;letter-spacing:1.5px;text-transform:uppercase;box-shadow:0 14px 30px rgba(168,85,247,.3)}""",
 'html': """<div class="df1"><div class="df1-h"><div class="tag">✨ Event</div><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div></div><div class="df1-b"><p>{{ body }}</p><div class="df1-info"><div><h4>When</h4><p>{{ date }}</p></div><div><h4>Where</h4><p>{{ venue }}</p></div></div><div class="df1-cta">RSVP · {{ contact }}</div></div></div>"""},

{'title': '🎨 Sale Mega Discount Red', 'desc': 'Bold red sale flyer with massive discount type.',
 'css': """.df2{font-family:'Inter',sans-serif;background:#dc2626;color:#fff;padding:0;border-radius:14px;overflow:hidden;position:relative;box-shadow:0 24px 60px rgba(220,38,38,.3)}
.df2::before{content:'';position:absolute;top:0;left:0;right:0;height:6px;background:repeating-linear-gradient(90deg,#fbbf24 0,#fbbf24 30px,#dc2626 30px,#dc2626 60px)}
.df2-top{padding:50px 40px 30px;text-align:center;position:relative}
.df2-top .badge{display:inline-block;background:#fbbf24;color:#7f1d1d;padding:8px 22px;border-radius:30px;font-size:12px;font-weight:900;letter-spacing:2px;text-transform:uppercase;transform:rotate(-3deg)}
.df2-top h1{font-size:96px;font-weight:900;letter-spacing:-5px;line-height:.85;margin:14px 0 4px;text-shadow:0 6px 0 rgba(0,0,0,.15)}
.df2-top h1 span{display:block;color:#fbbf24;font-size:54px;margin-top:8px}
.df2-top .sub{font-size:18px;font-weight:700;opacity:.95}
.df2-mid{background:#fbbf24;color:#7f1d1d;padding:22px 40px;text-align:center;font-size:15px;line-height:1.5;font-weight:600}
.df2-bot{padding:30px 40px;text-align:center;position:relative}
.df2-bot::before{content:'';position:absolute;top:0;left:0;right:0;height:6px;background:repeating-linear-gradient(90deg,#fbbf24 0,#fbbf24 30px,#dc2626 30px,#dc2626 60px)}
.df2-info{display:flex;justify-content:space-around;margin-top:18px;font-size:13px}
.df2-info div h4{margin:0 0 4px;font-size:9px;letter-spacing:2px;opacity:.85;text-transform:uppercase}
.df2-info div p{margin:0;font-weight:800;font-size:15px}""",
 'html': """<div class="df2"><div class="df2-top"><div class="badge">★ MEGA SALE ★</div><h1>{{ title }}<span>{{ subtitle }}</span></h1></div><div class="df2-mid">{{ body }}</div><div class="df2-bot"><div class="df2-info"><div><h4>Date</h4><p>{{ date }}</p></div><div><h4>Venue</h4><p>{{ venue }}</p></div><div><h4>Call</h4><p>{{ contact }}</p></div></div></div></div>"""},

{'title': '🎨 Minimal Business Promo', 'desc': 'Clean monochrome with elegant serif and split layout.',
 'css': """.df3{font-family:'Inter',sans-serif;background:#fff;border:1px solid #e5e5e5;border-radius:8px;padding:0;overflow:hidden;display:grid;grid-template-columns:1fr 1fr}
.df3-l{background:#0a0a0a;color:#fff;padding:50px 36px;display:flex;flex-direction:column;justify-content:center;position:relative}
.df3-l::before{content:'';position:absolute;top:30px;left:36px;width:40px;height:2px;background:#fff}
.df3-l .tag{font-size:11px;letter-spacing:3px;text-transform:uppercase;opacity:.7;margin-top:30px;font-weight:600}
.df3-l h1{font-family:'Playfair Display',serif;font-size:56px;font-weight:900;margin:14px 0 8px;line-height:.95;letter-spacing:-1.5px}
.df3-l .sub{font-size:14px;opacity:.85;font-style:italic}
.df3-r{padding:50px 36px;color:#0a0a0a}
.df3-r p{font-size:14px;line-height:1.7;color:#404040;margin:0 0 20px}
.df3-r .info{margin:24px 0}
.df3-r .info div{padding:14px 0;border-bottom:1px solid #e5e5e5;display:flex;justify-content:space-between;align-items:center}
.df3-r .info h4{margin:0;font-size:10px;text-transform:uppercase;letter-spacing:1.5px;color:#737373;font-weight:600}
.df3-r .info p{margin:0;font-weight:700;font-size:13px;color:#0a0a0a}
.df3-r .cta{background:#0a0a0a;color:#fff;padding:14px;text-align:center;font-size:12px;letter-spacing:2px;text-transform:uppercase;font-weight:700;margin-top:14px}""",
 'html': """<div class="df3"><div class="df3-l"><div class="tag">{{ subtitle }}</div><h1>{{ title }}</h1><div class="sub">An exclusive invitation</div></div><div class="df3-r"><p>{{ body }}</p><div class="info"><div><h4>Date</h4><p>{{ date }}</p></div><div><h4>Venue</h4><p>{{ venue }}</p></div><div><h4>Contact</h4><p>{{ contact }}</p></div></div><div class="cta">RSVP Required</div></div></div>"""},

{'title': '🎨 Music Concert Dark', 'desc': 'Dark concert poster with neon and bold rock vibes.',
 'css': """.df4{font-family:'Inter',sans-serif;background:#000;padding:50px 40px;color:#fff;border-radius:14px;position:relative;overflow:hidden;border:1px solid rgba(236,72,153,.3)}
.df4::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at top,rgba(236,72,153,.25),transparent 60%),radial-gradient(ellipse at bottom right,rgba(34,211,238,.2),transparent 50%)}
.df4-top{position:relative;text-align:center;border-bottom:1px solid rgba(255,255,255,.15);padding-bottom:24px;margin-bottom:24px}
.df4-top .tag{display:inline-block;color:#22d3ee;font-size:12px;letter-spacing:5px;text-transform:uppercase;font-weight:800;text-shadow:0 0 14px #22d3ee}
.df4-top h1{font-size:72px;font-weight:900;color:#fff;margin:14px 0 6px;line-height:.9;letter-spacing:-2px;text-shadow:0 0 30px rgba(236,72,153,.6)}
.df4-top .sub{color:#ec4899;font-size:18px;font-weight:700;letter-spacing:2px;text-transform:uppercase}
.df4-b{position:relative;text-align:center}
.df4-b p{color:#cbd5e1;font-size:14px;line-height:1.6;max-width:420px;margin:0 auto 22px}
.df4-info{display:flex;justify-content:space-around;margin-bottom:22px}
.df4-info div h4{font-size:9px;letter-spacing:2px;color:#22d3ee;text-transform:uppercase;margin:0 0 4px}
.df4-info div p{margin:0;color:#fff;font-weight:800;font-size:14px}
.df4-cta{background:#ec4899;color:#fff;padding:16px 32px;display:inline-block;border-radius:6px;font-weight:900;letter-spacing:2px;text-transform:uppercase;font-size:13px;box-shadow:0 0 30px rgba(236,72,153,.5)}""",
 'html': """<div class="df4"><div class="df4-top"><div class="tag">// LIVE CONCERT</div><h1>{{ title }}</h1><div class="sub">{{ subtitle }}</div></div><div class="df4-b"><p>{{ body }}</p><div class="df4-info"><div><h4>When</h4><p>{{ date }}</p></div><div><h4>Where</h4><p>{{ venue }}</p></div></div><div class="df4-cta">▸ Buy Tickets · {{ contact }}</div></div></div>"""},

{'title': '🎨 Vintage Workshop Cream', 'desc': 'Vintage cream with serif type and old-school feel.',
 'css': """.df5{font-family:'Georgia',serif;background:#fef9c3;padding:50px 40px;color:#78350f;border:6px double #78350f;border-radius:6px;text-align:center;position:relative}
.df5::before{content:'';position:absolute;top:14px;left:14px;right:14px;bottom:14px;border:1px solid #78350f;pointer-events:none}
.df5-tag{font-size:11px;letter-spacing:4px;text-transform:uppercase;font-weight:700;color:#92400e}
.df5-divider{display:flex;align-items:center;justify-content:center;gap:14px;margin:14px 0}
.df5-divider::before,.df5-divider::after{content:'';width:60px;height:1px;background:#78350f}
.df5-divider span{font-size:18px;color:#92400e}
.df5 h1{font-size:54px;font-weight:900;color:#451a03;margin:8px 0 6px;font-style:italic;letter-spacing:-1px;line-height:1}
.df5 .sub{font-size:14px;color:#78350f;letter-spacing:2px;text-transform:uppercase;font-weight:700}
.df5 p{font-family:'Inter',sans-serif;font-size:13px;line-height:1.7;color:#78350f;max-width:400px;margin:18px auto}
.df5-info{display:flex;justify-content:center;gap:30px;margin:18px 0;font-family:'Inter',sans-serif}
.df5-info div h4{margin:0;font-size:9px;letter-spacing:1.5px;text-transform:uppercase;color:#92400e}
.df5-info div p{margin:2px 0 0;font-weight:800;color:#451a03;font-size:13px}
.df5-cta{display:inline-block;margin-top:14px;background:#78350f;color:#fef9c3;padding:14px 30px;font-family:'Inter',sans-serif;font-size:11px;letter-spacing:2px;text-transform:uppercase;font-weight:800;border-radius:4px}""",
 'html': """<div class="df5"><div class="df5-tag">{{ subtitle }}</div><div class="df5-divider"><span>❦</span></div><h1>{{ title }}</h1><div class="sub">Est. 2026</div><p>{{ body }}</p><div class="df5-info"><div><h4>Date</h4><p>{{ date }}</p></div><div><h4>Venue</h4><p>{{ venue }}</p></div></div><div class="df5-cta">RSVP · {{ contact }}</div></div>"""},
]

# ============================================================
# FESTIVALS (5)
# ============================================================
FESTIVALS = [
{'title': '🎨 Diwali Royal Gold Diya', 'desc': 'Royal black gold with diya and ornamental border.',
 'css': """.dfs1{font-family:'Playfair Display',serif;background:radial-gradient(ellipse at center,#1e1b4b 0%,#0a0a0a 100%);padding:50px 40px;color:#fde68a;text-align:center;border-radius:16px;border:3px solid #d4af37;position:relative;overflow:hidden;box-shadow:0 24px 60px rgba(212,175,55,.2)}
.dfs1::before{content:'';position:absolute;top:14px;left:14px;right:14px;bottom:14px;border:1px solid rgba(212,175,55,.4);pointer-events:none;border-radius:8px}
.dfs1::after{content:'✨';position:absolute;top:40%;left:30px;font-size:24px;color:#fbbf24;opacity:.6}
.dfs1 .diya{font-size:56px;line-height:1;margin-bottom:8px}
.dfs1 .ornament{font-size:20px;color:#d4af37;letter-spacing:14px;margin:6px 0}
.dfs1 h1{font-size:48px;font-weight:900;color:#fde68a;margin:6px 0 14px;font-style:italic;letter-spacing:-1px;text-shadow:0 0 30px rgba(251,191,36,.5)}
.dfs1 .greeting{font-family:'Inter',sans-serif;font-size:14px;color:#d4af37;letter-spacing:3px;text-transform:uppercase;margin-bottom:14px}
.dfs1 p{font-family:'Inter',sans-serif;color:#fef3c7;line-height:1.7;font-size:14px;max-width:360px;margin:14px auto;font-style:italic}
.dfs1 .from{font-family:'Inter',sans-serif;margin-top:20px;font-size:12px;color:#d4af37;letter-spacing:2px;text-transform:uppercase;font-weight:700}""",
 'html': """<div class="dfs1"><div class="diya">🪔</div><div class="ornament">✦ ❋ ✦</div><h1>{{ festival }}</h1><div class="greeting">{{ greeting }}</div><p>{{ message }}</p><div class="from">— {{ sender }}</div></div>"""},

{'title': '🎨 Holi Color Splash Burst', 'desc': 'Vibrant Holi colors splash with playful energy.',
 'css': """.dfs2{font-family:'Inter',sans-serif;background:linear-gradient(135deg,#fce7f3 0%,#fef3c7 33%,#dbeafe 66%,#dcfce7 100%);padding:50px 40px;text-align:center;border-radius:18px;color:#831843;position:relative;overflow:hidden;box-shadow:0 24px 60px rgba(236,72,153,.18)}
.dfs2::before{content:'';position:absolute;top:-40px;right:-40px;width:180px;height:180px;background:radial-gradient(circle,#ec4899,transparent 60%);opacity:.5}
.dfs2::after{content:'';position:absolute;bottom:-50px;left:-50px;width:200px;height:200px;background:radial-gradient(circle,#3b82f6,transparent 60%);opacity:.4}
.dfs2-blob1{position:absolute;top:60%;right:30px;width:80px;height:80px;background:radial-gradient(circle,#fbbf24,transparent 65%);opacity:.55}
.dfs2-blob2{position:absolute;top:30%;left:30px;width:90px;height:90px;background:radial-gradient(circle,#10b981,transparent 65%);opacity:.5}
.dfs2 .splash{position:relative;font-size:54px;line-height:1}
.dfs2 h1{position:relative;font-family:'Playfair Display',serif;font-size:54px;font-weight:900;color:#831843;margin:8px 0 10px;letter-spacing:-1.5px;font-style:italic;line-height:1}
.dfs2 .greeting{position:relative;color:#9d174d;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;font-size:13px;margin-bottom:14px}
.dfs2 p{position:relative;color:#831843;line-height:1.7;font-size:14px;max-width:400px;margin:14px auto}
.dfs2 .from{position:relative;margin-top:16px;font-size:13px;color:#9d174d;font-weight:700;font-style:italic}""",
 'html': """<div class="dfs2"><div class="dfs2-blob1"></div><div class="dfs2-blob2"></div><div class="splash">🎨 🌈</div><h1>{{ festival }}</h1><div class="greeting">{{ greeting }}</div><p>{{ message }}</p><div class="from">~ {{ sender }} ~</div></div>"""},

{'title': '🎨 Christmas Red Green Classic', 'desc': 'Classic Christmas red & green with snowflakes.',
 'css': """.dfs3{font-family:'Georgia',serif;background:#fff;padding:0;border-radius:14px;overflow:hidden;text-align:center;color:#7f1d1d;border:6px solid #15803d;box-shadow:0 24px 60px rgba(21,128,61,.2);position:relative}
.dfs3::before{content:'❄ ❄ ❄ ❄ ❄ ❄ ❄ ❄';position:absolute;top:6px;left:0;right:0;color:#15803d;font-size:14px;letter-spacing:14px}
.dfs3::after{content:'❄ ❄ ❄ ❄ ❄ ❄ ❄ ❄';position:absolute;bottom:6px;left:0;right:0;color:#15803d;font-size:14px;letter-spacing:14px}
.dfs3-h{background:linear-gradient(180deg,#dc2626 0%,#991b1b 100%);color:#fff;padding:38px 30px 26px;margin-top:24px}
.dfs3-h .tree{font-size:48px}
.dfs3-h h1{font-size:46px;font-weight:900;font-style:italic;margin:8px 0 4px;color:#fde68a;letter-spacing:-1px;line-height:1}
.dfs3-h .greeting{font-size:13px;letter-spacing:3px;text-transform:uppercase;color:#fef3c7;font-family:'Inter',sans-serif;font-weight:700}
.dfs3-b{padding:30px 36px 50px}
.dfs3-b p{font-family:'Inter',sans-serif;color:#7f1d1d;line-height:1.7;font-size:14px;max-width:380px;margin:0 auto;font-style:italic}
.dfs3-b .from{font-family:'Inter',sans-serif;margin-top:18px;color:#15803d;font-weight:800;letter-spacing:1.5px;font-size:13px;text-transform:uppercase}""",
 'html': """<div class="dfs3"><div class="dfs3-h"><div class="tree">🎄</div><h1>{{ festival }}</h1><div class="greeting">{{ greeting }}</div></div><div class="dfs3-b"><p>{{ message }}</p><div class="from">— With Love, {{ sender }}</div></div></div>"""},

{'title': '🎨 Eid Crescent Moon Gold', 'desc': 'Elegant Eid with crescent moon and Islamic ornament.',
 'css': """.dfs4{font-family:'Playfair Display',serif;background:linear-gradient(180deg,#064e3b 0%,#022c22 100%);padding:50px 40px;color:#fde68a;text-align:center;border-radius:16px;position:relative;overflow:hidden;border:2px solid #d4af37;box-shadow:0 24px 60px rgba(4,120,87,.3)}
.dfs4::before{content:'';position:absolute;top:14px;left:14px;right:14px;bottom:14px;border:1px solid rgba(212,175,55,.4);pointer-events:none;border-radius:8px}
.dfs4 .moon{font-size:60px;line-height:1;color:#fde68a;text-shadow:0 0 30px rgba(251,191,36,.6)}
.dfs4 .stars{font-size:14px;color:#d4af37;letter-spacing:8px;margin:8px 0}
.dfs4 h1{font-size:46px;font-weight:900;color:#fde68a;margin:6px 0 8px;font-style:italic;letter-spacing:-1px;line-height:1}
.dfs4 .greeting{font-family:'Inter',sans-serif;font-size:13px;color:#d4af37;letter-spacing:3px;text-transform:uppercase;font-weight:700;margin-bottom:14px}
.dfs4 p{font-family:'Inter',sans-serif;color:#fef3c7;line-height:1.7;font-size:14px;max-width:380px;margin:14px auto;font-style:italic}
.dfs4 .from{font-family:'Inter',sans-serif;margin-top:18px;color:#d4af37;font-size:12px;text-transform:uppercase;letter-spacing:2px;font-weight:700}""",
 'html': """<div class="dfs4"><div class="moon">☪</div><div class="stars">★ ★ ★</div><h1>{{ festival }}</h1><div class="greeting">{{ greeting }}</div><p>{{ message }}</p><div class="from">— {{ sender }}</div></div>"""},

{'title': '🎨 New Year Sparkle Confetti', 'desc': 'New year midnight blue with gold sparkles and confetti.',
 'css': """.dfs5{font-family:'Inter',sans-serif;background:radial-gradient(ellipse at top,#312e81 0%,#0a0a0a 100%);padding:50px 40px;text-align:center;color:#fff;border-radius:18px;position:relative;overflow:hidden;box-shadow:0 24px 60px rgba(99,102,241,.3)}
.dfs5::before{content:'✨ ✦ ✨ ✦ ✨ ✦ ✨';position:absolute;top:30px;left:0;right:0;color:#fbbf24;font-size:18px;letter-spacing:14px;opacity:.7}
.dfs5::after{content:'✨ ✦ ✨ ✦ ✨ ✦ ✨';position:absolute;bottom:30px;left:0;right:0;color:#fbbf24;font-size:18px;letter-spacing:14px;opacity:.7}
.dfs5-y{font-family:'Playfair Display',serif;font-size:96px;font-weight:900;background:linear-gradient(180deg,#fde68a,#d4af37);-webkit-background-clip:text;background-clip:text;color:transparent;line-height:1;margin:60px 0 0;letter-spacing:-3px}
.dfs5 h1{font-family:'Playfair Display',serif;font-size:36px;font-weight:900;color:#fde68a;margin:6px 0 8px;font-style:italic;letter-spacing:-1px}
.dfs5 .greeting{font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#fbbf24;font-weight:700;margin-bottom:14px}
.dfs5 p{color:#e2e8f0;line-height:1.7;font-size:14px;max-width:380px;margin:14px auto;font-style:italic}
.dfs5 .from{margin-top:18px;color:#fbbf24;font-size:12px;text-transform:uppercase;letter-spacing:2px;font-weight:700;margin-bottom:60px}""",
 'html': """<div class="dfs5"><div class="dfs5-y">2026</div><h1>{{ festival }}</h1><div class="greeting">{{ greeting }}</div><p>{{ message }}</p><div class="from">✦ {{ sender }} ✦</div></div>"""},
]

# ============================================================
# MENUS (5)
# ============================================================
MENUS = [
{'title': '🎨 Elegant Restaurant Dark', 'desc': 'Dark sophisticated restaurant menu with serif elegance.',
 'css': """.dm1{font-family:'Playfair Display',serif;background:#0a0a0a;padding:50px 44px;color:#fde68a;border-radius:14px;border:1px solid #d4af37;box-shadow:0 24px 60px rgba(0,0,0,.4)}
.dm1-h{text-align:center;border-bottom:1px solid rgba(212,175,55,.4);padding-bottom:24px;margin-bottom:24px}
.dm1-h .ornament{font-size:18px;color:#d4af37;letter-spacing:14px}
.dm1-h h1{font-size:48px;font-weight:900;color:#fde68a;margin:12px 0 6px;font-style:italic;letter-spacing:-1px;line-height:1}
.dm1-h .tag{font-family:'Inter',sans-serif;font-size:12px;color:#d4af37;letter-spacing:3px;text-transform:uppercase}
.dm1-list{margin:20px 0}
.dm1-item{display:flex;align-items:baseline;justify-content:space-between;gap:14px;padding:14px 0;border-bottom:1px dashed rgba(212,175,55,.25)}
.dm1-item .name{font-family:'Inter',sans-serif;color:#fef3c7;font-weight:700;font-size:15px}
.dm1-item .desc{font-family:'Inter',sans-serif;color:#a8a29e;font-size:12px;font-style:italic;margin-top:3px}
.dm1-item .price{font-family:'Inter',sans-serif;color:#d4af37;font-weight:900;font-size:16px;flex-shrink:0}
.dm1-item .info{flex:1;min-width:0}""",
 'html': """<div class="dm1"><div class="dm1-h"><div class="ornament">✦ ❋ ✦</div><h1>{{ restaurant }}</h1><div class="tag">{{ tagline }}</div></div><div class="dm1-list">{% for it in items %}<div class="dm1-item"><div class="info"><div class="name">{{ it.name }}</div>{% if it.desc %}<div class="desc">{{ it.desc }}</div>{% endif %}</div><div class="price">{{ it.price }}</div></div>{% endfor %}</div></div>"""},

{'title': '🎨 Cafe Chalkboard Style', 'desc': 'Chalkboard look with handwritten cafe vibes.',
 'css': """.dm2{font-family:'Caveat','cursive';background:#1a2e1a;background-image:radial-gradient(rgba(255,255,255,.04) 1px,transparent 1px);background-size:8px 8px;padding:50px 40px;color:#f5f5dc;border-radius:14px;border:8px solid #78350f;box-shadow:0 24px 60px rgba(0,0,0,.4)}
.dm2-h{text-align:center;border-bottom:2px solid rgba(245,245,220,.3);padding-bottom:18px;margin-bottom:20px}
.dm2-h h1{font-size:54px;font-weight:700;color:#fef3c7;margin:0;line-height:1;text-shadow:1px 1px 0 rgba(0,0,0,.3)}
.dm2-h .tag{font-size:22px;color:#d4d4aa;font-style:italic;margin-top:4px}
.dm2-list{font-family:'Caveat',cursive}
.dm2-item{display:flex;align-items:baseline;justify-content:space-between;gap:14px;padding:12px 0;border-bottom:1px dashed rgba(245,245,220,.25)}
.dm2-item .name{color:#fef3c7;font-weight:700;font-size:24px;line-height:1}
.dm2-item .desc{color:#d4d4aa;font-size:16px;font-style:italic;margin-top:2px}
.dm2-item .price{color:#fbbf24;font-weight:700;font-size:26px;flex-shrink:0}
.dm2-item .info{flex:1;min-width:0}""",
 'html': """<div class="dm2"><div class="dm2-h"><h1>~ {{ restaurant }} ~</h1><div class="tag">{{ tagline }}</div></div><div class="dm2-list">{% for it in items %}<div class="dm2-item"><div class="info"><div class="name">{{ it.name }}</div>{% if it.desc %}<div class="desc">{{ it.desc }}</div>{% endif %}</div><div class="price">{{ it.price }}</div></div>{% endfor %}</div></div>"""},

{'title': '🎨 Modern Minimalist White', 'desc': 'Ultra-clean white with thin lines and modern type.',
 'css': """.dm3{font-family:'Inter',sans-serif;background:#fff;padding:50px 44px;color:#0a0a0a;border:1px solid #e5e5e5;border-radius:8px}
.dm3-h{text-align:center;padding-bottom:30px;margin-bottom:24px;border-bottom:2px solid #0a0a0a}
.dm3-h h1{font-family:'Playfair Display',serif;font-size:48px;font-weight:200;color:#0a0a0a;margin:0;letter-spacing:-1.5px;line-height:1}
.dm3-h h1 strong{font-weight:900}
.dm3-h .tag{font-size:11px;color:#737373;letter-spacing:3px;text-transform:uppercase;margin-top:8px}
.dm3-list{margin:0}
.dm3-item{padding:18px 0;border-bottom:1px solid #e5e5e5;display:flex;justify-content:space-between;align-items:flex-start;gap:18px}
.dm3-item .name{color:#0a0a0a;font-weight:800;font-size:15px;letter-spacing:.3px}
.dm3-item .desc{color:#737373;font-size:12px;margin-top:4px;line-height:1.5}
.dm3-item .price{color:#0a0a0a;font-weight:900;font-size:16px;flex-shrink:0}
.dm3-item .info{flex:1;min-width:0}""",
 'html': """<div class="dm3"><div class="dm3-h"><h1>{{ restaurant }}</h1><div class="tag">{{ tagline }}</div></div><div class="dm3-list">{% for it in items %}<div class="dm3-item"><div class="info"><div class="name">{{ it.name }}</div>{% if it.desc %}<div class="desc">{{ it.desc }}</div>{% endif %}</div><div class="price">{{ it.price }}</div></div>{% endfor %}</div></div>"""},

{'title': '🎨 Vintage Italian Trattoria', 'desc': 'Italian trattoria vintage cream with classic serif.',
 'css': """.dm4{font-family:'Georgia',serif;background:#fef9c3;padding:50px 40px;color:#78350f;border:5px double #78350f;border-radius:6px;position:relative}
.dm4::before{content:'';position:absolute;top:14px;left:14px;right:14px;bottom:14px;border:1px solid #78350f;pointer-events:none}
.dm4-h{text-align:center;padding-bottom:18px;margin-bottom:20px;border-bottom:2px solid #78350f}
.dm4-h .tag{font-size:11px;letter-spacing:4px;text-transform:uppercase;color:#92400e;font-weight:700}
.dm4-h h1{font-size:48px;font-weight:900;color:#451a03;margin:8px 0 4px;font-style:italic;letter-spacing:-1px;line-height:1}
.dm4-h .est{font-family:'Inter',sans-serif;font-size:10px;letter-spacing:3px;text-transform:uppercase;color:#92400e}
.dm4-list{margin:0}
.dm4-item{padding:14px 0;border-bottom:1px dotted #92400e;display:flex;align-items:baseline;justify-content:space-between;gap:18px}
.dm4-item .name{font-weight:900;color:#451a03;font-size:16px;font-style:italic}
.dm4-item .desc{font-family:'Inter',sans-serif;color:#78350f;font-size:11px;margin-top:3px;font-style:italic}
.dm4-item .price{color:#7f1d1d;font-weight:900;font-size:17px;flex-shrink:0;font-style:italic}
.dm4-item .info{flex:1;min-width:0}""",
 'html': """<div class="dm4"><div class="dm4-h"><div class="tag">~ Trattoria ~</div><h1>{{ restaurant }}</h1><div class="est">{{ tagline }} · Est. 2026</div></div><div class="dm4-list">{% for it in items %}<div class="dm4-item"><div class="info"><div class="name">{{ it.name }}</div>{% if it.desc %}<div class="desc">{{ it.desc }}</div>{% endif %}</div><div class="price">{{ it.price }}</div></div>{% endfor %}</div></div>"""},

{'title': '🎨 Tropical Beach Bar', 'desc': 'Tropical sunset gradient with palm and beach vibes.',
 'css': """.dm5{font-family:'Inter',sans-serif;background:linear-gradient(160deg,#fef3c7 0%,#fed7aa 50%,#fda4af 100%);padding:50px 40px;color:#7c2d12;border-radius:18px;position:relative;overflow:hidden;box-shadow:0 24px 60px rgba(251,146,60,.2)}
.dm5::before{content:'🌴';position:absolute;top:24px;left:24px;font-size:42px;opacity:.7}
.dm5::after{content:'🌺';position:absolute;top:24px;right:24px;font-size:42px;opacity:.7}
.dm5-h{text-align:center;padding:30px 0 20px;border-bottom:2px dashed #c2410c;margin-bottom:20px}
.dm5-h h1{font-family:'Caveat',cursive;font-size:54px;font-weight:700;color:#7c2d12;margin:0;line-height:1}
.dm5-h .tag{font-size:13px;color:#9a3412;letter-spacing:2px;text-transform:uppercase;font-weight:700;margin-top:4px}
.dm5-list{margin:0}
.dm5-item{padding:14px 0;border-bottom:1px dashed rgba(194,65,12,.4);display:flex;align-items:baseline;justify-content:space-between;gap:18px}
.dm5-item .name{font-weight:800;color:#7c2d12;font-size:15px}
.dm5-item .desc{color:#9a3412;font-size:12px;font-style:italic;margin-top:3px}
.dm5-item .price{background:#7c2d12;color:#fef3c7;padding:6px 14px;border-radius:30px;font-weight:800;font-size:13px;flex-shrink:0}
.dm5-item .info{flex:1;min-width:0}""",
 'html': """<div class="dm5"><div class="dm5-h"><h1>~ {{ restaurant }} ~</h1><div class="tag">{{ tagline }}</div></div><div class="dm5-list">{% for it in items %}<div class="dm5-item"><div class="info"><div class="name">{{ it.name }}</div>{% if it.desc %}<div class="desc">{{ it.desc }}</div>{% endif %}</div><div class="price">{{ it.price }}</div></div>{% endfor %}</div></div>"""},
]

# ============================================================
# TICKETS (5)
# ============================================================
TICKETS = [
{'title': '🎨 Concert Neon Stub', 'desc': 'Modern concert ticket with neon glow and tear stub.',
 'css': """.dt1{font-family:'Inter',sans-serif;background:#0a0014;display:grid;grid-template-columns:1fr 130px;border-radius:14px;overflow:hidden;color:#fff;box-shadow:0 24px 60px rgba(236,72,153,.3);border:1px solid rgba(236,72,153,.4)}
.dt1-main{padding:32px 30px;background:linear-gradient(135deg,#0a0014 0%,#1e0a2e 100%);position:relative}
.dt1-main::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at top right,rgba(236,72,153,.15),transparent 60%)}
.dt1-main .tag{position:relative;color:#22d3ee;font-size:11px;letter-spacing:4px;text-transform:uppercase;font-weight:800;text-shadow:0 0 14px #22d3ee}
.dt1-main h1{position:relative;font-size:32px;font-weight:900;margin:8px 0 14px;letter-spacing:-1px;line-height:1;color:#fff;text-shadow:0 0 20px rgba(236,72,153,.5)}
.dt1-main .grid{position:relative;display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:14px}
.dt1-main .grid div h4{margin:0;font-size:9px;letter-spacing:1.5px;color:#22d3ee;text-transform:uppercase}
.dt1-main .grid div p{margin:3px 0 0;font-size:13px;font-weight:700;color:#fff}
.dt1-stub{background:linear-gradient(180deg,#ec4899 0%,#a855f7 100%);padding:24px 14px;display:flex;flex-direction:column;justify-content:center;align-items:center;border-left:2px dashed rgba(255,255,255,.3);text-align:center;position:relative}
.dt1-stub::before,.dt1-stub::after{content:'';position:absolute;left:-10px;width:20px;height:20px;background:#0a0014;border-radius:50%}
.dt1-stub::before{top:-10px}.dt1-stub::after{bottom:-10px}
.dt1-stub h4{margin:0;font-size:9px;letter-spacing:1.5px;text-transform:uppercase;opacity:.85}
.dt1-stub .seat{font-size:34px;font-weight:900;line-height:1;margin:6px 0}
.dt1-stub .price{font-size:18px;font-weight:900;margin-top:8px}
.dt1-stub .no{font-family:monospace;font-size:9px;margin-top:10px;opacity:.85;letter-spacing:1px}""",
 'html': """<div class="dt1"><div class="dt1-main"><div class="tag">// LIVE</div><h1>{{ event }}</h1><div class="grid"><div><h4>Date</h4><p>{{ date }}</p></div><div><h4>Time</h4><p>{{ time }}</p></div><div><h4>Venue</h4><p>{{ venue }}</p></div><div><h4>Ticket #</h4><p>{{ ticket_no }}</p></div></div></div><div class="dt1-stub"><h4>Seat</h4><div class="seat">{{ seat }}</div><h4>Price</h4><div class="price">{{ price }}</div><div class="no">{{ ticket_no }}</div></div></div>"""},

{'title': '🎨 Cinema Vintage Red', 'desc': 'Classic cinema admit-one red vintage ticket.',
 'css': """.dt2{font-family:'Georgia',serif;background:#dc2626;display:grid;grid-template-columns:1fr 110px;border-radius:6px;overflow:hidden;color:#fef3c7;border:3px solid #78350f;box-shadow:0 24px 60px rgba(220,38,38,.3)}
.dt2-main{padding:24px 28px;border-right:2px dashed #fef3c7;position:relative}
.dt2-main::before{content:'';position:absolute;top:14px;left:14px;right:14px;bottom:14px;border:1px solid rgba(254,243,199,.3);pointer-events:none;border-radius:4px}
.dt2-main .tag{position:relative;font-size:10px;letter-spacing:4px;text-transform:uppercase;font-weight:700;text-align:center;color:#fbbf24}
.dt2-main h1{position:relative;font-size:30px;font-weight:900;font-style:italic;margin:6px 0 8px;text-align:center;letter-spacing:-.5px;line-height:1}
.dt2-main .divider{position:relative;text-align:center;color:#fbbf24;letter-spacing:14px;margin:6px 0;font-size:12px}
.dt2-main .info{position:relative;display:grid;grid-template-columns:1fr 1fr;gap:8px;font-size:11px;font-family:'Inter',sans-serif}
.dt2-main .info div{text-align:center}
.dt2-main .info h4{margin:0;font-size:8px;text-transform:uppercase;letter-spacing:1.5px;opacity:.85}
.dt2-main .info p{margin:2px 0 0;font-weight:800;color:#fff}
.dt2-stub{padding:22px 12px;text-align:center;background:rgba(0,0,0,.15);display:flex;flex-direction:column;justify-content:center}
.dt2-stub .lbl{font-family:'Inter',sans-serif;font-size:9px;letter-spacing:2px;text-transform:uppercase;opacity:.85}
.dt2-stub .seat{font-size:36px;font-weight:900;font-style:italic;margin:4px 0;color:#fbbf24;line-height:1}
.dt2-stub .price{font-size:16px;font-weight:900;color:#fff;margin-top:8px}
.dt2-stub .no{font-family:'monospace';font-size:8px;margin-top:8px;opacity:.7}""",
 'html': """<div class="dt2"><div class="dt2-main"><div class="tag">★ Admit One ★</div><h1>{{ event }}</h1><div class="divider">— • —</div><div class="info"><div><h4>Date</h4><p>{{ date }}</p></div><div><h4>Time</h4><p>{{ time }}</p></div><div><h4>Venue</h4><p>{{ venue }}</p></div><div><h4>Row</h4><p>{{ seat }}</p></div></div></div><div class="dt2-stub"><div class="lbl">Seat</div><div class="seat">{{ seat }}</div><div class="lbl">{{ price }}</div><div class="no">{{ ticket_no }}</div></div></div>"""},

{'title': '🎨 Conference Modern Gradient', 'desc': 'Professional conference badge with gradient header.',
 'css': """.dt3{font-family:'Inter',sans-serif;background:#fff;border-radius:14px;overflow:hidden;color:#0f172a;box-shadow:0 24px 60px rgba(59,130,246,.18)}
.dt3-h{background:linear-gradient(135deg,#1e40af 0%,#3b82f6 50%,#06b6d4 100%);padding:30px 32px;color:#fff;position:relative}
.dt3-h::after{content:'';position:absolute;bottom:-12px;left:0;right:0;height:24px;background:repeating-linear-gradient(90deg,#fff 0,#fff 12px,transparent 12px,transparent 24px)}
.dt3-h .tag{font-size:11px;letter-spacing:3px;text-transform:uppercase;opacity:.9;font-weight:700}
.dt3-h h1{font-size:30px;font-weight:900;letter-spacing:-1px;margin:6px 0 0;line-height:1.05}
.dt3-b{padding:30px 32px}
.dt3-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.dt3-grid div{padding:14px;background:#eff6ff;border-left:3px solid #3b82f6;border-radius:6px}
.dt3-grid h4{margin:0;font-size:10px;letter-spacing:1.5px;color:#3b82f6;text-transform:uppercase;font-weight:800}
.dt3-grid p{margin:3px 0 0;font-size:13px;font-weight:800;color:#0f172a}
.dt3-bot{margin-top:20px;display:flex;justify-content:space-between;align-items:center;border-top:2px dashed #e2e8f0;padding-top:18px}
.dt3-bot .seat{background:#1e40af;color:#fff;padding:14px 24px;border-radius:8px;font-weight:900;font-size:18px}
.dt3-bot .price{font-size:24px;font-weight:900;color:#0f172a}
.dt3-bot .no{font-family:monospace;font-size:11px;color:#64748b}""",
 'html': """<div class="dt3"><div class="dt3-h"><div class="tag">Conference Pass</div><h1>{{ event }}</h1></div><div class="dt3-b"><div class="dt3-grid"><div><h4>Date</h4><p>{{ date }}</p></div><div><h4>Time</h4><p>{{ time }}</p></div><div><h4>Venue</h4><p>{{ venue }}</p></div><div><h4>Ticket</h4><p>{{ ticket_no }}</p></div></div><div class="dt3-bot"><div class="seat">{{ seat }}</div><div class="price">{{ price }}</div><div class="no">{{ ticket_no }}</div></div></div></div>"""},

{'title': '🎨 Festival Holographic Vibe', 'desc': 'Holographic festival ticket with iridescent gradient.',
 'css': """.dt4{font-family:'Inter',sans-serif;background:linear-gradient(135deg,#a855f7 0%,#ec4899 25%,#f59e0b 50%,#10b981 75%,#3b82f6 100%);padding:3px;border-radius:18px;box-shadow:0 24px 60px rgba(168,85,247,.3)}
.dt4-inner{background:#0a0014;border-radius:16px;padding:32px 30px;color:#fff;position:relative;overflow:hidden}
.dt4-inner::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(168,85,247,.15),transparent 50%,rgba(236,72,153,.15));pointer-events:none}
.dt4-h{position:relative;text-align:center;border-bottom:1px dashed rgba(255,255,255,.3);padding-bottom:18px;margin-bottom:18px}
.dt4-h .tag{display:inline-block;background:linear-gradient(135deg,#a855f7,#ec4899);padding:5px 14px;border-radius:30px;font-size:10px;font-weight:800;letter-spacing:2px;text-transform:uppercase}
.dt4-h h1{font-size:32px;font-weight:900;margin:10px 0 0;letter-spacing:-1px;line-height:1;background:linear-gradient(135deg,#fff,#fde68a);-webkit-background-clip:text;background-clip:text;color:transparent}
.dt4-grid{position:relative;display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:18px}
.dt4-grid div h4{margin:0;font-size:9px;letter-spacing:1.5px;color:#fbbf24;text-transform:uppercase;font-weight:800}
.dt4-grid div p{margin:3px 0 0;font-size:13px;font-weight:700;color:#fff}
.dt4-bot{position:relative;display:flex;justify-content:space-between;align-items:center;background:rgba(255,255,255,.06);padding:14px 18px;border-radius:10px;border:1px solid rgba(255,255,255,.15)}
.dt4-bot .seat{font-size:24px;font-weight:900;background:linear-gradient(135deg,#fbbf24,#ec4899);-webkit-background-clip:text;background-clip:text;color:transparent}
.dt4-bot .price{font-size:18px;font-weight:900;color:#fbbf24}
.dt4-bot .no{font-family:monospace;font-size:9px;color:#94a3b8}""",
 'html': """<div class="dt4"><div class="dt4-inner"><div class="dt4-h"><div class="tag">★ Festival Pass</div><h1>{{ event }}</h1></div><div class="dt4-grid"><div><h4>Date</h4><p>{{ date }}</p></div><div><h4>Time</h4><p>{{ time }}</p></div><div><h4>Venue</h4><p>{{ venue }}</p></div><div><h4>Ticket</h4><p>{{ ticket_no }}</p></div></div><div class="dt4-bot"><div class="seat">{{ seat }}</div><div class="price">{{ price }}</div><div class="no">{{ ticket_no }}</div></div></div></div>"""},

{'title': '🎨 VIP Black Gold Elite', 'desc': 'Elite VIP black with gold foil and luxury feel.',
 'css': """.dt5{font-family:'Playfair Display',serif;background:#0a0a0a;display:grid;grid-template-columns:1fr 130px;border-radius:10px;overflow:hidden;color:#fde68a;border:2px solid #d4af37;box-shadow:0 24px 60px rgba(212,175,55,.25)}
.dt5-main{padding:30px 32px;border-right:2px dashed rgba(212,175,55,.4);position:relative}
.dt5-main::before{content:'';position:absolute;top:14px;left:14px;right:14px;bottom:14px;border:1px solid rgba(212,175,55,.3);pointer-events:none;border-radius:4px}
.dt5-main .crown{position:relative;font-size:28px;color:#d4af37;text-align:center;line-height:1}
.dt5-main .tag{position:relative;font-family:'Inter',sans-serif;font-size:10px;letter-spacing:5px;text-transform:uppercase;text-align:center;color:#d4af37;font-weight:800;margin-top:4px}
.dt5-main h1{position:relative;font-size:30px;font-weight:900;color:#fde68a;text-align:center;margin:8px 0 12px;font-style:italic;letter-spacing:-.5px;line-height:1}
.dt5-main .divider{position:relative;text-align:center;color:#d4af37;letter-spacing:14px;font-size:14px;margin:8px 0}
.dt5-main .info{position:relative;display:grid;grid-template-columns:1fr 1fr;gap:10px;font-family:'Inter',sans-serif;font-size:11px}
.dt5-main .info h4{margin:0;font-size:9px;letter-spacing:1.5px;color:#d4af37;text-transform:uppercase}
.dt5-main .info p{margin:2px 0 0;font-weight:800;color:#fef3c7}
.dt5-stub{padding:24px 12px;text-align:center;display:flex;flex-direction:column;justify-content:center;background:linear-gradient(180deg,rgba(212,175,55,.1),rgba(212,175,55,.04))}
.dt5-stub .lbl{font-family:'Inter',sans-serif;font-size:9px;letter-spacing:2px;text-transform:uppercase;color:#d4af37;font-weight:800}
.dt5-stub .seat{font-size:34px;font-weight:900;font-style:italic;color:#fde68a;line-height:1;margin:4px 0}
.dt5-stub .price{font-family:'Inter',sans-serif;font-size:14px;font-weight:900;color:#d4af37;margin-top:6px}
.dt5-stub .no{font-family:monospace;font-size:8px;margin-top:8px;color:#a8a29e}""",
 'html': """<div class="dt5"><div class="dt5-main"><div class="crown">♛</div><div class="tag">VIP Access</div><h1>{{ event }}</h1><div class="divider">— ✦ —</div><div class="info"><div><h4>Date</h4><p>{{ date }}</p></div><div><h4>Time</h4><p>{{ time }}</p></div><div><h4>Venue</h4><p>{{ venue }}</p></div><div><h4>Row</h4><p>{{ seat }}</p></div></div></div><div class="dt5-stub"><div class="lbl">Seat</div><div class="seat">{{ seat }}</div><div class="lbl">Price</div><div class="price">{{ price }}</div><div class="no">{{ ticket_no }}</div></div></div>"""},
]
