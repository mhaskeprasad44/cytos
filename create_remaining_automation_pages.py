# -*- coding: utf-8 -*-
"""
create_remaining_automation_pages.py
Creates pneumatic-welding-fixtures.html and plc-control-panels.html
"""

import os
from create_automation_pages import TOP_BAR_HTML, get_header_html, FOOTER_HTML, FLOATING_BAR_HTML, MODAL_HTML

PROJECT_DIR = r"c:\Users\PrasadMhaske\Downloads\Project1"

# -------------------------------------------------------------
# 2. PAGE: pneumatic-welding-fixtures.html
# -------------------------------------------------------------
PNEUMATIC_FIXTURES_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="64x64" href="favicon.png">
  <link rel="apple-touch-icon" href="favicon.png">

  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
  new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  }})(window,document,'script','dataLayer','GTM-P6DNQQ3H');</script>
  <!-- End Google Tag Manager -->

  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-TLPML4D2SB"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-TLPML4D2SB');
  </script>

  <!-- Microsoft Clarity -->
  <script type="text/javascript">
      (function(c,l,a,r,i,t,y){{
          c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
          t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
          y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
      }})(window, document, "clarity", "script", "ypy7znoaq7");
  </script>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pneumatic Welding Fixtures &amp; 90° Rotary Indexing Jigs | CyTOS Pune</title>
  <meta name="description" content="Heavy-duty pneumatic welding fixtures, 90°/180° rotary turnover jigs, and robotic MIG/TIG welding tooling manufactured in Pune by CyTOS. Up to 15 kN clamping force, hardened tool steel locators, zero thermal distortion.">
  <meta name="keywords" content="pneumatic welding fixture Pune, welding jig manufacturer India, robotic welding fixture Pune, 90 degree rotary welding jig, automotive chassis welding fixture, toggle clamp welding jig Pune">
  <link rel="canonical" href="https://cytos.in/pneumatic-welding-fixtures.html">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,500;0,700;0,900;1,400;1,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "CyTOS Heavy-Duty Pneumatic Welding Fixtures",
    "image": "https://cytos.in/assets/images/blogs/pneumatic-welding-fixtures-16x9.jpg",
    "description": "High-durability pneumatic welding fixtures with 90°/180° rotary turnover tables, hardened D2 tool steel locators, and integrated clamp sensor interlocks for robotic and manual welding.",
    "brand": {{
      "@type": "Brand",
      "name": "CyTOS"
    }},
    "manufacturer": {{
      "@type": "Organization",
      "name": "CyTOS - Cycle Time Optimising Solutions",
      "url": "https://cytos.in"
    }},
    "offers": {{
      "@type": "AggregateOffer",
      "priceCurrency": "INR",
      "availability": "https://schema.org/InStock",
      "price": "Custom Engineering Quote"
    }}
  }}
  </script>
</head>
<body>
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-P6DNQQ3H"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->

