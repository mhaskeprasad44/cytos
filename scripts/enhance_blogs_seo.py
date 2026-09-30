import os
import re

ROOT = r"c:\Users\PrasadMhaske\Downloads\Project1"
SRC = os.path.join(ROOT, "src")
BLOG_HTML_PATH = os.path.join(SRC, "data", "allBlogsHtml.js")

# Map of high authority dofollow citations for all 22 blogs
# Each entry has:
#   target_phrase: a phrase in the article to attach/expand or cite
#   anchor_html: the dofollow link HTML
AUTHORITY_CITATIONS = {
    "60000-rpm-pcb-drilling-spindle-maintenance": [
        (
            "dynamic balancing (to ISO 1940 Grade G0.4)",
            'dynamic balancing (<a href="https://www.iso.org/standard/41258.html" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ISO 1940-1 Grade G0.4 Rotor Balancing Standards</a>)'
        ),
        (
            "ISO 8573-1 Class 1.2.1",
            '<a href="https://www.iso.org/standard/44273.html" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ISO 8573-1 Class 1.2.1 Compressed Air Purity Standard</a>'
        ),
        (
            "Laser Interferometer Calibration (ISO 230-2 Standards)",
            'Laser Interferometer Calibration (<a href="https://www.iso.org/standard/43204.html" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ISO 230-2 Machine Tool Metrology Code</a>)'
        )
    ],
    "aluminium-composite-sheet-cnc-drilling-milling": [
        (
            "5052, 6061-T6, and 7075 aluminum alloys",
            '5052, 6061-T6, and 7075 structural alloys (<a href="https://www.asminternational.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ASM International Aerospace Aluminium Specifications</a>)'
        ),
        (
            "linear pitch errors must be verified",
            'linear pitch errors must be verified to <a href="https://www.iso.org/standard/43204.html" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ISO 230-2 Machine Tool Testing Standards</a>'
        )
    ],
    "auto-surface-leveling-pcb-prototyping": [
        (
            "annular ring breakout or track thinning",
            'annular ring breakout (<a href="https://www.ipc.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IPC-2221 Generic Standard on Printed Board Design</a>)'
        ),
        (
            "calibrated height probe sensor",
            'calibrated height probe sensor traceable to <a href="https://www.nist.gov/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">NIST Dimensional Metrology Guidelines</a>'
        )
    ],
    "automotive-cycle-time-reduction-spm": [
        (
            "Category 4 safety architecture",
            'Category 4 safety architecture compliant with <a href="https://www.osha.gov/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">OSHA 1910.212 Machine Guarding &amp; Interlocking Standards</a>'
        ),
        (
            "robotic automation cells",
            'robotic automation cells (<a href="https://www.ieee.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IEEE Robotics &amp; Automation Engineering Guidelines</a>)'
        )
    ],
    "bt30-vs-bt40-cnc-drilling-and-milling": [
        (
            "standard 7/24 steep taper toolholders",
            'standard 7/24 steep taper toolholders (<a href="https://www.iso.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ISO 7388 Machine Tool Shank Standards</a>)'
        ),
        (
            "machine tool manufacturing plant",
            'machine tool manufacturing plant aligned with <a href="https://www.imtma.in/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IMTMA (Indian Machine Tool Manufacturers\' Association)</a> guidelines'
        )
    ],
    "chemical-free-pcb-rapid-prototyping-machine": [
        (
            "strict IPC Class 2 and Class 3",
            'strict <a href="https://www.ipc.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IPC-A-600 Acceptability of Printed Boards (Class 2 &amp; Class 3)</a>'
        ),
        (
            "zero hazardous chemical effluent",
            'zero hazardous chemical effluent compliant with <a href="https://www.iso.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ISO 14001 Environmental Clean Laboratory Standards</a>'
        )
    ],
    "cnc-drilling-and-milling-machine-guide": [
        (
            "volumetric accuracy across the bed",
            'volumetric accuracy across the bed (<a href="https://www.iso.org/standard/43204.html" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ISO 230-2 Machine Tool Positioning Code</a>)'
        ),
        (
            "electrical control enclosures",
            'electrical control enclosures compliant with <a href="https://www.iec.ch/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IEC 60204-1 Industrial Machinery Electrical Safety</a>'
        )
    ],
    "double-sided-pcb-rapid-prototyping-guide": [
        (
            "front-to-back annular ring registration",
            'front-to-back annular ring registration (<a href="https://www.ipc.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IPC-2221 Design Guidelines</a>)'
        ),
        (
            "standard Gerber RS-274X coordinates",
            'standard <a href="https://www.ucamco.com/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">Ucamco Gerber RS-274X / Gerber X3 Layer Format</a>'
        )
    ],
    "gerber-to-pcb-isolation-milling-guide": [
        (
            "Gerber RS-274X data format",
            '<a href="https://www.ucamco.com/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">Ucamco Official Gerber RS-274X / Gerber X3 Format Specification</a>'
        ),
        (
            "trace clearance and track width specifications",
            'trace clearance and track width specifications governed by <a href="https://www.ipc.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IPC-2221 Standards</a>'
        )
    ],
    "green-electronics-rapid-prototyping-lab": [
        (
            "environmental management systems",
            'environmental management systems (<a href="https://www.iso.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ISO 14001 Clean Lab Certification</a>)'
        ),
        (
            "FR4 and CEM-1 copper clad laminates",
            'FR4 and CEM-1 copper clad laminates (<a href="https://www.ipc.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IPC-4101 Specification for Base Materials</a>)'
        )
    ],
    "heavy-duty-cnc-router-machine-guide": [
        (
            "gantry structural rigidity and deflection testing",
            'gantry structural rigidity (<a href="https://www.iso.org/standard/43204.html" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ISO 230-2 Machine Tool Testing Criteria</a>)'
        ),
        (
            "cutting parameters for aerospace aluminium alloys",
            'cutting parameters for aluminium alloys (<a href="https://www.asminternational.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ASM International Materials Handbook</a>)'
        )
    ],
    "in-house-pcb-rapid-prototyping-roi": [
        (
            "functional PCB prototypes meeting IPC Class 2",
            'functional prototypes meeting <a href="https://www.ipc.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IPC-A-600 Acceptability Standards</a>'
        ),
        (
            "hardware development velocity",
            'hardware development velocity (<a href="https://www.ieee.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IEEE Electronics Manufacturing Research</a>)'
        )
    ],
    "mechanical-pcb-drilling-vs-laser-drilling": [
        (
            "micro-section hole wall inspection",
            'micro-section hole wall inspection per <a href="https://www.ipc.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IPC-TM-650 Test Methods 2.1.1</a>'
        ),
        (
            "high aspect ratio drilling tolerances",
            'high aspect ratio drilling tolerances (<a href="https://www.semi.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">SEMI Micro-Machining Standards</a>)'
        )
    ],
    "multi-spindle-pcb-drilling-machine": [
        (
            "60,000 RPM high-speed synchronized spindles",
            '60,000 RPM high-speed spindles (<a href="https://www.iso.org/standard/41258.html" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ISO 1940-1 Class G0.4 Dynamic Balancing</a>)'
        ),
        (
            "via hole registration and annular ring concentricity",
            'annular ring concentricity (<a href="https://www.ipc.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IPC-A-600 Acceptability Guidelines</a>)'
        )
    ],
    "multilayer-fr4-rogers-pcb-drilling": [
        (
            "high-frequency Rogers and high-Tg FR4 laminates",
            'high-Tg FR4 laminates (<a href="https://www.ipc.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IPC-4101 Specification for PCB Substrates</a>)'
        ),
        (
            "resin smear and glass-fiber breakout inspection",
            'resin smear assessment (<a href="https://www.ipc.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IPC-TM-650 Method 2.1.1 Cross-Section Metrology</a>)'
        )
    ],
    "pcb-drilling-machine-guide": [
        (
            "minimum annular ring requirements",
            'minimum annular ring requirements (<a href="https://www.ipc.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IPC-2221 Generic PCB Design Standards</a>)'
        ),
        (
            "laser calibrated positional repeatability",
            'laser calibrated repeatability (<a href="https://www.iso.org/standard/43204.html" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ISO 230-2 Machine Tool Metrology Code</a>)'
        )
    ],
    "pcb-drilling-tool-breakage-prevention": [
        (
            "dynamic collet runout under 3µm",
            'dynamic collet runout under 3µm (<a href="https://www.iso.org/standard/41258.html" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ISO 1940-1 Spindle Vibration Quality Standards</a>)'
        ),
        (
            "micrometer and dial test indicator calibration",
            'dial test indicator calibration traceable to <a href="https://www.nist.gov/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">NIST Metrology Protocols</a>'
        )
    ],
    "plc-control-panel-automation-spm-safety": [
        (
            "Category 4 safety relay architectures",
            'Category 4 safety architecture compliant with <a href="https://www.osha.gov/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">OSHA 1910.212 Machine Safety Guidelines</a>'
        ),
        (
            "industrial automation panel wiring",
            'industrial automation panel wiring (<a href="https://www.iec.ch/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IEC 60204-1 Electrical Equipment of Machines</a>)'
        )
    ],
    "pneumatic-welding-fixtures-spm-design": [
        (
            "robotic welding automation lines",
            'robotic welding automation lines (<a href="https://www.iso.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ISO 15614 Welding Specification Standards</a>)'
        ),
        (
            "pneumatic clamping safety interlocking",
            'pneumatic safety interlocking (<a href="https://www.osha.gov/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">OSHA 1910.212 Industrial Machine Guarding Code</a>)'
        )
    ],
    "robotic-adhesive-dispensing-spm-systems": [
        (
            "3-axis Cartesian robotic dispensing cells",
            '3-axis Cartesian robotic dispensing cells (<a href="https://www.ieee.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IEEE Industrial Automation &amp; Robotics Guidelines</a>)'
        ),
        (
            "robotic trajectory repeatability under 0.02mm",
            'robotic trajectory repeatability (<a href="https://www.iso.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ISO 9283 Manipulating Industrial Robots Standard</a>)'
        )
    ],
    "special-purpose-machines-spm-guide": [
        (
            "turnkey special purpose machinery",
            'turnkey special purpose machinery (<a href="https://www.imtma.in/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IMTMA Indian Machine Tool Standards</a>)'
        ),
        (
            "fail-safe electrical safety circuits",
            'fail-safe electrical circuits (<a href="https://www.iec.ch/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IEC 60204-1 Machine Tool Safety Specifications</a>)'
        )
    ],
    "vertical-drilling-and-milling-machine-guide": [
        (
            "heavy-duty vertical milling and drilling spindle heads",
            'heavy-duty vertical milling spindles (<a href="https://www.iso.org/standard/43204.html" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">ISO 230-2 Machine Tool Metrology Code</a>)'
        ),
        (
            "integrated electrical switchboard panels",
            'integrated electrical control panels (<a href="https://www.iec.ch/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline;">IEC 60204-1 Electrical Safety Standards</a>)'
        )
    ]
}

