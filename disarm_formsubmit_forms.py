import os
import re

root_dir = r"c:\Users\PrasadMhaske\Downloads\Project1"

count_html = 0
count_jsx = 0

for dirpath, _, filenames in os.walk(root_dir):
    if "node_modules" in dirpath or ".git" in dirpath or "dist" in dirpath:
        continue
    for fname in filenames:
        if fname.endswith(".html"):
            fpath = os.path.join(dirpath, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            new_content = re.sub(
                r'action=["\']https://formsubmit\.co/[^"\']+["\']',
                'action="javascript:void(0);" onsubmit="return false;"',
                content
            )

            if new_content != content:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                count_html += 1
                print(f"Updated HTML: {fpath}")

        elif fname.endswith(".jsx"):
            fpath = os.path.join(dirpath, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            new_content = re.sub(
                r'action=\\"https://formsubmit\.co/[^\\"]+\\"',
                r'action=\\"javascript:void(0);\\" onsubmit=\\"return false;\\"',
                content
            )

            if new_content != content:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                count_jsx += 1
                print(f"Updated JSX: {fpath}")

print(f"Disarmed {count_html} HTML files and {count_jsx} JSX files successfully.")
