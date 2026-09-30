export const machinesData = [
  {
    id: "cnc-routers",
    path: "/cnc-routers-milling",
    name: "Heavy-Duty CNC Routers & Milling",
    category: "CNC Machining",
    tagline: "Industrial Heavy-Duty Gantry Router for High-Speed Routing & 3D Engraving",
    image: "/assets/images/cnc-router.jpg",
    badge: "Most Popular Industrial",
    spindle: "3.5 kW - 7.5 kW Air/Water Cooled",
    rpm: "18,000 - 24,000 RPM",
    bedSize: "1300 x 2500 mm / Custom",
    materials: "Aluminum, Brass, Acrylic, Composite, Wood, Foam",
    accuracy: "±0.02 mm Repeatability",
    description: "Built with heavy stress-relieved steel gantry, precision helical rack and pinion, and industrial linear motion guides for vibration-free heavy cutting.",
    specs: [
      { label: "Working Area", val: "1300 x 2500 x 200 mm (Customizable up to 2000 x 4000 mm)" },
      { label: "Spindle Motor", val: "3.5 kW to 9.0 kW High-Torque HSD / Italian Type" },
      { label: "Spindle Speed", val: "6,000 to 24,000 RPM Continuous Variable" },
      { label: "Drive System", val: "Hybrid Servo / AC Digital Servo Motors on All Axes" },
      { label: "Controller", val: "DSP Handheld / Mach3 Industrial / Syntec CNC" },
      { label: "Table Surface", val: "T-Slot Aluminum + Multi-Zone High Vacuum Bed" },
      { label: "Positional Accuracy", val: "±0.02 mm / 300 mm" },
      { label: "Max Rapid Speed", val: "25,000 mm/min" }
    ],
    features: [
      "Rigid welded structural steel tubular gantry normalized against internal stress",
      "Automatic Tool Length Sensor and Tool Touch Plate calibration",
      "High-power multi-zone vacuum clamping bed with oil-free vacuum pump",
      "Centralized automatic pulse lubrication system for all linear bearings and ball screws",
      "Integrated dust extraction hood and high-efficiency dual-bag chip collector"
    ]
  },
  {
    id: "pcb-drilling",
    path: "/pcb-drilling-routing",
    name: "PCB Drilling & Routing Machines",
    category: "Electronics Manufacturing",
    tagline: "Ultra-High Precision Micro-Hole PCB Drilling up to 60,000 RPM",
    image: "/assets/images/pcb-drilling.jpg",
    badge: "60k RPM High Frequency",
    spindle: "High-Frequency Electro-Spindle",
    rpm: "60,000 RPM (Optional 80,000 RPM)",
    bedSize: "300 x 400 mm / 500 x 600 mm",
    materials: "FR4, High-Tg FR4, Rogers, Polyimide, Aluminum-Clad MCPCB",
    accuracy: "±0.005 mm Micro-Precision",
    description: "Engineered specifically for electronics manufacturing plants and PCB prototyping labs demanding micro-via drilling from 0.2 mm with zero burr.",
    specs: [
      { label: "Work Area (Single / Multi)", val: "PCB-60 (Single Spindle: 320 x 450 mm) | PCB-12 (Twin Spindle)" },
      { label: "Spindle Technology", val: "Precision Hybrid Ceramic Bearing Electro-Spindle" },
      { label: "Drill Diameter Range", val: "0.2 mm to 3.175 mm (0.008\" to 0.125\")" },
      { label: "Spindle RPM", val: "10,000 - 60,000 RPM Variable Inverter Drive" },
      { label: "Z-Axis Stroke", val: "50 mm Precision Ball Screw with Linear Scale" },
      { label: "Positioning Repeatability", val: "±0.005 mm (5 microns)" },
      { label: "Depth Sensing", val: "Dynamic Optical / Electrical Surface Contact Sensor" },
      { label: "Collet Chuck", val: "Pneumatic Automatic / Manual Quick-Clamp 3.175 mm" }
    ],
    features: [
      "Dynamic auto-leveling surface map compensates for board warp in real-time",
      "Closed-loop micro chiller stabilizes spindle temperature within ±0.5°C",
      "Precision collet TIR (Total Indicated Runout) maintained below 3 microns",
      "Optical laser tool breakage detection prevents ruined copper boards",
      "Direct Gerber / Excellon drill file import with automatic tool mapping"
    ]
  },
  {
    id: "pcb-prototyping",
    path: "/pcb-prototyping",
    name: "Chemical-Free PCB Prototyping",
    category: "R&D & Laboratory",
    tagline: "In-House Rapid PCB Isolation Milling — No Acid Etching, No Fumes",
    image: "/assets/images/pcb-proto.jpg",
    badge: "Eco-Friendly Prototyping",
    spindle: "Precision Brushless DC / HF Spindle",
    rpm: "30,000 - 60,000 RPM",
    bedSize: "230 x 310 mm (A4 Format) / A3 Format",
    materials: "Single/Double Sided FR4, Rogers, PTFE, Flex-PCB",
    accuracy: "0.1 mm Trace / Space Isolation",
    description: "Turn your EDA Gerber files into physical working prototype circuit boards in under 30 minutes right in your engineering lab.",
    specs: [
      { label: "Working Format", val: "A4 (230 x 310 mm) / A3 (320 x 420 mm)" },
      { label: "Isolation Track Pitch", val: "0.1 mm (4 mil) minimum track / gap" },
      { label: "Spindle Motor", val: "High-Performance Brushless Spindle with Electronic Brake" },
      { label: "Software Included", val: "CyTOS CAM Pro with Gerber & Excellon Parser" },
      { label: "Board Clamping", val: "Precision Vacuum Base + Mechanical Low-Profile Clamps" },
      { label: "Weight & Footprint", val: "Compact Benchtop Lab Design (approx. 45 kg)" }
    ],
    features: [
      "100% chemical-free mechanical milling — eliminates toxic FeCl3 acid etching",
      "Auto surface probing generates a 100-point height map for uniform trace depth",
      "Instant turnaround: complete prototype delivered in 25 minutes vs 5-day fab house wait",
      "Dual-sided PCB alignment using precision optical dowel pin registration",
      "Safe for academic classrooms, defense defense labs, and corporate R&D"
    ]
  },
  {
    id: "vdm-milling",
    path: "/vdm-milling",
    name: "VDM Vertical Drilling & Milling",
    category: "Heavy Industrial Machining",
    tagline: "Rigid Vertical Milling Machine for Control Panels, Enclosures & Dies",
    image: "/assets/images/machines/vdm-milling-machine.png",
    badge: "Heavy Rigid Column",
    spindle: "BT30 / BT40 Mechanical Taper",
    rpm: "3,000 - 8,000 RPM High Torque",
    bedSize: "800 x 500 mm / 1200 x 600 mm",
    materials: "Mild Steel, Stainless Steel (SS304), Cast Iron, Copper Busbars",
    accuracy: "±0.015 mm Positioning",
    description: "Designed for electrical control panel builders, switchboard manufacturers, and toolrooms requiring deep slot milling, hole drilling, and rigid tapping.",
    specs: [
      { label: "Table Travel (X x Y x Z)", val: "800 x 500 x 400 mm" },
      { label: "Spindle Nose Taper", val: "BT30 / BT40 with Mechanical Drawbar" },
      { label: "Main Motor Power", val: "3.7 kW / 5.5 kW Induction Servo Motor" },
      { label: "Max Table Load", val: "500 kg Heavy-Duty Meehanite Cast Base" },
      { label: "Guideway Type", val: "Hardened & Ground Square Boxways / Heavy Linear Roller" },
      { label: "CNC Controller", val: "Siemens 808D / Fanuc Oi-TF / GSK CNC" }
    ],
    features: [
      "Meehanite cast iron structural base stress-relieved for lifetime thermal stability",
      "Heavy-duty rigid tapping capability for panel mounting threads (M3 to M20)",
      "High-pressure flood coolant system with magnetic chip separator",
      "Full perimeter splash guarding with interlocked safety sliding door"
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
      { label: "HMI Display", val: "7\" to 15\" Color TFT Touchscreens with Recipe Storage" },
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
