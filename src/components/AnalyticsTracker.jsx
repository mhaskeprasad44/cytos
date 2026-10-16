import { useEffect, useRef } from 'react';
import { useLocation } from 'react-router-dom';

/**
 * AnalyticsTracker
 * Ensures Google Analytics (GA4), Google Tag Manager (GTM), and Microsoft Clarity
 * accurately record virtual page views and navigation events across React Router SPA route transitions.
 */
export default function AnalyticsTracker() {
  const location = useLocation();
  const isFirstRender = useRef(true);

  useEffect(() => {
    // Initial page load is handled by the index.html snippet.
    // For subsequent client-side route transitions, dispatch page_view events.
    if (isFirstRender.current) {
      isFirstRender.current = false;
      return;
    }

    // Allow a small delay (120ms) for page components (HtmlPageWrapper / SEO) to update document.title & canonical
    const timer = setTimeout(() => {
      const pagePath = location.pathname + location.search + location.hash;
      const pageTitle = document.title || 'CyTOS Machines Pune';
      const pageLocation = window.location.href;

      // 1. Google Analytics 4 (gtag.js)
      if (typeof window.gtag === 'function') {
        window.gtag('config', 'G-TLPML4D2SB', {
          page_path: pagePath,
          page_title: pageTitle,
          page_location: pageLocation
        });
        window.gtag('event', 'page_view', {
          page_path: pagePath,
          page_title: pageTitle,
          page_location: pageLocation
        });
      }

      // 2. Google Tag Manager (dataLayer)
      if (Array.isArray(window.dataLayer)) {
        window.dataLayer.push({
          event: 'page_view',
          page_path: pagePath,
          page_title: pageTitle,
          page_location: pageLocation
        });
      }

      // 3. Microsoft Clarity (SPA Page Attribution)
      if (typeof window.clarity === 'function') {
        try {
          window.clarity('set', 'page', pagePath);
        } catch (e) {
          // Fallback if set page is not supported
        }
      }
    }, 120);

    return () => clearTimeout(timer);
  }, [location.pathname, location.search, location.hash]);

  return null;
}
