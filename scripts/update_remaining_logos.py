import os

ROOT = r"c:\Users\PrasadMhaske\Downloads\Project1"
PAGES_DIR = os.path.join(ROOT, "src", "pages")

targets = ['PrivacyPolicyPage.jsx', 'TermsPage.jsx', 'VdmMillingPage.jsx']

for filename in targets:
    filepath = os.path.join(PAGES_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    # Replace logo references in HTML strings
    content = content.replace('src=\\"Logo.png\\"', 'src=\\"/CyTOS New Logo.png\\"')
    content = content.replace('src=\\"Logo-footer.png\\"', 'src=\\"/CyTOS New Logo.png\\"')
    content = content.replace('src=\\"Logo-cropped.png\\"', 'src=\\"/CyTOS New Logo.png\\"')
    content = content.replace('src="Logo.png"', 'src="/CyTOS New Logo.png"')
    content = content.replace('src="Logo-footer.png"', 'src="/CyTOS New Logo.png"')
    content = content.replace('src="Logo-cropped.png"', 'src="/CyTOS New Logo.png"')

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated logo in {filename}")
    else:
        print(f"No match in {filename}")
