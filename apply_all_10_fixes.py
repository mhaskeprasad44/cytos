# -*- coding: utf-8 -*-
"""
Script to apply all 10 user requirements across styles.css and all 9 HTML files.
"""

import os
import re

# 1. SVGs for Contact & Actions
MAP_PIN_SVG = '''<svg class="footer-contact-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>'''

PHONE_SVG = '''<svg class="footer-contact-svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.24.2 2.45.57 3.57a1 1 0 01-.24 1.02l-2.21 2.2z"/></svg>'''

EMAIL_SVG = '''<svg class="footer-contact-svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>'''

CLOCK_SVG = '''<svg class="footer-contact-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>'''

CALENDAR_VISIT_SVG = '''<svg class="btn-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="18" height="18" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line><path d="M9 16l2 2 4-4"></path></svg>'''

WHATSAPP_BTN_SVG = '''<svg class="btn-icon-svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18" aria-hidden="true"><path d="M17.472 14.382c-.301-.15-1.777-.877-2.052-.977-.275-.1-.476-.15-.676.15-.2.301-.777.977-.952 1.177-.176.2-.351.226-.652.075-.301-.15-1.272-.469-2.423-1.495-.895-.798-1.5-1.784-1.676-2.085-.175-.301-.019-.464.132-.614.135-.135.301-.351.451-.527.15-.176.2-.301.301-.501.101-.2.05-.376-.025-.526-.075-.15-.676-1.63-.927-2.234-.244-.588-.492-.508-.676-.517l-.576-.01c-.2 0-.526.075-.802.376s-1.053 1.028-1.053 2.507 1.078 2.908 1.229 3.109c.15.2 2.122 3.24 5.14 4.542.718.31 1.279.496 1.716.635.72.23 1.376.197 1.895.122.578-.084 1.777-.727 2.028-1.429.251-.702.251-1.303.176-1.429-.075-.125-.276-.2-.577-.35z"/><path d="M12.004 2C6.479 2 2 6.48 2 12.006c0 1.954.563 3.778 1.536 5.32L2.05 22l4.834-1.44a9.96 9.96 0 0 0 5.12 1.446h.004c5.525 0 10.004-4.48 10.004-10.006C22.012 6.48 17.53 2 12.004 2zm0 18.254h-.003a8.27 8.27 0 0 1-4.214-1.151l-.302-.18-2.871.855.772-2.798-.196-.312a8.27 8.27 0 0 1-1.27-4.662c0-4.57 3.719-8.289 8.29-8.289 4.57 0 8.29 3.719 8.29 8.289 0 4.57-3.72 8.289-8.29 8.289z"/></svg>'''