{TOP_BAR_HTML}
{get_header_html("pneumatic-welding-fixtures.html")}

  <!-- Breadcrumbs -->
  <div class="breadcrumbs-bar">
    <div class="container">
      <div class="breadcrumbs-list">
        <a href="index.html">Home</a>
        <span class="breadcrumb-separator">/</span>
        <a href="spm-automation.html">Automation &amp; SPM</a>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-current">Pneumatic Welding Fixtures</span>
      </div>
    </div>
  </div>

  <!-- Page Hero -->
  <section class="page-hero">
    <div class="container">
      <div class="page-hero-grid">
        <div class="page-hero-content">
          <div class="hero-badge">
            <span>HEAVY-DUTY FABRICATION TOOLING • PUNE</span>
          </div>
          <h1 class="page-hero-title">Pneumatic Welding Fixtures &amp; 90° Rotary Indexing Jigs</h1>
          <p class="page-hero-subtitle">
            Eliminate weld distortion, dimensional out-of-squareness, and slow manual clamping. CyTOS engineers high-rigidity pneumatic welding jigs, 90°/180° rotary turnover tables, and robotic weld tooling in Pune with hardened D2 tool steel locators and up to 15 kN clamping force.
          </p>
          
          <div class="answer-first-callout">
            <strong>In brief:</strong> CyTOS manufactures custom pneumatic welding fixtures for automotive chassis fabricators, tractor cabin builders, and sheet metal enclosure manufacturers. Built with stress-relieved steel base plates, hardened locator pins (58–62 HRC), pneumatic toggle cylinders with magnetic reed switches, and copper-chromium backing chill plates, our fixtures cut welding cycle times by 40% to 60%.
          </div>

          <div class="slide-cta-row">
            <button class="btn btn-primary btn-lg" data-open-rfq data-machine="Pneumatic Welding Fixture">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="btn-icon-svg" aria-hidden="true"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect><path d="M9 12h6"></path><path d="M9 16h6"></path></svg> <span>Request Welding Fixture Feasibility</span>
            </button>
            <a href="https://wa.me/919921381071?text=Hi%20CyTOS,%20we%20have%20a%20welding%20fixture%20requirement%20to%20discuss." class="btn btn-secondary btn-lg" target="_blank" rel="noopener noreferrer">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="btn-icon-svg" aria-hidden="true"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg> <span>Discuss on WhatsApp with Tooling Lead</span>
            </a>
          </div>

          <div class="engineering-signoff-bar">
            <span class="signoff-icon"><svg viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg></span>
            <span><strong>Anti-Spatter Protection:</strong> Heavy-duty copper-chromium backing blocks, shielded pneumatic piping, and spatter-resistant shroud coatings guarantee 24×7 multi-shift longevity.</span>
          </div>
        </div>

        <div class="page-hero-media">
          <img src="assets/images/blogs/pneumatic-welding-fixtures-16x9.jpg" alt="Pneumatic Welding Fixture Pune CyTOS">
          <div class="page-hero-caption">
            <strong>Featured Tooling:</strong> CyTOS Heavy Pneumatic Welding Jig with 90° Indexing, Pneumatic Clamping &amp; Poka-Yoke Sensors
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 4 Core Welding Fixture Categories -->
  <section class="section" style="background: #ffffff;">
    <div class="container">
      <div class="section-header text-center">
        <div class="hero-badge" style="margin: 0 auto 1rem;">
          <span>WELDING TOOLING PORTFOLIO</span>
        </div>
        <h2 class="section-title">Four Pneumatic Welding Tooling Solutions</h2>
        <p class="section-subtitle">
          Engineered for robotic MIG/TIG cells, manual welding lines, and complex tubular assemblies.
        </p>
      </div>

      <div class="model-cards-grid" style="grid-template-columns: repeat(4, 1fr);">
        
        <!-- Category 1: 90° / 180° Turnover Jigs -->
        <article class="model-card">
          <div class="model-card-header">
            <div class="model-name">90° / 180° Turnover Jigs</div>
            <div class="model-subhead">Two-Sided Weld Access</div>
          </div>
          <div class="model-card-media">
            <img src="assets/images/machines/spm-pneumatic-fixture.jpg" alt="90 degree rotary welding turnover jig">
          </div>
          <div class="model-card-body">
            <p style="font-size: 0.875rem; color: var(--text-secondary);">
              Counterbalanced pneumatic trunnion or rotary turnover tables allowing the welder to access both top and bottom joints without un-clamping.
            </p>
            <ul class="model-specs-list">
              <li><span class="spec-label">Rotation</span><span class="spec-val">0°, 90°, 180° pneumatic lock</span></li>
              <li><span class="spec-label">Payload</span><span class="spec-val">Up to 800 kg frame</span></li>
              <li><span class="spec-label">Locking</span><span class="spec-val">Shot-pin pneumatic lock</span></li>
            </ul>
          </div>
          <div class="model-card-footer">
            <button class="btn btn-primary btn-block" data-open-rfq data-machine="90-Degree Turnover Welding Jig">Quote Turnover Jig</button>
          </div>
        </article>

        <!-- Category 2: Rotary Dial Welding Tables -->
        <article class="model-card">
          <div class="model-card-header">
            <div class="model-name">Rotary Dial Tables</div>
            <div class="model-subhead">High-Takt Production</div>
          </div>
          <div class="model-card-media">
            <img src="assets/images/blogs/spm-rotary-indexing-table.jpg" alt="Rotary Dial Welding Table Pune">
          </div>
          <div class="model-card-body">
            <p style="font-size: 0.875rem; color: var(--text-secondary);">
              2-station or 4-station indexing dial table separating operator load/unload station from the robotic welding booth with flash barrier shielding.
            </p>
            <ul class="model-specs-list">
              <li><span class="spec-label">Indexing</span><span class="spec-val">Cam-indexer &lt; 1.5s</span></li>
              <li><span class="spec-label">Stations</span><span class="spec-val">2 or 4 Stations</span></li>
              <li><span class="spec-label">Flash Barrier</span><span class="spec-val">Integrated optical shield</span></li>
            </ul>
          </div>
          <div class="model-card-footer">
            <button class="btn btn-primary btn-block" data-open-rfq data-machine="Rotary Dial Welding Table">Quote Rotary Table</button>
          </div>
        </article>

        <!-- Category 3: Heavy Toggle Clamp Jigs -->
        <article class="model-card">
          <div class="model-card-header">
            <div class="model-name">Pneumatic Toggle Jigs</div>
            <div class="model-subhead">High Clamping Force</div>
          </div>
          <div class="model-card-media">
            <img src="assets/images/blogs/pneumatic-toggle-clamp-jig.jpg" alt="Heavy duty pneumatic toggle clamp fixture">
          </div>
          <div class="model-card-body">
            <p style="font-size: 0.875rem; color: var(--text-secondary);">
              Heavy pneumatic toggle link cylinders providing mechanical over-center locking; clamps remain securely locked even if air pressure drops.
            </p>
            <ul class="model-specs-list">
              <li><span class="spec-label">Clamping Force</span><span class="spec-val">5 kN to 15 kN per clamp</span></li>
              <li><span class="spec-label">Lock Mechanism</span><span class="spec-val">Over-center mechanical lock</span></li>
              <li><span class="spec-label">Sensors</span><span class="spec-val">Clamp open/closed feedback</span></li>
            </ul>
          </div>
          <div class="model-card-footer">
            <button class="btn btn-primary btn-block" data-open-rfq data-machine="Pneumatic Toggle Clamp Jig">Quote Toggle Jig</button>
          </div>
        </article>

        <!-- Category 4: Chassis Sub-Assembly Tooling -->
        <article class="model-card">
          <div class="model-card-header">
            <div class="model-name">Chassis Frame Tooling</div>
            <div class="model-subhead">Automotive Tubular Frames</div>
          </div>
          <div class="model-card-media">
            <img src="assets/images/case-study-welding.jpg" alt="Automotive Chassis Frame Welding Fixture">
          </div>
          <div class="model-card-body">
            <p style="font-size: 0.875rem; color: var(--text-secondary);">
              Precision dimensional locators with hardened guide pins and Poka-Yoke sensors ensuring 100% correct component orientation before welding commences.
            </p>
            <ul class="model-specs-list">
              <li><span class="spec-label">Locators</span><span class="spec-val">D2 steel 58-62 HRC</span></li>
              <li><span class="spec-label">Poka-Yoke</span><span class="spec-val">Inductive part presence</span></li>
              <li><span class="spec-label">Base Plate</span><span class="spec-val">Stress-relieved ground MS</span></li>
            </ul>
          </div>
          <div class="model-card-footer">
            <button class="btn btn-primary btn-block" data-open-rfq data-machine="Chassis Frame Welding Tooling">Quote Frame Tooling</button>
          </div>
        </article>

      </div>
    </div>
  </section>

  <!-- Technical Specifications Table -->
  <section class="section" style="background: var(--bg-surface);">
    <div class="container">
      <div class="section-header text-center">
        <div class="hero-badge" style="margin: 0 auto 1rem;">
          <span>ENGINEERING SPECIFICATIONS</span>
        </div>
        <h2 class="section-title">Pneumatic Welding Fixture Comparison</h2>
        <p class="section-subtitle">
          Precision ground datum blocks, copper heat sinks, and pneumatic sequence logic built for zero thermal distortion.
        </p>
      </div>

      <div class="table-responsive">
        <table class="specs-table">
          <thead>
            <tr>
              <th>Specification Parameter</th>
              <th>90°/180° Turnover Fixture</th>
              <th>Rotary Dial Table Jig</th>
              <th>Stationary Robotic Tooling</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Clamping Mechanism</strong></td>
              <td>Pneumatic toggle cylinders with mechanical lock</td>
              <td>Multi-point pneumatic clamp sequencing</td>
              <td>High-force toggle clamps + pneumatic pushers</td>
            </tr>
            <tr>
              <td><strong>Clamping Force Range</strong></td>
              <td>2.5 kN to 10 kN per clamp point</td>
              <td>3.5 kN to 12 kN per clamp point</td>
              <td>5.0 kN to 15 kN per clamp point</td>
            </tr>
            <tr>
              <td><strong>Locator Pin Hardness</strong></td>
              <td>D2 / EN31 Tool Steel, Vacuum Hardened 58–62 HRC</td>
              <td>D2 Tool Steel, Hard Chrome Plated 60 HRC</td>
              <td>Carbide tipped or D2 hardened 60 HRC</td>
            </tr>
            <tr>
              <td><strong>Thermal Heat Dissipation</strong></td>
              <td>CuCrZr Copper-Chromium backing chill plates</td>
              <td>Integrated copper weld backing bars</td>
              <td>Water-cooled copper backing blocks (Optional)</td>
            </tr>
            <tr>
              <td><strong>Indexing Mechanism</strong></td>
              <td>Pneumatic cylinder rack &amp; pinion / Trunnion</td>
              <td>Heavy-duty barrel cam indexer with brake motor</td>
              <td>Stationary base / Pneumatic slide shuttle</td>
            </tr>
            <tr>
              <td><strong>Part Presence Sensors</strong></td>
              <td>Balluff / Omron weld-spatter immune inductive sensors</td>
              <td>High-temperature inductive proximity sensors</td>
              <td>Integrated optical &amp; inductive Poka-Yoke sensors</td>
            </tr>
            <tr>
              <td><strong>Safety Interlocks</strong></td>
              <td>Dual-hand tie-down buttons, shot-pin engaged sensor</td>
              <td>Optical safety light curtain, perimeter enclosure</td>
              <td>Robot controller safety circuit Category 4</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- Real Pune Case Study -->
  <section class="section" style="background: #ffffff;">
    <div class="container">
      <div class="section-header text-center">
        <div class="hero-badge" style="margin: 0 auto 1rem;">
          <span>VERIFIED SHOP FLOOR CASE STUDY</span>
        </div>
        <h2 class="section-title">Two-Wheeler Chassis Robotic Welding Line</h2>
        <p class="section-subtitle">
          How CyTOS cut frame welding takt time by 55% with a 90° pneumatic turnover indexing jig for a Tier-1 OEM in Bhosari, Pune.
        </p>
      </div>

      <div class="case-study-card" style="background: var(--bg-surface); border: 1px solid var(--border-light); border-radius: 12px; padding: 2.5rem; max-width: 960px; margin: 0 auto;">
        <div class="case-study-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem; align-items: center;">
          <div>
            <h3 style="color: var(--brand-navy); font-size: 1.4rem; margin-bottom: 1rem;">The Engineering Challenge</h3>
            <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.25rem;">
              A major two-wheeler chassis supplier was welding tubular steel frame assemblies using manual screw clamps on a flat welding bench. Operators had to manually unclamp, flip, and re-clamp the 28 kg chassis to weld bottom brackets, causing 85 seconds of handling takt time and angular distortion exceeding 2.5 mm.
            </p>
            <h3 style="color: var(--brand-navy); font-size: 1.4rem; margin-bottom: 1rem;">The CyTOS Solution</h3>
            <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">
              CyTOS designed a heavy-duty pneumatic fixture mounted on a 90° trunnion turnover axis. Featuring 8 sequenced pneumatic toggle clamps, copper-chromium chill backing plates, and inductive sensors that verify tube nesting before welding, the entire chassis is rotated effortlessly for continuous robotic welding.
            </p>
          </div>
          <div>
            <div style="background: #ffffff; border: 1px solid var(--border-light); border-radius: 8px; padding: 1.5rem;">
              <h4 style="color: var(--brand-gold-dark); font-size: 1.1rem; margin-bottom: 1rem; border-bottom: 2px solid var(--border-light); padding-bottom: 0.5rem;">Cycle Time &amp; Dimensional Impact</h4>
              <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.92rem; color: var(--text-secondary);">
                <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-light); display: flex; justify-content: space-between;">
                  <span>Manual Clamping &amp; Flip Takt:</span>
                  <strong style="color: #ef4444;">85 seconds</strong>
                </li>
                <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-light); display: flex; justify-content: space-between;">
                  <span>CyTOS Pneumatic Index Takt:</span>
                  <strong style="color: #10b981;">38 seconds (-55%)</strong>
                </li>
                <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-light); display: flex; justify-content: space-between;">
                  <span>Chassis Angular Distortion:</span>
                  <strong style="color: #10b981;">Reduced from 2.5mm to 0.3mm</strong>
                </li>
                <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-light); display: flex; justify-content: space-between;">
                  <span>Weld Spatter Clean-Up Time:</span>
                  <strong style="color: #10b981;">Reduced by 80%</strong>
                </li>
                <li style="padding: 0.6rem 0; display: flex; justify-content: space-between;">
                  <span>Capital Investment Payback:</span>
                  <strong style="color: var(--brand-navy);">4.2 Months</strong>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ Section with Schema -->
  <section class="section" style="background: var(--bg-surface);" itemscope itemtype="https://schema.org/FAQPage">
    <div class="container" style="max-width: 860px;">
      <div class="section-header text-center">
        <div class="hero-badge" style="margin: 0 auto 1rem;">
          <span>ENGINEERING FAQS</span>
        </div>
        <h2 class="section-title">Pneumatic Welding Fixture FAQs</h2>
        <p class="section-subtitle">Common technical questions on locator materials, clamping forces, and spatter management answered by CyTOS tooling designers.</p>
      </div>

      <div class="faq-accordion">
        <details class="faq-item" itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
          <summary class="faq-question" itemprop="name">How do CyTOS welding fixtures ensure clamps stay locked if shop pneumatic pressure drops?</summary>
          <div class="faq-answer" itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
            <p itemprop="text">
              We employ mechanical over-center toggle clamps. When the pneumatic cylinder fully extends, the linkage passes over dead center and locks mechanically. Even if airline pressure is completely lost, the workpiece remains rigidly clamped until reverse air pressure is actively commanded.
            </p>
          </div>
        </details>

        <details class="faq-item" itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
          <summary class="faq-question" itemprop="name">How does CyTOS protect pneumatic lines and sensors from intense MIG welding heat and spatter?</summary>
          <div class="faq-answer" itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
            <p itemprop="text">
              All pneumatic tubing is routed inside stainless steel braided armor or covered beneath machined steel deflectors. Proximity sensors feature PTFE spatter-resistant coatings and ceramic sensing faces specifically designed for resistance and arc welding cells.
            </p>
          </div>
        </details>

        <details class="faq-item" itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
          <summary class="faq-question" itemprop="name">Can CyTOS manufacture fixtures for robotic welding cells (Fanuc, Yaskawa, ABB, KUKA)?</summary>
          <div class="faq-answer" itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
            <p itemprop="text">
              Yes. We regularly design and build fixtures for integration onto 1-axis and 2-axis robotic positioners (headstock/tailstock or L-positioners). All electrical signals from clamp reed switches and part-presence sensors are consolidated into an IP67 junction box with standardized digital I/O for direct robotic handshake.
            </p>
          </div>
        </details>
      </div>
    </div>
  </section>

