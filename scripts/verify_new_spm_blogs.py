import os
import json
import re

with open("src/data/blogData.js", "r", encoding="utf-8") as f:
    blog_data_txt = f.read()

with open("src/data/allBlogsHtml.js", "r", encoding="utf-8") as f:
    all_blogs_txt = f.read()

with open("src/pages/BlogListingPage.jsx", "r", encoding="utf-8") as f:
    listing_txt = f.read()

with open("public/sitemap.xml", "r", encoding="utf-8") as f:
    sitemap_txt = f.read()

target_slugs = [
    "multi-spindle-drilling-tapping-spm",
    "automatic-foam-welding-machine-spm",
    "rotary-indexing-table-assembly-spm",
    "custom-gantry-pick-and-place-automation-spm",
    "spm-machine-roi-and-cycle-time-calculation"
]

print("=== VERIFICATION RESULTS FOR 5 NEW SPM BLOGS ===\n")

for slug in target_slugs:
    in_blog_data = f'"{slug}"' in blog_data_txt
    in_all_blogs = f'"{slug}":' in all_blogs_txt
    in_listing = f'/blog/{slug}' in listing_txt
    in_sitemap = f'/blog/{slug}' in sitemap_txt
    
    # Check length and headings in allBlogsHtml
    pos = all_blogs_txt.find(f'"{slug}":')
    if pos != -1:
        # find end of this entry
        next_pos = all_blogs_txt.find('\n  "', pos + len(slug) + 5)
        if next_pos == -1:
            next_pos = all_blogs_txt.rfind("};")
        entry_chunk = all_blogs_txt[pos:next_pos]
        length = len(entry_chunk)
        h2s = re.findall(r'<h2>(.*?)</h2>', entry_chunk)
        faqs = re.findall(r'<div class=\\"faq-item\\"', entry_chunk)
        ctas = re.findall(r'data-open-rfq', entry_chunk)
        wa = re.findall(r'wa\.me/917620414165', entry_chunk)
    else:
        length = 0
        h2s = []
        faqs = []
        ctas = []
        wa = []
        
    print(f"Slug: {slug}")
    print(f"  - blogData.js:      {'PASS' if in_blog_data else 'FAIL'}")
    print(f"  - allBlogsHtml.js:  {'PASS' if in_all_blogs else 'FAIL'} (HTML chunk length: {length:,} chars)")
    print(f"  - BlogListingPage:  {'PASS' if in_listing else 'FAIL'}")
    print(f"  - sitemap.xml:      {'PASS' if in_sitemap else 'FAIL'}")
    print(f"  - H2 Headings:      {len(h2s)} sections")
    print(f"  - FAQs:             {len(faqs)} items")
    print(f"  - RFQ Modal CTAs:   {len(ctas)} triggers")
    print(f"  - WhatsApp Triggers:{len(wa)} triggers")
    print()

print("All verifications complete.")
