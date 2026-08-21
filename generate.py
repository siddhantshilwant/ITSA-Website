import os

BASE = os.path.dirname(os.path.abspath(__file__))

# Fill in a path (relative to the itsa-site folder) for anyone whose portrait
# you've added to the portraits/ folder. Leave a name out and their card will
# just keep the icon placeholder.
PHOTOS = {
    # Web Team
    "Harsh Baviskar": "portraits/Harsh Baviskar_Web Team.jpg",
    "Soham Kangale": "portraits/Soham_Kangle_Web_Head.png",
    "Bhagyashree Badgujar": "portraits/Bhagyashree Badgujar_TE.jpg",
    "Vedant Ghevade": "portraits/VedantGhevade_SY.jpg",
    "Akshay Jain": "portraits/Akshad Jain.png",
    "Pranjal Gupta": "portraits/Pranjal Gupta SY.jpg",
    "Shravan Chavan": "portraits/Shravan Chavan SY IT B.jpg",
    "Rishi Agrawal": "portraits/Risshi_SY.jpeg",
    "Anurag Patil": "portraits/Anurag.jpg",
    "Sanskar Dingare": "portraits/Sanskar Dingre SY.jpeg",
    "Tilak Nagikar": "portraits/Tilak-SY.jpg",

    # Tech Team
    "Aradhana Hingane": "portraits/AradhanaHingane_TechHead.png",
    "Bhakti Vankhade": "portraits/Bhakti Vankhade Tech_Core.png",
    "Snehal Narale": "portraits/Snehal-Narale_BE.png",
    "Vinod Mangate": "portraits/Vinod-TE.jpg",
    "Prasad Dabhade": "portraits/Prasad-TE.jpg",
    "Harshwardhan Pandit": "portraits/Harshvardhan pandit SybtechIT.png",
    "Siddhant Shilawant": "portraits/SiddhantShilwant_SY.jpg",

    # Event Management Team
    "Sanika Deokar": "portraits/Sanika Deokar event head.jpg",
    "Sakshi Rajmane": "portraits/sakshi_rajmane_event_head.png",
    "Shruti Rupnar": "portraits/Shruti Rupnar SY IT-B.jpg",
    "Prajakta Mahadik": "portraits/Prajakta Mahadik SY.jpg",
    "Atharava Gore": "portraits/Atharva_Gore_SYIT.jpg",
    "Gayatri Lonsane": "portraits/Gayatri_Lonsane_SY_.jpg",
    "Disha Shelke": "portraits/Disha Shelke S.Y Btech(Div B).jpg",
    "Viraj Malshikare": "portraits/Viraj.jpg",
    "Mansi Phalke": "portraits/Mansi Phalke S. Y Btech (A)_.jpg",
    "Hridaya Khare": "portraits/Hridaya Khare TE IT.jpg",
    "Bhumika Kalambe": "portraits/Bhumika Kalambe_SY.jpg",
    "Rutuja Chambare": "portraits/RutujaChambhareA.jpg",

    # Social Media Team
    "Riddhi Limje": "portraits/Riddhi Limje SY-A .jpg",
    "Avadhoot Jagtap": "portraits/Avadhoot Jagtap SY.JPG",
    "Naureen Mulla": "portraits/Naureen Mulla SY.jpg",
    "Samradnyee Gaikwad": "portraits/Samradnyee Gaikwad SY IT A.jpg",
    "Dyanashri Donde": "portraits/Dnyanashri TE.jpg",
    "Virendra Kakade": "portraits/SY IT A virendra kakade.png",
    # "Sujal Nanaware": "portraits/Sujal-Nanaware.jpg",  # add extension to the file first

    # Operations & PR Team
    "Aryan Dhamdhere": "portraits/Aryan Dhamdhere Ops and PR Head.png",
    "Tejas Shinde": "portraits/Tejas Shinde Ops & PR Core Member.jpg",
    "Nachiket Bedekar": "portraits/Nachiket Bedekar.jpg",
    "Om Muli": "portraits/Om Muli.png",
    "Sanika Mohite": "portraits/Sanika_Mohite_SY_A.png",
    "Sayali Talekar": "portraits/Sayali Talekar_TE.jpg",
    "Rutuja Burkule": "portraits/Rutuja Burkule SY_.png",
    "Darshika Atram": "portraits/Darshika_Atram_TE.jpg",

    # Design & Production Team
    "Aditya Kulkarni": "portraits/Aditya_Kulkarni_DesignCore.jpg",
    "Neevan Redkar": "portraits/Neevan Redkar DnP Core.jpeg",
    "Nidhi Patil": "portraits/Nidhi Patil S.Y Btech(B).jpg",

    # Finance Team
    "Harsh Navare": "portraits/Harsh_Navare_Finance_Head.jpg",
    "Raj Borade": "portraits/Raj Borade - Finance Head.jpg",
    "Sushrut Paygude": "portraits/Sushrut_Paygude_SY.jpg",
    "Devansh Agrawal": "portraits/Devansh Agrawal_SY.jpg",
    "Avanti Kannawar": "portraits/Avanti  Kannawar _SY.jpg",
    "Ayush": "portraits/Ayush S Janunkar SY.png",
}