MASTER_FOOTER_HTML = f'''  <!-- ==========================================================================
       Master Footer (Optimized Colors & High-Contrast Typography)
       ========================================================================== -->
  <footer class="main-footer" id="footerSection">
    <div class="container">
      <div class="footer-grid">
        
        <!-- Col 1: Brand & Credentials -->
        <div class="footer-col">
          <div class="footer-brand-header">
            <img src="Logo.png" alt="CyTOS Logo" class="footer-brand-logo" width="140" height="52" style="height: 52px; width: auto; object-fit: contain; margin-bottom: 1.25rem;">
          </div>
          <p class="footer-desc" style="line-height: 1.65; margin-bottom: 1.25rem; font-size: 0.88rem; color: #94a3b8;">
            Pune-based machine tool &amp; industrial automation engineering company established in December 2019. Manufacturing precision CNC PCB drilling systems, green prototyping mills, heavy routers, and custom turnkey SPMs.
          </p>
          <div class="footer-badge-item">
            <span class="badge-dot"></span>
            <span>Factor of Safety 2.0 • 24×7 Rated Continuous Duty</span>
          </div>
        </div>

        <!-- Col 2: Machine Solutions -->
        <div class="footer-col">
          <h4 class="footer-col-title">Machine Solutions</h4>
          <ul class="footer-nav-list">
            <li><a href="pcb-drilling-routing.html">PCB Production Drilling &amp; Routing</a></li>
            <li><a href="pcb-prototyping.html">Chemical-Free PCB Prototyping</a></li>
            <li><a href="pcb-prototyping.html#educational-lab">Educational CNC Lab Trainers</a></li>
            <li><a href="cnc-routers-milling.html">4×4 &amp; 8×8 Industrial CNC Routers</a></li>
            <li><a href="cnc-routers-milling.html#vdm-heavy-milling">VDM Multi-Spindle Milling</a></li>
            <li><a href="spm-automation.html">Custom Turnkey SPMs &amp; Robotics</a></li>
          </ul>
        </div>

        <!-- Col 3: Key Applications -->
        <div class="footer-col">
          <h4 class="footer-col-title">Key Applications</h4>
          <ul class="footer-nav-list">
            <li><a href="case-studies.html">Automotive Sunroof Dispensing</a></li>
            <li><a href="case-studies.html#welding-fixtures">90° Pneumatic Weld Fixtures</a></li>
            <li><a href="applications.html#multilayer-pcb">Multilayer Double-Sided PCBs</a></li>
            <li><a href="applications.html#mcpcb">Aluminium MCPCB &amp; Heat Sinks</a></li>
            <li><a href="applications.html#composites">Acrylic &amp; Composite Routing</a></li>
            <li><a href="about.html">Pune 3,000 Sq. Ft. Facility Tour</a></li>
          </ul>
        </div>

        <!-- Col 4: Pune Engineering Hub & Contact -->
        <div class="footer-col">
          <h4 class="footer-col-title">Pune Works &amp; Contact</h4>
          <address class="footer-contact-list">
            <div class="footer-contact-item">
              {MAP_PIN_SVG}
              <span>S. No. 30, 5B, Dhayari-Narhe Road, Dhayari, Pune, Maharashtra 411041, India</span>
            </div>
            <div class="footer-contact-item">
              {PHONE_SVG}
              <div>
                <a href="tel:+919370158116">+91 93701 58116</a> / <a href="tel:+919921381071">+91 99213 81071</a>
              </div>
            </div>
            <div class="footer-contact-item">
              {EMAIL_SVG}
              <a href="mailto:info@cytos.in">info@cytos.in</a>
            </div>
            <div class="footer-contact-item">
              {CLOCK_SVG}
              <span>Monday – Saturday: 8:30 AM – 7:30 PM IST</span>
            </div>
          </address>
        </div>

      </div>

      <div class="footer-bottom-bar">
        <div class="copyright-text">
          &copy; 2019–2026 CyTOS Engineering Solutions. All Rights Reserved. Engineered with precision in Pune, Maharashtra.
        </div>
        <div class="footer-legal-links">
          <a href="about.html">About CyTOS</a>
          <a href="contact.html#visit">Plant Visits</a>
          <a href="contact.html">Terms of Supply</a>
          <a href="contact.html">Contact Us</a>
        </div>
      </div>
    </div>
  </footer>'''

