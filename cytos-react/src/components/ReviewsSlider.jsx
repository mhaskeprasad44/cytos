import React, { useState, useEffect } from 'react';

const reviews = [
  {
    initials: "SK",
    name: "Sanjay Kulkarni",
    designation: "GM - Production Automation, Tier-1 Auto Systems (Chakan MIDC)",
    avatarBg: "#eff6ff",
    avatarColor: "#1e40af",
    stars: 5,
    tag: "Robotic Dispensing SPM",
    review: "CyTOS delivered a 3-axis RTV silicone dispensing cell for our automotive headlamp assembly. Bead repeatability is strictly within ±0.02 mm across three shifts. Cycle time plummeted from 48 seconds manual to 16 seconds automated. Zero dispensing voids since 14 months of continuous production.",
    date: "February 2026",
    badge: "Verified Industrial Buyer"
  },
  {
    initials: "AD",
    name: "Anil Deshmukh",
    designation: "Plant Head, Precision PCB Solutions (Bhosari MIDC)",
    avatarBg: "#fef3c7",
    avatarColor: "#92400e",
    stars: 5,
    tag: "PCB-60 Micro-Drilling Machine",
    review: "Our multi-layer FR4 boards require clean 0.3 mm micro-vias without internal smear. The 60,000 RPM high-frequency spindle with auto-height mapping eliminated our via wander issues. Drill bit life jumped by nearly 40% due to the vibration-free pneumatic collet.",
    date: "January 2026",
    badge: "Verified Industrial Buyer"
  },
  {
    initials: "RM",
    name: "Rahul Mehta",
    designation: "Director - R&D Hardware Lab (Bengaluru / Electronic City)",
    avatarBg: "#f3e8ff",
    avatarColor: "#6b21a8",
    stars: 5,
    tag: "Chemical-Free PCB Prototyping",
    review: "The CyTOS benchtop isolation milling machine was a game changer for our hardware startup. We turn Eagle and KiCad Gerber files into double-sided working prototypes in 30 minutes flat. No harmful chemical etching baths, zero hazardous waste disposal headaches.",
    date: "March 2026",
    badge: "Verified R&D Lab"
  },
  {
    initials: "VG",
    name: "Vikram Gaikwad",
    designation: "Managing Director, AutoComponent Fixtures (Talegaon MIDC)",
    avatarBg: "#ecfdf5",
    avatarColor: "#065f46",
    stars: 5,
    tag: "Pneumatic Welding Fixtures",
    review: "We commissioned 4 sets of robotic welding fixtures for exhaust manifold fabrication. The clamping sequence and Poka-Yoke part presence sensors ensure 100% repeatable weld gap. CyTOS completed trial runs at their Bhosari shop before dispatch. Highly recommended.",
    date: "December 2025",
    badge: "Verified Industrial Buyer"
  },
  {
    initials: "PN",
    name: "Pooja Naik",
    designation: "Chief Technical Officer, Switchgear Enclosures (Aurangabad)",
    avatarBg: "#fef2f2",
    avatarColor: "#991b1b",
    stars: 5,
    tag: "VDM Milling Machine",
    review: "The BT30 Vertical Milling machine performs non-stop cutout milling and multi-tap drilling on CRCA 2.5 mm switchboard plates. Rigid cast frame, zero chatter, and Siemens CNC controls make operation effortless for our operators.",
    date: "November 2025",
    badge: "Verified Industrial Buyer"
  }
];

export default function ReviewsSlider() {
  const [currentIndex, setCurrentIndex] = useState(0);

  // Auto-advance
  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentIndex(prev => (prev + 1) % reviews.length);
    }, 6000);
    return () => clearInterval(timer);
  }, []);

  const handlePrev = () => {
    setCurrentIndex(prev => (prev === 0 ? reviews.length - 1 : prev - 1));
  };

  const handleNext = () => {
    setCurrentIndex(prev => (prev + 1) % reviews.length);
  };

  return (
    <div className="reviews-section-wrapper">
      <div className="reviews-header-row">
        <div>
          <span className="badge badge-primary">Industry Validated</span>
          <h2 className="section-title">What Production Heads & Engineers Say</h2>
          <p className="section-subtitle">Real feedback from Tier-1 automotive plants, electronics fabs, and R&D labs running CyTOS machines 24/7.</p>
        </div>
        <div className="reviews-nav-controls">
          <button className="slider-nav-btn prev" onClick={handlePrev} aria-label="Previous review">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" strokeWidth="2">
              <polyline points="15 18 9 12 15 6"></polyline>
            </svg>
          </button>
          <span className="reviews-slider-counter">{currentIndex + 1} / {reviews.length}</span>
          <button className="slider-nav-btn next" onClick={handleNext} aria-label="Next review">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" strokeWidth="2">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </button>
        </div>
      </div>

      <div className="reviews-slider-viewport">
        <div
          className="reviews-slider-track"
          style={{
            transform: `translateX(-${currentIndex * 100}%)`,
            transition: 'transform 0.45s cubic-bezier(0.25, 1, 0.5, 1)'
          }}
        >
          {reviews.map((rev, idx) => (
            <div key={idx} className="review-testimonial-card" style={{ flex: '0 0 100%', minWidth: '100%' }}>
              <div>
                <div className="review-card-top">
                  <div className="reviewer-profile">
                    <div
                      className="reviewer-avatar-circle"
                      style={{ background: rev.avatarBg, color: rev.avatarColor }}
                    >
                      {rev.initials}
                    </div>
                    <div>
                      <div className="reviewer-name">{rev.name}</div>
                      <div className="reviewer-designation">{rev.designation}</div>
                    </div>
                  </div>
                  <div className="google-source-badge">
                    <span>Google Review ★★★★★</span>
                  </div>
                </div>

                <div className="review-stars-row">
                  <div className="stars-gold">★★★★★</div>
                  <span className="review-date">{rev.date}</span>
                  <span className="badge badge-outline" style={{ fontSize: '0.72rem', padding: '0.2rem 0.5rem' }}>{rev.tag}</span>
                </div>

                <p className="review-body-text">"{rev.review}"</p>
              </div>

              <div className="review-card-footer">
                <span className="verified-badge">✓ {rev.badge}</span>
                <span className="midc-location-stamp">Maharashtra Industrial Corridor</span>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="reviews-slider-dots">
        {reviews.map((_, i) => (
          <button
            key={i}
            className={`slider-dot ${i === currentIndex ? 'active' : ''}`}
            onClick={() => setCurrentIndex(i)}
            aria-label={`Go to slide ${i + 1}`}
          />
        ))}
      </div>
    </div>
  );
}
