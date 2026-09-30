import React, { Suspense, lazy } from 'react';
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
        <Route path="/cnc-routers-milling" element={<CncRoutersPage />} />
        <Route path="/contact" element={<ContactPage />} />
        <Route path="/pcb-drilling-routing" element={<PcbDrillingPage />} />
        <Route path="/pcb-prototyping" element={<PcbPrototypingPage />} />
        <Route path="/plc-control-panels" element={<PlcPanelsPage />} />
        <Route path="/pneumatic-welding-fixtures" element={<PneumaticFixturesPage />} />
        <Route path="/privacy-policy" element={<PrivacyPolicyPage />} />
        <Route path="/robotic-dispensing-cells" element={<RoboticDispensingPage />} />
        <Route path="/spm-automation" element={<SpmAutomationPage />} />
        <Route path="/terms-conditions" element={<TermsPage />} />
        <Route path="/vdm-milling" element={<VdmMillingPage />} />
        
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
        <Route path="/cnc-routers-milling.html" element={<Navigate to="/cnc-routers-milling" replace />} />
        <Route path="/contact.html" element={<Navigate to="/contact" replace />} />
        <Route path="/pcb-drilling-routing.html" element={<Navigate to="/pcb-drilling-routing" replace />} />
        <Route path="/pcb-prototyping.html" element={<Navigate to="/pcb-prototyping" replace />} />
        <Route path="/plc-control-panels.html" element={<Navigate to="/plc-control-panels" replace />} />
        <Route path="/pneumatic-welding-fixtures.html" element={<Navigate to="/pneumatic-welding-fixtures" replace />} />
        <Route path="/privacy-policy.html" element={<Navigate to="/privacy-policy" replace />} />
        <Route path="/robotic-dispensing-cells.html" element={<Navigate to="/robotic-dispensing-cells" replace />} />
        <Route path="/spm-automation.html" element={<Navigate to="/spm-automation" replace />} />
        <Route path="/terms-conditions.html" element={<Navigate to="/terms-conditions" replace />} />
        <Route path="/vdm-milling.html" element={<Navigate to="/vdm-milling" replace />} />
        <Route path="/blog.html" element={<Navigate to="/blog" replace />} />

        {/* Fallback to Home */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
      <CookieConsent />
    </Suspense>
  );
}
