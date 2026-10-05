import urllib.request
import re

urls = [
    'https://www.induscnc.com/',
    'https://www.induscnc.com/cnc-drilling-machine.html',
    'https://www.induscnc.com/cnc-pcb-drilling-and-routing-machine.html',
    'https://www.induscnc.com/pcb-machine.html',
    'https://www.induscnc.com/printed-circuit-board-manufacturing-machines.html',
    'https://www.induscnc.com/cnc-machine.html'
]

for url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            title = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
            desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.I | re.S)
            keywords = re.search(r'<meta\s+name=["\']keywords["\']\s+content=["\'](.*?)["\']', html, re.I | re.S)
            h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.I | re.S)
            h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.I | re.S)
            images = re.findall(r'<img[^>]+src=["\'](.*?)["\'][^>]*alt=["\'](.*?)["\']', html, re.I)
            
            print('='*60)
            print('URL:', url)
            print('TITLE:', title.group(1).strip() if title else 'None')
            print('DESC:', desc.group(1).strip() if desc else 'None')
            print('KEYWORDS:', keywords.group(1).strip() if keywords else 'None')
            print('H1s:', [re.sub(r'<[^>]+>', '', h).strip() for h in h1s])
            print('H2s (first 4):', [re.sub(r'<[^>]+>', '', h).strip() for h in h2s[:4]])
            print('Images with alt (first 3):', [(src, alt) for src, alt in images[:3]])
    except Exception as e:
        print('Error fetching', url, e)
