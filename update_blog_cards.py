# -*- coding: utf-8 -*-
"""
update_blog_cards.py
Re-renders all 22 cards in blog.html with:
1. 16:9 featured images from assets/images/blogs/
2. Clickable image link: <a href="blog/{slug}.html" class="blog-card-img-wrap"><img ...></a>
3. Clickable title link: <h3 class="blog-card-title"><a href="blog/{slug}.html">{title}</a></h3>
4. Primary read technical guide button link
"""

import os
import re
from build_all_blogs import ALL_BLOGS, BLOG_FEATURE_IMAGES

PROJECT_DIR = r"c:\Users\PrasadMhaske\Downloads\Project1"
blog_index_path = os.path.join(PROJECT_DIR, "blog.html")

with open(blog_index_path, "r", encoding="utf-8") as f:
    html = f.read()

start_marker = '<div class="blog-grid" id="blogGrid">'
end_marker = '<!-- Technical Newsletter & Whitepaper Download Box -->'

s_idx = html.find(start_marker)
e_idx = html.find(end_marker)

if s_idx == -1 or e_idx == -1:
    print(f"Error: Markers not found. s_idx={s_idx}, e_idx={e_idx}")
    exit(1)

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

# Between start_marker and end_marker, replace with cards_html + "\n      </div>\n      "
content_to_insert = start_marker + cards_html + "\n      </div>\n      "
new_html = html[:s_idx] + content_to_insert + html[e_idx:]

with open(blog_index_path, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Updated blog.html with all 22 16:9 featured cards and clickable titles successfully!")