{FOOTER_HTML}
{FLOATING_BAR_HTML}
{MODAL_HTML}

  <script src="script.js"></script>
</body>
</html>
"""

# -------------------------------------------------------------
# 3. PAGE: plc-control-panels.html
# -------------------------------------------------------------
PLC_CONTROL_PANELS_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="64x64" href="favicon.png">
  <link rel="apple-touch-icon" href="favicon.png">

  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
  new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  }})(window,document,'script','dataLayer','GTM-P6DNQQ3H');</script>
  <!-- End Google Tag Manager -->

  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-TLPML4D2SB"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-TLPML4D2SB');
  </script>

  <!-- Microsoft Clarity -->
  <script type="text/javascript">
      (function(c,l,a,r,i,t,y){{
          c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
          t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
          y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
      }})(window, document, "clarity", "script", "ypy7znoaq7");
  </script>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Industrial PLC Automation Control Panels | Siemens S7 &amp; Delta | CyTOS Pune</title>
  <meta name="description" content="Custom turnkey PLC industrial control panels, Siemens S7-1200/1500 &amp; Delta programming, VFD drive integration, and HMI touchscreens engineered in Pune by CyTOS. IP55 powder-coated enclosures, neat ferruled wiring, Category 3/4 safety circuits.">
  <meta name="keywords" content="PLC control panel manufacturer Pune, industrial automation panel India, Siemens S7 PLC panel Pune, Delta PLC automation panel, VFD control panel manufacturer, electrical control panel Pune, SPM automation panel">
  <link rel="canonical" href="https://cytos.in/plc-control-panels.html">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,500;0,700;0,900;1,400;1,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "CyTOS Turnkey Industrial PLC Control Panels",
    "image": "https://cytos.in/assets/images/blogs/plc-control-panel-automation.jpg",
    "description": "Turnkey industrial PLC automation control panels designed, wired, and programmed with Siemens S7-1200/1500, Delta PLCs, Schneider switchgear, VFDs, and touchscreen HMIs.",
    "brand": {{
      "@type": "Brand",
      "name": "CyTOS"
    }},
    "manufacturer": {{
      "@type": "Organization",
      "name": "CyTOS - Cycle Time Optimising Solutions",
      "url": "https://cytos.in"
    }},
    "offers": {{
      "@type": "AggregateOffer",
      "priceCurrency": "INR",
      "availability": "https://schema.org/InStock",
      "price": "Custom Engineering Quote"
    }}
  }}
  </script>
</head>
<body>
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-P6DNQQ3H"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->

{TOP_BAR_HTML}
{get_header_html("plc-control-panels.html")}

  <!-- Breadcrumbs -->
  <div class="breadcrumbs-bar">
    <div class="container">
      <div class="breadcrumbs-list">
        <a href="index.html">Home</a>
        <span class="breadcrumb-separator">/</span>
        <a href="spm-automation.html">Automation &amp; SPM</a>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-current">PLC Industrial Control Panels</span>
      </div>
    </div>
  </div>

  <!-- Page Hero -->
  <section class="page-hero">
    <div class="container">
      <div class="page-hero-grid">
        <div class="page-hero-content">
          <div class="hero-badge">
            <span>TURNKEY ELECTRICAL AUTOMATION • SIEMENS / DELTA</span>
          </div>
          <h1 class="page-hero-title">Industrial PLC Automation Control Panels &amp; Systems</h1>
          <p class="page-hero-subtitle">
            Engineered for 24×7 continuous industrial uptime, zero electromagnetic interference, and intuitive operator interface. CyTOS designs, builds, programs, and commissions custom electrical control enclosures integrating Siemens S7-1200/1500 and Delta PLCs, Schneider switchgear, VFDs, and touchscreen HMIs.
          </p>
          
          <div class="answer-first-callout">
            <strong>In brief:</strong> CyTOS provides end-to-end electrical panel design, programming, wiring, and on-site commissioning in Pune for Special Purpose Machines (SPMs), conveyor lines, and process machinery. Featuring IP54/IP55 dustproof Rittal-type enclosures, neat ferruled wiring, isolated signal channels, and Category 3/4 safety interlocks, we ensure zero uncommanded machine stoppages.
          </div>

          <div class="slide-cta-row">
            <button class="btn btn-primary btn-lg" data-open-rfq data-machine="PLC Industrial Control Panel">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="btn-icon-svg" aria-hidden="true"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect><path d="M9 12h6"></path><path d="M9 16h6"></path></svg> <span>Request Panel Engineering Quote</span>
            </button>
            <a href="https://wa.me/919921381071?text=Hi%20CyTOS,%20we%20have%20an%20electrical%20PLC%20control%20panel%20requirement%20to%20discuss." class="btn btn-secondary btn-lg" target="_blank" rel="noopener noreferrer">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="btn-icon-svg" aria-hidden="true"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg> <span>Discuss Panel Specs on WhatsApp</span>
            </a>
          </div>

          <div class="engineering-signoff-bar">
            <span class="signoff-icon"><svg viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg></span>
            <span><strong>Full Engineering Documentation:</strong> Complete EPLAN electrical circuit schematics, I/O terminal assignments, cable schedule, and documented PLC ladder logic provided with every panel.</span>
          </div>
        </div>

        <div class="page-hero-media">
          <img src="assets/images/blogs/plc-control-panel-automation.jpg" alt="Industrial PLC Control Panel Pune CyTOS">
          <div class="page-hero-caption">
            <strong>Featured Enclosure:</strong> CyTOS Industrial Automation Control Panel with Siemens S7 PLC, Touchscreen HMI &amp; Neat Ferruled Ducting
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 4 Core Panel Categories -->
  <section class="section" style="background: #ffffff;">
    <div class="container">
      <div class="section-header text-center">
        <div class="hero-badge" style="margin: 0 auto 1rem;">
          <span>PANEL ARCHITECTURES</span>
        </div>
        <h2 class="section-title">Four Industrial Electrical Automation Solutions</h2>
        <p class="section-subtitle">
          Designed, wired, and tested in our Pune facility with certified industrial components and thermal dissipation calculations.
        </p>
      </div>

      <div class="model-cards-grid" style="grid-template-columns: repeat(4, 1fr);">
        
        <!-- Category 1: Turnkey SPM Control Panels -->
        <article class="model-card">
          <div class="model-card-header">
            <div class="model-name">Turnkey SPM Panels</div>
            <div class="model-subhead">Dedicated Machinery</div>
          </div>
          <div class="model-card-media">
            <img src="assets/images/machines/industrial-control-panel.jpg" alt="Turnkey SPM Automation Control Panel">
          </div>
          <div class="model-card-body">
            <p style="font-size: 0.875rem; color: var(--text-secondary);">
              Complete electrical architecture for multi-station rotary indexing machines, pneumatic assembly jigs, and custom punching systems.
            </p>
            <ul class="model-specs-list">
              <li><span class="spec-label">PLC</span><span class="spec-val">Siemens S7-1200 / Delta</span></li>
              <li><span class="spec-label">HMI</span><span class="spec-val">7" to 10" Color Touch</span></li>
              <li><span class="spec-label">Safety</span><span class="spec-val">Dual E-stop relays</span></li>
            </ul>
          </div>
          <div class="model-card-footer">
            <button class="btn btn-primary btn-block" data-open-rfq data-machine="Turnkey SPM Control Panel">Quote SPM Panel</button>
          </div>
        </article>

        <!-- Category 2: Multi-Axis VFD Motion Panels -->
        <article class="model-card">
          <div class="model-card-header">
            <div class="model-name">VFD Motion Panels</div>
            <div class="model-subhead">Conveyors &amp; Spindles</div>
          </div>
          <div class="model-card-media">
            <img src="assets/images/blogs/plc-wiring-enclosure.jpg" alt="VFD Motion Drive Control Panel">
          </div>
          <div class="model-card-body">
            <p style="font-size: 0.875rem; color: var(--text-secondary);">
              Variable Frequency Drive enclosures with line reactors, braking resistors, and shielded motor power cabling for harmonic dampening.
            </p>
            <ul class="model-specs-list">
              <li><span class="spec-label">VFD Drives</span><span class="spec-val">Schneider / Delta / ABB</span></li>
              <li><span class="spec-label">Cooling</span><span class="spec-val">Forced filtered fans</span></li>
              <li><span class="spec-label">Harmonics</span><span class="spec-val">Line chokes included</span></li>
            </ul>
          </div>
          <div class="model-card-footer">
            <button class="btn btn-primary btn-block" data-open-rfq data-machine="VFD Motion Drive Panel">Quote VFD Panel</button>
          </div>
        </article>

        <!-- Category 3: Remote I/O & Distributed Panels -->
        <article class="model-card">
          <div class="model-card-header">
            <div class="model-name">Remote I/O Panels</div>
            <div class="model-subhead">Plant-Wide Automation</div>
          </div>
          <div class="model-card-media">
            <img src="assets/images/machines/cytos-facility-overview.jpg" alt="Remote IO Automation Panel Pune">
          </div>
          <div class="model-card-body">
            <p style="font-size: 0.875rem; color: var(--text-secondary);">
              Distributed field junction enclosures communicating via PROFINET, Modbus TCP, or EtherCAT to eliminate long analog wiring runs.
            </p>
            <ul class="model-specs-list">
              <li><span class="spec-label">Fieldbus</span><span class="spec-val">PROFINET / Modbus</span></li>
              <li><span class="spec-label">Enclosure</span><span class="spec-val">IP65 Stainless / MS</span></li>
              <li><span class="spec-label">Wiring</span><span class="spec-val">Quick M12 connectors</span></li>
            </ul>
          </div>
          <div class="model-card-footer">
            <button class="btn btn-primary btn-block" data-open-rfq data-machine="Remote IO Automation Panel">Quote Remote Panel</button>
          </div>
        </article>

        <!-- Category 4: Relay-to-PLC Retrofit Enclosures -->
        <article class="model-card">
          <div class="model-card-header">
            <div class="model-name">PLC Retrofit Panels</div>
            <div class="model-subhead">Modernization &amp; Re-tooling</div>
          </div>
          <div class="model-card-media">
            <img src="assets/images/machines/spm-automation-cell.jpg" alt="Relay to PLC Modernization Panel">
          </div>
          <div class="model-card-body">
            <p style="font-size: 0.875rem; color: var(--text-secondary);">
              Drop-in modern PLC replacement panels for aging mechanical relay machinery, adding digital recipe memory, fault logging, and OEE tracking.
            </p>
            <ul class="model-specs-list">
              <li><span class="spec-label">Downtime</span><span class="spec-val">Overnight swap-over</span></li>
              <li><span class="spec-label">Diagnostics</span><span class="spec-val">Touchscreen error alarm</span></li>
              <li><span class="spec-label">OEE Log</span><span class="spec-val">USB cycle-time export</span></li>
            </ul>
          </div>
          <div class="model-card-footer">
            <button class="btn btn-primary btn-block" data-open-rfq data-machine="PLC Retrofit Panel">Quote Retrofit Panel</button>
          </div>
        </article>

      </div>
    </div>
  </section>

  <!-- Technical Specifications Table -->
  <section class="section" style="background: var(--bg-surface);">
    <div class="container">
      <div class="section-header text-center">
        <div class="hero-badge" style="margin: 0 auto 1rem;">
          <span>ENGINEERING SPECIFICATIONS</span>
        </div>
        <h2 class="section-title">PLC Automation Panel Specifications</h2>
        <p class="section-subtitle">
          Standardized high-grade industrial electrical components ensuring zero thermal failure and rapid maintenance.
        </p>
      </div>

      <div class="table-responsive">
        <table class="specs-table">
          <thead>
            <tr>
              <th>Electrical Parameter</th>
              <th>Standard SPM Control Panel</th>
              <th>Multi-Drive Motion Panel</th>
              <th>Process Line Control Center</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Primary Controller</strong></td>
              <td>Siemens S7-1200 CPU 1214C / Delta DVP-SE</td>
              <td>Siemens S7-1200 / S7-1500 with Motion Control</td>
              <td>Siemens S7-1500 or Delta High-Performance Modular</td>
            </tr>
            <tr>
              <td><strong>Operator HMI Screen</strong></td>
              <td>Siemens KTP700 Basic 7" or Kinco 7" Color Touch</td>
              <td>Siemens Comfort 9" / Weintek 10.1" Touch</td>
              <td>Siemens Comfort 12" / 15" Industrial Touch Panel</td>
            </tr>
            <tr>
              <td><strong>Enclosure Protection</strong></td>
              <td>IP54 / IP55 Powder-Coated Sheet Steel (1.6mm/2.0mm)</td>
              <td>IP55 Rittal-Style Enclosure with Filter Fans</td>
              <td>IP55 Double Door with Industrial Air Conditioner</td>
            </tr>
            <tr>
              <td><strong>Switchgear &amp; Breakers</strong></td>
              <td>Schneider Electric TeSys contactors &amp; Acti9 MCBs</td>
              <td>ABB / Schneider Electric Motor Protection Circuit Breakers</td>
              <td>Siemens / Schneider Heavy Switchgear with isolator handle</td>
            </tr>
            <tr>
              <td><strong>Wiring &amp; Ducting</strong></td>
              <td>Finolex / RR Kabel FRLS copper wire with PVC ducts</td>
              <td>Shielded cable for motor leads; separate signal raceways</td>
              <td>Fully ferruled, numbered, and heat-shrink wrapped</td>
            </tr>
            <tr>
              <td><strong>Safety Interlocks</strong></td>
              <td>Pilz / Schneider dual-channel safety relay, E-stop circuit</td>
              <td>Siemens Safety Integrated / Pilz PNOZ safety relay</td>
              <td>Category 4 Safety PLC with light curtain interlocks</td>
            </tr>
            <tr>
              <td><strong>Field Documentation</strong></td>
              <td>Complete EPLAN schematic diagram + I/O wiring chart</td>
              <td>EPLAN schematics, VFD parameter backup sheet</td>
              <td>Full electrical drawings, PLC logic backup on USB</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- Real Pune Case Study -->
  <section class="section" style="background: #ffffff;">
    <div class="container">
      <div class="section-header text-center">
        <div class="hero-badge" style="margin: 0 auto 1rem;">
          <span>VERIFIED SHOP FLOOR CASE STUDY</span>
        </div>
        <h2 class="section-title">Multi-Station SPM Control Panel Modernization</h2>
        <p class="section-subtitle">
          How CyTOS replaced failing relay logic with a Siemens S7-1200 + HMI panel, cutting troubleshooting downtime by 85% in Talwade, Pune.
        </p>
      </div>

      <div class="case-study-card" style="background: var(--bg-surface); border: 1px solid var(--border-light); border-radius: 12px; padding: 2.5rem; max-width: 960px; margin: 0 auto;">
        <div class="case-study-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem; align-items: center;">
          <div>
            <h3 style="color: var(--brand-navy); font-size: 1.4rem; margin-bottom: 1rem;">The Engineering Challenge</h3>
            <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.25rem;">
              An automotive pressing and staking line was operating on a 15-year-old hardwired relay control panel with loose wire tags, burned contactors, and zero diagnostic display. Whenever a limit switch jammed, the maintenance team spent 4 to 6 hours with multimeters tracking down the fault, resulting in severe assembly line hold-ups.
            </p>
            <h3 style="color: var(--brand-navy); font-size: 1.4rem; margin-bottom: 1rem;">The CyTOS Solution</h3>
            <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">
              CyTOS designed, wired, and programmed a modern IP55 control enclosure powered by a Siemens S7-1200 PLC and a 7" color HMI. The new system includes real-time sensor diagnostic visualization, automated pneumatic cylinder timeout alarms, and password-protected cycle timer parameterization.
            </p>
          </div>
          <div>
            <div style="background: #ffffff; border: 1px solid var(--border-light); border-radius: 8px; padding: 1.5rem;">
              <h4 style="color: var(--brand-gold-dark); font-size: 1.1rem; margin-bottom: 1rem; border-bottom: 2px solid var(--border-light); padding-bottom: 0.5rem;">Operational &amp; Uptime Impact</h4>
              <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.92rem; color: var(--text-secondary);">
                <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-light); display: flex; justify-content: space-between;">
                  <span>Average Fault Tracing Time:</span>
                  <strong style="color: #ef4444;">4.5 hours per breakdown</strong>
                </li>
                <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-light); display: flex; justify-content: space-between;">
                  <span>HMI Diagnostic Tracing Time:</span>
                  <strong style="color: #10b981;">&lt; 5 minutes (-98%)</strong>
                </li>
                <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-light); display: flex; justify-content: space-between;">
                  <span>Monthly Electrical Downtime:</span>
                  <strong style="color: #10b981;">Reduced from 28h to 2h</strong>
                </li>
                <li style="padding: 0.6rem 0; border-bottom: 1px solid var(--border-light); display: flex; justify-content: space-between;">
                  <span>Part Re-Tooling Recipe Load:</span>
                  <strong style="color: #10b981;">Instant via HMI touch</strong>
                </li>
                <li style="padding: 0.6rem 0; display: flex; justify-content: space-between;">
                  <span>Turnaround Installation Time:</span>
                  <strong style="color: var(--brand-navy);">1 Weekend (Zero Lost Production)</strong>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ Section with Schema -->
  <section class="section" style="background: var(--bg-surface);" itemscope itemtype="https://schema.org/FAQPage">
    <div class="container" style="max-width: 860px;">
      <div class="section-header text-center">
        <div class="hero-badge" style="margin: 0 auto 1rem;">
          <span>ENGINEERING FAQS</span>
        </div>
        <h2 class="section-title">PLC Automation Control Panel FAQs</h2>
        <p class="section-subtitle">Common technical questions on PLC programming platforms, electrical safety, and lead times answered by CyTOS controls engineers.</p>
      </div>

      <div class="faq-accordion">
        <details class="faq-item" itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
          <summary class="faq-question" itemprop="name">Which PLC and HMI brands does CyTOS standardize on for custom automation panels?</summary>
          <div class="faq-answer" itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
            <p itemprop="text">
              We primarily standardize on Siemens (S7-1200 / S7-1500 with TIA Portal) and Delta Electronics (DVP / AS Series with ISPSoft and DOP HMI). We also design and build panels utilizing Schneider Electric, Omron, Mitsubishi, and Rockwell Automation upon customer request.
            </p>
          </div>
        </details>

        <details class="faq-item" itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
          <summary class="faq-question" itemprop="name">Does CyTOS provide complete electrical CAD drawings and PLC backup code?</summary>
          <div class="faq-answer" itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
            <p itemprop="text">
              Yes, 100%. Every control panel delivery includes a laminated printed electrical schematic inside the panel door pocket, an electronic PDF copy with full terminal mapping, and an uncompiled, well-commented PLC ladder program and HMI project file provided on an archival USB drive.
            </p>
          </div>
        </details>

        <details class="faq-item" itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
          <summary class="faq-question" itemprop="name">Can CyTOS integrate machine vision, barcode scanners, and factory MES networks?</summary>
          <div class="faq-answer" itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
            <p itemprop="text">
              Yes. Our control architectures support industrial Ethernet (PROFINET, Modbus TCP, Ethernet/IP) for seamless integration with Keyence/Cognex vision cameras, hand-held 2D code scanners, automated weighing scales, and plant-wide SCADA or MES databases for complete part traceability.
            </p>
          </div>
        </details>
      </div>
    </div>
  </section>

{FOOTER_HTML}
{FLOATING_BAR_HTML}
{MODAL_HTML}

  <script src="script.js"></script>
</body>
</html>
"""

# Write files
with open(os.path.join(PROJECT_DIR, "pneumatic-welding-fixtures.html"), "w", encoding="utf-8") as f:
    f.write(PNEUMATIC_FIXTURES_HTML)
print("Created pneumatic-welding-fixtures.html")

with open(os.path.join(PROJECT_DIR, "plc-control-panels.html"), "w", encoding="utf-8") as f:
    f.write(PLC_CONTROL_PANELS_HTML)
print("Created plc-control-panels.html")

print("All dedicated Automation & SPM pages successfully written!")