TEAMS = [
    {
        "slug": "web",
        "name": "Web Team",
        "icon": "fa-code",
        "heads": ["Harsh Baviskar", "Soham Kangale"],
        "coheads": ["Hussain Patanwala"],
        "members": ["Bhagyashree Badgujar", "Vedant Ghevade", "Akshay Jain", "Pranjal Gupta",
                    "Pranav Joshi", "Shravan Chavan", "Madhura Kulkarni", "Rishi Agrawal",
                    "Anurag Patil", "Sanskar Dingare", "Tilak Nagikar"],
    },
    {
        "slug": "tech",
        "name": "Tech Team",
        "icon": "fa-microchip",
        "heads": ["Aradhana Hingane"],
        "coheads": ["Bhakti Vankhade"],
        "members": ["Snehal Narale", "Varad Gupta", "Vinod Mangate", "Prasad Dabhade",
                    "Aryan Rohada", "Omkar Malve", "Sumit Khodake", "Harshwardhan Pandit",
                    "Siddhant Shilawant"],
    },
    {
        "slug": "events",
        "name": "Event Management Team",
        "icon": "fa-calendar-days",
        "heads": ["Sanika Deokar", "Sakshi Rajmane"],
        "coheads": ["Vaibhav Bagul"],
        "members": ["Shruti Rupnar", "Prajakta Mahadik", "Atharava Gore", "Gayatri Lonsane",
                    "Disha Shelke", "Shravan Ganjare", "Viraj Malshikare", "Deep Lokhande",
                    "Dyaneshwar Khodake", "Mansi Phalke", "Hridaya Khare", "Sarvesh Gholap",
                    "Bhumika Kalambe", "Shreya Bhurse", "Tejaswini Mantode", "Rutuja Chambare"],
    },
    {
        "slug": "social",
        "name": "Social Media Team",
        "icon": "fa-hashtag",
        "heads": ["Prem Jagtap"],
        "coheads": ["Sujal Nanaware"],
        "members": ["Prithviraj Nikam", "Riddhi Limje", "Avadhoot Jagtap", "Naureen Mulla",
                    "Sandhya Godhade", "Samradnyee Gaikwad", "Dyanashri Donde", "Virendra Kakade"],
    },
    {
        "slug": "ops",
        "name": "Operations & PR Team",
        "icon": "fa-bullhorn",
        "heads": ["Aryan Dhamdhere"],
        "coheads": ["Tejas Shinde"],
        "members": ["Nachiket Bedekar", "Siddhi Jain", "Om Muli", "Monisha Gowda", "Ayusha Kale",
                    "Sham Patole", "Shardul Hawaldar", "Sanika Mohite", "Sayali Talekar",
                    "Rutuja Burkule", "Darshika Atram"],
    },
    {
        "slug": "design",
        "name": "Design & Production Team",
        "icon": "fa-palette",
        "heads": ["Rudraksha Shete"],
        "coheads": ["Aditya Kulkarni", "Neevan Redkar"],
        "members": ["Om Waghmare", "Nidhi Patil", "Dev Kulriya", "Soham Katkar", "Tanushree Kulkarni"],
    },
    {
        "slug": "finance",
        "name": "Finance Team",
        "icon": "fa-coins",
        "heads": ["Harsh Navare", "Raj Borade"],
        "coheads": [],
        "members": ["Vedant Ghevade", "Sushrut Paygude", "Devansh Agrawal", "Avanti Kannawar", "Ayush"],
    },
]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — ITSA</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link rel="stylesheet" href="style.css">
</head>
<body>

