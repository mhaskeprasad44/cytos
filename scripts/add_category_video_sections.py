# -*- coding: utf-8 -*-
"""
scripts/add_category_video_sections.py
Injects dedicated, direct in-place video demonstration sections into all 5 Category Hub pages:
- PcbDrillingPage.jsx
- PcbPrototypingPage.jsx
- CncRoutersPage.jsx
- VdmMillingPage.jsx
- PneumaticFixturesPage.jsx
"""

import os
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PAGES_DIR = os.path.join(BASE_DIR, "src", "pages")

CATEGORY_CONFIGS = [
    {
        "file": "PcbDrillingPage.jsx",
        "insert_before": "<!-- Complete Technical Specifications Table -->",
        "fallback_insert_before": "<!-- Workflow & Software Integration -->",
        "section_id": "pcb-drilling-videos",
        "badge": "FACTORY FOOTAGE • 1-CLICK DIRECT PLAY",
        "title": "PCB Drilling & Routing Systems in Live Action",
        "subtitle": "Watch 100,000 RPM high-speed electro-spindles, 0.1 mm micro-hole drilling, and multi-spindle synchronized panel fabrication running live at our Bhosari MIDC, Pune facility.",
        "videos": [
            {
                "id": "vvbIlXhe4BE",
                "title": "High Speed Industrial PCB Drilling Machine (CNC 6060)",
                "desc": "Watch the CyTOS CNC 6060 performing high-speed PCB drilling and routing with pneumatic automatic tool change (ATC) and high-frequency electro-spindles reaching up to 100,000 RPM at 160 hits/min.",
                "duration": "4K HD • 0:54",
                "spec_path": "/cnc-6060-pcb-drilling-routing-machine",
                "machine_name": "CNC 6060 PCB Drilling Machine"
            },
            {
                "id": "IT64Y8PkU9A",
                "title": "3-Axis Multi-Spindle PCB Drilling Machine with ATC (PCB12)",
                "desc": "Demonstrating three synchronized high-speed drilling spindles processing identical multilayer panels simultaneously, slashing batch cycle times by 66%.",
                "duration": "4K HD • 0:42",
                "spec_path": "/pcb12-multi-spindle-drilling-machine",
                "machine_name": "PCB12 Multi-Spindle Machine"
            }
        ]
    },
    {
        "file": "PcbPrototypingPage.jsx",
        "insert_before": "<!-- Comparison: Chemical Etching vs CyTOS Mechanical Milling -->",
        "fallback_insert_before": "<!-- Technical Specifications Table -->",
        "section_id": "pcb-prototyping-videos",
        "badge": "LAB DEMONSTRATION • DIRECT PLAY",
        "title": "Chemical-Free PCB Prototyping in Live Action",
        "subtitle": "Watch the CyTOS PCBE3020 mill 6-mil tracks, auto-compensate surface warpage with electronic probing, and drill through-holes without toxic ferric chloride chemical baths.",
        "videos": [
            {
                "id": "5qZVqYg9CYc",
                "title": "Chemical-Free PCB Prototyping Machine (PCBE3020)",
                "desc": "Complete mechanical isolation milling, through-hole drilling, and contour routing of double-sided FR4 circuit boards in under 30 minutes inside an interlocked safety cabinet.",
                "duration": "4K HD • 1:12",
                "spec_path": "/cnc-3020-pcb-prototyping-machine",
                "machine_name": "PCBE3020 Rapid Prototyper"
            }
        ]
    },
    {
        "file": "CncRoutersPage.jsx",
        "insert_before": "<!-- Technical Specifications Table -->",
        "fallback_insert_before": "<!-- Application / Material Matrix -->",
        "section_id": "cnc-router-videos",
        "badge": "WORKSHOP FOOTAGE • DIRECT PLAY",
        "title": "Industrial CNC Routers & Milling in Live Operation",
        "subtitle": "Heavy-duty gantry routers machining aluminium panels, acrylic lightguides, wood, and composites with high-speed surface finish and burr-free edges.",
        "videos": [
            {
                "id": "Wc9UoQiWpxI",
                "title": "High Accuracy Mini Milling Machine & CNC Router",
                "desc": "Precision vertical CNC milling demonstrating tool engagement, gantry rigidity, chip evacuation, and vibration-damped feeds on non-ferrous metals and composites.",
                "duration": "4K HD • 0:48",
                "spec_path": "/cnc-wood-acrylic-aluminium-router-machine",
                "machine_name": "CNC Router Milling Machine"
            }
        ]
    },
    {
        "file": "VdmMillingPage.jsx",
        "insert_before": "<!-- Technical Specifications Table -->",
        "fallback_insert_before": "<!-- Material Compatibility Matrix -->",
        "section_id": "vdm-milling-videos",
        "badge": "FACTORY FOOTAGE • DIRECT PLAY",
        "title": "VDM Heavy Vertical Drilling & Milling in Action",
        "subtitle": "Multi-spindle rigid milling and deep hole drilling on electrical switchboard busbars, composite mounting plates, and aluminium profiles filmed at CyTOS Pune.",
        "videos": [
            {
                "id": "Wc9UoQiWpxI",
                "title": "High Accuracy VDM Vertical Milling Machine",
                "desc": "Rigid column architecture and precision ball screws delivering vibration-free milling across non-ferrous and composite plates.",
                "duration": "4K HD • 0:48",
                "spec_path": "/vdm-heavy-vertical-drilling-milling-machine",
                "machine_name": "VDM Vertical Milling Machine"
            }
        ]
    },
    {
        "file": "PneumaticFixturesPage.jsx",
        "insert_before": "<!-- Turnkey Engineering Process -->",
        "fallback_insert_before": "<!-- Detailed Case Studies -->",
        "section_id": "pneumatic-fixture-videos",
        "badge": "AUTOMATION FOOTAGE • DIRECT PLAY",
        "title": "Pneumatic Welding & Automation Fixtures in Live Operation",
        "subtitle": "Watch custom pneumatic clamping, 90-degree rotary indexing, and turnkey assembly jigs engineered for automotive robotic welding lines.",
        "videos": [
            {
                "id": "FOrQVsCUNrk",
                "title": "2-Axis Automated Soldering Machine SPM",
                "desc": "Custom automated soldering station engineered for repeatable solder joint quality and zero cold joints within a 100 x 100 mm envelope.",
                "duration": "4K HD • 0:58",
                "spec_path": "/spm-automation",
                "machine_name": "Soldering Robot SPM"
            },
            {
                "id": "kiNI2cvIVa4",
                "title": "Automatic Drilling Machine SPM with Pneumatic Clamping",
                "desc": "Special Purpose Drilling Machine designed to drill up to 15 mm diameter with positioning accuracy of 0.05 mm and rapid pneumatic part hold-down.",
                "duration": "4K HD • 0:45",
                "spec_path": "/pneumatic-welding-fixtures",
                "machine_name": "Drilling SPM Fixture"
            }
        ]
    }
]

