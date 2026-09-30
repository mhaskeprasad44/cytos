# -*- coding: utf-8 -*-
"""
rebuild_blog_system.py
1. Compiles all 22 blog HTML files into /blog/{slug}.html
2. Compiles directory copies into /blog/{slug}/index.html
3. Updates blog.html:
   - Featured article with clickable image, clickable title, and direct link button
   - All 22 blog cards inside #blogGrid with 16:9 images, clickable images, clickable titles, and direct guide links
   - Icon-only floating quote button matching WhatsApp dock (no text span)
4. Updates sitemap.xml with all URLs
"""

import os
import re
import datetime
from blog_generator_core import generate_blog_html
from blog_data_pillar1 import PILLAR_1_BLOGS
from blog_data_pillar2 import PILLAR_2_BLOGS
from blog_data_pillar3 import PILLAR_3_BLOGS
from blog_data_pillar4 import PILLAR_4_BLOGS

ALL_BLOGS = PILLAR_1_BLOGS + PILLAR_2_BLOGS + PILLAR_3_BLOGS + PILLAR_4_BLOGS

BLOG_FEATURE_IMAGES = {
    "pcb-drilling-machine-guide": "assets/images/blogs/pcb-micro-drilling-featured.jpg",
    "multi-spindle-pcb-drilling-machine": "assets/images/blogs/multi-spindle-drilling-featured.jpg",
    "mechanical-pcb-drilling-vs-laser-drilling": "assets/images/blogs/pcb-drilling-laser-comparison-16x9.jpg",
    "pcb-drilling-tool-breakage-prevention": "assets/images/blogs/micro-drill-bit-breakage-prevention.jpg",
    "60000-rpm-pcb-drilling-spindle-maintenance": "assets/images/blogs/pcb-spindle-maintenance-16x9.jpg",
    "multilayer-fr4-rogers-pcb-drilling": "assets/images/blogs/multilayer-fr4-rogers-drilling-16x9.jpg",
    "chemical-free-pcb-rapid-prototyping-machine": "assets/images/blogs/pcb-rapid-prototyping-featured.jpg",
    "in-house-pcb-rapid-prototyping-roi": "assets/images/blogs/pcb-rapid-prototyping-roi-16x9.jpg",
    "gerber-to-pcb-isolation-milling-guide": "assets/images/blogs/pcb-isolation-milling-traces.jpg",
    "auto-surface-leveling-pcb-prototyping": "assets/images/blogs/auto-surface-leveling-16x9.jpg",
    "green-electronics-rapid-prototyping-lab": "assets/images/blogs/green-electronics-lab-16x9.jpg",
    "double-sided-pcb-rapid-prototyping-guide": "assets/images/blogs/double-sided-pcb-prototyping-16x9.jpg",
    "special-purpose-machines-spm-guide": "assets/images/blogs/spm-welding-automation-featured.jpg",
    "pneumatic-welding-fixtures-spm-design": "assets/images/blogs/pneumatic-welding-fixtures-16x9.jpg",
    "robotic-adhesive-dispensing-spm-systems": "assets/images/blogs/robotic-dispensing-spm-featured.jpg",
    "plc-control-panel-automation-spm-safety": "assets/images/blogs/plc-control-panel-automation.jpg",
    "automotive-cycle-time-reduction-spm": "assets/images/blogs/automotive-spm-cycle-time-16x9.jpg",
    "cnc-drilling-and-milling-machine-guide": "assets/images/blogs/cnc-milling-heavy-featured.jpg",
    "vertical-drilling-and-milling-machine-guide": "assets/images/blogs/vdm-switchboard-milling-featured.jpg",
    "bt30-vs-bt40-cnc-drilling-and-milling": "assets/images/blogs/bt30-vs-bt40-spindle-taper.jpg",
    "heavy-duty-cnc-router-machine-guide": "assets/images/blogs/cnc-gantry-router-featured.jpg",
    "aluminium-composite-sheet-cnc-drilling-milling": "assets/images/blogs/aluminum-sheet-cold-air-milling.jpg"
}

PROJECT_DIR = r"c:\Users\PrasadMhaske\Downloads\Project1"
BLOG_DIR = os.path.join(PROJECT_DIR, "blog")

def build_all_articles():
    print(f"Generating {len(ALL_BLOGS)} blog articles...")
    os.makedirs(BLOG_DIR, exist_ok=True)
    for idx, blog in enumerate(ALL_BLOGS, 1):
        slug = blog["slug"]
        html_content = generate_blog_html(blog, ALL_BLOGS)

        # 1. blog/{slug}.html
        file_path_html = os.path.join(BLOG_DIR, f"{slug}.html")
        with open(file_path_html, "w", encoding="utf-8") as f:
            f.write(html_content)

        # 2. blog/{slug}/index.html
        slug_dir = os.path.join(BLOG_DIR, slug)
        os.makedirs(slug_dir, exist_ok=True)
        file_path_dir_index = os.path.join(slug_dir, "index.html")
        dir_html_content = html_content.replace('href="../', 'href="../../')
        dir_html_content = dir_html_content.replace('src="../', 'src="../../')
        with open(file_path_dir_index, "w", encoding="utf-8") as f:
            f.write(dir_html_content)
        print(f"  [{idx:02d}/22] Generated: {slug}.html and {slug}/index.html")

