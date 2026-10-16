import React from 'react';

export default function VideoModal() {
  return (
    <div className="video-modal-backdrop" id="videoModal" aria-hidden="true" role="dialog" aria-modal="true" style={{ zIndex: 99999 }}>
      <div className="video-modal-content">
        <div className="video-modal-header">
          <h3 className="video-modal-title" id="videoModalTitle">Machine Video Demonstration</h3>
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
        <div className="video-modal-footer" style={{ display: 'flex', justifyContent: 'flex-end', gap: '0.75rem', alignItems: 'center', flexWrap: 'wrap' }}>
          <a href="#" className="btn-modal-specs" id="videoModalSpecsBtn">
            <span>Machine Specs ❯</span>
          </a>
          <button type="button" className="btn btn-primary btn-sm" id="videoModalQuoteBtn" data-open-rfq data-machine="Featured Video Machine">
            <span>Request Machine Quote</span>
          </button>
        </div>
      </div>
    </div>
  );
}
