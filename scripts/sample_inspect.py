import os, re

with open("src/data/allBlogsHtml.js", "r", encoding="utf-8") as f:
    content = f.read()

slugs = ["chemical-free-pcb-rapid-prototyping-machine", "gerber-to-pcb-isolation-milling-guide", "special-purpose-machines-spm-guide"]

for s in slugs:
    m = re.search(rf'"{s}":\s*\{{(.*?)\n  \}}', content, re.DOTALL)
    if m:
        txt = m.group(1)
        # Find all h2 and h3
        headers = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', txt)
        print(f"\n=== Article: {s} ===")
        for h in headers[:6]:
            print("  Header:", h)
        # Find first paragraph
        p = re.search(r'<p>(.*?)</p>', txt)
        if p:
            print("  First P:", p.group(1)[:120], "...")
