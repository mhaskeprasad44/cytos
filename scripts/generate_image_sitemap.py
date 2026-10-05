import datetime

date_str = "2026-10-05"

urls = [
    # 1. Homepage
    {
        "loc": "https://www.cytos.in/",
        "lastmod": date_str,
        "changefreq": "daily",
        "priority": "1.0",
        "images": [
            {
                "loc": "https://www.cytos.in/CyTOS%20New%20Logo.png",
                "title": "CyTOS Machines Pune - Precision CNC and Industrial Automation",
                "caption": "CyTOS - Cycle Time Optimising Solutions manufacturer logo"
            },
            {
                "loc": "https://www.cytos.in/assets/images/machines/pcb-drilling-pcb60.png",
                "title": "CyTOS PCB60 Dual-Spindle High Speed PCB Drilling Machine",
                "caption": "CyTOS PCB60 60,000 RPM dual spindle PCB drilling and routing machine in Pune"
            },
            {
                "loc": "https://www.cytos.in/assets/images/machines/pcb-prototyping-pcb30.png",
                "title": "CyTOS PCB30 Chemical-Free PCB Prototyping Machine",
                "caption": "Desktop chemical-free laboratory PCB rapid prototyping CNC machine"
            },
            {
                "loc": "https://www.cytos.in/assets/images/machines/cnc-router-gantry.png",
                "title": "CyTOS Heavy Duty Industrial Gantry CNC Router",
                "caption": "Precision industrial CNC router for aluminium, acrylic, composites and wood"
            }
        ]
    },

    # 2. Dedicated Product Pages (New Machine Showcase Pages)
    {
        "loc": "https://www.cytos.in/cnc-6060-pcb-drilling-routing-machine",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.95",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/pcb-drilling-pcb60.png",
                "title": "CNC 6060 PCB Drilling & Routing Machine - 60,000 to 100,000 RPM Spindle",
                "caption": "CyTOS CNC 6060 high-speed PCB drilling and routing machine manufactured in Pune with 600x600mm work area and 0.2mm micro-drilling precision"
            },
            {
                "loc": "https://www.cytos.in/assets/images/machines/pcb-cnc-cabinet.png",
                "title": "CNC 6060 Integrated Control Console and Servo Drives",
                "caption": "Industrial PC control console and hybrid closed-loop servo drives for CyTOS CNC 6060"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/cnc-3020-pcb-prototyping-machine",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.95",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/pcb-prototyping-pcb30.png",
                "title": "CNC 3020 PCB Rapid Prototyping Machine - Chemical Free Desktop Mill",
                "caption": "CyTOS CNC 3020 desktop chemical-free circuit board rapid prototyping machine with auto Z-leveling and 0.1mm isolation tracks"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/cnc-3030-pcb-prototyping-machine",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.95",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/pcb-prototyping-pcb30.png",
                "title": "CNC 3030 PCB Rapid Prototyping Machine - 40,000 RPM Lab Prototyper",
                "caption": "CyTOS CNC 3030 laboratory PCB rapid prototyping machine with 40,000 RPM spindle and direct Gerber RS-274X import"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/pcb12-multi-spindle-drilling-machine",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.95",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/pcb12-multi-spindle.png",
                "title": "PCB12 Multi-Spindle PCB Drilling Machine - 3 Spindles 60,000 RPM",
                "caption": "CyTOS PCB12 heavy-duty 3-spindle synchronized PCB drilling machine for commercial PCB manufacturing plants"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/cnc-wood-acrylic-aluminium-router-machine",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.95",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/cnc-router-gantry.png",
                "title": "CNC Wood, Acrylic & Aluminium Router Machine - Heavy Duty Gantry",
                "caption": "Industrial CNC router machine for non-ferrous metals, acrylic, composites and wood with vacuum hold-down bed"
            },
            {
                "loc": "https://www.cytos.in/assets/images/machines/cnc-router-workshop.png",
                "title": "CyTOS Heavy Duty CNC Gantry Welding and Stress Relieving",
                "caption": "Welded tubular steel gantry engineered to Safety Factor 2.0 at CyTOS Bhosari MIDC Pune plant"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/vdm-heavy-vertical-drilling-milling-machine",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.95",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/vdm-milling-machine.png",
                "title": "VDM Heavy Vertical Drilling & Milling Machine - Multi-Spindle SPM",
                "caption": "CyTOS VDM multi-spindle rigid vertical drilling and milling machine for switchboard door cutouts and busbars"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/foam-welding-machine",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.95",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/foam-welding-machine.png",
                "title": "Industrial Foam Welding Machine - Hot Air Thermal Welder",
                "caption": "Automated hot-air thermal bonding and welding machine for acoustic foam and protective packaging"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/educational-cnc-machines",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.95",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/educational-cnc-lab.png",
                "title": "Educational CNC Machines - Lab Lathe, Milling & Training Systems",
                "caption": "Fully enclosed safe industrial-grade CNC training lathe and milling machines for engineering universities"
            }
        ]
    },

    # 3. Category & Core Solution Pages
    {
        "loc": "https://www.cytos.in/pcb-drilling-routing",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.90",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/pcb-drilling-pcb60.png",
                "title": "High Speed CNC PCB Drilling & Routing Machines",
                "caption": "CyTOS PCB drilling machines engineered for 24/7 high volume production with 60,000 RPM spindles"
            },
            {
                "loc": "https://www.cytos.in/assets/images/machines/pcb12-multi-spindle.png",
                "title": "Multi-Spindle PCB Drilling Systems",
                "caption": "3-spindle synchronized drilling for commercial panel production"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/pcb-prototyping",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.90",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/pcb-prototyping-pcb30.png",
                "title": "Chemical-Free PCB Rapid Prototyping Systems",
                "caption": "In-house green R&D laboratory circuit board isolation milling CNC systems"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/cnc-routers-milling",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.90",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/cnc-router-gantry.png",
                "title": "Industrial CNC Routers & Gantry Milling Machines",
                "caption": "Heavy duty gantry CNC routers for non-ferrous metals and industrial composite sheets"
            },
            {
                "loc": "https://www.cytos.in/assets/images/machines/cnc-router-acrylic.jpg",
                "title": "High Precision CNC Acrylic and Aluminium Routing",
                "caption": "Vibration-damped rigid steel gantry with high-torque liquid cooled spindle"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/vdm-milling",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.90",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/vdm-milling-machine.png",
                "title": "VDM Series Multi-Spindle Vertical Milling & Drilling",
                "caption": "Multi-spindle rigid milling for electrical switchboard plates and busbar fabrication"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/spm-automation",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.90",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/spm-automation-cell.jpg",
                "title": "Custom Turnkey Special Purpose Machines (SPM)",
                "caption": "Turnkey SPM automation cells designed to reduce manufacturing cycle times by 30% to 60%"
            },
            {
                "loc": "https://www.cytos.in/assets/images/machines/spm-pneumatic-fixture.jpg",
                "title": "Automotive Pneumatic Welding Jigs and Fixtures",
                "caption": "90 degree rotary indexing turnover fixture for robotic welding lines"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/robotic-dispensing-cells",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.85",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/spm-automation-cell.jpg",
                "title": "Robotic Dispensing Cells - 3-Axis Cartesian Automation",
                "caption": "High-speed automated dispensing systems for RTV silicone, sealants, and potting adhesives"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/pneumatic-welding-fixtures",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.85",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/spm-pneumatic-fixture.jpg",
                "title": "Pneumatic Welding Fixtures & 90° Rotary Indexing Jigs",
                "caption": "Heavy clamping jigs and positioners engineered for zero thermal distortion in Pune"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/plc-control-panels",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.85",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/industrial-control-panel.jpg",
                "title": "Industrial PLC Automation Control Panels",
                "caption": "Siemens S7-1200, Mitsubishi, and Delta PLC control panel enclosures with HMI touchscreens"
            }
        ]
    },

    # 4. Applications, Case Studies & Institutional Pages
    {
        "loc": "https://www.cytos.in/case-studies",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.85",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/precision-machining-parts.jpg",
                "title": "CyTOS Engineering Case Studies and Customer Results",
                "caption": "Cycle time optimization, multi-spindle throughput gains, and robotic welding fixture deployment proof"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/applications",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.85",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/precision-machining-parts.png",
                "title": "Industrial Applications of CyTOS CNC & Automation Machinery",
                "caption": "Precision parts machined for electronics, automotive tier-1, switchgear, aerospace and medical devices"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/about",
        "lastmod": date_str,
        "changefreq": "monthly",
        "priority": "0.80",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/cytos-pune-plant.jpg",
                "title": "CyTOS Manufacturing Plant in Bhosari MIDC, Pune",
                "caption": "Modern 3,000 sq ft CNC machine tool fabrication and assembly facility in Pune, Maharashtra"
            },
            {
                "loc": "https://www.cytos.in/assets/images/machines/cytos-assembly-floor.png",
                "title": "CyTOS Clean Assembly Floor and CNC Calibration Bay",
                "caption": "Precision laser alignment and granite metrology validation on CyTOS assembly floor"
            },
            {
                "loc": "https://www.cytos.in/assets/images/machines/cytos-testing-station.png",
                "title": "72-Hour Continuous Burn-in Testing Station",
                "caption": "Machine endurance and dynamic runout testing before nationwide dispatch"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/blog",
        "lastmod": date_str,
        "changefreq": "daily",
        "priority": "0.90",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/cytos-engineering-cad.png",
                "title": "CyTOS Engineering Blog and Technical Insights",
                "caption": "Technical guides on PCB drilling, chemical-free prototyping, heavy CNC routing, and custom SPMs"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/contact",
        "lastmod": date_str,
        "changefreq": "monthly",
        "priority": "0.85",
        "images": [
            {
                "loc": "https://www.cytos.in/assets/images/machines/cytos-facility-overview.png",
                "title": "Contact CyTOS Pune - Machine Consultation & Plant Visit",
                "caption": "J-153, MIDC Bhosari, Pune - application engineers and live machine demonstrations"
            }
        ]
    },
    {
        "loc": "https://www.cytos.in/terms-conditions",
        "lastmod": date_str,
        "changefreq": "yearly",
        "priority": "0.50",
        "images": []
    },
    {
        "loc": "https://www.cytos.in/privacy-policy",
        "lastmod": date_str,
        "changefreq": "yearly",
        "priority": "0.50",
        "images": []
    }
]

