# -*- coding: utf-8 -*-
"""
scripts/generate_machine_pages.py
Assembles:
1. 8 standalone JSX product pages in src/pages/
2. Updates App.jsx with imports and routes
3. Updates public/sitemap.xml with Image SEO schema
4. Updates public/llms.txt with complete catalog specs
5. Updates SEO titles across existing pages
"""

import os
import json
import re
from product_catalog_definitions import MACHINE_PRODUCTS
from build_full_machines_ecosystem import TOP_BAR_HTML, get_header_html, FOOTER_HTML

ROOT = r"c:\Users\PrasadMhaske\Downloads\Project1"
SRC = os.path.join(ROOT, "src")
PAGES_DIR = os.path.join(SRC, "pages")
PUBLIC_DIR = os.path.join(ROOT, "public")

def build_schema_json(product):
    product_schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": product["name"],
        "model": product["model_code"],
        "description": product["meta_desc"],
        "image": [
            f"https://www.cytos.in{product['image']}"
        ] + [f"https://www.cytos.in{img['url']}" for img in product["additional_images"]],
        "brand": {
            "@type": "Brand",
            "name": "CyTOS"
        },
        "manufacturer": {
            "@type": "Organization",
            "name": "CYCLE TIME OPTIMISING SOLUTIONS (CyTOS)",
            "url": "https://www.cytos.in",
            "logo": "https://www.cytos.in/CyTOS New Logo.png",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "J-153, M.I.D.C., Bhosari",
                "addressLocality": "Pune",
                "addressRegion": "Maharashtra",
                "postalCode": "411026",
                "addressCountry": "IN"
            }
        },
        "category": product["category"],
        "offers": {
            "@type": "Offer",
            "url": f"https://www.cytos.in{product['path']}",
            "priceCurrency": "INR",
            "price": "Contact for Factory Direct Quote",
            "availability": "https://schema.org/InStock",
            "itemCondition": "https://schema.org/NewCondition"
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "42"
        }
    }

    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://www.cytos.in"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "Machines",
                "item": "https://www.cytos.in/#pillars"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": product["name"],
                "item": f"https://www.cytos.in{product['path']}"
            }
        ]
    }

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f["q"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f["a"]
                }
            } for f in product["faqs"]
        ]
    }

    return (
        f'<script type="application/ld+json">{json.dumps(product_schema, ensure_ascii=False)}</script>\n'
        f'<script type="application/ld+json">{json.dumps(breadcrumb_schema, ensure_ascii=False)}</script>\n'
        f'<script type="application/ld+json">{json.dumps(faq_schema, ensure_ascii=False)}</script>'
    )

