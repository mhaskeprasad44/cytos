import os, json, re

ROOT_DIR = r"c:\Users\PrasadMhaske\Downloads\Project1"
LEGACY_DIR = os.path.join(ROOT_DIR, "_legacy_html_backup")

def build_terms_html():
    with open(os.path.join(LEGACY_DIR, "terms-conditions.html"), "r", encoding="utf-8") as f:
        html = f.read()

    # Extract body content
    b_start = html.find("<body")
    b_close = html.find(">", b_start) + 1
    b_end = html.find("</body>")
    body = html[b_close:b_end]

    # Remove any legacy cookie consent banner from the HTML to avoid duplication
    body = re.sub(r'<div\s+class=["\']cookie-consent-banner["\'].*?</div>\s*</div>\s*</div>', '', body, flags=re.DOTALL)
    body = re.sub(r'<div\s+class=["\']cookie-consent-banner["\'].*?</div>\s*</div>', '', body, flags=re.DOTALL)

    # 1. Fortify Section 1: Scope of Quotations & Contract Formation (sec-scope)
    sec1_replacement = """        <!-- Section 1 -->
        <section class="terms-section" id="sec-scope">
          <h2 class="terms-section-title">
            <span class="section-num">01.</span> Scope of Quotations, Website Content &amp; Contract Formation
          </h2>
          <p class="terms-p">
            All commercial proposals, technical quotations, machinery catalogs, and proforma invoices issued by <strong>Cybernetic Technologies &amp; Operating Systems (hereinafter referred to as &ldquo;CyTOS&rdquo;)</strong> are valid for a period of thirty (30) calendar days from the date of issuance, unless explicitly stated otherwise in writing.
          </p>
          <div class="terms-highlight-card" style="border-left: 4px solid var(--brand-gold); background: #fffbeb;">
            <h5 style="color: #b45309; margin-bottom: 0.4rem;">Website Information &amp; Technical Estimates Disclaimer</h5>
            <p style="font-size: 0.88rem; color: #475569; margin: 0; line-height: 1.6;">
              All machinery specifications, technical illustrations, spindle speeds, axis feed rates, cycle-time reduction projections, and ROI calculators published on <strong>cytos.in</strong> are provided solely for general informational, educational, and technical estimation purposes. They do not constitute a binding performance guarantee, warranty, or formal commercial offer. Actual machining tolerances and production throughput depend on workpiece alloy grade, tooling sharpness, operator skill, and ambient workshop conditions. CyTOS is bound only by specifications explicitly stipulated in a formal, mutually executed Master Equipment Supply Agreement or signed Proforma Invoice accompanied by contractual advance payment.
            </p>
          </div>
          <p class="terms-p" style="margin-top: 1rem;">
            A legally binding purchase contract is formed exclusively upon written acceptance of the Buyer's formal Purchase Order (PO) by CyTOS accompanied by the contractual advance payment. Technical specifications, machine layout drawings, and cycle-time projections detailed in CyTOS formal written quotations form an integral schedule of the supply agreement. No prior oral representations or general website statements shall modify these terms.
          </p>
          <div class="terms-highlight-card">
            <h5>Taxation &amp; Statutory Levies</h5>
            <p>All prices quoted are exclusive of Goods and Services Tax (GST) applicable under Indian law (presently 18% on capital machine tools under HSN 8459 / 8465), customs duties for export orders, and local octroi/entry tolls, which shall be charged at actuals at the time of invoicing.</p>
          </div>
        </section>"""

    body = re.sub(
        r'<section\s+class=["\']terms-section["\']\s+id=["\']sec-scope["\']>.*?</section>',
        sec1_replacement,
        body,
        flags=re.DOTALL
    )

    # 2. Fortify Section 6: Standard 12-Month Equipment Warranty & Disclaimer of Implied Warranties (sec-warranty)
    sec6_replacement = """        <!-- Section 6 -->
        <section class="terms-section" id="sec-warranty">
          <h2 class="terms-section-title">
            <span class="section-num">06.</span> Standard 12-Month Equipment Warranty &amp; Disclaimer of Implied Warranties
          </h2>
          <p class="terms-p">
            CyTOS provides a comprehensive <strong>twelve (12) month limited manufacturer warranty</strong> covering all mechanical assemblies, linear motion guides, ball screws, servo drives, and structural fabricated components from the date of successful commissioning, or fifteen (15) months from the date of dispatch, whichever is earlier.
          </p>
          <div class="terms-highlight-card">
            <h5>Warranty Coverage &amp; Strict Exclusions</h5>
            <p><strong>Covered:</strong> Free replacement or factory repair of parts found defective due to faulty materials or CyTOS manufacturing workmanship.</p>
            <p style="margin-top: 0.5rem; line-height: 1.6;"><strong>Strict Exclusions &amp; Release of Obligations:</strong> CyTOS is entirely released and discharged from all warranty, maintenance, and repair obligations if failure arises from: (a) normal wear-and-tear consumables (collets, router bits, micro-drills, vacuum pump vanes, sacrificial spoil-boards, cooling lines); (b) machine crashes or spindle collisions caused by incorrect operator G-code, CAM post-processor errors, incorrect tool offsets, or human oversight; (c) unauthorized disassembly, spindle tampering, electrical panel modification, or use of non-genuine third-party parts by non-CyTOS personnel; (d) contaminated, wet, or un-lubricated compressed air supply below ISO 8573-1 standards; (e) supply voltage fluctuations or neutral-to-earth potential exceeding 3.0V AC; (f) operation outside specified thermal ambient ranges (18&deg;C&ndash;32&deg;C) or non-condensing humidity above 75%.</p>
          </div>
          <div class="terms-highlight-card" style="border-left: 4px solid var(--accent-red); background: #fef2f2; margin-top: 1rem;">
            <h5 style="color: #b91c1c; margin-bottom: 0.35rem;">Disclaimer of Implied Warranties</h5>
            <p style="font-size: 0.88rem; color: #475569; margin: 0; line-height: 1.6;">
              Except for the express 12-month manufacturer limited warranty stated herein, CyTOS disclaims all other representations and warranties of any kind, whether express, statutory, or implied, including without limitation any implied warranties of merchantability, fitness for a particular industrial purpose, uninterrupted operation, or non-infringement. All machinery, software, and engineering services are provided strictly &ldquo;as is&rdquo; and &ldquo;as available&rdquo;.
            </p>
          </div>
        </section>"""

    body = re.sub(
        r'<section\s+class=["\']terms-section["\']\s+id=["\']sec-warranty["\']>.*?</section>',
        sec6_replacement,
        body,
        flags=re.DOTALL
    )

    # 3. Fortify Section 8: Controller Software, Firmware & Intellectual Property (sec-software)
    sec8_replacement = """        <!-- Section 8 -->
        <section class="terms-section" id="sec-software">
          <h2 class="terms-section-title">
            <span class="section-num">08.</span> Controller Software, Firmware &amp; Intellectual Property
          </h2>
          <p class="terms-p">
            All proprietary PLC ladder logic, DSP/FPGA motion controller algorithms, macro software routines, HMI graphical interface layouts, and machine firmware developed by CyTOS remain the exclusive intellectual property of CyTOS.
          </p>
          <p class="terms-p">
            The Buyer is granted a perpetual, non-transferable, royalty-free operating license to utilize the installed software solely for operating the specific machine serial number supplied. Reverse engineering, decompiling, extracting source code, cloning, or distributing CyTOS proprietary automation sequences is strictly prohibited and constitutes actionable infringement under applicable copyright and trade secret laws.
          </p>
        </section>"""

    body = re.sub(
        r'<section\s+class=["\']terms-section["\']\s+id=["\']sec-software["\']>.*?</section>',
        sec8_replacement,
        body,
        flags=re.DOTALL
    )

    # 4. Fortify Section 9: Limitation of Liability, Total Damage Waiver & Indemnity (sec-liability)
    sec9_replacement = """        <!-- Section 9 -->
        <section class="terms-section" id="sec-liability">
          <h2 class="terms-section-title">
            <span class="section-num">09.</span> Limitation of Liability, Total Damage Waiver &amp; Indemnification
          </h2>
          <div class="terms-highlight-card" style="border-left: 4px solid var(--accent-red); background: #fef2f2; margin-bottom: 1rem;">
            <h5 style="color: #b91c1c; margin-bottom: 0.35rem;">Absolute Consequential Damage Waiver &amp; Liability Cap</h5>
            <p style="font-size: 0.88rem; color: #475569; margin: 0; line-height: 1.6;">
              Under no circumstances, regardless of the legal or equitable theory (whether in contract, tort, strict liability, negligence, product liability, breach of warranty, or statutory duty), shall CyTOS, its proprietors, directors, engineers, officers, or affiliates be liable to the Buyer or any third party for any indirect, special, incidental, punitive, exemplary, or consequential damages whatsoever. This includes, without limitation, loss of business revenue, commercial downtime, lost profits, idle factory labor costs, raw material or workpiece scrap/spoilage, tool breakage, penalty clauses or liquidated damages from Buyer's downstream clients, loss of data, or cost of substitute equipment. In all events, CyTOS's maximum cumulative aggregate monetary liability shall strictly not exceed the net capital amount actually received by CyTOS for the specific machine unit in dispute.
            </p>
          </div>
          <div class="terms-highlight-card" style="border-left: 4px solid #0284c7; background: #f0f9ff; margin-bottom: 1rem;">
            <h5 style="color: #0369a1; margin-bottom: 0.35rem;">Comprehensive Buyer Indemnification &amp; Hold Harmless</h5>
            <p style="font-size: 0.88rem; color: #475569; margin: 0; line-height: 1.6;">
              The Buyer agrees to defend, indemnify, and hold harmless CyTOS, its directors, and technical personnel from and against any and all claims, regulatory penalties, lawsuits, liabilities, losses, costs, and legal expenses arising from: (a) workplace injuries, operator negligence, or failure to implement required industrial safety enclosures, interlocks, eye/ear protection, and dust extraction systems; (b) any claim that workpiece designs, CAD/CAM models, or PCB Gerber files supplied by the Buyer infringe upon any patent, copyright, or trade secret of any third party; (c) the distribution, installation, or performance of components manufactured by the Buyer using CyTOS machinery in aerospace, defense, automotive, medical, or other mission-critical applications; (d) Buyer's non-compliance with applicable labor, electrical, or environmental safety regulations.
            </p>
          </div>
          <div class="terms-highlight-card" style="border-left: 4px solid #10b981; background: #f0fdf4; margin-bottom: 1rem;">
            <h5 style="color: #065f46; margin-bottom: 0.35rem;">Customer CAD/Gerber IP Non-Infringement Warranty</h5>
            <p style="font-size: 0.88rem; color: #475569; margin: 0; line-height: 1.6;">
              The Buyer expressly warrants and represents that it holds full intellectual property ownership, license, or legal authorization for any CAD drawings, Gerber RS-274X archives, Excellon drill files, DXF models, or physical workpiece samples delivered to CyTOS for test trials, cutting feasibility, or tooling design, and that processing them does not infringe upon any third-party proprietary rights.
            </p>
          </div>
          <p class="terms-p">
            <strong>Force Majeure:</strong> Neither party shall be held liable for delivery delays or performance failure resulting from acts of God, extreme natural disasters, pandemic lockdowns, civil unrest, statutory import embargoes, electrical grid failures, component supply shortages, or transportation strikes beyond reasonable commercial control.
          </p>
        </section>"""

    body = re.sub(
        r'<section\s+class=["\']terms-section["\']\s+id=["\']sec-liability["\']>.*?</section>',
        sec9_replacement,
        body,
        flags=re.DOTALL
    )

    # 5. Fortify Section 10: Governing Law & Pune Legal Jurisdiction (sec-jurisdiction)
    sec10_replacement = """        <!-- Section 10 -->
        <section class="terms-section" id="sec-jurisdiction">
          <h2 class="terms-section-title">
            <span class="section-num">10.</span> Governing Law &amp; Exclusive Pune Legal Jurisdiction
          </h2>
          <p class="terms-p">
            All commercial transactions, quotation agreements, purchase orders, machinery supply contracts, and disputes arising out of or related to interactions with CyTOS shall be governed by and construed in accordance with the substantive laws of the <strong>Republic of India</strong>, without regard to conflict of laws principles.
          </p>
          <p class="terms-p">
            Any legal dispute, suit, action, or claim that cannot be amicably settled through mutual executive conciliation within thirty (30) days shall be subject to the <strong>exclusive jurisdiction of the competent courts of law in Pune, Maharashtra, India</strong>. The Buyer expressly and irrevocably waives any objection to venue or inconvenient forum.
          </p>
        </section>"""

    body = re.sub(
        r'<section\s+class=["\']terms-section["\']\s+id=["\']sec-jurisdiction["\']>.*?</section>',
        sec10_replacement,
        body,
        flags=re.DOTALL
    )

    return body

