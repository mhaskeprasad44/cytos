# -*- coding: utf-8 -*-
"""
scripts/generate_spm_blogs.py
Builds and integrates 5 new Special Purpose Machine (SPM) blogs for CyTOS Pune into:
1. src/data/allBlogsHtml.js
2. src/data/blogData.js
3. src/pages/BlogListingPage.jsx
4. src/pages/BlogIndexPage.jsx
5. public/sitemap.xml
"""

import os
import json
import re
from spm_blog_definitions import SPM_BLOGS

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
DATA_DIR = os.path.join(SRC, "data")
PAGES_DIR = os.path.join(SRC, "pages")
PUBLIC_DIR = os.path.join(ROOT, "public")

print(f"Generating 5 SPM blogs in {ROOT}...")

# 1. Read allBlogsHtml.js to extract templates
ALL_BLOGS_HTML_PATH = os.path.join(DATA_DIR, "allBlogsHtml.js")
with open(ALL_BLOGS_HTML_PATH, "r", encoding="utf-8") as f:
    all_blogs_txt = f.read()

# Extract top navigation and master footer templates from an existing blog
sample_pos = all_blogs_txt.find('"special-purpose-machines-spm-guide":')
sample_pos2 = all_blogs_txt.find('"vertical-drilling-and-milling-machine-guide":', sample_pos)
sample_chunk = all_blogs_txt[sample_pos:sample_pos2]

html_start = sample_chunk.find('"html": "') + len('"html": "')
bc_start = sample_chunk.find('<!-- Breadcrumbs -->')
footer_start = sample_chunk.find('<!-- Master Footer -->')

TOP_NAV = sample_chunk[html_start:bc_start]

# Footer extraction: must end at the end of the HTML string (before the closing quote)
tail = sample_chunk[footer_start:]
q_pos = tail.rfind('"\n  },\n')
if q_pos == -1:
    q_pos = tail.rfind('"\n  }')
if q_pos != -1:
    FOOTER_AND_SCRIPTS = tail[:q_pos]
else:
    raise ValueError("Could not find terminating quote of sample blog HTML!")

print(f"Extracted TOP_NAV ({len(TOP_NAV)} chars) and FOOTER ({len(FOOTER_AND_SCRIPTS)} chars).")
print(f"FOOTER tail: {repr(FOOTER_AND_SCRIPTS[-40:])}")

