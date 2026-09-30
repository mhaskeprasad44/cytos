import glob, os, re

files = sorted(glob.glob('*.html') + glob.glob('blog/*.html'))
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    forms = re.findall(r'(<form[^>]*>)', c)
    if forms:
        print(f'{f}: {len(forms)} forms')
        for form in forms:
            print('   ', form)
