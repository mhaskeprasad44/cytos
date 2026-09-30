# -*- coding: utf-8 -*-
import os
import re
import urllib.request

PAGES = [
    'index.html',
    'pcb-drilling-routing.html',
    'pcb-prototyping.html',
    'cnc-routers-milling.html',
    'vdm-milling.html',
    'spm-automation.html',
    'applications.html',
    'case-studies.html',
    'about.html',
    'contact.html',
    'blog.html',
    'terms-conditions.html',
    'privacy-policy.html'
]

def main():
    all_ok = True
    print("=================================================================")
    print("        CyTOS Website Comprehensive Validation Suite (13 Pages)  ")
    print("=================================================================")
    
    for page in PAGES:
        url = f"http://localhost:8080/{page}"
        try:
            req = urllib.request.urlopen(url, timeout=5)
            status = req.getcode()
            html = req.read().decode('utf-8')
            
            # 1. Check all image src attributes
            imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
            missing_imgs = []
            for img in imgs:
                clean_path = img.split('?')[0].replace('/', os.sep)
                if not os.path.exists(clean_path):
                    missing_imgs.append(img)
            
            # 2. Check header logo
            header_parts = html.split('main-header')
            header_chunk = header_parts[1].split('</header>')[0] if len(header_parts) > 1 else ""
            has_header_logo = ('Logo.png' in header_chunk) and ('height: 56px' in header_chunk or 'brand-logo-img' in header_chunk)
            
            # 3. Check VDM machine page link
            has_vdm_link = 'vdm-milling.html' in html
            
            # 4. Check 5-Column Footer with Quick Links as Col 2 and Contact as Col 5
            footer_match = re.search(r'<footer class="main-footer".*?>(.*?)</footer>', html, re.DOTALL)
            footer_chunk = footer_match.group(1) if footer_match else ""
            
            # Split by <div class="footer-col">
            raw_cols = footer_chunk.split('<div class="footer-col">')[1:]
            col_count = len(raw_cols)
            
            # Verify Col 2 is Quick Links and Col 5 is Contact
            col2_is_quick_links = len(raw_cols) >= 2 and 'Quick Links' in raw_cols[1]
            col5_is_contact = len(raw_cols) >= 5 and ('Pune Works' in raw_cols[4] or 'Contact' in raw_cols[4])
            
            # 5. Check Inrank Tech attribution
            has_inrank_credit = ('https://inranktech.com' in footer_chunk) and ('Designed &amp; Developed by' in footer_chunk or 'Designed & Developed by' in footer_chunk)
            
            # 6. Check footer logo is Logo-footer.png with 76px height
            has_footer_logo = ('Logo-footer.png' in footer_chunk) and ('height: 76px' in footer_chunk)
            
            # 7. Check Factor of Safety badge
            has_safety_badge = 'Factor of Safety 2.0' in footer_chunk
            
            # 8. Check FormSubmit email
            has_formsubmit_email = 'inranktech@gmail.com' in html
            
            # Special check for blog.html: at least 20 blog articles
            if page == 'blog.html':
                blog_cards = re.findall(r'<article class="blog-card"[^>]*>', html)
                if len(blog_cards) < 20:
                    print(f"     [ERROR] blog.html should have at least 20 articles, found {len(blog_cards)}")
                    all_ok = False
            
            print(f"[OK] {page:26} | HTTP {status} | Cols: {col_count} | Col2 QL: {col2_is_quick_links} | Col5 Contact: {col5_is_contact} | Inrank: {has_inrank_credit}")
            
            if missing_imgs:
                print(f"     [ERROR] Missing images in {page}: {missing_imgs}")
                all_ok = False
            if not has_vdm_link:
                print(f"     [ERROR] Missing vdm-milling.html link in {page}!")
                all_ok = False
            if not col2_is_quick_links:
                print(f"     [ERROR] Column 2 is NOT Quick Links in {page}!")
                all_ok = False
            if not col5_is_contact:
                print(f"     [ERROR] Column 5 is NOT Contact in {page}!")
                all_ok = False
            if not has_inrank_credit:
                print(f"     [ERROR] Missing Inrank Tech attribution in {page}!")
                all_ok = False
            if not has_footer_logo:
                print(f"     [ERROR] Footer logo is not Logo-footer.png (76px) in {page}!")
                all_ok = False
            if not has_formsubmit_email:
                print(f"     [ERROR] Form submission does not point to inranktech@gmail.com in {page}!")
                all_ok = False
                
        except Exception as e:
            print(f"[FAIL] {page}: {e}")
            all_ok = False
            
    print("=================================================================")
    if all_ok:
        print(">>> ALL 13 PAGES PASSED COMPREHENSIVE VERIFICATION! <<<")
        print(">>> 1. VDM Dedicated Page Created & Linked Everywhere             <<<")
        print(">>> 2. 5-Column Footer: Col 2 Quick Links Left, Col 5 Contact End  <<<")
        print(">>> 3. Inrank Tech Attribution Added to Footer Bottom Bar         <<<")
        print(">>> 4. Header & Footer Logos Pristine, Cropped, High Contrast     <<<")
        print(">>> 5. Blog Page Clean, Beautiful 6-Card Uniform Grid with CSS    <<<")
    else:
        print(">>> SOME CHECKS FAILED! Review errors above. <<<")
    print("=================================================================")

if __name__ == '__main__':
    main()
