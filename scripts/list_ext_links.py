import os, re

SRC = "src"
href_pattern = re.compile(r'href=(?:\\?["\'])(https?://[^"\'\\]+)(?:\\?["\'])')
links = {}
for root, dirs, files in os.walk(SRC):
    for fn in files:
        if fn.endswith((".jsx", ".js")):
            with open(os.path.join(root, fn), "r", encoding="utf-8", errors="ignore") as f:
                c = f.read()
            for m in href_pattern.findall(c):
                links[m] = links.get(m, 0) + 1

print(f"Total distinct external links: {len(links)}")
for l, cnt in sorted(links.items()):
    if "wa.me" not in l and "google" not in l and "schema.org" not in l:
        print(f"  {l} ({cnt} citations)")
