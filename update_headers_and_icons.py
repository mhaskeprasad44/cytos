# -*- coding: utf-8 -*-
"""
Script to update all 9 HTML files:
1. Header: Logo ONLY (no brand-meta text beside it)
2. Menu: Sub-products organized into dropdown submenus (Machines & Automation/SPM)
3. Icons: WhatsApp & Request Quote SVG icons in header, top bar, modals, and CTAs
4. Machine images: ensure only pure machine photos are referenced (no brochure text/tables)
"""

import os
import re

PAGES = [
    {
        "filename": "index.html",
        "active_nav": "home",
        "active_sub": None,
        "rfq_default": "General CNC Application"
    },
    {
        "filename": "pcb-drilling-routing.html",
        "active_nav": "machines",
        "active_sub": "pcb-drilling",
        "rfq_default": "PCB Drilling Series"
    },
    {
        "filename": "pcb-prototyping.html",
        "active_nav": "machines",
        "active_sub": "pcb-proto",
        "rfq_default": "PCB Prototyping Series"
    },
    {
        "filename": "cnc-routers-milling.html",
        "active_nav": "machines",
        "active_sub": "cnc-routers",
        "rfq_default": "CNC Routers & Milling"
    },
    {
        "filename": "spm-automation.html",
        "active_nav": "spm",
        "active_sub": "spm-main",
        "rfq_default": "Turnkey SPM Automation"
    },
    {
        "filename": "applications.html",
        "active_nav": "applications",
        "active_sub": None,
        "rfq_default": "Material Cutting & Application"
    },
    {
        "filename": "case-studies.html",
        "active_nav": "case-studies",
        "active_sub": None,
        "rfq_default": "Turnkey Cycle Time Project"
    },
    {
        "filename": "about.html",
        "active_nav": "about",
        "active_sub": None,
        "rfq_default": "Plant Visit & Technical Inquiry"
    },
    {
        "filename": "contact.html",
        "active_nav": "contact",
        "active_sub": None,
        "rfq_default": "General Engineering Inquiry"
    }
]

WHATSAPP_ICON_SVG = '''<svg class="btn-icon-svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18" aria-hidden="true"><path d="M17.472 14.382c-.301-.15-1.777-.877-2.052-.977-.275-.1-.476-.15-.676.15-.2.301-.777.977-.952 1.177-.176.2-.351.226-.652.075-.301-.15-1.272-.469-2.423-1.495-.895-.798-1.5-1.784-1.676-2.085-.175-.301-.019-.464.132-.614.135-.135.301-.351.451-.527.15-.176.2-.301.301-.501.101-.2.05-.376-.025-.526-.075-.15-.676-1.63-.927-2.234-.244-.588-.492-.508-.676-.517l-.576-.01c-.2 0-.526.075-.802.376s-1.053 1.028-1.053 2.507 1.078 2.908 1.229 3.109c.15.2 2.122 3.24 5.14 4.542.718.31 1.279.496 1.716.635.72.23 1.376.197 1.895.122.578-.084 1.777-.727 2.028-1.429.251-.702.251-1.303.176-1.429-.075-.125-.276-.2-.577-.35z"/><path d="M12.004 2C6.479 2 2 6.48 2 12.006c0 1.954.563 3.778 1.536 5.32L2.05 22l4.834-1.44a9.96 9.96 0 0 0 5.12 1.446h.004c5.525 0 10.004-4.48 10.004-10.006C22.012 6.48 17.53 2 12.004 2zm0 18.254h-.003a8.27 8.27 0 0 1-4.214-1.151l-.302-.18-2.871.855.772-2.798-.196-.312a8.27 8.27 0 0 1-1.27-4.662c0-4.57 3.719-8.289 8.29-8.289 4.57 0 8.29 3.719 8.29 8.289 0 4.57-3.72 8.289-8.29 8.289z"/></svg>'''

QUOTE_ICON_SVG = '''<svg class="btn-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="18" height="18" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>'''

PHONE_ICON_SVG_SMALL = '''<svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14" style="vertical-align: -2px; margin-right: 4px;" aria-hidden="true"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.24.2 2.45.57 3.57a1 1 0 01-.24 1.02l-2.21 2.2z"/></svg>'''