def generate_video_section_html(cfg):
    videos = cfg["videos"]
    
    if len(videos) == 1:
        v = videos[0]
        inner_content = f'''      <div class="machine-video-grid">
        <div class="machine-video-frame-box video-thumb-box inline-video-thumb" data-video-id="{v['id']}" data-video-title="{v['title']}" title="Click to play {v['title']} right on this thumbnail" style="cursor: pointer; position: relative;">
          <img src="https://i.ytimg.com/vi/{v['id']}/hqdefault.jpg" alt="{v['title']}" loading="lazy" class="video-thumb-img" style="width: 100%; height: 100%; object-fit: cover; display: block;">
          <div class="video-play-overlay">
            <div class="video-play-circle" aria-label="Play {v['title']}">
              <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor" aria-hidden="true"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
            </div>
          </div>
          <span class="video-duration-pill">{v['duration']}</span>
        </div>
        <div class="machine-video-content">
          <div class="hero-badge" style="background: rgba(37,99,235,0.2); border-color: rgba(59,130,246,0.35); color: #93c5fd; margin-bottom: 0.75rem;">
            <span>{cfg['badge']}</span>
          </div>
          <h3 style="font-size: 1.75rem; color: #ffffff; margin: 0 0 0.85rem; font-weight: 800; line-height: 1.3;">{v['title']}</h3>
          <p style="color: #94a3b8; font-size: 0.95rem; line-height: 1.65; margin-bottom: 1.25rem;">{v['desc']}</p>
          <ul class="machine-video-feature-list">
            <li>
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>Recorded live at CyTOS Bhosari MIDC manufacturing plant in Pune</span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>Authentic tool speeds, feeds, surface finish &amp; clamping cycle</span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>1-click playback directly on this thumbnail with zero popup delay</span>
            </li>
          </ul>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
            <button class="btn btn-primary btn-play-trigger" data-video-id="{v['id']}" data-video-title="{v['title']}">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" style="margin-right: 6px;" aria-hidden="true"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
              <span>Play Video on Thumbnail</span>
            </button>
            <a href="{v['spec_path']}" class="btn btn-outline" style="border-color: rgba(255,255,255,0.25); color: #ffffff;">
              <span>View Full Machine Specs ❯</span>
            </a>
            <a href="https://www.youtube.com/watch?v={v['id']}" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="border-color: rgba(255,255,255,0.15); color: #94a3b8; font-size: 0.85rem;">
              <span>YouTube ↗</span>
            </a>
          </div>
        </div>
      </div>'''
    else:
        cards_html = []
        for v in videos:
            cards_html.append(f'''        <div style="background: rgba(30,41,59,0.7); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
          <div class="machine-video-frame-box video-thumb-box inline-video-thumb" data-video-id="{v['id']}" data-video-title="{v['title']}" title="Click to play {v['title']} right on this thumbnail" style="cursor: pointer; position: relative; margin-bottom: 1rem;">
            <img src="https://i.ytimg.com/vi/{v['id']}/hqdefault.jpg" alt="{v['title']}" loading="lazy" class="video-thumb-img" style="width: 100%; height: 100%; object-fit: cover; display: block;">
            <div class="video-play-overlay">
              <div class="video-play-circle" aria-label="Play {v['title']}">
                <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor" aria-hidden="true"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
              </div>
            </div>
            <span class="video-duration-pill">{v['duration']}</span>
          </div>
          <h4 style="color: #fff; margin: 0 0 0.5rem; font-size: 1.15rem; font-weight: 700; line-height: 1.35;">{v['title']}</h4>
          <p style="color: #94a3b8; font-size: 0.88rem; line-height: 1.55; margin-bottom: 1.25rem; flex-grow: 1;">{v['desc']}</p>
          <div style="display: flex; gap: 0.65rem; flex-wrap: wrap;">
            <button class="btn btn-primary btn-sm btn-play-trigger" data-video-id="{v['id']}" data-video-title="{v['title']}" style="flex: 1; min-width: 140px;">
              <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor" style="margin-right: 4px;" aria-hidden="true"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
              <span>Play on Thumbnail</span>
            </button>
            <a href="{v['spec_path']}" class="btn btn-outline btn-sm" style="border-color: rgba(255,255,255,0.25); color: #e2e8f0;">
              <span>Specs ❯</span>
            </a>
          </div>
        </div>''')
        
        cards_joined = "\n".join(cards_html)
        inner_content = f'''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.75rem;">
{cards_joined}
      </div>'''

    section_markup = f'''
  <!-- Live Machinery Video Demonstration Section (In-Place Thumbnail Playback) -->
  <section class="machine-video-section" id="{cfg['section_id']}" style="background: #0b1120; padding: 3.5rem 0; border-top: 1px solid rgba(255,255,255,0.08); border-bottom: 1px solid rgba(255,255,255,0.08);">
    <div class="container">
      <div class="section-header text-center" style="margin-bottom: 2.5rem;">
        <div class="hero-badge" style="background: rgba(37,99,235,0.2); border-color: rgba(59,130,246,0.35); color: #93c5fd; margin: 0 auto 0.75rem;">
          <span>{cfg['badge']}</span>
        </div>
        <h2 class="section-title" style="color: #ffffff;">{cfg['title']}</h2>
        <p class="section-subtitle" style="color: #94a3b8; max-width: 760px; margin: 0 auto;">
          {cfg['subtitle']}
        </p>
      </div>

{inner_content}
    </div>
  </section>
'''
    return section_markup

