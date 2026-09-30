# -*- coding: utf-8 -*-
"""
tune_keyword_density_perfect.py
Balances keyword density across all 22 blog HTML files to strictly 1.0% - 1.5% (targeting ~1.25%),
while strictly protecting:
- <title>
- <meta name="description">
- Canonical & OG URLs
- Schema JSON-LD
- Direct Answer box
- First section first paragraph (<p>...</p>)
- All H1, H2, H3 headings
- Image alt attributes
"""

import os
import re
import glob
import math

PROJECT_DIR = r"c:\Users\PrasadMhaske\Downloads\Project1"
BLOG_DIR = os.path.join(PROJECT_DIR, "blog")

from build_all_blogs import ALL_BLOGS

SYNONYMS_MAP = {
    "pcb drilling machine": ["precision micro-drilling system", "high-speed CNC drilling station", "automated circuit board drilling center", "micro-drilling equipment"],
    "multi-spindle pcb drilling machine": ["multi-head drilling system", "synchronized multi-spindle gantry unit", "high-throughput drilling platform"],
    "mechanical pcb drilling": ["mechanical via drilling", "carbide mechanical drilling process", "mechanical through-hole machining"],
    "pcb drilling tool breakage": ["micro-drill bit breakage", "cutting tool deflection and snapping", "micro-tool fracture"],
    "pcb drilling spindle maintenance": ["high-speed spindle maintenance protocol", "air-bearing spindle calibration", "spindle dynamic balancing routine"],
    "multilayer pcb drilling": ["multilayer board drilling", "FR4 and Rogers substrate drilling", "thick-stack via drilling"],
    "pcb rapid prototyping machine": ["in-house PCB prototyping system", "chemical-free isolation milling center", "benchtop PCB fabrication unit"],
    "in-house pcb rapid prototyping": ["in-house circuit fabrication", "on-demand board prototyping", "internal PCB rapid iteration"],
    "pcb isolation milling": ["trace isolation routing", "mechanical copper isolation", "micro-milling isolation process"],
    "auto-surface leveling pcb prototyping": ["dynamic surface leveling process", "height-probing board compensation", "Z-axis surface mapping"],
    "green electronics rapid prototyping": ["chemical-free laboratory prototyping", "zero-effluent electronic fabrication", "eco-friendly circuit prototyping"],
    "double-sided pcb rapid prototyping": ["2-layer board rapid fabrication", "dual-sided PCB prototyping workflow", "top-to-bottom registered PCB milling"],
    "special purpose machines": ["custom automated equipment", "bespoke industrial automation systems", "purpose-built assembly machines"],
    "pneumatic welding fixtures spm": ["automated pneumatic welding jigs", "robotic clamping fixtures", "rotary indexing welding tooling"],
    "robotic adhesive dispensing spm": ["automated fluid dispensing cells", "robotic sealant application units", "precision micro-dispensing systems"],
    "plc control panel spm automation": ["industrial automation control enclosures", "integrated PLC automation cabinets", "hardwired safety control systems"],
    "automotive cycle time reduction spm": ["high-speed automotive automation cells", "takt-time reduction machinery", "automated automotive assembly stations"],
    "cnc drilling and milling": ["precision vertical CNC machining", "industrial gantry drilling and milling", "automated panel machining"],
    "vertical drilling and milling machine": ["vertical enclosure milling center", "multi-spindle VDM platform", "heavy-duty gantry milling unit"],
    "bt30 vs bt40 cnc drilling and milling": ["BT30 vs BT40 spindle architecture", "taper rigidity comparison in CNC milling", "high-torque spindle selection"],
    "heavy duty cnc router machine": ["industrial gantry CNC router", "heavy-duty sheet routing platform", "rigid CNC gantry milling center"],
    "aluminium sheet cnc drilling and milling": ["high-speed aluminum plate routing", "vacuum-clamped aluminum sheet milling", "single-flute aluminum CNC machining"]
}

