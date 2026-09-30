import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { machinesData } from '../data/machinesData';

export default function MachineFinder({ onOpenQuote }) {
  const [step, setStep] = useState(1);
  const [selection, setSelection] = useState({
    industry: '',
    material: '',
    volume: ''
  });

  const handleSelectIndustry = (ind) => {
    setSelection(prev => ({ ...prev, industry: ind }));
    setStep(2);
  };

  const handleSelectMaterial = (mat) => {
    setSelection(prev => ({ ...prev, material: mat }));
    setStep(3);
  };

  const handleSelectVolume = (vol) => {
    setSelection(prev => ({ ...prev, volume: vol }));
    setStep(4);
  };

  const resetFinder = () => {
    setSelection({ industry: '', material: '', volume: '' });
    setStep(1);
  };

  // Logic to determine recommended machine
  const getRecommendation = () => {
    const { industry, material } = selection;
    if (industry === 'pcb') {
      if (material === 'proto') return machinesData.find(m => m.id === 'pcb-prototyping');
      return machinesData.find(m => m.id === 'pcb-drilling');
    }
    if (industry === 'auto') {
      if (material === 'sealant') return machinesData.find(m => m.id === 'robotic-dispensing');
      return machinesData.find(m => m.id === 'pneumatic-fixtures');
    }
    if (industry === 'panel') {
      return machinesData.find(m => m.id === 'vdm-milling');
    }
    if (industry === 'automation') {
      return machinesData.find(m => m.id === 'spm-automation');
    }
    return machinesData.find(m => m.id === 'cnc-routers');
  };

  const recommendedMachine = getRecommendation() || machinesData[0];

  return (
    <div className="machine-finder-card">
      <div className="finder-header">
        <span className="badge badge-gold">Interactive Tool</span>
        <h3>Smart Machine Selector & Cycle Time Matcher</h3>
        <p>Answer 3 quick technical questions to find the ideal machine model and spindle configuration for your factory.</p>
      </div>

      {/* Progress Indicator */}
      <div className="finder-progress-bar">
        <div className={`step-dot ${step >= 1 ? 'active' : ''}`}>1. Application</div>
        <div className="step-line"></div>
        <div className={`step-dot ${step >= 2 ? 'active' : ''}`}>2. Material</div>
        <div className="step-line"></div>
        <div className={`step-dot ${step >= 3 ? 'active' : ''}`}>3. Production Volume</div>
        <div className="step-line"></div>
        <div className={`step-dot ${step === 4 ? 'active' : ''}`}>4. Result</div>
      </div>

      {/* Step 1: Industry / Application */}
      {step === 1 && (
        <div className="finder-step-content">
          <h4 className="step-title">Select Your Core Manufacturing Application:</h4>
          <div className="finder-options-grid">
            <button className="finder-opt-btn" onClick={() => handleSelectIndustry('cnc')}>
              <span className="opt-title">CNC Sheet Metal & Routing</span>
              <span className="opt-desc">Heavy cutting, 2D/3D carving, non-ferrous plates & composite</span>
            </button>
            <button className="finder-opt-btn" onClick={() => handleSelectIndustry('pcb')}>
              <span className="opt-title">Electronics & PCB Fabrication</span>
              <span className="opt-desc">60k RPM micro-hole drilling, via routing, or chemical-free prototyping</span>
            </button>
            <button className="finder-opt-btn" onClick={() => handleSelectIndustry('auto')}>
              <span className="opt-title">Automotive Assembly & Welding</span>
              <span className="opt-desc">Precision pneumatic jigs, welding fixtures, or adhesive dispensing</span>
            </button>
            <button className="finder-opt-btn" onClick={() => handleSelectIndustry('panel')}>
              <span className="opt-title">Switchboard & Enclosure Machining</span>
              <span className="opt-desc">Vertical drilling, multi-tapping & cutout milling on steel/aluminum panels</span>
            </button>
            <button className="finder-opt-btn" onClick={() => handleSelectIndustry('automation')}>
              <span className="opt-title">Custom Turnkey SPM Automation</span>
              <span className="opt-desc">Dedicated multi-station assembly, automated testing, or rotary transfer cells</span>
            </button>
          </div>
        </div>
      )}

      {/* Step 2: Primary Material */}
      {step === 2 && (
        <div className="finder-step-content">
          <h4 className="step-title">What is Your Primary Workpiece Material?</h4>
          <div className="finder-options-grid">
            {selection.industry === 'pcb' ? (
              <>
                <button className="finder-opt-btn" onClick={() => handleSelectMaterial('proto')}>
                  <span className="opt-title">Single/Double Sided FR4 (R&D Labs)</span>
                  <span className="opt-desc">Fast in-house prototyping without chemical etching</span>
                </button>
                <button className="finder-opt-btn" onClick={() => handleSelectMaterial('fr4')}>
                  <span className="opt-title">High-Tg FR4 & Multi-layer Rogers</span>
                  <span className="opt-desc">Production micro-via drilling from 0.2 mm at 60k RPM</span>
                </button>
                <button className="finder-opt-btn" onClick={() => handleSelectMaterial('metal')}>
                  <span className="opt-title">Aluminum-Clad MCPCB (LED / EV)</span>
                  <span className="opt-desc">Heavy copper & aluminum thermal core routing</span>
                </button>
              </>
            ) : selection.industry === 'auto' ? (
              <>
                <button className="finder-opt-btn" onClick={() => handleSelectMaterial('weld')}>
                  <span className="opt-title">Stamped Sheet Metal Parts & Tubes</span>
                  <span className="opt-desc">Robot welding fixtures with toggle clamps</span>
                </button>
                <button className="finder-opt-btn" onClick={() => handleSelectMaterial('sealant')}>
                  <span className="opt-title">RTV Silicone / PU Adhesive / Epoxies</span>
                  <span className="opt-desc">Automated fluid dispensing & gasket sealing</span>
                </button>
              </>
            ) : (
              <>
                <button className="finder-opt-btn" onClick={() => handleSelectMaterial('al')}>
                  <span className="opt-title">Aluminum / Brass / Copper</span>
                  <span className="opt-desc">High-speed non-ferrous milling with mist cooling</span>
                </button>
                <button className="finder-opt-btn" onClick={() => handleSelectMaterial('steel')}>
                  <span className="opt-title">CRCA Sheet / Mild Steel Plates</span>
                  <span className="opt-desc">Rigid vertical tapping & cutout machining</span>
                </button>
                <button className="finder-opt-btn" onClick={() => handleSelectMaterial('acryl')}>
                  <span className="opt-title">Acrylic / Foam / Wood / Composite</span>
                  <span className="opt-desc">High rapid traverse speed router beds</span>
                </button>
              </>
            )}
          </div>
          <div className="step-back-btn">
            <button className="btn btn-outline btn-sm" onClick={() => setStep(1)}>← Change Application</button>
          </div>
        </div>
      )}

      {/* Step 3: Production Volume */}
      {step === 3 && (
        <div className="finder-step-content">
          <h4 className="step-title">What is Your Estimated Production Throughput?</h4>
          <div className="finder-options-grid">
            <button className="finder-opt-btn" onClick={() => handleSelectVolume('low')}>
              <span className="opt-title">R&D Lab / Rapid Prototyping</span>
              <span className="opt-desc">1 - 20 parts/day with quick job changeovers</span>
            </button>
            <button className="finder-opt-btn" onClick={() => handleSelectVolume('mid')}>
              <span className="opt-title">Batch Manufacturing (1-2 Shifts)</span>
              <span className="opt-desc">50 - 500 parts/day with dedicated fixturing</span>
            </button>
            <button className="finder-opt-btn" onClick={() => handleSelectVolume('high')}>
              <span className="opt-title">Mass Production (24/7 Continuous)</span>
              <span className="opt-desc">1,000+ parts/day with automated loading & multi-spindle</span>
            </button>
          </div>
          <div className="step-back-btn">
            <button className="btn btn-outline btn-sm" onClick={() => setStep(2)}>← Change Material</button>
          </div>
        </div>
      )}

      {/* Step 4: Matched Machine Result */}
      {step === 4 && (
        <div className="finder-result-box">
          <div className="result-header">
            <span className="badge badge-success">Optimal Machine Match</span>
            <h4>{recommendedMachine.name}</h4>
            <p className="result-tagline">{recommendedMachine.tagline}</p>
          </div>

          <div className="result-grid">
            <div className="result-img-wrap">
              <img src={recommendedMachine.image} alt={recommendedMachine.name} />
            </div>
            <div className="result-specs-wrap">
              <div className="result-spec-item">
                <span className="label">Spindle Rating:</span>
                <span className="value">{recommendedMachine.spindle}</span>
              </div>
              <div className="result-spec-item">
                <span className="label">Max RPM:</span>
                <span className="value">{recommendedMachine.rpm}</span>
              </div>
              <div className="result-spec-item">
                <span className="label">Working Bed:</span>
                <span className="value">{recommendedMachine.bedSize}</span>
              </div>
              <div className="result-spec-item">
                <span className="label">Positional Repeatability:</span>
                <span className="value">{recommendedMachine.accuracy}</span>
              </div>
              <div className="result-spec-item">
                <span className="label">Best For Materials:</span>
                <span className="value">{recommendedMachine.materials}</span>
              </div>

              <div className="result-actions">
                <button
                  className="btn btn-primary"
                  onClick={() => onOpenQuote(recommendedMachine.name)}
                >
                  Request Technical Quotation
                </button>
                <Link to={recommendedMachine.path} className="btn btn-outline">
                  View Full Machine Specs →
                </Link>
                <button className="btn btn-link" onClick={resetFinder}>
                  ↻ Retake Selector
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