def process_page(cfg):
    file_path = os.path.join(PAGES_DIR, cfg["file"])
    if not os.path.exists(file_path):
        print(f"Error: {file_path} does not exist.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # If section already added, skip
    if cfg["section_id"] in content:
        print(f"Info: {cfg['file']} already has {cfg['section_id']}, skipping.")
        return

    sec_html = generate_video_section_html(cfg)

    # Format for escaped javascript string inside const pageHtml = "..."
    # Note that inside the file, double quotes are escaped as \" or line breaks are \r\n
    # Let's inspect how the target file formats pageHtml
    is_template_literal = "const pageHtml = `" in content
    
    if is_template_literal:
        formatted_sec = sec_html
    else:
        # String literal with escaped quotes and \r\n
        formatted_sec = sec_html.replace('\\', '\\\\').replace('"', '\\"').replace('\r\n', '\n').replace('\n', '\\r\\n')

    # Try inserting before target marker
    target = cfg["insert_before"]
    fallback = cfg.get("fallback_insert_before")

    target_idx = content.find(target)
    if target_idx == -1 and fallback:
        target_idx = content.find(fallback)

    if target_idx != -1:
        new_content = content[:target_idx] + formatted_sec + content[target_idx:]
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Success: Injected video showcase into {cfg['file']}")
    else:
        # Try finding </section> before footer
        idx_footer = content.find("main-footer")
        if idx_footer != -1:
            idx_prev_sec = content.rfind("<section", 0, idx_footer)
            if idx_prev_sec != -1:
                new_content = content[:idx_prev_sec] + formatted_sec + content[idx_prev_sec:]
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Success: Injected video showcase into {cfg['file']} (before section near footer)")
            else:
                print(f"Warning: Could not find insert spot in {cfg['file']}")
        else:
            print(f"Warning: Could not find insert spot in {cfg['file']}")

if __name__ == "__main__":
    for cfg in CATEGORY_CONFIGS:
        process_page(cfg)
