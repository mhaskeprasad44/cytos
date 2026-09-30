# -*- coding: utf-8 -*-
"""
restore_and_update_damaged_pages.py
Restores blog.html, terms-conditions.html, privacy-policy.html, and vdm-milling.html
with complete valid structure, clean top bar, single phone number, modern modal, and trust cards.
"""

import os
import re

PROJECT_DIR = r"c:\Users\PrasadMhaske\Downloads\Project1"

TOP_BAR_HTML = """  <!-- Top Telemetry Bar -->
  <aside class="top-telemetry-bar" aria-label="Facility Status and Quick Contact">
    <div class="top-bar-inner">
      <div class="telemetry-item">
        <span class="status-dot"></span>
        <span style="background: rgba(37,99,235,0.12); color: #1d4ed8; font-weight: 800; font-size: 0.76rem; padding: 2px 7px; border-radius: 4px; margin-right: 6px;">🇮🇳 PAN-INDIA DISPATCH</span>
        <span><strong>Direct Factory Delivery Across India:</strong> On-Site Commissioning &amp; Service in Maharashtra, Gujarat, Karnataka, Tamil Nadu, Delhi-NCR &amp; All States</span>
      </div>
      <div class="top-bar-contacts">
        <a href="tel:+919921381071" id="topPhoneLink" title="Direct Engineering Hotline">
          <svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14" style="vertical-align: -2px; margin-right: 4px;" aria-hidden="true"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.24.2 2.45.57 3.57a1 1 0 01-.24 1.02l-2.21 2.2z"/></svg>
          <span>+91 99213 81071</span>
        </a>
        <a href="https://wa.me/919921381071?text=Hi%20CyTOS%20team,%20I%20would%20like%20to%20discuss%20a%20CNC%20machine%20or%20automation%20requirement." target="_blank" rel="noopener noreferrer" id="topWhatsappLink" title="Chat on WhatsApp">
          <svg class="whatsapp-icon-svg" viewBox="0 0 24 24" fill="currentColor" width="14" height="14" style="vertical-align: -2px; margin-right: 4px;" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.68C7.02 10.88 7.9 12.04 8.02 12.2C8.14 12.37 9.73 14.95 12.24 15.93C14.33 16.75 14.75 16.59 15.22 16.54C15.69 16.49 16.74 15.91 16.96 15.29C17.18 14.66 17.18 14.13 17.11 14.02C17.05 13.91 16.89 13.84 16.64 13.72C16.39 13.6 15.17 13 14.94 12.92C14.72 12.83 14.56 12.79 14.4 13.04C14.24 13.29 13.77 13.84 13.63 14.01C13.5 14.17 13.36 14.19 13.11 14.07C12.87 13.95 12.08 13.69 11.15 12.86C10.42 12.21 9.93 11.41 9.79 11.17C9.65 10.92 9.78 10.79 9.9 10.67C10.01 10.56 10.15 10.38 10.27 10.23C10.4 10.08 10.44 9.97 10.52 9.81C10.6 9.65 10.56 9.51 10.5 9.39C10.44 9.27 9.97 8.12 9.78 7.65C9.59 7.19 9.39 7.25 9.24 7.24C9.1 7.23 8.94 7.23 8.78 7.23H8.53Z"/></svg>
          <span>Technical Applications Desk</span>
        </a>
      </div>
    </div>
  </aside>"""

