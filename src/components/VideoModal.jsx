import React from 'react';

export default function VideoModal() {
  return (
    <div className="video-modal-backdrop" id="videoModal" aria-hidden="true" role="dialog" aria-modal="true" style={{ zIndex: 99999 }}>
      <div className="video-modal-content">
        <div className="video-modal-header">
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <span className="badge-mini" style={{ background: 'rgba(37,99,235,0.25)', color: '#93c5fd', borderColor: 'rgba(59,130,246,0.4)', fontWeight: 700 }}>
              VERIFIED WORKSHOP DEMO
            </span>
            <h3 className="video-modal-title" id="videoModalTitle">Machine Video Demonstration</h3>
          </div>
          <button type="button" className="video-modal-close" id="videoModalClose" aria-label="Close Video Player">&times;</button>
        </div>
        <div className="video-modal-frame-container">
          <iframe 
            id="videoModalIframe" 
            src="" 
            title="CyTOS Machinery Demonstration Video" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            allowFullScreen>
          </iframe>
        </div>
        <div className="video-modal-footer">
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{ display: 'inline-block', width: '8px', height: '8px', borderRadius: '50%', background: '#10b981', flexShrink: 0 }}></span>
            <span style={{ fontSize: '0.86rem', color: '#cbd5e1' }}>Filmed live at CyTOS facility in Bhosari MIDC, Pune • Direct Factory Supply</span>
          </div>
          <div style={{ display: 'flex', gap: '0.75rem', alignItems: 'center', flexWrap: 'wrap' }}>
            <a href="#" className="btn-modal-specs" id="videoModalSpecsBtn">
              <span>Machine Specs ❯</span>
            </a>
            <button type="button" className="btn btn-primary btn-sm" id="videoModalQuoteBtn" data-open-rfq data-machine="Featured Video Machine">
              <span>Request Machine Quote</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
