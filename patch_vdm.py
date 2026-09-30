import re

with open('cytos-react/src/pages/VdmMillingPage.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove duplicate top telemetry bar
# First telemetry bar ends at </aside>, second begins right after
pattern_dup = re.compile(
    r'(<aside class=\\"top-telemetry-bar\\".*?</aside>\\r?\\n\\r?\\n\s*<!-- Master Header -->\\r?\\n\s*<!-- =+.*?1\. Top Trust & Telemetry Bar.*?=+ -->\\r?\\n\s*<aside class=\\"top-telemetry-bar\\".*?</aside>)',
    re.DOTALL
)

m = pattern_dup.search(content)
if m:
    print("Found duplicate top telemetry bar!")
    # Keep only the first telemetry bar
    # Let's see what m.group(1) matched
    first_aside_end = m.group(1).find('</aside>') + len('</aside>')
    first_aside = m.group(1)[:first_aside_end]
    content = content[:m.start()] + first_aside + content[m.end():]
    print("Replaced duplicate top telemetry bar successfully!")
else:
    print("Pattern for duplicate top telemetry bar not matched.")

# 2. Fix Breadcrumbs in VdmMillingPage.jsx
old_bc_pattern = re.compile(
    r'<!-- Page Breadcrumbs -->\\r?\\n\s*<nav class=\\"breadcrumbs-bar\\".*?</nav>',
    re.DOTALL
)
new_bc = '<!-- Page Breadcrumbs -->\\r\\n  <div class=\\"breadcrumbs-bar\\">\\r\\n    <div class=\\"container\\">\\r\\n      <div class=\\"breadcrumbs-list\\">\\r\\n        <a href=\\"/\\">Home</a>\\r\\n        <span class=\\"breadcrumb-separator\\">/</span>\\r\\n        <a href=\\"/#pillars\\">Machines</a>\\r\\n        <span class=\\"breadcrumb-separator\\">/</span>\\r\\n        <span class=\\"breadcrumb-current\\">CyTOS VDM Heavy Multi-Spindle Milling</span>\\r\\n      </div>\\r\\n    </div>\\r\\n  </div>'

if old_bc_pattern.search(content):
    content = old_bc_pattern.sub(new_bc, content)
    print("Replaced breadcrumbs in VdmMillingPage.jsx successfully!")
else:
    print("Breadcrumbs pattern not found in VdmMillingPage.jsx")

# 3. Fix Tested Production Applications in VdmMillingPage.jsx
old_grid_pattern = re.compile(
    r'<div class=\\"proof-metrics-grid\\">.*?</div>\s*</div>\s*</section>',
    re.DOTALL
)
new_grid = '''<div class=\\"engineering-workflow-grid\\">\\r\\n        <div class=\\"workflow-card\\">\\r\\n          <div class=\\"workflow-step-num\\">APPLICATION 01</div>\\r\\n          <h4 class=\\"workflow-title\\">Electrical Switchboards</h4>\\r\\n          <p class=\\"workflow-desc\\">Simultaneous square/circular cutouts and mounting holes on heavy MS doors and gland plates.</p>\\r\\n        </div>\\r\\n        <div class=\\"workflow-card\\">\\r\\n          <div class=\\"workflow-step-num\\">APPLICATION 02</div>\\r\\n          <h4 class=\\"workflow-title\\">Hydraulic Manifolds</h4>\\r\\n          <p class=\\"workflow-desc\\">Deep drilling, high-pressure port counterbores, and thread tapping on solid mild steel blocks.</p>\\r\\n        </div>\\r\\n        <div class=\\"workflow-card\\">\\r\\n          <div class=\\"workflow-step-num\\">APPLICATION 03</div>\\r\\n          <h4 class=\\"workflow-title\\">Aluminium Die Plates</h4>\\r\\n          <p class=\\"workflow-desc\\">High-accuracy pocket milling and ejector pin drilling on heavy 7075 / 6061 tooling blocks.</p>\\r\\n        </div>\\r\\n        <div class=\\"workflow-card\\">\\r\\n          <div class=\\"workflow-step-num\\">APPLICATION 04</div>\\r\\n          <h4 class=\\"workflow-title\\">Structural Flanges</h4>\\r\\n          <p class=\\"workflow-desc\\">Multi-spindle bolt circle (PCD) drilling and tapping on cast iron and forged steel flanges.</p>\\r\\n        </div>\\r\\n      </div>\\r\\n    </div>\\r\\n  </section>'''

if old_grid_pattern.search(content):
    content = old_grid_pattern.sub(new_grid, content)
    print("Replaced Tested Production Applications in VdmMillingPage.jsx successfully!")
else:
    print("Tested Production Applications grid pattern not found in VdmMillingPage.jsx")

with open('cytos-react/src/pages/VdmMillingPage.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished patching VdmMillingPage.jsx!")
