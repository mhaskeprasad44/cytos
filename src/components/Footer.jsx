import React from 'react';
import { Link } from 'react-router-dom';

export default function Footer({ onOpenQuote }) {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="site-footer">
      <div className="container footer-container">
        {/* Company Identity */}
        <div className="footer-col footer-col-brand">
          <Link to="/" className="footer-logo">
            <img src="/CyTOS-New-Logo-White.png" alt="CyTOS Machines Pune" width="180" height="48" />
          </Link>
          <p className="footer-brand-desc">
            CyTOS Machines is an ISO 9001:2015 certified manufacturer of high-precision CNC Routers, 60,000 RPM PCB Drilling & Routing Machines, Vertical Milling Centers, and Special Purpose Automation Systems (SPM) based in Bhosari MIDC, Pune.
          </p>
          <div className="footer-badges">
            <span className="badge badge-gold">ISO 9001:2015 Certified</span>
            <span className="badge badge-primary">Make In India</span>
            <span className="badge badge-outline">CE Standard Compliance</span>
          </div>
          <div className="footer-direct-call">
            <span style={{ fontSize: '0.82rem', color: 'var(--text-muted)' }}>Factory Direct Support:</span>
            <a href="tel:+919422035109" className="footer-phone-highlight">+91 94220 35109</a>
          </div>
        </div>

        {/* Machine Categories & Dedicated Models */}
        <div className="footer-col">
          <h4 className="footer-heading">Precision CNC Machines</h4>
          <ul className="footer-links">
            <li><Link to="/cnc-6060-pcb-drilling-routing-machine">CNC 6060 PCB Drilling & Routing</Link></li>
            <li><Link to="/cnc-3020-pcb-prototyping-machine">CNC 3020 PCB Rapid Prototyper</Link></li>
            <li><Link to="/cnc-3030-pcb-prototyping-machine">CNC 3030 PCB Prototyper</Link></li>
            <li><Link to="/pcb12-multi-spindle-drilling-machine">PCB12 Multi-Spindle (3-Head)</Link></li>
            <li><Link to="/cnc-wood-acrylic-aluminium-router-machine">CNC Wood/Acrylic/Aluminium Router</Link></li>
            <li><Link to="/vdm-heavy-vertical-drilling-milling-machine">VDM Heavy Drilling & Milling</Link></li>
            <li><Link to="/foam-welding-machine">Foam Welding Machine</Link></li>
            <li><Link to="/educational-cnc-machines">Educational CNC Machines</Link></li>
          </ul>
        </div>

        {/* Industry Solutions */}
        <div className="footer-col">
          <h4 className="footer-heading">Industries & Solutions</h4>
          <ul className="footer-links">
            <li><Link to="/applications">Automotive Tier-1 & Tier-2</Link></li>
            <li><Link to="/applications">Electronics & PCB Fabrication</Link></li>
            <li><Link to="/applications">Aerospace & Defense Precision</Link></li>
            <li><Link to="/applications">Switchboard & Electrical Enclosures</Link></li>
            <li><Link to="/applications">Academic & R&D Prototyping Labs</Link></li>
            <li><Link to="/case-studies">Real Factory Case Studies</Link></li>
            <li><Link to="/blog">Engineering Knowledge Base</Link></li>
            <li><a href="/cytos_newcatalog2026_with BG.pdf" target="_blank" rel="noopener noreferrer">Download 2026 Product Catalog (PDF)</a></li>
          </ul>
        </div>

        {/* Factory Contact & Location */}
        <div className="footer-col">
          <h4 className="footer-heading">CyTOS Manufacturing Plant</h4>
          <div className="footer-contact-block">
            <p className="footer-address">
              <strong>Factory Works:</strong><br />
              J-153, M.I.D.C., Bhosari,<br />
              Pune - 411026, Maharashtra, India
            </p>
            <p className="footer-contact-item">
              <strong>Sales & Consultation:</strong><br />
              <a href="tel:+919422035109">+91 94220 35109</a> / <a href="tel:+919850983637">+91 98509 83637</a>
            </p>
            <p className="footer-contact-item">
              <strong>Technical Inquiries:</strong><br />
              <a href="mailto:cytospune@gmail.com">cytospune@gmail.com</a>
            </p>
            <button
              className="btn btn-primary btn-sm"
              style={{ marginTop: '0.75rem', width: '100%', justifyContent: 'center' }}
              onClick={onOpenQuote}
            >
              Request Custom Machine Quote
            </button>
          </div>
        </div>
      </div>

      {/* Pan India Support Bar */}
      <div className="footer-pan-india">
        <div className="container">
          <div className="pan-india-inner">
            <span className="pan-india-label">Direct Pan-India Installation, Spare Parts & On-Site Service:</span>
            <div className="pan-india-cities">
              <span>Pune (Bhosari / Chakan / Talegaon)</span>
              <span>•</span>
              <span>Mumbai & Thane</span>
              <span>•</span>
              <span>Aurangabad & Nashik</span>
              <span>•</span>
              <span>Ahmedabad & Vadodara</span>
              <span>•</span>
              <span>Bengaluru & Peenya</span>
              <span>•</span>
              <span>Chennai & Sriperumbudur</span>
              <span>•</span>
              <span>Hyderabad</span>
              <span>•</span>
              <span>Delhi NCR & Manesar</span>
              <span>•</span>
              <span>Coimbatore</span>
            </div>
          </div>
        </div>
      </div>

      {/* Copyright & Legal Bar */}
      <div className="footer-bottom">
        <div className="container footer-bottom-inner">
          <p className="copyright-text">
            © {currentYear} CyTOS Machines. All Rights Reserved. Engineered and Manufactured in Pune, India.
          </p>
          <div className="footer-legal-links">
            <Link to="/privacy-policy">Privacy Policy</Link>
            <span className="divider">|</span>
            <Link to="/terms-conditions">Terms & Conditions</Link>
            <span className="divider">|</span>
            <a href="/sitemap.xml" target="_blank" rel="noopener noreferrer">Sitemap</a>
          </div>
        </div>
      </div>
    </footer>
  );
}
