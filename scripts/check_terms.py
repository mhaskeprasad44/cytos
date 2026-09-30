import os, re

with open("src/data/allBlogsHtml.js", "r", encoding="utf-8") as f:
    content = f.read()

terms = [
    "IPC", "IPC-2221", "IPC-A-600", "IPC-4101", "IPC-TM-650",
    "ISO 230-2", "ISO 1940", "ISO 14001", "ISO 8573-1", "ISO 9001", "ISO 10816",
    "Gerber RS-274X", "RS-274X", "Excellon",
    "6061", "7075", "5052",
    "Category 4", "interlock", "Siemens", "Delta",
    "laser interferometer", "dial test indicator", "dial indicator"
]

for t in terms:
    cnt = len(re.findall(re.escape(t), content))
    print(f"'{t}': {cnt} occurrences")
