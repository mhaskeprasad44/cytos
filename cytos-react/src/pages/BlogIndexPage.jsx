import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import SEO from '../components/SEO';
import { blogArticles } from '../data/blogData';

export default function BlogIndexPage() {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');

  const categories = ['All', 'PCB Drilling & Routing', 'PCB Prototyping', 'CNC Machining', 'Automation & SPM'];

  const filteredArticles = blogArticles.filter(art => {
    const matchesSearch = art.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                          art.metaDescription.toLowerCase().includes(searchTerm.toLowerCase()) ||
                          art.category.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCategory = selectedCategory === 'All' ||
                            art.category.toLowerCase().includes(selectedCategory.toLowerCase());
    return matchesSearch && matchesCategory;
  });

  return (
    <>
      <SEO
        title="Technical Blog & Engineering Guides | CyTOS Pune"
        description="Explore 22 technical engineering guides on 60,000 RPM PCB drilling, collet runout calibration, chemical-free isolation milling, CNC gantry routers, and robotic dispensing automation."
        canonical="https://cytos.in/blog"
      />

      <section className="page-header-section">
        <div className="container">
          <div className="breadcrumbs">
            <Link to="/">Home</Link>
            <span>/</span>
            <span className="current">Technical Blog</span>
          </div>

          <div className="page-header-content">
            <span className="badge badge-gold">Engineering Knowledge Hub</span>
            <h1 className="page-title">CyTOS Technical Guides & Machine Tool Metrology</h1>
            <p className="page-subtitle">
              Deep-dive engineering tutorials, cycle time benchmarking, spindle maintenance protocols, and isolation milling techniques authored by the CyTOS machine tool design team.
            </p>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="container">
          {/* Search & Category Filter Controls */}
          <div className="blog-filter-bar">
            <div className="blog-search-box">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2">
                <circle cx="11" cy="11" r="8"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
              </svg>
              <input
                type="text"
                placeholder="Search by topic, spindle, FR4, cycle time..."
                value={searchTerm}
                onChange={e => setSearchTerm(e.target.value)}
              />
            </div>

            <div className="blog-category-pills">
              {categories.map((cat, idx) => (
                <button
                  key={idx}
                  className={`category-pill-btn ${selectedCategory === cat ? 'active' : ''}`}
                  onClick={() => setSelectedCategory(cat)}
                >
                  {cat}
                </button>
              ))}
            </div>
          </div>

          <div style={{ marginBottom: '1.5rem', color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
            Showing <strong>{filteredArticles.length}</strong> technical articles
          </div>

          {/* Blog Cards Grid */}
          <div className="blog-cards-grid">
            {filteredArticles.map((art) => (
              <article key={art.slug} className="blog-post-card">
                <div className="blog-post-img-wrap">
                  <Link to={`/blog/${art.slug}`}>
                    <img src={art.image} alt={art.title} loading="lazy" />
                  </Link>
                  <span className="blog-category-badge">{art.category}</span>
                </div>

                <div className="blog-post-card-body">
                  <div className="blog-card-meta">
                    <span className="read-time">⏱️ {art.readTime}</span>
                    <span className="meta-sep">•</span>
                    <span className="iso-tag">ISO 9001:2015</span>
                  </div>

                  <h3 className="blog-card-title">
                    <Link to={`/blog/${art.slug}`}>{art.title}</Link>
                  </h3>

                  <p className="blog-card-excerpt">
                    {art.metaDescription || art.excerpt}
                  </p>

                  <div className="blog-card-footer">
                    <Link to={`/blog/${art.slug}`} className="read-more-link">
                      <span>Read Technical Guide</span>
                      <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2">
                        <line x1="5" y1="12" x2="19" y2="12"></line>
                        <polyline points="12 5 19 12 12 19"></polyline>
                      </svg>
                    </Link>
                  </div>
                </div>
              </article>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}