def update_html_files():
    pages = [
        'index.html',
        'pcb-drilling-routing.html',
        'pcb-prototyping.html',
        'cnc-routers-milling.html',
        'spm-automation.html',
        'applications.html',
        'case-studies.html',
        'about.html',
        'contact.html'
    ]

    for p in pages:
        if not os.path.exists(p):
            continue
        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Increase Logo size in Header
        content = re.sub(
            r'<img\s+src="Logo\.png"\s+alt="[^"]*"\s+class="brand-logo-img"[^>]*>',
            '<img src="Logo.png" alt="CyTOS - Cycle Time Optimising Solutions" class="brand-logo-img" width="150" height="56" style="height: 56px; width: auto; object-fit: contain;">',
            content
        )

        # 2. Remove all lightening icon (⚡) from buttons
        # e.g., <span>⚡ Request Quote</span> -> <span>Request Quote</span>
        content = re.sub(r'<span>⚡\s*', '<span>', content)
        content = re.sub(r'>⚡\s*', '>', content)

        # 3. Replace entire footer with standardized MASTER_FOOTER_HTML
        footer_pattern = re.compile(r'<footer class="main-footer"[^>]*>.*?</footer>', re.DOTALL)
        content = footer_pattern.sub(MASTER_FOOTER_HTML, content)

        # 4. Fix RFQ Modal so it is never an open form after the footer
        # Replace class="rfq-modal-backdrop" with class="rfq-modal-overlay"
        content = content.replace('class="rfq-modal-backdrop"', 'class="rfq-modal-overlay"')
        content = content.replace('class="rfq-modal-container"', 'class="rfq-modal-window"')
        content = content.replace('class="rfq-modal-header"', 'class="modal-header"')
        content = content.replace('class="rfq-close-btn"', 'class="modal-close-btn"')
        content = content.replace('class="rfq-modal-body"', 'class="modal-body"')

        # Specific page adjustments:
        if p == 'about.html':
            # Fix hero image to use generated text-free facility photo
            content = re.sub(
                r'src="assets/images/machines/cytos-facility-overview\.jpg"\s+alt="[^"]*"',
                'src="assets/images/machines/cytos-facility-overview.jpg" alt="CyTOS 3,000 Sq. Ft. Machine Tool Manufacturing Plant, Pune"',
                content
            )
            # Fix Image 2 buttons: "Book an In-Person Pune Plant Visit" & "Direct WhatsApp with Leadership"
            btn_row_pattern = re.compile(r'<div class="slide-cta-row">.*?</div>\s*<div class="engineering-signoff-bar">', re.DOTALL)
            new_btn_row = f'''<div class="slide-cta-row">
            <a href="contact.html#visit" class="btn btn-primary btn-lg">
              {CALENDAR_VISIT_SVG}
              <span>Book an In-Person Pune Plant Visit</span>
            </a>
            <a href="https://wa.me/919370158116?text=Hi%20CyTOS,%20I%20would%20like%20to%20discuss%20our%20plant%20requirements%20with%20your%20leadership%20team." class="btn btn-whatsapp btn-lg" target="_blank" rel="noopener noreferrer">
              {WHATSAPP_BTN_SVG}
              <span>Direct WhatsApp with Leadership</span>
            </a>
          </div>

          <div class="engineering-signoff-bar">'''
            content = btn_row_pattern.sub(new_btn_row, content)

            # Fix Image 3: 6 items in proof-metrics-grid
            metrics_grid_pattern = re.compile(r'<div class="proof-metrics-grid">.*?</div>\s*</div>\s*</section>', re.DOTALL)
            new_metrics_grid = '''<div class="proof-metrics-grid">
        <div class="proof-metric-item">
          <div class="metric-number">2019</div>
          <div class="metric-label">Year Established in Pune</div>
        </div>
        <div class="proof-metric-item">
          <div class="metric-number">15+</div>
          <div class="metric-label">Engineering Professionals</div>
        </div>
        <div class="proof-metric-item">
          <div class="metric-number">3,000</div>
          <div class="metric-label">Sq. Ft. Dedicated Facility</div>
        </div>
        <div class="proof-metric-item">
          <div class="metric-number">2.0×</div>
          <div class="metric-label">Structural Safety Factor</div>
        </div>
        <div class="proof-metric-item">
          <div class="metric-number">24×7</div>
          <div class="metric-label">Continuous Duty Rating</div>
        </div>
        <div class="proof-metric-item">
          <div class="metric-number">&lt; 3 µm</div>
          <div class="metric-label">Spindle Runout Standard</div>
        </div>
      </div>
    </div>
  </section>'''
            content = metrics_grid_pattern.sub(new_metrics_grid, content)

        if p == 'contact.html':
            # Fix Map Embed & Location Card
            map_pattern = re.compile(r'<!-- Embedded Map View -->.*?</div>\s*</div>\s*</div>\s*</section>', re.DOTALL)
            new_map_block = '''<!-- Embedded Map View with Accurate CyTOS Location -->
          <div class="map-embed-wrapper">
            <div class="map-header-bar">
              <div style="display: flex; align-items: center; gap: 0.65rem;">
                <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20" style="color: var(--brand-gold-dark);"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                <strong>CyTOS Facility &amp; Works: Dhayari-Narhe Road, Pune</strong>
              </div>
              <a href="https://www.google.com/maps/search/?api=1&query=CyTOS+Engineering+Solutions+Dhayari+Narhe+Road+Pune+411041" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">
                Open in Google Maps ↗
              </a>
            </div>
            <iframe 
              src="https://maps.google.com/maps?q=CyTOS+Engineering+Solutions,+S.+No.+30,+5B,+Dhayari-Narhe+Road,+Dhayari,+Pune+411041&t=&z=16&ie=UTF8&iwloc=&output=embed" 
              width="100%" 
              height="380" 
              style="border:0;" 
              allowfullscreen="" 
              loading="lazy" 
              referrerpolicy="no-referrer-when-downgrade"
              title="CyTOS Facility Location Map">
            </iframe>
          </div>
        </div>

      </div>
    </div>
  </section>'''
            content = map_pattern.sub(new_map_block, content)

            # Replace contact-method-tile emojis with SVGs
            content = content.replace('<div class="contact-method-icon">📍</div>', f'<div class="contact-method-icon">{MAP_PIN_SVG}</div>')
            content = content.replace('<div class="contact-method-icon">📞</div>', f'<div class="contact-method-icon">{PHONE_SVG}</div>')
            content = content.replace('<div class="contact-method-icon">✉️</div>', f'<div class="contact-method-icon">{EMAIL_SVG}</div>')
            content = content.replace('<div class="contact-method-icon">🕒</div>', f'<div class="contact-method-icon">{CLOCK_SVG}</div>')

        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {p}")

if __name__ == '__main__':
    update_html_files()