# 5. Technical Blog Posts (22 articles)
blog_slugs = [
    ("pcb-drilling-machine-guide", "PCB Drilling Machine Complete Engineering Guide", "pcb-drilling-pcb60.png", "Guide to high speed PCB drilling machines, spindles, feeds and speeds"),
    ("multi-spindle-pcb-drilling-machine", "Multi-Spindle PCB Drilling Machines Throughput Analysis", "pcb12-multi-spindle.png", "Scaling commercial PCB panel drilling with 2 and 3 synchronized spindles"),
    ("mechanical-pcb-drilling-vs-laser-drilling", "Mechanical PCB Drilling vs Laser Drilling Comparison", "pcb-drilling-pcb60.png", "Hole-wall quality, micro-via accuracy, thermal smear and ROI comparison"),
    ("pcb-drilling-tool-breakage-prevention", "PCB Drilling Micro-Tool Breakage Prevention Guide", "cnc-tooling-system.png", "Preventing 0.2mm carbide micro-drill bit breakage in high-speed spindles"),
    ("60000-rpm-pcb-drilling-spindle-maintenance", "60,000 RPM PCB Drilling Spindle Maintenance Guide", "pcb-drilling-pcb60.png", "Ceramic bearing maintenance, chiller fluid, and dynamic runout calibration"),
    ("multilayer-fr4-rogers-pcb-drilling", "Multilayer FR4 and Rogers High-Frequency PCB Drilling", "pcb-drilling-pcb60.png", "Drilling high-frequency PTFE, Rogers RF, and metal core laminates"),
    ("chemical-free-pcb-rapid-prototyping-machine", "Chemical-Free PCB Rapid Prototyping Machine Guide", "pcb-prototyping-pcb30.png", "Mechanical circuit board isolation milling without etching acids"),
    ("in-house-pcb-rapid-prototyping-roi", "In-House PCB Rapid Prototyping ROI and Payback Analysis", "pcb-prototyping-pcb30.png", "Financial ROI model comparing outsourced prototype fab vs same-day in-house milling"),
    ("gerber-to-pcb-isolation-milling-guide", "Gerber to PCB Isolation Milling CAM Software Guide", "pcb-prototyping-pcb30.png", "Direct RS-274X Gerber file ingestion, rubout algorithms, and tool compensation"),
    ("auto-surface-leveling-pcb-prototyping", "Auto-Surface Leveling in PCB Prototyping CNC Machines", "pcb-prototyping-pcb30.png", "Capacitive surface height matrix leveling for perfectly uniform trace depth"),
    ("green-electronics-rapid-prototyping-lab", "Setting Up a Green Electronics Rapid Prototyping Lab", "educational-cnc-lab.png", "Zero-chemical electronics R&D infrastructure with HEPA dust extraction"),
    ("double-sided-pcb-rapid-prototyping-guide", "Double-Sided PCB Rapid Prototyping Step-by-Step", "pcb-prototyping-pcb30.png", "Dowel pin registration, layer flipping, through-hole eyeletting, and ground clearance"),
    ("special-purpose-machines-spm-guide", "Turnkey Special Purpose Machines (SPM) Engineering Guide", "spm-automation-cell.jpg", "Concept-to-commissioning architecture for custom industrial automation"),
    ("pneumatic-welding-fixtures-spm-design", "Pneumatic Welding Fixture Design and Toggle Clamping", "spm-pneumatic-fixture.jpg", "90-degree rotary turnover welding jigs and thermal distortion control"),
    ("robotic-adhesive-dispensing-spm-systems", "Robotic Adhesive Dispensing SPM Systems", "spm-automation-cell.jpg", "Progressive cavity pumps and 3-axis path control for sealant bead accuracy"),
    ("plc-control-panel-automation-spm-safety", "PLC Control Panel Automation and Machine Safety Standards", "industrial-control-panel.jpg", "Category 4 emergency stops, optical light curtains, and IEC 61439 panels"),
    ("automotive-cycle-time-reduction-spm", "Automotive Cycle Time Reduction SPM Case Study", "spm-automation-cell.jpg", "60% cycle time reduction on tier-1 robotic automotive component welding lines"),
    ("cnc-drilling-and-milling-machine-guide", "Heavy Duty CNC Drilling and Milling Machine Guide", "cnc-milling-detail.png", "Cast iron gantry rigidity, preloaded linear rails, and high-feed metal milling"),
    ("vertical-drilling-and-milling-machine-guide", "Vertical Drilling & Milling (VDM) Machines for Switchboards", "vdm-milling-machine.png", "Switchgear door cutouts, rectangular meter cutouts, and busbar multi-drilling"),
    ("bt30-vs-bt40-cnc-drilling-and-milling", "BT30 vs BT40 Spindle Taper Comparison for Drilling & Milling", "cnc-tooling-system.png", "High-RPM light alloy milling vs high-torque face milling rigidity trade-offs"),
    ("heavy-duty-cnc-router-machine-guide", "Heavy Duty Industrial CNC Router Machine Guide", "cnc-router-gantry.png", "Stress-relieved steel gantry, 24,000 RPM spindle, and multi-zone vacuum bed engineering"),
    ("aluminium-composite-sheet-cnc-drilling-milling", "Aluminium & Composite Sheet CNC Drilling and Milling Guide", "cnc-router-acrylic.jpg", "Single-flute polished carbide tool geometry, cold air cooling, and burr-free edges")
]