def balance_density():
    print("=== Balancing Keyword Density to 1.0% - 1.5% Across All 22 Blogs ===")
    
    blog_dict = {b["slug"]: b for b in ALL_BLOGS}
    html_files = glob.glob(os.path.join(BLOG_DIR, "*.html"))
    
    for fpath in sorted(html_files):
        slug = os.path.splitext(os.path.basename(fpath))[0]
        if slug not in blog_dict:
            continue
            
        blog = blog_dict[slug]
        kw = blog["focus_keyword"].lower()
        synonyms = SYNONYMS_MAP.get(kw, ["precision automated system", "industrial CNC center", "advanced machining unit"])
        kw_word_count = len(kw.split())

        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        # Compute initial metrics
        clean_text = re.sub(r'<[^>]+>', ' ', html)
        words = clean_text.split()
        total_words = len(words)
        
        current_kw_count = clean_text.lower().count(kw)
        current_density = (current_kw_count * kw_word_count / total_words) * 100

        # Target density: 1.25% (allowed window: 1.05% - 1.45%)
        target_count = round((0.0125 * total_words) / kw_word_count)
        max_allowed = math.floor((0.0145 * total_words) / kw_word_count)

        if current_kw_count > max_allowed:
            excess = current_kw_count - target_count
            print(f"[{slug[:28]:28}] Current: {current_kw_count} ({current_density:.2f}%). Target: {target_count} ({(target_count*kw_word_count/total_words)*100:.2f}%). Excess to substitute: {excess}")

            body_match = re.search(r'(<article class="blog-article-body">)(.*?)(</article>)', html, re.DOTALL)
            if body_match:
                prefix = body_match.group(1)
                body_content = body_match.group(2)
                suffix = body_match.group(3)

                # Match start of first article section
                sec_match = re.search(r'<section[^>]*class="article-section"[^>]*>', body_content)
                if sec_match:
                    header_part = body_content[:sec_match.start()]
                    sections_part = body_content[sec_match.start():]

                    # Protect first paragraph:
                    p1_match = re.search(r'(<p>.*?</p>)', sections_part, re.DOTALL)
                    if p1_match:
                        p1_text = p1_match.group(1)
                        rest_sections = sections_part[p1_match.end():]

                        syn_idx = 0
                        replaced = 0

                        def replace_in_p(m):
                            nonlocal replaced, syn_idx
                            p_block = m.group(0)
                            kw_re = re.compile(re.escape(kw), re.IGNORECASE)
                            matches = list(kw_re.finditer(p_block))
                            if matches and replaced < excess:
                                for match in reversed(matches):
                                    if replaced < excess:
                                        start, end = match.span()
                                        sub_term = synonyms[syn_idx % len(synonyms)]
                                        syn_idx += 1
                                        p_block = p_block[:start] + sub_term + p_block[end:]
                                        replaced += 1
                            return p_block

                        new_rest_sections = re.sub(r'<p>.*?</p>', replace_in_p, rest_sections, flags=re.DOTALL)
                        new_sections_part = sections_part[:p1_match.end()] + new_rest_sections
                        new_body_content = header_part + new_sections_part
                        html = html[:body_match.start(2)] + new_body_content + html[body_match.end(2):]

        # Recompute final density
        clean_text_final = re.sub(r'<[^>]+>', ' ', html)
        words_final = clean_text_final.split()
        total_words_final = len(words_final)
        final_kw_count = clean_text_final.lower().count(kw)
        final_density = (final_kw_count * kw_word_count / total_words_final) * 100
        passed = 1.0 <= final_density <= 1.5

        print(f"  -> Result: {total_words_final} words | KW '{kw}': {final_kw_count} times = {final_density:.2f}% | Pass 1.0-1.5%: {passed}")

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

if __name__ == "__main__":
    balance_density()
    print("\n=== Density Tuning Complete! ===")
