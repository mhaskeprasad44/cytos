import os
import re

ROOT = r"c:\Users\PrasadMhaske\Downloads\Project1"
SRC = os.path.join(ROOT, "src")
PAGES_DIR = os.path.join(SRC, "pages")
BLOG_HTML_PATH = os.path.join(SRC, "data", "allBlogsHtml.js")

# List of relative html replacements to clean SPA routes
HTML_REPLACEMENTS = [
    # Specific anchors first
    (r'applications\.html#composites', '/applications#composites'),
    (r'applications\.html#mcpcb', '/applications#mcpcb'),
    (r'applications\.html#multilayer-pcb', '/applications#multilayer-pcb'),
    (r'case-studies\.html#welding-fixtures', '/case-studies#welding-fixtures'),
    (r'pcb-prototyping\.html#educational-lab', '/pcb-prototyping#educational-lab'),
    (r'cnc-routers-milling\.html#vdm-heavy-milling', '/vdm-milling'),
    (r'contact\.html#visit', '/contact'),
    (r'index\.html#pillars', '/#pillars'),
    (r'spm-automation\.html#control-panels', '/plc-control-panels'),
    (r'spm-automation\.html#robotic-dispensing', '/robotic-dispensing-cells'),
    (r'spm-automation\.html#welding-fixtures', '/pneumatic-welding-fixtures'),
    
    # Generic .html page links
    (r'about\.html', '/about'),
    (r'applications\.html', '/applications'),
    (r'blog\.html', '/blog'),
    (r'case-studies\.html', '/case-studies'),
    (r'cnc-routers-milling\.html', '/cnc-routers-milling'),
    (r'contact\.html', '/contact'),
    (r'pcb-drilling-routing\.html', '/pcb-drilling-routing'),
    (r'pcb-prototyping\.html', '/pcb-prototyping'),
    (r'plc-control-panels\.html', '/plc-control-panels'),
    (r'pneumatic-welding-fixtures\.html', '/pneumatic-welding-fixtures'),
    (r'privacy-policy\.html', '/privacy-policy'),
    (r'robotic-dispensing-cells\.html', '/robotic-dispensing-cells'),
    (r'spm-automation\.html', '/spm-automation'),
    (r'terms-conditions\.html', '/terms-conditions'),
    (r'vdm-milling\.html', '/vdm-milling'),
    (r'index\.html', '/'),
]

def fix_jsx_pages():
    for fn in os.listdir(PAGES_DIR):
        if not fn.endswith(".jsx"):
            continue
        fp = os.path.join(PAGES_DIR, fn)
        with open(fp, "r", encoding="utf-8") as f:
            content = f.read()

        orig = content

        # 1. Update logo to CyTOS New Logo
        content = content.replace('src=\\"/Logo.png\\"', 'src=\\"/CyTOS New Logo.png\\"')
        content = content.replace('src=\\"/Logo-footer.png\\"', 'src=\\"/CyTOS New Logo.png\\"')
        content = content.replace('src=\\"/Logo-cropped.png\\"', 'src=\\"/CyTOS New Logo.png\\"')
        content = content.replace('src="/Logo.png"', 'src="/CyTOS New Logo.png"')
        content = content.replace('src="/Logo-footer.png"', 'src="/CyTOS New Logo.png"')
        content = content.replace('src="/Logo-cropped.png"', 'src="/CyTOS New Logo.png"')

        # 2. Fix home/index
        content = content.replace('href=\\"/index\\"', 'href=\\"/\\"')
        content = content.replace('href="/index"', 'href="/"')

        # 3. Apply all HTML replacements
        for pattern, repl in HTML_REPLACEMENTS:
            # Handle both escaped and unescaped quotes
            content = re.sub(rf'(href|to)=(["\']|\\+["\']){pattern}(["\']|\\+["\'])', rf'\1=\2{repl}\3', content)

        if content != orig:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated JSX page: {fn}")

fix_jsx_pages()