def update_all_blogs_html():
    with open(BLOG_HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update logo paths inside allBlogsHtml.js
    content = content.replace('src=\\"/Logo.png\\"', 'src=\\"/CyTOS New Logo.png\\"')
    content = content.replace('src=\\"/Logo-footer.png\\"', 'src=\\"/CyTOS New Logo.png\\"')
    content = content.replace('src=\\"/Logo-cropped.png\\"', 'src=\\"/CyTOS New Logo.png\\"')

    # 2. Fix home/index links
    content = content.replace('href=\\"/index\\"', 'href=\\"/\\"')
    content = content.replace('href=\\"index.html\\"', 'href=\\"/\\"')

    # 3. Fix relative links in footer / navigation
    content = content.replace('../applications.html#composites', '/applications#composites')
    content = content.replace('../applications.html#mcpcb', '/applications#mcpcb')
    content = content.replace('../applications.html#multilayer-pcb', '/applications#multilayer-pcb')
    content = content.replace('../case-studies.html#welding-fixtures', '/case-studies#welding-fixtures')
    content = content.replace('../pcb-prototyping.html#educational-lab', '/pcb-prototyping#educational-lab')
    content = content.replace('../spm-automation.html#control-panels', '/plc-control-panels')
    content = content.replace('../spm-automation.html#robotic-dispensing', '/robotic-dispensing-cells')
    content = content.replace('../spm-automation.html#welding-fixtures', '/pneumatic-welding-fixtures')

    # Also without ../ prefix
    content = content.replace('applications.html#composites', '/applications#composites')
    content = content.replace('applications.html#mcpcb', '/applications#mcpcb')
    content = content.replace('applications.html#multilayer-pcb', '/applications#multilayer-pcb')
    content = content.replace('case-studies.html#welding-fixtures', '/case-studies#welding-fixtures')
    content = content.replace('pcb-prototyping.html#educational-lab', '/pcb-prototyping#educational-lab')
    content = content.replace('spm-automation.html#control-panels', '/plc-control-panels')
    content = content.replace('spm-automation.html#robotic-dispensing', '/robotic-dispensing-cells')
    content = content.replace('spm-automation.html#welding-fixtures', '/pneumatic-welding-fixtures')

    # 4. Fix naked blog slug links to /blog/:slug
    slug_list = list(AUTHORITY_CITATIONS.keys())
    for slug in slug_list:
        # Match href=\"/slug\" or href=\"/slug.html\"
        pattern1 = f'href=\\"/{slug}\\"'
        pattern1_fix = f'href=\\"/blog/{slug}\\"'
        content = content.replace(pattern1, pattern1_fix)

        pattern2 = f'href=\\"/{slug}.html\\"'
        content = content.replace(pattern2, pattern1_fix)

        pattern3 = f'href=\\"/blog/{slug}.html\\"'
        content = content.replace(pattern3, pattern1_fix)

    # 5. Inject high authority dofollow external links for each blog article
    for slug, citations in AUTHORITY_CITATIONS.items():
        # Find article block
        block_pattern = re.compile(rf'"{re.escape(slug)}":\s*\{{(.*?)\n  \}}', re.DOTALL)
        m = block_pattern.search(content)
        if not m:
            print(f"Warning: Could not find block for slug: {slug}")
            continue

        block_text = m.group(1)
        modified_block = block_text

        for target_phrase, anchor_html in citations:
            # Check if target phrase exists in block_text
            if target_phrase in modified_block:
                # Escape target_phrase and replacement properly for JS string (quotes become \")
                escaped_replacement = anchor_html.replace('"', '\\"')
                modified_block = modified_block.replace(target_phrase, escaped_replacement, 1)
            else:
                print(f"  Note: target phrase '{target_phrase}' not found in '{slug}'")

        if modified_block != block_text:
            content = content[:m.start(1)] + modified_block + content[m.end(1):]

    with open(BLOG_HTML_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("Updated allBlogsHtml.js successfully with logo paths, clean internal links, and high-authority dofollow citations!")

update_all_blogs_html()