def update_blog_html_page():
    print("\nUpdating blog.html...")
    blog_index_path = os.path.join(PROJECT_DIR, "blog.html")
    with open(blog_index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Featured Master Article
    old_featured_pattern = re.compile(r'<!-- Featured Master Article -->.*?<!-- \d+ Technical Articles Grid -->', re.DOTALL)
    new_featured_html = '''<!-- Featured Master Article -->
      <article class="featured-blog-card" data-category="pcb-proto">
        <a href="blog/chemical-free-pcb-rapid-prototyping-machine.html" class="featured-blog-img-wrap" title="Chemical-Free PCB Prototyping vs Traditional Wet Chemical Etching: A 2026 Engineering, Cost &amp; Environmental Audit">
          <img src="assets/images/blogs/pcb-rapid-prototyping-featured.jpg" alt="Chemical-Free PCB Prototyping Machine in R&amp;D Lab" loading="lazy">
        </a>
        <div class="featured-blog-body">
          <div class="blog-meta-row">
            <span class="blog-category-badge">PCB Prototyping</span>
            <span>•</span>
            <span>September 2026</span>
            <span>•</span>
            <span>8 min read</span>
          </div>
          <h2 class="blog-title-featured">
            <a href="blog/chemical-free-pcb-rapid-prototyping-machine.html" title="Chemical-Free PCB Prototyping vs Traditional Wet Chemical Etching: A 2026 Engineering, Cost &amp; Environmental Audit">
              Chemical-Free PCB Prototyping vs Traditional Wet Chemical Etching: A 2026 Engineering, Cost &amp; Environmental Audit
            </a>
          </h2>
          <p class="blog-excerpt">
            Why leading defense electronics labs, automotive R&amp;D centers, and engineering institutes in India are phasing out hazardous ferric chloride (FeCl₃) baths in favor of 60,000 RPM high-speed CNC isolation milling with auto-leveling surface height compensation.
          </p>
          <div class="blog-author-bar">
            <div class="blog-author-info">
              <div class="blog-author-avatar">CY</div>
              <div>
                <strong>CyTOS Applications Engineering Team</strong>
                <div style="font-size: 0.78rem; color: var(--text-tertiary);">R&amp;D Prototyping Division, Pune</div>
              </div>
            </div>
            <a href="blog/chemical-free-pcb-rapid-prototyping-machine.html" class="btn btn-primary btn-sm">Read Featured Guide</a>
          </div>
        </div>
      </article>

      <!-- 22 Technical Articles Grid -->'''

    if old_featured_pattern.search(html):
        html = old_featured_pattern.sub(new_featured_html, html)
        print("  -> Updated Featured Master Article with clickable image and title.")
    else:
        print("  -> Warning: Could not find Featured Master Article pattern.")

    # 2. Build and Replace All 22 Cards in blogGrid
    cards_html = ""
    for blog in ALL_BLOGS:
        slug = blog["slug"]
        cat_id = blog["category"]
        cat_name = blog["category_name"]
        read_time = blog["read_time"]
        title = blog["title"]
        meta_desc = blog["meta_description"]
        img_src = BLOG_FEATURE_IMAGES.get(slug, blog["images"][0]["src"])
        img_alt = blog["images"][0]["alt"]

        cards_html += f'''
        <!-- Blog Card: {slug} -->
        <article class="blog-card" data-category="{cat_id}">
          <a href="blog/{slug}.html" class="blog-card-img-wrap" title="{title}">
            <img src="{img_src}" alt="{img_alt}" loading="lazy">
          </a>
          <div class="blog-card-body">
            <div class="blog-meta-row">
              <span class="blog-category-badge">{cat_name}</span>
              <span>•</span>
              <span>{read_time}</span>
            </div>
            <h3 class="blog-card-title">
              <a href="blog/{slug}.html" title="{title}">{title}</a>
            </h3>
            <p class="blog-excerpt">{meta_desc}</p>
            <a href="blog/{slug}.html" class="blog-card-link" title="Read full guide: {title}">
              <span>Read Technical Guide</span>
              <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
          </div>
        </article>'''

    grid_start = '<div class="blog-grid" id="blogGrid">'
    grid_end = '<!-- Technical Newsletter & Whitepaper Download Box -->'
    s_idx = html.find(grid_start)
    e_idx = html.find(grid_end)

    if s_idx != -1 and e_idx != -1:
        replacement = grid_start + cards_html + "\n      </div>\n\n      "
        html = html[:s_idx] + replacement + html[e_idx:]
        print(f"  -> Replaced #blogGrid with all {len(ALL_BLOGS)} technical cards (clickable titles & 16:9 images).")
    else:
        print(f"  -> Error: Grid markers not found. s_idx={s_idx}, e_idx={e_idx}")

    # 3. Standardize Floating Action Buttons to Icon Version Only
    old_float_pattern = re.compile(r'<!-- Floating Fast Action Buttons -->.*?<\/aside>', re.DOTALL)
    new_float_html = '''<!-- Sticky Floating Action Buttons (Icon Version Only) -->
  <aside class="floating-contact-bar" aria-label="Quick Communication Dock">
    <a href="https://wa.me/919921381071?text=Hi%20CyTOS%20team,%20I%20am%20reading%20your%20engineering%20blog%20and%20would%20like%20to%20discuss%20a%20CNC%20machine." target="_blank" rel="noopener noreferrer" class="floating-btn floating-whatsapp" title="Chat with Technical Applications Desk" aria-label="Chat with Technical Applications Desk">
      <svg class="whatsapp-icon-svg" viewBox="0 0 24 24" width="26" height="26" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.68C7.02 10.88 7.9 12.04 8.02 12.2C8.14 12.37 9.73 14.95 12.24 15.93C14.33 16.75 14.75 16.59 15.22 16.54C15.69 16.49 16.74 15.91 16.96 15.29C17.18 14.66 17.18 14.13 17.11 14.02C17.05 13.91 16.89 13.84 16.64 13.72C16.39 13.6 15.17 13 14.94 12.92C14.72 12.83 14.56 12.79 14.4 13.04C14.24 13.29 13.77 13.84 13.63 14.01C13.5 14.17 13.36 14.19 13.11 14.07C12.87 13.95 12.08 13.69 11.15 12.86C10.42 12.21 9.93 11.41 9.79 11.17C9.65 10.92 9.78 10.79 9.9 10.67C10.01 10.56 10.15 10.38 10.27 10.23C10.4 10.08 10.44 9.97 10.52 9.81C10.6 9.65 10.56 9.51 10.5 9.39C10.44 9.27 9.97 8.12 9.78 7.65C9.59 7.19 9.39 7.25 9.24 7.24C9.1 7.23 8.94 7.23 8.78 7.23H8.53Z"/></svg>
    </a>
    <button class="floating-btn floating-quote-btn" data-open-rfq data-machine="Blog Engineering Consultation" title="Request Fast Technical Quote" aria-label="Request Fast Quote">
      <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    </button>
  </aside>'''

    if old_float_pattern.search(html):
        html = old_float_pattern.sub(new_float_html, html)
        print("  -> Replaced floating buttons with clean icon-only floating-contact-bar.")
    else:
        print("  -> Notice: Floating action bar already updated or pattern differed.")

    with open(blog_index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  -> blog.html written successfully!")

def update_sitemap():
    print("\nUpdating sitemap.xml...")
    sitemap_path = os.path.join(PROJECT_DIR, "sitemap.xml")
    today = datetime.date.today().strftime("%Y-%m-%d")

    core_pages = [
        ("https://cytos.in/", "1.0", "daily"),
        ("https://cytos.in/pcb-drilling-routing.html", "0.95", "weekly"),
        ("https://cytos.in/pcb-prototyping.html", "0.95", "weekly"),
        ("https://cytos.in/cnc-routers-milling.html", "0.90", "weekly"),
        ("https://cytos.in/vdm-milling.html", "0.90", "weekly"),
        ("https://cytos.in/spm-automation.html", "0.90", "weekly"),
        ("https://cytos.in/robotic-dispensing-cells.html", "0.85", "weekly"),
        ("https://cytos.in/pneumatic-welding-fixtures.html", "0.85", "weekly"),
        ("https://cytos.in/plc-control-panels.html", "0.85", "weekly"),
        ("https://cytos.in/case-studies.html", "0.85", "weekly"),
        ("https://cytos.in/applications.html", "0.85", "weekly"),
        ("https://cytos.in/about.html", "0.80", "monthly"),
        ("https://cytos.in/blog.html", "0.90", "daily"),
        ("https://cytos.in/contact.html", "0.85", "monthly"),
        ("https://cytos.in/terms-conditions.html", "0.50", "yearly"),
        ("https://cytos.in/privacy-policy.html", "0.50", "yearly"),
    ]

    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for url, prio, freq in core_pages:
        sitemap_xml += f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>\n'

    for blog in ALL_BLOGS:
        blog_url = f"https://cytos.in/blog/{blog['slug']}"
        sitemap_xml += f'  <url>\n    <loc>{blog_url}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.85</priority>\n  </url>\n'

    sitemap_xml += '</urlset>\n'

    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print(f"  -> Generated sitemap.xml with {len(core_pages) + len(ALL_BLOGS)} URLs.")

if __name__ == "__main__":
    build_all_articles()
    update_blog_html_page()
    update_sitemap()
    print("\n=== All Blog System Updates Finished Successfully! ===")
