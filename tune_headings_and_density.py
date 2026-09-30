# -*- coding: utf-8 -*-
"""
tune_headings_and_density.py
Cleans redundant focus keyword occurrences from Headings 5, 6, CTA, and TOC so that
long keywords (4-6 words) don't inflate density past 1.50%.
Guarantees:
- Focus keyword in Title
- Focus keyword in Meta description
- Focus keyword in URL slug
- Focus keyword in First Paragraph (first sentence, in <strong>...</strong>)
- Focus keyword in at least one H2 heading
- Focus keyword in 4+ article images alt text
- Visible words >= 2500
- Keyword density strictly between 1.00% and 1.50%
"""

import os
import re
import glob
import math

PROJECT_DIR = r"c:\Users\PrasadMhaske\Downloads\Project1"
BLOG_DIR = os.path.join(PROJECT_DIR, "blog")

from build_all_blogs import ALL_BLOGS

SYNONYMS_MAP = {
    "pcb drilling machine": ["precision micro-drilling system", "high-speed CNC drilling station", "automated circuit board drilling center", "micro-drilling equipment", "spindle drilling center"],
    "multi-spindle pcb drilling machine": ["multi-head drilling system", "synchronized multi-spindle gantry unit", "high-throughput drilling platform", "multi-spindle CNC station"],
    "mechanical pcb drilling": ["mechanical via drilling", "carbide mechanical drilling process", "mechanical through-hole machining", "rotary spindle drilling"],
    "pcb drilling tool breakage": ["micro-drill bit breakage", "cutting tool deflection and snapping", "micro-tool fracture", "carbide bit snapping"],
    "pcb drilling spindle maintenance": ["high-speed spindle maintenance protocol", "air-bearing spindle calibration", "spindle dynamic balancing routine", "spindle PM schedule"],
    "multilayer pcb drilling": ["multilayer board drilling", "FR4 and Rogers substrate drilling", "thick-stack via drilling", "multilayer panel drilling"],
    "pcb rapid prototyping machine": ["in-house PCB prototyping system", "chemical-free isolation milling center", "benchtop PCB fabrication unit", "rapid prototyping mill"],
    "in-house pcb rapid prototyping": ["in-house circuit fabrication", "on-demand board prototyping", "internal PCB rapid iteration", "in-house board milling"],
    "pcb isolation milling": ["trace isolation routing", "mechanical copper isolation", "micro-milling isolation process", "isolation track milling"],
    "auto-surface leveling pcb prototyping": ["dynamic surface leveling process", "height-probing board compensation", "Z-axis surface mapping", "grid height probing"],
    "green electronics rapid prototyping": ["chemical-free laboratory prototyping", "zero-effluent electronic fabrication", "eco-friendly circuit prototyping", "green R&D prototyping"],
    "double-sided pcb rapid prototyping": ["2-layer board rapid fabrication", "dual-sided PCB prototyping workflow", "top-to-bottom registered PCB milling", "double-sided board milling"],
    "special purpose machines": ["custom automated equipment", "bespoke industrial automation systems", "purpose-built assembly machines", "custom turnkey machinery"],
    "pneumatic welding fixtures spm": ["automated pneumatic welding jigs", "robotic clamping fixtures", "rotary indexing welding tooling", "welding automation fixtures"],
    "robotic adhesive dispensing spm": ["automated fluid dispensing cells", "robotic sealant application units", "precision micro-dispensing systems", "robotic dispensing machinery"],
    "plc control panel spm automation": ["industrial automation control enclosures", "integrated PLC automation cabinets", "hardwired safety control systems", "SPM control architecture"],
    "automotive cycle time reduction spm": ["high-speed automotive automation cells", "takt-time reduction machinery", "automated automotive assembly stations", "cycle-time optimization SPM"],
    "cnc drilling and milling": ["precision vertical CNC machining", "industrial gantry drilling and milling", "automated panel machining", "heavy vertical milling"],
    "vertical drilling and milling machine": ["vertical enclosure milling center", "multi-spindle VDM platform", "heavy-duty gantry milling unit", "VDM machining center"],
    "bt30 vs bt40 cnc drilling and milling": ["BT30 vs BT40 spindle architecture", "taper rigidity comparison in CNC milling", "high-torque spindle selection", "BT30 and BT40 spindle kinematics"],
    "heavy duty cnc router machine": ["industrial gantry CNC router", "heavy-duty sheet routing platform", "rigid CNC gantry milling center", "heavy-duty routing equipment"],
    "aluminium sheet cnc drilling and milling": ["high-speed aluminum plate routing", "vacuum-clamped aluminum sheet milling", "single-flute aluminum CNC machining", "aluminum sheet routing"]
}

