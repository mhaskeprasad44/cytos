# -*- coding: utf-8 -*-
"""
Script to apply styling updates to styles.css
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update logo size
css = css.replace(
    '.brand-logo-img {\n  height: 48px;',
    '.brand-logo-img {\n  height: 56px;'
)

# 2. Add .section and uniform spacing rules if not already present
if '.section, .section-wrapper {' not in css:
    css = css.replace(
        '.section-wrapper {\n  padding: 4.5rem 0;\n  position: relative;\n}',
        '''.section, .section-wrapper {
  padding: 4.5rem 0;
  position: relative;
}

.section-sm {
  padding: 3rem 0;
}

.section-header, .section-head {
  text-align: center;
  max-width: 800px;
  margin: 0 auto 3rem;
}'''
    )

# 3. Add proof-metrics-grid 6-col rule and card styling
proof_metrics_old = '''.proof-metrics-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 1rem;
  text-align: center;
}'''

proof_metrics_new = '''.proof-metrics-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 1.25rem;
  text-align: center;
  width: 100%;
}

.proof-strip-section .proof-metrics-grid {
  grid-template-columns: repeat(5, 1fr);
}

.proof-metric-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 1.5rem 1rem;
  background: #ffffff;
  border: 1px solid var(--border-subtle);
  border-radius: 8px;
  box-shadow: var(--shadow-sm);
  transition: all var(--transition-fast);
}

.proof-metric-item:hover {
  border-color: var(--brand-gold);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.proof-metric-item .metric-number {
  font-size: 2.15rem;
  font-weight: 900;
  color: var(--brand-gold-dark);
  line-height: 1.1;
  margin-bottom: 0.45rem;
}

.proof-metric-item .metric-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-primary);
  line-height: 1.35;
}'''

if proof_metrics_old in css:
    css = css.replace(proof_metrics_old, proof_metrics_new)

# 4. Enhance button colors (eliminate muddy brown)
btn_primary_old = '''.btn-primary {
  background: var(--brand-gold);
  color: #ffffff;
  border-color: var(--brand-gold-dark);
  box-shadow: 0 2px 8px rgba(217, 119, 6, 0.25);
}

.btn-primary:hover {
  background: var(--brand-gold-dark);
  color: #ffffff;
  box-shadow: 0 4px 14px rgba(217, 119, 6, 0.35);
  transform: translateY(-1px);
}'''

btn_primary_new = '''.btn-primary {
  background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
  color: #ffffff;
  border: 1px solid #b45309;
  box-shadow: 0 2px 8px rgba(217, 119, 6, 0.25);
  font-weight: 600;
}

.btn-primary:hover {
  background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
  color: #ffffff;
  border-color: #b45309;
  box-shadow: 0 4px 14px rgba(217, 119, 6, 0.35);
  transform: translateY(-1px);
}'''

if btn_primary_old in css:
    css = css.replace(btn_primary_old, btn_primary_new)

# 5. Fix modal classes so that both .rfq-modal-overlay and .rfq-modal-backdrop are fixed and hidden
modal_rules = '''.rfq-modal-overlay,
.rfq-modal-backdrop {
  position: fixed !important;
  inset: 0 !important;
  top: 0 !important;
  left: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  background: rgba(15, 23, 42, 0.7) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  z-index: 99999 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 1.5rem !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  transition: all var(--transition-normal) !important;
}

.rfq-modal-overlay.active,
.rfq-modal-backdrop.active {
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
}

.rfq-modal-window,
.rfq-modal-container {
  background: #ffffff !important;
  border: 1px solid var(--border-medium) !important;
  border-radius: 12px !important;
  width: 100% !important;
  max-width: 660px !important;
  max-height: 90vh !important;
  overflow-y: auto !important;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.35) !important;
  position: relative !important;
  transform: translateY(16px) !important;
  transition: transform var(--transition-normal) !important;
}

.rfq-modal-overlay.active .rfq-modal-window,
.rfq-modal-backdrop.active .rfq-modal-container {
  transform: translateY(0) !important;
}'''

# Replace .rfq-modal-overlay block
rfq_overlay_start = css.find('.rfq-modal-overlay {')
if rfq_overlay_start != -1:
    rfq_window_end = css.find('.rfq-modal-overlay.active .rfq-modal-window {\n  transform: translateY(0);\n}', rfq_overlay_start)
    if rfq_window_end != -1:
        end_idx = rfq_window_end + len('.rfq-modal-overlay.active .rfq-modal-window {\n  transform: translateY(0);\n}')
        css = css[:rfq_overlay_start] + modal_rules + css[end_idx:]

# 6. Add master footer and map header styling
extra_footer_styles = '''
/* Standardized Dark Slate Master Footer */
.main-footer {
  background-color: #0b1120;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding: 4.5rem 0 2rem;
  font-size: 0.9rem;
  color: #94a3b8;
}

.footer-brand-logo {
  height: 52px;
  width: auto;
  object-fit: contain;
  margin-bottom: 1.25rem;
  display: block;
}

.footer-badge-item {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.78rem;
  font-weight: 600;
  color: #34d399;
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.2);
  padding: 0.35rem 0.75rem;
  border-radius: 999px;
  margin-top: 0.5rem;
}

.footer-badge-item .badge-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: #34d399;
}

.footer-col-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 1.25rem;
  position: relative;
  padding-bottom: 0.5rem;
}

.footer-col-title::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 28px;
  height: 2px;
  background-color: var(--brand-gold);
}

.footer-nav-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-nav-list li {
  margin-bottom: 0.65rem;
}

.footer-nav-list a {
  color: #94a3b8;
  transition: all var(--transition-fast);
  display: inline-block;
  font-size: 0.88rem;
}

.footer-nav-list a:hover {
  color: #f59e0b;
  transform: translateX(4px);
}

.footer-contact-list {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  font-style: normal;
}

.footer-contact-item {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  font-size: 0.88rem;
  color: #cbd5e1;
  line-height: 1.5;
}

.footer-contact-svg {
  width: 18px;
  height: 18px;
  color: var(--brand-gold-light);
  flex-shrink: 0;
  margin-top: 0.2rem;
}

.footer-contact-item a {
  color: #cbd5e1;
  font-weight: 500;
  transition: color var(--transition-fast);
}

.footer-contact-item a:hover {
  color: #f59e0b;
}

.map-header-bar {
  padding: 0.85rem 1.25rem;
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.75rem;
  font-size: 0.88rem;
}

.contact-method-icon svg {
  width: 24px;
  height: 24px;
  color: var(--brand-gold-dark);
}
'''

if '.footer-brand-logo' not in css:
    css += extra_footer_styles

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated styles.css successfully!')