WHATSAPP_ICON_SVG_SMALL = '''<svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14" style="vertical-align: -2px; margin-right: 4px;" aria-hidden="true"><path d="M17.472 14.382c-.301-.15-1.777-.877-2.052-.977-.275-.1-.476-.15-.676.15-.2.301-.777.977-.952 1.177-.176.2-.351.226-.652.075-.301-.15-1.272-.469-2.423-1.495-.895-.798-1.5-1.784-1.676-2.085-.175-.301-.019-.464.132-.614.135-.135.301-.351.451-.527.15-.176.2-.301.301-.501.101-.2.05-.376-.025-.526-.075-.15-.676-1.63-.927-2.234-.244-.588-.492-.508-.676-.517l-.576-.01c-.2 0-.526.075-.802.376s-1.053 1.028-1.053 2.507 1.078 2.908 1.229 3.109c.15.2 2.122 3.24 5.14 4.542.718.31 1.279.496 1.716.635.72.23 1.376.197 1.895.122.578-.084 1.777-.727 2.028-1.429.251-.702.251-1.303.176-1.429-.075-.125-.276-.2-.577-.35z"/><path d="M12.004 2C6.479 2 2 6.48 2 12.006c0 1.954.563 3.778 1.536 5.32L2.05 22l4.834-1.44a9.96 9.96 0 0 0 5.12 1.446h.004c5.525 0 10.004-4.48 10.004-10.006C22.012 6.48 17.53 2 12.004 2zm0 18.254h-.003a8.27 8.27 0 0 1-4.214-1.151l-.302-.18-2.871.855.772-2.798-.196-.312a8.27 8.27 0 0 1-1.27-4.662c0-4.57 3.719-8.289 8.29-8.289 4.57 0 8.29 3.719 8.29 8.289 0 4.57-3.72 8.289-8.29 8.289z"/></svg>'''

def build_header_html(active_nav, active_sub, rfq_default):
    is_home = ' active' if active_nav == 'home' else ''
    is_machines = ' active' if active_nav == 'machines' else ''
    is_spm = ' active' if active_nav == 'spm' else ''
    is_app = ' active' if active_nav == 'applications' else ''
    is_cases = ' active' if active_nav == 'case-studies' else ''
    is_about = ' active' if active_nav == 'about' else ''
    is_contact = ' active' if active_nav == 'contact' else ''

    return f'''  <header class="main-header" id="mainHeader">
    <div class="nav-container">
      <!-- Logo ONLY (Optimized per user request) -->
      <a href="index.html" class="logo-wrapper" title="CyTOS - Precision CNC &amp; Industrial Automation">
        <img src="Logo.png" alt="CyTOS - Cycle Time Optimising Solutions" class="brand-logo-img" width="130" height="46" style="height: 44px; width: auto; object-fit: contain;">
      </a>

      <!-- Streamlined Desktop Navigation with Submenus -->
      <nav class="nav-links" id="navLinks" aria-label="Main Navigation">
        <a href="index.html" class="nav-link{is_home}">Home</a>

        <!-- Machines Dropdown Submenu -->
        <div class="nav-item-dropdown">
          <a href="pcb-drilling-routing.html" class="nav-link dropdown-trigger{is_machines}">
            <span>Machines</span>
            <svg class="dropdown-arrow" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
              <path d="M2 4.5l4 4 4-4"/>
            </svg>
          </a>
          <div class="dropdown-menu">
            <a href="pcb-drilling-routing.html" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>PCB Drilling &amp; Routing</span>
                <span class="badge-mini">Production</span>
              </div>
              <span class="dropdown-item-desc">Single, dual &amp; 3-spindle 60,000 RPM systems (PCB30, PCB60, PCB12)</span>
            </a>
            <a href="pcb-prototyping.html" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>PCB Rapid Prototyping</span>
                <span class="badge-mini">R&amp;D / Lab</span>
              </div>
              <span class="dropdown-item-desc">Chemical-free instant desktop prototyping (PCBE3020 &amp; PCB30)</span>
            </a>
            <a href="cnc-routers-milling.html" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>Industrial CNC Routers</span>
                <span class="badge-mini">Heavy Gantry</span>
              </div>
              <span class="dropdown-item-desc">High-precision 4x4, 8x4 &amp; 8x8 routers for non-ferrous metals &amp; composites</span>
            </a>
            <a href="cnc-routers-milling.html#vdm-heavy-milling" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>VDM Heavy Milling &amp; Drilling</span>
                <span class="badge-mini">Multi-Spindle</span>
              </div>
              <span class="dropdown-item-desc">Multi-spindle rigid milling for switchboard &amp; electrical plates</span>
            </a>
          </div>
        </div>

        <!-- Automation & SPM Dropdown Submenu -->
        <div class="nav-item-dropdown">
          <a href="spm-automation.html" class="nav-link dropdown-trigger{is_spm}">
            <span>Automation &amp; SPM</span>
            <svg class="dropdown-arrow" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
              <path d="M2 4.5l4 4 4-4"/>
            </svg>
          </a>
          <div class="dropdown-menu">
            <a href="spm-automation.html" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>Custom Turnkey SPMs</span>
                <span class="badge-mini">Turnkey</span>
              </div>
              <span class="dropdown-item-desc">Custom single-purpose machinery engineered to cut cycle time up to 60%</span>
            </a>
            <a href="spm-automation.html#robotic-dispensing" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>Robotic Dispensing Cells</span>
                <span class="badge-mini">Automotive</span>
              </div>
              <span class="dropdown-item-desc">3-Axis high-speed dispensing cells for sealants, adhesives &amp; potting</span>
            </a>
            <a href="spm-automation.html#welding-fixtures" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>Pneumatic Welding Fixtures</span>
                <span class="badge-mini">Pneumatic</span>
              </div>
              <span class="dropdown-item-desc">90° indexing &amp; heavy-clamping jigs for automotive robotic welding lines</span>
            </a>
            <a href="spm-automation.html#control-panels" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>PLC Industrial Control Panels</span>
                <span class="badge-mini">Siemens / Delta</span>
              </div>
              <span class="dropdown-item-desc">Turnkey PLC/HMI automation control enclosures with safety interlocks</span>
            </a>
          </div>
        </div>

        <a href="applications.html" class="nav-link{is_app}">Applications</a>
        <a href="case-studies.html" class="nav-link{is_cases}">Case Studies</a>
        <a href="about.html" class="nav-link{is_about}">About Us</a>
        <a href="contact.html" class="nav-link{is_contact}">Contact</a>
      </nav>

      <!-- Action CTAs with Official SVG Icons -->
      <div class="nav-actions">
        <a href="https://wa.me/919370158116?text=Hi%20CyTOS%20team,%20I%20need%20a%20technical%20quote%20for%20a%20CNC%20machine." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" id="navWhatsappBtn" title="Chat on WhatsApp">
          {WHATSAPP_ICON_SVG}
          <span>WhatsApp</span>
        </a>
        <button class="btn btn-primary" data-open-rfq data-machine="{rfq_default}" id="navQuoteBtn">
          {QUOTE_ICON_SVG}
          <span>Request Quote</span>
        </button>
        <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Toggle Navigation Menu">
          <span>☰</span>
        </button>
      </div>
    </div>
  </header>'''

