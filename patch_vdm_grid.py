with open('cytos-react/src/pages/VdmMillingPage.jsx', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<div class=\\"proof-metrics-grid\\">'
end_marker = '<!-- Master Footer (5-Column Layout: Quick Links on Left, Contact in the End) -->'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    old_block = text[start_idx:end_idx]
    new_block = '''<div class=\\"engineering-workflow-grid\\">\\r\\n        <div class=\\"workflow-card\\">\\r\\n          <div class=\\"workflow-step-num\\">APPLICATION 01</div>\\r\\n          <h4 class=\\"workflow-title\\">Electrical Switchboards</h4>\\r\\n          <p class=\\"workflow-desc\\">Simultaneous square/circular cutouts and mounting holes on heavy MS doors and gland plates.</p>\\r\\n        </div>\\r\\n        <div class=\\"workflow-card\\">\\r\\n          <div class=\\"workflow-step-num\\">APPLICATION 02</div>\\r\\n          <h4 class=\\"workflow-title\\">Hydraulic Manifolds</h4>\\r\\n          <p class=\\"workflow-desc\\">Deep drilling, high-pressure port counterbores, and thread tapping on solid mild steel blocks.</p>\\r\\n        </div>\\r\\n        <div class=\\"workflow-card\\">\\r\\n          <div class=\\"workflow-step-num\\">APPLICATION 03</div>\\r\\n          <h4 class=\\"workflow-title\\">Aluminium Die Plates</h4>\\r\\n          <p class=\\"workflow-desc\\">High-accuracy pocket milling and ejector pin drilling on heavy 7075 / 6061 tooling blocks.</p>\\r\\n        </div>\\r\\n        <div class=\\"workflow-card\\">\\r\\n          <div class=\\"workflow-step-num\\">APPLICATION 04</div>\\r\\n          <h4 class=\\"workflow-title\\">Structural Flanges</h4>\\r\\n          <p class=\\"workflow-desc\\">Multi-spindle bolt circle (PCD) drilling and tapping on cast iron and forged steel flanges.</p>\\r\\n        </div>\\r\\n      </div>\\r\\n    </div>\\r\\n  </section>\\r\\n\\r\\n  '''
    text = text[:start_idx] + new_block + text[end_idx:]
    with open('cytos-react/src/pages/VdmMillingPage.jsx', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully updated Tested Production Applications in VdmMillingPage.jsx!")
else:
    print("Markers not found:", start_idx, end_idx)
