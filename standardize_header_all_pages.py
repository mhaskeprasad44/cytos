# -*- coding: utf-8 -*-
"""
standardize_header_all_pages.py
Standardizes the header across all pages to match index.html exactly,
while setting the appropriate active classes for each page.
"""

import os, re

PROJECT_DIR = r"c:\Users\PrasadMhaske\Downloads\Project1"

def get_header_html(active_page="index.html", is_blog=False):
    prefix = "../" if is_blog else ""
    
    # Active class logic
    is_home = active_page == "index.html"
    is_pcb_drill = active_page == "pcb-drilling-routing.html"
    is_pcb_proto = active_page == "pcb-prototyping.html"
    is_cnc_router = active_page == "cnc-routers-milling.html"
    is_vdm = active_page == "vdm-milling.html"
    is_machines = is_pcb_drill or is_pcb_proto or is_cnc_router or is_vdm
    
    is_spm_turnkey = active_page == "spm-automation.html"
    is_robotic = active_page == "robotic-dispensing-cells.html"
    is_pneumatic = active_page == "pneumatic-welding-fixtures.html"
    is_plc = active_page == "plc-control-panels.html"
    is_automation = is_spm_turnkey or is_robotic or is_pneumatic or is_plc
    
    is_app = active_page == "applications.html"
    is_case = active_page == "case-studies.html"
    
    is_about = active_page == "about.html"
    is_blog_page = active_page == "blog.html" or is_blog
    is_about_group = is_about or is_blog_page
    
    is_contact = active_page == "contact.html"
    
    home_active = ' active' if is_home else ''
    mach_trigger_active = ' active' if is_machines else ''
    pcb_drill_item_active = ' active' if is_pcb_drill else ''
    pcb_proto_item_active = ' active' if is_pcb_proto else ''
    cnc_router_item_active = ' active' if is_cnc_router else ''
    vdm_item_active = ' active' if is_vdm else ''
    
    auto_trigger_active = ' active' if is_automation else ''
    spm_turnkey_item_active = ' active' if is_spm_turnkey else ''
    robotic_item_active = ' active' if is_robotic else ''
    pneumatic_item_active = ' active' if is_pneumatic else ''
    plc_item_active = ' active' if is_plc else ''
    
    app_active = ' active' if is_app else ''
    case_active = ' active' if is_case else ''
    
    about_trigger_active = ' active' if is_about_group else ''
    about_item_active = ' active' if is_about else ''
    blog_item_active = ' active' if is_blog_page else ''
    
    contact_active = ' active' if is_contact else ''

    return f'''  <!-- ==========================================================================
       1. Top Trust & Telemetry Bar
       ========================================================================== -->
  <aside class="top-telemetry-bar" aria-label="Facility Status and Quick Contact">
    <div class="top-bar-inner">
      <div class="telemetry-item">
        <span class="status-dot"></span>
        <span style="background: rgba(37,99,235,0.12); color: #1d4ed8; font-weight: 800; font-size: 0.76rem; padding: 2px 7px; border-radius: 4px; margin-right: 6px;">🇮🇳 PAN-INDIA DISPATCH</span>
        <span><strong>Direct Factory Delivery Across India:</strong> On-Site Commissioning &amp; Service in Maharashtra, Gujarat, Karnataka, Tamil Nadu, Delhi-NCR &amp; All States</span>
      </div>
    </div>
  </aside>

  <!-- ==========================================================================
       2. Sticky Main Header & Navigation
       ========================================================================== -->
  <header class="main-header" id="mainHeader">
    <div class="nav-container">
      <!-- Logo ONLY (Clean & Optimized) -->
      <a href="{prefix}index.html" class="logo-wrapper" title="CyTOS - Precision CNC &amp; Industrial Automation">
        <img src="{prefix}Logo.png" alt="CyTOS - Cycle Time Optimising Solutions" class="brand-logo-img" width="130" height="72" style="height: 72px; width: auto; object-fit: contain;">
      </a>

      <!-- Streamlined Desktop Navigation with Submenus -->
      <nav class="nav-links" id="navLinks" aria-label="Main Navigation">
        <a href="{prefix}index.html" class="nav-link{home_active}">Home</a>

        <!-- Machines Dropdown Submenu -->
        <div class="nav-item-dropdown">
          <a href="{prefix}pcb-drilling-routing.html" class="nav-link dropdown-trigger{mach_trigger_active}">
            <span>Machines</span>
            <svg class="dropdown-arrow" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
              <path d="M2 4.5l4 4 4-4"/>
            </svg>
          </a>
          <div class="dropdown-menu">
            <a href="{prefix}pcb-drilling-routing.html" class="dropdown-item{pcb_drill_item_active}">
              <div class="dropdown-item-title">
                <span>PCB Drilling &amp; Routing</span>
                <span class="badge-mini">Production</span>
              </div>
              <span class="dropdown-item-desc">Single, dual &amp; 3-spindle 60,000 RPM systems (PCB30, PCB60, PCB12)</span>
            </a>
            <a href="{prefix}pcb-prototyping.html" class="dropdown-item{pcb_proto_item_active}">
              <div class="dropdown-item-title">
                <span>PCB Rapid Prototyping</span>
                <span class="badge-mini">R&amp;D / Lab</span>
              </div>
              <span class="dropdown-item-desc">Chemical-free instant desktop prototyping (PCBE3020 &amp; PCB30)</span>
            </a>
            <a href="{prefix}cnc-routers-milling.html" class="dropdown-item{cnc_router_item_active}">
              <div class="dropdown-item-title">
                <span>Industrial CNC Routers</span>
                <span class="badge-mini">Heavy Gantry</span>
              </div>
              <span class="dropdown-item-desc">High-precision 4x4, 8x4 &amp; 8x8 routers for non-ferrous metals &amp; composites</span>
            </a>
            <a href="{prefix}vdm-milling.html" class="dropdown-item{vdm_item_active}">
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
          <a href="{prefix}spm-automation.html" class="nav-link dropdown-trigger{auto_trigger_active}">
            <span>Automation &amp; SPM</span>
            <svg class="dropdown-arrow" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
              <path d="M2 4.5l4 4 4-4"/>
            </svg>
          </a>
          <div class="dropdown-menu">
            <a href="{prefix}spm-automation.html" class="dropdown-item{spm_turnkey_item_active}">
              <div class="dropdown-item-title">
                <span>Custom Turnkey SPMs</span>
                <span class="badge-mini">Turnkey</span>
              </div>
              <span class="dropdown-item-desc">Custom single-purpose machinery engineered to cut cycle time up to 60%</span>
            </a>
            <a href="{prefix}robotic-dispensing-cells.html" class="dropdown-item{robotic_item_active}">
              <div class="dropdown-item-title">
                <span>Robotic Dispensing Cells</span>
                <span class="badge-mini">Automotive</span>
              </div>
              <span class="dropdown-item-desc">3-Axis high-speed dispensing cells for sealants, adhesives &amp; potting</span>
            </a>
            <a href="{prefix}pneumatic-welding-fixtures.html" class="dropdown-item{pneumatic_item_active}">
              <div class="dropdown-item-title">
                <span>Pneumatic Welding Fixtures</span>
                <span class="badge-mini">Pneumatic</span>
              </div>
              <span class="dropdown-item-desc">90° indexing &amp; heavy-clamping jigs for automotive robotic welding lines</span>
            </a>
            <a href="{prefix}plc-control-panels.html" class="dropdown-item{plc_item_active}">
              <div class="dropdown-item-title">
                <span>PLC Industrial Control Panels</span>
                <span class="badge-mini">Siemens / Delta</span>
              </div>
              <span class="dropdown-item-desc">Turnkey PLC/HMI automation control enclosures with safety interlocks</span>
            </a>
          </div>
        </div>

        <a href="{prefix}applications.html" class="nav-link{app_active}">Applications</a>
        <a href="{prefix}case-studies.html" class="nav-link{case_active}">Case Studies</a>

        <!-- About Dropdown Submenu with Blog -->
        <div class="nav-item-dropdown">
          <a href="{prefix}about.html" class="nav-link dropdown-trigger{about_trigger_active}">
            <span>About</span>
            <svg class="dropdown-arrow" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
              <path d="M2 4.5l4 4 4-4"/>
            </svg>
          </a>
          <div class="dropdown-menu">
            <a href="{prefix}about.html" class="dropdown-item{about_item_active}">
              <div class="dropdown-item-title">
                <span>About CyTOS</span>
                <span class="badge-mini">Company</span>
              </div>
              <span class="dropdown-item-desc">Our Pune manufacturing plant, engineering heritage &amp; 12-year track record</span>
            </a>
            <a href="{prefix}blog.html" class="dropdown-item{blog_item_active}">
              <div class="dropdown-item-title">
                <span>Engineering Blog &amp; Insights</span>
                <span class="badge-mini">Articles</span>
              </div>
              <span class="dropdown-item-desc">Technical articles on PCB drilling, CNC milling, chemical-free prototyping &amp; SPMs</span>
            </a>
          </div>
        </div>

        <a href="{prefix}contact.html" class="nav-link{contact_active}">Contact</a>
      </nav>

      <!-- Action CTAs: Icons Only -->
      <div class="nav-actions">
        <a href="https://wa.me/919921381071?text=Hi%20CyTOS%20team,%20I%20need%20a%20technical%20quote%20for%20a%20CNC%20machine." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" id="navWhatsappBtn" title="Chat on WhatsApp"><svg class="btn-icon-svg whatsapp-icon-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.68C7.02 10.88 7.9 12.04 8.02 12.2C8.14 12.37 9.73 14.95 12.24 15.93C14.33 16.75 14.75 16.59 15.22 16.54C15.69 16.49 16.74 15.91 16.96 15.29C17.18 14.66 17.18 14.13 17.11 14.02C17.05 13.91 16.89 13.84 16.64 13.72C16.39 13.6 15.17 13 14.94 12.92C14.72 12.83 14.56 12.79 14.4 13.04C14.24 13.29 13.77 13.84 13.63 14.01C13.5 14.17 13.36 14.19 13.11 14.07C12.87 13.95 12.08 13.69 11.15 12.86C10.42 12.21 9.93 11.41 9.79 11.17C9.65 10.92 9.78 10.79 9.9 10.67C10.01 10.56 10.15 10.38 10.27 10.23C10.4 10.08 10.44 9.97 10.52 9.81C10.6 9.65 10.56 9.51 10.5 9.39C10.44 9.27 9.97 8.12 9.78 7.65C9.59 7.19 9.39 7.25 9.24 7.24C9.1 7.23 8.94 7.23 8.78 7.23H8.53Z"/></svg>
        <span>WhatsApp</span>
        </a>
        <button class="btn btn-primary" data-open-rfq data-machine="General CNC Application" id="navQuoteBtn">
          <svg class="btn-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="18" height="18" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          <span>Request Quote</span>
        </button>
        <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Toggle Navigation Menu">
          <svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" fill="none" aria-hidden="true"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </button>
      </div>
    </div>
  </header>'''