def build_article_html(blog):
    slug = blog["slug"]
    title = blog["title"]
    date = blog["date"]
    read_time = blog["readTime"]
    image = blog["image"]
    alt_text = blog["altText"]
    aeo_answer = blog["aeoAnswer"]
    machine_name = blog["machineName"]
    whatsapp_text = blog["whatsappText"]
    encoded_wa = re.sub(r'\s+', '%20', whatsapp_text).replace('&', '%26')

    # Breadcrumbs & Hero
    header_html = f"""<!-- Breadcrumbs -->\\r\\n  <div class=\\"breadcrumbs-bar\\">\\r\\n    <div class=\\"container\\">\\r\\n      <ul class=\\"breadcrumbs-list\\">\\r\\n        <li><a href=\\"/\\">Home</a></li>\\r\\n        <li><span class=\\"bc-sep\\">/</span></li>\\r\\n        <li><a href=\\"/blog\\">Engineering Blog</a></li>\\r\\n        <li><span class=\\"bc-sep\\">/</span></li>\\r\\n        <li><span class=\\"current\\">{title}</span></li>\\r\\n      </ul>\\r\\n    </div>\\r\\n  </div>\\r\\n\\r\\n  <!-- Blog Article Hero -->\\r\\n  <header class=\\"blog-article-hero\\">\\r\\n    <div class=\\"container\\">\\r\\n      <div class=\\"badge-accent\\">\\r\\n        <span class=\\"badge-dot\\"></span>\\r\\n        <span>SPM &amp; Automation • Peer-Reviewed Engineering Guide</span>\\r\\n      </div>\\r\\n      <h1 class=\\"blog-article-title\\">{title}</h1>\\r\\n      <div class=\\"blog-article-meta\\">\\r\\n        <div class=\\"blog-article-meta-item\\">\\r\\n          <svg viewBox=\\"0 0 24 24\\" width=\\"16\\" height=\\"16\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"2\\"><circle cx=\\"12\\" cy=\\"12\\" r=\\"10\\"></circle><polyline points=\\"12 6 12 12 16 14\\"></polyline></svg>\\r\\n          <span>Published: {date}</span>\\r\\n        </div>\\r\\n        <div class=\\"blog-article-meta-item\\">\\r\\n          <svg viewBox=\\"0 0 24 24\\" width=\\"16\\" height=\\"16\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"2\\"><path d=\\"M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z\\"></path><path d=\\"M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z\\"></path></svg>\\r\\n          <span>{read_time}</span>\\r\\n        </div>\\r\\n        <div class=\\"blog-article-meta-item\\">\\r\\n          <svg viewBox=\\"0 0 24 24\\" width=\\"16\\" height=\\"16\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"2\\"><path d=\\"M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2\\"></path><circle cx=\\"12\\" cy=\\"7\\" r=\\"4\\"></circle></svg>\\r\\n          <span>By: CyTOS Machine Tool Engineering Team</span>\\r\\n        </div>\\r\\n      </div>\\r\\n    </div>\\r\\n  </header>\\r\\n\\r\\n  <!-- Main Article Layout -->\\r\\n  <main class=\\"container\\">\\r\\n    <div class=\\"blog-layout-container\\">\\r\\n      \\r\\n      <!-- Article Content Column -->\\r\\n      <article class=\\"blog-article-body\\">\\r\\n\\r\\n        <!-- Article Featured Hero Banner (16:9 4K Quality) -->\\r\\n        <figure class=\\"article-featured-lead-image\\">\\r\\n          <img src=\\"{image}\\" alt=\\"{alt_text}\\" width=\\"1200\\" height=\\"675\\" loading=\\"eager\\">\\r\\n        </figure>\\r\\n\\r\\n        <!-- AEO Direct Answer Box (Google AI Overview & LLM Snippets) -->\\r\\n        <div class=\\"aeo-direct-answer-card\\">\\r\\n          <div class=\\"aeo-header\\">\\r\\n            <span class=\\"aeo-badge\\">\\r\\n              <svg viewBox=\\"0 0 24 24\\" width=\\"16\\" height=\\"16\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"2.5\\"><polyline points=\\"20 6 9 17 4 12\\"></polyline></svg>\\r\\n              <span>Quick Technical Summary / Direct Answer</span>\\r\\n            </span>\\r\\n            <span style=\\"font-size: 0.78rem; color: #92400e; font-weight: 700;\\">ISO 9001:2015 Verified</span>\\r\\n          </div>\\r\\n          <p class=\\"aeo-direct-text\\">\\r\\n            {aeo_answer}\\r\\n          </p>\\r\\n        </div>\\r\\n\\r\\n        <!-- Table of Contents -->\\r\\n        <nav class=\\"blog-toc-card\\" aria-label=\\"Table of Contents\\">\\r\\n          <div class=\\"blog-toc-title\\">\\r\\n            <svg viewBox=\\"0 0 24 24\\" width=\\"20\\" height=\\"20\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"2\\"><line x1=\\"8\\" y1=\\"6\\" x2=\\"21\\" y2=\\"6\\"></line><line x1=\\"8\\" y1=\\"12\\" x2=\\"21\\" y2=\\"12\\"></line><line x1=\\"8\\" y1=\\"18\\" x2=\\"21\\" y2=\\"18\\"></line><line x1=\\"3\\" y1=\\"6\\" x2=\\"3.01\\" y2=\\"6\\"></line><line x1=\\"3\\" y1=\\"12\\" x2=\\"3.01\\" y2=\\"12\\"></line><line x1=\\"3\\" y1=\\"18\\" x2=\\"3.01\\" y2=\\"18\\"></line></svg>\\r\\n            <span>Article Navigation (Table of Contents)</span>\\r\\n          </div>\\r\\n          <ul class=\\"blog-toc-list\\">"""

    for item in blog["toc"]:
        t_id = item["id"]
        t_title = item["title"]
        header_html += f"""\\r\\n            <li><a href=\\"#{t_id}\\">{t_title}</a></li>"""

    header_html += f"""\\r\\n          </ul>\\r\\n        </nav>\\r\\n\\r\\n        <!-- Dynamic Content Sections -->"""

    # Body sections
    body_html = ""
    for sec in blog["sections"]:
        s_id = sec["id"]
        s_h2 = sec["h2"]
        s_content = sec["content"].replace('"', '\\"').replace('\n', '\\r\\n')
        body_html += f"""\\r\\n\\r\\n        <section id=\\"{s_id}\\">\\r\\n          <h2>{s_h2}</h2>\\r\\n          {s_content}\\r\\n        </section>"""

    # FAQ Section
    faq_html = f"""\\r\\n\\r\\n        <!-- FAQ Section (Schema.org Microdata & JSON-LD Bot Readable) -->\\r\\n        <section id=\\"frequently-asked-questions\\" class=\\"blog-faq-section\\" itemscope itemtype=\\"https://schema.org/FAQPage\\">\\r\\n          <h2>Frequently Asked Questions</h2>\\r\\n          <p class=\\"section-intro-text\\">Technical answers authored by CyTOS machine tool design engineers in Pune regarding special purpose machine manufacturing, tooling, cycle time optimization, and factory acceptance testing.</p>\\r\\n          <div class=\\"faq-accordion\\">"""

    for i, faq in enumerate(blog["faqs"], 1):
        q = faq["q"].replace('"', '&quot;')
        a = faq["a"].replace('"', '\\"').replace('\n', '\\r\\n')
        faq_html += f"""\\r\\n            <div class=\\"faq-item\\" itemscope itemprop=\\"mainEntity\\" itemtype=\\"https://schema.org/Question\\">\\r\\n              <button class=\\"faq-question\\" aria-expanded=\\"false\\">\\r\\n                <span itemprop=\\"name\\">Q{i}: {q}</span>\\r\\n                <svg class=\\"faq-icon\\" viewBox=\\"0 0 24 24\\" width=\\"18\\" height=\\"18\\"><polyline points=\\"6 9 12 15 18 9\\"></polyline></svg>\\r\\n              </button>\\r\\n              <div class=\\"faq-answer\\" itemscope itemprop=\\"acceptedAnswer\\" itemtype=\\"https://schema.org/Answer\\">\\r\\n                <div itemprop=\\"text\\">\\r\\n                  <p>{a}</p>\\r\\n                </div>\\r\\n              </div>\\r\\n            </div>"""

    faq_html += f"""\\r\\n          </div>\\r\\n        </section>"""

    # Author card & CTA
    author_cta_html = f"""\\r\\n\\r\\n        <!-- E-E-A-T Author Card -->\\r\\n        <div class=\\"article-author-card\\">\\r\\n          <div class=\\"author-card-avatar\\">CY</div>\\r\\n          <div class=\\"author-card-info\\">\\r\\n            <h4>CyTOS Machine Tool &amp; SPM Engineering Team</h4>\\r\\n            <p><strong>Senior Application Engineers, CyTOS Pune Works</strong></p>\\r\\n            <p>CyTOS Engineering Works specializes in cycle time optimization, multi-spindle drilling &amp; tapping systems, automatic thermal foam welding machines, robotic dispensing cells, and turnkey custom automated Special Purpose Machines (SPMs) designed and manufactured at our 3,000 sq. ft. plant in Dhayari, Pune, India.</p>\\r\\n          </div>\\r\\n        </div>\\r\\n\\r\\n        <!-- In-Article Machine Recommendation CTA -->\\r\\n        <div class=\\"tech-newsletter-card\\" id=\\"engineering-consultation\\" style=\\"margin: 3.5rem 0 1rem;\\">\\r\\n          <div>\\r\\n            <span class=\\"badge-accent\\" style=\\"margin-bottom: 0.5rem; display: inline-block;\\">Factory Consultation</span>\\r\\n            <h3>Consult CyTOS Applications Team on Technical Solutions</h3>\\r\\n            <p>\\r\\n              Looking to cut cycle time, eliminate bit breakages, or commission a high-rigidity Special Purpose Machine? Share your drawings or technical specs for a guaranteed 24-hour engineering assessment.\\r\\n            </p>\\r\\n          </div>\\r\\n          <div style=\\"display: flex; flex-direction: column; gap: 0.75rem;\\">\\r\\n            <button class=\\"btn btn-primary\\" data-open-rfq data-machine=\\"{machine_name}\\">\\r\\n              <span>Request Technical Consultation</span>\\r\\n            </button>\\r\\n            <a href=\\"https://wa.me/917620414165?text={encoded_wa}\\" target=\\"_blank\\" rel=\\"noopener noreferrer\\" class=\\"btn btn-whatsapp\\" style=\\"justify-content: center;\\">\\r\\n              <span>Chat with Application Engineer</span>\\r\\n            </a>\\r\\n          </div>\\r\\n        </div>\\r\\n\\r\\n      </article>"""

    # Sticky Sidebar
    sidebar_html = f"""\\r\\n\\r\\n      <!-- Sticky Sidebar -->\\r\\n      <aside class=\\"blog-sidebar\\">\\r\\n        \\r\\n        <!-- Primary Fast RFQ Card -->\\r\\n        <div class=\\"sidebar-lead-card\\">\\r\\n          <span class=\\"badge-mini\\" style=\\"background: var(--brand-gold); color: #fff; margin-bottom: 0.75rem; display: inline-block;\\">Factory Direct</span>\\r\\n          <h4>Get Machine Pricing &amp; Feasibility Report</h4>\\r\\n          <p>\\r\\n            Direct consultation with CyTOS design engineers in Pune. Guaranteed response within 24 hours with complete cycle time calculation and tooling recommendation.\\r\\n          </p>\\r\\n          <button class=\\"btn btn-primary\\" data-open-rfq data-machine=\\"{machine_name}\\">\\r\\n            <svg class=\\"btn-icon-svg\\" viewBox=\\"0 0 24 24\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"2\\"><path d=\\"M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z\\"></path><polyline points=\\"14 2 14 8 20 8\\"></polyline><line x1=\\"16\\" y1=\\"13\\" x2=\\"8\\" y2=\\"13\\"></line><line x1=\\"16\\" y1=\\"17\\" x2=\\"8\\" y2=\\"17\\"></line><polyline points=\\"10 9 9 9 8 9\\"></polyline></svg>\\r\\n            <span>Request Fast Quote</span>\\r\\n          </button>\\r\\n          <a href=\\"https://wa.me/917620414165?text={encoded_wa}\\" target=\\"_blank\\" rel=\\"noopener noreferrer\\" class=\\"btn btn-whatsapp\\">\\r\\n            <svg class=\\"whatsapp-icon-svg btn-icon-svg\\" viewBox=\\"0 0 24 24\\" fill=\\"currentColor\\"><path d=\\"M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.68C7.02 10.88 7.9 12.04 8.02 12.2C8.14 12.37 9.73 14.95 12.24 15.93C14.33 16.75 14.75 16.59 15.22 16.54C15.69 16.49 16.74 15.91 16.96 15.29C17.18 14.66 17.18 14.13 17.11 14.02C17.05 13.91 16.89 13.84 16.64 13.72C16.39 13.6 15.17 13 14.94 12.92C14.72 12.83 14.56 12.79 14.4 13.04C14.24 13.29 13.77 13.84 13.63 14.01C13.5 14.17 13.36 14.19 13.11 14.07C12.87 13.95 12.08 13.69 11.15 12.86C10.42 12.21 9.93 11.41 9.79 11.17C9.65 10.92 9.78 10.79 9.9 10.67C10.01 10.56 10.15 10.38 10.27 10.23C10.4 10.08 10.44 9.97 10.52 9.81C10.6 9.65 10.56 9.51 10.5 9.39C10.44 9.27 9.97 8.12 9.78 7.65C9.59 7.19 9.39 7.25 9.24 7.24C9.1 7.23 8.94 7.23 8.78 7.23H8.53Z\\"/></svg>\\r\\n            <span>WhatsApp RFQ</span>\\r\\n          </a>\\r\\n        </div>\\r\\n\\r\\n        <!-- Machine Model Spotlight Card -->\\r\\n        <div class=\\"sidebar-machine-card\\">\\r\\n          <div class=\\"sidebar-machine-badge\\">SPM Featured Solution</div>\\r\\n          <div class=\\"sidebar-machine-img-wrap\\">\\r\\n            <img src=\\"{image}\\" alt=\\"{machine_name}\\" loading=\\"lazy\\">\\r\\n          </div>\\r\\n          <div class=\\"sidebar-machine-body\\">\\r\\n            <h5>{machine_name}</h5>\\r\\n            <p>Custom-engineered single-purpose automated production cell designed to reduce cycle times by up to 70%.</p>\\r\\n            <ul class=\\"sidebar-machine-specs\\">\\r\\n              <li><span>Factor of Safety:</span><strong>2.0 Heavy Duty</strong></li>\\r\\n              <li><span>Duty Cycle:</span><strong>24x7 Continuous</strong></li>\\r\\n              <li><span>Origin:</span><strong>Pune, India</strong></li>\\r\\n            </ul>\\r\\n            <a href=\\"/spm-automation\\" class=\\"btn btn-outline btn-sm btn-block\\">\\r\\n              <span>View SPM Portfolio</span>\\r\\n            </a>\\r\\n          </div>\\r\\n        </div>\\r\\n\\r\\n        <!-- Phone Hotline Card -->\\r\\n        <div class=\\"sidebar-lead-card\\" style=\\"text-align: center;\\">\\r\\n          <span class=\\"badge-mini\\" style=\\"background: rgba(37,99,235,0.12); color: #1d4ed8; margin-bottom: 0.5rem; display: inline-block;\\">Application Engineering Hotline</span>\\r\\n          <h4 style=\\"font-size: 1.05rem; margin-bottom: 0.35rem;\\">Speak Directly With an SPM Design Engineer</h4>\\r\\n          <p style=\\"font-size: 0.85rem; margin-bottom: 1rem;\\">Mon–Sat, 9:00 AM – 7:00 PM IST</p>\\r\\n          <a href=\\"tel:+917620414165\\" class=\\"btn btn-primary btn-block\\" style=\\"font-size: 0.95rem; justify-content: center;\\">\\r\\n            <svg class=\\"btn-icon-svg\\" viewBox=\\"0 0 24 24\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"2\\"><path d=\\"M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z\\"></path></svg>\\r\\n            <span>+91 76204 14165</span>\\r\\n          </a>\\r\\n        </div>\\r\\n\\r\\n      </aside>\\r\\n    </div>\\r\\n  </main>"""

    # Related Posts Strip
    related_posts_html = f"""\\r\\n\\r\\n  <!-- Related Technical Articles Strip -->\\r\\n  <section class=\\"related-posts-section\\">\\r\\n    <div class=\\"container\\">\\r\\n      <h2 class=\\"related-posts-title\\">Related Technical Machining &amp; Automation Guides</h2>\\r\\n      <div class=\\"blog-grid\\" style=\\"margin-bottom: 0;\\">\\r\\n        <article class=\\"blog-card\\" data-category=\\"spm-automation\\">\\r\\n          <a href=\\"/blog/special-purpose-machines-spm-guide\\" class=\\"blog-card-img-wrap\\" title=\\"Special Purpose Machines (SPM): How Custom Industrial Automation Cuts Cycle Time 60%\\">\\r\\n            <img src=\\"/assets/images/blogs/spm-welding-automation-featured.jpg\\" alt=\\"Special purpose machines spm guide\\" loading=\\"lazy\\">\\r\\n          </a>\\r\\n          <div class=\\"blog-card-body\\">\\r\\n            <div class=\\"blog-meta-row\\">\\r\\n              <span class=\\"blog-category-badge\\">SPM &amp; Automation</span>\\r\\n              <span>•</span>\\r\\n              <span>15 min read</span>\\r\\n            </div>\\r\\n            <h3 class=\\"blog-card-title\\">\\r\\n              <a href=\\"/blog/special-purpose-machines-spm-guide\\">Special Purpose Machines (SPM): How Custom Industrial Automation Cuts Cycle Time 60%</a>\\r\\n            </h3>\\r\\n            <p class=\\"blog-excerpt\\">Discover how custom special purpose machines (SPM) engineered in Pune slash manufacturing cycle time by 60% and eliminate bottlenecks.</p>\\r\\n            <a href=\\"/blog/special-purpose-machines-spm-guide\\" class=\\"blog-card-link\\"><span>Read Technical Guide</span></a>\\r\\n          </div>\\r\\n        </article>\\r\\n        <article class=\\"blog-card\\" data-category=\\"spm-automation\\">\\r\\n          <a href=\\"/blog/pneumatic-welding-fixtures-spm-design\\" class=\\"blog-card-img-wrap\\" title=\\"Pneumatic Welding Fixtures SPM: Engineering 90° Rotary Indexing Jigs for Robotics\\">\\r\\n            <img src=\\"/assets/images/blogs/pneumatic-welding-fixtures-16x9.jpg\\" alt=\\"Pneumatic welding fixtures spm design\\" loading=\\"lazy\\">\\r\\n          </a>\\r\\n          <div class=\\"blog-card-body\\">\\r\\n            <div class=\\"blog-meta-row\\">\\r\\n              <span class=\\"blog-category-badge\\">SPM &amp; Automation</span>\\r\\n              <span>•</span>\\r\\n              <span>14 min read</span>\\r\\n            </div>\\r\\n            <h3 class=\\"blog-card-title\\">\\r\\n              <a href=\\"/blog/pneumatic-welding-fixtures-spm-design\\">Pneumatic Welding Fixtures SPM: Engineering 90° Rotary Indexing Jigs for Robotics</a>\\r\\n            </h3>\\r\\n            <p class=\\"blog-excerpt\\">Engineer high-durability pneumatic welding fixtures SPM systems for robotic welding cells with 90° rotary indexing.</p>\\r\\n            <a href=\\"/blog/pneumatic-welding-fixtures-spm-design\\" class=\\"blog-card-link\\"><span>Read Technical Guide</span></a>\\r\\n          </div>\\r\\n        </article>\\r\\n        <article class=\\"blog-card\\" data-category=\\"spm-automation\\">\\r\\n          <a href=\\"/blog/robotic-adhesive-dispensing-spm-systems\\" class=\\"blog-card-img-wrap\\" title=\\"Robotic Adhesive Dispensing SPM: Achieving Repeatable 0.05ml Bead Accuracy\\">\\r\\n            <img src=\\"/assets/images/blogs/robotic-dispensing-spm-featured.jpg\\" alt=\\"Robotic adhesive dispensing spm\\" loading=\\"lazy\\">\\r\\n          </a>\\r\\n          <div class=\\"blog-card-body\\">\\r\\n            <div class=\\"blog-meta-row\\">\\r\\n              <span class=\\"blog-category-badge\\">SPM &amp; Automation</span>\\r\\n              <span>•</span>\\r\\n              <span>14 min read</span>\\r\\n            </div>\\r\\n            <h3 class=\\"blog-card-title\\">\\r\\n              <a href=\\"/blog/robotic-adhesive-dispensing-spm-systems\\">Robotic Adhesive Dispensing SPM: Achieving Repeatable 0.05ml Bead Accuracy</a>\\r\\n            </h3>\\r\\n            <p class=\\"blog-excerpt\\">Master robotic adhesive dispensing SPM engineering. Learn 3-axis volumetric dispensing and bead accuracy.</p>\\r\\n            <a href=\\"/blog/robotic-adhesive-dispensing-spm-systems\\" class=\\"blog-card-link\\"><span>Read Technical Guide</span></a>\\r\\n          </div>\\r\\n        </article>\\r\\n      </div>\\r\\n    </div>\\r\\n  </section>\\r\\n\\r\\n  """

    # Assemble full HTML string
    full_html = TOP_NAV + header_html + body_html + faq_html + author_cta_html + sidebar_html + related_posts_html + FOOTER_AND_SCRIPTS
    return full_html

