import fs from 'fs';
import { videosData } from '../src/data/videosData.js';

let homeContent = fs.readFileSync('src/pages/HomePage.jsx', 'utf8');

// Build cards that play directly in-place on the same thumbnail
const videoCardsHtml = videosData.map(v => {
  let catClass = 'spm';
  let catLabel = 'SPM Automation';
  if (v.category.includes('PCB')) {
    catClass = 'pcb';
    catLabel = 'PCB Drilling & Routing';
  } else if (v.category.includes('Milling') || v.category.includes('Welding') || v.category.includes('Packaging')) {
    catClass = 'milling';
    catLabel = v.category;
  }

  return `          <article class="video-card" data-category="${catClass}">
            <div class="video-thumb-box" data-video-id="${v.id}" data-video-title="${v.title.replace(/"/g, '&quot;')}" data-video-path="${v.relatedMachinePath}" data-video-machine="${v.title.replace(/"/g, '&quot;')}" title="Click to watch ${v.title.replace(/"/g, '&quot;')}">
              <img src="${v.thumbnail}" alt="${v.title.replace(/"/g, '&quot;')}" loading="lazy" class="video-thumb-img">
              <div class="video-play-overlay">
                <div class="video-play-circle" aria-label="Play ${v.title.replace(/"/g, '&quot;')}">
                  <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor" aria-hidden="true"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                </div>
              </div>
              <span class="video-duration-pill">${v.duration}</span>
            </div>
            <div class="video-card-body">
              <div class="video-card-meta">
                <span class="video-badge-tag">${catLabel}</span>
                <span style="font-size: 0.75rem; color: #94a3b8; font-weight: 600;">Autoplay 4K</span>
              </div>
              <h3 class="video-card-title">${v.title}</h3>
              <p class="video-card-desc">${v.description}</p>
              <div class="video-card-actions">
                <button class="btn btn-primary btn-sm btn-play-trigger" style="flex: 1; padding: 0.55rem 0.85rem; font-size: 0.85rem;" data-video-id="${v.id}" data-video-title="${v.title.replace(/"/g, '&quot;')}" data-video-path="${v.relatedMachinePath}" data-video-machine="${v.title.replace(/"/g, '&quot;')}">
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor" style="margin-right: 5px; vertical-align: -2px;" aria-hidden="true"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                  <span>Watch Video</span>
                </button>
                <a href="${v.relatedMachinePath}" class="btn-card-specs">
                  <span>Specs ❯</span>
                </a>
              </div>
            </div>
          </article>`;
}).join('\n');

const videoSchema = {
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "CyTOS Official Machinery Demonstration Videos",
  "description": "Video demonstrations of industrial PCB drilling machines, custom SPMs, robotic dispensing cells, and automated thermal foam welders by CyTOS Pune.",
  "itemListElement": videosData.map((v, i) => ({
    "@type": "ListItem",
    "position": i + 1,
    "item": {
      "@type": "VideoObject",
      "name": v.title,
      "description": v.description,
      "thumbnailUrl": [v.thumbnail],
      "uploadDate": "2026-10-01T00:00:00+05:30",
      "contentUrl": v.youtubeUrl,
      "embedUrl": v.embedUrl,
      "publisher": {
        "@type": "Organization",
        "name": "CYCLE TIME OPTIMISING SOLUTIONS (CyTOS)",
        "logo": {
          "@type": "ImageObject",
          "url": "https://www.cytos.in/CyTOS New Logo.png"
        }
      }
    }
  }))
};

