# -*- coding: utf-8 -*-
"""
scripts/product_catalog_definitions.py
Structured product data extracted directly from CyTOS 2026 Catalog & Profile.
"""

MACHINE_PRODUCTS = [
    {
        "id": "cnc-6060",
        "path": "/cnc-6060-pcb-drilling-routing-machine",
        "jsx_filename": "Cnc6060Page.jsx",
        "name": "CNC 6060 PCB Drilling & Routing Machine",
        "model_code": "CyTOS CNC 6060",
        "category": "PCB Drilling & Routing Machines",
        "seo_title": "CNC 6060 PCB Drilling & Routing Machine - 60,000 to 100,000 RPM Spindle Manufacturer from Pune | CyTOS",
        "meta_desc": "Manufacturer of CNC 6060 PCB Drilling & Routing Machine - 18,000 to 100,000 RPM spindle, 0.2mm micro-drilling, multi-spindle & pneumatic ATC options. Direct factory price from CyTOS Pune, Maharashtra.",
        "keywords": "CNC 6060 PCB Drilling Machine, PCB Routing Machine, PCB Drilling Machine Manufacturer Pune, 60000 RPM PCB Spindle, Micro Drill PCB Machine, Industrial PCB Drilling Machine India, CyTOS Bhosari MIDC",
        "image": "/assets/images/machines/pcb-drilling-pcb60.png",
        "image_title": "CNC 6060 PCB Drilling and Routing Machine Double Spindle with ATC, Pune, India",
        "image_caption": "CyTOS CNC 6060 floor-mounted PCB drilling and routing machine equipped with 60,000 to 100,000 RPM electro-spindle and PC-based industrial console.",
        "additional_images": [
            {
                "url": "/assets/images/machines/pcb-cnc-cabinet.png",
                "title": "CyTOS CNC Industrial Electrical Cabinet and Servo Drives, Pune",
                "caption": "Precision motion controller cabinet with segregated AC servo drives and noise-immune industrial wiring."
            },
            {
                "url": "/assets/images/machines/precision-machining-parts.png",
                "title": "Burr-free 0.2mm Micro-hole PCB Drilling Sample, Pune",
                "caption": "Microscopic cross-section of 0.2mm drill via walls in multilayer FR4 panel processed on CyTOS CNC 6060."
            }
        ],
        "badge": "100,000 RPM ULTRA-HIGH SPEED",
        "hero_title": "CNC 6060 PCB Drilling &amp; Routing Machine",
        "hero_subtitle": "Industrial floor-mounted PCB production machine with 18,000 to 100,000 RPM electro-spindles, 0.2 mm micro-hole drilling capability, dowel-pin and vacuum bed clamping, and 1 to 5 spindle synchronized configurations for continuous 24/7 manufacturing shifts.",
        "in_brief": "The CyTOS CNC 6060 is our flagship commercial PCB drilling and routing workhorse, manufactured at our Bhosari MIDC facility in Pune. Designed for medium to large production volumes, it delivers 0.2 mm micro-drilling and high-speed contour routing across multilayer FR4, CEM-1, CEM-3, and aluminium-backed MCPCB panels with ±0.03 mm repeatability and optional pneumatic tool changing.",
        "highlights": [
            {"val": "100,000 RPM", "lbl": "Max Spindle RPM"},
            {"val": "0.2 mm", "lbl": "Min Micro-Drill Dia"},
            {"val": "600 × 600 mm", "lbl": "Single Working Area"},
            {"val": "1 to 5", "lbl": "Spindle Configurations"}
        ],
        "specs": [
            {"param": "Machine Architecture", "val": "Heavy Floor Mounted Welded Steel & Cast Structure", "cls": "Standard"},
            {"param": "Working Area (Single Spindle)", "val": "X: 600 mm × Y: 600 mm × Z: 100 mm", "cls": "Standard"},
            {"param": "Spindle RPM Range", "val": "18,000 RPM to 100,000 RPM Variable Inverter Drive", "cls": "High Frequency"},
            {"param": "Spindle Power Rating", "val": "1.2 kW to 4.5 kW Water/Air Cooled", "cls": "Standard"},
            {"param": "Number of Spindles", "val": "1 to 5 Synchronized Spindles (Custom Configurable)", "cls": "Configurable"},
            {"param": "Drilling Diameter Range", "val": "0.2 mm to 3.0 mm Micro-Drill Bits", "cls": "Tested Metric"},
            {"param": "Routing Diameter Range", "val": "1.0 mm to 4.0 mm Contour Cutters", "cls": "Standard"},
            {"param": "Rapid Traverse Speed", "val": "6,000 mm/min to 15,000 mm/min", "cls": "Standard"},
            {"param": "Positional Accuracy", "val": "0.05 mm (50 Microns)", "cls": "Laser Verified"},
            {"param": "Repeatability", "val": "±0.03 mm to ±0.05 mm", "cls": "Laser Verified"},
            {"param": "Axis Drive Motors", "val": "Easy Servo / Digital AC Servo Axis Motors", "cls": "Industrial Grade"},
            {"param": "Motion Mechanism", "val": "C5 Precision Ground Ball Screws + HIWIN Linear Guide Rails", "cls": "Standard"},
            {"param": "Workpiece Clamping", "val": "Dowel Pin Fixture / T-Slot Aluminium Bed + Vacuum Hold-Down", "cls": "Dual System"},
            {"param": "Tool Changing", "val": "Manual Quick Collet / Pneumatic Automatic Tool Changer (ATC)", "cls": "Optional ATC"},
            {"param": "Collet Size", "val": "3 mm to 6 mm Precision Collets", "cls": "Standard"},
            {"param": "Controller Hardware", "val": "CyTOS PC-Based CNC Controller with High-Speed USB 2.0 Interface", "cls": "In-House System"},
            {"param": "Programming Standard", "val": "Standard NC Language (G-Code, M-Code), Direct Excellon (.drl) & Gerber Import", "cls": "Universal"},
            {"param": "Power Supply Requirements", "val": "230V – 240V AC, 16A, 50Hz (Single Phase or 3-Phase available)", "cls": "Standard"},
            {"param": "Accessories Included", "val": "Coolant Tank, Dust Collection Hood, Operator Console with Monitor & CPU", "cls": "Complete Turnkey"}
        ],
        "features": [
            "Heavy floor-mounted structural steel frame normalized against internal stresses for vibration-free 24/7 continuous operation",
            "Ultra-high-speed hybrid ceramic bearing electro-spindle achieving up to 100,000 RPM with dynamic runout (TIR) under 3 microns",
            "Multi-spindle modular configuration allowing 1 to 5 synchronized heads to drill multiple identical PCB panels simultaneously",
            "Integrated optical / touch surface height probing that compensates for PCB panel warp and guarantees uniform Z-depth across the entire 600x600mm bed",
            "Proprietary CyTOS CAM software supporting native Excellon drill and Gerber RS-274X contour files without third-party converter licenses"
        ],
        "materials": [
            {"mat": "Standard FR4 (Single / Double Sided)", "status": "Optimal", "speed": "40,000 – 60,000 RPM", "notes": "Clean burr-free entry/exit holes down to 0.2mm"},
            {"mat": "Multilayer FR4 (4 to 12 Layers)", "status": "Optimal", "speed": "50,000 – 80,000 RPM", "notes": "No pad tear or inner-layer delamination with pecking cycles"},
            {"mat": "Aluminium-Core MCPCB (LED Boards)", "status": "Optimal", "speed": "28,000 – 40,000 RPM", "notes": "Mist coolant prevents aluminium chip welding"},
            {"mat": "CEM-1 & CEM-3 Composite Laminates", "status": "Optimal", "speed": "35,000 – 50,000 RPM", "notes": "High feed rate and long tool life for consumer electronics"},
            {"mat": "Rogers & PTFE High-Frequency Substrates", "status": "Capable", "speed": "60,000 – 100,000 RPM", "notes": "Special micro-grain carbide bits prevent PTFE smear"},
            {"mat": "Bakelite & Phenolic Paper Boards", "status": "Optimal", "speed": "30,000 – 45,000 RPM", "notes": "Dry cutting with dual-bag vacuum extraction"}
        ],
        "standard_accessories": [
            "Complete PC-Based CNC Controller with Color LED Display & Keyboard Console",
            "High-Efficiency Dual-Bag Dust Collector & Vacuum Suction Shroud",
            "Coolant Recirculation Tank with Submersible Pump & Filtration Mesh",
            "Universal T-Slot Aluminium Clamping Bed with Dowel Pin Alignment Holes",
            "Pre-loaded CyTOS CAM & Motion Studio Software with G-Code Interpreter",
            "12-Month Comprehensive Factory Warranty & On-Site Installation in India"
        ],
        "optional_accessories": [
            "Pneumatic Automatic Tool Changer (ATC) with 6 to 12 Tool Station Rack",
            "Optical CCD Vision Camera for Fiducial Registration & Panel Skew Correction",
            "Closed-Loop Water Chiller for High-Duty Spindle Temperature Stabilization",
            "Multi-Zone High-Flow Vacuum Clamping Bed with Rotary Vane Vacuum Pump",
            "Additional Spindle Heads (up to 5 Synchronized Spindles per Gantry)",
            "Automated Tool Length Sensor & Micro-Drill Breakage Laser Detector"
        ],
        "faqs": [
            {
                "q": "What is the smallest hole diameter the CNC 6060 can drill in production?",
                "a": "The CyTOS CNC 6060 reliably drills holes down to 0.2 mm (200 microns) in standard FR4 and multilayer circuit boards. Combined with 60,000 to 100,000 RPM spindles and controlled micro-pecking cycles, drill bit breakage is minimized even during continuous batch runs."
            },
            {
                "q": "Can the CNC 6060 handle both drilling and edge routing in a single job?",
                "a": "Yes. The CNC 6060 is a full dual-purpose machine. It performs all high-speed through-hole and via drilling, followed immediately by outer board contour routing, slotting, V-grooving, and panel tab de-paneling without removing the workpiece from the fixture."
            },
            {
                "q": "How does the multi-spindle configuration benefit our manufacturing line?",
                "a": "With multi-spindle setups (up to 5 spindles), the machine operates synchronously across multiple panels mounted on the table. A 3-spindle machine produces 3 complete panels in the same cycle time as a single spindle, effectively tripling production capacity without tripling floor space or operator costs."
            },
            {
                "q": "What file formats does the machine accept from EDA software like Altium or KiCad?",
                "a": "The machine accepts standard Excellon drill files (.drl, .txt) and Gerber RS-274X files (.gbr) directly. Our in-house CAM software automatically parses tool diameters, optimizes toolpath travel to reduce cycle times, and assigns spindle speeds."
            },
            {
                "q": "What after-sales service and spare parts support is available?",
                "a": "All machines are manufactured at our Bhosari MIDC facility in Pune. We maintain a full inventory of spindles, collets, ball screws, stepper/servo drives, and controllers. Our field engineers provide direct on-site installation, commissioning, operator training, and annual maintenance contracts (AMC) across India."
            }
        ]
    },
    {
        "id": "cnc-3020",
        "path": "/cnc-3020-pcb-prototyping-machine",
        "jsx_filename": "Cnc3020Page.jsx",
        "name": "CNC 3020 PCB Rapid Prototyping Machine",
        "model_code": "CyTOS CNC 3020",
        "category": "PCB Prototyping & R&D Machines",
        "seo_title": "CNC 3020 PCB Rapid Prototyping Machine - Chemical-Free Desktop Milling Machine Manufacturer from Pune | CyTOS",
        "meta_desc": "Manufacturer of CNC 3020 PCB Rapid Prototyping Machine - Chemical-free isolation milling, 40,000 RPM spindle, auto-leveling & visual camera for R&D labs and colleges. CyTOS Pune, Maharashtra.",
        "keywords": "CNC 3020 PCB Prototyping Machine, Desktop PCB Milling Machine, Chemical Free PCB Prototyping, PCB Prototyper India, Lab PCB CNC Machine, Educational PCB CNC Pune, CyTOS Rapid Prototyping",
        "image": "/assets/images/machines/pcb-prototyping-pcb30.png",
        "image_title": "CNC 3020 Chemical-Free Desktop PCB Rapid Prototyping Machine, Pune, India",
        "image_caption": "CyTOS CNC 3020 tabletop rapid PCB prototyping machine featuring auto-surface leveling and optical camera for engineering colleges and corporate R&D labs.",
        "additional_images": [
            {
                "url": "/assets/images/machines/educational-cnc-lab.png",
                "title": "Educational PCB CNC Prototyping Laboratory Setup, Pune",
                "caption": "Fully enclosed chemical-free PCB prototyping workcell installed in academic research laboratory."
            },
            {
                "url": "/assets/images/machines/precision-machining-parts.png",
                "title": "Fine Track Isolation Milling Sample 0.1mm Pitch, Pune",
                "caption": "Clean mechanical isolation milling traces and micro-via pads on double-sided FR4 circuit board."
            }
        ],
        "badge": "100% CHEMICAL-FREE PROTOTYPING",
        "hero_title": "CNC 3020 PCB Rapid Prototyping Machine",
        "hero_subtitle": "Compact tabletop PCB isolation milling machine engineered specifically for corporate R&D departments, defense labs, and engineering colleges. Features 18,000 to 40,000 RPM spindle, dynamic auto-surface leveling, optical camera alignment, and 100% dry mechanical processing with zero toxic wet chemicals.",
        "in_brief": "The CyTOS CNC 3020 allows electronics design engineers to convert CAD Gerber files into physical working double-sided circuit prototypes in under 30 minutes right in their lab. Manufactured in Pune, it completely replaces slow, toxic ferric chloride acid etching with clean, high-precision mechanical isolation milling.",
        "highlights": [
            {"val": "40,000 RPM", "lbl": "High-Speed Spindle"},
            {"val": "300 × 200 mm", "lbl": "A4 Working Area"},
            {"val": "0.1 mm", "lbl": "Min Track / Gap"},
            {"val": "0% Acid", "lbl": "Green Lab Safe"}
        ],
        "specs": [
            {"param": "Machine Category", "val": "Compact Tabletop Precision PCB Prototyper", "cls": "Standard"},
            {"param": "Working Envelope (X × Y × Z)", "val": "X: 300 mm × Y: 200 mm × Z: 60 mm (A4 Format)", "cls": "Standard"},
            {"param": "Overall Machine Dimensions", "val": "3 ft × 4 ft × 5 ft (Compact Benchtop Footprint)", "cls": "Standard"},
            {"param": "Machine Weight", "val": "60 kg to 80 kg (Solid Vibration-Resistant Structure)", "cls": "Benchtop"},
            {"param": "Spindle Motor Power", "val": "0.8 kW to 1.2 kW Precision Spindle Motor", "cls": "Standard"},
            {"param": "Spindle Speed Range", "val": "18,000 RPM to 40,000 RPM Continuous Variable", "cls": "High Frequency"},
            {"param": "Spindle Cooling Options", "val": "Air Cooled & Water Cooled Both Available", "cls": "Configurable"},
            {"param": "Min Drill Diameter", "val": "0.4 mm to 3.0 mm Carbide Drills", "cls": "Tested Metric"},
            {"param": "Min Routing Diameter", "val": "1.0 mm to 3.0 mm End Mills", "cls": "Standard"},
            {"param": "Min Track Pitch / Isolation", "val": "0.1 mm (4 mil) Minimum Trace & Clearance Width", "cls": "High Precision"},
            {"param": "Travel Speed", "val": "Up to 6,000 mm/min Rapid Traverse", "cls": "Standard"},
            {"param": "Positional Accuracy", "val": "0.05 mm (50 Microns)", "cls": "Laser Calibrated"},
            {"param": "Repeatability (99%)", "val": "±0.05 mm Consistent Positioning", "cls": "Laser Calibrated"},
            {"param": "Tool Changing Mechanism", "val": "Manual Quick-Clamp / Pneumatic Button Press ATC", "cls": "Standard/Opt"},
            {"param": "PCB Clamping Mechanism", "val": "Precision Dowel Pin Fixture / T-Slot Aluminium Bed", "cls": "Standard"},
            {"param": "Surface Leveling System", "val": "Automated Dynamic Surface Height Matrix Probing", "cls": "Included"},
            {"param": "Optical Inspection", "val": "Integrated Optical USB Camera for Visual Alignment", "cls": "Included"},
            {"param": "Safety & Environment", "val": "Transparent Polycarbonate Protective Enclosure", "cls": "Included"},
            {"param": "Control System", "val": "PC-Based CyTOS Studio with USB 2.0 Interface & G-Code Support", "cls": "Standard"}
        ],
        "features": [
            "100% chemical-free mechanical isolation milling — completely eliminates toxic ferric chloride (FeCl3) acid handling, fumes, and hazardous chemical disposal",
            "Automated multi-point capacitive surface probing creates a digital height map to compensate for PCB board warpage and maintain exact trace depth",
            "High-resolution optical camera overlay allows real-time visual inspection of pad alignment and zero-point calibration directly on the monitor",
            "Precision dowel pin registration system makes double-sided PCB fabrication straightforward with exact top-to-bottom pad alignment",
            "Compact, fully enclosed tabletop design with interlocked transparent safety shield suitable for cleanroom, university, or corporate lab deployment"
        ],
        "materials": [
            {"mat": "Single & Double Sided FR4 Copper Clad", "status": "Optimal", "speed": "30,000 – 40,000 RPM", "notes": "Clean 0.1mm isolation tracks and 0.4mm vias in minutes"},
            {"mat": "Rogers High-Frequency RF Laminates", "status": "Optimal", "speed": "35,000 – 40,000 RPM", "notes": "Ideal for 2.4GHz and 5GHz antenna and filter prototyping"},
            {"mat": "Flexible PCB Substrates (Polyimide)", "status": "Capable", "speed": "25,000 – 35,000 RPM", "notes": "Requires vacuum hold-down bed to prevent membrane flutter"},
            {"mat": "Aluminium-Core MCPCBs", "status": "Capable", "speed": "20,000 – 30,000 RPM", "notes": "Excellent for high-power LED driver board prototyping"},
            {"mat": "Acrylic & Soft Plastic Enclosures", "status": "Optimal", "speed": "18,000 – 25,000 RPM", "notes": "Faceplate cutouts, engraving, and LED lens machining"}
        ],
        "standard_accessories": [
            "Fully Enclosed Tabletop Safety Cabinet with Transparent Viewing Window",
            "Automatic Surface Height Probing Probe and Ground Clip",
            "High-Resolution Visual Alignment Camera with On-Screen Crosshairs",
            "Starter Tooling Kit: 10x Isolation V-Bits, 10x Micro-Drills, 5x End Mills",
            "CyTOS CAM Pro Software License with Gerber RS-274X & Excellon Importer",
            "12-Month Comprehensive Warranty and Factory Operator Video Training"
        ],
        "optional_accessories": [
            "Pneumatic Button-Press Automatic Tool Changing (ATC) Collet System",
            "Micro Vacuum Hold-Down Table with Low-Noise Oil-Free Diaphragm Pump",
            "Fine Dust Evacuation Shroud with Compact HEPA Laboratory Filter",
            "Double-Sided PCB Riveting Press for Metallized Through-Hole Vias",
            "Educational Curriculum Package with 20 Student Lab Workbooks"
        ],
        "faqs": [
            {
                "q": "How does chemical-free PCB prototyping compare with traditional wet etching?",
                "a": "Wet etching requires acid handling, photoresist printing, UV exposure, chemical etching tanks, neutralizing baths, and hazardous waste disposal — taking several hours and posing safety hazards. The CyTOS CNC 3020 mechanically mills the copper isolation channels directly using a carbide V-bit in 15 to 30 minutes with zero chemicals, zero fumes, and zero hazardous waste."
            },
            {
                "q": "How does the machine handle warped or uneven PCB boards?",
                "a": "The CNC 3020 features an automated surface leveling probe. Before milling, the tool lightly touches the copper board at 50 to 100 points across the surface, generating an exact 3D height map. During isolation milling, the Z-axis dynamically interpolates to follow the board curvature, guaranteeing constant 0.05 mm trace depth."
            },
            {
                "q": "Can students or junior technicians operate this machine safely?",
                "a": "Yes. The CNC 3020 is designed specifically for academic institutions and prototyping labs. It features a fully interlocked polycarbonate safety enclosure, emergency stop button, low noise levels under 65 dB, and an intuitive graphical user interface that imports Gerber files with one click."
            },
            {
                "q": "Can we make double-sided circuit boards with via alignment?",
                "a": "Yes. The machine includes a precision optical camera and hardened dowel pin alignment block. After milling side A, the board is flipped along the reference dowel pins, and the optical camera confirms pad coordinates, ensuring exact via hole alignment between top and bottom layers."
            },
            {
                "q": "What is the typical turnaround time from CAD schematic to physical prototype?",
                "a": "Once your schematic and layout are completed in Altium, KiCad, or Eagle, exporting the Gerber files and milling a standard 100 × 80 mm double-sided prototype board typically takes just 20 to 25 minutes on the CyTOS CNC 3020."
            }
        ]
    },
    {
        "id": "cnc-3030",
        "path": "/cnc-3030-pcb-prototyping-machine",
        "jsx_filename": "Cnc3030Page.jsx",
        "name": "CNC 3030 High Precision PCB Drilling & Routing Machine",
        "model_code": "CyTOS CNC 3030",
        "category": "High Speed PCB Prototyping",
        "seo_title": "CNC 3030 PCB Drilling & Routing Machine - 60,000 RPM High Precision Prototyping Machine Manufacturer from Pune | CyTOS",
        "meta_desc": "Manufacturer of CNC 3030 PCB Drilling and Routing Machine - 60,000 RPM spindle, 0.3mm track isolation, pneumatic ATC & T-slot bed. Benchtop precision from CyTOS Pune.",
        "keywords": "CNC 3030 PCB Drilling Machine, High Precision PCB Prototyping, 60000 RPM PCB Machine, Benchtop PCB Milling Machine Pune, PCB Router Machine, CyTOS CNC Pune Manufacturer",
        "image": "/assets/images/machines/pcb-prototyping-pcb30.png",
        "image_title": "CyTOS CNC 3030 Heavy-Duty High-Precision PCB Drilling & Routing Machine, Pune",
        "image_caption": "CyTOS CNC 3030 heavy benchtop PCB machining center with 60,000 RPM water-cooled spindle and AC servo motion control.",
        "additional_images": [
            {
                "url": "/assets/images/machines/precision-machining-parts.png",
                "title": "Precision PCB Drilling and Milling Components, Pune",
                "caption": "Close-up of fine-pitch SMD pads and contour routed edges produced on the CNC 3030."
            },
            {
                "url": "/assets/images/machines/pcb-cnc-cabinet.png",
                "title": "Digital AC Servo Drive Integration for CNC 3030, Pune",
                "caption": "High-torque closed-loop servo drive configuration delivering 166 mm/sec rapid travel speeds."
            }
        ],
        "badge": "60,000 RPM HIGH PRECISION",
        "hero_title": "CNC 3030 High Precision PCB Drilling &amp; Routing Machine",
        "hero_subtitle": "Heavy-duty benchtop CNC machine with travel speeds up to 166 mm/sec (10,000 mm/min), spindle options up to 60,000 RPM 1.5 kW, closed-loop AC servo drives, pneumatic button-press ATC, and 300 × 300 mm working envelope for demanding R&D labs and fast-turnaround batch pilot runs.",
        "in_brief": "The CyTOS CNC 3030 bridges the gap between desktop rapid prototyping and high-throughput production. With a rigid 250 to 370 kg frame, precision ball screws, and high-frequency electro-spindles up to 60,000 RPM, it easily achieves 0.3 mm track isolation, fine-pitch micro-via drilling, and high-speed PCB outer contour routing.",
        "highlights": [
            {"val": "60,000 RPM", "lbl": "Water-Cooled Spindle"},
            {"val": "300 × 300 mm", "lbl": "Square Working Bed"},
            {"val": "166 mm/sec", "lbl": "Rapid Travel Speed"},
            {"val": "AC Servo", "lbl": "Closed-Loop Motion"}
        ],
        "specs": [
            {"param": "Machine Model", "val": "CyTOS CNC 3030 Heavy Benchtop Precision", "cls": "Standard"},
            {"param": "Working Area (X × Y × Z)", "val": "X: 300 mm × Y: 300 mm × Z: 60 mm", "cls": "Standard"},
            {"param": "Travel Speed", "val": "166 mm/sec (10,000 mm/min) High Speed Traverse", "cls": "High Velocity"},
            {"param": "Spindle Configuration Options", "val": "28k RPM (800W) / 40k RPM (1.5kW) / 60k RPM (1.5kW)", "cls": "Configurable"},
            {"param": "Spindle Cooling", "val": "Water Cooled with Closed-Loop Circulator", "cls": "Standard"},
            {"param": "Drive System Options", "val": "Easy Servo / AC Digital Servo Axis Motors", "cls": "Standard/Opt"},
            {"param": "Tool Change System", "val": "Manual Quick Collet / Pneumatic (Button Press) ATC", "cls": "Configurable"},
            {"param": "Machine Net Weight", "val": "250 kg (Stepper) / 300 kg (Easy Servo) / 370 kg (AC Servo ATC)", "cls": "Heavy Duty"},
            {"param": "Workpiece Clamping", "val": "Dowel Pin Reference Holes + T-Slot Aluminium Bed", "cls": "Standard"},
            {"param": "Min Track Width / Isolation", "val": "0.3 mm (Engraving & Rapid Prototyping)", "cls": "Tested Metric"},
            {"param": "Collet Size Compatibility", "val": "3 mm to 6 mm Industrial Collets", "cls": "Standard"},
            {"param": "Positional Accuracy", "val": "0.05 mm (50 Microns)", "cls": "Laser Verified"},
            {"param": "Repeatability", "val": "±0.05 mm Repeatability", "cls": "Laser Verified"},
            {"param": "Control System", "val": "CyTOS PC-Based Industrial System with Monitor, Keyboard & CPU", "cls": "Included"},
            {"param": "Power Supply", "val": "230V – 240V AC, 16A, 50Hz Standard Workshop Supply", "cls": "Standard"},
            {"param": "Standard Accessories", "val": "Coolant Tank, Dust Collection Shroud, PC Controller & Stand", "cls": "Complete"}
        ],
        "features": [
            "Vibration-absorbing heavy steel frame weighing up to 370 kg for zero-resonance cutting at 60,000 RPM",
            "High-frequency 1.5 kW electro-spindle offering extreme dynamic stiffness and long bearing life during continuous milling",
            "Closed-loop AC digital servo motors delivering rapid positioning speeds up to 166 mm/sec with zero lost steps",
            "Pneumatic button-press quick tool change reduces cutter swap time to less than 5 seconds without wrench hassle",
            "Comprehensive dust collection shroud and chip vacuum arrangement keeping sensitive optical scales and bearings clean"
        ],
        "materials": [
            {"mat": "FR4 Double Sided Copper Clad", "status": "Optimal", "speed": "40,000 – 60,000 RPM", "notes": "Rapid 166 mm/sec routing and clean micro-via drilling"},
            {"mat": "High-Tg Multilayer FR4 Boards", "status": "Optimal", "speed": "45,000 – 60,000 RPM", "notes": "No resin smear or delamination under high feed rates"},
            {"mat": "Aluminium Sheet & MCPCB Plates", "status": "Optimal", "speed": "24,000 – 35,000 RPM", "notes": "Rigid machine frame enables smooth aluminium plate routing"},
            {"mat": "Brass & Copper Soft Metal Plates", "status": "Capable", "speed": "18,000 – 28,000 RPM", "notes": "Light face milling and engraving with flood/mist coolant"},
            {"mat": "Acrylic & Polycarbonate Panels", "status": "Optimal", "speed": "20,000 – 30,000 RPM", "notes": "Crystal-clear routed edges with single-flute spiral cutters"}
        ],
        "standard_accessories": [
            "Complete Industrial PC Operator Console with High-Resolution Monitor & CPU",
            "Coolant Recirculation Tank with Submersible Pump and Flexible Nozzles",
            "High-Flow Dust Collection Shroud with Industrial Suction Vacuum Hose",
            "Heavy-Duty Machined T-Slot Aluminium Base with Dowel Locating Pins",
            "Precision Tool Height Touch Plate and Automatic Z-Zero Setting Sensor",
            "12-Month Comprehensive On-Site Warranty Across Maharashtra and India"
        ],
        "optional_accessories": [
            "Pneumatic Button-Press Collet Clamping System with Rapid Tool Release",
            "Closed-Loop Refrigerated Spindle Water Chiller with Digital Temperature Display",
            "Optical CCD Vision Camera for Board Edge & Fiducial Alignment",
            "Rotary 4th Axis Attachment for Cylindrical Component Engraving",
            "Full Soundproof Protective Enclosure with Safety Interlock Doors"
        ],
        "faqs": [
            {
                "q": "What makes the CNC 3030 different from the desktop CNC 3020?",
                "a": "While the CNC 3020 is a lightweight 60 kg desktop machine designed for lab prototyping, the CNC 3030 is a heavy-duty 250 to 370 kg industrial benchtop system. It features faster travel speeds (166 mm/sec vs 100 mm/sec), higher-power spindles (1.5 kW up to 60,000 RPM), and AC servo motor options, making it capable of both prototyping and small-batch production."
            },
            {
                "q": "Can the CNC 3030 machine aluminium and brass plates?",
                "a": "Yes. Thanks to its heavy structural steel frame and rigid C5 ball screws, the CNC 3030 easily machines non-ferrous soft metals such as aluminium, brass, and copper busbars for electrical panels and heat sinks using appropriate feed rates and mist coolant."
            },
            {
                "q": "What spindle options are available on the CNC 3030?",
                "a": "We offer three primary configurations: 28,000 RPM 800W air-cooled spindle (Stepper drive), 40,000 RPM 1.5 kW water-cooled spindle (Easy Servo), and 60,000 RPM 1.5 kW high-frequency electro-spindle with pneumatic ATC (Digital AC Servo)."
            },
            {
                "q": "How does the pneumatic tool change function?",
                "a": "With the pneumatic button-press ATC collet option, the operator presses a quick-release push button on the spindle head to release the tool collet pneumatically in 2 seconds, eliminating wrench slippage and collet runout errors."
            },
            {
                "q": "Where can we see a live demonstration of the CNC 3030?",
                "a": "You are welcome to visit our manufacturing works at J-153, MIDC Bhosari in Pune. You can bring your component drawings or sample PCB material for a live trial run and cycle time test."
            }
        ]
    },
    {
        "id": "pcb12",
        "path": "/pcb12-multi-spindle-drilling-machine",
        "jsx_filename": "Pcb12MultiSpindlePage.jsx",
        "name": "CyTOS PCB12 3-Spindle High Throughput PCB Machine",
        "model_code": "CyTOS PCB12 Multi-Spindle",
        "category": "Multi-Spindle PCB Manufacturing",
        "seo_title": "Multi Spindle PCB Drilling Machine - Three Spindle High Volume PCB Production Machine Manufacturer from Pune | CyTOS",
        "meta_desc": "Manufacturer of Three Spindle PCB Drilling Machine (PCB12) - 1200x1200mm working area, 3x synchronized 60,000 RPM spindles for mass production. CyTOS Pune, Maharashtra.",
        "keywords": "Multi Spindle PCB Drilling Machine, Three Spindle PCB Machine, Comber Board Drilling Machine Three Spindle, PCB12 CyTOS Pune, High Volume PCB Production Machine, 3 Spindle CNC Drilling Machine India",
        "image": "/assets/images/machines/pcb12-multi-spindle.png",
        "image_title": "CyTOS PCB12 Three-Spindle High-Throughput PCB Production Drilling Machine, Pune",
        "image_caption": "Large format 1,200 x 1,200 mm 3-spindle synchronized gantry drilling 3 full-size panels simultaneously for 3X output.",
        "additional_images": [
            {
                "url": "/assets/images/machines/pcb-drilling-pcb60.png",
                "title": "Industrial Touch Console and Spindle Chiller Unit, Pune",
                "caption": "Precision multi-axis synchronization controller with independent Z-axis depth calibration."
            },
            {
                "url": "/assets/images/machines/pcb-cnc-cabinet.png",
                "title": "Multi-Spindle Servo Inverter Drive Cabinet, Pune",
                "caption": "Independent inverter drives for each high-frequency electro-spindle with optical sync."
            }
        ],
        "badge": "3X MASS PRODUCTION THROUGHPUT",
        "hero_title": "CyTOS PCB12 3-Spindle High Throughput PCB Machine",
        "hero_subtitle": "Large-format 1,200 × 1,200 mm multi-spindle CNC drilling and routing machine equipped with three synchronized 40,000 to 60,000 RPM high-frequency electro-spindles with independent pitch control, delivering 300% throughput scaling for high-volume commercial PCB fabrication plants.",
        "in_brief": "The CyTOS PCB12 is designed for commercial circuit board manufacturers seeking maximum output per square foot of factory floor. By synchronizing three precision spindles across an expansive 1,200 × 1,200 mm granite/cast-iron bed, the machine drills three identical panels concurrently, slashing per-panel cycle times by 66%.",
        "highlights": [
            {"val": "3 Spindles", "lbl": "Synchronized Heads"},
            {"val": "1200 × 1200 mm", "lbl": "Large-Format Bed"},
            {"val": "60,000 RPM", "lbl": "Per Spindle Speed"},
            {"val": "300%", "lbl": "Throughput Scaling"}
        ],
        "specs": [
            {"param": "Machine Architecture", "val": "Heavy-Duty Floor Gantry with Cast Iron / Granite Vibration Base", "cls": "Massive Rigidity"},
            {"param": "Overall Working Envelope", "val": "1,200 mm × 1,200 mm (Accommodates Multiple Standard Panels)", "cls": "Standard"},
            {"param": "Spindle Configuration", "val": "3 Synchronized Electro-Spindles with Independent Pitch Spacing", "cls": "3-Spindle Sync"},
            {"param": "Spindle RPM Range", "val": "40,000 RPM to 60,000 RPM High Frequency Inverter Cont.", "cls": "High Velocity"},
            {"param": "Minimum Micro-Drill Dia", "val": "0.25 mm Micro-Hole Drilling in Multilayer FR4", "cls": "Tested Metric"},
            {"param": "Maximum Routing Collet", "val": "3.175 mm (1/8\") and 4.0 mm ER11 Precision Collets", "cls": "Standard"},
            {"param": "Rapid Traverse Velocity", "val": "Up to 15,000 mm/min High Speed Axis Motion", "cls": "High Velocity"},
            {"param": "Drilling Hit Rate", "val": "Up to 3 × 160 hits/min (480 hits/min combined rate)", "cls": "Mass Production"},
            {"param": "Positional Accuracy", "val": "±0.015 mm over 1,200 mm Stroke (Laser Interferometer Verified)", "cls": "Laser Verified"},
            {"param": "Repeatability", "val": "±0.008 mm (8 Microns)", "cls": "Laser Verified"},
            {"param": "Drive System", "val": "High-Torque Delta / Yaskawa AC Servo Motors on All Axes", "cls": "Industrial Grade"},
            {"param": "Guideway System", "val": "Heavy-Duty THK / HIWIN Ground Linear Motion Guides", "cls": "Standard"},
            {"param": "Tool Clamping", "val": "Multi-Head Pneumatic Quick Clamp with Safety Pressure Sensors", "cls": "Standard"},
            {"param": "Registration Alignment", "val": "Multi-Camera CCD Fiducial Vision Alignment System", "cls": "Optical Vision"},
            {"param": "Workpiece Hold-Down", "val": "High-Pressure Multi-Zone Vacuum Bed with Independent Clamps", "cls": "Dual System"},
            {"param": "CNC Controller", "val": "CyTOS Industrial Multi-Axis Synchronized CNC Core with Dual Core DSP", "cls": "Proprietary"},
            {"param": "Electrical Power", "val": "415V AC, 3-Phase, 50Hz, 7.5 kW Connected Load", "cls": "Standard"}
        ],
        "features": [
            "Triple-spindle synchronized motion cuts batch processing time by 66% compared to conventional single-head CNC machines",
            "Independent Z-axis depth offsets and dynamic surface touch probing ensure consistent hole wall quality across all three panels",
            "Heavy stress-relieved steel and cast iron structure dampens all harmonic vibrations generated at 60,000 RPM",
            "Multi-camera optical fiducial recognition automatically detects board stretch, shrinkage, and rotation across all three stations",
            "High-capacity vacuum hold-down bed securely clamps warped or thin copper laminates without mechanical distortion"
        ],
        "materials": [
            {"mat": "Standard FR4 Panels (Single/Double Sided)", "status": "Optimal", "speed": "45,000 – 60,000 RPM", "notes": "3x panels drilled concurrently with zero burr"},
            {"mat": "High-Layer Count Multilayer FR4 (up to 16L)", "status": "Optimal", "speed": "50,000 – 60,000 RPM", "notes": "Precise pecking depth prevents drill wander in thick boards"},
            {"mat": "Aluminium Core MCPCB Panels (LED Lighting)", "status": "Optimal", "speed": "30,000 – 40,000 RPM", "notes": "Simultaneous 3-panel routing with mist cooling"},
            {"mat": "Comber Board & Heavy Industrial Boards", "status": "Optimal", "speed": "35,000 – 50,000 RPM", "notes": "High hit rate and rigid spindle taper for thick industrial sheets"},
            {"mat": "CEM-1 & Paper Phenolic Laminates", "status": "Optimal", "speed": "40,000 – 55,000 RPM", "notes": "Extreme cost-per-hole efficiency in high-volume runs"}
        ],
        "standard_accessories": [
            "Industrial 3-Spindle CNC Operator Workstation with Touchscreen & CAM Software",
            "Heavy-Duty Multi-Zone High Vacuum Clamping Bed with Rotary Vane Pump",
            "Dedicated Closed-Loop Industrial Spindle Refrigeration Chiller Unit",
            "Triple-Channel High-Volume Swarf Evacuation & Dust Collection Shroud",
            "Optical CCD Vision Camera System with Multi-Fiducial Recognition",
            "12-Month Comprehensive Pan-India Warranty and Operator Training in Pune"
        ],
        "optional_accessories": [
            "Independent Spindle Pitch Adjustment Servo Mechanism",
            "Automated Optical Tool Breakage Detection with High-Speed Laser Beams",
            "HEPA Fine Particulate Air Exhaust Filtration System for Cleanrooms",
            "Annual Comprehensive Maintenance Contract (AMC) with Guaranteed 4-Hour Response"
        ],
        "faqs": [
            {
                "q": "How does the three-spindle synchronization work on the CyTOS PCB12?",
                "a": "All three spindles are mounted on a shared rigid gantry and move synchronously along the X and Y axes, while each spindle features independent fine Z-axis depth adjustment. When drilling panel arrays, all three spindles hit identical coordinates at the same time, producing 3 panels in the time of 1."
            },
            {
                "q": "Can the distance (pitch) between the three spindles be adjusted?",
                "a": "Yes. The spindle pitch is mechanically adjustable across precision locating pins, allowing you to configure spindle spacing to match your standard panel dimensions (e.g., 300 mm, 350 mm, or 400 mm panel widths)."
            },
            {
                "q": "What is the combined drilling hit rate of the PCB12?",
                "a": "At full production speed, each spindle achieves up to 160 hits/min on standard FR4 panels, resulting in a combined hit rate of up to 480 hits/min across the three active panels."
            },
            {
                "q": "What power and air utilities are needed at our facility?",
                "a": "The PCB12 requires a 415V AC, 3-Phase, 50Hz electrical supply (7.5 kW connected load) and a dry, oil-free pneumatic air supply at 6 to 7 bar for the collet clamping and swarf pressure foot."
            },
            {
                "q": "How quickly can CyTOS deliver and commission the PCB12 in India?",
                "a": "Manufacturing lead time is typically 6 to 8 weeks from our Pune works. Our factory installation team conducts on-site laser leveling, optical camera calibration, test panel drilling, and complete operator training at your plant."
            }
        ]
    },
    {
        "id": "cnc-routers",
        "path": "/cnc-wood-acrylic-aluminium-router-machine",
        "jsx_filename": "CncWoodAcrylicAluminiumRouterPage.jsx",
        "name": "High Accuracy CNC Router Machine (Wood, Acrylic & Aluminium)",
        "model_code": "CyTOS Heavy Router Series",
        "category": "Industrial CNC Routers & Milling",
        "seo_title": "CNC Router Machine - Heavy Duty Industrial Router for Aluminium, Acrylic & Wood Manufacturer from Pune | CyTOS",
        "meta_desc": "Manufacturer of Heavy-Duty CNC Router Machine for Wood, Acrylic, Aluminium & Soft Metals - 4x4, 8x4, 10x5 ft beds, multi-spindle & vacuum table. CyTOS Pune, Maharashtra.",
        "keywords": "CNC Router Machine Pune, Industrial CNC Router Manufacturer, CNC Wood Router Pune, Aluminium CNC Router Machine, Acrylic CNC Cutting Machine, Heavy Duty Gantry Router India, CyTOS Bhosari",
        "image": "/assets/images/machines/cnc-router-gantry.png",
        "image_title": "Heavy-Duty Industrial CNC Gantry Router for Aluminium and Wood, Pune, India",
        "image_caption": "CyTOS heavy-duty stress-relieved gantry router with 24,000 RPM high-torque spindle, vacuum matrix bed, and AC servo drives.",
        "additional_images": [
            {
                "url": "/assets/images/machines/cnc-router-workshop.png",
                "title": "CyTOS CNC Router Production Floor Bhosari MIDC, Pune",
                "caption": "Precision assembly and laser alignment of large-format 8x4 and 10x5 ft router frames."
            },
            {
                "url": "/assets/images/machines/cnc-router-acrylic.jpg",
                "title": "Clean Acrylic and Aluminium CNC Profile Machining, Pune",
                "caption": "Vibration-free 3D engraving and burr-free edge finish on heavy composite and soft metal sheets."
            }
        ],
        "badge": "HEAVY STRESS-RELIEVED STEEL GANTRY",
        "hero_title": "High Accuracy CNC Router Machine (Wood, Acrylic &amp; Aluminium)",
        "hero_subtitle": "Industrial heavy-duty gantry CNC routers engineered with normalized tubular steel frames, 24,000 RPM high-torque spindles up to 6.5 kW / 9 kW HSD, multi-zone vacuum beds, and bed sizes from 4×4 ft to 10×10 ft (1 to 5 spindles) for non-stop routing of aluminium, brass, wood, acrylic, and composite sheets.",
        "in_brief": "The CyTOS High Accuracy Router Machine is built for manufacturers demanding vibration-free, heavy-duty cutting across wood, acrylic, PVC, bakelite, composites, and soft metals like aluminium and brass. Featuring a stress-relieved tubular steel frame, precision ball screws, helical rack-and-pinion drives, and multi-spindle options, it delivers high dimensional repeatability year after year.",
        "highlights": [
            {"val": "24,000 RPM", "lbl": "High-Torque Spindle"},
            {"val": "8×4 / 10×5 ft", "lbl": "Standard Bed Sizes"},
            {"val": "1 to 5", "lbl": "Spindle Heads (Custom)"},
            {"val": "±0.02 mm", "lbl": "Repeatability"}
        ],
        "specs": [
            {"param": "Machine Frame Structure", "val": "Rigid Stress-Relieved Welded Mild Steel Tubular Gantry", "cls": "Heavy Duty"},
            {"param": "Standard Table Sizes", "val": "4ft × 4ft (1200×1200mm) / 8ft × 4ft (1300×2500mm) / 10ft × 5ft (1500×3000mm)", "cls": "Standard"},
            {"param": "Z-Axis Clearance & Travel", "val": "250 mm to 300 mm Z-Axis Clearance (Customizable to 400 mm)", "cls": "Standard"},
            {"param": "Number of Spindles", "val": "1 to 5 Spindles (Single or Multi-Spindle Custom Configurable)", "cls": "Configurable"},
            {"param": "Spindle Motor Power", "val": "3.5 kW to 6.5 kW (Optional 9.0 kW HSD / Italian High-Torque Spindle)", "cls": "High Torque"},
            {"param": "Spindle RPM Range", "val": "6,000 RPM to 24,000 RPM Continuous Variable Inverter Drive", "cls": "Standard"},
            {"param": "Spindle Cooling Type", "val": "Water Cooled with Circulator / High-Flow Air Cooled", "cls": "Configurable"},
            {"param": "Motion Drive System", "val": "Precision Helical Rack & Pinion (X/Y) + C5 Ground Ball Screw (Z)", "cls": "Standard"},
            {"param": "Motors & Drives", "val": "Leadshine Easy Servo / Delta Digital AC Servo Drives on All Axes", "cls": "Servo Upgrade"},
            {"param": "Traverse & Cutting Speeds", "val": "Rapid: Up to 25,000 mm/min | Cutting: 4,000 to 10,000 mm/min", "cls": "High Speed"},
            {"param": "Table Clamping Surface", "val": "Heavy T-Slot Aluminium + Multi-Zone High Flow Vacuum Matrix Bed", "cls": "Dual System"},
            {"param": "Positional Accuracy", "val": "0.1 mm / 1,000 mm", "cls": "Laser Verified"},
            {"param": "Repeatability", "val": "±0.05 mm (50 Microns)", "cls": "Laser Verified"},
            {"param": "Tool Collet Size", "val": "3 mm to 10 mm (ER20 / ER25 / ER32 Precision Collets)", "cls": "Standard"},
            {"param": "Controller Interface", "val": "PC-Based CyTOS CNC Studio / DSP Handheld / Syntec CNC", "cls": "Industrial"},
            {"param": "Machine Total Weight", "val": "800 kg to 1,050 kg (Heavy Vibration-Absorbing Mass)", "cls": "Solid Mass"},
            {"param": "Power Supply Requirements", "val": "230V – 240V AC, 16A Single Phase or 415V 3-Phase", "cls": "Standard"},
            {"param": "Turnkey Inclusions", "val": "Coolant Pump & Tank, Dual-Bag Dust Collector, Industrial PC & Stand", "cls": "Complete"}
        ],
        "features": [
            "Heavy mild steel tubular gantry normalized and stress-relieved to absorb cutting harmonics and eliminate chatter marks",
            "Multi-zone high-vacuum clamping bed securely holds full 8×4 ft sheets as well as smaller offcuts without mechanical clamps",
            "Precision helical rack and pinion drive on X and Y axes coupled with digital AC servos for smooth, high-speed 25,000 mm/min rapid traverse",
            "Centralized automated lubrication pump continuously oils all linear guideways and ball screws to prevent premature wear",
            "Modular multi-spindle capability (1 to 5 spindles) allowing simultaneous parallel production on multiple identical workpieces"
        ],
        "materials": [
            {"mat": "Aluminium (6061, 5052, 7075) & Brass Plates", "status": "Optimal", "speed": "18,000 – 24,000 RPM", "notes": "Burr-free routing with cold-air mist lubrication"},
            {"mat": "Acrylic (Cast & Extruded) & Polycarbonate", "status": "Optimal", "speed": "18,000 – 22,000 RPM", "notes": "Flame-polish finish edges with single flute spiral cutters"},
            {"mat": "Hardwood, Teak, MDF, Plywood & Solid Wood", "status": "Optimal", "speed": "18,000 – 24,000 RPM", "notes": "Deep 3D carving, furniture profiling, and sign making"},
            {"mat": "Bakelite, FR4 Sheet & Electrical Composites", "status": "Optimal", "speed": "16,000 – 20,000 RPM", "notes": "Dry cutting with dual-bag dust extraction"},
            {"mat": "Aluminium Composite Panels (ACP) & Foam Sheets", "status": "Optimal", "speed": "20,000 – 24,000 RPM", "notes": "V-grooving and folding profiles for architectural cladding"}
        ],
        "standard_accessories": [
            "Complete Industrial Operator Console with PC Controller & Monitor",
            "Multi-Zone High Vacuum Bed with Heavy-Duty Rotary Vane Vacuum Pump",
            "High-Efficiency Dual-Bag Industrial Dust Extraction Collector & Shroud",
            "Automatic Tool Length Touch Sensor and Reference Setting Probe",
            "Mist Coolant Lubrication System for Aluminium and Non-Ferrous Metal Cutting",
            "12-Month Comprehensive Warranty with Pan-India Factory Support"
        ],
        "optional_accessories": [
            "Automatic Tool Changer (ATC) with Linear or Carousel Tool Rack",
            "Italian High-Torque HSD Air-Cooled Spindle (6.5 kW / 9.0 kW)",
            "Multi-Spindle Configuration (2, 3, 4, or 5 Synchronized Spindles)",
            "Vortex Cold Air Gun for Chemical-Free Dry Aluminium Machining",
            "Rotary 4th Axis Lathe Chuck for Columns and Cylindrical 3D Carving"
        ],
        "faqs": [
            {
                "q": "Can the CyTOS CNC Router cut aluminium plates and profiles cleanly?",
                "a": "Yes. CyTOS CNC routers are specially engineered with rigid stress-relieved steel gantries and high-torque spindles to handle aluminium alloys (such as 6061, 5052, and 7075), brass, and copper. Using our mist coolant or vortex cold air attachment, it produces clean, mirror-like edges with zero burr."
            },
            {
                "q": "What bed sizes are available?",
                "a": "Standard bed sizes include 4×4 ft (1200×1200 mm), 8×4 ft (1300×2500 mm), and 10×5 ft (1500×3000 mm). Because we manufacture all machine frames in-house in Pune, we also build custom envelope sizes up to 2000 × 4000 mm upon request."
            },
            {
                "q": "How does the multi-spindle configuration benefit high-volume production?",
                "a": "With 2, 3, or more spindles mounted on the same gantry, you can process multiple identical sheets simultaneously. For example, a 3-spindle router produces three 600×2500 mm parts at once, tripling throughput with a single operator."
            },
            {
                "q": "What vacuum pump is supplied with the vacuum bed?",
                "a": "We provide heavy-duty oil-free or water-ring vacuum pumps (typically 5.5 kW to 7.5 kW) connected to a multi-zone vacuum manifold with individual toggle valves, allowing you to activate vacuum suction only under your active workpiece."
            },
            {
                "q": "What design and CAM software can we use with this machine?",
                "a": "Our PC-based controller accepts standard G-code and M-code generated by any leading CAD/CAM software including Vectric Aspire, ArtCAM, Mastercam, Fusion 360, RhinoCAM, and SolidWorks CAM."
            }
        ]
    },
    {
        "id": "vdm-milling",
        "path": "/vdm-heavy-vertical-drilling-milling-machine",
        "jsx_filename": "VdmHeavyDrillingMillingPage.jsx",
        "name": "VDM Heavy Vertical Drilling & Milling Machine (VDM30M / 50M / 100M)",
        "model_code": "CyTOS VDM Series",
        "category": "Heavy Industrial Metal Machining",
        "seo_title": "VDM Vertical Drilling & Milling Machine - Cast Iron Heavy Metal CNC Machine Manufacturer from Pune | CyTOS",
        "meta_desc": "Manufacturer of VDM Heavy Vertical Drilling & Milling Machine (VDM30M, VDM50M, VDM100M) - 1mm to 50mm drilling, BT30/BT40 taper, Delta CNC controller. CyTOS Pune.",
        "keywords": "VDM Vertical Drilling Machine, CNC Milling Machine Pune, Heavy Drilling Machine Manufacturer, VDM30M VDM50M VDM100M, Switchboard Plate Milling Machine, Cast Iron CNC Machine India, CyTOS Bhosari",
        "image": "/assets/images/machines/vdm-milling-machine.png",
        "image_title": "CyTOS VDM Heavy Vertical Drilling and Milling Machine for MS, SS and Switchboards, Pune",
        "image_caption": "Heavy cast-iron base VDM series vertical drilling and milling machine with BT30/BT40 taper and Delta CNC controller.",
        "additional_images": [
            {
                "url": "/assets/images/machines/precision-machining-parts.png",
                "title": "Rigid Tapped Holes and Enclosure Cutouts, Pune",
                "caption": "Precision milled rectangular cutouts, deep drilled holes, and rigid tapped threads in mild steel and copper busbars."
            },
            {
                "url": "/assets/images/machines/cytos-assembly-floor.png",
                "title": "CyTOS Precision Cast Iron Scraping and Assembly, Pune",
                "caption": "Hand scraping and laser interferometer alignment of heavy cast iron slideways at Bhosari facility."
            }
        ],
        "badge": "HEAVY CAST IRON VIBRATION DAMPENING",
        "hero_title": "VDM Heavy Vertical Drilling &amp; Milling Machine",
        "hero_subtitle": "Rigid cast iron base and square column vertical machining center engineered for electrical control panel builders, switchgear manufacturers, and heavy toolrooms. Models VDM30M, VDM50M, and VDM100M feature 1 mm to 50 mm drilling capacity, rigid tapping (M3 to M20), BT30/BT40 spindles, and Delta CNC controllers.",
        "in_brief": "The CyTOS VDM Series is purpose-built to handle tough metal machining on mild steel (MS), stainless steel (SS304), cast iron, brass, and copper busbars. Featuring heavy cast iron Meehanite structures that absorb cutting vibrations, preloaded HIWIN linear roller rails, and Delta CNC controls, it is the ideal machine for switchboard door cutouts, plate drilling, and deep tapping.",
        "highlights": [
            {"val": "1 to 50 mm", "lbl": "Drilling Capacity"},
            {"val": "BT30 / BT40", "lbl": "Spindle Taper"},
            {"val": "M3 to M20", "lbl": "Rigid Tapping"},
            {"val": "Cast Iron", "lbl": "Meehanite Structure"}
        ],
        "specs": [
            {"param": "Machine Frame Structure", "val": "Heavy High-Grade Cast Iron Base & Square Column Assembly", "cls": "Vibration Absorbing"},
            {"param": "Models in Series", "val": "VDM30M (Compact) | VDM50M (Production) | VDM100M (Heavy Capacity)", "cls": "3 Model Tiers"},
            {"param": "Max Drilling Diameter", "val": "VDM30M: 1-12 mm | VDM50M: 1-25 mm | VDM100M: 1-50 mm", "cls": "Heavy Duty"},
            {"param": "Machining Processes", "val": "Precision Drilling, Rigid Tapping (M3-M20), Boring, Face & End Milling", "cls": "Multi-Function"},
            {"param": "Standard Bed Sizes", "val": "VDM30M: 300×300mm | VDM50M: 500×500mm | VDM100M: 1000×1000mm", "cls": "Standard"},
            {"param": "Spindle Nose Taper", "val": "BT30 / BT40 Mechanical Taper with Mechanical Drawbar", "cls": "Standard"},
            {"param": "Spindle Motor Power", "val": "VDM30M: 1.5 kW (2 HP) | VDM50M: 2.5 kW (3.3 HP) | VDM100M: 3.5 kW (5 HP) Servo", "cls": "High Torque"},
            {"param": "Axis Motor Technology", "val": "Stepper/Easy Servo (VDM30M) | Digital AC Servo Motors (VDM50M / VDM100M)", "cls": "Standard/Servo"},
            {"param": "Guideway System", "val": "Heavy-Duty HIWIN / THK Linear Guideways on All 3 Axes", "cls": "High Precision"},
            {"param": "Foundation Type", "val": "Tabletop (VDM30M) | Heavy Base Floor Mounted (VDM50M & VDM100M)", "cls": "Standard"},
            {"param": "Positional Accuracy", "val": "0.05 mm (50 Microns)", "cls": "Laser Calibrated"},
            {"param": "Coolant System", "val": "High-Pressure Coolant Pump & Sump Tank with Chip Filter (50M & 100M)", "cls": "Included"},
            {"param": "Machine Enclosure", "val": "Open (VDM30M) | Sheet Metal Guarding with Sliding Door (50M & 100M)", "cls": "Enclosed"},
            {"param": "CNC Controller", "val": "PC-Based System (VDM30M) | Delta CNC Industrial Controller (50M & 100M)", "cls": "Industrial Grade"},
            {"param": "Power Supply Requirements", "val": "415V AC, 3-Phase, 50Hz Standard Industrial Connection", "cls": "Standard"}
        ],
        "features": [
            "Heavy Meehanite cast iron structural base engineered to channel and dissipate cutting forces directly into the foundation",
            "High-torque servo spindle drive delivers full torque down to low RPM for heavy 50 mm hole drilling and clean thread tapping up to M20",
            "Precision ground square guideways and HIWIN linear motion rails ensure maximum rigidity under side-load milling operations",
            "Integrated high-pressure flood coolant system with magnetic chip separator keeps cutting edges sharp and components cool",
            "Industrial Delta CNC controller with full conversational programming and G-code execution for rapid setup of cutout arrays"
        ],
        "materials": [
            {"mat": "Mild Steel (MS) Plates & Enclosure Panels", "status": "Optimal", "speed": "800 – 3,000 RPM", "notes": "Heavy slotting, meter cutouts, and hinge mounting holes"},
            {"mat": "Stainless Steel (SS304, SS316)", "status": "Optimal", "speed": "600 – 2,200 RPM", "notes": "Rigid tapping with high-pressure coolant prevents work hardening"},
            {"mat": "Cast Iron Blocks & Machine Castings", "status": "Optimal", "speed": "1,000 – 3,500 RPM", "notes": "Heavy drilling and boring with superior surface finish"},
            {"mat": "Copper & Aluminium Busbars", "status": "Optimal", "speed": "2,500 – 6,000 RPM", "notes": "Fast multi-hole drilling for electrical power distribution panels"},
            {"mat": "Die-Cast Aluminium Enclosures", "status": "Optimal", "speed": "3,000 – 8,000 RPM", "notes": "High speed profiling and cable gland hole tapping"}
        ],
        "standard_accessories": [
            "Delta CNC Industrial Controller with Handwheel (MPG) & Color Screen",
            "High-Pressure Flood Coolant Pump, Tank & Adjustable Dual Nozzles",
            "Centralized Automatic Pulse Lubrication System for Guideways",
            "T-Slot Heavy Cast Iron Machining Bed with Perimeter Coolant Trough",
            "Full Sheet Metal Protective Enclosure with Interlocked Safety Door",
            "12-Month Comprehensive Warranty and Factory Commissioning in India"
        ],
        "optional_accessories": [
            "BT40 Heavy Spindle Taper Upgrade for Face Milling up to 80 mm Cutters",
            "Rotary 4th Axis CNC Indexing Table for Multi-Faceted Part Machining",
            "Air Blast Chip Clearing Nozzle for Dry Cast Iron Machining",
            "Renishaw Workpiece Touch Probe for Automated Part Alignment"
        ],
        "faqs": [
            {
                "q": "What industries typically use the CyTOS VDM machine series?",
                "a": "The VDM series is widely used by electrical switchgear manufacturers, control panel builders, fabrication shops, and automotive toolrooms. It is ideal for milling rectangular meter cutouts, drilling hundreds of terminal holes in enclosure doors, and tapping copper busbars."
            },
            {
                "q": "What is the difference between VDM30M, VDM50M, and VDM100M?",
                "a": "VDM30M is a compact tabletop machine with 300×300 mm bed and 12 mm max drill. VDM50M is a floor-mounted production machine with 500×500 mm bed, 25 mm max drill, and full enclosure. VDM100M is our largest machine with 1000×1000 mm bed, 50 mm max drill, and 3.5 kW AC servo spindle for heavy plates."
            },
            {
                "q": "Can the VDM series perform rigid tapping without a floating tap holder?",
                "a": "Yes. The VDM50M and VDM100M feature synchronized spindle and Z-axis servo interpolation, allowing rigid tapping from M3 up to M20 threads with standard solid collet holders without requiring expensive tension-compression floating tap heads."
            },
            {
                "q": "How does cast iron construction compare with fabricated sheet frames?",
                "a": "Meehanite cast iron has over 10 times the natural vibration dampening capacity of fabricated sheet steel. This prevents chatter during heavy milling, extends cutting tool life, and maintains positional accuracy across years of heavy use."
            },
            {
                "q": "What controller is used on the VDM series?",
                "a": "The VDM50M and VDM100M are powered by industrial Delta CNC controllers with dedicated digital servo drives, electronic handwheels (MPG), and conversational canned drilling/tapping cycles."
            }
        ]
    },
    {
        "id": "foam-welding",
        "path": "/foam-welding-machine",
        "jsx_filename": "FoamWeldingMachinePage.jsx",
        "name": "Automatic Thermal Foam Welding Machine",
        "model_code": "CyTOS Foam Welder",
        "category": "Packaging & Foam Automation",
        "seo_title": "Automatic Foam Welding Machine - Thermal Packaging & Foam Fabrication Machine Manufacturer from Pune | CyTOS",
        "meta_desc": "Manufacturer of Automatic Foam Welding Machine - High speed automated thermal welding for packaging and industrial foam fabrication. Direct factory from CyTOS Pune.",
        "keywords": "Automatic Foam Welding Machine, Thermal Foam Welding Machine, Foam Welding Machine Manufacturer Pune, Packaging Foam Machine, EPE Foam Welding Machine India, Industrial Foam Fabrication CyTOS",
        "image": "/assets/images/machines/foam-welding-machine.png",
        "image_title": "Automatic Thermal Foam Welding Machine for Industrial Packaging, Pune, India",
        "image_caption": "CyTOS automatic thermal foam welding machine with digital temperature control and pneumatic clamping platen.",
        "additional_images": [
            {
                "url": "/assets/images/machines/cytos-assembly-floor.png",
                "title": "CyTOS Packaging Automation Machine Assembly Floor, Pune",
                "caption": "Precision assembly and thermal calibration of mass production foam welding fixtures."
            },
            {
                "url": "/assets/images/machines/spm-automation-cell.jpg",
                "title": "Automated Pneumatic Actuation and Safety Interlocks, Pune",
                "caption": "Integrated PLC stroke timing and safety light curtains for high-speed cycle times."
            }
        ],
        "badge": "MASS PRODUCTION FOAM AUTOMATION",
        "hero_title": "Automatic Thermal Foam Welding Machine",
        "hero_subtitle": "Specialized high-speed automated thermal foam welding system engineered for packaging converters, automotive cushioning, and industrial foam fabrication. Features digital temperature control, automated pneumatic platen stroke, precision ball screws, and custom sizing options.",
        "in_brief": "The CyTOS Foam Welding Machine is purpose-built for the packaging and foam handling industry. Replacing slow, toxic adhesive gluing and manual hot-air guns, it uses precision thermal heating elements and automatic stroke timing to thermally fuse PE, EPE, EVA, and polyurethane foam inserts in seconds with unbreakable seams.",
        "highlights": [
            {"val": "5 to 15 s", "lbl": "Fast Cycle Time"},
            {"val": "Digital PID", "lbl": "Temp Control"},
            {"val": "Zero Glue", "lbl": "Thermal Fusion"},
            {"val": "100% Bond", "lbl": "Weld Strength"}
        ],
        "specs": [
            {"param": "Machine Category", "val": "Automatic Industrial Thermal Foam Welding Machine", "cls": "Turnkey"},
            {"param": "Frame Construction", "val": "High-Grade Aluminium & Structural Steel Tubular Frame", "cls": "Rigid Structure"},
            {"param": "Motion Mechanism", "val": "Precision Linear Guideways & Ball Screw Platen Actuation", "cls": "Smooth Motion"},
            {"param": "Platen Heating System", "val": "Uniform PID-Controlled Thermal Heating Plate / Wire Array", "cls": "Precision Heating"},
            {"param": "Temperature Range", "val": "50°C to 300°C Digital Closed-Loop Control", "cls": "Variable"},
            {"param": "Platen Size", "val": "Standard 600×400 mm (Customizable up to 1500×1000 mm)", "cls": "Customizable"},
            {"param": "Actuation & Clamping", "val": "Pneumatic Cylinders with Dual Pressure Regulators", "cls": "Pneumatic"},
            {"param": "Cycle Time Target", "val": "Typically 5 to 15 seconds per completed weld cycle", "cls": "High Throughput"},
            {"param": "Control Interface", "val": "Touchscreen HMI / Digital Timer & Temperature Console", "cls": "Easy Operation"},
            {"param": "Safety Interlocks", "val": "Dual-Hand Safety Anti-Tie-Down Buttons & Emergency Stop", "cls": "CE Standard"},
            {"param": "Power Supply", "val": "230V AC Single Phase or 415V 3-Phase (4 to 8 kW Heating)", "cls": "Standard"}
        ],
        "features": [
            "Eliminates expensive hot-melt glues, solvent-based adhesives, and toxic VOC emissions from your packaging assembly floor",
            "Digital closed-loop PID temperature controller guarantees uniform heat distribution across the entire welding platen surface",
            "Synchronized pneumatic stroke actuation ensures uniform contact pressure and prevents foam crushing or uneven seams",
            "Two-hand safety start control and light curtain option ensure complete operator hand safety during downward platen stroke",
            "Custom-engineered heating platen profiles and interchangeable locating nests allow rapid retooling between different box designs"
        ],
        "materials": [
            {"mat": "EPE (Expanded Polyethylene) Foam Sheets", "status": "Optimal", "speed": "5 – 10 sec cycle", "notes": "Permanent molecular bond without glue residue"},
            {"mat": "EVA (Ethylene Vinyl Acetate) Tool Trays", "status": "Optimal", "speed": "8 – 15 sec cycle", "notes": "Clean multi-layer laminated tool & instrument inserts"},
            {"mat": "XLPE (Cross-Linked Polyethylene) Foam", "status": "Optimal", "speed": "10 – 15 sec cycle", "notes": "High aesthetic finish for luxury packaging & medical boxes"},
            {"mat": "Polyurethane (PU) Cushioning Inserts", "status": "Capable", "speed": "10 – 18 sec cycle", "notes": "Thermal fusing of complex geometric corners and partitions"},
            {"mat": "Foam-to-Corrugated Plastic (PP Bubble Guard)", "status": "Capable", "speed": "8 – 14 sec cycle", "notes": "Thermal bonding for reusable returnable dunnage boxes"}
        ],
        "standard_accessories": [
            "Complete Automatic Foam Welding Machine Unit with Digital HMI Console",
            "Pneumatic Air Filter-Regulator-Lubricator (FRL) Unit with Pressure Gauge",
            "Interchangeable Heat-Resistant Non-Stick Teflon Platen Cover",
            "Two-Hand Safety Anti-Tie-Down Operator Trigger Panel",
            "12-Month Comprehensive Factory Warranty from CyTOS Pune"
        ],
        "optional_accessories": [
            "Custom CNC-Machined Locating Jigs for Complex Foam Contours",
            "Optical Safety Light Curtains for Automated Cycle Triggering",
            "Extended Bed Platen Sizes (up to 1500 × 1000 mm for Large Boxes)",
            "Automated Pneumatic Slide-Out Drawer Table for Fast Loading/Unloading"
        ],
        "faqs": [
            {
                "q": "What types of foam can be welded on this machine?",
                "a": "The CyTOS Foam Welding Machine handles EPE (Expanded Polyethylene), EVA, XLPE (Cross-Linked Polyethylene), and polyurethane foams commonly used in electronics cushioning, tool trays, returnable automotive dunnage, and medical packaging."
            },
            {
                "q": "How does thermal welding compare with hot-melt glue?",
                "a": "Thermal welding melts the contact surfaces of the foam slightly and presses them together to create a permanent molecular bond that is as strong as the virgin material. Unlike glue, it costs zero rupees in consumables, eliminates glue strings, avoids toxic solvent smells, and is 100% recyclable."
            },
            {
                "q": "Can the platen size be customized for our specific packaging boxes?",
                "a": "Yes. While our standard platen is 600 × 400 mm, we custom engineer platen sizes up to 1,500 × 1,000 mm with multi-zone heating elements to fit your largest packaging formats."
            },
            {
                "q": "What is the typical production speed?",
                "a": "A typical welding cycle takes between 5 to 15 seconds depending on the foam density and thickness, allowing an operator to produce 200 to 400 finished welded foam assemblies per hour."
            }
        ]
    },
    {
        "id": "educational-cnc",
        "path": "/educational-cnc-machines",
        "jsx_filename": "EducationalCncPage.jsx",
        "name": "Educational & Training CNC Machines",
        "model_code": "CyTOS EduCNC Series",
        "category": "Educational & Institutional CNC",
        "seo_title": "Educational CNC Machines - Desktop & Benchtop Training CNC Machine Manufacturer from Pune | CyTOS",
        "meta_desc": "Manufacturer of Educational CNC Machines - Compact training CNC milling, router, and PCB machines with safety enclosures for engineering colleges and labs. CyTOS Pune.",
        "keywords": "Educational CNC Machines Pune, Training CNC Machine India, Desktop CNC Trainer for Colleges, Student CNC Milling Machine, Polytehnic CNC Lab Equipment, CyTOS Educational Machines",
        "image": "/assets/images/machines/educational-cnc-lab.png",
        "image_title": "Educational & Training CNC Machine Lab Workcell for Engineering Colleges, Pune",
        "image_caption": "Compact, fully enclosed educational CNC trainer machine featuring safety interlocks and PC-based G-code simulation for polytechnics and universities.",
        "additional_images": [
            {
                "url": "/assets/images/machines/pcb-prototyping-pcb30.png",
                "title": "Chemical-Free Student PCB Prototyping Trainer, Pune",
                "caption": "Safe tabletop isolation milling and circuit fabrication workstation designed for student electronics labs."
            },
            {
                "url": "/assets/images/machines/precision-machining-parts.png",
                "title": "Student CNC Milling Project Samples, Pune",
                "caption": "3D engraved badges, nameplates, aluminium components, and circuit boards fabricated by students."
            }
        ],
        "badge": "COLLEGE & INSTITUTIONAL TRAINER",
        "hero_title": "Educational &amp; Training CNC Machines",
        "hero_subtitle": "Compact, robust, and safe CNC machine tools engineered specifically for engineering colleges, polytechnics, ITIs, and skill development centres. Features full transparent safety enclosures, door interlocks, PC-based CNC simulation software, and curriculum packages for teaching G-code programming, 3D routing, and PCB fabrication.",
        "in_brief": "The CyTOS Educational CNC Series bridges academic theory and real-world industrial practice. Built with the same precision ball screws, linear guides, and controllers as our factory production machines, it provides students with hands-on machining experience in a safe, quiet, and clean laboratory environment.",
        "highlights": [
            {"val": "100% Safe", "lbl": "Enclosed Design"},
            {"val": "G & M Code", "lbl": "Standard NC Control"},
            {"val": "PC Based", "lbl": "Simulation & CAM"},
            {"val": "Turnkey", "lbl": "Lab Curriculum"}
        ],
        "specs": [
            {"param": "Machine Category", "val": "Educational Benchtop CNC Machining & Prototyping Trainer", "cls": "Academic"},
            {"param": "Working Envelope", "val": "300 × 200 × 60 mm / 300 × 300 × 80 mm", "cls": "Standard"},
            {"param": "Safety Housing", "val": "360° Transparent Polycarbonate Enclosure with Door Safety Interlock", "cls": "100% Safe"},
            {"param": "Spindle Motor", "val": "800W to 1.5 kW Precision High-Speed Spindle (up to 40,000 RPM)", "cls": "Variable"},
            {"param": "Motion Mechanisms", "val": "Hardened Linear Guideways & C7 Precision Ball Screws", "cls": "Industrial Grade"},
            {"param": "Drive Motors", "val": "Micro-Step Stepper Motors / Easy Servo Closed-Loop Drives", "cls": "Standard"},
            {"param": "Accuracy & Repeatability", "val": "±0.05 mm (Demonstrates Real Industrial Tolerances)", "cls": "Precision"},
            {"param": "Operating Software", "val": "CyTOS EduCAM Studio with Real-Time 3D Toolpath Simulation", "cls": "Included"},
            {"param": "Supported Languages", "val": "Standard ISO G-Code and M-Code (Fanuc & Siemens compatible syntax)", "cls": "Universal"},
            {"param": "Workpiece Clamping", "val": "T-Slot Aluminium Bed with Quick-Action Mechanical Clamps", "cls": "Standard"},
            {"param": "Noise Level", "val": "Under 65 dB (Classroom Friendly Operation)", "cls": "Quiet"},
            {"param": "Power Supply", "val": "Standard 230V AC Single Phase Domestic Wall Plug (No Industrial 3-Phase Required)", "cls": "Plug & Play"}
        ],
        "features": [
            "Complete physical safety with transparent shatterproof polycarbonate enclosure and emergency interlock that cuts spindle power if doors open",
            "Real-world industrial controller interface teaching students authentic G-code, tool offsets, work coordinates (G54-G59), and feed rate overrides",
            "3D graphic toolpath preview and virtual collision simulation before cutting, eliminating accidental tool crashes and student mistakes",
            "Versatile multi-material machining capability: students can prototype electronics PCBs, 3D wood sculptures, acrylic signs, and aluminium brackets",
            "Comprehensive turnkey delivery: includes student lab exercises, faculty training workshops, and ongoing curriculum support"
        ],
        "materials": [
            {"mat": "PCB Copper-Clad Laminates (FR4)", "status": "Optimal", "speed": "24,000 – 40,000 RPM", "notes": "Chemical-free student circuit design and fabrication"},
            {"mat": "Aluminium (6061) & Brass Ingots", "status": "Optimal", "speed": "18,000 – 24,000 RPM", "notes": "Teaches metal cutting speeds, chip loads, and feeds"},
            {"mat": "Acrylic & Polycarbonate Sheets", "status": "Optimal", "speed": "16,000 – 22,000 RPM", "notes": "Engraving, optical lens machining, and light guide signs"},
            {"mat": "Wood, MDF & Modeling Foam", "status": "Optimal", "speed": "18,000 – 24,000 RPM", "notes": "Rapid 3D surface contouring and industrial design models"},
            {"mat": "Delrin, Nylon & Engineering Plastics", "status": "Optimal", "speed": "16,000 – 20,000 RPM", "notes": "Mechanical gears, robot chassis, and mechanical parts"}
        ],
        "standard_accessories": [
            "Complete Benchtop CNC Machine with Safety Enclosure and E-Stop",
            "Pre-Configured Operator PC with CyTOS EduCAM Software & Simulation",
            "Starter Tooling Package (End Mills, V-Carve Bits, Ball Nose, Micro-Drills)",
            "Mechanical Clamping Kit, T-Nuts, and Precision Workpiece Vise",
            "Faculty Training Session Conducted by CyTOS Application Engineers",
            "12-Month Institutional Warranty and Technical Phone/Email Support"
        ],
        "optional_accessories": [
            "Rotary 4th Axis Attachment for Teaching 4-Axis Simultaneous Machining",
            "Automated Surface Touch Probe for Auto Z-Zero Leveling Demonstration",
            "Compact Laboratory HEPA Dust Extractor with Anti-Static Hose",
            "Annual Institutional Maintenance & Faculty Refresher Training Contract"
        ],
        "faqs": [
            {
                "q": "Why should colleges invest in CyTOS Educational CNC machines over consumer CNC kits?",
                "a": "Consumer hobby kits use weak 3D-printed parts, belt drives, and unstable open-source controllers that break quickly under student use. CyTOS Educational machines are built with genuine industrial ball screws, linear guides, and steel frames, offering real industrial reliability, accuracy, and Fanuc/Siemens-compatible G-code syntax."
            },
            {
                "q": "What training is provided for faculty and lab assistants?",
                "a": "We conduct an extensive hands-on faculty training program upon installation. Our engineers guide instructors through machine operation, safety protocols, CAD-to-CAM workflow, tooling selection, and troubleshooting so faculty can confidently teach student batches."
            },
            {
                "q": "Is special three-phase power or compressed air needed in the lab?",
                "a": "No. The CyTOS Educational CNC machine runs on standard 230V AC single-phase power from a regular domestic socket, requiring no special electrical substation or high-pressure plant air."
            },
            {
                "q": "Can students use standard CAD/CAM software like Fusion 360 or SolidWorks?",
                "a": "Yes. CyTOS EduCAM accepts standard G-code exported from Autodesk Fusion 360, SolidWorks, Mastercam, Creo, NX, and EDA packages like Altium, KiCad, and Eagle."
            }
        ]
    }
]

print(f"Loaded {len(MACHINE_PRODUCTS)} comprehensive machine product models.")