# 2. Append new blogs to allBlogsHtml.js
print("Integrating into allBlogsHtml.js...")
with open(ALL_BLOGS_HTML_PATH, "r", encoding="utf-8") as f:
    orig_all_blogs = f.read()

new_articles_list = []
for b in SPM_BLOGS:
    if f'"{b["slug"]}":' in orig_all_blogs:
        print(f"Skipping {b['slug']} in allBlogsHtml.js - already present.")
        continue
    
    html_val = build_article_html(b)
    # Write as JS object property
    entry = f'  "{b["slug"]}": {{\n'
    entry += f'    "title": "{b["title"].replace(chr(34), chr(92) + chr(34))}",\n'
    entry += f'    "description": "{b["metaDescription"].replace(chr(34), chr(92) + chr(34))}",\n'
    entry += f'    "html": "{html_val}"\n'
    entry += '  }'
    new_articles_list.append(entry)

if new_articles_list:
    # Find position of last `};`
    last_brace = orig_all_blogs.rfind("};")
    prefix = orig_all_blogs[:last_brace].rstrip()
    
    # Ensure there is a comma after the previous last entry
    if not prefix.endswith(","):
        prefix += ",\n"
    else:
        prefix += "\n"
        
    inserted_chunk = ",\n".join(new_articles_list) + "\n};\n"
    updated_all_blogs = prefix + inserted_chunk
    with open(ALL_BLOGS_HTML_PATH, "w", encoding="utf-8") as f:
        f.write(updated_all_blogs)
    print("allBlogsHtml.js updated successfully.")
