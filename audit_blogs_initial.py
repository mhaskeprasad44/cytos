# -*- coding: utf-8 -*-
import sys
import re
from blog_data_pillar1 import PILLAR_1_BLOGS
from blog_data_pillar2 import PILLAR_2_BLOGS
from blog_data_pillar3 import PILLAR_3_BLOGS
from blog_data_pillar4 import PILLAR_4_BLOGS

all_blogs = PILLAR_1_BLOGS + PILLAR_2_BLOGS + PILLAR_3_BLOGS + PILLAR_4_BLOGS

print(f"Total blogs loaded: {len(all_blogs)}")
for i, b in enumerate(all_blogs, 1):
    kw = b['focus_keyword'].lower()
    title = b['title'].lower()
    meta = b['meta_description'].lower()
    slug = b['slug'].lower()
    
    in_title = kw in title
    in_meta = kw in meta
    
    # slug check
    slug_words = set(slug.replace('-', ' ').split())
    kw_words = [w for w in kw.split() if w not in ['and', '&', 'in', 'vs', 'the', 'for']]
    in_slug = all(w in slug_words for w in kw_words)
    
    # check first p
    first_sec = b['sections'][0]['content']
    p_match = re.search(r'<p>(.*?)</p>', first_sec, re.DOTALL)
    in_p = kw in p_match.group(1).lower() if p_match else False
    
    # check headings
    all_h = ' '.join(s['title'].lower() for s in b['sections'])
    in_h = kw in all_h

    # images check
    images_with_kw = sum(1 for img in b['images'] if kw in img['alt'].lower())
    
    status = "OK" if (in_title and in_meta and in_slug and in_p and in_h and images_with_kw == len(b['images'])) else "CHECK"
    print(f"{i:02d}. [{status}] {slug[:32]:32} | Title: {in_title} | Meta: {in_meta} | Slug: {in_slug} | P1: {in_p} | H: {in_h} | Img: {images_with_kw}/{len(b['images'])}")
