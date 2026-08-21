ITSA Website

Official website for the Information Technology Students Association (ITSA), IT Department, PVG's College of Engineering & Technology, Pune.

A multi-page static site — dark, glassmorphism/cyberpunk aesthetic with neon cyan/purple accents, animated background particles, and glowing hover/click effects throughout.

Folder structure

itsa-site/


├── index.html 

Main landing page (Home, About, Events, Team overview)

├── style.css              

Shared styles for the entire site

├── script.js              

Shared behavior (particles, mobile nav, click-pulse)

├── generate.py          

Generates all team-*.html pages from roster data

├── team-web.html          

Web Team — full member list

├── team-tech.html        

Tech Team — full member list

├── team-events.html      

Event Management Team — full member list

├── team-social.html      

Social Media Team — full member list

├── team-ops.html        

Operations & PR Team — full member list

├── team-design.html      

Design & Production Team — full member list

├── team-finance.html      

Finance Team — full member list

└── portraits/             

Member photos (add your own .jpg/.png files here)

Every page shares the same style.css and script.js, so edits to either file apply site-wide.
