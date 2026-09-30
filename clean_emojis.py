# -*- coding: utf-8 -*-
import glob
import re

for p in sorted(glob.glob('*.html')):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()

    # Remove badge-icon spans with emojis
    c = re.sub(r'<span class="badge-icon">.*?</span>\s*', '', c)
    # Remove emojis inside badges and pill text
    c = c.replace('🔬 ', '')
    c = c.replace('📐 ', '')
    c = c.replace('🤖 ', '')
    c = c.replace('⚡ ', '')
    c = c.replace('⚙️ ', '')
    c = c.replace('📊 ', '')
    c = c.replace('🏛️ ', '')
    c = c.replace('⏱️', '')
    c = c.replace('📎 ', '')

    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)

print('Successfully cleaned badge emojis!')