CLEAN_MODAL_HTML = """  <!-- Fast Quote RFQ Modal -->
  <div class="modal-backdrop" id="rfqModal" role="dialog" aria-modal="true" aria-labelledby="modalTitle">
    <div class="modal-dialog">
      <div class="modal-header">
        <div>
          <span class="badge-mini" style="background: rgba(217, 119, 6, 0.12); color: var(--brand-gold-dark); font-weight: 700; padding: 3px 8px; border-radius: 4px; display: inline-block;">24-Hour Guaranteed Turnaround</span>
          <h3 id="modalTitle">Request Technical Machine Quotation</h3>
        </div>
        <button type="button" class="modal-close-btn" id="modalCloseBtn" aria-label="Close dialog">&times;</button>
      </div>

      <form id="rfqForm" action="https://formsubmit.co/info@cytos.in" method="POST">
        <input type="hidden" name="_cc" value="inranktech@gmail.com">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_subject" value="New Technical RFQ - CyTOS Machine Portal">
        <input type="hidden" name="_next" value="https://cytos.in/contact.html?rfq_submitted=1">

        <div class="form-grid-2">
          <div class="form-group">
            <label for="rfqName" class="form-label">Full Name *</label>
            <input type="text" id="rfqName" name="name" class="form-input" required placeholder="e.g. Rajesh Sharma">
          </div>
          <div class="form-group">
            <label for="rfqCompany" class="form-label">Company / Institution *</label>
            <input type="text" id="rfqCompany" name="company" class="form-input" required placeholder="e.g. Bharat Electronics Ltd">
          </div>
        </div>

        <div class="form-grid-2">
          <div class="form-group">
            <label for="rfqEmail" class="form-label">Corporate Email *</label>
            <input type="email" id="rfqEmail" name="email" class="form-input" required placeholder="name@company.com">
          </div>
          <div class="form-group">
            <label for="rfqPhone" class="form-label">Phone / WhatsApp Number *</label>
            <input type="tel" id="rfqPhone" name="phone" class="form-input" required placeholder="+91 98765 43210">
          </div>
        </div>

        <div class="form-group">
          <label for="rfqMachine" class="form-label">Machine or System of Interest *</label>
          <select id="rfqMachine" name="machine" class="form-select" required>
            <option value="PCB Drilling Series">PCB Production Drilling (PCB30 / PCB60 / PCB12)</option>
            <option value="PCB Prototyping Series">Chemical-Free PCB Prototyping (PCBE3020 / PCB30)</option>
            <option value="Industrial CNC Routers">Industrial CNC Routers (4x4, 8x4, 8x8 Gantry)</option>
            <option value="CyTOS VDM Series Heavy Drilling Milling Machine">CyTOS VDM Multi-Spindle Vertical Milling &amp; Drilling Series</option>
            <option value="Custom Turnkey SPM Automation">Custom Turnkey SPM Automation</option>
            <option value="Robotic Dispensing Cell">Robotic Dispensing Automation</option>
            <option value="Welding Fixtures">Pneumatic Welding Fixture Jigs</option>
            <option value="PLC Industrial Control Panels">PLC Industrial Control Panels</option>
            <option value="CyTOS Engineering Solutions" selected>CyTOS Machine System / Engineering Consultation</option>
          </select>
        </div>

        <div class="form-group">
          <label for="rfqDetails" class="form-label">Technical Requirements / Material / Tolerances</label>
          <textarea id="rfqDetails" name="details" class="form-textarea" rows="3" placeholder="Provide material type, thickness, target cycle time, or spindle RPM requirement..."></textarea>
        </div>

        <div class="modal-footer-actions">
          <button type="submit" class="btn btn-primary" id="rfqSubmitBtn" style="flex: 1;">
            <svg class="btn-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            <span>Submit Technical RFQ</span>
          </button>
          <button type="button" class="btn btn-whatsapp" id="rfqWhatsAppSubmitBtn">
            <svg class="whatsapp-icon-svg btn-icon-svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.68C7.02 10.88 7.9 12.04 8.02 12.2C8.14 12.37 9.73 14.95 12.24 15.93C14.33 16.75 14.75 16.59 15.22 16.54C15.69 16.49 16.74 15.91 16.96 15.29C17.18 14.66 17.18 14.13 17.11 14.02C17.05 13.91 16.89 13.84 16.64 13.72C16.39 13.6 15.17 13 14.94 12.92C14.72 12.83 14.56 12.79 14.4 13.04C14.24 13.29 13.77 13.84 13.63 14.01C13.5 14.17 13.36 14.19 13.11 14.07C12.87 13.95 12.08 13.69 11.15 12.86C10.42 12.21 9.93 11.41 9.79 11.17C9.65 10.92 9.78 10.79 9.9 10.67C10.01 10.56 10.15 10.38 10.27 10.23C10.4 10.08 10.44 9.97 10.52 9.81C10.6 9.65 10.56 9.51 10.5 9.39C10.44 9.27 9.97 8.12 9.78 7.65C9.59 7.19 9.39 7.25 9.24 7.24C9.1 7.23 8.94 7.23 8.78 7.23H8.53Z"/></svg>
            <span>Send Technical RFQ via WhatsApp</span>
          </button>
        </div>
      </form>
    </div>
  </div>"""

