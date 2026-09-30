import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

export default function CookieConsent() {
  const [isOpen, setIsOpen] = useState(false);
  const [showSettings, setShowSettings] = useState(false);
  const [consentGiven, setConsentGiven] = useState(false);
  const [preferences, setPreferences] = useState({
    necessary: true,
    analytics: true,
    functional: true
  });

  useEffect(() => {
    // Check if consent was already recorded in localStorage
    try {
      const saved = localStorage.getItem('cytos_cookie_consent');
      if (saved) {
        setConsentGiven(true);
        const parsed = JSON.parse(saved);
        if (parsed && typeof parsed === 'object') {
          setPreferences({
            necessary: true,
            analytics: parsed.analytics !== false,
            functional: parsed.functional !== false
          });
        }
      } else {
        // If first visit, show after a smooth 800ms delay
        const timer = setTimeout(() => {
          setIsOpen(true);
        }, 800);
        return () => clearTimeout(timer);
      }
    } catch (e) {
      // LocalStorage fallback
      setIsOpen(true);
    }
  }, []);

  const handleAcceptAll = () => {
    const all = { necessary: true, analytics: true, functional: true, timestamp: new Date().toISOString() };
    try {
      localStorage.setItem('cytos_cookie_consent', JSON.stringify(all));
    } catch (e) {}
    setPreferences(all);
    setConsentGiven(true);
    setIsOpen(false);
    setShowSettings(false);
  };

  const handleNecessaryOnly = () => {
    const nec = { necessary: true, analytics: false, functional: false, timestamp: new Date().toISOString() };
    try {
      localStorage.setItem('cytos_cookie_consent', JSON.stringify(nec));
    } catch (e) {}
    setPreferences(nec);
    setConsentGiven(true);
    setIsOpen(false);
    setShowSettings(false);
  };

  const handleSaveCustom = () => {
    const custom = { ...preferences, necessary: true, timestamp: new Date().toISOString() };
    try {
      localStorage.setItem('cytos_cookie_consent', JSON.stringify(custom));
    } catch (e) {}
    setConsentGiven(true);
    setIsOpen(false);
    setShowSettings(false);
  };

  return (
    <>
      {/* 1. CookieYes-Style Persistent Floating Button in Bottom-Left Corner */}
      {!isOpen && (
        <div className="cytos-cookie-widget" style={{ position: 'fixed', bottom: '24px', left: '24px', zIndex: 99998 }}>
          <button
            type="button"
            onClick={() => setIsOpen(true)}
            className="cytos-cookie-float-btn"
            aria-label="Cookie & Privacy Consent Preferences"
            title="Cookie & Privacy Settings"
            style={{
              width: '46px',
              height: '46px',
              borderRadius: '50%',
              backgroundColor: '#d97706',
              color: '#ffffff',
              border: '2px solid rgba(255, 255, 255, 0.9)',
              boxShadow: '0 4px 14px rgba(217, 119, 6, 0.35)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              cursor: 'pointer',
              transition: 'all 0.25s cubic-bezier(0.16, 1, 0.3, 1)',
              outline: 'none'
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.transform = 'scale(1.1)';
              e.currentTarget.style.boxShadow = '0 6px 20px rgba(217, 119, 6, 0.5)';
              e.currentTarget.style.backgroundColor = '#d97706';
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.transform = 'scale(1)';
              e.currentTarget.style.boxShadow = '0 4px 14px rgba(217, 119, 6, 0.35)';
              e.currentTarget.style.backgroundColor = '#d97706';
            }}
          >
            {/* Crisp Cookie SVG Icon */}
            <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor" aria-hidden="true">
              <path d="M21.598 11.064a1.006 1.006 0 0 0-.854-.172A3.993 3.993 0 0 1 15.6 6.353a1.006 1.006 0 0 0-.685-.945 4.025 4.025 0 0 1-2.613-3.804 1.006 1.006 0 0 0-.852-.99A10.038 10.038 0 0 0 2 10.5C2 16.299 6.701 21 12.5 21c5.441 0 9.943-4.135 10.088-9.553a1.004 1.004 0 0 0-.99-1.383zM12.5 19C7.813 19 4 15.187 4 10.5c0-3.32 1.91-6.19 4.68-7.61a6.035 6.035 0 0 0 1.91 3.5 5.992 5.992 0 0 0 5.46 4.79 6.002 6.002 0 0 0 4.95 4.67C19.78 17.58 16.42 19 12.5 19z" />
              <circle cx="8.5" cy="13.5" r="1.5" />
              <circle cx="12" cy="16" r="1.25" />
              <circle cx="15.5" cy="13.5" r="1.25" />
              <circle cx="10" cy="9.5" r="1" />
            </svg>
          </button>
        </div>
      )}

      {/* 2. Interactive Consent Box / Modal */}
      {isOpen && (
        <div
          role="dialog"
          aria-modal="true"
          aria-label="Cookie & Privacy Consent"
          style={{
            position: 'fixed',
            bottom: '24px',
            left: '24px',
            maxWidth: '480px',
            width: 'calc(100% - 48px)',
            backgroundColor: '#ffffff',
            borderRadius: '12px',
            boxShadow: '0 20px 40px -10px rgba(15, 23, 42, 0.25), 0 0 0 1px rgba(15, 23, 42, 0.08)',
            zIndex: 99999,
            overflow: 'hidden',
            fontFamily: "'Roboto', sans-serif",
            animation: 'cytosSlideUp 0.3s cubic-bezier(0.16, 1, 0.3, 1)'
          }}
        >
          {/* Header */}
          <div
            style={{
              padding: '16px 20px',
              borderBottom: '1px solid #e2e8f0',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              backgroundColor: '#f8fafc'
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <span style={{ fontSize: '20px' }}>🍪</span>
              <h3 style={{ margin: 0, fontSize: '1.05rem', fontWeight: 700, color: '#0f172a' }}>
                Cookie & Privacy Preferences
              </h3>
            </div>
            <button
              type="button"
              onClick={() => setIsOpen(false)}
              aria-label="Close cookie consent box"
              style={{
                background: 'none',
                border: 'none',
                fontSize: '20px',
                color: '#64748b',
                cursor: 'pointer',
                padding: '4px 8px',
                lineHeight: 1
              }}
            >
              &times;
            </button>
          </div>

          {/* Body Content */}
          <div style={{ padding: '18px 20px', maxHeight: '340px', overflowY: 'auto' }}>
            <p style={{ margin: '0 0 12px', fontSize: '0.88rem', color: '#475569', lineHeight: 1.55 }}>
              CyTOS Machines uses cookies and local telemetry to deliver precision technical calculations, preserve machine RFQ quotes, and analyze traffic under India's <strong>DPDP Act 2023</strong>. We strictly do not sell your commercial data.
            </p>

            <div style={{ fontSize: '0.82rem', color: '#64748b', marginBottom: '14px' }}>
              Review our <Link to="/privacy-policy" onClick={() => setIsOpen(false)} style={{ color: '#b45309', fontWeight: 600, textDecoration: 'underline' }}>Privacy Policy</Link> and{' '}
              <Link to="/terms-conditions" onClick={() => setIsOpen(false)} style={{ color: '#b45309', fontWeight: 600, textDecoration: 'underline' }}>Terms & Conditions</Link>.
            </div>

            {/* Expandable Preferences Toggle */}
            <div style={{ marginBottom: '14px' }}>
              <button
                type="button"
                onClick={() => setShowSettings(!showSettings)}
                style={{
                  background: 'none',
                  border: 'none',
                  color: '#d97706',
                  fontWeight: 600,
                  fontSize: '0.84rem',
                  cursor: 'pointer',
                  padding: 0,
                  display: 'flex',
                  alignItems: 'center',
                  gap: '5px'
                }}
              >
                <span>{showSettings ? '▲ Hide Cookie Details' : '▼ Customize Cookie Preferences'}</span>
              </button>
            </div>

            {/* Granular Cookie Categories */}
            {showSettings && (
              <div style={{ background: '#f1f5f9', padding: '12px', borderRadius: '8px', marginBottom: '14px', fontSize: '0.82rem' }}>
                {/* Category 1 */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px', paddingBottom: '8px', borderBottom: '1px solid #e2e8f0' }}>
                  <div>
                    <strong style={{ color: '#0f172a' }}>Essential & Security</strong>
                    <div style={{ color: '#64748b', fontSize: '0.75rem' }}>Necessary for RFQ quotes, CAD uploads & security.</div>
                  </div>
                  <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#059669', background: '#ecfdf5', padding: '2px 6px', borderRadius: '4px' }}>Always Active</span>
                </div>

                {/* Category 2 */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px', paddingBottom: '8px', borderBottom: '1px solid #e2e8f0' }}>
                  <div>
                    <strong style={{ color: '#0f172a' }}>Performance & Analytics</strong>
                    <div style={{ color: '#64748b', fontSize: '0.75rem' }}>Aggregated telemetry to measure page speed and catalog visits.</div>
                  </div>
                  <input
                    type="checkbox"
                    checked={preferences.analytics}
                    onChange={(e) => setPreferences({ ...preferences, analytics: e.target.checked })}
                    style={{ cursor: 'pointer', width: '16px', height: '16px', accentColor: '#d97706' }}
                  />
                </div>

                {/* Category 3 */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div>
                    <strong style={{ color: '#0f172a' }}>Functional & Preferences</strong>
                    <div style={{ color: '#64748b', fontSize: '0.75rem' }}>Remembers machine filters, table units & chat history.</div>
                  </div>
                  <input
                    type="checkbox"
                    checked={preferences.functional}
                    onChange={(e) => setPreferences({ ...preferences, functional: e.target.checked })}
                    style={{ cursor: 'pointer', width: '16px', height: '16px', accentColor: '#d97706' }}
                  />
                </div>
              </div>
            )}
          </div>

          {/* Action Buttons */}
          <div
            style={{
              padding: '14px 20px',
              borderTop: '1px solid #e2e8f0',
              display: 'flex',
              gap: '10px',
              justifyContent: 'flex-end',
              flexWrap: 'wrap',
              backgroundColor: '#f8fafc'
            }}
          >
            {showSettings ? (
              <button
                type="button"
                onClick={handleSaveCustom}
                style={{
                  padding: '8px 16px',
                  borderRadius: '6px',
                  fontSize: '0.85rem',
                  fontWeight: 600,
                  backgroundColor: '#d97706',
                  color: '#ffffff',
                  border: 'none',
                  cursor: 'pointer'
                }}
              >
                Save Preferences
              </button>
            ) : null}
            <button
              type="button"
              onClick={handleNecessaryOnly}
              style={{
                padding: '8px 16px',
                borderRadius: '6px',
                fontSize: '0.85rem',
                fontWeight: 600,
                backgroundColor: '#ffffff',
                color: '#475569',
                border: '1px solid #cbd5e1',
                cursor: 'pointer'
              }}
            >
              Necessary Only
            </button>
            <button
              type="button"
              onClick={handleAcceptAll}
              style={{
                padding: '8px 18px',
                borderRadius: '6px',
                fontSize: '0.85rem',
                fontWeight: 700,
                backgroundColor: '#d97706',
                color: '#ffffff',
                border: 'none',
                cursor: 'pointer',
                boxShadow: '0 2px 6px rgba(217, 119, 6, 0.25)'
              }}
            >
              Accept All
            </button>
          </div>
        </div>
      )}

      {/* Global CSS for Animations and Legacy Banner Override */}
      <style>{`
        @keyframes cytosSlideUp {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        /* Hide any legacy static cookie consent banners so only the modern reactive CookieYes system operates */
        .cookie-consent-banner {
          display: none !important;
        }
        @media (max-width: 600px) {
          .cytos-cookie-widget {
            left: 14px !important;
            bottom: 14px !important;
          }
          .cytos-cookie-float-btn {
            width: 40px !important;
            height: 40px !important;
          }
        }
      `}</style>
    </>
  );
}
