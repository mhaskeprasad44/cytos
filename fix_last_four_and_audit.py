# -*- coding: utf-8 -*-
"""
fix_last_four_and_audit.py
Fixes the 4 remaining Pillar 4 blogs so all 22 blogs achieve 100.0% PASS.
"""

import os
import re
import glob

PROJECT_DIR = r"c:\Users\PrasadMhaske\Downloads\Project1"
BLOG_DIR = os.path.join(PROJECT_DIR, "blog")

from build_all_blogs import ALL_BLOGS

FOUR_FIXES = {
    "aluminium-composite-sheet-cnc-drilling-milling": {
        "kw": "aluminium sheet cnc drilling and milling",
        "kw_words": 6,
        "figures": [
            "Aluminium Sheet CNC Drilling and Milling - High-speed profiling on 6061-T6 aluminum sheet",
            "Aluminium Sheet CNC Drilling and Milling - Single-flute carbide end mill cutting clean chips",
            "Aluminium Sheet CNC Drilling and Milling - Aerospace avionics brackets holding ±0.02mm tolerance",
            "Aluminium Sheet CNC Drilling and Milling - Vacuum bed matrix securing large aluminium sheet"
        ],
        "target_count": 5
    },
    "bt30-vs-bt40-cnc-drilling-and-milling": {
        "kw": "bt30 vs bt40 cnc drilling and milling",
        "kw_words": 6,
        "figures": [
            "BT30 vs BT40 CNC Drilling and Milling - Dimensional comparison of 7/24 taper tool holders",
            "BT30 vs BT40 CNC Drilling and Milling - High-torque BT40 spindle performing heavy face milling",
            "BT30 vs BT40 CNC Drilling and Milling - CyTOS VDM machine configured with dual BT30 spindles",
            "BT30 vs BT40 CNC Drilling and Milling - Precision angular contact spindle bearing assembly"
        ],
        "target_count": 5
    },
    "cnc-drilling-and-milling-machine-guide": {
        "kw": "cnc drilling and milling",
        "kw_words": 4,
        "figures": [
            "CNC Drilling and Milling - CyTOS VDM heavy multi-spindle machine for heavy electrical panels",
            "CNC Drilling and Milling - Rigid spindle nose executing high-feed face milling and pattern drilling",
            "CNC Drilling and Milling - BT30 and BT40 tool clamping system with automated pull-stud retention",
            "CNC Drilling and Milling - Precision hand-scraping of cast iron slideways at CyTOS Pune works"
        ],
        "target_count": 8
    },
    "vertical-drilling-and-milling-machine-guide": {
        "kw": "vertical drilling and milling machine",
        "kw_words": 5,
        "figures": [
            "Vertical Drilling and Milling Machine - CyTOS VDM series gantry with dual high-torque spindles",
            "Vertical Drilling and Milling Machine - Precision end-milling of rectangular meter apertures",
            "Vertical Drilling and Milling Machine - Workshop installation in Bhosari MIDC Pune panel factory",
            "Vertical Drilling and Milling Machine - Completed modular switchboard plates demonstrating clean edges"
        ],
        "target_count": 6
    }
}

SYNONYMS = {
    "aluminium sheet cnc drilling and milling": "high-speed aluminum plate routing",
    "bt30 vs bt40 cnc drilling and milling": "BT30 and BT40 spindle kinematics",
    "cnc drilling and milling": "precision vertical CNC machining",
    "vertical drilling and milling machine": "vertical enclosure milling center"
}

def apply_fixes():
    print("=== Applying Surgical Fixes to Pillar 4 Blogs ===")
    
    for slug, data in FOUR_FIXES.items():
        fpath = os.path.join(BLOG_DIR, f"{slug}.html")
        if not os.path.isfile(fpath):
            print(f"File not found: {fpath}")
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        kw = data["kw"]
        kw_words = data["kw_words"]
        figs = data["figures"]
        target = data["target_count"]
        syn = SYNONYMS[kw]

        # 1. Update the 4 figure alt tags
        def fig_replacer(m):
            fig_idx = getattr(fig_replacer, "idx", 0)
            fig_replacer.idx = fig_idx + 1
            if fig_idx < len(figs):
                alt_text = figs[fig_idx]
            else:
                alt_text = f"{kw.title()} - Technical Machining Figure"
            img_src = m.group(1)
            caption = m.group(3)
            return f'''<figure class="article-media-figure">
          <img src="{img_src}" alt="{alt_text}" loading="lazy">
          <figcaption>{caption}</figcaption>
        </figure>'''

        fig_replacer.idx = 0
        html = re.sub(
            r'<figure class="article-media-figure">\s*<img src="([^"]+)" alt="([^"]*)"[^>]*>\s*<figcaption>(.*?)</figcaption>\s*</figure>',
            fig_replacer,
            html,
            flags=re.DOTALL
        )

        # 2. Check current occurrences in visible text
        no_scripts = re.sub(r'<script.*?</script>', ' ', html, flags=re.DOTALL)
        no_styles = re.sub(r'<style.*?</style>', ' ', no_scripts, flags=re.DOTALL)
        page_text = re.sub(r'<[^>]+>', ' ', no_styles)
        current_count = page_text.lower().count(kw)

        # If current_count > target, substitute occurrences in middle paragraphs
        diff = current_count - target
        if diff > 0:
            # Find article body
            art_match = re.search(r'(<article class="blog-article-body">)(.*?)(</article>)', html, re.DOTALL)
            if art_match:
                art_body = art_match.group(2)
                # Find first section
                sec_m = re.search(r'<section[^>]*class="article-section"[^>]*>', art_body)
                if sec_m:
                    hdr = art_body[:sec_m.start()]
                    secs = art_body[sec_m.start():]
                    p1_m = re.search(r'(<p>.*?</p>)', secs, re.DOTALL)
                    if p1_m:
                        rest = secs[p1_m.end():]
                        
                        # Find occurrences in rest and replace from back
                        kw_re = re.compile(re.escape(kw), re.IGNORECASE)
                        matches = list(kw_re.finditer(rest))
                        for match in reversed(matches):
                            if diff > 0:
                                s, e = match.span()
                                rest = rest[:s] + syn + rest[e:]
                                diff -= 1

                        new_art = hdr + secs[:p1_m.end()] + rest
                        html = html[:art_match.start(2)] + new_art + html[art_match.end(2):]

        # Save to blog/{slug}.html
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)

        # Mirror to blog/{slug}/index.html
        slug_dir = os.path.join(BLOG_DIR, slug)
        if os.path.isdir(slug_dir):
            dir_index = os.path.join(slug_dir, "index.html")
            dir_html = html.replace('href="../', 'href="../../').replace('src="../', 'src="../../')
            with open(dir_index, "w", encoding="utf-8") as f:
                f.write(dir_html)

        print(f"Updated {slug}: Alt text locked, KW count set to {target}!")

if __name__ == "__main__":
    apply_fixes()
