import React from 'react';
import HtmlPageWrapper from '../components/HtmlPageWrapper';

const pageHtml = `
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-P6DNQQ3H"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Product", "name": "Educational & Training CNC Machines", "model": "CyTOS EduCNC Series", "description": "Manufacturer of Educational CNC Machines - Compact training CNC milling, router, and PCB machines with safety enclosures for engineering colleges and labs. CyTOS Pune.", "image": ["https://www.cytos.in/assets/images/machines/educational-cnc-lab.png", "https://www.cytos.in/assets/images/machines/pcb-prototyping-pcb30.png", "https://www.cytos.in/assets/images/machines/precision-machining-parts.png"], "brand": {"@type": "Brand", "name": "CyTOS"}, "manufacturer": {"@type": "Organization", "name": "CYCLE TIME OPTIMISING SOLUTIONS (CyTOS)", "url": "https://www.cytos.in", "logo": "https://www.cytos.in/CyTOS New Logo.png", "address": {"@type": "PostalAddress", "streetAddress": "J-153, M.I.D.C., Bhosari", "addressLocality": "Pune", "addressRegion": "Maharashtra", "postalCode": "411026", "addressCountry": "IN"}}, "category": "Educational & Institutional CNC", "offers": {"@type": "Offer", "url": "https://www.cytos.in/educational-cnc-machines", "priceCurrency": "INR", "price": "Contact for Factory Direct Quote", "availability": "https://schema.org/InStock", "itemCondition": "https://schema.org/NewCondition"}, "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "42"}}</script>
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.cytos.in"}, {"@type": "ListItem", "position": 2, "name": "Machines", "item": "https://www.cytos.in/#pillars"}, {"@type": "ListItem", "position": 3, "name": "Educational & Training CNC Machines", "item": "https://www.cytos.in/educational-cnc-machines"}]}</script>
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "Why should colleges invest in CyTOS Educational CNC machines over consumer CNC kits?", "acceptedAnswer": {"@type": "Answer", "text": "Consumer hobby kits use weak 3D-printed parts, belt drives, and unstable open-source controllers that break quickly under student use. CyTOS Educational machines are built with genuine industrial ball screws, linear guides, and steel frames, offering real industrial reliability, accuracy, and Fanuc/Siemens-compatible G-code syntax."}}, {"@type": "Question", "name": "What training is provided for faculty and lab assistants?", "acceptedAnswer": {"@type": "Answer", "text": "We conduct an extensive hands-on faculty training program upon installation. Our engineers guide instructors through machine operation, safety protocols, CAD-to-CAM workflow, tooling selection, and troubleshooting so faculty can confidently teach student batches."}}, {"@type": "Question", "name": "Is special three-phase power or compressed air needed in the lab?", "acceptedAnswer": {"@type": "Answer", "text": "No. The CyTOS Educational CNC machine runs on standard 230V AC single-phase power from a regular domestic socket, requiring no special electrical substation or high-pressure plant air."}}, {"@type": "Question", "name": "Can students use standard CAD/CAM software like Fusion 360 or SolidWorks?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. CyTOS EduCAM accepts standard G-code exported from Autodesk Fusion 360, SolidWorks, Mastercam, Creo, NX, and EDA packages like Altium, KiCad, and Eagle."}}]}</script>

  <!-- Top Telemetry Bar -->
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
  </aside>

  <!-- Sticky Main Header -->
  <header class="main-header" id="mainHeader">
    <div class="nav-container">
      <a href="/" class="logo-wrapper" title="CyTOS - Precision CNC &amp; Industrial Automation">
        <img src="/CyTOS New Logo.png" alt="CyTOS - Cycle Time Optimising Solutions" class="brand-logo-img" width="130" height="72" style="height: 72px; width: auto; object-fit: contain;">
      </a>

      <!-- Streamlined Desktop Navigation with Submenus -->
      <nav class="nav-links" id="navLinks" aria-label="Main Navigation">
        <a href="/" class="nav-link">Home</a>

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
          <svg class="btn-icon-svg whatsapp-icon-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.68C7.02 10.88 7.9 12.04 8.02 12.2C8.14 12.37 9.73 14.95 12.24 15.93C14.33 16.75 14.75 16.59 15.22 16.54C15.69 16.49 16.74 15.91 16.96 15.29C17.18 14.66 17.18 14.13 17.11 14.02C17.05 13.91 16.89 13.84 16.64 13.72C16.39 13.6 15.17 13 14.94 12.92C14.72 12.83 14.56 12.79 14.4 13.04C14.24 13.29 13.77 13.84 13.63 14.01C13.5 14.17 13.36 14.19 13.11 14.07C12.87 13.95 12.08 13.69 11.15 12.86C10.42 12.21 9.93 11.41 9.79 11.17C9.65 10.92 9.78 10.79 9.9 10.67C10.01 10.56 10.15 10.38 10.27 10.23C10.4 10.08 10.44 9.97 10.52 9.81C10.6 9.65 10.56 9.51 10.5 9.39C10.44 9.27 9.97 8.12 9.78 7.65C9.59 7.19 9.39 7.25 9.24 7.24C9.1 7.23 8.94 7.23 8.78 7.23H8.53Z"/></svg>
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
  </header>

  <!-- Breadcrumbs Bar -->
  <div class="breadcrumbs-bar">
    <div class="container">
      <div class="breadcrumbs-list">
        <a href="/">Home</a>
        <span class="breadcrumb-separator">/</span>
        <a href="/#pillars">Machines</a>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-current">Educational & Training CNC Machines</span>
      </div>
    </div>
  </div>

  <!-- Product Page Hero Section -->
  <section class="page-hero">
    <div class="container">
      <div class="page-hero-grid">
        <div class="page-hero-content">
          <div class="hero-badge">
            <span>COLLEGE & INSTITUTIONAL TRAINER</span>
          </div>
          <h1 class="page-hero-title">Educational &amp; Training CNC Machines</h1>
          <p class="page-hero-subtitle">
            Compact, robust, and safe CNC machine tools engineered specifically for engineering colleges, polytechnics, ITIs, and skill development centres. Features full transparent safety enclosures, door interlocks, PC-based CNC simulation software, and curriculum packages for teaching G-code programming, 3D routing, and PCB fabrication.
          </p>
          
          <!-- Answer-First Box for Search & Direct Buyers -->
          <div class="answer-first-callout">
            <strong>In brief:</strong> The CyTOS Educational CNC Series bridges academic theory and real-world industrial practice. Built with the same precision ball screws, linear guides, and controllers as our factory production machines, it provides students with hands-on machining experience in a safe, quiet, and clean laboratory environment.
          </div>

          <div class="slide-cta-row">
            <button class="btn btn-primary btn-lg" data-open-rfq data-machine="Educational & Training CNC Machines">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="btn-icon-svg" aria-hidden="true"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect><path d="M9 12h6"></path><path d="M9 16h6"></path></svg> <span>Request Technical Quote</span>
            </button>
            <a href="https://wa.me/919921381071?text=Hi%20CyTOS,%20I%20am%20interested%20in%20Educational & Training CNC Machines.%20Please%20send%20pricing%20and%20proposal." class="btn btn-whatsapp btn-lg" target="_blank" rel="noopener noreferrer">
              <svg class="btn-icon-svg whatsapp-icon-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.68C7.02 10.88 7.9 12.04 8.02 12.2C8.14 12.37 9.73 14.95 12.24 15.93C14.33 16.75 14.75 16.59 15.22 16.54C15.69 16.49 16.74 15.91 16.96 15.29C17.18 14.66 17.18 14.13 17.11 14.02C17.05 13.91 16.89 13.84 16.64 13.72C16.39 13.6 15.17 13 14.94 12.92C14.72 12.83 14.56 12.79 14.4 13.04C14.24 13.29 13.77 13.84 13.63 14.01C13.5 14.17 13.36 14.19 13.11 14.07C12.87 13.95 12.08 13.69 11.15 12.86C10.42 12.21 9.93 11.41 9.79 11.17C9.65 10.92 9.78 10.79 9.9 10.67C10.01 10.56 10.15 10.38 10.27 10.23C10.4 10.08 10.44 9.97 10.52 9.81C10.6 9.65 10.56 9.51 10.5 9.39C10.44 9.27 9.97 8.12 9.78 7.65C9.59 7.19 9.39 7.25 9.24 7.24C9.1 7.23 8.94 7.23 8.78 7.23H8.53Z"/></svg> <span>Chat with Pune Engineer</span>
            </a>
            <a href="/cytos_newcatalog2026_with BG.pdf" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-lg" style="margin-top: 0.5rem; width: 100%; justify-content: center;">
              <span>Download 2026 Machine Catalog (PDF)</span>
            </a>
          </div>

          <div class="engineering-signoff-bar">
            <span class="signoff-icon"><svg viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg></span>
            <span><strong>Technical Specification Verified:</strong> Reviewed by CyTOS Lead CNC Controls &amp; Spindle Specialist • Revision v4.2 (2026)</span>
          </div>
        </div>

        <div class="page-hero-media">
          <img src="/assets/images/machines/educational-cnc-lab.png" alt="Educational & Training CNC Machine Lab Workcell for Engineering Colleges, Pune" title="Educational & Training CNC Machine Lab Workcell for Engineering Colleges, Pune" class="slide-img" fetchpriority="high" style="border-radius: 8px; max-height: 480px; width: 100%; object-fit: contain; background: #ffffff;">
          <div class="page-hero-caption">
            <strong>Featured Model:</strong> Educational & Training CNC Machines • CyTOS EduCNC Series • Manufactured at Bhosari MIDC, Pune
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Performance Highlights Grid -->
  <section class="section" style="background: #ffffff; padding: 2.5rem 0;">
    <div class="container">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.25rem;">
          <div class="spec-cell" style="background: var(--bg-surface); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-subtle); text-align: center;">
            <div class="spec-value" style="font-size: 1.8rem; font-weight: 800; color: var(--brand-primary); margin-bottom: 0.25rem;">100% Safe</div>
            <div class="spec-label" style="font-size: 0.82rem; font-weight: 600; text-transform: uppercase; color: var(--text-secondary);">Enclosed Design</div>
          </div>
          <div class="spec-cell" style="background: var(--bg-surface); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-subtle); text-align: center;">
            <div class="spec-value" style="font-size: 1.8rem; font-weight: 800; color: var(--brand-primary); margin-bottom: 0.25rem;">G & M Code</div>
            <div class="spec-label" style="font-size: 0.82rem; font-weight: 600; text-transform: uppercase; color: var(--text-secondary);">Standard NC Control</div>
          </div>
          <div class="spec-cell" style="background: var(--bg-surface); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-subtle); text-align: center;">
            <div class="spec-value" style="font-size: 1.8rem; font-weight: 800; color: var(--brand-primary); margin-bottom: 0.25rem;">PC Based</div>
            <div class="spec-label" style="font-size: 0.82rem; font-weight: 600; text-transform: uppercase; color: var(--text-secondary);">Simulation & CAM</div>
          </div>
          <div class="spec-cell" style="background: var(--bg-surface); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-subtle); text-align: center;">
            <div class="spec-value" style="font-size: 1.8rem; font-weight: 800; color: var(--brand-primary); margin-bottom: 0.25rem;">Turnkey</div>
            <div class="spec-label" style="font-size: 0.82rem; font-weight: 600; text-transform: uppercase; color: var(--text-secondary);">Lab Curriculum</div>
          </div>
      </div>
    </div>
  </section>

  <!-- In-Depth Engineering Features -->
  <section class="section" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header">
        <div class="hero-badge" style="margin: 0 0 0.75rem;">
          <span>ENGINEERING EXCELLENCE</span>
        </div>
        <h2 class="section-title">Core Machine Design &amp; Architectural Features</h2>
        <p class="section-subtitle">
          Built from the ground up at our Pune works with stress-relieved structures, premium motion hardware, and in-house proprietary controls.
        </p>
      </div>

      <div style="background: #ffffff; padding: 2.5rem; border-radius: 12px; border: 1px solid var(--border-subtle); box-shadow: var(--shadow-sm);">
        <ul style="list-style: none; padding: 0; margin: 0;">
            <li style="display: flex; gap: 0.75rem; margin-bottom: 0.85rem; align-items: flex-start;">
              <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--brand-gold)" stroke-width="2.5" style="flex-shrink: 0; margin-top: 2px;"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span style="color: var(--text-primary); font-size: 0.95rem; line-height: 1.6;">Complete physical safety with transparent shatterproof polycarbonate enclosure and emergency interlock that cuts spindle power if doors open</span>
            </li>
            <li style="display: flex; gap: 0.75rem; margin-bottom: 0.85rem; align-items: flex-start;">
              <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--brand-gold)" stroke-width="2.5" style="flex-shrink: 0; margin-top: 2px;"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span style="color: var(--text-primary); font-size: 0.95rem; line-height: 1.6;">Real-world industrial controller interface teaching students authentic G-code, tool offsets, work coordinates (G54-G59), and feed rate overrides</span>
            </li>
            <li style="display: flex; gap: 0.75rem; margin-bottom: 0.85rem; align-items: flex-start;">
              <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--brand-gold)" stroke-width="2.5" style="flex-shrink: 0; margin-top: 2px;"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span style="color: var(--text-primary); font-size: 0.95rem; line-height: 1.6;">3D graphic toolpath preview and virtual collision simulation before cutting, eliminating accidental tool crashes and student mistakes</span>
            </li>
            <li style="display: flex; gap: 0.75rem; margin-bottom: 0.85rem; align-items: flex-start;">
              <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--brand-gold)" stroke-width="2.5" style="flex-shrink: 0; margin-top: 2px;"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span style="color: var(--text-primary); font-size: 0.95rem; line-height: 1.6;">Versatile multi-material machining capability: students can prototype electronics PCBs, 3D wood sculptures, acrylic signs, and aluminium brackets</span>
            </li>
            <li style="display: flex; gap: 0.75rem; margin-bottom: 0.85rem; align-items: flex-start;">
              <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--brand-gold)" stroke-width="2.5" style="flex-shrink: 0; margin-top: 2px;"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span style="color: var(--text-primary); font-size: 0.95rem; line-height: 1.6;">Comprehensive turnkey delivery: includes student lab exercises, faculty training workshops, and ongoing curriculum support</span>
            </li>
        </ul>
      </div>
    </div>
  </section>

  <!-- Detailed Technical Specifications Table -->
  <section class="section" style="background: #ffffff;">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Factory Verified Technical Specifications</h2>
        <p class="section-subtitle">
          Transparent, factory-tested parameters from the 2026 CyTOS Machine Catalog.
        </p>
      </div>

      <div class="spec-table-container">
        <table class="spec-table">
          <thead>
            <tr>
              <th style="width: 35%;">Specification Parameter</th>
              <th style="width: 45%;">Engineering Value / Standard</th>
              <th style="width: 20%;">Classification</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Machine Category</strong></td>
              <td>Educational Benchtop CNC Machining & Prototyping Trainer</td>
              <td><span class="badge-std">Academic</span></td>
            </tr>
            <tr>
              <td><strong>Working Envelope</strong></td>
              <td>300 × 200 × 60 mm / 300 × 300 × 80 mm</td>
              <td><span class="badge-std">Standard</span></td>
            </tr>
            <tr>
              <td><strong>Safety Housing</strong></td>
              <td>360° Transparent Polycarbonate Enclosure with Door Safety Interlock</td>
              <td><span class="badge-std">100% Safe</span></td>
            </tr>
            <tr>
              <td><strong>Spindle Motor</strong></td>
              <td>800W to 1.5 kW Precision High-Speed Spindle (up to 40,000 RPM)</td>
              <td><span class="badge-std">Variable</span></td>
            </tr>
            <tr>
              <td><strong>Motion Mechanisms</strong></td>
              <td>Hardened Linear Guideways & C7 Precision Ball Screws</td>
              <td><span class="badge-std">Industrial Grade</span></td>
            </tr>
            <tr>
              <td><strong>Drive Motors</strong></td>
              <td>Micro-Step Stepper Motors / Easy Servo Closed-Loop Drives</td>
              <td><span class="badge-std">Standard</span></td>
            </tr>
            <tr>
              <td><strong>Accuracy & Repeatability</strong></td>
              <td>±0.05 mm (Demonstrates Real Industrial Tolerances)</td>
              <td><span class="badge-std">Precision</span></td>
            </tr>
            <tr>
              <td><strong>Operating Software</strong></td>
              <td>CyTOS EduCAM Studio with Real-Time 3D Toolpath Simulation</td>
              <td><span class="badge-std">Included</span></td>
            </tr>
            <tr>
              <td><strong>Supported Languages</strong></td>
              <td>Standard ISO G-Code and M-Code (Fanuc & Siemens compatible syntax)</td>
              <td><span class="badge-std">Universal</span></td>
            </tr>
            <tr>
              <td><strong>Workpiece Clamping</strong></td>
              <td>T-Slot Aluminium Bed with Quick-Action Mechanical Clamps</td>
              <td><span class="badge-std">Standard</span></td>
            </tr>
            <tr>
              <td><strong>Noise Level</strong></td>
              <td>Under 65 dB (Classroom Friendly Operation)</td>
              <td><span class="badge-std">Quiet</span></td>
            </tr>
            <tr>
              <td><strong>Power Supply</strong></td>
              <td>Standard 230V AC Single Phase Domestic Wall Plug (No Industrial 3-Phase Required)</td>
              <td><span class="badge-std">Plug & Play</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- Material Compatibility Matrix -->
  <section class="section" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Tested Substrate &amp; Material Compatibility</h2>
        <p class="section-subtitle">
          Recommended cutting speeds, feeds, and application performance validated on CyTOS test beds.
        </p>
      </div>

      <div class="spec-table-container">
        <table class="spec-table">
          <thead>
            <tr>
              <th style="width: 30%;">Material Substrate</th>
              <th style="width: 15%;">Suitability</th>
              <th style="width: 25%;">Recommended Spindle Speed</th>
              <th style="width: 30%;">Application Notes</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>PCB Copper-Clad Laminates (FR4)</strong></td>
              <td><span class="matrix-status-cell optimal">● Optimal</span></td>
              <td>24,000 – 40,000 RPM</td>
              <td>Chemical-free student circuit design and fabrication</td>
            </tr>
            <tr>
              <td><strong>Aluminium (6061) & Brass Ingots</strong></td>
              <td><span class="matrix-status-cell optimal">● Optimal</span></td>
              <td>18,000 – 24,000 RPM</td>
              <td>Teaches metal cutting speeds, chip loads, and feeds</td>
            </tr>
            <tr>
              <td><strong>Acrylic & Polycarbonate Sheets</strong></td>
              <td><span class="matrix-status-cell optimal">● Optimal</span></td>
              <td>16,000 – 22,000 RPM</td>
              <td>Engraving, optical lens machining, and light guide signs</td>
            </tr>
            <tr>
              <td><strong>Wood, MDF & Modeling Foam</strong></td>
              <td><span class="matrix-status-cell optimal">● Optimal</span></td>
              <td>18,000 – 24,000 RPM</td>
              <td>Rapid 3D surface contouring and industrial design models</td>
            </tr>
            <tr>
              <td><strong>Delrin, Nylon & Engineering Plastics</strong></td>
              <td><span class="matrix-status-cell optimal">● Optimal</span></td>
              <td>16,000 – 20,000 RPM</td>
              <td>Mechanical gears, robot chassis, and mechanical parts</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- Standard Equipment vs Optional Upgrades -->
  <section class="section" style="background: #ffffff;">
    <div class="container">
      <div class="section-header text-center">
        <h2 class="section-title">Standard Package &amp; Factory Custom Options</h2>
        <p class="section-subtitle">
          Configure your machine according to specific production volumes, panel formats, and cycle times.
        </p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem;">
        <div style="background: var(--bg-surface); padding: 2rem; border-radius: 10px; border: 1px solid var(--border-subtle);">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1.25rem;">
            <h3 style="margin: 0; color: var(--text-pure); font-size: 1.25rem;">Standard Factory Package</h3>
            <span class="badge-std" style="background: #10b981; color: #fff;">INCLUDED</span>
          </div>
          <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.92rem; color: var(--text-secondary); line-height: 1.7;">
            <li style="margin-bottom: 0.6rem;">✓ Complete Benchtop CNC Machine with Safety Enclosure and E-Stop</li>
            <li style="margin-bottom: 0.6rem;">✓ Pre-Configured Operator PC with CyTOS EduCAM Software & Simulation</li>
            <li style="margin-bottom: 0.6rem;">✓ Starter Tooling Package (End Mills, V-Carve Bits, Ball Nose, Micro-Drills)</li>
            <li style="margin-bottom: 0.6rem;">✓ Mechanical Clamping Kit, T-Nuts, and Precision Workpiece Vise</li>
            <li style="margin-bottom: 0.6rem;">✓ Faculty Training Session Conducted by CyTOS Application Engineers</li>
            <li style="margin-bottom: 0.6rem;">✓ 12-Month Institutional Warranty and Technical Phone/Email Support</li>
          </ul>
        </div>

        <div style="background: var(--bg-surface); padding: 2rem; border-radius: 10px; border: 1px solid var(--brand-gold-border); box-shadow: var(--shadow-sm);">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1.25rem;">
            <h3 style="margin: 0; color: var(--text-pure); font-size: 1.25rem;">Optional Factory Upgrades</h3>
            <span class="badge-std" style="background: var(--brand-gold); color: #fff;">CUSTOMIZABLE</span>
          </div>
          <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.92rem; color: var(--text-secondary); line-height: 1.7;">
            <li style="margin-bottom: 0.6rem;">+ Rotary 4th Axis Attachment for Teaching 4-Axis Simultaneous Machining</li>
            <li style="margin-bottom: 0.6rem;">+ Automated Surface Touch Probe for Auto Z-Zero Leveling Demonstration</li>
            <li style="margin-bottom: 0.6rem;">+ Compact Laboratory HEPA Dust Extractor with Anti-Static Hose</li>
            <li style="margin-bottom: 0.6rem;">+ Annual Institutional Maintenance & Faculty Refresher Training Contract</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- Visual Image Gallery for Image SEO -->
  <section class="section" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Machine Gallery &amp; Detail Views</h2>
        <p class="section-subtitle">
          High-resolution engineering views of components, spindle tapers, and electronic control architecture.
        </p>
      </div>

      <div style="display: flex; flex-wrap: wrap; gap: 1.5rem;">
          <div style="flex: 1; min-width: 260px; background: #ffffff; border: 1px solid var(--border-subtle); border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
            <img src="/assets/images/machines/pcb-prototyping-pcb30.png" alt="Chemical-Free Student PCB Prototyping Trainer, Pune" title="Chemical-Free Student PCB Prototyping Trainer, Pune" loading="lazy" style="width: 100%; height: 220px; object-fit: cover; display: block;">
            <div style="padding: 1rem;">
              <strong style="color: var(--text-pure); font-size: 0.9rem; display: block; margin-bottom: 0.35rem;">Chemical-Free Student PCB Prototyping Trainer, Pune</strong>
              <p style="color: var(--text-secondary); font-size: 0.82rem; margin: 0; line-height: 1.5;">Safe tabletop isolation milling and circuit fabrication workstation designed for student electronics labs.</p>
            </div>
          </div>
          <div style="flex: 1; min-width: 260px; background: #ffffff; border: 1px solid var(--border-subtle); border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
            <img src="/assets/images/machines/precision-machining-parts.png" alt="Student CNC Milling Project Samples, Pune" title="Student CNC Milling Project Samples, Pune" loading="lazy" style="width: 100%; height: 220px; object-fit: cover; display: block;">
            <div style="padding: 1rem;">
              <strong style="color: var(--text-pure); font-size: 0.9rem; display: block; margin-bottom: 0.35rem;">Student CNC Milling Project Samples, Pune</strong>
              <p style="color: var(--text-secondary); font-size: 0.82rem; margin: 0; line-height: 1.5;">3D engraved badges, nameplates, aluminium components, and circuit boards fabricated by students.</p>
            </div>
          </div>
      </div>
    </div>
  </section>

  <!-- Live Cutting Trial Banner -->
  <section class="section" style="background: #ffffff;">
    <div class="container">
      <div class="sample-trial-banner" style="background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%); border: 2px solid var(--brand-gold-border); padding: 2.5rem; border-radius: 12px; display: grid; grid-template-columns: 1.6fr 1fr; gap: 2rem; align-items: center;">
        <div>
          <div class="hero-badge" style="margin-bottom: 0.75rem;">
            <span>ZERO-RISK TECHNICAL EVALUATION</span>
          </div>
          <h2 style="font-size: 1.85rem; color: var(--text-pure); margin-bottom: 1rem;">
            Schedule a Live Cutting Trial on the Educational & Training CNC Machines
          </h2>
          <p style="color: var(--text-secondary); line-height: 1.6; margin-bottom: 1.5rem;">
            Bring your material or send component drawings (DXF/STEP/Gerber) to our Bhosari MIDC works in Pune. Our application specialists will run a live trial, calculate cycle times, measure edge finish, and provide a full technical report.
          </p>
          <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
            <button class="btn btn-primary btn-lg" data-open-rfq data-machine="Educational & Training CNC Machines Live Trial">
              <span>Book Live Trial at Pune Works</span>
            </button>
            <a href="https://wa.me/919921381071?text=Hi%20CyTOS,%20I%20want%20to%20send%20a%20drawing%20for%20a%20cutting%20trial%20on%20Educational & Training CNC Machines." class="btn btn-whatsapp btn-lg" target="_blank" rel="noopener noreferrer">
              <span>Send Drawing on WhatsApp</span>
            </a>
          </div>
        </div>

        <div style="background: #ffffff; padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-subtle); box-shadow: var(--shadow-sm);">
          <h4 style="color: var(--text-pure); margin-bottom: 0.75rem;">Trial Execution Protocol:</h4>
          <ol style="padding-left: 1.25rem; font-size: 0.88rem; color: var(--text-secondary); line-height: 1.8; margin: 0;">
            <li>Share DXF/Gerber or courier sample stock to Pune.</li>
            <li>Application engineer calculates optimal feed &amp; speed.</li>
            <li>Trial executed live with video recording.</li>
            <li>Finished parts &amp; cycle analysis returned in 48 hours.</li>
          </ol>
        </div>
      </div>
    </div>
  </section>

  <!-- Frequently Asked Questions -->
  <section class="section" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header text-center">
        <h2 class="section-title">Frequently Asked Questions</h2>
        <p class="section-subtitle">
          Direct engineering answers about specifications, tooling, delivery, and support for the Educational & Training CNC Machines.
        </p>
      </div>

      <div style="max-width: 860px; margin: 0 auto;">
        <details class="faq-item" style="background: #ffffff; padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-subtle); margin-bottom: 0.85rem;">
          <summary style="font-weight: 700; color: var(--text-pure); cursor: pointer; font-size: 1.05rem;">Why should colleges invest in CyTOS Educational CNC machines over consumer CNC kits?</summary>
          <p style="margin-top: 0.75rem; color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">Consumer hobby kits use weak 3D-printed parts, belt drives, and unstable open-source controllers that break quickly under student use. CyTOS Educational machines are built with genuine industrial ball screws, linear guides, and steel frames, offering real industrial reliability, accuracy, and Fanuc/Siemens-compatible G-code syntax.</p>
        </details>
        <details class="faq-item" style="background: #ffffff; padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-subtle); margin-bottom: 0.85rem;">
          <summary style="font-weight: 700; color: var(--text-pure); cursor: pointer; font-size: 1.05rem;">What training is provided for faculty and lab assistants?</summary>
          <p style="margin-top: 0.75rem; color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">We conduct an extensive hands-on faculty training program upon installation. Our engineers guide instructors through machine operation, safety protocols, CAD-to-CAM workflow, tooling selection, and troubleshooting so faculty can confidently teach student batches.</p>
        </details>
        <details class="faq-item" style="background: #ffffff; padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-subtle); margin-bottom: 0.85rem;">
          <summary style="font-weight: 700; color: var(--text-pure); cursor: pointer; font-size: 1.05rem;">Is special three-phase power or compressed air needed in the lab?</summary>
          <p style="margin-top: 0.75rem; color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">No. The CyTOS Educational CNC machine runs on standard 230V AC single-phase power from a regular domestic socket, requiring no special electrical substation or high-pressure plant air.</p>
        </details>
        <details class="faq-item" style="background: #ffffff; padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-subtle); margin-bottom: 0.85rem;">
          <summary style="font-weight: 700; color: var(--text-pure); cursor: pointer; font-size: 1.05rem;">Can students use standard CAD/CAM software like Fusion 360 or SolidWorks?</summary>
          <p style="margin-top: 0.75rem; color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">Yes. CyTOS EduCAM accepts standard G-code exported from Autodesk Fusion 360, SolidWorks, Mastercam, Creo, NX, and EDA packages like Altium, KiCad, and Eagle.</p>
        </details>
      </div>
    </div>
  </section>

  <!-- Related Precision Machines -->
  <section class="section" style="background: #ffffff;">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Explore Related Precision Machines</h2>
        <p class="section-subtitle">
          Discover other industrial CNC routers, PCB machines, and automation cells manufactured by CyTOS in Pune.
        </p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
          <article class="machine-card" style="background: #ffffff; border: 1px solid var(--border-subtle); border-radius: 10px; overflow: hidden; display: flex; flex-direction: column;">
            <div class="machine-img-box" style="height: 220px; overflow: hidden; background: #f8fafc; position: relative;">
              <img src="/assets/images/machines/pcb-drilling-pcb60.png" alt="CNC 6060 PCB Drilling & Routing Machine" title="CNC 6060 PCB Drilling and Routing Machine Double Spindle with ATC, Pune, India" loading="lazy" style="width: 100%; height: 100%; object-fit: contain; padding: 1rem;">
              <div class="machine-badge-tag" style="position: absolute; top: 10px; left: 10px; background: rgba(15,23,42,0.85); color: #fff; font-size: 0.72rem; padding: 3px 8px; border-radius: 4px; font-weight: 700;">100,000 RPM ULTRA-HIGH SPEED</div>
            </div>
            <div class="machine-body" style="padding: 1.5rem; flex: 1; display: flex; flex-direction: column;">
              <h3 class="machine-name" style="font-size: 1.15rem; color: var(--text-pure); margin-bottom: 0.5rem;"><a href="/cnc-6060-pcb-drilling-routing-machine" style="text-decoration: none; color: inherit;">CNC 6060 PCB Drilling & Routing Machine</a></h3>
              <p style="font-size: 0.88rem; color: var(--text-secondary); flex: 1; margin-bottom: 1.25rem;">Industrial floor-mounted PCB production machine with 18,000 to 100,000 RPM electro-spindles, 0.2 mm micro-hole drilling capability, dowel-pi...</p>
              <div style="display: flex; gap: 0.5rem;">
                <a href="/cnc-6060-pcb-drilling-routing-machine" class="btn btn-outline btn-block" style="text-align: center; text-decoration: none;">View Model ❯</a>
                <button class="btn btn-primary" data-open-rfq data-machine="CNC 6060 PCB Drilling & Routing Machine">Quote</button>
              </div>
            </div>
          </article>
          <article class="machine-card" style="background: #ffffff; border: 1px solid var(--border-subtle); border-radius: 10px; overflow: hidden; display: flex; flex-direction: column;">
            <div class="machine-img-box" style="height: 220px; overflow: hidden; background: #f8fafc; position: relative;">
              <img src="/assets/images/machines/pcb-prototyping-pcb30.png" alt="CNC 3020 PCB Rapid Prototyping Machine" title="CNC 3020 Chemical-Free Desktop PCB Rapid Prototyping Machine, Pune, India" loading="lazy" style="width: 100%; height: 100%; object-fit: contain; padding: 1rem;">
              <div class="machine-badge-tag" style="position: absolute; top: 10px; left: 10px; background: rgba(15,23,42,0.85); color: #fff; font-size: 0.72rem; padding: 3px 8px; border-radius: 4px; font-weight: 700;">100% CHEMICAL-FREE PROTOTYPING</div>
            </div>
            <div class="machine-body" style="padding: 1.5rem; flex: 1; display: flex; flex-direction: column;">
              <h3 class="machine-name" style="font-size: 1.15rem; color: var(--text-pure); margin-bottom: 0.5rem;"><a href="/cnc-3020-pcb-prototyping-machine" style="text-decoration: none; color: inherit;">CNC 3020 PCB Rapid Prototyping Machine</a></h3>
              <p style="font-size: 0.88rem; color: var(--text-secondary); flex: 1; margin-bottom: 1.25rem;">Compact tabletop PCB isolation milling machine engineered specifically for corporate R&D departments, defense labs, and engineering colleges...</p>
              <div style="display: flex; gap: 0.5rem;">
                <a href="/cnc-3020-pcb-prototyping-machine" class="btn btn-outline btn-block" style="text-align: center; text-decoration: none;">View Model ❯</a>
                <button class="btn btn-primary" data-open-rfq data-machine="CNC 3020 PCB Rapid Prototyping Machine">Quote</button>
              </div>
            </div>
          </article>
          <article class="machine-card" style="background: #ffffff; border: 1px solid var(--border-subtle); border-radius: 10px; overflow: hidden; display: flex; flex-direction: column;">
            <div class="machine-img-box" style="height: 220px; overflow: hidden; background: #f8fafc; position: relative;">
              <img src="/assets/images/machines/pcb-prototyping-pcb30.png" alt="CNC 3030 High Precision PCB Drilling & Routing Machine" title="CyTOS CNC 3030 Heavy-Duty High-Precision PCB Drilling & Routing Machine, Pune" loading="lazy" style="width: 100%; height: 100%; object-fit: contain; padding: 1rem;">
              <div class="machine-badge-tag" style="position: absolute; top: 10px; left: 10px; background: rgba(15,23,42,0.85); color: #fff; font-size: 0.72rem; padding: 3px 8px; border-radius: 4px; font-weight: 700;">60,000 RPM HIGH PRECISION</div>
            </div>
            <div class="machine-body" style="padding: 1.5rem; flex: 1; display: flex; flex-direction: column;">
              <h3 class="machine-name" style="font-size: 1.15rem; color: var(--text-pure); margin-bottom: 0.5rem;"><a href="/cnc-3030-pcb-prototyping-machine" style="text-decoration: none; color: inherit;">CNC 3030 High Precision PCB Drilling & Routing Machine</a></h3>
              <p style="font-size: 0.88rem; color: var(--text-secondary); flex: 1; margin-bottom: 1.25rem;">Heavy-duty benchtop CNC machine with travel speeds up to 166 mm/sec (10,000 mm/min), spindle options up to 60,000 RPM 1.5 kW, closed-loop AC...</p>
              <div style="display: flex; gap: 0.5rem;">
                <a href="/cnc-3030-pcb-prototyping-machine" class="btn btn-outline btn-block" style="text-align: center; text-decoration: none;">View Model ❯</a>
                <button class="btn btn-primary" data-open-rfq data-machine="CNC 3030 High Precision PCB Drilling & Routing Machine">Quote</button>
              </div>
            </div>
          </article>
      </div>
    </div>
  </section>

  <!-- Pre-Footer Engineering Hotline Conversion Bar -->
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

`;

export default function EducationalCncPage() {
  return (
    <HtmlPageWrapper
      htmlContent={pageHtml}
      title="Educational CNC Machines - Desktop & Benchtop Training CNC Machine Manufacturer from Pune | CyTOS"
      description="Manufacturer of Educational CNC Machines - Compact training CNC milling, router, and PCB machines with safety enclosures for engineering colleges and labs. CyTOS Pune."
      canonical="https://www.cytos.in/educational-cnc-machines"
    />
  );
}
