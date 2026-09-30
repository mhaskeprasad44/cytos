# -*- coding: utf-8 -*-
"""
update_all_dropdowns_and_footers.py
Updates the Automation & SPM navigation menu across all pages:
- Custom Turnkey SPMs -> spm-automation.html
- Robotic Dispensing Cells -> robotic-dispensing-cells.html
- Pneumatic Welding Fixtures -> pneumatic-welding-fixtures.html
- PLC Industrial Control Panels -> plc-control-panels.html
Also updates footers and sitemap.xml.
"""

import os
import re
import glob

PROJECT_DIR = r"c:\Users\PrasadMhaske\Downloads\Project1"

# 1. Update blog_generator_core.py
core_file = os.path.join(PROJECT_DIR, "blog_generator_core.py")
with open(core_file, "r", encoding="utf-8") as f:
    core_content = f.read()

core_content = core_content.replace(
    'href="../spm-automation.html#robotic-dispensing"',
    'href="../robotic-dispensing-cells.html"'
)
core_content = core_content.replace(
    'href="../spm-automation.html#welding-fixtures"',
    'href="../pneumatic-welding-fixtures.html"'
)
core_content = core_content.replace(
    'href="../spm-automation.html#control-panels"',
    'href="../plc-control-panels.html"'
)

with open(core_file, "w", encoding="utf-8") as f:
    f.write(core_content)
print("Updated blog_generator_core.py dropdown links")

# 2. Update all Root HTML pages
root_pages = glob.glob(os.path.join(PROJECT_DIR, "*.html"))
for fpath in root_pages:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    orig = content
    content = content.replace(
        'href="spm-automation.html#robotic-dispensing"',
        'href="robotic-dispensing-cells.html"'
    )
    content = content.replace(
        'href="spm-automation.html#welding-fixtures"',
        'href="pneumatic-welding-fixtures.html"'
    )
    content = content.replace(
        'href="spm-automation.html#control-panels"',
        'href="plc-control-panels.html"'
    )

    # In footer machine solutions, ensure all 4 are listed
    old_footer_machines = """          <ul class="footer-nav-list">
            <li><a href="pcb-drilling-routing.html">PCB Production Drilling &amp; Routing</a></li>
            <li><a href="pcb-prototyping.html">Chemical-Free PCB Prototyping</a></li>
            <li><a href="cnc-routers-milling.html">4x4 &amp; 8x8 Industrial CNC Routers</a></li>
            <li><a href="vdm-milling.html">VDM Multi-Spindle Milling</a></li>
            <li><a href="spm-automation.html">Custom Turnkey SPMs &amp; Robotics</a></li>
          </ul>"""

    new_footer_machines = """          <ul class="footer-nav-list">
            <li><a href="pcb-drilling-routing.html">PCB Production Drilling &amp; Routing</a></li>
            <li><a href="pcb-prototyping.html">Chemical-Free PCB Prototyping</a></li>
            <li><a href="cnc-routers-milling.html">4x4 &amp; 8x8 Industrial CNC Routers</a></li>
            <li><a href="vdm-milling.html">VDM Multi-Spindle Milling</a></li>
            <li><a href="spm-automation.html">Custom Turnkey SPMs</a></li>
            <li><a href="robotic-dispensing-cells.html">Robotic Dispensing Cells</a></li>
            <li><a href="pneumatic-welding-fixtures.html">Pneumatic Welding Fixtures</a></li>
            <li><a href="plc-control-panels.html">PLC Industrial Control Panels</a></li>
          </ul>"""

    if old_footer_machines in content:
        content = content.replace(old_footer_machines, new_footer_machines)

    if content != orig:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated dropdown & footer in {os.path.basename(fpath)}")

# 3. Update all Blog HTML files
blog_pages = glob.glob(os.path.join(PROJECT_DIR, "blog", "*.html")) + glob.glob(os.path.join(PROJECT_DIR, "blog", "*", "index.html"))
for fpath in blog_pages:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    orig = content
    # For blog/*.html
    content = content.replace(
        'href="../spm-automation.html#robotic-dispensing"',
        'href="../robotic-dispensing-cells.html"'
    )
    content = content.replace(
        'href="../spm-automation.html#welding-fixtures"',
        'href="../pneumatic-welding-fixtures.html"'
    )
    content = content.replace(
        'href="../spm-automation.html#control-panels"',
        'href="../plc-control-panels.html"'
    )
    # For blog/*/index.html
    content = content.replace(
        'href="../../spm-automation.html#robotic-dispensing"',
        'href="../../robotic-dispensing-cells.html"'
    )
    content = content.replace(
        'href="../../spm-automation.html#welding-fixtures"',
        'href="../../pneumatic-welding-fixtures.html"'
    )
    content = content.replace(
        'href="../../spm-automation.html#control-panels"',
        'href="../../plc-control-panels.html"'
    )

    if content != orig:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