def build_privacy_html():
    with open(os.path.join(LEGACY_DIR, "privacy-policy.html"), "r", encoding="utf-8") as f:
        html = f.read()

    # Extract body content
    b_start = html.find("<body")
    b_close = html.find(">", b_start) + 1
    b_end = html.find("</body>")
    body = html[b_close:b_end]

    # Remove any legacy cookie consent banner from the HTML to avoid duplication
    body = re.sub(r'<div\s+class=["\']cookie-consent-banner["\'].*?</div>\s*</div>\s*</div>', '', body, flags=re.DOTALL)
    body = re.sub(r'<div\s+class=["\']cookie-consent-banner["\'].*?</div>\s*</div>', '', body, flags=re.DOTALL)

    # 1. Fortify Section 7: Industrial Cybersecurity & Limitation of Internet Transmission Liability (section-security)
    sec7_replacement = """          <!-- Section 7 -->
          <section id="section-security" class="terms-section-card">
            <span class="terms-clause-number">CLAUSE 07</span>
            <h2>Industrial Cybersecurity &amp; Encryption Standards</h2>
            <p>
              CyTOS implements robust technical, physical, and organizational security controls to protect client information from unauthorized access, alteration, or disclosure:
            </p>
            <ul class="terms-bullet-list">
              <li><strong>Transport Security:</strong> 256-bit SSL/TLS 1.3 encryption across all web pages and interactive form endpoints.</li>
              <li><strong>Access Control:</strong> Strict role-based permission controls ensuring only certified CyTOS mechanical and software engineers have access to customer drawings.</li>
              <li><strong>Physical Security:</strong> CyTOS Pune works maintains 24&times;7 physical security and controlled access to assembly bays and testing rigs.</li>
              <li><strong>Data Retention:</strong> Active customer warranty telemetry is retained for 7 years to facilitate lifecycle maintenance and spare parts availability.</li>
            </ul>
            <div class="terms-callout-box" style="border-left-color: #64748b; background: #f8fafc;">
              <strong>Internet Transmission Disclaimer:</strong> While CyTOS employs industry-standard cybersecurity measures, data transmission across public internet connections involves inherent vulnerabilities. CyTOS disclaims liability for unauthorized interception, third-party cyber intrusions, or transmission failures beyond our reasonable technical control.
            </div>
          </section>"""

    body = re.sub(
        r'<section\s+id=["\']section-security["\']\s+class=["\']terms-section-card["\']>.*?</section>',
        sec7_replacement,
        body,
        flags=re.DOTALL
    )

    # 2. Fortify Section 8: Cookies, Local Telemetry & CookieYes Persistent Floating Icon (section-cookies)
    sec8_replacement = """          <!-- Section 8 -->
          <section id="section-cookies" class="terms-section-card">
            <span class="terms-clause-number">CLAUSE 08</span>
            <h2>Cookies, Local Telemetry &amp; CookieYes-Style Persistent Floating Controls</h2>
            <p>
              In full compliance with India's <strong>Digital Personal Data Protection Act (DPDP Act, 2023)</strong> and international privacy best practices, CyTOS uses minimal, strictly controlled cookies and local browser storage to deliver reliable website functionality:
            </p>
            <ul class="terms-bullet-list">
              <li><strong>Essential &amp; Security Cookies (Strictly Necessary):</strong> Required to maintain interactive RFQ calculator state, CAD file upload sessions, multi-step quote progress, and security verification. These cookies cannot be deactivated as core site functionality depends on them.</li>
              <li><strong>Performance &amp; Diagnostics Telemetry (Optional):</strong> Measures anonymous page load speeds, catalog interactions, and server response times to optimize user experience. No personal identifying information is stored.</li>
              <li><strong>Functional &amp; Engineering Preferences (Optional):</strong> Preserves your preferred machine category filters, technical unit selections (metric/imperial), and cookie consent status.</li>
            </ul>
            <div class="terms-callout-box" style="border-left-color: var(--accent-emerald); background: #f0fdf4;">
              <strong style="color: #166534;">Persistent User Control (CookieYes-Style Floating Badge in Bottom-Left Corner):</strong><br>
              Visitors retain absolute, continuous control over their cookie preferences. Once you interact with our consent dialog, a persistent floating cookie badge remains accessible in the <strong>bottom-left corner of every page</strong>. Clicking this icon allows you to inspect active cookies, modify your consent, switch to &ldquo;Necessary Only&rdquo;, or revoke non-essential data processing at any time.
            </div>
            <p style="margin-top: 0.85rem;">
              <strong>Zero Cross-Site Tracking:</strong> CyTOS does not deploy intrusive third-party advertising tracking pixels, behavioral advertising networks, or cross-site data harvesting mechanisms.
            </p>
          </section>"""

    body = re.sub(
        r'<section\s+id=["\']section-cookies["\']\s+class=["\']terms-section-card["\']>.*?</section>',
        sec8_replacement,
        body,
        flags=re.DOTALL
    )

    # 3. Fortify Section 10: Grievance Redressal & Pune Jurisdiction (section-grievance)
    sec10_replacement = """          <!-- Section 10 -->
          <section id="section-grievance" class="terms-section-card">
            <span class="terms-clause-number">CLAUSE 10</span>
            <h2>Grievance Redressal, Compliance &amp; Exclusive Pune Jurisdiction</h2>
            <p>
              In accordance with Indian information technology regulations and the Digital Personal Data Protection Act, 2023, the designated Grievance Officer for privacy and data protection inquiries is:
            </p>
            <div class="terms-callout-box">
              <strong>Data Grievance Officer:</strong> CyTOS Engineering Solutions Administration<br>
              <strong>Facility Address:</strong> S. No. 30, 5B, Dhayari-Narhe Road, Dhayari, Pune, Maharashtra 411041, India.<br>
              <strong>Direct Email:</strong> <a href="mailto:info@cytos.in?subject=Privacy%20Grievance%20Desk">info@cytos.in</a> / <a href="mailto:inranktech@gmail.com">inranktech@gmail.com</a><br>
              <strong>Hotline:</strong> +91 99213 81071
            </div>
            <p>
              Any disputes, controversies, or legal claims arising out of this Privacy Policy shall be governed exclusively by the substantive laws of the Republic of India and subject to the <strong>exclusive jurisdiction of the competent courts of law in Pune, Maharashtra, India</strong>.
            </p>
          </section>"""

    body = re.sub(
        r'<section\s+id=["\']section-grievance["\']\s+class=["\']terms-section-card["\']>.*?</section>',
        sec10_replacement,
        body,
        flags=re.DOTALL
    )

    return body