else:
    print("allBlogsHtml.js already contains all blogs.")

# 3. Append metadata to blogData.js
BLOG_DATA_PATH = os.path.join(DATA_DIR, "blogData.js")
with open(BLOG_DATA_PATH, "r", encoding="utf-8") as f:
    orig_blog_data = f.read()

new_blog_data_entries = ""
for b in SPM_BLOGS:
    if f'"{b["slug"]}"' in orig_blog_data:
        print(f"Skipping {b['slug']} in blogData.js - already present.")
        continue
    
    # Construct paragraph list from sections
    paragraphs = []
    for sec in b["sections"]:
        raw_paras = re.findall(r'<p>(.*?)</p>', sec["content"], re.DOTALL)
        for p in raw_paras:
            clean_p = re.sub(r'<[^>]+>', '', p).strip()
            if clean_p:
                paragraphs.append(clean_p)

    metadata_obj = {
        "slug": b["slug"],
        "title": b["title"],
        "metaDescription": b["metaDescription"],
        "category": b["category"],
        "image": b["image"],
        "readTime": b["readTime"],
        "date": b["date"],
        "aeoAnswer": b["aeoAnswer"],
        "excerpt": b["excerpt"],
        "paragraphs": paragraphs[:6],
        "faqs": [],
        "toc": b["toc"]
    }
    
    obj_json = json.dumps(metadata_obj, indent=4)
    indented = "\n".join("  " + line for line in obj_json.splitlines())
    new_blog_data_entries += f",\n{indented}"

