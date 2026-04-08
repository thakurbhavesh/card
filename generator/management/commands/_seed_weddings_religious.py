"""15 additional wedding templates organized by religion / region."""

# Extended field schema for richer wedding cards (parents, blessing, ceremonies)
WEDDING_FIELDS_PRO = [
    {'name': 'bride', 'label': 'Bride Name', 'type': 'text'},
    {'name': 'groom', 'label': 'Groom Name', 'type': 'text'},
    {'name': 'bride_parents', 'label': "Bride's Parents", 'type': 'text'},
    {'name': 'groom_parents', 'label': "Groom's Parents", 'type': 'text'},
    {'name': 'date', 'label': 'Wedding Date', 'type': 'text'},
    {'name': 'time', 'label': 'Time', 'type': 'text'},
    {'name': 'venue', 'label': 'Venue', 'type': 'textarea'},
    {'name': 'blessing', 'label': 'Blessing / Quote', 'type': 'textarea', 'ai': True},
    {'name': 'message', 'label': 'Message', 'type': 'textarea', 'ai': True},
    {'name': 'rsvp', 'label': 'RSVP Contact', 'type': 'text'},
]

# Multi-ceremony field schema (Gujarati / Marathi / multi-event weddings)
WEDDING_FIELDS_MULTI = [
    {'name': 'bride', 'label': 'Bride Name', 'type': 'text'},
    {'name': 'groom', 'label': 'Groom Name', 'type': 'text'},
    {'name': 'bride_parents', 'label': "Bride's Parents", 'type': 'text'},
    {'name': 'groom_parents', 'label': "Groom's Parents", 'type': 'text'},
    {'name': 'blessing', 'label': 'Blessing / Heading', 'type': 'text', 'ai': True},
    {'name': 'subtext', 'label': 'Sub-text', 'type': 'textarea', 'ai': True},
    {'name': 'venue', 'label': 'Main Venue', 'type': 'text'},
    {'name': 'invited_by', 'label': 'Invited By', 'type': 'text'},
    {'name': 'ceremonies', 'label': 'Ceremonies', 'type': 'items',
     'item_fields': [
         {'name': 'name', 'label': 'Ceremony Name', 'placeholder': 'e.g. Mandap Muhurat'},
         {'name': 'date', 'label': 'Date', 'placeholder': 'Sun, 29th May'},
         {'name': 'time', 'label': 'Time', 'placeholder': 'From 3 PM'},
         {'name': 'venue', 'label': 'Venue', 'placeholder': 'At Banquet'},
     ]},
]

GUJARATI_SAMPLE = {
    'bride': 'Krisha',
    'groom': 'Rohan',
    'bride_parents': 'D/o Smt. Sonal Patel & Sh. Hitesh Patel',
    'groom_parents': 'S/o Smt. Bhavna Patel & Sh. Ramesh Patel',
    'blessing': 'શુભ વિવાહ',
    'subtext': 'We Wholeheartedly Seek Your Plentiful Blessings For The Couple',
    'venue': 'Farm Name, Katargam, Surat',
    'invited_by': 'Invited By Patel Family',
    'ceremonies': [
        {'name': 'મંડપ મુહૂર્ત', 'date': 'Sun, 29th May', 'time': 'From 3 PM',  'venue': 'At Banquet Name'},
        {'name': 'ભોજન સમારંભ', 'date': 'Sun, 29th May', 'time': 'From 6 PM',  'venue': 'At Banquet Name'},
        {'name': 'રાસ ગરબા',     'date': 'Sun, 29th May', 'time': 'From 8 PM',  'venue': 'At Farm Name'},
        {'name': 'જાન પ્રસ્થાન',  'date': 'Mon, 30th May', 'time': 'From 6 PM',  'venue': ''},
        {'name': 'હસ્તમેળાપ',     'date': 'Mon, 30th May', 'time': 'From 8 PM',  'venue': ''},
    ],
}

# Religion-specific sample data
PAKISTANI_SAMPLE = {
    'bride': 'Bride Name', 'groom': 'Groom Name',
    'bride_parents': '', 'groom_parents': '',
    'date': 'December 16, 2024', 'time': 'At 8:00 PM',
    'venue': 'Excellency Banquet,\nnear continental bakery,\nGulistan e Johar',
    'blessing': 'بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ',
    'message': 'cordially invite you to join the occasion of their joyous commitment on',
    'rsvp': 'RSVP +92 300 1234567',
}

SAMIRA_SAMPLE = {
    'bride': 'Samira', 'groom': 'Raid',
    'bride_parents': '', 'groom_parents': '',
    'date': 'June 07, 2024', 'time': 'At 12 PM',
    'venue': '123 Anywhere St,\nAny City, ST 12345',
    'blessing': 'بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ',
    'message': 'In the name of Allah, the Most Gracious, the Most Merciful',
    'rsvp': 'Reception to follow',
}

CEREMONY_SAMPLES = {
    'mehendi': {
        'bride': 'Priya', 'groom': 'Arjun',
        'bride_parents': '', 'groom_parents': '',
        'date': 'Friday, 20th November 2026', 'time': '4:00 PM onwards',
        'venue': 'Sharma Residence,\nGreen Park, Delhi',
        'blessing': '|| Mehendi Ceremony ||',
        'message': 'Join us for an evening of mehendi, music and laughter as we celebrate the bride-to-be.',
        'rsvp': '+91 98765 43210',
    },
    'sangeet': {
        'bride': 'Priya', 'groom': 'Arjun',
        'bride_parents': '', 'groom_parents': '',
        'date': 'Saturday, 21st November 2026', 'time': '7:00 PM onwards',
        'venue': 'The Grand Ballroom,\nLeela Palace, Delhi',
        'blessing': '~ Sangeet Night ~',
        'message': 'A night of music, dance and celebration. Bring your dancing shoes!',
        'rsvp': '+91 98765 43210',
    },
    'haldi': {
        'bride': 'Priya', 'groom': 'Arjun',
        'bride_parents': '', 'groom_parents': '',
        'date': 'Sunday, 22nd November 2026', 'time': '10:00 AM',
        'venue': 'Sharma Residence,\nGreen Park, Delhi',
        'blessing': '~ Haldi Ceremony ~',
        'message': 'Join us for the auspicious Haldi ceremony — wear yellow and bring blessings!',
        'rsvp': '+91 98765 43210',
    },
    'baraat': {
        'bride': 'Priya', 'groom': 'Arjun',
        'bride_parents': '', 'groom_parents': '',
        'date': 'Sunday, 22nd November 2026', 'time': '6:00 PM',
        'venue': 'Departing from Kapoor Residence',
        'blessing': '~ Baraat Procession ~',
        'message': 'Join the groom\'s grand procession with dhol, dance and celebration!',
        'rsvp': '+91 98765 43210',
    },
    'tamil': {
        'bride': 'Lakshmi', 'groom': 'Karthik',
        'bride_parents': 'Mr. & Mrs. Iyer', 'groom_parents': 'Mr. & Mrs. Raman',
        'date': 'Friday, 18th September 2026', 'time': '6:30 AM (Muhurtham)',
        'venue': 'Sri Ranganathaswamy Temple,\nSrirangam, Tamil Nadu',
        'blessing': '|| ஓம் கணேசாய நமஹ ||\nWith the divine blessings of Lord Vinayaka',
        'message': 'திருமண அழைப்பிதழ் — Cordially invite you to grace the auspicious wedding ceremony.',
        'rsvp': '+91 98401 23456',
    },
    'telugu': {
        'bride': 'Sravani', 'groom': 'Sai Krishna',
        'bride_parents': 'Sri & Smt. Reddy', 'groom_parents': 'Sri & Smt. Rao',
        'date': 'Sunday, 12th October 2026', 'time': '5:30 AM (Muhurtham)',
        'venue': 'Tirumala Tirupati Devasthanam,\nTirupati',
        'blessing': '|| శ్రీ గణేశాయ నమః ||\nWith the blessings of Lord Venkateswara',
        'message': 'వివాహ శుభాకాంక్షలు — Request the honour of your presence at the wedding.',
        'rsvp': '+91 99489 12345',
    },
    'marathi': {
        'bride': 'Sneha', 'groom': 'Rohit',
        'bride_parents': 'Shri. & Sau. Patil', 'groom_parents': 'Shri. & Sau. Joshi',
        'date': 'Saturday, 14th February 2026', 'time': '11:30 AM (Muhurt)',
        'venue': 'Saraswati Mangal Karyalaya,\nPune, Maharashtra',
        'blessing': '|| श्री गणेशाय नमः ||\nशुभ विवाह सोहळा',
        'message': 'विवाह सोहळ्यास सहकुटुंब उपस्थित राहावे ही नम्र विनंती.',
        'rsvp': '+91 98220 34567',
    },
    'punjabi': {
        'bride': 'Simran', 'groom': 'Harpreet',
        'bride_parents': 'S. Gurmeet Singh & Family', 'groom_parents': 'S. Jaswinder Singh & Family',
        'date': 'Sunday, 5th October 2026', 'time': '10:00 AM',
        'venue': 'Gurudwara Bangla Sahib,\nNew Delhi',
        'blessing': 'ੴ ਸਤਿ ਨਾਮੁ\nWith the blessings of Waheguru Ji',
        'message': 'ਆਨੰਦ ਕਾਰਜ — Cordially invite you to grace the Anand Karaj ceremony.',
        'rsvp': '+91 99887 76655',
    },
}

