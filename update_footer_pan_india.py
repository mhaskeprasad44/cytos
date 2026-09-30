import glob, re

files = [
    'index.html',
    'pcb-drilling-routing.html',
    'pcb-prototyping.html',
    'cnc-routers-milling.html',
    'vdm-milling.html',
    'spm-automation.html',
    'applications.html',
    'case-studies.html',
    'about.html',
    'contact.html',
    'blog.html',
    'terms-conditions.html',
    'privacy-policy.html'
]

pattern = re.compile(
    r'(<div class="footer-badge-item">\s*<span class="badge-dot"></span>\s*<span>Factor of Safety 2\.0[^\n<]+</span>\s*</div>)',
    re.DOTALL
)

replacement = r'''\1
          <div class="footer-badge-item" style="margin-top: 0.4rem;">
            <span class="badge-dot" style="background: #38bdf8;"></span>
            <span>🇮🇳 Direct Factory Machine Delivery &amp; On-Site Commissioning Across All India</span>
          </div>'''

updated = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if 'Across All India' not in c and pattern.search(c):
        new_c = pattern.sub(replacement, c)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(new_c)
        updated += 1
        print(f"Updated footer in {f}")

print(f"Total footers updated with PAN-India badge: {updated}/{len(files)}")
