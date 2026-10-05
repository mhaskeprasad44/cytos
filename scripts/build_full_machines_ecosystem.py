# -*- coding: utf-8 -*-
"""
scripts/build_full_machines_ecosystem.py
Complete generator for CyTOS machine pages, SEO titles, Image SEO, sitemap.xml, llms.txt, and App.jsx routing.
"""

import os
import json
import xml.etree.ElementTree as ET

ROOT = r"c:\Users\PrasadMhaske\Downloads\Project1"
SRC = os.path.join(ROOT, "src")
PAGES_DIR = os.path.join(SRC, "pages")
DATA_DIR = os.path.join(SRC, "data")
PUBLIC_DIR = os.path.join(ROOT, "public")

# Common Top Bar & Nav Header HTML
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
        <a href="https://wa.me/919921381071?text=Hi%20CyTOS%20team,%20I%20need%20a%20technical%20quote%20for%20a%20CNC%20machine." target="_blank" rel="noopener noreferrer" id="topWhatsappLink" title="Chat on WhatsApp">
          <svg class="whatsapp-icon-svg" viewBox="0 0 24 24" fill="currentColor" width="14" height="14" style="vertical-align: -2px; margin-right: 4px;" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.68C7.02 10.88 7.9 12.04 8.02 12.2C8.14 12.37 9.73 14.95 12.24 15.93C14.33 16.75 14.75 16.59 15.22 16.54C15.69 16.49 16.74 15.91 16.96 15.29C17.18 14.66 17.18 14.13 17.11 14.02C17.05 13.91 16.89 13.84 16.64 13.72C16.39 13.6 15.17 13 14.94 12.92C14.72 12.83 14.56 12.79 14.4 13.04C14.24 13.29 13.77 13.84 13.63 14.01C13.5 14.17 13.36 14.19 13.11 14.07C12.87 13.95 12.08 13.69 11.15 12.86C10.42 12.21 9.93 11.41 9.79 11.17C9.65 10.92 9.78 10.79 9.9 10.67C10.01 10.56 10.15 10.38 10.27 10.23C10.4 10.08 10.44 9.97 10.52 9.81C10.6 9.65 10.56 9.51 10.5 9.39C10.44 9.27 9.97 8.12 9.78 7.65C9.59 7.19 9.39 7.25 9.24 7.24C9.1 7.23 8.94 7.23 8.78 7.23H8.53Z"/></svg>
          <span>WhatsApp RFQ</span>
        </a>
      </div>
    </div>
  </aside>"""

def get_header_html(active_link=""):
    return f"""  <!-- Sticky Main Header -->
  <header class="main-header" id="mainHeader">
    <div class="nav-container">
      <a href="/" class="logo-wrapper" title="CyTOS - Precision CNC &amp; Industrial Automation">
        <img src="/CyTOS New Logo.png" alt="CyTOS - Cycle Time Optimising Solutions" class="brand-logo-img" width="130" height="72" style="height: 72px; width: auto; object-fit: contain;">
      </a>

      <!-- Streamlined Desktop Navigation with Submenus -->
      <nav class="nav-links" id="navLinks" aria-label="Main Navigation">
        <a href="/" class="nav-link{' active' if active_link == '/' else ''}">Home</a>

        <!-- Machines Dropdown Submenu -->
        <div class="nav-item-dropdown">
          <a href="/pcb-drilling-routing" class="nav-link dropdown-trigger active">
            <span>Machines</span>
            <svg class="dropdown-arrow" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
              <path d="M2 4.5l4 4 4-4"/>
            </svg>
          </a>
          <div class="dropdown-menu">
            <a href="/cnc-6060-pcb-drilling-routing-machine" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>CNC 6060 PCB Drilling &amp; Routing</span>
                <span class="badge-mini">100k RPM</span>
              </div>
              <span class="dropdown-item-desc">High-speed 18,000-100,000 RPM 0.2mm micro-drilling system (1-5 Spindles)</span>
            </a>
            <a href="/cnc-3020-pcb-prototyping-machine" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>CNC 3020 Rapid Prototyper</span>
                <span class="badge-mini">Tabletop</span>
              </div>
              <span class="dropdown-item-desc">Chemical-free instant lab PCB isolation milling with auto-leveling &amp; camera</span>
            </a>
            <a href="/cnc-3030-pcb-prototyping-machine" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>CNC 3030 High Precision PCB</span>
                <span class="badge-mini">Pneumatic ATC</span>
              </div>
              <span class="dropdown-item-desc">60,000 RPM precision benchtop routing with 0.3mm isolation &amp; ATC option</span>
            </a>
            <a href="/pcb12-multi-spindle-drilling-machine" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>PCB12 Multi-Spindle Gantry</span>
                <span class="badge-mini">3-Spindle</span>
              </div>
              <span class="dropdown-item-desc">1,200x1,200mm high throughput 3-spindle synchronized mass production</span>
            </a>
            <a href="/cnc-wood-acrylic-aluminium-router-machine" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>Industrial CNC Routers</span>
                <span class="badge-mini">4x4 to 10x5 ft</span>
              </div>
              <span class="dropdown-item-desc">Heavy mild steel gantry router for aluminium, brass, acrylic &amp; composites</span>
            </a>
            <a href="/vdm-heavy-vertical-drilling-milling-machine" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>VDM Heavy Drilling &amp; Milling</span>
                <span class="badge-mini">Cast Iron</span>
              </div>
              <span class="dropdown-item-desc">VDM30M / 50M / 100M BT30/BT40 rigid milling for MS, SS &amp; switchboards</span>
            </a>
            <a href="/foam-welding-machine" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>Foam Welding Machine</span>
                <span class="badge-mini">Packaging</span>
              </div>
              <span class="dropdown-item-desc">Automatic thermal packaging foam welding machine for mass production</span>
            </a>
            <a href="/educational-cnc-machines" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>Educational CNC Machines</span>
                <span class="badge-mini">Colleges/Labs</span>
              </div>
              <span class="dropdown-item-desc">Compact enclosed training CNC routers &amp; PCB machines for academic institutions</span>
            </a>
          </div>
        </div>

        <!-- Automation & SPM Dropdown Submenu -->
        <div class="nav-item-dropdown">
          <a href="/spm-automation" class="nav-link dropdown-trigger">
            <span>Automation &amp; SPM</span>
            <svg class="dropdown-arrow" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
              <path d="M2 4.5l4 4 4-4"/>
            </svg>
          </a>
          <div class="dropdown-menu">
            <a href="/spm-automation" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>Custom Turnkey SPMs</span>
                <span class="badge-mini">Turnkey</span>
              </div>
              <span class="dropdown-item-desc">Custom single-purpose machinery engineered to cut cycle time up to 60%</span>
            </a>
            <a href="/robotic-dispensing-cells" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>Robotic Dispensing Cells</span>
                <span class="badge-mini">Automotive</span>
              </div>
              <span class="dropdown-item-desc">3-Axis high-speed dispensing cells for sealants, adhesives &amp; potting</span>
            </a>
            <a href="/pneumatic-welding-fixtures" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>Pneumatic Welding Fixtures</span>
                <span class="badge-mini">Pneumatic</span>
              </div>
              <span class="dropdown-item-desc">90° indexing &amp; heavy-clamping jigs for automotive robotic welding lines</span>
            </a>
            <a href="/plc-control-panels" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>PLC Industrial Control Panels</span>
                <span class="badge-mini">Siemens / Delta</span>
              </div>
              <span class="dropdown-item-desc">Turnkey PLC/HMI automation control enclosures with safety interlocks</span>
            </a>
          </div>
        </div>

        <a href="/applications" class="nav-link">Applications</a>
        <a href="/case-studies" class="nav-link">Case Studies</a>

        <!-- About Dropdown Submenu with Blog -->
        <div class="nav-item-dropdown">
          <a href="/about" class="nav-link dropdown-trigger">
            <span>About</span>
            <svg class="dropdown-arrow" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
              <path d="M2 4.5l4 4 4-4"/>
            </svg>
          </a>
          <div class="dropdown-menu">
            <a href="/about" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>About CyTOS</span>
                <span class="badge-mini">Company</span>
              </div>
              <span class="dropdown-item-desc">Our Pune manufacturing plant, engineering heritage &amp; track record</span>
            </a>
            <a href="/blog" class="dropdown-item">
              <div class="dropdown-item-title">
                <span>Engineering Blog &amp; Insights</span>
                <span class="badge-mini">Articles</span>
              </div>
              <span class="dropdown-item-desc">Technical articles on PCB drilling, CNC milling, chemical-free prototyping &amp; SPMs</span>
            </a>
          </div>
        </div>

        <a href="/contact" class="nav-link">Contact</a>
      </nav>

      <!-- Action CTAs: WhatsApp & Quote -->
      <div class="nav-actions">
        <a href="https://wa.me/919921381071?text=Hi%20CyTOS%20team,%20I%20need%20a%20technical%20quote%20for%20a%20CNC%20machine." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" id="navWhatsappBtn" title="Chat on WhatsApp">
          <svg class="btn-icon-svg whatsapp-icon-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.68C7.02 10.88 7.9 12.04 8.02 12.2C8.14 12.37 9.73 14.95 12.24 15.93C14.33 16.75 14.75 16.59 15.22 16.54C15.69 16.49 16.74 15.91 16.96 15.29C17.18 14.66 17.18 14.13 17.11 14.02C17.05 13.91 16.89 13.84 16.64 13.72C16.39 13.6 15.17 13 14.94 12.92C14.72 12.83 14.56 12.79 14.4 13.04C14.24 13.29 13.77 13.84 13.63 14.01C13.5 14.17 13.36 14.19 13.11 14.07C12.87 13.95 12.08 13.69 11.15 12.86C10.42 12.21 9.93 11.41 9.79 11.17C9.65 10.92 9.78 10.79 9.9 10.67C10.01 10.56 10.15 10.38 10.27 10.23C10.4 10.08 10.44 9.97 10.52 9.81C10.6 9.65 10.56 9.51 10.5 9.39C10.44 9.27 9.97 8.12 9.78 7.65C9.59 7.19 9.39 7.25 9.24 7.24C9.1 7.23 8.94 7.23 8.78 7.23H8.53Z\"/></svg>
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
  </header>"""

# Pre-Footer Hotline and Footer HTML
FOOTER_HTML = """  <!-- Pre-Footer Engineering Hotline Conversion Bar -->
  <aside class="sticky-rfq-bar" aria-label="Engineering Hotline">
    <div class="sticky-rfq-container">
      <div class="sticky-rfq-info">
        <div class="hotline-icon-badge">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
          </svg>
        </div>
        <div>
          <span class="rfq-highlight">CyTOS Engineering Hotline:</span>
          <span class="rfq-desc">Need custom spindle speed, table sizing, or multi-head configuration? Speak directly with a Pune application specialist.</span>
        </div>
      </div>
      <div class="sticky-rfq-buttons">
        <a href="tel:+919921381071" class="btn btn-outline" title="Call Engineering Hotline">
          <svg viewBox="0 0 24 24" fill="currentColor" width="15" height="15" style="vertical-align: -2px; margin-right: 4px;" aria-hidden="true"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.24.2 2.45.57 3.57a1 1 0 01-.24 1.02l-2.21 2.2z"/></svg>
          <span>+91 99213 81071</span>
        </a>
        <a href="https://wa.me/919921381071?text=Hi%20CyTOS%20team,%20I%20need%20a%20quote%20for%20a%20CNC%20machine." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" title="WhatsApp Quote">
          <svg class="whatsapp-icon-svg btn-icon-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.68C7.02 10.88 7.9 12.04 8.02 12.2C8.14 12.37 9.73 14.95 12.24 15.93C14.33 16.75 14.75 16.59 15.22 16.54C15.69 16.49 16.74 15.91 16.96 15.29C17.18 14.66 17.18 14.13 17.11 14.02C17.05 13.91 16.89 13.84 16.64 13.72C16.39 13.6 15.17 13 14.94 12.92C14.72 12.83 14.56 12.79 14.4 13.04C14.24 13.29 13.77 13.84 13.63 14.01C13.5 14.17 13.36 14.19 13.11 14.07C12.87 13.95 12.08 13.69 11.15 12.86C10.42 12.21 9.93 11.41 9.79 11.17C9.65 10.92 9.78 10.79 9.9 10.67C10.01 10.56 10.15 10.38 10.27 10.23C10.4 10.08 10.44 9.97 10.52 9.81C10.6 9.65 10.56 9.51 10.5 9.39C10.44 9.27 9.97 8.12 9.78 7.65C9.59 7.19 9.39 7.25 9.24 7.24C9.1 7.23 8.94 7.23 8.78 7.23H8.53Z"/></svg>
          <span>Quick WhatsApp RFQ</span>
        </a>
      </div>
    </div>
  </aside>

  <!-- Complete Site Footer -->
  <footer class="site-footer-main" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <!-- Col 1: Brand & Credentials -->
        <div class="footer-col footer-col-brand">
          <div class="footer-brand-logo">
            <img src="/CyTOS-New-Logo-White.png" alt="CyTOS Logo" class="footer-logo-img" width="130" height="72" style="height: 64px; width: auto; object-fit: contain;">
          </div>
          <p class="footer-brand-desc">
            CYCLE TIME OPTIMISING SOLUTIONS (CyTOS) is a premier machine tool &amp; industrial automation manufacturer based in Bhosari MIDC, Pune, India. Specializing in high-speed PCB drilling machines (up to 100,000 RPM), chemical-free PCB prototyping, heavy-duty CNC routers, VDM milling, and custom turnkey SPMs.
          </p>
          <div class="footer-badges-list">
            <span class="badge-mini">ISO 9001:2015</span>
            <span class="badge-mini">Make In India</span>
            <span class="badge-mini">Bhosari MIDC Plant</span>
            <span class="badge-mini">CE / IEC 61439</span>
          </div>
        </div>

        <!-- Col 2: Machine Solutions -->
        <div class="footer-col">
          <h4 class="footer-col-title">Precision CNC Machines</h4>
          <ul class="footer-links-list">
            <li><a href="/cnc-6060-pcb-drilling-routing-machine">CNC 6060 PCB Drilling &amp; Routing</a></li>
            <li><a href="/cnc-3020-pcb-prototyping-machine">CNC 3020 PCB Rapid Prototyper</a></li>
            <li><a href="/cnc-3030-pcb-prototyping-machine">CNC 3030 High Precision PCB Machine</a></li>
            <li><a href="/pcb12-multi-spindle-drilling-machine">PCB12 3-Spindle High Throughput Gantry</a></li>
            <li><a href="/cnc-wood-acrylic-aluminium-router-machine">Industrial CNC Routers (4x4 to 10x5 ft)</a></li>
            <li><a href="/vdm-heavy-vertical-drilling-milling-machine">VDM Heavy Drilling &amp; Milling Machine</a></li>
            <li><a href="/foam-welding-machine">Automatic Foam Welding Machine</a></li>
            <li><a href="/educational-cnc-machines">Educational &amp; Training CNC Machines</a></li>
          </ul>
        </div>

        <!-- Col 3: Automation & Resources -->
        <div class="footer-col">
          <h4 class="footer-col-title">Automation &amp; Solutions</h4>
          <ul class="footer-links-list">
            <li><a href="/spm-automation">Custom SPM Automation</a></li>
            <li><a href="/robotic-dispensing-cells">Robotic Dispensing Cells</a></li>
            <li><a href="/pneumatic-welding-fixtures">Pneumatic Welding Fixtures</a></li>
            <li><a href="/plc-control-panels">PLC Industrial Control Panels</a></li>
            <li><a href="/applications">Industry Applications</a></li>
            <li><a href="/case-studies">Automotive &amp; Industrial Case Studies</a></li>
            <li><a href="/blog">Engineering Knowledge Base</a></li>
            <li><a href="/cytos_newcatalog2026_with BG.pdf" target="_blank" rel="noopener noreferrer">Download 2026 Machine Catalog (PDF)</a></li>
          </ul>
        </div>

        <!-- Col 4: Pune Works & Direct Contact -->
        <div class="footer-col">
          <h4 class="footer-col-title">Factory Works &amp; Contact</h4>
          <div class="footer-contact-list">
            <div class="footer-contact-item">
              <svg class="footer-contact-svg" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              <span>J-153, MIDC Bhosari, Pune, MH 411026, India</span>
            </div>
            <div class="footer-contact-item">
              <svg class="footer-contact-svg" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              <span>+91 99213 81071 / +91 76204 14165</span>
            </div>
            <div class="footer-contact-item">
              <svg class="footer-contact-svg" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              <span>cytos.ltd@gmail.com</span>
            </div>
            <div style="margin-top: 1rem;">
              <button class="btn btn-primary btn-block" data-open-rfq data-machine="Factory Direct Consultation">
                <span>Request Machine Quote</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Pan-India Delivery Bar -->
      <div class="footer-pan-india-bar" style="margin-top: 2rem; padding: 1rem 0; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.85rem; color: #94a3b8; text-align: center;">
        <strong style="color: #cbd5e1;">PAN-India Direct Delivery, Installation &amp; Service:</strong>
        Pune (Bhosari / Chakan / Talegaon) • Mumbai • Nashik • Aurangabad • Ahmedabad • Vadodara • Bengaluru • Chennai • Hyderabad • Delhi NCR • Coimbatore
      </div>

      <div class="footer-bottom-bar" style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.06); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem; font-size: 0.8rem; color: #64748b;">
        <div>&copy; 2026 CYCLE TIME OPTIMISING SOLUTIONS (CyTOS). All rights reserved. Made in Pune, India.</div>
        <div class="footer-legal-links">
          <a href="/privacy-policy" style="color: #64748b; margin-right: 1rem;">Privacy Policy</a>
          <a href="/terms-conditions" style="color: #64748b; margin-right: 1rem;">Terms &amp; Conditions</a>
          <a href="/sitemap.xml" target="_blank" rel="noopener noreferrer" style="color: #64748b;">Sitemap</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Floating WhatsApp Action -->
  <a href="https://wa.me/919921381071?text=Hello%20CyTOS%20Team%2C%20I%20am%20interested%20in%20your%20CNC%20and%20Automation%20Machines.%20Please%20share%20pricing%20and%20catalogue." target="_blank" rel="noopener noreferrer" class="whatsapp-float-btn" aria-label="Chat on WhatsApp" title="Chat on WhatsApp">
    <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor">
      <path d="M12.031 2C6.495 2 2 6.495 2 12.031c0 1.954.557 3.784 1.521 5.337L2 22l4.808-1.503a9.983 9.983 0 0 0 5.223 1.534h.005c5.535 0 10.03-4.495 10.03-10.031C22.066 6.495 17.571 2 12.031 2zm5.834 14.195c-.244.685-1.42 1.309-1.958 1.393-.513.08-1.182.115-1.914-.12-.444-.143-1.015-.333-1.748-.654-3.087-1.353-5.105-4.475-5.26-4.68-.154-.206-1.258-1.674-1.258-3.193 0-1.52.793-2.268 1.074-2.576.282-.308.615-.385.82-.385.205 0 .41.002.59.01.19.01.446-.072.697.533.256.615.872 2.128.949 2.282.077.154.128.333.026.539-.103.205-.154.333-.308.513-.154.18-.323.4-.462.538-.154.154-.314.323-.135.63.18.308.798 1.318 1.713 2.133 1.176 1.048 2.167 1.373 2.475 1.527.308.154.487.128.667-.077.18-.205.769-.897.974-1.205.205-.308.41-.256.692-.154.282.103 1.794.846 2.102 1.001.308.154.513.23.59.359.077.128.077.744-.167 1.429z" />
    </svg>
    <span class="whatsapp-float-label">Chat with Us</span>
  </a>

  <!-- RFQ Quote Modal -->
  <div class="rfq-modal-overlay" id="rfqModal" role="dialog" aria-modal="true" aria-label="Machine Quote Request">
    <div class="rfq-modal-dialog">
      <div class="rfq-modal-header">
        <div class="rfq-modal-title-group">
          <span class="badge-mini" style="background: var(--brand-gold); color: #fff;">DIRECT FACTORY PRICING</span>
          <h3 class="rfq-modal-title" id="rfqMachineTitle">Request Machine Quotation</h3>
          <p class="rfq-modal-subtitle">Direct from CyTOS Bhosari MIDC Plant, Pune. Response within 2 business hours.</p>
        </div>
        <button class="rfq-modal-close" id="closeRfqModal" aria-label="Close RFQ Modal">&times;</button>
      </div>
      <form class="rfq-modal-form" id="rfqForm" onsubmit="event.preventDefault(); window.open('https://wa.me/919921381071?text=' + encodeURIComponent('Hi CyTOS, I requested quote for ' + (document.getElementById('rfqSelectedMachine').value || 'CNC Machine') + '. Name: ' + document.getElementById('rfqName').value + ', Company: ' + document.getElementById('rfqCompany').value + ', Phone: ' + document.getElementById('rfqPhone').value), '_blank'); document.getElementById('rfqModal').classList.remove('active');">
        <input type="hidden" id="rfqSelectedMachine" value="General Inquiry">
        <div class="form-row-2">
          <div class="form-group">
            <label for="rfqName">Full Name *</label>
            <input type="text" id="rfqName" required placeholder="e.g. Rahul Sharma">
          </div>
          <div class="form-group">
            <label for="rfqCompany">Company / Institution *</label>
            <input type="text" id="rfqCompany" required placeholder="e.g. Precision Electronics Ltd">
          </div>
        </div>
        <div class="form-row-2">
          <div class="form-group">
            <label for="rfqPhone">Phone / WhatsApp *</label>
            <input type="tel" id="rfqPhone" required placeholder="e.g. +91 98765 43210">
          </div>
          <div class="form-group">
            <label for="rfqEmail">Work Email *</label>
            <input type="email" id="rfqEmail" required placeholder="e.g. rahul@company.com">
          </div>
        </div>
        <div class="form-group">
          <label for="rfqRequirements">Workpiece Material &amp; Target Specifications</label>
          <textarea id="rfqRequirements" rows="3" placeholder="Tell us about your panel/part size, material (FR4, MS, Aluminium), required tolerances, or monthly production volume..."></textarea>
        </div>
        <div class="form-actions-row">
          <button type="submit" class="btn btn-primary btn-block">
            <span>Send RFQ on WhatsApp (Instant Reply)</span>
          </button>
        </div>
      </form>
    </div>
  </div>
"""

print("Base layout templates defined.")