if new_blog_data_entries:
    last_bracket = orig_blog_data.rfind("];")
    updated_blog_data = orig_blog_data[:last_bracket] + new_blog_data_entries + "\n" + orig_blog_data[last_bracket:]
    with open(BLOG_DATA_PATH, "w", encoding="utf-8") as f:
        f.write(updated_blog_data)
    print("blogData.js updated successfully.")
else:
    print("blogData.js already contains all blog metadata.")

# 4. Update BlogListingPage.jsx
BLOG_LISTING_PATH = os.path.join(PAGES_DIR, "BlogListingPage.jsx")
with open(BLOG_LISTING_PATH, "r", encoding="utf-8") as f:
    orig_listing = f.read()

new_listing_cards = ""
for b in SPM_BLOGS:
    if f'/blog/{b["slug"]}' in orig_listing:
        print(f"Skipping card {b['slug']} in BlogListingPage.jsx - already present.")
        continue
    
    title = b["title"].replace('"', '&quot;')
    slug = b["slug"]
    img = b["image"]
    alt = b["altText"].replace('"', '&quot;')
    read_time = b["readTime"]
    excerpt = b["excerpt"][:220].replace('"', '&quot;') + "..."
    
    card_html = f"""        <!-- Blog Card: {slug} -->\\r\\n        <article class=\\"blog-card\\" data-category=\\"spm-automation\\">\\r\\n          <a href=\\"/blog/{slug}\\" class=\\"blog-card-img-wrap\\" title=\\"{title}\\">\\r\\n            <img src=\\"{img}\\" alt=\\"{alt}\\" loading=\\"lazy\\">\\r\\n          </a>\\r\\n          <div class=\\"blog-card-body\\">\\r\\n            <div class=\\"blog-meta-row\\">\\r\\n              <span class=\\"blog-category-badge\\">SPM &amp; Automation</span>\\r\\n              <span>•</span>\\r\\n              <span>{read_time}</span>\\r\\n            </div>\\r\\n            <h3 class=\\"blog-card-title\\">\\r\\n              <a href=\\"/blog/{slug}\\" title=\\"{title}\\">{title}</a>\\r\\n            </h3>\\r\\n            <p class=\\"blog-excerpt\\">{excerpt}</p>\\r\\n            <a href=\\"/blog/{slug}\\" class=\\"blog-card-link\\" title=\\"Read full guide: {title}\\">\\r\\n              <span>Read Technical Guide</span>\\r\\n              <svg viewBox=\\"0 0 24 24\\" width=\\"16\\" height=\\"16\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"2\\" stroke-linecap=\\"round\\" stroke-linejoin=\\"round\\" aria-hidden=\\"true\\"><line x1=\\"5\\" y1=\\"12\\" x2=\\"19\\" y2=\\"12\\"></line><polyline points=\\"12 5 19 12 12 19\\"></polyline></svg>\\r\\n            </a>\\r\\n          </div>\\r\\n        </article>\\r\\n"""
    new_listing_cards += card_html