for slug, title, img, caption in blog_slugs:
    urls.append({
        "loc": f"https://www.cytos.in/blog/{slug}",
        "lastmod": date_str,
        "changefreq": "weekly",
        "priority": "0.85",
        "images": [
            {
                "loc": f"https://www.cytos.in/assets/images/machines/{img}",
                "title": title,
                "caption": caption
            }
        ]
    })

lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
    '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">'
]

for u in urls:
    lines.append('  <url>')
    lines.append(f'    <loc>{u["loc"]}</loc>')
    lines.append(f'    <lastmod>{u["lastmod"]}</lastmod>')
    lines.append(f'    <changefreq>{u["changefreq"]}</changefreq>')
    lines.append(f'    <priority>{u["priority"]}</priority>')
    for img in u.get("images", []):
        lines.append('    <image:image>')
        lines.append(f'      <image:loc>{img["loc"]}</image:loc>')
        # Escape any ampersands or special characters
        safe_title = img["title"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        safe_caption = img["caption"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        lines.append(f'      <image:title>{safe_title}</image:title>')
        lines.append(f'      <image:caption>{safe_caption}</image:caption>')
        lines.append('    </image:image>')
    lines.append('  </url>')

lines.append('</urlset>')
lines.append('')

output_content = '\n'.join(lines)

with open(r"c:\Users\PrasadMhaske\Downloads\Project1\public\sitemap.xml", "w", encoding="utf-8") as f:
    f.write(output_content)

print(f"Generated sitemap with {len(urls)} URLs and rich Google Image SEO tags!")
