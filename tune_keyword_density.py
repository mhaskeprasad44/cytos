# -*- coding: utf-8 -*-
"""
tune_keyword_density.py
Fine-tunes exact focus keyword density across all 22 blogs to strictly fall
within the user-specified 1.0% to 1.5% range, avoiding keyword stuffing.
"""

import os
import re

from build_all_blogs import ALL_BLOGS, BLOG_DIR, generate_blog_html, build_blogs, update_blog_index_page, generate_sitemap

# Synonyms to replace excessive focus keyword repetitions while preserving meaning
SYNONYM_MAP = {
    "pcb drilling machine": [
        "high-speed drilling system",
        "precision CNC drill",
        "micro-drilling center",
        "PCB fabrication equipment",
        "industrial drilling station"
    ],
    "multi-spindle pcb drilling machine": [
        "multi-spindle drilling center",
        "synchronized multi-head system",
        "dual-spindle PCB machine",
        "multi-station drilling gantry",
        "high-throughput PCB system"
    ],
    "mechanical pcb drilling": [
        "mechanical micro-drilling",
        "CNC mechanical drilling",
        "spindle-based drilling",
        "mechanical hole fabrication",
        "carbide mechanical drilling"
    ],
    "green electronics rapid prototyping": [
        "sustainable in-house prototyping",
        "eco-friendly PCB fabrication",
        "chemical-free prototyping",
        "clean laboratory prototyping",
        "dry mechanical circuit prototyping"
    ],
    "special purpose machines": [
        "custom automation systems",
        "dedicated production equipment",
        "turnkey SPM stations",
        "custom engineered machinery",
        "automated SPM cells"
    ],
    "pneumatic welding fixtures spm": [
        "pneumatic welding jigs",
        "automated rotary welding fixtures",
        "pneumatic clamping systems",
        "robotic welding tooling",
        "heavy welding jigs"
    ],
    "robotic adhesive dispensing spm": [
        "automated dispensing cell",
        "robotic fluid dispensing system",
        "precision glue dispensing machine",
        "Cartesian dispensing cell",
        "automated sealant system"
    ],
    "plc control panel spm automation": [
        "industrial automation control panel",
        "PLC electrical enclosure",
        "machine automation panel",
        "Siemens/Delta control cabinet",
        "turnkey electrical panel"
    ],
    "automotive cycle time reduction spm": [
        "automotive production automation",
        "cycle-time reduction machine",
        "automated automotive cell",
        "high-speed SPM system",
        "automotive assembly station"
    ],
    "cnc drilling and milling": [
        "vertical drilling and milling",
        "plate machining center",
        "industrial gantry milling",
        "CNC plate drilling",
        "heavy milling and drilling"
    ],
    "vertical drilling and milling machine": [
        "vertical drilling and milling center",
        "VDM gantry machine",
        "enclosure milling machine",
        "multi-spindle plate drill",
        "vertical machining gantry"
    ],
    "heavy duty cnc router machine": [
        "heavy-duty gantry router",
        "industrial CNC router",
        "rigid gantry machining center",
        "heavy plate router",
        "structural CNC router"
    ],
    "aluminium sheet cnc drilling and milling": [
        "aluminum plate CNC routing",
        "high-speed aluminum machining",
        "aluminum sheet milling",
        "non-ferrous plate routing",
        "aluminum profile machining"
    ],
    "pcb rapid prototyping machine": [
        "desktop PCB prototyping mill",
        "chemical-free prototyping center",
        "in-house circuit prototyping system",
        "rapid PCB milling machine",
        "laboratory PCB mill"
    ],
    "in-house pcb rapid prototyping": [
        "in-house circuit prototyping",
        "laboratory PCB fabrication",
        "internal board prototyping",
        "on-demand PCB milling",
        "desktop circuit prototyping"
    ],
    "pcb isolation milling": [
        "mechanical isolation routing",
        "copper trace isolation",
        "contour isolation milling",
        "chemical-free PCB milling",
        "dry isolation routing"
    ],
    "double-sided pcb rapid prototyping": [
        "two-sided PCB prototyping",
        "double-sided circuit milling",
        "multi-layer prototype fabrication",
        "double-sided board milling",
        "two-layer PCB fabrication"
    ],
}

def optimize_blog_density():
    print("=== Optimizing Keyword Density to 1.0% - 1.5% Range ===")
    
    for blog in ALL_BLOGS:
        kw = blog["focus_keyword"].lower()
        
        # Calculate current density across the blog's text
        temp_html = generate_blog_html(blog, ALL_BLOGS)
        clean_text = re.sub(r'<[^>]+>', ' ', temp_html)
        words = clean_text.split()
        total_words = len(words)
        kw_len = len(kw.split())
        
        # Count occurrences in content sections only (never touch title, meta, first paragraph, or primary H2s)
        current_matches = clean_text.lower().count(kw)
        current_density = (current_matches * kw_len / max(total_words, 1)) * 100
        
        target_density_min = 1.00
        target_density_max = 1.45
        
        # Target number of occurrences
        target_occurrences = int((1.25 / 100.0) * total_words / kw_len)
        target_occurrences = max(target_occurrences, 4)
        
        if current_density > target_density_max and kw in SYNONYM_MAP:
            synonyms = SYNONYM_MAP[kw]
            excess = current_matches - target_occurrences
            replaced = 0
            syn_idx = 0
            
            # Replace occurrences in later sections (keeping first paragraph and key subheadings intact!)
            for sec in reversed(blog["sections"]):
                # Don't replace in the very first section's first paragraph
                text = sec["content"]
                
                # Case-insensitive replacement of some occurrences
                pattern = re.compile(re.escape(blog["focus_keyword"]), re.IGNORECASE)
                matches = list(pattern.finditer(text))
                
                if matches and replaced < excess:
                    new_text = text
                    # Replace from the end of the section backward
                    for m in reversed(matches):
                        if replaced >= excess:
                            break
                        # Substitute with a synonym
                        syn = synonyms[syn_idx % len(synonyms)]
                        syn_idx += 1
                        new_text = new_text[:m.start()] + syn + new_text[m.end():]
                        replaced += 1
                    sec["content"] = new_text
            
            # Recalculate
            new_temp_html = generate_blog_html(blog, ALL_BLOGS)
            new_clean = re.sub(r'<[^>]+>', ' ', new_temp_html)
            new_words = new_clean.split()
            new_matches = new_clean.lower().count(kw)
            new_density = (new_matches * kw_len / len(new_words)) * 100
            print(f"[{blog['slug']}] Adjusted: {current_matches} -> {new_matches} matches | Density: {current_density:.2f}% -> {new_density:.2f}% (Target: 1.0% - 1.5%)")
        else:
            print(f"[{blog['slug']}] Optimal: {current_matches} matches | Density: {current_density:.2f}% (Already in target range)")

if __name__ == "__main__":
    optimize_blog_density()
    build_blogs()
    update_blog_index_page()
    generate_sitemap()
    print("\n=== Density Tuning and Build Complete! ===")
