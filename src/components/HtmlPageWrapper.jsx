import React, { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { initAllPageScripts } from '../legacyScript';

export default function HtmlPageWrapper({ htmlContent, title, description, canonical }) {
  const containerRef = useRef(null);
  const navigate = useNavigate();

  useEffect(() => {
    // 1. Update Title and Meta
    if (title) {
      document.title = title;
      let ogTitle = document.querySelector('meta[property="og:title"]');
      if (ogTitle) ogTitle.setAttribute('content', title);
      let twTitle = document.querySelector('meta[name="twitter:title"]');
      if (twTitle) twTitle.setAttribute('content', title);
    }
    if (description) {
      let metaDesc = document.querySelector('meta[name="description"]');
      if (!metaDesc) {
        metaDesc = document.createElement('meta');
        metaDesc.setAttribute('name', 'description');
        document.head.appendChild(metaDesc);
      }
      metaDesc.setAttribute('content', description);
      let ogDesc = document.querySelector('meta[property="og:description"]');
      if (ogDesc) ogDesc.setAttribute('content', description);
      let twDesc = document.querySelector('meta[name="twitter:description"]');
      if (twDesc) twDesc.setAttribute('content', description);
    }

    // 2. Set Page-Specific Canonical URL
    const pathname = window.location.pathname || '/';
    const cleanPath = pathname === '/' ? '/' : pathname.replace(/\/$/, '');
    const canonicalUrl = canonical || (`https://www.cytos.in${cleanPath}`);

    let linkCanonical = document.querySelector('link[rel="canonical"]');
    if (!linkCanonical) {
      linkCanonical = document.createElement('link');
      linkCanonical.setAttribute('rel', 'canonical');
      document.head.appendChild(linkCanonical);
    }
    linkCanonical.setAttribute('href', canonicalUrl);

    let ogUrl = document.querySelector('meta[property="og:url"]');
    if (ogUrl) ogUrl.setAttribute('content', canonicalUrl);

    window.scrollTo(0, 0);

    // 2. Intercept internal links for React Router SPA navigation
    const container = containerRef.current;
    if (!container) return;

    const handleLinkClick = (e) => {
      const link = e.target.closest('a');
      if (!link) return;

      const href = link.getAttribute('href');
      if (!href) return;

      // Ignore anchor jumps, tel, mailto, whatsapp, target="_blank", or files
      if (
        href.startsWith('#') ||
        href.startsWith('tel:') ||
        href.startsWith('mailto:') ||
        href.includes('wa.me') ||
        link.target === '_blank' ||
        href.endsWith('.pdf') ||
        href.endsWith('.xml')
      ) {
        return;
      }

      // Check if external URL
      if (href.startsWith('http://') || href.startsWith('https://')) {
        return;
      }

      // Convert .html link to clean route path
      let [pathPart, hashPart] = href.split('#');
      let cleanPath = pathPart.replace(/\.html$/, '');
      if (cleanPath === 'index' || cleanPath === './index' || cleanPath === '/index') cleanPath = '/';
      else if (!cleanPath.startsWith('/')) cleanPath = '/' + cleanPath;

      e.preventDefault();
      navigate(cleanPath);
      if (hashPart) {
        setTimeout(() => {
          const el = document.getElementById(hashPart);
          if (el) el.scrollIntoView({ behavior: 'smooth' });
        }, 100);
      } else {
        window.scrollTo(0, 0);
      }
    };

    container.addEventListener('click', handleLinkClick);

    // 3. Initialize all interactive sliders, finder, tabs, accordions, modals
    const timer = setTimeout(() => {
      initAllPageScripts();
    }, 50);

    return () => {
      container.removeEventListener('click', handleLinkClick);
      clearTimeout(timer);
    };
  }, [htmlContent, title, description, navigate]);

  return (
    <div
      ref={containerRef}
      className="page-html-content-root"
      dangerouslySetInnerHTML={{ __html: htmlContent }}
    />
  );
}
