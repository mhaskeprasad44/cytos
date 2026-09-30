import json

with open('vdm-milling.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract content inside <body> ... </body>
start_body = content.find('<body>')
end_body = content.rfind('</body>')

if start_body != -1 and end_body != -1:
    body_content = content[start_body + len('<body>'):end_body]
else:
    body_content = content

# Replace .html links with React router friendly paths in nav
body_content = body_content.replace('href="/index.html"', 'href="/"')

jsx_code = f'''import React from 'react';
import HtmlPageWrapper from '../components/HtmlPageWrapper';

const pageHtml = {json.dumps(body_content)};

export default function VdmMillingPage() {{
  return (
    <HtmlPageWrapper
      htmlContent={{pageHtml}}
      title="VDM Series Multi-Spindle Vertical Milling & Drilling Machine | CyTOS Pune"
      description="CyTOS VDM Series multi-spindle rigid milling and drilling machines for switchboard plates, mild steel, and automotive components. Cut cycle times up to 65% with synchronized gantry spindles."
    />
  );
}}
'''

with open('cytos-react/src/pages/VdmMillingPage.jsx', 'w', encoding='utf-8') as f:
    f.write(jsx_code)

print('Successfully generated VdmMillingPage.jsx')