def update_file(p_info):
    fname = p_info["filename"]
    if not os.path.exists(fname):
        print(f"File not found: {fname}")
        return

    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update the top telemetry bar phone and whatsapp links to use clean SVGs
    top_bar_pattern = re.compile(r'<div class="top-bar-contacts">.*?</div>\s*</div>\s*</aside>', re.DOTALL)
    new_top_contacts = f'''<div class="top-bar-contacts">
        <span class="telemetry-item">
          <span>⚡ <strong>Standards:</strong> Factor of Safety 2.0 • 24x7 Rated Continuous Duty</span>
        </span>
        <a href="tel:+919370158116" id="topPhoneLink" title="Direct Engineering Hotline">
          {PHONE_ICON_SVG_SMALL}
          <span>+91 93701 58116</span>
        </a>
        <a href="https://wa.me/919370158116?text=Hi%20CyTOS%20team,%20I%20would%20like%20to%20discuss%20a%20CNC%20machine%20or%20automation%20requirement." target="_blank" rel="noopener noreferrer" id="topWhatsappLink" title="Chat on WhatsApp">
          {WHATSAPP_ICON_SVG_SMALL}
          <span>WhatsApp Engineer</span>
        </a>
      </div>
    </div>
  </aside>'''
    content = top_bar_pattern.sub(new_top_contacts, content)

    # 2. Replace the entire <header class="main-header" id="mainHeader"> ... </header>
    header_pattern = re.compile(r'<header class="main-header" id="mainHeader">.*?</header>', re.DOTALL)
    new_header = build_header_html(p_info["active_nav"], p_info["active_sub"], p_info["rfq_default"])
    content = header_pattern.sub(new_header, content)

    # 3. Fix machine-only images in index.html specifically
    if fname == "index.html":
        # Replace line 620 educational-cnc-lab.jpg in PCB12 card with real pcb12-multi-spindle.png
        content = re.sub(
            r'src="assets/images/machines/educational-cnc-lab\.jpg"\s+alt="CyTOS PCB12 Triple-Spindle Large Format Machine in Lab"',
            r'src="assets/images/machines/pcb12-multi-spindle.png" alt="CyTOS PCB12 Triple-Spindle Production Drilling & Routing Machine"',
            content
        )
        # Replace line 1039 robotic-spm.jpg with pure spm-automation-cell.jpg
        content = re.sub(
            r'src="assets/images/robotic-spm\.jpg"',
            r'src="assets/images/machines/spm-automation-cell.jpg"',
            content
        )
        # Clean alt text on facility overview
        content = re.sub(
            r'alt="CyTOS Pune Plant Overview and Company Profile Spread"',
            r'alt="CyTOS Pune Engineering & Manufacturing Facility"',
            content
        )

    # 4. In RFQ Modal, ensure WhatsApp button has WhatsApp icon
    content = re.sub(
        r'<button type="button" class="btn btn-whatsapp" id="rfqWhatsAppSubmitBtn">\s*<span>💬 Send Technical RFQ via WhatsApp</span>\s*</button>',
        f'<button type="button" class="btn btn-whatsapp" id="rfqWhatsAppSubmitBtn">{WHATSAPP_ICON_SVG}<span>Send Technical RFQ via WhatsApp</span></button>',
        content
    )

    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully updated: {fname}")

def main():
    for p in PAGES:
        update_file(p)

if __name__ == "__main__":
    main()
