# -*- coding: utf-8 -*-
import os
import re
import glob
from build_all_blogs import ALL_BLOGS

PROJECT_DIR = r"c:\Users\PrasadMhaske\Downloads\Project1"
BLOG_DIR = os.path.join(PROJECT_DIR, "blog")

blog_dict = {b["slug"]: b for b in ALL_BLOGS}
html_files = glob.glob(os.path.join(BLOG_DIR, "*.html"))

print("=== Checking Exact Body Content Density (Yoast / RankMath / Google Standard) ===")

for fpath in sorted(html_files):
    slug = os.path.splitext(os.path.basename(fpath))[0]
    if slug not in blog_dict:
        continue
    blog = blog_dict[slug]
    kw = blog["focus_keyword"].lower()
    kw_words = len(kw.split())

    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Whole page visible text (excluding scripts/styles)
    no_scripts = re.sub(r'<script.*?</script>', ' ', html, flags=re.DOTALL)
    no_styles = re.sub(r'<style.*?</style>', ' ', no_scripts, flags=re.DOTALL)
    page_text = re.sub(r'<[^>]+>', ' ', no_styles)
    page_text = re.sub(r'\s+', ' ', page_text).strip()
    page_words = len(page_text.split())
    page_kw_count = page_text.lower().count(kw)
    page_density = (page_kw_count * kw_words / page_words) * 100

    # 2. Article body text only (<article class="blog-article-body">...</article>)
    m = re.search(r'<article class="blog-article-body">(.*?)</article>', no_styles, re.DOTALL)
    if m:
        art_text = re.sub(r'<[^>]+>', ' ', m.group(1))
        art_text = re.sub(r'\s+', ' ', art_text).strip()
        art_words = len(art_text.split())
        art_kw_count = art_text.lower().count(kw)
        art_density = (art_kw_count * kw_words / art_words) * 100
    else:
        art_words, art_kw_count, art_density = 0, 0, 0

    print(f"{slug[:28]:28} | Page: {page_words}w, kw:{page_kw_count} ({page_density:.2f}%) | Article: {art_words}w, kw:{art_kw_count} ({art_density:.2f}%)")
