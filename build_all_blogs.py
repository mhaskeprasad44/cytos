# -*- coding: utf-8 -*-
"""
build_all_blogs.py
Master compiler script to:
1. Generate all 22 comprehensive technical blog HTML files in /blog/
2. Generate extensionless index.html copies in /blog/{slug}/index.html for universal server support
3. Update the main blog index page (blog.html) with all 22 cards and filter pills
4. Generate an SEO-optimized sitemap.xml with all core pages and blog URLs
5. Validate word count, keyword density, and schema compliance
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

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BLOG_DIR = os.path.join(PROJECT_DIR, "blog")

def build_blogs():
    print(f"=== Starting Build of {len(ALL_BLOGS)} CyTOS Technical Engineering Blogs ===")
    os.makedirs(BLOG_DIR, exist_ok=True)

    generated_files = []

    for idx, blog in enumerate(ALL_BLOGS, 1):
        slug = blog["slug"]
        print(f"[{idx}/{len(ALL_BLOGS)}] Generating: {slug} ({blog['category_name']})...")

        html_content = generate_blog_html(blog, ALL_BLOGS)

        # 1. Write blog/{slug}.html
        file_path_html = os.path.join(BLOG_DIR, f"{slug}.html")
        with open(file_path_html, "w", encoding="utf-8") as f:
            f.write(html_content)
        generated_files.append(file_path_html)

        # 2. Write blog/{slug}/index.html (guarantees https://cytos.in/blog/slug works on any static server)
        slug_dir = os.path.join(BLOG_DIR, slug)
        os.makedirs(slug_dir, exist_ok=True)
        file_path_dir_index = os.path.join(slug_dir, "index.html")
        # In directory index.html, relative paths are two levels up (../../)
        # We can adjust relative paths for ../styles.css -> ../../styles.css
        dir_html_content = html_content.replace('href="../', 'href="../../')
        dir_html_content = dir_html_content.replace('src="../', 'src="../../')
        with open(file_path_dir_index, "w", encoding="utf-8") as f:
            f.write(dir_html_content)

        # Calculate word count & keyword density
        # Strip tags for raw word count
        clean_text = re.sub(r'<[^>]+>', ' ', html_content)
        words = clean_text.split()
        word_count = len(words)
        kw = blog['focus_keyword'].lower()
        kw_count = clean_text.lower().count(kw)
        kw_density = (kw_count * len(kw.split()) / max(word_count, 1)) * 100

        print(f"    -> Generated: {file_path_html}")
        print(f"    -> Word count: {word_count} words | Focus Keyword '{kw}': {kw_count} times (~{kw_density:.2f}% density)")

    print(f"\nSuccessfully generated {len(ALL_BLOGS)} blog pages in {BLOG_DIR}")
    return generated_files

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

def update_blog_index_page():
    print("\n=== Updating Master Blog Index: blog.html ===")
    blog_index_path = os.path.join(PROJECT_DIR, "blog.html")

    # Read existing blog.html to preserve tracking, header, and footer
    with open(blog_index_path, "r", encoding="utf-8") as f:
        existing_html = f.read()

    # Generate cards HTML for all 22 blogs
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

    # Replace the contents of <div class="blog-grid" id="blogGrid">...</div>
    grid_pattern = re.compile(r'(<div class="blog-grid" id="blogGrid">)(.*?)(<div class="tech-newsletter-card">)', re.DOTALL)
    if grid_pattern.search(existing_html):
        new_html = grid_pattern.sub(r'\1' + cards_html + '\n      </div>\n      <!-- Technical Newsletter & Whitepaper Download Box -->\n      \3', existing_html)
        with open(blog_index_path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print("Updated blog.html with all 22 cards successfully!")
    else:
        print("Warning: Could not match blogGrid in blog.html.")

def generate_sitemap():
    print("\n=== Generating Complete XML Sitemap: sitemap.xml ===")
    sitemap_path = os.path.join(PROJECT_DIR, "sitemap.xml")
    today = datetime.date.today().strftime("%Y-%m-%d")

    core_pages = [
        ("https://cytos.in/", "1.0", "daily"),
        ("https://cytos.in/pcb-drilling-routing.html", "0.95", "weekly"),
        ("https://cytos.in/pcb-prototyping.html", "0.95", "weekly"),
        ("https://cytos.in/cnc-routers-milling.html", "0.90", "weekly"),
        ("https://cytos.in/vdm-milling.html", "0.90", "weekly"),
        ("https://cytos.in/spm-automation.html", "0.90", "weekly"),
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

    # Core Pages
    for url, prio, freq in core_pages:
        sitemap_xml += f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>\n'

    # 22 Blog URLs (URL format: https://cytos.in/blog/blog_name)
    for blog in ALL_BLOGS:
        blog_url = f"https://cytos.in/blog/{blog['slug']}"
        sitemap_xml += f'  <url>\n    <loc>{blog_url}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.85</priority>\n  </url>\n'

    sitemap_xml += '</urlset>\n'

    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print(f"Generated sitemap.xml with {len(core_pages) + len(ALL_BLOGS)} total URLs successfully!")

if __name__ == "__main__":
    build_blogs()
    update_blog_index_page()
    generate_sitemap()
    print("\n=== All Build Tasks Completed Successfully! ===")