<canvas id="particle-canvas"></canvas>
<div class="ambient-glow glow-a"></div>
<div class="ambient-glow glow-b"></div>
<div class="ambient-glow glow-c"></div>

<header>
  <div class="nav-wrap">
    <a href="index.html" class="logo">
      <span class="logo-mark">IT</span>
      <span>ITSA</span>
    </a>

    <ul class="nav-links">
      <li><a href="index.html#home">Home</a></li>
      <li><a href="index.html#about">About</a></li>
      <li><a href="index.html#events">Events</a></li>
      <li><a href="index.html#team" class="active">Team</a></li>
    </ul>

    <button class="btn-join desktop-only">JOIN</button>

    <button class="burger" id="burger" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </button>
  </div>

  <nav class="mobile-nav" id="mobileNav">
    <a href="index.html#home">Home</a>
    <a href="index.html#about">About</a>
    <a href="index.html#events">Events</a>
    <a href="index.html#team">Team</a>
    <button class="btn-join" style="margin-top:14px;">JOIN</button>
  </nav>
</header>

<main>
  <div class="member-page-head">
    <a href="index.html#team" class="back-link"><i class="fa-solid fa-arrow-left"></i> BACK TO ALL TEAMS</a>
    <div class="member-team-icon"><i class="fa-solid {icon}"></i></div>
    <h1 style="font-size: clamp(1.8rem, 5vw, 2.8rem); font-weight: 700;">{name}</h1>
    <p style="margin-top: 12px; color: var(--mist); font-size: 0.98rem;">{count} core members</p>
  </div>

  <section class="member-section">
"""

TAIL = """
  </section>
</main>

<footer>
  &copy; <span class="year"></span> Information Technology Students Association — PVG's College of Engineering &amp; Technology, Pune
</footer>

<script src="script.js"></script>
</body>
</html>
"""


def member_card(name, role, photo=None):
    if photo:
        avatar = f'<img src="{photo}" alt="{name}">'
    else:
        avatar = '<i class="fa-solid fa-user"></i>'
    return f"""      <div class="member-card" tabindex="0">
        <div class="avatar-circle">{avatar}</div>
        <p class="member-role">{role}</p>
        <p class="member-name">{name}</p>
      </div>
"""


def build_team_page(team):
    total = len(team["heads"]) + len(team["coheads"]) + len(team["members"])
    html = HEAD.format(title=team["name"], icon=team["icon"], name=team["name"].upper(), count=total)

    head_label = "HEAD" if len(team["heads"]) == 1 else "HEAD"
    html += f'    <p class="member-subhead">// {head_label}{"S" if len(team["heads"]) > 1 else ""}</p>\n'
    html += '    <div class="member-grid">\n'
    for n in team["heads"]:
        html += member_card(n, "HEAD", PHOTOS.get(n))
    html += '    </div>\n'

    if team["coheads"]:
        cohead_label = "CO-HEAD" + ("S" if len(team["coheads"]) > 1 else "")
        html += f'    <p class="member-subhead">// {cohead_label}</p>\n'
        html += '    <div class="member-grid">\n'
        for n in team["coheads"]:
            html += member_card(n, "CO-HEAD", PHOTOS.get(n))
        html += '    </div>\n'

    html += '    <p class="member-subhead">// MEMBERS</p>\n'
    html += '    <div class="member-grid">\n'
    for n in team["members"]:
        html += member_card(n, "MEMBER", PHOTOS.get(n))
    html += '    </div>\n'

    html += TAIL
    return html


for team in TEAMS:
    page = build_team_page(team)
    path = os.path.join(BASE, f"team-{team['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)
    print("wrote", path)
