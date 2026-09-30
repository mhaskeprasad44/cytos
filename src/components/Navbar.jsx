import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';

export default function Navbar({ onOpenQuote }) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const location = useLocation();

  useEffect(() => {
    setMobileMenuOpen(false);
    setDropdownOpen(false);
  }, [location.pathname]);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const isActive = (path) => location.pathname === path;
  const isProductActive = [
    '/cnc-routers-milling',
    '/pcb-drilling-routing',
    '/pcb-prototyping',
    '/vdm-milling',
    '/robotic-dispensing-cells',
    '/pneumatic-welding-fixtures',
    '/plc-control-panels',
    '/spm-automation'
  ].includes(location.pathname);

  return (
    <>
      {/* Top Announcement & Quick Contact Header */}
      <div className="top-bar">
        <div className="container top-bar-inner">
          <div className="top-bar-left">
            <span className="top-bar-item">
              <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                <circle cx="12" cy="10" r="3"></circle>
              </svg>
              <span>J-153, MIDC Bhosari, Pune, MH 411026</span>
            </span>
            <span className="top-bar-divider">|</span>
            <span className="top-bar-item">
              <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="2">
                <circle cx="12" cy="12" r="10"></circle>
                <polyline points="12 6 12 12 16 14"></polyline>
              </svg>
              <span>Mon - Sat: 9:00 AM - 6:30 PM IST</span>
            </span>
          </div>
          <div className="top-bar-right">
            <a href="tel:+919422035109" className="top-bar-link">
              <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
              </svg>
              <span>+91 94220 35109</span>
            </a>
            <span className="top-bar-divider">|</span>
            <a href="mailto:cytospune@gmail.com" className="top-bar-link">
              <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                <polyline points="22,6 12,13 2,6"></polyline>
              </svg>
              <span>cytospune@gmail.com</span>
            </a>
          </div>
        </div>
      </div>

      {/* Main Navbar */}
      <header className={`site-header ${scrolled ? 'scrolled' : ''}`}>
        <div className="container header-container">
          <Link to="/" className="site-logo" aria-label="CyTOS Machines Home">
            <img src="/CyTOS New Logo.png" alt="CyTOS Machines Pune Logo" width="180" height="48" />
          </Link>

          {/* Desktop Navigation */}
          <nav className="desktop-nav" aria-label="Main Navigation">
            <Link to="/" className={`nav-link ${isActive('/') ? 'active' : ''}`}>
              Home
            </Link>

            {/* Products Dropdown */}
            <div
              className={`nav-item-dropdown ${dropdownOpen ? 'open' : ''}`}
              onMouseEnter={() => setDropdownOpen(true)}
              onMouseLeave={() => setDropdownOpen(false)}
            >
              <button
                className={`nav-link dropdown-toggle ${isProductActive ? 'active' : ''}`}
                onClick={() => setDropdownOpen(!dropdownOpen)}
                aria-expanded={dropdownOpen}
              >
                <span>Machines & SPM</span>
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="2">
                  <polyline points="6 9 12 15 18 9"></polyline>
                </svg>
              </button>

              <div className="dropdown-menu">
                <Link to="/cnc-routers-milling" className="dropdown-item">
                  <div className="dropdown-item-title">Heavy-Duty CNC Routers</div>
                  <div className="dropdown-item-desc">Precision routing & engraving for non-ferrous metals & acrylics</div>
                </Link>
                <Link to="/pcb-drilling-routing" className="dropdown-item">
                  <div className="dropdown-item-title">PCB Drilling & Routing</div>
                  <div className="dropdown-item-desc">60,000 RPM high-speed micro-hole drilling (PCB-60 & PCB-12)</div>
                </Link>
                <Link to="/pcb-prototyping" className="dropdown-item">
                  <div className="dropdown-item-title">Chemical-Free PCB Prototyping</div>
                  <div className="dropdown-item-desc">Instant isolation milling with auto-leveling & software</div>
                </Link>
                <Link to="/vdm-milling" className="dropdown-item">
                  <div className="dropdown-item-title">VDM Vertical Drilling & Milling</div>
                  <div className="dropdown-item-desc">Heavy BT30 / BT40 switchboard & die-sink machining</div>
                </Link>
                <Link to="/robotic-dispensing-cells" className="dropdown-item">
                  <div className="dropdown-item-title">Robotic Dispensing Cells</div>
                  <div className="dropdown-item-desc">Automated adhesive, thermal paste & polyurethane gasket dispensing</div>
                </Link>
                <Link to="/pneumatic-welding-fixtures" className="dropdown-item">
                  <div className="dropdown-item-title">Pneumatic Welding Fixtures</div>
                  <div className="dropdown-item-desc">Repeatable clamping jigs & weld tooling with zero distortion</div>
                </Link>
                <Link to="/plc-control-panels" className="dropdown-item">
                  <div className="dropdown-item-title">PLC Control Panels</div>
                  <div className="dropdown-item-desc">Custom automation enclosures, Siemens/Mitsubishi integration</div>
                </Link>
                <Link to="/spm-automation" className="dropdown-item">
                  <div className="dropdown-item-title">Custom SPM Automation</div>
                  <div className="dropdown-item-desc">Special purpose multi-axis machines for automotive & electronics</div>
                </Link>
              </div>
            </div>

            <Link to="/applications" className={`nav-link ${isActive('/applications') ? 'active' : ''}`}>
              Applications
            </Link>
            <Link to="/case-studies" className={`nav-link ${isActive('/case-studies') ? 'active' : ''}`}>
              Case Studies
            </Link>
            <Link to="/about" className={`nav-link ${isActive('/about') ? 'active' : ''}`}>
              About Us
            </Link>
            <Link to="/blog" className={`nav-link ${isActive('/blog') ? 'active' : ''}`}>
              Technical Blog
            </Link>
            <Link to="/contact" className={`nav-link ${isActive('/contact') ? 'active' : ''}`}>
              Contact
            </Link>
          </nav>

          <div className="header-actions">
            <button className="btn btn-primary nav-rfq-btn" onClick={() => onOpenQuote()}>
              <span>Request Quote</span>
              <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2">
                <line x1="5" y1="12" x2="19" y2="12"></line>
                <polyline points="12 5 19 12 12 19"></polyline>
              </svg>
            </button>

            {/* Mobile Hamburger Toggle */}
            <button
              className="mobile-toggle-btn"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              aria-label="Toggle navigation menu"
              aria-expanded={mobileMenuOpen}
            >
              {mobileMenuOpen ? (
                <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" strokeWidth="2">
                  <line x1="18" y1="6" x2="6" y2="18"></line>
                  <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
              ) : (
                <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" strokeWidth="2">
                  <line x1="3" y1="12" x2="21" y2="12"></line>
                  <line x1="3" y1="6" x2="21" y2="6"></line>
                  <line x1="3" y1="18" x2="21" y2="18"></line>
                </svg>
              )}
            </button>
          </div>
        </div>
      </header>

      {/* Mobile Menu Drawer */}
      <div className={`mobile-nav-drawer ${mobileMenuOpen ? 'open' : ''}`}>
        <div className="mobile-nav-content">
          <Link to="/" className="mobile-nav-link" onClick={() => setMobileMenuOpen(false)}>
            Home
          </Link>
          
          <div className="mobile-nav-section-title">Machines & Automation SPM</div>
          <Link to="/cnc-routers-milling" className="mobile-nav-sublink" onClick={() => setMobileMenuOpen(false)}>
            Heavy-Duty CNC Routers
          </Link>
          <Link to="/pcb-drilling-routing" className="mobile-nav-sublink" onClick={() => setMobileMenuOpen(false)}>
            PCB Drilling & Routing (60k RPM)
          </Link>
          <Link to="/pcb-prototyping" className="mobile-nav-sublink" onClick={() => setMobileMenuOpen(false)}>
            Chemical-Free PCB Prototyping
          </Link>
          <Link to="/vdm-milling" className="mobile-nav-sublink" onClick={() => setMobileMenuOpen(false)}>
            Vertical Drilling & Milling (VDM)
          </Link>
          <Link to="/robotic-dispensing-cells" className="mobile-nav-sublink" onClick={() => setMobileMenuOpen(false)}>
            Robotic Dispensing Cells
          </Link>
          <Link to="/pneumatic-welding-fixtures" className="mobile-nav-sublink" onClick={() => setMobileMenuOpen(false)}>
            Pneumatic Welding Fixtures
          </Link>
          <Link to="/plc-control-panels" className="mobile-nav-sublink" onClick={() => setMobileMenuOpen(false)}>
            PLC Control Panels
          </Link>
          <Link to="/spm-automation" className="mobile-nav-sublink" onClick={() => setMobileMenuOpen(false)}>
            Custom SPM Automation
          </Link>

          <div className="mobile-nav-section-title">Company & Resources</div>
          <Link to="/applications" className="mobile-nav-link" onClick={() => setMobileMenuOpen(false)}>
            Applications & Industries
          </Link>
          <Link to="/case-studies" className="mobile-nav-link" onClick={() => setMobileMenuOpen(false)}>
            Case Studies & Proof
          </Link>
          <Link to="/about" className="mobile-nav-link" onClick={() => setMobileMenuOpen(false)}>
            About CyTOS Machines
          </Link>
          <Link to="/blog" className="mobile-nav-link" onClick={() => setMobileMenuOpen(false)}>
            Technical Blog (22 Guides)
          </Link>
          <Link to="/contact" className="mobile-nav-link" onClick={() => setMobileMenuOpen(false)}>
            Contact Factory
          </Link>

          <div style={{ marginTop: '2rem', padding: '0 1rem' }}>
            <button
              className="btn btn-primary"
              style={{ width: '100%', justifyContent: 'center' }}
              onClick={() => {
                setMobileMenuOpen(false);
                onOpenQuote();
              }}
            >
              <span>Request Factory Quotation</span>
            </button>
          </div>

          <div className="mobile-nav-contact-footer">
            <p><strong>CyTOS Factory:</strong> J-153, MIDC Bhosari, Pune</p>
            <p><a href="tel:+919422035109">+91 94220 35109</a> | <a href="mailto:cytospune@gmail.com">cytospune@gmail.com</a></p>
          </div>
        </div>
      </div>
    </>
  );
}
