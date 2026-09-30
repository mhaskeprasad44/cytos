# -*- coding: utf-8 -*-
"""
fix_modals_placement.py
Moves any RFQ modal from after </footer> to before <footer> across all HTML pages.
"""

import os
import re
import glob

PROJECT_DIR = r"c:\Users\PrasadMhaske\Downloads\Project1"
all_html = glob.glob(os.path.join(PROJECT_DIR, "*.html")) + glob.glob(os.path.join(PROJECT_DIR, "blog", "*.html"))

pattern = re.compile(
    r'(\s*(?:<!--.*?-->\s*)?<div[^>]*id=[\'"](?:rfqModal|rfqModalOverlay)[\'"][^>]*>.*?</form>\s*</div>\s*</div>)',
    re.DOTALL
)

fixed_count = 0
for fpath in all_html:
    with open(fpath, "r", encoding="utf-8") as fp:
        c = fp.read()

    if "</footer>" not in c:
        continue

    parts = c.split("</footer>", 1)
    before_footer = parts[0]
    after_footer = parts[1]

    if "<form" not in after_footer:
        continue

    m = pattern.search(after_footer)
    if m:
        modal_block = m.group(1)
        after_footer = after_footer[:m.start()] + after_footer[m.end():]
        # Insert before <footer>
        footer_match = re.search(r'(<!--.*?Footer.*?-->\s*<footer|<footer)', before_footer, re.IGNORECASE)
        if footer_match:
            pos = footer_match.start()
            before_footer = before_footer[:pos] + modal_block + "\n\n  " + before_footer[pos:]
        else:
            before_footer = before_footer + "\n\n  " + modal_block

        new_c = before_footer + "</footer>" + after_footer
        with open(fpath, "w", encoding="utf-8") as fp:
            fp.write(new_c)

        # Mirror if blog
        if "blog\\" in fpath or "blog/" in fpath:
            slug = os.path.splitext(os.path.basename(fpath))[0]
            dir_index = os.path.join(PROJECT_DIR, "blog", slug, "index.html")
            if os.path.exists(dir_index):
                dir_content = new_c.replace('href="../', 'href="../../').replace('src="../', 'src="../../')
                with open(dir_index, "w", encoding="utf-8") as fp:
                    fp.write(dir_content)

        fixed_count += 1
        print(f"[FIXED] {os.path.relpath(fpath, PROJECT_DIR)}")

print(f"\nTotal files fixed: {fixed_count}")
