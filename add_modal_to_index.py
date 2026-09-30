# -*- coding: utf-8 -*-
from create_automation_pages import MODAL_HTML

for fn in ['index.html', 'contact.html']:
    with open(fn, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if 'id="rfqModal"' not in c and '</body>' in c:
        c = c.replace('</body>', MODAL_HTML + '\n\n</body>')
        with open(fn, 'w', encoding='utf-8') as fp:
            fp.write(c)
        print('Added modal to', fn)
