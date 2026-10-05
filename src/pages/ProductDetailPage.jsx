import React from 'react';
import { Link } from 'react-router-dom';
import SEO from '../components/SEO';
import { machinesData } from '../data/machinesData';

export default function ProductDetailPage({ machineId, onOpenQuote }) {
  const machine = machinesData.find(m => m.id === machineId) || machinesData[0];

  return (
    <>
      <SEO
        title={`${machine.name} | CyTOS Machines Pune`}
        description={machine.description}
        canonical={`https://www.cytos.in${machine.path}`}
        keywords={`${machine.name}, CyTOS Pune, industrial machine, Bhosari MIDC, ${machine.category}`}
      />

      {/* Product Hero Header */}
      <section className="page-header-section">
        <div className="container">
          <div className="breadcrumbs">
            <Link to="/">Home</Link>
            <span>/</span>
            <Link to="/#products">Machines & SPM</Link>
            <span>/</span>
            <span className="current">{machine.name}</span>
          </div>

          <div className="page-header-content">
            <span className="badge badge-gold">{machine.badge}</span>
            <h1 className="page-title">{machine.name}</h1>
            <p className="page-subtitle">{machine.tagline}</p>
          </div>
        </div>
      </section>

      {/* Main Product Showcase */}
      <section className="section">
        <div className="container">
          <div className="product-detail-layout">
            {/* Left: Product Image & Quick Fact Card */}
            <div className="product-detail-media">
              <div className="product-main-image-wrap">
                <img src={machine.image} alt={machine.name} className="product-detail-main-img" />
              </div>

              <div className="product-specs-highlight-box">
                <h4>Core Performance Parameters</h4>
                <div className="highlight-specs-grid">
                  <div className="highlight-spec-item">
                    <span className="label">Spindle Power:</span>
                    <span className="value">{machine.spindle}</span>
                  </div>
                  <div className="highlight-spec-item">
                    <span className="label">Max Velocity:</span>
                    <span className="value">{machine.rpm}</span>
                  </div>
                  <div className="highlight-spec-item">
                    <span className="label">Standard Table:</span>
                    <span className="value">{machine.bedSize}</span>
                  </div>
                  <div className="highlight-spec-item">
                    <span className="label">Repeatability:</span>
                    <span className="value">{machine.accuracy}</span>
                  </div>
                  <div className="highlight-spec-item">
                    <span className="label">Workpiece Materials:</span>
                    <span className="value">{machine.materials}</span>
                  </div>
                </div>

                <div style={{ marginTop: '1.5rem' }}>
                  <button
                    className="btn btn-primary"
                    style={{ width: '100%', justifyContent: 'center' }}
                    onClick={() => onOpenQuote(machine.name)}
                  >
                    Request Machine Proposal & Pricing
                  </button>
                  <a
                    href="/cytos_newcatalog2026_with BG.pdf"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="btn btn-outline"
                    style={{ width: '100%', justifyContent: 'center', marginTop: '0.75rem' }}
                  >
                    Download 2026 Machine Catalog (PDF)
                  </a>
                </div>
              </div>
            </div>

            {/* Right: Technical Description & Deep Features */}
            <div className="product-detail-info">
              <div className="detail-section-block">
                <h3>Engineering Overview</h3>
                <p className="detail-text">{machine.description}</p>
                <p className="detail-text">
                  Manufactured at our Bhosari MIDC facility in Pune, each machine undergoes comprehensive laser interferometer calibration, dynamic spindle runout verification, and extended 72-hour burn-in trial before factory acceptance sign-off.
                </p>
              </div>

              {/* Technical Specifications Table */}
              <div className="detail-section-block">
                <h3>Detailed Technical Specifications</h3>
                <div className="table-responsive">
                  <table className="specs-table">
                    <thead>
                      <tr>
                        <th>Specification Parameter</th>
                        <th>Engineering Standard / Value</th>
                      </tr>
                    </thead>
                    <tbody>
                      {machine.specs.map((s, idx) => (
                        <tr key={idx}>
                          <td><strong>{s.label}</strong></td>
                          <td>{s.val}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>

              {/* Key Features & Advantages */}
              <div className="detail-section-block">
                <h3>Key Features & Design Advantages</h3>
                <ul className="product-features-bullet-list">
                  {machine.features.map((f, idx) => (
                    <li key={idx}>
                      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--brand-primary)" strokeWidth="2.5">
                        <polyline points="20 6 9 17 4 12"></polyline>
                      </svg>
                      <span>{f}</span>
                    </li>
                  ))}
                </ul>
              </div>

              {/* Trial & Delivery CTA */}
              <div className="factory-trial-cta-card">
                <h4>Schedule a Live Cutting Trial at Bhosari MIDC</h4>
                <p>
                  Bring your material or send component drawings (DXF/STEP) to our Pune works. Our application engineers will run a live demonstration, optimize toolpaths, and calculate exact cycle times.
                </p>
                <div className="cta-actions-row">
                  <button className="btn btn-primary" onClick={() => onOpenQuote(machine.name)}>
                    Request Trial & Quote
                  </button>
                  <a href="tel:+919422035109" className="btn btn-outline">
                    Call: +91 94220 35109
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Other Related Machines */}
      <section className="section bg-light">
        <div className="container">
          <div className="section-header-center">
            <span className="badge badge-primary">Explore Alternatives</span>
            <h2 className="section-title">Other Precision Machines by CyTOS</h2>
          </div>

          <div className="products-grid">
            {machinesData.filter(m => m.id !== machineId).slice(0, 3).map((m) => (
              <div key={m.id} className="product-card">
                <div className="product-card-image-wrap">
                  <img src={m.image} alt={m.name} loading="lazy" />
                  <span className="product-badge">{m.badge}</span>
                </div>
                <div className="product-card-body">
                  <span className="product-category-tag">{m.category}</span>
                  <h3 className="product-title">
                    <Link to={m.path}>{m.name}</Link>
                  </h3>
                  <p className="product-desc">{m.description}</p>
                  <div className="product-card-actions">
                    <Link to={m.path} className="btn btn-outline btn-sm">View Details →</Link>
                    <button className="btn btn-primary btn-sm" onClick={() => onOpenQuote(m.name)}>Quote</button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}