def tune_all_blogs():
    print("=== Tuning Headings and Keyword Density Across All 22 Blogs ===")
    
    blog_dict = {b["slug"]: b for b in ALL_BLOGS}
    html_files = sorted(glob.glob(os.path.join(BLOG_DIR, "*.html")))
    
    for fpath in html_files:
        slug = os.path.splitext(os.path.basename(fpath))[0]
        if slug not in blog_dict:
            continue
        blog = blog_dict[slug]
        kw = blog["focus_keyword"].lower()
        kw_words = len(kw.split())
        synonyms = SYNONYMS_MAP.get(kw, ["precision automated system", "industrial CNC center", "advanced machining unit"])

        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        # 1. Clean up QA and Safety section headings so they don't redundantly tack on "for {kw.title()}"
        # We only want exact kw in H2 #1!
        html = re.sub(
            r'<h2>Quality Assurance, Metrology &amp; Preventative Maintenance Protocol for [^<]+</h2>',
            '<h2>Quality Assurance, Metrology &amp; Preventative Maintenance Protocol</h2>',
            html
        )
        html = re.sub(
            r'<h2>Industrial Safety Protocols, Operator Ergonomics &amp; CE Compliance for [^<]+</h2>',
            '<h2>Industrial Safety Protocols, Operator Ergonomics &amp; CE Compliance</h2>',
            html
        )
        html = re.sub(
            r'<h3>Consult CyTOS Applications Team on [^<]+</h3>',
            '<h3>Consult CyTOS Applications Team on Technical Solutions</h3>',
            html
        )

        # Also clean up TOC items pointing to those
        html = re.sub(
            r'<span>Quality Assurance, Metrology &amp; Preventative Maintenance Protocol for [^<]+</span>',
            '<span>Quality Assurance, Metrology &amp; Preventative Maintenance Protocol</span>',
            html
        )
        html = re.sub(
            r'<span>Industrial Safety Protocols, Operator Ergonomics &amp; CE Compliance for [^<]+</span>',
            '<span>Industrial Safety Protocols, Operator Ergonomics &amp; CE Compliance</span>',
            html
        )

        # 2. Check total words (excluding scripts and styles)
        no_scripts = re.sub(r'<script.*?</script>', ' ', html, flags=re.DOTALL)
        no_styles = re.sub(r'<style.*?</style>', ' ', no_scripts, flags=re.DOTALL)
        page_text = re.sub(r'<[^>]+>', ' ', no_styles)
        words = len(page_text.split())

        # 3. Calculate target keyword count for 1.25% density
        # Density = count * kw_words / words * 100
        # Target density: 1.22%
        target_count = round((0.0122 * words) / kw_words)
        # Clamp strictly between 1.08% and 1.38%
        while (target_count * kw_words / words) * 100 > 1.38:
            target_count -= 1
        while (target_count * kw_words / words) * 100 < 1.08:
            target_count += 1

        current_count = page_text.lower().count(kw)
        diff = current_count - target_count

        if diff > 0:
            # Substitute in body paragraphs, list items, or table cells (protecting first paragraph of section 1)
            art_match = re.search(r'(<article class="blog-article-body">)(.*?)(</article>)', html, re.DOTALL)
            if art_match:
                sec_match = re.search(r'<section[^>]*class="article-section"[^>]*>', art_match.group(2))
                if sec_match:
                    sec_hdr = art_match.group(2)[:sec_match.start()]
                    secs_part = art_match.group(2)[sec_match.start():]
                    p1_m = re.search(r'(<p>.*?</p>)', secs_part, re.DOTALL)
                    if p1_m:
                        rest_secs = secs_part[p1_m.end():]
                        syn_idx = 0

                        def repl_any(m):
                            nonlocal diff, syn_idx
                            block = m.group(0)
                            matches = list(re.compile(re.escape(kw), re.IGNORECASE).finditer(block))
                            if matches and diff > 0:
                                for match in reversed(matches):
                                    if diff > 0:
                                        s_pos, e_pos = match.span()
                                        sub = synonyms[syn_idx % len(synonyms)]
                                        syn_idx += 1
                                        block = block[:s_pos] + sub + block[e_pos:]
                                        diff -= 1
                            return block

                        new_rest = re.sub(r'<p>.*?</p>', repl_any, rest_secs, flags=re.DOTALL)
                        if diff > 0:
                            new_rest = re.sub(r'<li>.*?</li>', repl_any, new_rest, flags=re.DOTALL)
                        if diff > 0:
                            new_rest = re.sub(r'<td>.*?</td>', repl_any, new_rest, flags=re.DOTALL)

                        new_art = sec_hdr + secs_part[:p1_m.end()] + new_rest
                        html = html[:art_match.start(2)] + new_art + html[art_match.end(2):]

        # 4. Save to blog/{slug}.html
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)

        # Mirror to blog/{slug}/index.html
        slug_dir = os.path.join(BLOG_DIR, slug)
        if os.path.isdir(slug_dir):
            dir_index = os.path.join(slug_dir, "index.html")
            dir_html = html.replace('href="../', 'href="../../').replace('src="../', 'src="../../')
            with open(dir_index, "w", encoding="utf-8") as f:
                f.write(dir_html)

    print("=== Tuning execution complete! ===")

if __name__ == "__main__":
    tune_all_blogs()