SAMPLES = {
    'pakistani': PAKISTANI_SAMPLE,
    'samira': SAMIRA_SAMPLE,
    **CEREMONY_SAMPLES,
    'hindu': {
        'bride': 'Priya', 'groom': 'Arjun',
        'bride_parents': 'Mr. & Mrs. Sharma', 'groom_parents': 'Mr. & Mrs. Kapoor',
        'date': 'Sunday, 22nd November 2026', 'time': '7:00 PM onwards',
        'venue': 'Umaid Bhawan Palace,\nJodhpur, Rajasthan',
        'blessing': '|| श्री गणेशाय नमः ||\nWith the blessings of Lord Ganesha and our elders',
        'message': 'Together with their families, request the honour of your presence to celebrate the union of their children in holy matrimony.',
        'rsvp': '+91 98765 43210',
    },
    'muslim': {
        'bride': 'Ayesha', 'groom': 'Imran',
        'bride_parents': 'Mr. & Mrs. Khan', 'groom_parents': 'Mr. & Mrs. Ahmed',
        'date': 'Friday, 14th August 2026', 'time': '8:00 PM onwards',
        'venue': 'The Oberoi,\nHyderabad',
        'blessing': 'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\nIn the name of Allah, the Most Gracious',
        'message': 'You are cordially invited to the Nikah ceremony and walima reception of our beloved children.',
        'rsvp': '+91 91234 56789',
    },
    'christian': {
        'bride': 'Sarah', 'groom': 'Daniel',
        'bride_parents': 'Mr. & Mrs. D\'Souza', 'groom_parents': 'Mr. & Mrs. Fernandes',
        'date': 'Saturday, 12th December 2026', 'time': '4:00 PM',
        'venue': 'St. Mary\'s Church,\nGoa',
        'blessing': '"Two are better than one... A cord of three strands is not quickly broken." — Ecclesiastes 4:9-12',
        'message': 'Together with their families, request the pleasure of your company at the wedding ceremony followed by a reception.',
        'rsvp': '+91 90000 11111',
    },
    'sikh': {
        'bride': 'Simran', 'groom': 'Harpreet',
        'bride_parents': 'S. Gurmeet Singh & Family', 'groom_parents': 'S. Jaswinder Singh & Family',
        'date': 'Sunday, 5th October 2026', 'time': '10:00 AM',
        'venue': 'Gurudwara Bangla Sahib,\nNew Delhi',
        'blessing': 'ੴ ਸਤਿ ਨਾਮੁ\nWith the blessings of Waheguru',
        'message': 'You are cordially invited to grace the Anand Karaj ceremony of our beloved children.',
        'rsvp': '+91 99887 76655',
    },
    'south': {
        'bride': 'Lakshmi', 'groom': 'Karthik',
        'bride_parents': 'Mr. & Mrs. Iyer', 'groom_parents': 'Mr. & Mrs. Raman',
        'date': 'Friday, 18th September 2026', 'time': '6:30 AM (Muhurtham)',
        'venue': 'Sri Ranganathaswamy Temple,\nSrirangam, Tamil Nadu',
        'blessing': '|| ॐ श्री महा गणपतये नमः ||\nWith the divine blessings of Lord Ganesha',
        'message': 'Cordially invite you with family to grace the auspicious occasion of the wedding ceremony.',
        'rsvp': '+91 98401 23456',
    },
    'bengali': {
        'bride': 'Riya', 'groom': 'Abhijit',
        'bride_parents': 'Mr. & Mrs. Banerjee', 'groom_parents': 'Mr. & Mrs. Mukherjee',
        'date': 'Sunday, 8th February 2026', 'time': '7:30 PM',
        'venue': 'ITC Sonar,\nKolkata',
        'blessing': '|| শুভ বিবাহ ||\nWith joyful hearts and family blessings',
        'message': 'Request the pleasure of your company at the wedding ceremony of our beloved children.',
        'rsvp': '+91 98300 12345',
    },
}


