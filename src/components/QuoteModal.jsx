import React, { useState } from 'react';

export default function QuoteModal({ isOpen, onClose, defaultMachine = '' }) {
  const [formData, setFormData] = useState({
    name: '',
    company: '',
    email: '',
    phone: '',
    machine: defaultMachine || 'CNC Routers',
    material: 'FR4 / Aluminum',
    notes: ''
  });
  const [submitted, setSubmitted] = useState(false);

  if (!isOpen) return null;

  const handleChange = (e) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);

    // Also offer WhatsApp direct pre-fill
    const message = `Hello CyTOS Engineering Team!%0A*RFQ Request Details:*%0A- *Name:* ${encodeURIComponent(formData.name)}%0A- *Company:* ${encodeURIComponent(formData.company)}%0A- *Phone:* ${encodeURIComponent(formData.phone)}%0A- *Email:* ${encodeURIComponent(formData.email)}%0A- *Machine Interested:* ${encodeURIComponent(formData.machine)}%0A- *Material:* ${encodeURIComponent(formData.material)}%0A- *Requirements:* ${encodeURIComponent(formData.notes)}`;
    
    // Redirect to WhatsApp after 1.5s
    setTimeout(() => {
      window.open(`https://wa.me/919422035109?text=${message}`, '_blank');
      setTimeout(() => {
        setSubmitted(false);
        onClose();
      }, 1000);
    }, 1200);
  };

  return (
    <div className="rfq-modal-overlay active" onClick={onClose} role="dialog" aria-modal="true">
      <div className="rfq-modal-card" onClick={e => e.stopPropagation()}>
        <button className="rfq-modal-close" onClick={onClose} aria-label="Close dialog">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>

        <div className="rfq-modal-header">
          <span className="badge badge-primary">Direct Factory Pricing</span>
          <h3>Request Technical Quote & Consultation</h3>
          <p>Get a formal quotation, cycle time estimation, and machine proposal within 4 business hours.</p>
        </div>

        {submitted ? (
          <div style={{ padding: '2.5rem 1rem', textAlign: 'center' }}>
            <div style={{ fontSize: '3rem', marginBottom: '1rem', color: '#16a34a' }}>✓</div>
            <h4 style={{ fontSize: '1.25rem', marginBottom: '0.5rem', color: 'var(--brand-primary)' }}>Request Received!</h4>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '1rem' }}>
              Redirecting you to our Application Engineers via WhatsApp for priority proposal generation...
            </p>
          </div>
        ) : (
          <form className="rfq-form" onSubmit={handleSubmit}>
            <div className="form-group-row">
              <div className="form-field">
                <label>Full Name *</label>
                <input
                  type="text"
                  name="name"
                  required
                  placeholder="e.g. Rajesh Sharma"
                  value={formData.name}
                  onChange={handleChange}
                />
              </div>
              <div className="form-field">
                <label>Company / Organization *</label>
                <input
                  type="text"
                  name="company"
                  required
                  placeholder="e.g. Precision Electronics Ltd"
                  value={formData.company}
                  onChange={handleChange}
                />
              </div>
            </div>

            <div className="form-group-row">
              <div className="form-field">
                <label>Business Email *</label>
                <input
                  type="email"
                  name="email"
                  required
                  placeholder="name@company.com"
                  value={formData.email}
                  onChange={handleChange}
                />
              </div>
              <div className="form-field">
                <label>Phone / WhatsApp Number *</label>
                <input
                  type="tel"
                  name="phone"
                  required
                  placeholder="+91 98765 43210"
                  value={formData.phone}
                  onChange={handleChange}
                />
              </div>
            </div>

            <div className="form-group-row">
              <div className="form-field">
                <label>Select Machine Category</label>
                <select name="machine" value={formData.machine} onChange={handleChange}>
                  <option value="CNC Routers">Heavy-Duty CNC Routers (Sheet Metal / Engraving)</option>
                  <option value="PCB Drilling & Routing">PCB Drilling & Routing Machines (60k RPM)</option>
                  <option value="PCB Prototyping">Chemical-Free PCB Prototyping (Auto-leveling)</option>
                  <option value="VDM Milling">Vertical Drilling & Milling (VDM BT30/BT40)</option>
                  <option value="Robotic Dispensing">Robotic Dispensing Cells (Automated SPM)</option>
                  <option value="Welding Fixtures">Pneumatic Welding Fixtures & Clamping</option>
                  <option value="PLC Panels">PLC & Industrial Control Panels</option>
                  <option value="Custom SPM">Custom Special Purpose Automation (SPM)</option>
                </select>
              </div>
              <div className="form-field">
                <label>Primary Workpiece Material</label>
                <input
                  type="text"
                  name="material"
                  placeholder="e.g. FR4, Aluminum, Brass, Mild Steel"
                  value={formData.material}
                  onChange={handleChange}
                />
              </div>
            </div>

            <div className="form-field">
              <label>Project Details / Cycle Time Requirements</label>
              <textarea
                name="notes"
                rows="3"
                placeholder="Mention component dimensions, cycle time target, or specific spindle requirements..."
                value={formData.notes}
                onChange={handleChange}
              ></textarea>
            </div>

            <div className="rfq-modal-footer">
              <button type="submit" className="btn btn-primary" style={{ width: '100%', justifyContent: 'center' }}>
                <span>Submit RFQ & Connect with Engineer</span>
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2">
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                  <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
              </button>
            </div>

            <div style={{ marginTop: '0.75rem', fontSize: '0.75rem', color: 'var(--text-muted)', textAlign: 'center' }}>
              🔒 ISO 9001:2015 Compliant Engineering. Your technical information is protected under NDA.
            </div>
          </form>
        )}
      </div>
    </div>
  );
}
