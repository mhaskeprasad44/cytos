import os
import re

SITEMAP_PATH = r"c:\Users\PrasadMhaske\Downloads\Project1\public\sitemap.xml"

with open(SITEMAP_PATH, "r", encoding="utf-8") as f:
    xml = f.read()

# Replace .html in URLs except if none
xml = re.sub(r'<loc>https://cytos\.in/([a-zA-Z0-9\-]+)\.html</loc>', r'<loc>https://cytos.in/\1</loc>', xml)

with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
    f.write(xml)

print("Updated sitemap.xml to clean canonical URLs!")