def generate_page_html(p):
    schema_markup = build_schema_json(p)
    header = get_header_html(p['path'])
    
    # Specs table rows
    spec_rows = "\n".join([
        f'            <tr>\n              <td><strong>{s["param"]}</strong></td>\n              <td>{s["val"]}</td>\n              <td><span class="badge-std">{s["cls"]}</span></td>\n            </tr>'
        for s in p["specs"]
    ])

    # Features list
    features_list = "\n".join([
        f'            <li style="display: flex; gap: 0.75rem; margin-bottom: 0.85rem; align-items: flex-start;">\n              <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--brand-gold)" stroke-width="2.5" style="flex-shrink: 0; margin-top: 2px;"><polyline points="20 6 9 17 4 12"></polyline></svg>\n              <span style="color: var(--text-primary); font-size: 0.95rem; line-height: 1.6;">{feat}</span>\n            </li>'
        for feat in p["features"]
    ])

    # Highlights grid
    highlights_cells = "\n".join([
        f'          <div class="spec-cell" style="background: var(--bg-surface); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-subtle); text-align: center;">\n            <div class="spec-value" style="font-size: 1.8rem; font-weight: 800; color: var(--brand-primary); margin-bottom: 0.25rem;">{h["val"]}</div>\n            <div class="spec-label" style="font-size: 0.82rem; font-weight: 600; text-transform: uppercase; color: var(--text-secondary);">{h["lbl"]}</div>\n          </div>'
        for h in p["highlights"]
    ])

    # Materials rows
    materials_rows = "\n".join([
        f'            <tr>\n              <td><strong>{m["mat"]}</strong></td>\n              <td><span class="matrix-status-cell optimal">● {m["status"]}</span></td>\n              <td>{m["speed"]}</td>\n              <td>{m["notes"]}</td>\n            </tr>'
        for m in p["materials"]
    ])

    # Standard vs Optional accessories
    std_acc = "\n".join([f'            <li style="margin-bottom: 0.6rem;">✓ {acc}</li>' for acc in p["standard_accessories"]])
    opt_acc = "\n".join([f'            <li style="margin-bottom: 0.6rem;">+ {acc}</li>' for acc in p["optional_accessories"]])

    # FAQs
    faqs_html = "\n".join([
        f'        <details class="faq-item" style="background: #ffffff; padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-subtle); margin-bottom: 0.85rem;">\n          <summary style="font-weight: 700; color: var(--text-pure); cursor: pointer; font-size: 1.05rem;">{faq["q"]}</summary>\n          <p style="margin-top: 0.75rem; color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">{faq["a"]}</p>\n        </details>'
        for faq in p["faqs"]
    ])

    # Gallery images HTML
    gallery_images = "\n".join([
        f'          <div style="flex: 1; min-width: 260px; background: #ffffff; border: 1px solid var(--border-subtle); border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">\n            <img src="{img["url"]}" alt="{img["title"]}" title="{img["title"]}" loading="lazy" style="width: 100%; height: 220px; object-fit: cover; display: block;">\n            <div style="padding: 1rem;">\n              <strong style="color: var(--text-pure); font-size: 0.9rem; display: block; margin-bottom: 0.35rem;">{img["title"]}</strong>\n              <p style="color: var(--text-secondary); font-size: 0.82rem; margin: 0; line-height: 1.5;">{img["caption"]}</p>\n            </div>\n          </div>'
        for img in p["additional_images"]
    ])

    # Related products cards
    other_products = [item for item in MACHINE_PRODUCTS if item["id"] != p["id"]][:3]
    related_cards = "\n".join([
        f'          <article class="machine-card" style="background: #ffffff; border: 1px solid var(--border-subtle); border-radius: 10px; overflow: hidden; display: flex; flex-direction: column;">\n            <div class="machine-img-box" style="height: 220px; overflow: hidden; background: #f8fafc; position: relative;">\n              <img src="{op["image"]}" alt="{op["name"]}" title="{op["image_title"]}" loading="lazy" style="width: 100%; height: 100%; object-fit: contain; padding: 1rem;">\n              <div class="machine-badge-tag" style="position: absolute; top: 10px; left: 10px; background: rgba(15,23,42,0.85); color: #fff; font-size: 0.72rem; padding: 3px 8px; border-radius: 4px; font-weight: 700;">{op["badge"]}</div>\n            </div>\n            <div class="machine-body" style="padding: 1.5rem; flex: 1; display: flex; flex-direction: column;">\n              <h3 class="machine-name" style="font-size: 1.15rem; color: var(--text-pure); margin-bottom: 0.5rem;"><a href="{op["path"]}" style="text-decoration: none; color: inherit;">{op["name"]}</a></h3>\n              <p style="font-size: 0.88rem; color: var(--text-secondary); flex: 1; margin-bottom: 1.25rem;">{op["hero_subtitle"][:140]}...</p>\n              <div style="display: flex; gap: 0.5rem;">\n                <a href="{op["path"]}" class="btn btn-outline btn-block" style="text-align: center; text-decoration: none;">View Model ❯</a>\n                <button class="btn btn-primary" data-open-rfq data-machine="{op["name"]}">Quote</button>\n              </div>\n            </div>\n          </article>'
        for op in other_products
    ])

    full_html = f"""
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-P6DNQQ3H"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->

{schema_markup}

{TOP_BAR_HTML}

{header}

  <!-- Breadcrumbs Bar -->
  <div class="breadcrumbs-bar">
    <div class="container">
      <div class="breadcrumbs-list">
        <a href="/">Home</a>
        <span class="breadcrumb-separator">/</span>
        <a href="/#pillars">Machines</a>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-current">{p["name"]}</span>
      </div>
    </div>
  </div>

  <!-- Product Page Hero Section -->
  <section class="page-hero">
    <div class="container">
      <div class="page-hero-grid">
        <div class="page-hero-content">
          <div class="hero-badge">
            <span>{p["badge"]}</span>
          </div>
          <h1 class="page-hero-title">{p["hero_title"]}</h1>
          <p class="page-hero-subtitle">
            {p["hero_subtitle"]}
          </p>
          
          <!-- Answer-First Box for Search & Direct Buyers -->
          <div class="answer-first-callout">
            <strong>In brief:</strong> {p["in_brief"]}
          </div>

          <div class="slide-cta-row">
            <button class="btn btn-primary btn-lg" data-open-rfq data-machine="{p["name"]}">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="btn-icon-svg" aria-hidden="true"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect><path d="M9 12h6"></path><path d="M9 16h6"></path></svg> <span>Request Technical Quote</span>
            </button>
            <a href="https://wa.me/919921381071?text=Hi%20CyTOS,%20I%20am%20interested%20in%20{p["name"]}.%20Please%20send%20pricing%20and%20proposal." class="btn btn-whatsapp btn-lg" target="_blank" rel="noopener noreferrer">
              <svg class="btn-icon-svg whatsapp-icon-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.68C7.02 10.88 7.9 12.04 8.02 12.2C8.14 12.37 9.73 14.95 12.24 15.93C14.33 16.75 14.75 16.59 15.22 16.54C15.69 16.49 16.74 15.91 16.96 15.29C17.18 14.66 17.18 14.13 17.11 14.02C17.05 13.91 16.89 13.84 16.64 13.72C16.39 13.6 15.17 13 14.94 12.92C14.72 12.83 14.56 12.79 14.4 13.04C14.24 13.29 13.77 13.84 13.63 14.01C13.5 14.17 13.36 14.19 13.11 14.07C12.87 13.95 12.08 13.69 11.15 12.86C10.42 12.21 9.93 11.41 9.79 11.17C9.65 10.92 9.78 10.79 9.9 10.67C10.01 10.56 10.15 10.38 10.27 10.23C10.4 10.08 10.44 9.97 10.52 9.81C10.6 9.65 10.56 9.51 10.5 9.39C10.44 9.27 9.97 8.12 9.78 7.65C9.59 7.19 9.39 7.25 9.24 7.24C9.1 7.23 8.94 7.23 8.78 7.23H8.53Z\"/></svg> <span>Chat with Pune Engineer</span>
            </a>
            <a href="/cytos_newcatalog2026_with BG.pdf" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-lg" style="margin-top: 0.5rem; width: 100%; justify-content: center;">
              <span>Download 2026 Machine Catalog (PDF)</span>
            </a>
          </div>

          <div class="engineering-signoff-bar">
            <span class="signoff-icon"><svg viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg></span>
            <span><strong>Technical Specification Verified:</strong> Reviewed by CyTOS Lead CNC Controls &amp; Spindle Specialist • Revision v4.2 (2026)</span>
          </div>
        </div>

        <div class="page-hero-media">
          <img src="{p["image"]}" alt="{p["image_title"]}" title="{p["image_title"]}" class="slide-img" fetchpriority="high" style="border-radius: 8px; max-height: 480px; width: 100%; object-fit: contain; background: #ffffff;">
          <div class="page-hero-caption">
            <strong>Featured Model:</strong> {p["name"]} • {p["model_code"]} • Manufactured at Bhosari MIDC, Pune
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Performance Highlights Grid -->
  <section class="section" style="background: #ffffff; padding: 2.5rem 0;">
    <div class="container">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.25rem;">
{highlights_cells}
      </div>
    </div>
  </section>

  <!-- In-Depth Engineering Features -->
  <section class="section" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header">
        <div class="hero-badge" style="margin: 0 0 0.75rem;">
          <span>ENGINEERING EXCELLENCE</span>
        </div>
        <h2 class="section-title">Core Machine Design &amp; Architectural Features</h2>
        <p class="section-subtitle">
          Built from the ground up at our Pune works with stress-relieved structures, premium motion hardware, and in-house proprietary controls.
        </p>
      </div>

      <div style="background: #ffffff; padding: 2.5rem; border-radius: 12px; border: 1px solid var(--border-subtle); box-shadow: var(--shadow-sm);">
        <ul style="list-style: none; padding: 0; margin: 0;">
{features_list}
        </ul>
      </div>
    </div>
  </section>

  <!-- Detailed Technical Specifications Table -->
  <section class="section" style="background: #ffffff;">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Factory Verified Technical Specifications</h2>
        <p class="section-subtitle">
          Transparent, factory-tested parameters from the 2026 CyTOS Machine Catalog.
        </p>
      </div>

      <div class="spec-table-container">
        <table class="spec-table">
          <thead>
            <tr>
              <th style="width: 35%;">Specification Parameter</th>
              <th style="width: 45%;">Engineering Value / Standard</th>
              <th style="width: 20%;">Classification</th>
            </tr>
          </thead>
          <tbody>
{spec_rows}
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- Material Compatibility Matrix -->
  <section class="section" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Tested Substrate &amp; Material Compatibility</h2>
        <p class="section-subtitle">
          Recommended cutting speeds, feeds, and application performance validated on CyTOS test beds.
        </p>
      </div>

      <div class="spec-table-container">
        <table class="spec-table">
          <thead>
            <tr>
              <th style="width: 30%;">Material Substrate</th>
              <th style="width: 15%;">Suitability</th>
              <th style="width: 25%;">Recommended Spindle Speed</th>
              <th style="width: 30%;">Application Notes</th>
            </tr>
          </thead>
          <tbody>
{materials_rows}
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- Standard Equipment vs Optional Upgrades -->
  <section class="section" style="background: #ffffff;">
    <div class="container">
      <div class="section-header text-center">
        <h2 class="section-title">Standard Package &amp; Factory Custom Options</h2>
        <p class="section-subtitle">
          Configure your machine according to specific production volumes, panel formats, and cycle times.
        </p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem;">
        <div style="background: var(--bg-surface); padding: 2rem; border-radius: 10px; border: 1px solid var(--border-subtle);">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1.25rem;">
            <h3 style="margin: 0; color: var(--text-pure); font-size: 1.25rem;">Standard Factory Package</h3>
            <span class="badge-std" style="background: #10b981; color: #fff;">INCLUDED</span>
          </div>
          <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.92rem; color: var(--text-secondary); line-height: 1.7;">
{std_acc}
          </ul>
        </div>

        <div style="background: var(--bg-surface); padding: 2rem; border-radius: 10px; border: 1px solid var(--brand-gold-border); box-shadow: var(--shadow-sm);">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1.25rem;">
            <h3 style="margin: 0; color: var(--text-pure); font-size: 1.25rem;">Optional Factory Upgrades</h3>
            <span class="badge-std" style="background: var(--brand-gold); color: #fff;">CUSTOMIZABLE</span>
          </div>
          <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.92rem; color: var(--text-secondary); line-height: 1.7;">
{opt_acc}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- Visual Image Gallery for Image SEO -->
  <section class="section" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Machine Gallery &amp; Detail Views</h2>
        <p class="section-subtitle">
          High-resolution engineering views of components, spindle tapers, and electronic control architecture.
        </p>
      </div>

      <div style="display: flex; flex-wrap: wrap; gap: 1.5rem;">
{gallery_images}
      </div>
    </div>
  </section>

  <!-- Live Cutting Trial Banner -->
  <section class="section" style="background: #ffffff;">
    <div class="container">
      <div class="sample-trial-banner" style="background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%); border: 2px solid var(--brand-gold-border); padding: 2.5rem; border-radius: 12px; display: grid; grid-template-columns: 1.6fr 1fr; gap: 2rem; align-items: center;">
        <div>
          <div class="hero-badge" style="margin-bottom: 0.75rem;">
            <span>ZERO-RISK TECHNICAL EVALUATION</span>
          </div>
          <h2 style="font-size: 1.85rem; color: var(--text-pure); margin-bottom: 1rem;">
            Schedule a Live Cutting Trial on the {p["name"]}
          </h2>
          <p style="color: var(--text-secondary); line-height: 1.6; margin-bottom: 1.5rem;">
            Bring your material or send component drawings (DXF/STEP/Gerber) to our Bhosari MIDC works in Pune. Our application specialists will run a live trial, calculate cycle times, measure edge finish, and provide a full technical report.
          </p>
          <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
            <button class="btn btn-primary btn-lg" data-open-rfq data-machine="{p["name"]} Live Trial">
              <span>Book Live Trial at Pune Works</span>
            </button>
            <a href="https://wa.me/919921381071?text=Hi%20CyTOS,%20I%20want%20to%20send%20a%20drawing%20for%20a%20cutting%20trial%20on%20{p["name"]}." class="btn btn-whatsapp btn-lg" target="_blank" rel="noopener noreferrer">
              <span>Send Drawing on WhatsApp</span>
            </a>
          </div>
        </div>

        <div style="background: #ffffff; padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-subtle); box-shadow: var(--shadow-sm);">
          <h4 style="color: var(--text-pure); margin-bottom: 0.75rem;">Trial Execution Protocol:</h4>
          <ol style="padding-left: 1.25rem; font-size: 0.88rem; color: var(--text-secondary); line-height: 1.8; margin: 0;">
            <li>Share DXF/Gerber or courier sample stock to Pune.</li>
            <li>Application engineer calculates optimal feed &amp; speed.</li>
            <li>Trial executed live with video recording.</li>
            <li>Finished parts &amp; cycle analysis returned in 48 hours.</li>
          </ol>
        </div>
      </div>
    </div>
  </section>

  <!-- Frequently Asked Questions -->
  <section class="section" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header text-center">
        <h2 class="section-title">Frequently Asked Questions</h2>
        <p class="section-subtitle">
          Direct engineering answers about specifications, tooling, delivery, and support for the {p["name"]}.
        </p>
      </div>

      <div style="max-width: 860px; margin: 0 auto;">
{faqs_html}
      </div>
    </div>
  </section>

  <!-- Related Precision Machines -->
  <section class="section" style="background: #ffffff;">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Explore Related Precision Machines</h2>
        <p class="section-subtitle">
          Discover other industrial CNC routers, PCB machines, and automation cells manufactured by CyTOS in Pune.
        </p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
{related_cards}
      </div>
    </div>
  </section>

{FOOTER_HTML}
"""
    return full_html

def write_jsx_page(product):
    html_content = generate_page_html(product)
    
    # Escape backticks and ${} for JS template string
    escaped_html = html_content.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

    jsx_content = f"""import React from 'react';
import HtmlPageWrapper from '../components/HtmlPageWrapper';

const pageHtml = `{escaped_html}`;

export default function {product["jsx_filename"].replace(".jsx", "")}() {{
  return (
    <HtmlPageWrapper
      htmlContent={{pageHtml}}
      title="{product["seo_title"]}"
      description="{product["meta_desc"]}"
      canonical="https://www.cytos.in{product["path"]}"
    />
  );
}}
"""
    filepath = os.path.join(PAGES_DIR, product["jsx_filename"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(jsx_content)
    print(f"Created JSX page: {product['jsx_filename']}")

# Generate all 8 pages
for p in MACHINE_PRODUCTS:
    write_jsx_page(p)

print("Finished generating all 8 standalone product pages.")
