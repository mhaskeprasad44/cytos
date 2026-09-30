import os, re

with open("src/data/blogData.js", "r", encoding="utf-8") as f:
    txt = f.read()

items = re.findall(r'"slug":\s*"([^"]+)",\s*"title":\s*"([^"]+)",.*?"category":\s*"([^"]+)"', txt, re.DOTALL)
print(f"Total blogs found: {len(items)}")
for i, (s, t, c) in enumerate(items, 1):
    print(f"{i:02d}. [{c}] {s}")
    print(f"    {t}")