if new_listing_cards:
    spm_marker = '<!-- Blog Card: special-purpose-machines-spm-guide -->'
    if spm_marker in orig_listing:
        idx = orig_listing.find(spm_marker)
        updated_listing = orig_listing[:idx] + new_listing_cards + orig_listing[idx:]
    else:
        grid_end = orig_listing.find('</div>\\r\\n    </div>\\r\\n  </main>')
        updated_listing = orig_listing[:grid_end] + new_listing_cards + orig_listing[grid_end:]
    
    updated_listing = updated_listing.replace("22 Technical Articles Grid", "27 Technical Articles Grid")
    updated_listing = updated_listing.replace("Explore 22 technical engineering guides", "Explore 27 technical engineering guides")
    with open(BLOG_LISTING_PATH, "w", encoding="utf-8") as f:
        f.write(updated_listing)
    print("BlogListingPage.jsx updated successfully.")
else:
    print("BlogListingPage.jsx already contains cards.")

# 5. Update BlogIndexPage.jsx count
BLOG_INDEX_PATH = os.path.join(PAGES_DIR, "BlogIndexPage.jsx")
with open(BLOG_INDEX_PATH, "r", encoding="utf-8") as f:
    idx_content = f.read()

if "22 technical engineering guides" in idx_content:
    idx_content = idx_content.replace("22 technical engineering guides", "27 technical engineering guides")
    with open(BLOG_INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(idx_content)
    print("BlogIndexPage.jsx updated count.")

# 6. Update public/sitemap.xml
SITEMAP_PATH = os.path.join(PUBLIC_DIR, "sitemap.xml")
if os.path.exists(SITEMAP_PATH):
    with open(SITEMAP_PATH, "r", encoding="utf-8") as f:
        sm_content = f.read()
    
    sm_additions = ""
    for b in SPM_BLOGS:
        url = f"https://www.cytos.in/blog/{b['slug']}"
        if url not in sm_content:
            sm_additions += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{b['date']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>\n"""
    
    if sm_additions:
        sm_content = sm_content.replace("</urlset>", sm_additions + "</urlset>")
        with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
            f.write(sm_content)
        print("sitemap.xml updated with 5 new URLs.")
    else:
        print("sitemap.xml already contains new URLs.")

print("All 5 SPM blogs generated and integrated successfully!")