WEDDINGS_RELIGIOUS = [
    # ============ HINDU (5 variants) ============
    {'title': 'Hindu Royal Maroon', 'religion': 'hindu',
     'desc': 'Traditional maroon & gold Hindu wedding with Ganesha blessing.',
     'css': ".hr1{width:560px;margin:30px auto;padding:0;background:#fff;font-family:Georgia,serif;text-align:center;border:6px double #c9a227;box-shadow:0 30px 70px rgba(122,0,25,.4)}.hr1 .top{background:linear-gradient(135deg,#7a0019,#a51c30);color:#fff8e1;padding:30px 40px;border-bottom:4px solid #c9a227}.hr1 .ico{font-size:46px;color:#f5c842;margin-bottom:6px}.hr1 .small{font-size:11px;letter-spacing:6px;color:#f5c842;text-transform:uppercase}.hr1 .blessing{font-style:italic;font-size:14px;color:#fff8e1;line-height:1.7;margin-top:10px;white-space:pre-line}.hr1 .body{padding:30px 40px;background:#fffaf0}.hr1 .parents{font-size:13px;color:#7a0019;margin:8px 0}.hr1 h1{font-size:46px;margin:14px 0 6px;color:#7a0019;font-style:italic}.hr1 .weds{font-size:18px;color:#c9a227;letter-spacing:6px;margin:10px 0}.hr1 .info{margin-top:20px;padding-top:18px;border-top:1px solid #c9a227;font-size:14px;line-height:1.8;color:#5d4037}.hr1 .info strong{color:#7a0019;display:block;font-size:16px}.hr1 .msg{font-size:13px;font-style:italic;color:#666;margin:14px 30px}",
     'html': '<div class="hr1"><div class="top"><div class="ico">🕉</div><div class="small">SHUBH VIVAH</div><div class="blessing">{{ blessing }}</div></div><div class="body"><div class="parents">{{ bride_parents }}<br>cordially invite you to the wedding of their daughter</div><h1>{{ bride }}</h1><div class="weds">WEDS</div><h1>{{ groom }}</h1><div class="parents">son of {{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br><br>RSVP: {{ rsvp }}</div></div></div>'},

    {'title': 'Hindu Saffron Mandap', 'religion': 'hindu',
     'desc': 'Saffron & marigold themed mandap-style invite.',
     'css': ".hr2{width:560px;margin:30px auto;padding:50px 40px;background:linear-gradient(180deg,#fff8e1 0%,#ffe0b2 100%);color:#bf360c;text-align:center;font-family:Georgia,serif;border:8px solid #ff6f00;border-radius:8px;box-shadow:0 30px 70px rgba(255,111,0,.3);position:relative}.hr2::before{content:'🌼 🌼 🌼 🌼 🌼';display:block;font-size:18px;letter-spacing:8px;margin-bottom:14px}.hr2::after{content:'🌼 🌼 🌼 🌼 🌼';display:block;font-size:18px;letter-spacing:8px;margin-top:14px}.hr2 .ico{font-size:40px;color:#bf360c}.hr2 .blessing{font-style:italic;color:#bf360c;font-size:14px;line-height:1.7;margin:14px 30px;white-space:pre-line}.hr2 h1{font-size:48px;margin:14px 0 6px;color:#bf360c;font-style:italic}.hr2 .weds{font-size:16px;color:#e65100;letter-spacing:6px;margin:10px 0;font-weight:bold}.hr2 .parents{font-size:13px;color:#5d4037;margin:6px 0}.hr2 .msg{font-size:13px;font-style:italic;color:#5d4037;margin:14px 30px}.hr2 .info{margin-top:18px;padding-top:14px;border-top:2px solid #ff6f00;font-size:14px;line-height:1.8;color:#5d4037}.hr2 .info strong{color:#bf360c}",
     'html': '<div class="hr2"><div class="ico">🛕</div><div class="blessing">{{ blessing }}</div><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">~ वि वा ह ~</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Hindu Lotus Pink', 'religion': 'hindu',
     'desc': 'Soft pink lotus motif for serene Hindu weddings.',
     'css': ".hr3{width:560px;margin:30px auto;padding:50px 40px;background:#fff0f5;color:#880e4f;text-align:center;font-family:Georgia,serif;border:3px double #ec407a;border-radius:14px;box-shadow:0 24px 60px rgba(236,64,122,.3)}.hr3 .ico{font-size:46px;color:#e91e63}.hr3 .small{font-size:11px;letter-spacing:6px;color:#ad1457;text-transform:uppercase}.hr3 .blessing{font-style:italic;color:#ad1457;font-size:14px;line-height:1.7;margin:14px 30px;white-space:pre-line}.hr3 h1{font-size:48px;margin:14px 0 6px;color:#880e4f;font-style:italic}.hr3 .weds{font-size:18px;color:#ec407a;letter-spacing:6px;margin:10px 0}.hr3 .parents{font-size:13px;color:#ad1457;margin:6px 0}.hr3 .msg{font-size:13px;font-style:italic;color:#666;margin:14px 30px}.hr3 .info{margin-top:18px;padding-top:14px;border-top:1px solid #ec407a;font-size:14px;line-height:1.8;color:#5d4037}.hr3 .info strong{color:#880e4f}",
     'html': '<div class="hr3"><div class="ico">🪷</div><div class="small">SHUBH VIVAH</div><div class="blessing">{{ blessing }}</div><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">&amp;</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Hindu Ganesh Tradition', 'religion': 'hindu',
     'desc': 'Ganesh-blessed traditional invite with classic ornament.',
     'css': ".hr4{width:560px;margin:30px auto;padding:50px 40px;background:#fffaf0;color:#3e2723;text-align:center;font-family:Georgia,serif;border:1px solid #c9a227;outline:6px double #c9a227;outline-offset:-14px;box-shadow:0 24px 60px rgba(0,0,0,.15)}.hr4 .ico{font-size:50px;color:#c9a227;margin-bottom:6px}.hr4 .blessing{font-style:italic;color:#7a4f2b;font-size:14px;line-height:1.7;margin:14px 30px;white-space:pre-line}.hr4 .parents{font-size:13px;color:#5d4037;margin:6px 0;font-style:italic}.hr4 h1{font-size:48px;margin:14px 0 6px;color:#7a4f2b;font-style:italic}.hr4 .weds{font-size:14px;color:#c9a227;letter-spacing:8px;margin:10px 0}.hr4 .msg{font-size:13px;font-style:italic;color:#666;margin:14px 30px}.hr4 .info{margin-top:18px;padding-top:14px;border-top:1px solid #c9a227;font-size:14px;line-height:1.8;color:#5d4037}.hr4 .info strong{color:#7a4f2b}",
     'html': '<div class="hr4"><div class="ico">🐘</div><div class="blessing">{{ blessing }}</div><div class="parents">{{ bride_parents }}<br>request the honour of your presence at the wedding of their beloved daughter</div><h1>{{ bride }}</h1><div class="weds">— W I T H —</div><h1>{{ groom }}</h1><div class="parents">son of {{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Hindu Royal Purple', 'religion': 'hindu',
     'desc': 'Regal purple & gold for grand Hindu celebrations.',
     'css': ".hr5{width:560px;margin:30px auto;padding:0;background:#fff;font-family:Georgia,serif;text-align:center;border:4px solid #4a148c;box-shadow:0 30px 70px rgba(74,20,140,.4)}.hr5 .top{background:linear-gradient(135deg,#4a148c,#6a1b9a);color:#f5c842;padding:30px 40px}.hr5 .ico{font-size:46px}.hr5 .blessing{font-style:italic;font-size:14px;color:#fff8e1;line-height:1.7;margin-top:10px;white-space:pre-line}.hr5 .body{padding:30px 40px;background:#fef9e7}.hr5 .parents{font-size:13px;color:#4a148c;margin:6px 0}.hr5 h1{font-size:46px;margin:14px 0 6px;color:#4a148c;font-style:italic}.hr5 .weds{font-size:16px;color:#c9a227;letter-spacing:6px;margin:10px 0;font-weight:bold}.hr5 .msg{font-size:13px;font-style:italic;color:#666;margin:14px 30px}.hr5 .info{margin-top:18px;padding-top:14px;border-top:1px solid #c9a227;font-size:14px;line-height:1.8;color:#5d4037}.hr5 .info strong{color:#4a148c}",
     'html': '<div class="hr5"><div class="top"><div class="ico">🕉 ✨ 🕉</div><div class="blessing">{{ blessing }}</div></div><div class="body"><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">~ WEDS ~</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div></div>'},

    # ============ MUSLIM (3 variants) ============
    {'title': 'Muslim Nikah Green', 'religion': 'muslim',
     'desc': 'Elegant Islamic Nikah invite in green & gold.',
     'css': ".mu1{width:560px;margin:30px auto;padding:0;background:#fff;font-family:Georgia,serif;text-align:center;border:4px solid #1b5e20;box-shadow:0 30px 70px rgba(27,94,32,.4)}.mu1 .top{background:linear-gradient(135deg,#1b5e20,#2e7d32);color:#f5c842;padding:30px 40px;border-bottom:3px solid #f5c842}.mu1 .ico{font-size:50px}.mu1 .small{font-size:11px;letter-spacing:6px;color:#f5c842;text-transform:uppercase;margin-top:6px}.mu1 .blessing{font-size:15px;color:#fff;line-height:1.8;margin-top:10px;font-style:italic;white-space:pre-line}.mu1 .body{padding:30px 40px;background:#f1f8e9}.mu1 .parents{font-size:13px;color:#1b5e20;margin:6px 0}.mu1 h1{font-size:46px;margin:14px 0 6px;color:#1b5e20;font-style:italic}.mu1 .weds{font-size:14px;color:#558b2f;letter-spacing:6px;margin:10px 0}.mu1 .msg{font-size:13px;font-style:italic;color:#666;margin:14px 30px}.mu1 .info{margin-top:18px;padding-top:14px;border-top:1px solid #558b2f;font-size:14px;line-height:1.8;color:#33691e}.mu1 .info strong{color:#1b5e20}",
     'html': '<div class="mu1"><div class="top"><div class="ico">☪ ✦ ☪</div><div class="small">NIKAH CEREMONY</div><div class="blessing">{{ blessing }}</div></div><div class="body"><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">— WITH —</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div></div>'},

    {'title': 'Muslim Royal Blue Gold', 'religion': 'muslim',
     'desc': 'Royal blue & gold Islamic wedding card.',
     'css': ".mu2{width:560px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#1a237e,#0d47a1);color:#f5c842;text-align:center;font-family:Georgia,serif;border:3px double #f5c842;box-shadow:0 30px 70px rgba(13,71,161,.4)}.mu2 .ico{font-size:50px}.mu2 .small{font-size:12px;letter-spacing:6px;color:#f5c842}.mu2 .blessing{font-size:15px;color:#fff;line-height:1.8;margin:14px 30px;font-style:italic;white-space:pre-line}.mu2 .parents{font-size:13px;color:#bbdefb;margin:6px 0}.mu2 h1{font-size:48px;margin:14px 0 6px;color:#fff;font-style:italic}.mu2 .weds{font-size:14px;color:#f5c842;letter-spacing:6px;margin:10px 0}.mu2 .msg{font-size:13px;font-style:italic;color:#bbdefb;margin:14px 30px}.mu2 .info{margin-top:18px;padding-top:14px;border-top:1px solid #f5c842;font-size:14px;line-height:1.8;color:#fff}.mu2 .info strong{color:#f5c842}",
     'html': '<div class="mu2"><div class="ico">🕌 ✨ 🌙</div><div class="small">YOU ARE INVITED</div><div class="blessing">{{ blessing }}</div><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">— &amp; —</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Muslim Cream Geometric', 'religion': 'muslim',
     'desc': 'Soft cream with Islamic geometric border.',
     'css': ".mu3{width:560px;margin:30px auto;padding:50px 40px;background:#fffaf0;color:#3e2723;text-align:center;font-family:Georgia,serif;border:6px double #2e7d32;box-shadow:0 24px 60px rgba(0,0,0,.15);position:relative}.mu3::before{content:'❋ ❋ ❋ ❋ ❋';display:block;color:#2e7d32;font-size:14px;letter-spacing:14px;margin-bottom:14px}.mu3::after{content:'❋ ❋ ❋ ❋ ❋';display:block;color:#2e7d32;font-size:14px;letter-spacing:14px;margin-top:14px}.mu3 .ico{font-size:40px;color:#2e7d32}.mu3 .blessing{font-size:14px;color:#1b5e20;line-height:1.8;margin:14px 30px;font-style:italic;white-space:pre-line}.mu3 .parents{font-size:13px;color:#5d4037;margin:6px 0}.mu3 h1{font-size:48px;margin:14px 0 6px;color:#1b5e20;font-style:italic}.mu3 .weds{font-size:14px;color:#558b2f;letter-spacing:6px;margin:10px 0}.mu3 .msg{font-size:13px;font-style:italic;color:#666;margin:14px 30px}.mu3 .info{margin-top:18px;padding-top:14px;border-top:1px solid #2e7d32;font-size:14px;line-height:1.8;color:#5d4037}.mu3 .info strong{color:#1b5e20}",
     'html': '<div class="mu3"><div class="ico">☪</div><div class="blessing">{{ blessing }}</div><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">— NIKAH —</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div>'},

    # ============ CHRISTIAN (3 variants) ============
    {'title': 'Christian Church White', 'religion': 'christian',
     'desc': 'Classic white church wedding with cross blessing.',
     'css': ".ch1{width:560px;margin:30px auto;padding:50px 40px;background:#fff;color:#37474f;text-align:center;font-family:Georgia,serif;border:1px solid #c9a227;outline:4px solid #fff;outline-offset:-12px;box-shadow:0 24px 60px rgba(0,0,0,.15)}.ch1 .ico{font-size:46px;color:#c9a227}.ch1 .small{font-size:11px;letter-spacing:6px;color:#c9a227;text-transform:uppercase;margin-top:6px}.ch1 .blessing{font-size:14px;color:#546e7a;line-height:1.8;margin:14px 30px;font-style:italic}.ch1 .parents{font-size:13px;color:#546e7a;margin:6px 0}.ch1 h1{font-size:48px;margin:14px 0 6px;color:#263238;font-style:italic}.ch1 .weds{font-size:14px;color:#c9a227;letter-spacing:6px;margin:10px 0;font-weight:bold}.ch1 .msg{font-size:13px;font-style:italic;color:#666;margin:14px 30px}.ch1 .info{margin-top:18px;padding-top:14px;border-top:1px solid #c9a227;font-size:14px;line-height:1.8;color:#37474f}.ch1 .info strong{color:#263238}",
     'html': '<div class="ch1"><div class="ico">✝</div><div class="small">HOLY MATRIMONY</div><div class="blessing">{{ blessing }}</div><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">— &amp; —</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Christian Floral Soft', 'religion': 'christian',
     'desc': 'Soft floral Christian wedding invite.',
     'css': ".ch2{width:560px;margin:30px auto;padding:50px 40px;background:#fff8f0;color:#5d4037;text-align:center;font-family:Georgia,serif;border:3px solid #d7ccc8;box-shadow:0 24px 60px rgba(0,0,0,.1)}.ch2::before{content:'❀ ✝ ❀';display:block;font-size:20px;color:#a1887f;letter-spacing:6px;margin-bottom:14px}.ch2 .ico{display:none}.ch2 .small{font-size:11px;letter-spacing:6px;color:#8d6e63;text-transform:uppercase}.ch2 .blessing{font-size:14px;color:#5d4037;line-height:1.8;margin:14px 30px;font-style:italic}.ch2 .parents{font-size:13px;color:#6d4c41;margin:6px 0}.ch2 h1{font-size:48px;margin:14px 0 6px;color:#4e342e;font-style:italic}.ch2 .weds{font-size:14px;color:#a1887f;letter-spacing:6px;margin:10px 0}.ch2 .msg{font-size:13px;font-style:italic;color:#8d6e63;margin:14px 30px}.ch2 .info{margin-top:18px;padding-top:14px;border-top:1px solid #d7ccc8;font-size:14px;line-height:1.8;color:#5d4037}.ch2 .info strong{color:#4e342e}",
     'html': '<div class="ch2"><div class="small">WE INVITE YOU</div><div class="blessing">{{ blessing }}</div><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">— TO WED —</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Christian Gold Classic', 'religion': 'christian',
     'desc': 'Classic ivory & gold Christian wedding card.',
     'css': ".ch3{width:560px;margin:30px auto;padding:0;background:#fff;font-family:Georgia,serif;text-align:center;border:4px solid #c9a227}.ch3 .top{background:#c9a227;color:#fff;padding:24px;border-bottom:4px solid #fff}.ch3 .ico{font-size:36px}.ch3 .small{font-size:12px;letter-spacing:6px;margin-top:6px}.ch3 .body{padding:30px 40px;background:#fffaf0}.ch3 .blessing{font-size:14px;color:#5d4037;line-height:1.8;margin:14px 30px;font-style:italic}.ch3 .parents{font-size:13px;color:#7a4f2b;margin:6px 0}.ch3 h1{font-size:46px;margin:14px 0 6px;color:#7a4f2b;font-style:italic}.ch3 .weds{font-size:14px;color:#c9a227;letter-spacing:6px;margin:10px 0;font-weight:bold}.ch3 .msg{font-size:13px;font-style:italic;color:#666;margin:14px 30px}.ch3 .info{margin-top:18px;padding-top:14px;border-top:1px solid #c9a227;font-size:14px;line-height:1.8;color:#5d4037}.ch3 .info strong{color:#7a4f2b}",
     'html': '<div class="ch3"><div class="top"><div class="ico">⛪ ✝ ⛪</div><div class="small">JOIN US IN CELEBRATION</div></div><div class="body"><div class="blessing">{{ blessing }}</div><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">— &amp; —</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div></div>'},

    # ============ SIKH (2 variants) ============
    {'title': 'Sikh Anand Karaj Saffron', 'religion': 'sikh',
     'desc': 'Traditional Sikh Anand Karaj in saffron & navy.',
     'css': ".sk1{width:560px;margin:30px auto;padding:0;background:#fff;font-family:Georgia,serif;text-align:center;border:6px solid #1a237e;box-shadow:0 30px 70px rgba(26,35,126,.4)}.sk1 .top{background:linear-gradient(135deg,#ff6f00,#ff8f00);color:#1a237e;padding:30px 40px;border-bottom:4px solid #1a237e}.sk1 .ico{font-size:50px}.sk1 .small{font-size:11px;letter-spacing:6px;color:#1a237e;text-transform:uppercase;margin-top:6px;font-weight:bold}.sk1 .blessing{font-size:15px;color:#1a237e;line-height:1.8;margin-top:10px;font-style:italic;white-space:pre-line;font-weight:bold}.sk1 .body{padding:30px 40px;background:#fff8e1}.sk1 .parents{font-size:13px;color:#bf360c;margin:6px 0;font-weight:bold}.sk1 h1{font-size:46px;margin:14px 0 6px;color:#1a237e;font-style:italic}.sk1 .weds{font-size:16px;color:#bf360c;letter-spacing:6px;margin:10px 0;font-weight:bold}.sk1 .msg{font-size:13px;font-style:italic;color:#666;margin:14px 30px}.sk1 .info{margin-top:18px;padding-top:14px;border-top:2px solid #1a237e;font-size:14px;line-height:1.8;color:#5d4037}.sk1 .info strong{color:#1a237e}",
     'html': '<div class="sk1"><div class="top"><div class="ico">☬ ✦ ☬</div><div class="small">ANAND KARAJ</div><div class="blessing">{{ blessing }}</div></div><div class="body"><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">~ WEDS ~</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div></div>'},

    {'title': 'Sikh Royal Maroon Khanda', 'religion': 'sikh',
     'desc': 'Royal maroon Sikh wedding with Khanda symbol.',
     'css': ".sk2{width:560px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#7a0019,#b71c1c);color:#fff8e1;text-align:center;font-family:Georgia,serif;border:3px double #f5c842;box-shadow:0 30px 70px rgba(122,0,25,.4)}.sk2 .ico{font-size:50px;color:#f5c842}.sk2 .small{font-size:11px;letter-spacing:6px;color:#f5c842;text-transform:uppercase;font-weight:bold}.sk2 .blessing{font-size:15px;color:#fff;line-height:1.8;margin:14px 30px;font-style:italic;white-space:pre-line}.sk2 .parents{font-size:13px;color:#fff8e1;margin:6px 0}.sk2 h1{font-size:48px;margin:14px 0 6px;color:#fff;font-style:italic}.sk2 .weds{font-size:14px;color:#f5c842;letter-spacing:6px;margin:10px 0;font-weight:bold}.sk2 .msg{font-size:13px;font-style:italic;color:#fff8e1;margin:14px 30px}.sk2 .info{margin-top:18px;padding-top:14px;border-top:1px solid #f5c842;font-size:14px;line-height:1.8;color:#fff}.sk2 .info strong{color:#f5c842}",
     'html': '<div class="sk2"><div class="ico">☬</div><div class="small">ANAND KARAJ CEREMONY</div><div class="blessing">{{ blessing }}</div><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">— &amp; —</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div>'},

    # ============ REGIONAL (2 variants) ============
    {'title': 'South Indian Temple', 'religion': 'south',
     'desc': 'Tamil/Telugu temple-style wedding invitation.',
     'css': ".so1{width:560px;margin:30px auto;padding:0;background:#fff;font-family:Georgia,serif;text-align:center;border:6px solid #c62828;box-shadow:0 30px 70px rgba(198,40,40,.4)}.so1 .top{background:linear-gradient(135deg,#fff8e1,#ffe0b2);color:#bf360c;padding:30px 40px;border-bottom:4px solid #c62828}.so1 .ico{font-size:46px}.so1 .small{font-size:11px;letter-spacing:6px;color:#c62828;text-transform:uppercase;font-weight:bold}.so1 .blessing{font-size:14px;color:#bf360c;line-height:1.8;margin-top:10px;font-style:italic;white-space:pre-line;font-weight:bold}.so1 .body{padding:30px 40px;background:#fffaf0}.so1 .parents{font-size:13px;color:#5d4037;margin:6px 0;font-style:italic}.so1 h1{font-size:46px;margin:14px 0 6px;color:#bf360c;font-style:italic}.so1 .weds{font-size:14px;color:#c62828;letter-spacing:6px;margin:10px 0;font-weight:bold}.so1 .msg{font-size:13px;font-style:italic;color:#666;margin:14px 30px}.so1 .info{margin-top:18px;padding-top:14px;border-top:2px solid #c62828;font-size:14px;line-height:1.8;color:#5d4037}.so1 .info strong{color:#bf360c}",
     'html': '<div class="so1"><div class="top"><div class="ico">🛕 🪔 🛕</div><div class="small">SUBHA VIVAHA</div><div class="blessing">{{ blessing }}</div></div><div class="body"><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">~ WEDS ~</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div></div>'},

    # ===== PAKISTANI / MUSLIM PREMIUM (matched to user reference images) =====
    {'title': 'Pakistani Royal Arch Bismillah', 'religion': 'pakistani',
     'desc': 'Cream & gold Pakistani wedding card with Bismillah, arch frame, couple illustration & florals.',
     'css': ".pak1{width:560px;margin:30px auto;padding:0;background:linear-gradient(180deg,#fdf6e3 0%,#f5e6c8 100%);font-family:'Cormorant Garamond',Georgia,serif;text-align:center;color:#4a3520;border:1px solid #c9a227;position:relative;box-shadow:0 30px 70px rgba(74,53,32,.3);overflow:hidden}.pak1::before{content:'';position:absolute;inset:0;background-image:radial-gradient(circle at 30% 30%,rgba(201,162,39,.08) 1px,transparent 1px),radial-gradient(circle at 70% 70%,rgba(201,162,39,.08) 1px,transparent 1px);background-size:24px 24px;pointer-events:none}.pak1 .arch{padding:30px 40px 20px;border-bottom:2px solid #c9a227;background:#fffaf0;position:relative;border-radius:0 0 200px 200px / 0 0 50px 50px;margin:0 30px}.pak1 .arch::before{content:'';position:absolute;top:6px;left:6px;right:6px;bottom:0;border:1px solid #c9a227;border-radius:0 0 200px 200px / 0 0 45px 45px;border-top:none}.pak1 .arabic{font-family:'Amiri','Scheherazade New','Traditional Arabic',serif;font-size:28px;color:#7a4f1d;line-height:1.6;letter-spacing:1px;direction:rtl;margin:8px 0;position:relative}.pak1 .body{padding:24px 50px 20px;position:relative}.pak1 .small{font-style:italic;color:#8a6d3b;font-size:14px;margin:8px 0}.pak1 h1{font-size:42px;color:#5d3a0e;margin:6px 0;font-weight:500;line-height:1.1}.pak1 .amp{font-size:36px;color:#c9a227;font-style:italic;margin:4px 0;font-family:'Playfair Display',Georgia,serif}.pak1 .invite{font-style:italic;color:#7a6a4a;font-size:13px;margin:14px 30px;line-height:1.5}.pak1 .date-row{display:flex;justify-content:center;align-items:center;gap:24px;margin:18px 0 8px}.pak1 .date-row .col{text-align:center;font-size:11px;letter-spacing:3px;color:#7a4f1d;text-transform:uppercase}.pak1 .date-row .num{font-size:46px;color:#5d3a0e;font-weight:600;line-height:1;font-family:'Playfair Display',Georgia,serif}.pak1 .year{font-size:30px;color:#5d3a0e;margin:8px 0;font-weight:500;font-family:'Playfair Display',serif}.pak1 .at{font-style:italic;color:#8a6d3b;font-size:14px;margin:6px 0}.pak1 .venue{font-size:15px;color:#5d3a0e;font-weight:500;margin:10px 30px;line-height:1.6;font-style:italic}.pak1 .couple-ill{position:absolute;bottom:20px;left:14px;font-size:54px;line-height:1}.pak1 .florals-l{position:absolute;top:50%;left:0;transform:translateY(-50%);font-size:30px;line-height:1.6;color:#c9a227;opacity:.85}.pak1 .florals-r{position:absolute;top:50%;right:0;transform:translateY(-50%);font-size:30px;line-height:1.6;text-align:right}.pak1 .rsvp-brush{margin:14px auto 20px;background:linear-gradient(90deg,#5a8a3a,#7a9d4a);color:#fff;display:inline-block;padding:8px 36px;letter-spacing:6px;font-size:13px;transform:rotate(-2deg);border-radius:4px;font-family:Inter,sans-serif;font-weight:600}.pak1 .lotus{position:absolute;bottom:6px;right:14px;font-size:30px}",
     'html': '<div class="pak1"><div class="florals-l">🌿<br>🌸<br>🌿</div><div class="florals-r">🦚<br>🌸<br>🕊</div><div class="arch"><div class="arabic">بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ</div></div><div class="body"><div class="small">Together with their families</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="invite">{{ message }}</div><div class="date-row"><div class="col">December<br><div class="num"></div></div><div class="col"><div class="num">16</div></div><div class="col">At 8:00 PM<br><div class="num"></div></div></div><div class="year">2024</div><div class="at">at</div><div class="venue">{{ venue|linebreaksbr }}</div><div class="rsvp-brush">RSVP</div></div><div class="couple-ill">👰🏽‍♀️🤵🏽‍♂️</div><div class="lotus">🪷</div></div>'},

    {'title': 'Muslim Floral Samira Style', 'religion': 'samira',
     'desc': 'White & gold Muslim wedding card with Bismillah, floral corners & couple illustration.',
     'css': ".sam1{width:520px;margin:30px auto;padding:50px 40px;background:#fffaf3;font-family:'Cormorant Garamond',Georgia,serif;text-align:center;color:#3d2d18;position:relative;box-shadow:0 30px 70px rgba(0,0,0,.15);border:1px solid #e8d8b8;overflow:hidden}.sam1::before{content:'';position:absolute;top:30px;left:30px;right:30px;bottom:30px;border:1px solid #c9a227;pointer-events:none}.sam1 .floral-tl{position:absolute;top:8px;left:8px;font-size:46px;line-height:1;color:#d97560;transform:rotate(-15deg)}.sam1 .floral-br{position:absolute;bottom:8px;right:8px;font-size:46px;line-height:1;color:#d97560;transform:rotate(165deg)}.sam1 .leaves-tr{position:absolute;top:14px;right:30px;font-size:30px;line-height:1.4;color:#7a9d4a;text-align:right}.sam1 .leaves-bl{position:absolute;bottom:14px;left:30px;font-size:30px;line-height:1.4;color:#7a9d4a}.sam1 .content{position:relative;padding:24px 20px;z-index:2}.sam1 .arabic{font-family:'Amiri','Scheherazade New','Traditional Arabic',serif;font-size:26px;color:#7a4f1d;line-height:1.6;direction:rtl;margin:8px 0 6px}.sam1 .bismillah-en{font-size:11px;color:#7a4f1d;letter-spacing:3px;text-transform:uppercase;margin:6px 0 18px;font-family:Inter,sans-serif}.sam1 .label{font-size:11px;letter-spacing:5px;color:#7a4f1d;text-transform:uppercase;margin:4px 0 10px;font-family:Inter,sans-serif}.sam1 .names{font-family:'Great Vibes','Allura',cursive;font-size:48px;color:#5d3a0e;margin:14px 0;line-height:1;font-style:italic}.sam1 .invite{font-size:11px;letter-spacing:3px;color:#7a4f1d;text-transform:uppercase;margin:14px 0 8px;font-family:Inter,sans-serif}.sam1 .date-row{display:flex;justify-content:center;align-items:center;gap:18px;margin:14px 0;padding:12px 0;border-top:1px solid #c9a227;border-bottom:1px solid #c9a227}.sam1 .col{text-align:center;color:#5d3a0e;font-family:Inter,sans-serif}.sam1 .col .lbl{font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#7a4f1d}.sam1 .col .big{font-size:42px;font-weight:300;font-family:'Playfair Display',serif;color:#5d3a0e;line-height:1}.sam1 .year{font-size:24px;font-family:'Playfair Display',serif;color:#5d3a0e;margin:6px 0 14px}.sam1 .venue{font-size:11px;letter-spacing:2px;color:#5d3a0e;text-transform:uppercase;line-height:1.7;font-family:Inter,sans-serif;margin:8px 0}.sam1 .reception{font-family:'Great Vibes','Allura',cursive;font-size:22px;color:#7a4f1d;margin-top:8px;font-style:italic}.sam1 .couple-ill{position:absolute;bottom:40px;right:50px;font-size:50px;line-height:1}",
     'html': '<div class="sam1"><div class="floral-tl">🌹🌸</div><div class="leaves-tr">🌿</div><div class="leaves-bl">🌿</div><div class="floral-br">🌹🌸</div><div class="content"><div class="arabic">بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ</div><div class="bismillah-en">In the Name of Allah,<br>The Most Gracious, The Most Merciful</div><div class="label">Together with their families</div><div class="names">{{ bride }} &amp; {{ groom }}</div><div class="invite">Invite you to join their<br>wedding celebration on</div><div class="date-row"><div class="col"><div class="lbl">Friday</div></div><div class="col"><div class="lbl">June</div><div class="big">07</div></div><div class="col"><div class="lbl">At 12 PM</div></div></div><div class="year">2024</div><div class="venue">{{ venue|linebreaksbr }}</div><div class="reception">Reception to follow</div></div><div class="couple-ill">👰🏽‍♀️🤵🏽‍♂️</div></div>'},

    {'title': 'Gujarati Multi-Ceremony Arch', 'religion': 'gujarati', 'multi': True,
     'desc': 'Traditional Gujarati arch-frame invite with multiple ceremonies, lanterns, Ganesh & peacocks.',
     'css': ".gj1{width:560px;margin:30px auto;padding:0 0 30px;background:linear-gradient(180deg,#fff5e6 0%,#fff8ed 100%);font-family:Georgia,serif;text-align:center;color:#5d4037;border:1px solid #e8c39e;border-radius:120px 120px 14px 14px;box-shadow:0 30px 70px rgba(212,131,69,.25);position:relative;overflow:hidden}.gj1 .lanterns{position:absolute;top:14px;left:0;right:0;display:flex;justify-content:space-between;padding:0 30px;font-size:34px;z-index:2;pointer-events:none}.gj1 .arch{padding:60px 40px 20px;border-radius:120px 120px 0 0;border:2px dashed #d48345;border-bottom:none;margin:14px 24px 0;background:#fffaf0;position:relative}.gj1 .ganesh{font-size:38px;color:#bf360c;line-height:1}.gj1 h1{font-size:46px;margin:10px 0 6px;color:#bf360c;font-style:italic;font-weight:bold}.gj1 .sub{font-size:13px;color:#6d4c41;font-style:italic;margin:6px 20px}.gj1 .parents{font-size:12px;color:#5d4037;margin:14px 0 4px;font-weight:600}.gj1 .couple{font-size:38px;font-style:italic;color:#c62828;margin:6px 0;font-weight:bold;font-family:'Playfair Display',Georgia,serif}.gj1 .ceremonies{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;padding:20px 30px 14px}.gj1 .cer{font-size:11px;color:#5d4037;line-height:1.6}.gj1 .cer .nm{color:#bf360c;font-weight:bold;font-size:13px;display:block;margin-bottom:4px}.gj1 .couple-img{font-size:46px;margin:6px 0}.gj1 .venue-block{padding:8px 30px;color:#bf360c;font-weight:bold;font-size:14px}.gj1 .venue-block .lbl{font-size:12px;color:#bf360c;font-weight:bold}.gj1 .invited{font-size:12px;color:#5d4037;margin-top:8px;font-style:italic}.gj1 .peacocks{display:flex;justify-content:space-between;padding:14px 24px 0;font-size:34px}",
     'html': '<div class="gj1"><div class="lanterns"><span>🪔</span><span>🪔</span></div><div class="arch"><div class="ganesh">🕉</div><h1>{{ blessing }}</h1><div class="sub">"{{ subtext }}"</div><div class="parents">{{ groom_parents }}</div><div class="couple">{{ groom }} &amp; {{ bride }}</div><div class="parents">{{ bride_parents }}</div></div><div class="ceremonies">{% for c in ceremonies %}<div class="cer"><span class="nm">{{ c.name }}</span>{{ c.date }}<br>{{ c.time }}{% if c.venue %}<br>{{ c.venue }}{% endif %}</div>{% endfor %}</div><div class="couple-img">👰🏽‍♀️ 🤵🏽‍♂️</div><div class="venue-block"><span class="lbl">લગ્ન સ્થળ</span><br>{{ venue }}<div class="invited">{{ invited_by }}</div></div><div class="peacocks"><span>🦚</span><span>🦚</span></div></div>'},

    # ===== CEREMONY-SPECIFIC CARDS =====
    {'title': 'Mehendi Ceremony Floral', 'religion': 'mehendi',
     'desc': 'Henna green & gold mehendi ceremony invitation.',
     'css': ".mh1{width:560px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#1b5e20,#2e7d32);color:#fff8e1;text-align:center;font-family:Georgia,serif;border:4px solid #f5c842;border-radius:14px;box-shadow:0 30px 70px rgba(27,94,32,.4)}.mh1 .ico{font-size:54px}.mh1 .label{font-size:11px;letter-spacing:6px;color:#f5c842;text-transform:uppercase;font-weight:bold}.mh1 .blessing{font-size:18px;color:#f5c842;margin:14px 0;font-style:italic}.mh1 h1{font-size:48px;margin:14px 0 6px;font-style:italic;color:#fff}.mh1 .amp{font-size:32px;color:#f5c842;margin:6px 0}.mh1 .msg{font-size:14px;color:#fff8e1;line-height:1.7;margin:14px 30px;font-style:italic}.mh1 .info{margin-top:18px;padding-top:14px;border-top:1px solid #f5c842;font-size:14px;line-height:1.8}.mh1 .info strong{color:#f5c842;display:block}",
     'html': '<div class="mh1"><div class="ico">🌿 🪷 🌿</div><div class="label">MEHENDI CEREMONY</div><div class="blessing">{{ blessing }}</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Sangeet Night Glam', 'religion': 'sangeet',
     'desc': 'Glittery purple Sangeet ceremony card.',
     'css': ".sg1{width:560px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#4a148c,#7b1fa2);color:#fff;text-align:center;font-family:Georgia,serif;border:3px double #f5c842;border-radius:14px;box-shadow:0 30px 70px rgba(74,20,140,.5)}.sg1 .ico{font-size:54px}.sg1 .label{font-size:11px;letter-spacing:6px;color:#f5c842;text-transform:uppercase}.sg1 .blessing{font-size:20px;color:#f5c842;margin:14px 0;font-style:italic}.sg1 h1{font-size:48px;margin:14px 0 6px;font-style:italic;color:#fff}.sg1 .amp{font-size:32px;color:#f5c842;margin:6px 0}.sg1 .msg{font-size:14px;color:#e1bee7;line-height:1.7;margin:14px 30px;font-style:italic}.sg1 .info{margin-top:18px;padding-top:14px;border-top:1px solid #f5c842;font-size:14px;line-height:1.8}.sg1 .info strong{color:#f5c842;display:block}",
     'html': '<div class="sg1"><div class="ico">💃 🪘 🎶</div><div class="label">SANGEET NIGHT</div><div class="blessing">{{ blessing }}</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Haldi Ceremony Sunshine', 'religion': 'haldi',
     'desc': 'Bright yellow Haldi ceremony card.',
     'css': ".hl1{width:560px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#fff176,#fdd835);color:#5d4037;text-align:center;font-family:Georgia,serif;border:6px solid #f57f17;border-radius:14px;box-shadow:0 30px 70px rgba(245,127,23,.4)}.hl1 .ico{font-size:54px}.hl1 .label{font-size:11px;letter-spacing:6px;color:#bf360c;text-transform:uppercase;font-weight:bold}.hl1 .blessing{font-size:18px;color:#bf360c;margin:14px 0;font-style:italic}.hl1 h1{font-size:48px;margin:14px 0 6px;font-style:italic;color:#bf360c}.hl1 .amp{font-size:32px;color:#f57f17;margin:6px 0}.hl1 .msg{font-size:14px;color:#5d4037;line-height:1.7;margin:14px 30px;font-style:italic}.hl1 .info{margin-top:18px;padding-top:14px;border-top:2px solid #f57f17;font-size:14px;line-height:1.8;color:#5d4037}.hl1 .info strong{color:#bf360c;display:block}",
     'html': '<div class="hl1"><div class="ico">🌼 ✨ 🌼</div><div class="label">HALDI CEREMONY</div><div class="blessing">{{ blessing }}</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>Dress code: Yellow!<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Baraat Procession Royal', 'religion': 'baraat',
     'desc': 'Royal red & gold baraat procession card.',
     'css': ".br1{width:560px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#b71c1c,#7f0000);color:#fff;text-align:center;font-family:Georgia,serif;border:4px double #f5c842;border-radius:14px;box-shadow:0 30px 70px rgba(183,28,28,.4)}.br1 .ico{font-size:54px;color:#f5c842}.br1 .label{font-size:11px;letter-spacing:6px;color:#f5c842;text-transform:uppercase;font-weight:bold}.br1 .blessing{font-size:18px;color:#f5c842;margin:14px 0;font-style:italic}.br1 h1{font-size:48px;margin:14px 0 6px;font-style:italic;color:#fff}.br1 .amp{font-size:32px;color:#f5c842;margin:6px 0}.br1 .msg{font-size:14px;color:#fff8e1;line-height:1.7;margin:14px 30px;font-style:italic}.br1 .info{margin-top:18px;padding-top:14px;border-top:1px solid #f5c842;font-size:14px;line-height:1.8}.br1 .info strong{color:#f5c842;display:block}",
     'html': '<div class="br1"><div class="ico">🐎 🪘 🎉</div><div class="label">BARAAT PROCESSION</div><div class="blessing">{{ blessing }}</div><h1>{{ bride }}</h1><div class="amp">&amp;</div><h1>{{ groom }}</h1><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div>'},

    # ===== REGIONAL INDIAN WEDDINGS =====
    {'title': 'Tamil Wedding Temple', 'religion': 'tamil',
     'desc': 'Traditional Tamil wedding card with temple motifs and Tamil script.',
     'css': ".tm1{width:560px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#fff8e1,#ffe0b2);color:#bf360c;text-align:center;font-family:Georgia,serif;border:8px solid #c62828;border-radius:14px;box-shadow:0 30px 70px rgba(198,40,40,.4)}.tm1 .ico{font-size:50px;color:#bf360c}.tm1 .label{font-size:11px;letter-spacing:6px;color:#bf360c;text-transform:uppercase;font-weight:bold}.tm1 .blessing{font-size:16px;color:#bf360c;margin:14px 0;font-style:italic;font-weight:bold;line-height:1.6}.tm1 h1{font-size:46px;margin:14px 0 6px;color:#bf360c;font-style:italic}.tm1 .amp{font-size:30px;color:#c62828;margin:6px 0}.tm1 .parents{font-size:13px;color:#5d4037;margin:6px 0;font-style:italic}.tm1 .msg{font-size:14px;color:#5d4037;line-height:1.7;margin:14px 30px;font-style:italic}.tm1 .info{margin-top:18px;padding-top:14px;border-top:2px solid #c62828;font-size:14px;line-height:1.8;color:#5d4037}.tm1 .info strong{color:#bf360c;display:block}",
     'html': '<div class="tm1"><div class="ico">🛕 🪔 🛕</div><div class="label">SUBHA VIVAHAM</div><div class="blessing">{{ blessing }}</div><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="amp">~ WEDS ~</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Telugu Wedding Tirupati', 'religion': 'telugu',
     'desc': 'Telugu wedding card with Tirupati blessings.',
     'css': ".te1{width:560px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#f5c842,#ff8f00);color:#5d4037;text-align:center;font-family:Georgia,serif;border:6px solid #c62828;border-radius:14px;box-shadow:0 30px 70px rgba(255,143,0,.4)}.te1 .ico{font-size:50px;color:#bf360c}.te1 .label{font-size:11px;letter-spacing:6px;color:#bf360c;text-transform:uppercase;font-weight:bold}.te1 .blessing{font-size:16px;color:#bf360c;margin:14px 0;font-style:italic;font-weight:bold;line-height:1.6}.te1 h1{font-size:46px;margin:14px 0 6px;color:#bf360c;font-style:italic}.te1 .amp{font-size:30px;color:#c62828;margin:6px 0}.te1 .parents{font-size:13px;color:#5d4037;margin:6px 0;font-style:italic}.te1 .msg{font-size:14px;color:#3e2723;line-height:1.7;margin:14px 30px;font-style:italic}.te1 .info{margin-top:18px;padding-top:14px;border-top:2px solid #bf360c;font-size:14px;line-height:1.8}.te1 .info strong{color:#bf360c;display:block}",
     'html': '<div class="te1"><div class="ico">🛕 🪷 🛕</div><div class="label">VIVAHA SHUBHAKANKSHALU</div><div class="blessing">{{ blessing }}</div><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="amp">~ WEDS ~</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Marathi Wedding Saraswati', 'religion': 'marathi',
     'desc': 'Traditional Marathi wedding with Devanagari script.',
     'css': ".ma1{width:560px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#fff8e1,#ffecb3);color:#bf360c;text-align:center;font-family:Georgia,serif;border:6px solid #c62828;border-radius:14px;box-shadow:0 30px 70px rgba(198,40,40,.4)}.ma1 .ico{font-size:50px;color:#bf360c}.ma1 .label{font-size:11px;letter-spacing:6px;color:#bf360c;text-transform:uppercase;font-weight:bold}.ma1 .blessing{font-size:16px;color:#bf360c;margin:14px 0;font-style:italic;font-weight:bold;line-height:1.6;white-space:pre-line}.ma1 h1{font-size:46px;margin:14px 0 6px;color:#bf360c;font-style:italic}.ma1 .amp{font-size:30px;color:#c62828;margin:6px 0}.ma1 .parents{font-size:13px;color:#5d4037;margin:6px 0;font-style:italic}.ma1 .msg{font-size:14px;color:#5d4037;line-height:1.7;margin:14px 30px;font-style:italic}.ma1 .info{margin-top:18px;padding-top:14px;border-top:2px solid #c62828;font-size:14px;line-height:1.8;color:#5d4037}.ma1 .info strong{color:#bf360c;display:block}",
     'html': '<div class="ma1"><div class="ico">🛕 🪔 🛕</div><div class="label">SHUBH VIVAH</div><div class="blessing">{{ blessing }}</div><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="amp">~ ANI ~</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Punjabi Anand Karaj', 'religion': 'punjabi',
     'desc': 'Royal Punjabi Anand Karaj wedding card.',
     'css': ".pn1{width:560px;margin:30px auto;padding:50px 40px;background:linear-gradient(135deg,#bf360c,#c62828);color:#fff;text-align:center;font-family:Georgia,serif;border:4px double #f5c842;border-radius:14px;box-shadow:0 30px 70px rgba(198,40,40,.4)}.pn1 .ico{font-size:54px;color:#f5c842}.pn1 .label{font-size:11px;letter-spacing:6px;color:#f5c842;text-transform:uppercase;font-weight:bold}.pn1 .blessing{font-size:16px;color:#f5c842;margin:14px 0;font-style:italic;font-weight:bold;line-height:1.6;white-space:pre-line}.pn1 h1{font-size:46px;margin:14px 0 6px;color:#fff;font-style:italic}.pn1 .amp{font-size:30px;color:#f5c842;margin:6px 0}.pn1 .parents{font-size:13px;color:#fff8e1;margin:6px 0}.pn1 .msg{font-size:14px;color:#fff8e1;line-height:1.7;margin:14px 30px;font-style:italic}.pn1 .info{margin-top:18px;padding-top:14px;border-top:1px solid #f5c842;font-size:14px;line-height:1.8;color:#fff}.pn1 .info strong{color:#f5c842;display:block}",
     'html': '<div class="pn1"><div class="ico">☬ ✦ ☬</div><div class="label">ANAND KARAJ</div><div class="blessing">{{ blessing }}</div><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="amp">~ WEDS ~</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div>'},

    {'title': 'Bengali Tradition Red', 'religion': 'bengali',
     'desc': 'Traditional Bengali wedding card with conch motif.',
     'css': ".be1{width:560px;margin:30px auto;padding:0;background:#fff;font-family:Georgia,serif;text-align:center;border:4px solid #b71c1c;box-shadow:0 30px 70px rgba(183,28,28,.4)}.be1 .top{background:linear-gradient(135deg,#b71c1c,#d32f2f);color:#fff8e1;padding:30px 40px;border-bottom:4px solid #f5c842}.be1 .ico{font-size:46px;color:#f5c842}.be1 .small{font-size:11px;letter-spacing:6px;color:#f5c842;text-transform:uppercase;margin-top:6px}.be1 .blessing{font-size:15px;color:#fff;line-height:1.8;margin-top:10px;font-style:italic;white-space:pre-line}.be1 .body{padding:30px 40px;background:#fff8e1}.be1 .parents{font-size:13px;color:#b71c1c;margin:6px 0}.be1 h1{font-size:46px;margin:14px 0 6px;color:#b71c1c;font-style:italic}.be1 .weds{font-size:14px;color:#bf360c;letter-spacing:6px;margin:10px 0;font-weight:bold}.be1 .msg{font-size:13px;font-style:italic;color:#666;margin:14px 30px}.be1 .info{margin-top:18px;padding-top:14px;border-top:2px solid #b71c1c;font-size:14px;line-height:1.8;color:#5d4037}.be1 .info strong{color:#b71c1c}",
     'html': '<div class="be1"><div class="top"><div class="ico">🐚 🌺 🐚</div><div class="small">SHUBHO BIBAHO</div><div class="blessing">{{ blessing }}</div></div><div class="body"><div class="parents">{{ bride_parents }}</div><h1>{{ bride }}</h1><div class="weds">~ WEDS ~</div><h1>{{ groom }}</h1><div class="parents">{{ groom_parents }}</div><div class="msg">{{ message }}</div><div class="info"><strong>{{ date }}</strong>{{ time }}<br>{{ venue|linebreaksbr }}<br>RSVP: {{ rsvp }}</div></div></div>'},
]