const newShowcaseSectionHtml = `
  <!-- ==========================================================================
       6. Live Machinery in Action: Video Showcase Section (In-Place Thumbnail Playback)
       ========================================================================== -->
  <section class="video-showcase-section" id="videos" aria-label="Machinery Video Demonstrations">
    <script type="application/ld+json">${JSON.stringify(videoSchema)}</script>
    <div class="container">
      <div class="video-section-header">
        <div class="hero-badge" style="background: rgba(37,99,235,0.2); border-color: rgba(59,130,246,0.35); color: #93c5fd; margin: 0 auto 0.75rem;">
          <span>VERIFIED FACTORY FOOTAGE • AUTOPLAY 4K DEMOS</span>
        </div>
        <h2 class="section-title" style="color: #ffffff;">
          Machinery in Action — <span class="gradient-text">Live Demonstration Videos</span>
        </h2>
        <p class="section-subtitle" style="color: #94a3b8; max-width: 720px; margin: 0 auto;">
          Watch industrial 125,000 RPM PCB drilling, 100% chemical-free circuit prototyping, robotic dispensing, and thermal foam fusion running live at our Pune facility. Click any demonstration to watch in theatre popup with instant autoplay.
        </p>

        <!-- Category Filter Tabs -->
        <div class="video-filter-tabs" role="tablist">
          <button class="video-tab-chip active" data-filter="all" role="tab">
            <span>All Demonstrations</span>
            <span class="video-tab-count">11</span>
          </button>
          <button class="video-tab-chip" data-filter="pcb" role="tab">
            <span>PCB Manufacturing</span>
            <span class="video-tab-count">4</span>
          </button>
          <button class="video-tab-chip" data-filter="spm" role="tab">
            <span>SPM Automation &amp; Robotics</span>
            <span class="video-tab-count">5</span>
          </button>
          <button class="video-tab-chip" data-filter="milling" role="tab">
            <span>Milling &amp; Foam Welding</span>
            <span class="video-tab-count">2</span>
          </button>
        </div>
      </div>

      <!-- Videos Grid -->
      <div class="video-grid" id="videoGridContainer">
${videoCardsHtml}
      </div>

      <!-- Bottom YouTube Channel Conversion Bar -->
      <div style="margin-top: 3.5rem; background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 2rem; display: flex; align-items: center; justify-content: space-between; gap: 1.5rem; flex-wrap: wrap;">
        <div style="display: flex; align-items: center; gap: 1rem;">
          <div style="width: 50px; height: 50px; background: #dc2626; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #fff; flex-shrink: 0; box-shadow: 0 4px 15px rgba(220, 38, 38, 0.4);">
            <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          </div>
          <div>
            <h4 style="margin: 0 0 0.25rem; color: #ffffff; font-size: 1.15rem; font-weight: 700;">Subscribe to CyTOS Official YouTube Channel</h4>
            <p style="margin: 0; color: #94a3b8; font-size: 0.88rem;">New machinery cut-tests, live customer trials, and CNC engineering walkthroughs published weekly.</p>
          </div>
        </div>
        <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
          <a href="https://www.youtube.com/channel/UCIDSzh9jMLfUf_xC9CLEt1A" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="border-color: rgba(255,255,255,0.25); color: #ffffff;">
            <span>Visit YouTube Channel ↗</span>
          </a>
          <button class="btn btn-primary" data-open-rfq data-machine="Video Demonstration Cutting Trial">
            <span>Schedule Live Trial at Pune Plant</span>
          </button>
        </div>
      </div>
    </div>
  </section>
`;

const formattedSection = newShowcaseSectionHtml
  .replace(/\\/g, '\\\\')
  .replace(/"/g, '\\"')
  .replace(/\r?\n/g, '\\r\\n');

// Find start and end of the existing video-showcase-section in HomePage.jsx
const markerStart = 'video-showcase-section';
const idxStart = homeContent.indexOf(markerStart);

if (idxStart !== -1) {
  // Find opening '<section' tag before marker
  const tagStart = homeContent.lastIndexOf('<section', idxStart);
  // Find '</section>' that closes this section (after the YouTube Subscribe bar)
  const markerEnd = 'Visit YouTube Channel';
  const idxMarkerEnd = homeContent.indexOf(markerEnd, idxStart);
  if (idxMarkerEnd !== -1) {
    const tagEnd = homeContent.indexOf('</section>', idxMarkerEnd) + '</section>'.length;
    // Also if there was a videoModal backdrop right after it, remove it
    let finalEnd = tagEnd;
    const modalMarker = 'videoModal';
    const idxModal = homeContent.indexOf(modalMarker, tagEnd);
    if (idxModal !== -1 && idxModal - tagEnd < 200) {
      const modalEnd = homeContent.indexOf('</section>', idxModal);
      if (modalEnd !== -1) {
        finalEnd = modalEnd + '</section>'.length;
      }
    }
    homeContent = homeContent.slice(0, tagStart) + formattedSection.trim() + homeContent.slice(finalEnd);
    fs.writeFileSync('src/pages/HomePage.jsx', homeContent, 'utf8');
    console.log('Successfully updated HomePage.jsx with direct in-place thumbnail video player!');
  }
} else {
  console.error('Could not find video-showcase-section in HomePage.jsx');
}
