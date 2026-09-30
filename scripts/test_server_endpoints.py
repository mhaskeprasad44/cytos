import urllib.request

urls = [
    'http://localhost:5173/',
    'http://localhost:5173/blog',
    'http://localhost:5173/blog/chemical-free-pcb-rapid-prototyping-machine',
    'http://localhost:5173/CyTOS%20New%20Logo.png',
    'http://localhost:5173/favicon-32x32.png',
    'http://localhost:5173/sitemap.xml'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = resp.read()
            print(f"{resp.status} OK: {u} (Length: {len(data)})")
    except Exception as e:
        print(f"ERROR on {u}: {e}")