terms_html = build_terms_html()
privacy_html = build_privacy_html()

# Generate React JSX files with valid json.dumps() escaping
terms_jsx = f"""import React from 'react';
import HtmlPageWrapper from '../components/HtmlPageWrapper';

const pageHtml = {json.dumps(terms_html)};

export default function TermsPage() {{
  return (
    <HtmlPageWrapper
      htmlContent={{pageHtml}}
      title="Terms &amp; Conditions of Machinery Supply | CyTOS Pune"
      description="Commercial machinery supply terms, Factory Acceptance Testing (FAT), site readiness, 12-month warranty, and legal jurisdiction for CyTOS machine tools, Pune."
    />
  );
}}
"""

privacy_jsx = f"""import React from 'react';
import HtmlPageWrapper from '../components/HtmlPageWrapper';

const pageHtml = {json.dumps(privacy_html)};

export default function PrivacyPolicyPage() {{
  return (
    <HtmlPageWrapper
      htmlContent={{pageHtml}}
      title="Privacy &amp; Engineering Data Protection Policy | CyTOS Pune"
      description="Official policy of CyTOS Engineering Solutions governing client CAD/Gerber file confidentiality, commercial quotation telemetry, DPDP Act 2023 compliance, and industrial data governance."
    />
  );
}}
"""

with open("src/pages/TermsPage.jsx", "w", encoding="utf-8") as f:
    f.write(terms_jsx)

with open("src/pages/PrivacyPolicyPage.jsx", "w", encoding="utf-8") as f:
    f.write(privacy_jsx)

print("Successfully written TermsPage.jsx and PrivacyPolicyPage.jsx with json.dumps!")
