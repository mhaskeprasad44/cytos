import os

ROOT = r"c:\Users\PrasadMhaske\Downloads\Project1"
PAGES_DIR = os.path.join(ROOT, "src", "pages")

pages = ['AboutPage.jsx', 'CncRoutersPage.jsx', 'PcbDrillingPage.jsx', 'PcbPrototypingPage.jsx', 'SpmAutomationPage.jsx']

for p in pages:
    path = os.path.join(PAGES_DIR, p)
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # If unescaped attributes are found, escape them
    # Specifically target the injected citations
    replacements = [
        # ISO / IMTMA
        ('<a href="https://www.iso.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;">ISO 9001:2015</a>',
         '<a href=\\"https://www.iso.org/\\" target=\\"_blank\\" rel=\\"noopener\\" style=\\"color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;\\">ISO 9001:2015</a>'),
        
        ('<a href="https://www.imtma.in/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;">Make in India (IMTMA Aligned)</a>',
         '<a href=\\"https://www.imtma.in/\\" target=\\"_blank\\" rel=\\"noopener\\" style=\\"color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;\\">Make in India (IMTMA Aligned)</a>'),

        # CNC Routers
        ('<a href="https://www.asminternational.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;">6061-T6 Aluminium</a>',
         '<a href=\\"https://www.asminternational.org/\\" target=\\"_blank\\" rel=\\"noopener\\" style=\\"color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;\\">6061-T6 Aluminium</a>'),

        ('<a href="https://www.iso.org/standard/43204.html" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;">Laser Aligned Gantry (ISO 230-2)</a>',
         '<a href=\\"https://www.iso.org/standard/43204.html\\" target=\\"_blank\\" rel=\\"noopener\\" style=\\"color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;\\">Laser Aligned Gantry (ISO 230-2)</a>'),

        # PCB Drilling
        ('<a href="https://www.iso.org/standard/41258.html" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;">Dynamic Balancing ISO 1940 G0.4</a>',
         '<a href=\\"https://www.iso.org/standard/41258.html\\" target=\\"_blank\\" rel=\\"noopener\\" style=\\"color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;\\">Dynamic Balancing ISO 1940 G0.4</a>'),

        ('<a href="https://www.ipc.org/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;">0.2mm Micro-Drilling (IPC-A-600 Class 3)</a>',
         '<a href=\\"https://www.ipc.org/\\" target=\\"_blank\\" rel=\\"noopener\\" style=\\"color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;\\">0.2mm Micro-Drilling (IPC-A-600 Class 3)</a>'),

        # PCB Prototyping
        ('Direct <a href="https://www.ucamco.com/en/gerber" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;">Gerber RS-274X / X3 (Ucamco)</a>',
         'Direct <a href=\\"https://www.ucamco.com/en/gerber\\" target=\\"_blank\\" rel=\\"noopener\\" style=\\"color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;\\">Gerber RS-274X / X3 (Ucamco)</a>'),

        ('<a href="https://www.iso.org/iso-14001-environmental-management.html" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;">Chemical-Free Isolation (ISO 14001 Safe)</a>',
         '<a href=\\"https://www.iso.org/iso-14001-environmental-management.html\\" target=\\"_blank\\" rel=\\"noopener\\" style=\\"color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;\\">Chemical-Free Isolation (ISO 14001 Safe)</a>'),

        # SPM Automation
        ('<a href="https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.212" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;">Safety Factor 2.0 Automation (OSHA 1910.212)</a>',
         '<a href=\\"https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.212\\" target=\\"_blank\\" rel=\\"noopener\\" style=\\"color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;\\">Safety Factor 2.0 Automation (OSHA 1910.212)</a>'),

        ('<a href="https://www.iec.ch/" target="_blank" rel="noopener" style="color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;">Siemens / Delta (IEC 60204-1 Compliant)</a>',
         '<a href=\\"https://www.iec.ch/\\" target=\\"_blank\\" rel=\\"noopener\\" style=\\"color: var(--brand-gold-dark); text-decoration: underline; font-weight: 600;\\">Siemens / Delta (IEC 60204-1 Compliant)</a>')
    ]

    modified = False
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            modified = True
            print(f"Fixed quotes in {p}: {old[:40]}...")

    if modified:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved {p}")
