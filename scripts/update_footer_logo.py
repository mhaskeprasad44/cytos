import glob
import os
import re

files_updated = []
count_replaced = 0

# 1. Update src/components/Footer.jsx
footer_jsx = 'src/components/Footer.jsx'
if os.path.exists(footer_jsx):
    with open(footer_jsx, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace('src="/CyTOS New Logo.png"', 'src="/CyTOS-New-Logo-White.png"')
    if new_content != content:
        with open(footer_jsx, 'w', encoding='utf-8') as f:
            f.write(new_content)
        files_updated.append(footer_jsx)
        count_replaced += 1
        print('Updated Footer.jsx')

# 2. Update src/pages/*.jsx and src/data/allBlogsHtml.js
pages_and_blogs = glob.glob('src/pages/*.jsx') + ['src/data/allBlogsHtml.js']

for file_path in pages_and_blogs:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    file_replaces = [0]
    def repl_footer_img(m):
        tag = m.group(0)
        new_tag = tag.replace('/CyTOS New Logo.png', '/CyTOS-New-Logo-White.png')
        if new_tag != tag:
            file_replaces[0] += 1
        return new_tag

    # Match any <img with CyTOS New Logo and footer in it
    new_content = re.sub(
        r'<img[^>]*?/CyTOS New Logo\.png[^>]*?class=\\"(?:footer-brand-logo|footer-logo-img)\\"[^>]*?>',
        repl_footer_img,
        content
    )
    # Also if class appears before src
    new_content = re.sub(
        r'<img[^>]*?class=\\"(?:footer-brand-logo|footer-logo-img)\\"[^>]*?/CyTOS New Logo\.png[^>]*?>',
        repl_footer_img,
        new_content
    )

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        files_updated.append(file_path)
        count_replaced += file_replaces[0]
        print(f'Updated {file_path} ({file_replaces[0]} replacements)')

print(f'\nTotal files updated: {len(files_updated)}')
print(f'Total occurrences replaced: {count_replaced}')
