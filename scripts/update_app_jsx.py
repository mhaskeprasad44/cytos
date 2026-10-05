# -*- coding: utf-8 -*-
"""
scripts/update_app_jsx.py
Updates src/App.jsx with all new product page routes and redirects.
"""

import os

ROOT = r"c:\Users\PrasadMhaske\Downloads\Project1"
APP_FILE = os.path.join(ROOT, "src", "App.jsx")

app_content = """import React, { Suspense, lazy } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';

import HomePage from './pages/HomePage';
import AboutPage from './pages/AboutPage';
import ApplicationsPage from './pages/ApplicationsPage';
import CaseStudiesPage from './pages/CaseStudiesPage';
import CncRoutersPage from './pages/CncRoutersPage';
import ContactPage from './pages/ContactPage';
import PcbDrillingPage from './pages/PcbDrillingPage';
import PcbPrototypingPage from './pages/PcbPrototypingPage';
import PlcPanelsPage from './pages/PlcPanelsPage';
import PneumaticFixturesPage from './pages/PneumaticFixturesPage';
import PrivacyPolicyPage from './pages/PrivacyPolicyPage';
import RoboticDispensingPage from './pages/RoboticDispensingPage';
import SpmAutomationPage from './pages/SpmAutomationPage';
import TermsPage from './pages/TermsPage';
import VdmMillingPage from './pages/VdmMillingPage';
import BlogListingPage from './pages/BlogListingPage';
import CookieConsent from './components/CookieConsent';
import { blogArticles } from './data/blogData';

// Standalone Individual Machine Pages
import Cnc6060Page from './pages/Cnc6060Page';
import Cnc3020Page from './pages/Cnc3020Page';
import Cnc3030Page from './pages/Cnc3030Page';
import Pcb12MultiSpindlePage from './pages/Pcb12MultiSpindlePage';
import CncWoodAcrylicAluminiumRouterPage from './pages/CncWoodAcrylicAluminiumRouterPage';
import VdmHeavyDrillingMillingPage from './pages/VdmHeavyDrillingMillingPage';
import FoamWeldingMachinePage from './pages/FoamWeldingMachinePage';
import EducationalCncPage from './pages/EducationalCncPage';

const BlogPostPage = lazy(() => import('./pages/BlogPostPage'));

function PageLoader() {
  return (
    <div style={{ minHeight: '60vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ width: '40px', height: '40px', border: '3px solid #e2e8f0', borderTopColor: '#0a369d', borderRadius: '50%', animation: 'spin 0.8s linear infinite' }} />
      <style>{`@keyframes spin { to { transform: rotate(360deg); } }`}</style>
    </div>
  );
}

export default function App() {
  return (
    <Suspense fallback={<PageLoader />}>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/applications" element={<ApplicationsPage />} />
        <Route path="/case-studies" element={<CaseStudiesPage />} />
        <Route path="/contact" element={<ContactPage />} />
        <Route path="/privacy-policy" element={<PrivacyPolicyPage />} />
        <Route path="/terms-conditions" element={<TermsPage />} />
        
        {/* Machine Category Hubs */}
        <Route path="/pcb-drilling-routing" element={<PcbDrillingPage />} />
        <Route path="/pcb-prototyping" element={<PcbPrototypingPage />} />
        <Route path="/cnc-routers-milling" element={<CncRoutersPage />} />
        <Route path="/vdm-milling" element={<VdmMillingPage />} />
        <Route path="/robotic-dispensing-cells" element={<RoboticDispensingPage />} />
        <Route path="/pneumatic-welding-fixtures" element={<PneumaticFixturesPage />} />
        <Route path="/plc-control-panels" element={<PlcPanelsPage />} />
        <Route path="/spm-automation" element={<SpmAutomationPage />} />

        {/* Dedicated Individual Machine Pages */}
        <Route path="/cnc-6060-pcb-drilling-routing-machine" element={<Cnc6060Page />} />
        <Route path="/cnc-3020-pcb-prototyping-machine" element={<Cnc3020Page />} />
        <Route path="/cnc-3030-pcb-prototyping-machine" element={<Cnc3030Page />} />
        <Route path="/pcb12-multi-spindle-drilling-machine" element={<Pcb12MultiSpindlePage />} />
        <Route path="/cnc-wood-acrylic-aluminium-router-machine" element={<CncWoodAcrylicAluminiumRouterPage />} />
        <Route path="/vdm-heavy-vertical-drilling-milling-machine" element={<VdmHeavyDrillingMillingPage />} />
        <Route path="/foam-welding-machine" element={<FoamWeldingMachinePage />} />
        <Route path="/educational-cnc-machines" element={<EducationalCncPage />} />

        {/* Blog Knowledge Hub */}
        <Route path="/blog" element={<BlogListingPage />} />
        <Route path="/blog/:slug" element={<BlogPostPage />} />
        <Route path="/blog/:slug.html" element={<BlogPostPage />} />

        {/* Naked blog slug redirects to /blog/:slug */}
        {blogArticles.map((b) => (
          <React.Fragment key={b.slug}>
            <Route path={`/${b.slug}`} element={<Navigate to={`/blog/${b.slug}`} replace />} />
            <Route path={`/${b.slug}.html`} element={<Navigate to={`/blog/${b.slug}`} replace />} />
          </React.Fragment>
        ))}

        {/* Direct .html aliases for backwards compatibility */}
        <Route path="/index.html" element={<Navigate to="/" replace />} />
        <Route path="/about.html" element={<Navigate to="/about" replace />} />
        <Route path="/applications.html" element={<Navigate to="/applications" replace />} />
        <Route path="/case-studies.html" element={<Navigate to="/case-studies" replace />} />
        <Route path="/contact.html" element={<Navigate to="/contact" replace />} />
        <Route path="/privacy-policy.html" element={<Navigate to="/privacy-policy" replace />} />
        <Route path="/terms-conditions.html" element={<Navigate to="/terms-conditions" replace />} />
        <Route path="/blog.html" element={<Navigate to="/blog" replace />} />

        <Route path="/pcb-drilling-routing.html" element={<Navigate to="/pcb-drilling-routing" replace />} />
        <Route path="/pcb-prototyping.html" element={<Navigate to="/pcb-prototyping" replace />} />
        <Route path="/cnc-routers-milling.html" element={<Navigate to="/cnc-routers-milling" replace />} />
        <Route path="/vdm-milling.html" element={<Navigate to="/vdm-milling" replace />} />
        <Route path="/robotic-dispensing-cells.html" element={<Navigate to="/robotic-dispensing-cells" replace />} />
        <Route path="/pneumatic-welding-fixtures.html" element={<Navigate to="/pneumatic-welding-fixtures" replace />} />
        <Route path="/plc-control-panels.html" element={<Navigate to="/plc-control-panels" replace />} />
        <Route path="/spm-automation.html" element={<Navigate to="/spm-automation" replace />} />

        {/* Dedicated Machine .html aliases */}
        <Route path="/cnc-6060-pcb-drilling-routing-machine.html" element={<Navigate to="/cnc-6060-pcb-drilling-routing-machine" replace />} />
        <Route path="/cnc-3020-pcb-prototyping-machine.html" element={<Navigate to="/cnc-3020-pcb-prototyping-machine" replace />} />
        <Route path="/cnc-3030-pcb-prototyping-machine.html" element={<Navigate to="/cnc-3030-pcb-prototyping-machine" replace />} />
        <Route path="/pcb12-multi-spindle-drilling-machine.html" element={<Navigate to="/pcb12-multi-spindle-drilling-machine" replace />} />
        <Route path="/cnc-wood-acrylic-aluminium-router-machine.html" element={<Navigate to="/cnc-wood-acrylic-aluminium-router-machine" replace />} />
        <Route path="/vdm-heavy-vertical-drilling-milling-machine.html" element={<Navigate to="/vdm-heavy-vertical-drilling-milling-machine" replace />} />
        <Route path="/foam-welding-machine.html" element={<Navigate to="/foam-welding-machine" replace />} />
        <Route path="/educational-cnc-machines.html" element={<Navigate to="/educational-cnc-machines" replace />} />

        {/* Fallback to Home */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
      <CookieConsent />
    </Suspense>
  );
}
"""

with open(APP_FILE, "w", encoding="utf-8") as f:
    f.write(app_content)

print("Updated src/App.jsx with all new routes and aliases.")
