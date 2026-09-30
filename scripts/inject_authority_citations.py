import os
import re

ROOT = r"c:\Users\PrasadMhaske\Downloads\Project1"
SRC = os.path.join(ROOT, "src")
BLOG_HTML_PATH = os.path.join(SRC, "data", "allBlogsHtml.js")
PAGES_DIR = os.path.join(SRC, "pages")

# Style for authority links
A_STYLE = 'style=\\"color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;\\"'
A_STYLE_PAGES = 'style="color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;"'

def enhance_blogs():
    with open(BLOG_HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Metrology Section Citations (applies to all 22 articles)
    # (ISO 230-2 Standards) -> ISO 230-2 Standards with link
    content = re.sub(
        r'\(ISO 230-2 Standards\)',
        rf'(<a href=\\"https://www.iso.org/standard/43204.html\\" target=\\"_blank\\" rel=\\"noopener\\" {A_STYLE}>ISO 230-2 Standards</a>)',
        content
    )

    # ISO 8573-1 Class 1.4.1 / 1.2.1
    content = re.sub(
        r'ISO 8573-1 Class (1\.[24]\.1)',
        rf'<a href=\\"https://www.iso.org/standard/44273.html\\" target=\\"_blank\\" rel=\\"noopener\\" {A_STYLE}>ISO 8573-1 Class \1 Standards</a>',
        content
    )

    # ISO 1940 Grade G0.4 / ISO 10816 Class G0.4
    content = re.sub(
        r'ISO (?:1940 Grade|10816 Class) G0\.4',
        rf'<a href=\\"https://www.iso.org/standard/41258.html\\" target=\\"_blank\\" rel=\\"noopener\\" {A_STYLE}>ISO 1940 Grade G0.4 Rotor Balance Standards</a>',
        content
    )

    # Multi-axis laser interferometers -> NIST
    content = re.sub(
        r'multi-axis laser interferometers\.',
        rf'multi-axis laser interferometers calibrated to <a href=\\"https://www.nist.gov/\\" target=\\"_blank\\" rel=\\"noopener\\" {A_STYLE}>NIST Dimensional Metrology Standards</a>.',
        content
    )

    # 2. PCB / Gerber / IPC Citations
    # Gerber RS-274X -> Ucamco Gerber
    # Let's replace only instances not already inside a tag
    content = re.sub(
        r'Gerber RS-274X(?!<|</a>|\\"|")',
        rf'<a href=\\"https://www.ucamco.com/en/gerber\\" target=\\"_blank\\" rel=\\"noopener\\" {A_STYLE}>Gerber RS-274X</a>',
        content,
        count=22
    )

    # IPC-2221
    content = re.sub(
        r'IPC-2221(?!<|</a>|\\"|")',
        rf'<a href=\\"https://www.ipc.org/\\" target=\\"_blank\\" rel=\\"noopener\\" {A_STYLE}>IPC-2221 Standards</a>',
        content,
        count=15
    )

    # IPC-A-600
    content = re.sub(
        r'IPC-A-600(?!<|</a>|\\"|")',
        rf'<a href=\\"https://www.ipc.org/\\" target=\\"_blank\\" rel=\\"noopener\\" {A_STYLE}>IPC-A-600 Acceptability Standards</a>',
        content,
        count=15
    )

    # ISO 14001
    content = re.sub(
        r'ISO 14001(?!<|</a>|\\"|")',
        rf'<a href=\\"https://www.iso.org/iso-14001-environmental-management.html\\" target=\\"_blank\\" rel=\\"noopener\\" {A_STYLE}>ISO 14001 Clean Lab Standards</a>',
        content,
        count=10
    )

    # 3. Aluminium & Metallurgy Citations
    content = re.sub(
        r'6061-T6(?!<|</a>|\\"|")',
        rf'<a href=\\"https://www.asminternational.org/\\" target=\\"_blank\\" rel=\\"noopener\\" {A_STYLE}>6061-T6 Aluminium</a>',
        content,
        count=8
    )

    # 4. Automation & Safety Citations
    content = re.sub(
        r'Category 4 safety (?:circuits|relays|architecture)(?!<|</a>|\\"|")',
        rf'Category 4 safety architecture compliant with <a href=\\"https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.212\\" target=\\"_blank\\" rel=\\"noopener\\" {A_STYLE}>OSHA 1910.212 Machine Safety Standards</a>',
        content,
        count=10
    )

    # IEC 60204-1
    content = re.sub(
        r'IEC 60204-1(?!<|</a>|\\"|")',
        rf'<a href=\\"https://www.iec.ch/\\" target=\\"_blank\\" rel=\\"noopener\\" {A_STYLE}>IEC 60204-1 Industrial Machinery Electrical Safety Standard</a>',
        content,
        count=10
    )

    with open(BLOG_HTML_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("Updated allBlogsHtml.js with high authority dofollow external links!")

def enhance_pages():
    # 1. PcbDrillingPage.jsx
    pcb_page = os.path.join(PAGES_DIR, "PcbDrillingPage.jsx")
    if os.path.exists(pcb_page):
        with open(pcb_page, "r", encoding="utf-8") as f:
            p_content = f.read()
        p_content = p_content.replace(
            "Dynamic Balancing G0.4",
            f'<a href="https://www.iso.org/standard/41258.html" target="_blank" rel="noopener" {A_STYLE_PAGES}>Dynamic Balancing ISO 1940 G0.4</a>'
        )
        p_content = p_content.replace(
            "0.2mm Micro-Drilling",
            f'<a href="https://www.ipc.org/" target="_blank" rel="noopener" {A_STYLE_PAGES}>0.2mm Micro-Drilling (IPC-A-600 Class 3)</a>'
        )
        with open(pcb_page, "w", encoding="utf-8") as f:
            f.write(p_content)
        print("Enhanced PcbDrillingPage.jsx with authoritative citations!")

    # 2. PcbPrototypingPage.jsx
    proto_page = os.path.join(PAGES_DIR, "PcbPrototypingPage.jsx")
    if os.path.exists(proto_page):
        with open(proto_page, "r", encoding="utf-8") as f:
            p_content = f.read()
        p_content = p_content.replace(
            "Direct Gerber RS-274X",
            f'Direct <a href="https://www.ucamco.com/en/gerber" target="_blank" rel="noopener" {A_STYLE_PAGES}>Gerber RS-274X / X3 (Ucamco)</a>'
        )
        p_content = p_content.replace(
            "Chemical-Free Isolation",
            f'<a href="https://www.iso.org/iso-14001-environmental-management.html" target="_blank" rel="noopener" {A_STYLE_PAGES}>Chemical-Free Isolation (ISO 14001 Safe)</a>'
        )
        with open(proto_page, "w", encoding="utf-8") as f:
            f.write(p_content)
        print("Enhanced PcbPrototypingPage.jsx with authoritative citations!")

    # 3. CncRoutersPage.jsx
    router_page = os.path.join(PAGES_DIR, "CncRoutersPage.jsx")
    if os.path.exists(router_page):
        with open(router_page, "r", encoding="utf-8") as f:
            p_content = f.read()
        p_content = p_content.replace(
            "6061-T6",
            f'<a href="https://www.asminternational.org/" target="_blank" rel="noopener" {A_STYLE_PAGES}>6061-T6 Aluminium</a>'
        )
        p_content = p_content.replace(
            "Laser Aligned Gantry",
            f'<a href="https://www.iso.org/standard/43204.html" target="_blank" rel="noopener" {A_STYLE_PAGES}>Laser Aligned Gantry (ISO 230-2)</a>'
        )
        with open(router_page, "w", encoding="utf-8") as f:
            f.write(p_content)
        print("Enhanced CncRoutersPage.jsx with authoritative citations!")

    # 4. SpmAutomationPage.jsx
    spm_page = os.path.join(PAGES_DIR, "SpmAutomationPage.jsx")
    if os.path.exists(spm_page):
        with open(spm_page, "r", encoding="utf-8") as f:
            p_content = f.read()
        p_content = p_content.replace(
            "Safety Factor 2.0 Automation",
            f'<a href="https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.212" target="_blank" rel="noopener" {A_STYLE_PAGES}>Safety Factor 2.0 Automation (OSHA 1910.212)</a>'
        )
        p_content = p_content.replace(
            "Siemens / Delta",
            f'<a href="https://www.iec.ch/" target="_blank" rel="noopener" {A_STYLE_PAGES}>Siemens / Delta (IEC 60204-1 Compliant)</a>'
        )
        with open(spm_page, "w", encoding="utf-8") as f:
            f.write(p_content)
        print("Enhanced SpmAutomationPage.jsx with authoritative citations!")

    # 5. AboutPage.jsx
    about_page = os.path.join(PAGES_DIR, "AboutPage.jsx")
    if os.path.exists(about_page):
        with open(about_page, "r", encoding="utf-8") as f:
            p_content = f.read()
        p_content = p_content.replace(
            "ISO 9001:2015",
            f'<a href="https://www.iso.org/" target="_blank" rel="noopener" {A_STYLE_PAGES}>ISO 9001:2015</a>'
        )
        p_content = p_content.replace(
            "Make in India",
            f'<a href="https://www.imtma.in/" target="_blank" rel="noopener" {A_STYLE_PAGES}>Make in India (IMTMA Aligned)</a>'
        )
        with open(about_page, "w", encoding="utf-8") as f:
            f.write(p_content)
        print("Enhanced AboutPage.jsx with authoritative citations!")

enhance_blogs()
enhance_pages()
