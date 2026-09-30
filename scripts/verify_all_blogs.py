import os, re

with open("src/data/allBlogsHtml.js", "r", encoding="utf-8") as f:
    txt = f.read()

# find keys: '  "slug": {'
keys = re.findall(r'^\s*\"([a-z0-9\-]+)\":\s*\{', txt, re.MULTILINE)
print(f"Total keys in allBlogsHtml: {len(keys)}")
for k in keys:
    print("  ", k)