FOOTER_TRUST_SECTION_HTML = """      <!-- 2-Column Industrial Trust Cards -->
      <div class="footer-trust-strip">
        <div class="footer-trust-grid">
          
          <!-- Card 1: Factor of Safety 2.0 -->
          <div class="footer-trust-card">
            <div class="footer-trust-card-header">
              <div class="footer-trust-card-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
              </div>
              <h4 class="footer-trust-card-title">Factor of Safety 2.0 • 24×7 Continuous Duty</h4>
            </div>
            <p class="footer-trust-card-desc">
              Every CyTOS CNC gantry, high-frequency spindle, and automation fixture is engineered with a strict 2.0 safety factor for round-the-clock industrial duty cycles without thermal distortion.
            </p>
            <div class="footer-trust-card-pills">
              <span class="footer-trust-pill">100% Tested at Pune Plant</span>
              <span class="footer-trust-pill">Dynamic Balancing G0.4</span>
              <span class="footer-trust-pill">Class C3 Ground Ball Screws</span>
            </div>
          </div>

          <!-- Card 2: Pan-India Delivery & Commissioning -->
          <div class="footer-trust-card">
            <div class="footer-trust-card-header">
              <div class="footer-trust-card-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg>
              </div>
              <h4 class="footer-trust-card-title">🇮🇳 Direct Factory Machine Delivery &amp; On-Site Commissioning Across All India</h4>
            </div>
            <p class="footer-trust-card-desc">
              Doorstep factory delivery, uncrating, laser alignment, and operator training across Maharashtra, Gujarat, Karnataka, Tamil Nadu, Delhi-NCR, and all industrial clusters nationwide.
            </p>
            <div class="footer-trust-card-pills">
              <span class="footer-trust-pill">Turnkey Delivery</span>
              <span class="footer-trust-pill">On-Site Calibration</span>
              <span class="footer-trust-pill">Lifetime Spares &amp; Support</span>
            </div>
          </div>

        </div>
      </div>
"""

targets = ["vdm-milling.html", "blog.html", "privacy-policy.html", "terms-conditions.html"]

for t in targets:
    rec_path = os.path.join(PROJECT_DIR, f"recovered_{t}")
    dest_path = os.path.join(PROJECT_DIR, t)
    with open(rec_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Top Bar
    # Replace any <aside class="top-telemetry-bar">...</aside>
    content = re.sub(
        r'<aside class="top-telemetry-bar"[\s\S]*?</aside>',
        TOP_BAR_HTML,
        content
    )

    # 2. Modernize Logo height: 72px
    content = re.sub(
        r'(<img[^>]*class="brand-logo-img"[^>]*style="[^"]*height:\s*)\d+px;',
        r'\g<1>72px;',
        content
    )

    # 3. Replace any old phone numbers
    content = content.replace("+91 93701 58116", "+91 99213 81071")
    content = content.replace("9370158116", "9921381071")

    # 4. Replace WhatsApp Engineer text
    content = re.sub(r'WhatsApp Engineer', 'Technical Applications Desk', content)
    content = re.sub(r'WhatsApp Technical Engineer', 'Technical Applications Desk', content)
    content = re.sub(r'WhatsApp Engineering Contact', 'Technical Applications Desk', content)

    # 5. Insert Footer Trust Cards before <div class="footer-grid">
    if "footer-trust-strip" not in content and '<div class="footer-grid">' in content:
        content = content.replace(
            '<div class="footer-grid">',
            FOOTER_TRUST_SECTION_HTML + '\n      <div class="footer-grid">'
        )

    # 6. Deduplicate phone in footer contact item
    content = re.sub(
        r'<div class="footer-contact-item">\s*<svg[^>]*class="footer-contact-svg"[^>]*>[\s\S]*?</svg>\s*<div>\s*<a[^>]*>.*?</a>\s*/\s*<a[^>]*>.*?</a>\s*</div>\s*</div>',
        r'<div class="footer-contact-item">\n              <svg class="footer-contact-svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.24.2 2.45.57 3.57a1 1 0 01-.24 1.02l-2.21 2.2z"/></svg>\n              <div>\n                <a href="tel:+919921381071">+91 99213 81071</a>\n              </div>\n            </div>',
        content
    )

    # 7. Remove any existing rfqModal block
    content = re.sub(
        r'<!--\s*Fast Quote RFQ Modal\s*-->\s*<div class="modal-backdrop" id="rfqModal"[\s\S]*?</form>\s*</div>\s*</div>',
        '',
        content
    )
    content = re.sub(
        r'<div class="modal-backdrop" id="rfqModal"[\s\S]*?</form>\s*</div>\s*</div>',
        '',
        content
    )

    # Insert CLEAN_MODAL_HTML right before </body>
    if "</body>" in content:
        content = content.replace("</body>", f"\n{CLEAN_MODAL_HTML}\n\n</body>")

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully restored and polished {t} (length={len(content)})")

print("All 4 damaged pages restored and updated!")