# Apply to all 16 root pages
root_pages = [
    "index.html",
    "pcb-drilling-routing.html",
    "pcb-prototyping.html",
    "cnc-routers-milling.html",
    "vdm-milling.html",
    "spm-automation.html",
    "robotic-dispensing-cells.html",
    "pneumatic-welding-fixtures.html",
    "plc-control-panels.html",
    "case-studies.html",
    "applications.html",
    "about.html",
    "blog.html",
    "contact.html",
    "terms-conditions.html",
    "privacy-policy.html"
]

header_regex = re.compile(
    r'(?:<aside class="top-telemetry-bar"[\s\S]*?</aside>\s*)?(?:<!-- Sticky Main Header[^-]*-->\s*)?<header class="main-header" id="mainHeader">[\s\S]*?</header>',
    re.IGNORECASE
)

for p in root_pages:
    filepath = os.path.join(PROJECT_DIR, p)
    if not os.path.exists(filepath):
        print(f"Skipping missing {p}")
        continue
    with open(filepath, "r", encoding="utf-8") as fp:
        html = fp.read()
    
    new_hdr = get_header_html(active_page=p, is_blog=False)
    
    if header_regex.search(html):
        new_html = header_regex.sub(new_hdr, html, count=1)
        with open(filepath, "w", encoding="utf-8") as fp:
            fp.write(new_html)
        print(f"Successfully updated header in {p}")
    else:
        print(f"WARNING: header regex did not match in {p}")

print("\nRoot pages header standardization complete!")
