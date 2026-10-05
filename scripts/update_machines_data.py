# -*- coding: utf-8 -*-
"""
scripts/update_machines_data.py
Updates src/data/machinesData.js with comprehensive details for all 12 machines/categories.
"""

import os

ROOT = r"c:\Users\PrasadMhaske\Downloads\Project1"
MACHINES_DATA_FILE = os.path.join(ROOT, "src", "data", "machinesData.js")

machines_data_js = """export const machinesData = [
  {
    id: "cnc-6060",
    path: "/cnc-6060-pcb-drilling-routing-machine",
    name: "CNC 6060 PCB Drilling & Routing Machine",
    category: "PCB Drilling & Routing",
    tagline: "Industrial PCB Drilling & Routing Machine up to 100,000 RPM",
    image: "/assets/images/machines/pcb-drilling-pcb60.png",
    badge: "100k RPM Ultra Speed",
    spindle: "1.2 kW - 4.5 kW High Frequency",
    rpm: "18,000 - 100,000 RPM",
    bedSize: "600 x 600 x 100 mm",
    materials: "Multilayer FR4, CEM-1, CEM-3, MCPCB, Rogers, PTFE",
    accuracy: "0.05 mm (±0.03 mm Repeatability)",
    description: "Floor-mounted industrial machine engineered for continuous PCB production. Features 1 to 5 synchronized spindles, 0.2mm micro-drilling, pneumatic ATC, and vacuum hold-down.",
    specs: [
      { label: "Working Area", val: "X: 600 mm × Y: 600 mm × Z: 100 mm" },
      { label: "Spindle Speed", val: "18,000 to 100,000 RPM Continuous Inverter" },
      { label: "Spindle Power", val: "1.2 kW to 4.5 kW Electro-Spindle" },
      { label: "Number of Spindles", val: "1 to 5 Synchronized Heads" },
      { label: "Drill Diameter Range", val: "0.2 mm to 3.0 mm Carbide Drills" },
      { label: "Routing Diameter", val: "1.0 mm to 4.0 mm End Mills" },
      { label: "Travel Speed", val: "6,000 to 15,000 mm/min" },
      { label: "Positional Accuracy", val: "0.05 mm / 600 mm" },
      { label: "Work Clamping", val: "Dowel Pin Fixture / T-Slot Bed + Vacuum" }
    ],
    features: [
      "Rigid welded structural steel tubular frame normalized against internal stresses",
      "Ultra-high-speed ceramic hybrid bearing spindle with dynamic runout under 3 microns",
      "Multi-spindle synchronous motion for 2X to 5X throughput scaling",
      "Dynamic auto-leveling surface height compensation for warped panels",
      "Native Excellon drill (.drl) and Gerber RS-274X (.gbr) file execution"
    ]
  },
  {
    id: "cnc-3020",
    path: "/cnc-3020-pcb-prototyping-machine",
    name: "CNC 3020 PCB Rapid Prototyping Machine",
    category: "PCB Prototyping & R&D",
    tagline: "Chemical-Free Tabletop PCB Isolation Milling & Prototyping",
    image: "/assets/images/machines/pcb-prototyping-pcb30.png",
    badge: "100% Chemical-Free",
    spindle: "0.8 kW - 1.2 kW Spindle Motor",
    rpm: "18,000 - 40,000 RPM",
    bedSize: "300 x 200 x 60 mm (A4 Format)",
    materials: "Single/Double Sided FR4, Rogers, Polyimide, Flex PCB",
    accuracy: "0.05 mm (0.1 mm Track/Gap)",
    description: "Compact desktop PCB rapid prototyper for colleges, defense labs, and corporate R&D. Complete with auto-leveling surface probing, camera alignment, and transparent safety enclosure.",
    specs: [
      { label: "Working Envelope", val: "X: 300 mm × Y: 200 mm × Z: 60 mm (A4 Format)" },
      { label: "Spindle Speed", val: "18,000 to 40,000 RPM Variable Inverter" },
      { label: "Min Track / Gap", val: "0.1 mm (4 mil) Isolation Width" },
      { label: "Drill Diameter", val: "0.4 mm to 3.0 mm Micro-Drill Bits" },
      { label: "Travel Speed", val: "Up to 6,000 mm/min Rapid Traverse" },
      { label: "Surface Leveling", val: "Automated Multi-Point Digital Height Matrix" },
      { label: "Camera Inspection", val: "Integrated USB Camera for Visual Alignment" },
      { label: "Safety Housing", val: "Transparent Interlocked Safety Enclosure" }
    ],
    features: [
      "Zero toxic wet chemistry — 100% dry mechanical isolation milling eliminates ferric chloride acid baths",
      "Auto surface height mapping dynamically interpolates Z-depth across board warpage",
      "High-resolution visual camera alignment ensures exact pad registration on double-sided boards",
      "Hardened dowel pin alignment block for easy top-to-bottom board registration",
      "Quiet operation under 65 dB, ideal for clean university laboratories and engineering classrooms"
    ]
  },
  {
    id: "cnc-3030",
    path: "/cnc-3030-pcb-prototyping-machine",
    name: "CNC 3030 High Precision PCB Drilling & Routing Machine",
    category: "High Speed PCB Prototyping",
    tagline: "Heavy Benchtop Precision Machine with 166 mm/sec Travel Speed",
    image: "/assets/images/machines/pcb-prototyping-pcb30.png",
    badge: "60,000 RPM Precision",
    spindle: "1.5 kW High-Frequency Water Cooled",
    rpm: "28,000 - 60,000 RPM",
    bedSize: "300 x 300 x 60 mm",
    materials: "FR4, Rogers, Aluminium Sheet, Brass, Acrylic, Polycarbonate",
    accuracy: "0.05 mm (±0.05 mm Repeatability)",
    description: "Heavy-duty 250 to 370 kg benchtop machining center for precision PCB routing, non-ferrous metal engraving, and fast pilot runs with closed-loop AC servos and pneumatic ATC.",
    specs: [
      { label: "Working Area", val: "X: 300 mm × Y: 300 mm × Z: 60 mm" },
      { label: "Spindle RPM", val: "Up to 60,000 RPM (1.5 kW Water Cooled)" },
      { label: "Travel Speed", val: "166 mm/sec (10,000 mm/min)" },
      { label: "Drive System", val: "Digital AC Servo / Easy Servo Motors" },
      { label: "Machine Weight", val: "250 kg to 370 kg Heavy Rigid Frame" },
      { label: "Tool Changer", val: "Pneumatic Button-Press Quick Clamp ATC" },
      { label: "Min Track Width", val: "0.3 mm Isolation Width" },
      { label: "Work Clamping", val: "Dowel Pin Reference Holes + T-Slot Bed" }
    ],
    features: [
      "Heavy vibration-absorbing steel frame weighing up to 370 kg for resonance-free high-speed cutting",
      "Closed-loop AC digital servo motors delivering rapid positioning with zero missed steps",
      "Pneumatic button-press collet release reduces cutter changeover time to under 3 seconds",
      "Integrated dust collection shroud and chip vacuum keeping linear bearings and scales clean",
      "Multi-material capability: machines double-sided FR4 as well as aluminium and brass faceplates"
    ]
  },
  {
    id: "pcb12",
    path: "/pcb12-multi-spindle-drilling-machine",
    name: "CyTOS PCB12 3-Spindle High Throughput PCB Machine",
    category: "Multi-Spindle PCB Manufacturing",
    tagline: "Large-Format 1200x1200mm 3-Spindle High Volume Production Gantry",
    image: "/assets/images/machines/pcb12-multi-spindle.png",
    badge: "3X Production Throughput",
    spindle: "3× High Frequency Spindles",
    rpm: "40,000 - 60,000 RPM per Spindle",
    bedSize: "1,200 x 1,200 mm",
    materials: "FR4, Multilayer Panels, CEM-1, Aluminium MCPCB, Industrial Comber Board",
    accuracy: "±0.015 mm over 1,200 mm (±0.008 mm Repeatability)",
    description: "Triple-spindle synchronized gantry machine designed for commercial PCB manufacturing plants. Drills three identical panels concurrently, slashing cycle times by 66%.",
    specs: [
      { label: "Working Envelope", val: "1,200 mm × 1,200 mm Large Format Gantry" },
      { label: "Spindle Count", val: "3 Synchronized Spindles with Independent Pitch" },
      { label: "Spindle Speed", val: "40,000 to 60,000 RPM Continuous Inverter" },
      { label: "Combined Hit Rate", val: "Up to 480 hits/min (3 × 160 hits/min)" },
      { label: "Min Drill Dia", val: "0.25 mm Micro-Hole Drilling" },
      { label: "Traverse Speed", val: "Up to 15,000 mm/min High Speed Axis Motion" },
      { label: "Drive Hardware", val: "Delta High-Torque AC Servos + C5 Ground Ball Screws" },
      { label: "Vision System", val: "Multi-Camera CCD Fiducial Vision Alignment" },
      { label: "Work Clamping", val: "High-Pressure Multi-Zone Vacuum Table" }
    ],
    features: [
      "Triple synchronized spindles cut batch processing time by 66% compared to single-head machines",
      "Independent Z-axis depth adjustment ensures identical hole wall quality across all 3 stations",
      "Multi-camera optical fiducial recognition corrects for panel skew, stretch, and shrinkage",
      "Heavy cast iron / normalized structural steel gantry dampens all high-frequency vibrations",
      "Continuous-duty chilled spindle array designed for non-stop 24/7 manufacturing operations"
    ]
  },
  {
    id: "cnc-routers",
    path: "/cnc-wood-acrylic-aluminium-router-machine",
    name: "High Accuracy CNC Router Machine (Wood, Acrylic & Aluminium)",
    category: "Industrial CNC Routers & Milling",
    tagline: "Heavy-Duty Gantry Router for Aluminium, Acrylic, Wood & Composites",
    image: "/assets/images/machines/cnc-router-gantry.png",
    badge: "Heavy Structural Steel",
    spindle: "3.5 kW - 6.5 kW (Optional 9 kW HSD)",
    rpm: "6,000 - 24,000 RPM",
    bedSize: "4x4 ft, 8x4 ft, 10x5 ft (up to 2000x4000 mm)",
    materials: "Aluminium, Brass, Copper, Acrylic, Wood, MDF, Bakelite, ACP",
    accuracy: "0.1 mm (±0.05 mm Repeatability)",
    description: "Industrial heavy-duty gantry CNC router built with normalized stress-relieved tubular steel. Available in 1 to 5 spindle configurations with multi-zone vacuum clamping.",
    specs: [
      { label: "Working Envelopes", val: "4x4 ft (1200×1200) / 8x4 ft (1300×2500) / 10x5 ft (1500×3000 mm)" },
      { label: "Z-Axis Clearance", val: "250 mm to 300 mm Clearance" },
      { label: "Number of Spindles", val: "1 to 5 Spindles (Custom Configurable)" },
      { label: "Spindle Power", val: "3.5 kW to 6.5 kW Water/Air Cooled (Optional 9 kW HSD)" },
      { label: "Spindle Speed", val: "6,000 to 24,000 RPM Continuous Variable" },
      { label: "Motion Drives", val: "Precision Helical Rack & Pinion (X/Y) + C5 Ball Screw (Z)" },
      { label: "Axis Motors", val: "Leadshine Easy Servo / Delta AC Digital Servos" },
      { label: "Table Clamping", val: "Heavy T-Slot Aluminium + Multi-Zone High Vacuum Bed" },
      { label: "Rapid Traverse", val: "Up to 25,000 mm/min Rapid Speed" }
    ],
    features: [
      "Rigid welded structural steel tubular gantry normalized against internal stress for zero chatter",
      "Multi-zone vacuum matrix bed with high-capacity pump holds small offcuts and full 8x4 sheets securely",
      "Helical rack and pinion drive combined with AC digital servos for smooth 25,000 mm/min rapid motion",
      "Centralized automatic pulse lubrication system for all linear bearings and ball screws",
      "Modular multi-spindle capability (1-5 heads) allowing simultaneous parallel production"
    ]
  },
  {
    id: "vdm-milling",
    path: "/vdm-heavy-vertical-drilling-milling-machine",
    name: "VDM Heavy Vertical Drilling & Milling Machine (VDM30M / 50M / 100M)",
    category: "Heavy Industrial Metal Machining",
    tagline: "Cast Iron Rigid Machining Center for Mild Steel, SS304 & Switchboard Panels",
    image: "/assets/images/machines/vdm-milling-machine.png",
    badge: "Heavy Cast Iron Structure",
    spindle: "BT30 / BT40 Mechanical Taper",
    rpm: "600 - 8,000 RPM High Torque Servo",
    bedSize: "300x300 mm / 500x500 mm / 1000x1000 mm",
    materials: "Mild Steel (MS), Stainless Steel (SS304), Cast Iron, Copper Busbars, Aluminium",
    accuracy: "0.05 mm Positioning",
    description: "Heavy cast iron square-column vertical drilling and milling machine for switchboard manufacturers and toolrooms. Features 1 to 50 mm drilling, M3 to M20 rigid tapping, and Delta CNC.",
    specs: [
      { label: "Models in Series", val: "VDM30M (Compact) | VDM50M (Production) | VDM100M (Heavy Capacity)" },
      { label: "Drilling Capacity", val: "VDM30M: 1-12 mm | VDM50M: 1-25 mm | VDM100M: 1-50 mm" },
      { label: "Spindle Nose Taper", val: "BT30 / BT40 Mechanical Drawbar Taper" },
      { label: "Main Motor Power", val: "1.5 kW (2 HP) to 3.5 kW (5 HP) High-Torque Servo" },
      { label: "Standard Bed Sizes", val: "300×300 mm / 500×500 mm / 1000×1000 mm" },
      { label: "Tapping Capacity", val: "Rigid Synchronized Tapping from M3 up to M20" },
      { label: "Guideway Type", val: "HIWIN / THK Linear Guideways on Heavy Ground Box Ways" },
      { label: "Coolant & Enclosure", val: "High-Pressure Flood Coolant Pump & Protective Sheet Enclosure" },
      { label: "CNC Controller", val: "Delta CNC Industrial Controller with MPG Handwheel" }
    ],
    features: [
      "Meehanite cast iron structural base engineered to absorb heavy cutting and tapping vibrations",
      "High-torque servo spindle drive delivers full torque down to low RPM for 50mm drilling and tapping",
      "Rigid tapping capability without floating tap holders via synchronized spindle/Z-axis interpolation",
      "High-pressure flood coolant system with magnetic chip separator for continuous metal milling",
      "Delta CNC industrial controller with conversational canned cycles for rapid cutout programming"
    ]
  },
  {
    id: "foam-welding",
    path: "/foam-welding-machine",
    name: "Automatic Thermal Foam Welding Machine",
    category: "Packaging Automation",
    tagline: "Automated High-Speed Thermal Welding for Industrial Foam Fabrication",
    image: "/assets/images/machines/foam-welding-machine.png",
    badge: "Mass Production Foam Automation",
    spindle: "Thermal Platen Array",
    rpm: "Cycle Time: 5 - 15 Seconds",
    bedSize: "600 x 400 mm (Custom up to 1500 x 1000 mm)",
    materials: "EPE, EVA, XLPE, Polyurethane (PU) Foam, PP Bubble Guard",
    accuracy: "100% Thermal Molecular Fusion",
    description: "Automated packaging foam welding machine. Replaces expensive hot-melt glue and toxic solvents with clean, permanent thermal fusion for tool trays, cushioning, and dunnage boxes.",
    specs: [
      { label: "Machine Category", val: "Automatic Industrial Thermal Foam Welding Machine" },
      { label: "Platen Dimensions", val: "Standard 600×400 mm (Customizable up to 1500×1000 mm)" },
      { label: "Temperature Control", val: "50°C to 300°C Digital Closed-Loop PID Temperature System" },
      { label: "Cycle Time", val: "5 to 15 Seconds per Finished Welded Assembly" },
      { label: "Actuation Mechanism", val: "Pneumatic Cylinders with Dual Pressure Regulators & Ball Screws" },
      { label: "Safety System", val: "Two-Hand Anti-Tie-Down Safety Buttons & Light Curtain Option" },
      { label: "Power Supply", val: "230V Single Phase or 415V 3-Phase (4 to 8 kW Heating Load)" }
    ],
    features: [
      "100% glue-free thermal fusion eliminates adhesive costs, glue strings, and hazardous VOC fumes",
      "Digital PID temperature controller guarantees uniform heat distribution across the entire platen",
      "Pneumatically synchronized downward stroke ensures uniform bond pressure without crushing foam",
      "Dual two-hand safety anti-tie-down buttons provide complete operator protection",
      "Interchangeable tooling nests allow rapid retooling between different foam box formats in minutes"
    ]
  },
  {
    id: "educational-cnc",
    path: "/educational-cnc-machines",
    name: "Educational & Training CNC Machines",
    category: "Educational & Institutional CNC",
    tagline: "Safe Enclosed Training CNC Routers & PCB Machines for Colleges & Labs",
    image: "/assets/images/machines/educational-cnc-lab.png",
    badge: "College & Institutional Trainer",
    spindle: "800W - 1.5 kW Precision Spindle",
    rpm: "10,000 - 40,000 RPM",
    bedSize: "300 x 200 x 60 mm / 300 x 300 x 80 mm",
    materials: "PCB Clad, Aluminium, Brass, Acrylic, Wood, Modeling Foam, Delrin",
    accuracy: "±0.05 mm Industrial Grade Precision",
    description: "Compact benchtop CNC machine tools engineered specifically for engineering colleges, polytechnics, and skill development centres. Features full transparent safety enclosure and simulation software.",
    specs: [
      { label: "Machine Category", val: "Educational Benchtop CNC Machining & Prototyping Trainer" },
      { label: "Working Envelope", val: "300 × 200 × 60 mm / 300 × 300 × 80 mm" },
      { label: "Safety Enclosure", val: "360° Transparent Polycarbonate Housing with Interlock Switch" },
      { label: "Spindle Motor", val: "800W to 1.5 kW Precision Spindle (up to 40,000 RPM)" },
      { label: "Motion System", val: "Ground Linear Guideways & C7 Precision Ball Screws" },
      { label: "Operating Software", val: "CyTOS EduCAM Studio with Real-Time 3D Toolpath Simulation" },
      { label: "Language Standards", val: "Standard ISO G-Code and M-Code (Fanuc/Siemens Compatible)" },
      { label: "Electrical Input", val: "230V AC Single Phase Domestic Wall Plug (No 3-Phase Required)" }
    ],
    features: [
      "Complete physical safety: interlocked transparent enclosure cuts spindle power if doors open",
      "Authentic industrial CNC control teaching students real G-code, tool offsets, and work coordinates",
      "Virtual 3D toolpath simulation prevents accidental tool crashes and student programming errors",
      "Multi-material capability: students can machine PCBs, acrylic signs, wood, and aluminium brackets",
      "Turnkey institutional delivery includes student laboratory exercises and faculty training workshops"
    ]
  },
  {
    id: "robotic-dispensing",
    path: "/robotic-dispensing-cells",
    name: "Robotic Dispensing Cells",
    category: "SPM Automation",
    tagline: "Automated 3-Axis & 6-Axis Adhesive & Gasket Dispensing SPM",
    image: "/assets/images/robotic-spm.jpg",
    badge: "Zero Waste Automation",
    spindle: "Precision Dispensing Head (1K / 2K)",
    rpm: "Servo Positive Displacement",
    bedSize: "400 x 400 mm to 1500 x 1500 mm",
    materials: "RTV Silicone, Polyurethane, Epoxy, Thermal Paste, UV Glue",
    accuracy: "±0.01 mm Bead Consistency",
    description: "Custom automated robotic dispensing cells engineered for automotive lighting, EV battery packs, filter sealing, and electronics potting.",
    specs: [
      { label: "Kinematics", val: "3-Axis Cartesian Gantry / 6-Axis Articulated Robot Arm" },
      { label: "Dispensing Repeatability", val: "±0.01 mm Path Tracking Accuracy" },
      { label: "Flow Rate Range", val: "0.01 cc/sec to 15 cc/sec Micro-Controlled" },
      { label: "Mix Ratio (2K Resin)", val: "100:10 to 100:100 Dynamic Metering" },
      { label: "Material Feeding", val: "Pressurized Tank / 5-Gal Pail Pump / 55-Gal Drum Unloader" }
    ],
    features: [
      "Eliminates operator fatigue and reduces adhesive material wastage by 35%",
      "Vision camera option for automatic workpiece skew correction and bead verification",
      "Integrated suck-back anti-drip valve ensures crisp start and stop transitions",
      "Programmable continuous bead, micro-dotting, potting, and encapsulation cycles"
    ]
  },
  {
    id: "pneumatic-fixtures",
    path: "/pneumatic-welding-fixtures",
    name: "Pneumatic Welding Fixtures & Tooling",
    category: "Welding & Fabrication",
    tagline: "Precision Clamping Fixtures & Turnkey Welding Automation Jigs",
    image: "/assets/images/case-study-welding.jpg",
    badge: "Automotive Grade",
    spindle: "Pneumatic Power Clamps",
    rpm: "Cycle Time: 8-15 seconds",
    bedSize: "Custom to component geometry",
    materials: "Hardened Tool Steel (EN31, D2), Copper Chill Blocks",
    accuracy: "±0.1 mm Welding Datum Repeatability",
    description: "Heavy-duty pneumatic clamping fixtures, robotic weld cells, and assembly jigs designed to eliminate weld distortion and guarantee component interchangeability.",
    specs: [
      { label: "Actuation", val: "Festool / SMC Pneumatic Cylinders & Toggle Clamps" },
      { label: "Sensors", val: "Proximity & Part-Seating Sensors with Safety Interlocks" },
      { label: "Base Structure", val: "Machined Steel Baseplate with Ground Locating Pins" },
      { label: "Heat Dissipation", val: "Integrated Beryllium-Copper Heat Sinks / Chill Blocks" }
    ],
    features: [
      "Foolproof 'Poka-Yoke' design prevents incorrect loading of automotive stampings",
      "Integrated pneumatic sequence valves for synchronized progressive clamping",
      "High-wear locating pins hardened to 58-62 HRC for 500,000+ cycle life",
      "Modular design for rapid retooling between vehicle variant batches"
    ]
  },
  {
    id: "plc-panels",
    path: "/plc-control-panels",
    name: "PLC & Industrial Control Panels",
    category: "Industrial Electrical",
    tagline: "Custom Automation Control Panels, VFD Drives & SCADA Integration",
    image: "/assets/images/machines/industrial-control-panel.jpg",
    badge: "IP55 / IP65 Certified",
    spindle: "Siemens / Mitsubishi / Schneider",
    rpm: "Real-Time 1ms PLC Scan Time",
    bedSize: "Wall Mount / Floor Standing Rittal Enclosures",
    materials: "CRCA Powder Coated Sheet / SS304 Stainless Steel",
    accuracy: "CE / IEC 61439 Standard",
    description: "Turnkey electrical design, PLC programming, VFD motor control, servo drive configuration, and HMI/SCADA dashboarding for manufacturing plants.",
    specs: [
      { label: "Enclosure Rating", val: "IP54 / IP55 / IP65 Dust and Water Protection" },
      { label: "PLC Hardware", val: "Siemens S7-1200 / S7-1500, Mitsubishi FX5U, Delta" },
      { label: "HMI Display", val: "7\\\" to 15\\\" Color TFT Touchscreens with Recipe Storage" },
      { label: "Switchgear Brands", val: "Schneider Electric / ABB / Siemens Industrial Switchgear" },
      { label: "Documentation", val: "Complete EPLAN Circuit Schematics & Wire Ferruling Map" }
    ],
    features: [
      "Color-coded wire routing with laser-printed heat-shrink ferrules at every terminal",
      "Type-tested short-circuit withstand and thermal ventilation simulation",
      "Emergency Stop relay circuits meeting Cat 4 / PL e safety standards",
      "Cloud IoT gateway option for remote OEE monitoring and predictive maintenance"
    ]
  },
  {
    id: "spm-automation",
    path: "/spm-automation",
    name: "Custom SPM Automation Machines",
    category: "Turnkey Systems",
    tagline: "Purpose-Built Multi-Station Machines Engineered Around Your Product",
    image: "/assets/images/machines/spm-automation-cell.jpg",
    badge: "Turnkey Engineering",
    spindle: "Multi-Station Servo & Pneumatic",
    rpm: "Custom Indexed Cycles",
    bedSize: "Rotary Dial / Linear Transfer / Gantry",
    materials: "Automotive, FMCG, Electrical, Medical Parts",
    accuracy: "High Throughput Mass Production",
    description: "End-to-end custom machine design from conceptual 3D CAD to CNC machining, assembly, commissioning, and cycle-time optimization in our Pune facility.",
    specs: [
      { label: "Architecture", val: "Rotary Indexing Table / Walking Beam / Cartesian Gantry" },
      { label: "Cycle Time Target", val: "Typically 6 to 30 seconds per finished assembly" },
      { label: "Quality Inspection", val: "Keyence / Cognex Vision Cameras & LVDT Gauges" },
      { label: "Traceability", val: "Laser Marker + 2D DataMatrix Barcode Scanner Integration" }
    ],
    features: [
      "Single-source responsibility: in-house mechanical CAD, machining, wiring & software",
      "Pre-delivery factory acceptance test (FAT) with actual production run at our plant",
      "Full operator safety light curtains, interlocked polycarbonate doors & E-stop zones",
      "Over 150+ custom SPM systems successfully deployed across Indian industrial corridors"
    ]
  }
];
"""

with open(MACHINES_DATA_FILE, "w", encoding="utf-8") as f:
    f.write(machines_data_js)

print("Updated src/data/machinesData.js with all 12 machines.")