print(f"Updated {len(blog_pages)} blog files.")

# 4. Update spm-automation.html specifically to link cards to dedicated pages
spm_path = os.path.join(PROJECT_DIR, "spm-automation.html")
with open(spm_path, "r", encoding="utf-8") as f:
    spm_c = f.read()

# Make pillar card 1 have id="robotic-dispensing" and link to robotic-dispensing-cells.html
spm_c = spm_c.replace(
    '<!-- Pillar 1: Robotic Cells -->\n        <article class="model-card">',
    '<!-- Pillar 1: Robotic Cells -->\n        <article class="model-card" id="robotic-dispensing">\n          <div style="background: rgba(37,99,235,0.08); padding: 4px 8px; border-radius: 4px; font-size: 0.76rem; font-weight: 700; color: #1d4ed8; margin-bottom: 0.5rem; text-align: center;">DEDICATED AUTOMOTIVE CELL</div>'
)
spm_c = spm_c.replace(
    '<button class="btn btn-primary btn-block" data-open-rfq data-machine="Robotic SPM Cell">Quote Robotic Cell</button>',
    '<a href="robotic-dispensing-cells.html" class="btn btn-primary btn-block" style="text-align: center; text-decoration: none;">View Robotic Dispensing Specs</a>'
)

# Make pillar card 2 have id="welding-fixtures" and link to pneumatic-welding-fixtures.html
spm_c = spm_c.replace(
    '<!-- Pillar 2: Pneumatic Fixtures -->\n        <article class="model-card">',
    '<!-- Pillar 2: Pneumatic Fixtures -->\n        <article class="model-card" id="welding-fixtures">\n          <div style="background: rgba(217,119,6,0.08); padding: 4px 8px; border-radius: 4px; font-size: 0.76rem; font-weight: 700; color: var(--brand-gold-dark); margin-bottom: 0.5rem; text-align: center;">90° ROTARY TURNOVER JIGS</div>'
)
spm_c = spm_c.replace(
    '<button class="btn btn-primary btn-block" data-open-rfq data-machine="Pneumatic Welding Fixture">Quote Fixture</button>',
    '<a href="pneumatic-welding-fixtures.html" class="btn btn-primary btn-block" style="text-align: center; text-decoration: none;">View Welding Fixture Specs</a>'
)

# Make pillar card 3 have id="control-panels" and link to plc-control-panels.html
spm_c = spm_c.replace(
    '<!-- Pillar 3: Control Panels -->\n        <article class="model-card" id="panels">',
    '<!-- Pillar 3: Control Panels -->\n        <article class="model-card" id="control-panels">\n          <div style="background: rgba(16,185,129,0.08); padding: 4px 8px; border-radius: 4px; font-size: 0.76rem; font-weight: 700; color: #059669; margin-bottom: 0.5rem; text-align: center;">SIEMENS &amp; DELTA ENCLOSURES</div>'
)
spm_c = spm_c.replace(
    '<button class="btn btn-primary btn-block" data-open-rfq data-machine="Industrial Control Panel">Quote Control Panel</button>',
    '<a href="plc-control-panels.html" class="btn btn-primary btn-block" style="text-align: center; text-decoration: none;">View Control Panel Specs</a>'
)

with open(spm_path, "w", encoding="utf-8") as f:
    f.write(spm_c)
print("Updated spm-automation.html cards with dedicated page links & anchors")

# 5. Update sitemap.xml with the new pages
sitemap_path = os.path.join(PROJECT_DIR, "sitemap.xml")
if os.path.exists(sitemap_path):
    with open(sitemap_path, "r", encoding="utf-8") as f:
        sitemap_c = f.read()

    new_urls = """  <url>
    <loc>https://cytos.in/robotic-dispensing-cells.html</loc>
    <lastmod>2026-09-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>
  <url>
    <loc>https://cytos.in/pneumatic-welding-fixtures.html</loc>
    <lastmod>2026-09-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>
  <url>
    <loc>https://cytos.in/plc-control-panels.html</loc>
    <lastmod>2026-09-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>
</urlset>"""

    if "robotic-dispensing-cells.html" not in sitemap_c:
        sitemap_c = sitemap_c.replace("</urlset>", new_urls)
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(sitemap_c)
        print("Added new automation pages to sitemap.xml")

print("All updates completed successfully!")
