import os
import re
import json

ROOT = r"c:\Users\PrasadMhaske\Downloads\Project1"
SRC = os.path.join(ROOT, "src")

valid_routes = {
    "/",
    "/about",
    "/applications",
    "/case-studies",
    "/cnc-routers-milling",
    "/contact",
    "/pcb-drilling-routing",
    "/pcb-prototyping",
    "/plc-control-panels",
    "/pneumatic-welding-fixtures",
    "/privacy-policy",
    "/robotic-dispensing-cells",
    "/spm-automation",
    "/terms-conditions",
    "/vdm-milling",
    "/blog"
}

with open(os.path.join(SRC, "data", "blogData.js"), "r", encoding="utf-8") as f:
    blog_data_txt = f.read()

slugs = re.findall(r'["\']slug["\']:\s*["\']([^"\']+)["\']', blog_data_txt)
for s in slugs:
    valid_routes.add(f"/blog/{s}")

slug_set = set(slugs)

target_files = []
for root, dirs, files in os.walk(SRC):
    for fn in files:
        if fn.endswith((".jsx", ".js")) and not fn.startswith("inspect_"):
            target_files.append(os.path.join(root, fn))

broken_internal_links = []
relative_html_links = []

href_pattern = re.compile(r'(?:href|to)=(?:\\?["\'])([^"\'\\]+)(?:\\?["\'])')

for file_path in target_files:
    rel_path = os.path.relpath(file_path, ROOT)
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    matches = href_pattern.findall(content)
    for target in matches:
        target = target.strip()
        if not target:
            continue
        if target.startswith("http://") or target.startswith("https://") or target.startswith("tel:") or target.startswith("mailto:") or target.startswith("#") or target.startswith("javascript:"):
            continue
        if target.endswith(".pdf") or target.endswith(".png") or target.endswith(".jpg") or target.endswith(".svg"):
            continue

        clean = target.split("?")[0].split("#")[0]
        if clean.endswith(".html"):
            relative_html_links.append((rel_path, target, clean))
        
        clean_route = clean.rstrip("/") if clean != "/" else "/"
        if clean_route.endswith(".html"):
            clean_route = clean_route[:-5]
        if clean_route and not clean_route.startswith("/"):
            clean_route = "/" + clean_route

        if clean_route == "/index":
            clean_route = "/"

        if clean_route not in valid_routes and clean_route != "":
            naked = clean_route.lstrip("/")
            if naked in slug_set:
                broken_internal_links.append((rel_path, target, f"Naked blog slug! Should be /blog/{naked}"))
            else:
                broken_internal_links.append((rel_path, target, f"Unknown route: {clean_route}"))

print(f"Total Broken: {len(broken_internal_links)}")
for r, t, reason in sorted(set(broken_internal_links)):
    print(f"  [{r}] -> '{t}' ({reason})")

print(f"\nTotal .html links: {len(relative_html_links)}")
for r, t, c in sorted(set(relative_html_links)):
    print(f"  [{r}] -> '{t}'")
