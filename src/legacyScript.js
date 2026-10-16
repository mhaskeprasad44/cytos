// Central Lead Dispatcher & LocalStorage Vault
async function dispatchEmailToInranktech(payload) {
  // 1. Vault lead locally immediately so no inquiry is ever lost
  try {
    const existing = JSON.parse(localStorage.getItem('cytos_saved_leads') || '[]');
    existing.push({
      timestamp: new Date().toISOString(),
      ...payload
    });
    localStorage.setItem('cytos_saved_leads', JSON.stringify(existing));
    console.log('[CyTOS] Inquiry securely saved to local vault:', payload);
  } catch (storageErr) {
    console.warn('[CyTOS] LocalStorage vault warning:', storageErr);
  }

  // 2. Primary Dispatch: Server-Side Hostinger PHP Mailer (/api/contact.php)
  let phpSuccess = false;
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 4000);
    const res = await fetch('/api/contact.php', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      signal: controller.signal,
      body: JSON.stringify(payload)
    });
    clearTimeout(timeoutId);
    if (res.ok) {
      phpSuccess = true;
      console.log('[CyTOS] Lead successfully delivered via /api/contact.php');
    }
  } catch (phpErr) {
    console.warn('[CyTOS] /api/contact.php notice (fallback active):', phpErr.message || phpErr);
  }

  // 3. Redundant Backup Dispatch: FormSubmit to cytospune@gmail.com and CC inranktech@gmail.com
  try {
    const controller2 = new AbortController();
    const timeoutId2 = setTimeout(() => controller2.abort(), 4000);
    fetch('https://formsubmit.co/ajax/cytospune@gmail.com', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      signal: controller2.signal,
      body: JSON.stringify({
        _subject: payload._subject || 'New CyTOS Machinery Inquiry',
        _cc: 'inranktech@gmail.com',
        _captcha: 'false',
        _template: 'table',
        ...payload
      })
    }).then(r => r.json()).then(d => {
      console.log('[CyTOS] FormSubmit backup status:', d);
    }).catch(fsErr => {
      console.warn('[CyTOS] FormSubmit backup note:', fsErr.message || fsErr);
    }).finally(() => {
      clearTimeout(timeoutId2);
    });
  } catch (err) {
    console.warn('[CyTOS] Background mailer note:', err.message || err);
  }

  return true;
}

export function initAllPageScripts() {
  initHeroSlider();
  initMachineFinder();
  initReviewsSlider();
  initRoiCalculator();
  initProductTabs();
  initApplicationFilter();
  initFaqAccordion();
  initRfqModal();
  initMetricCounters();
  initStickyHeader();
  initMobileNav();
  initContactForm();
  initConsentBanner();
  initBlogFilter();
  initTermsToc();
  initVideoShowcase();
  checkSubmissionStatus();
}

function checkSubmissionStatus() {
  try {
    const params = new URLSearchParams(window.location.search);
    if (params.get('submitted') || params.get('rfq_submitted') || params.get('status') === 'success') {
      alert('Thank you! Your Technical Inquiry has been received. Our Pune engineering desk (info@cytos.in) will review your specifications and respond within 2 business hours.');
    }
  } catch (e) {
    // Ignore URL search param parsing errors
  }
}

/* ==========================================================================
   1. Hero Section Interactive Slider
   ========================================================================== */
function initHeroSlider() {
  const slides = document.querySelectorAll('.hero-slide');
  const tabs = document.querySelectorAll('.slider-tab-btn');
  const prevBtn = document.getElementById('sliderPrevBtn');
  const nextBtn = document.getElementById('sliderNextBtn');
  const sliderContainer = document.querySelector('.hero-slider-container');
  
  if (!slides.length) return;

  let currentSlide = 0;
  const slideCount = slides.length;
  const slideIntervalDuration = 5000;
  let slideTimer = null;

  function showSlide(index) {
    if (index < 0) index = slideCount - 1;
    if (index >= slideCount) index = 0;

    currentSlide = index;

    slides.forEach((slide, i) => {
      slide.classList.toggle('active', i === currentSlide);
    });

    const counterCurrent = document.getElementById('sliderCounterCurrent');
    const counterTotal = document.getElementById('sliderCounterTotal');
    if (counterCurrent) counterCurrent.textContent = String(currentSlide + 1).padStart(2, '0');
    if (counterTotal) counterTotal.textContent = String(slideCount).padStart(2, '0');

    tabs.forEach((tab, i) => {
      tab.classList.toggle('active', i === currentSlide);
      const progressBar = tab.querySelector('.tab-progress-line');
      if (progressBar) {
        progressBar.style.transition = 'none';
        progressBar.style.width = '0%';
        if (i === currentSlide) {
          setTimeout(() => {
            progressBar.style.transition = `width ${slideIntervalDuration}ms linear`;
            progressBar.style.width = '100%';
          }, 30);
        }
      }
    });
  }

  function startAutoSlide() {
    stopAutoSlide();
    showSlide(currentSlide);
    slideTimer = setInterval(() => {
      showSlide((currentSlide + 1) % slideCount);
    }, slideIntervalDuration);
  }

  function stopAutoSlide() {
    if (slideTimer) {
      clearInterval(slideTimer);
      slideTimer = null;
    }
  }

  if (prevBtn) {
    prevBtn.onclick = (e) => {
      e.preventDefault();
      showSlide((currentSlide - 1 + slideCount) % slideCount);
      startAutoSlide();
    };
  }

  if (nextBtn) {
    nextBtn.onclick = (e) => {
      e.preventDefault();
      showSlide((currentSlide + 1) % slideCount);
      startAutoSlide();
    };
  }

  tabs.forEach((tab, index) => {
    tab.onclick = () => {
      showSlide(index);
      startAutoSlide();
    };
  });

  startAutoSlide();
}

/* ==========================================================================
   2. Machine & Feasibility Finder
   ========================================================================== */
function initMachineFinder() {
  const reqSelect = document.getElementById('finderRequirement');
  const matSelect = document.getElementById('finderMaterial');
  const modelText = document.getElementById('finderModelResult');
  const specsText = document.getElementById('finderSpecsResult');
  const quoteBtn = document.getElementById('finderQuoteBtn');

  if (!reqSelect || !matSelect) return;

  const machineDatabase = {
    'pcb-prod': {
      'fr4': {
        model: 'CyTOS PCB60 Dual-Spindle',
        specs: '600x600mm • 60,000 RPM • 0.2mm Min Drill • 2X Throughput',
        ref: 'PCB60'
      },
      'mcpcb': {
        model: 'CyTOS PCB12 Multi-Spindle High-Power',
        specs: '1200x1200mm • 60,000 RPM • Heavy-Duty Aluminium Core Routing',
        ref: 'PCB12'
      },
      'default': {
        model: 'CyTOS PCB60 / PCB12 Series',
        specs: 'Custom Spindle Count (1-3) • 60,000 RPM Spindles • Auto Tool Change',
        ref: 'PCB-Series'
      }
    },
    'pcb-proto': {
      'fr4': {
        model: 'CyTOS PCB30 Chemical-Free Prototyping',
        specs: '300x300mm • Zero Chemistry • Direct Gerber • 15-Min Turnaround',
        ref: 'PCB30'
      },
      'edu': {
        model: 'CyTOS PCBE3020 Educational CNC Lab System',
        specs: 'Safe Enclosure • Excellon Import • Comprehensive Lab Curriculum',
        ref: 'PCBE3020'
      },
      'default': {
        model: 'CyTOS PCB30 Benchtop Lab Prototyper',
        specs: '0.1mm Track Resolution • Z-Surface Mapping • Gerber RS-274X',
        ref: 'PCB30'
      }
    },
    'cnc-router': {
      'metal': {
        model: 'CyTOS 4x4 Rigid Aluminium Router',
        specs: '1220x1220mm • 24,000 RPM Water-Cooled • AC-Servo • Mist Coolant',
        ref: 'Router-4x4'
      },
      'composite': {
        model: 'CyTOS 8x8 Industrial Heavy Gantry',
        specs: '2440x2440mm • Vacuum Bed Clamping • High-Torque Spindle',
        ref: 'Router-8x8'
      },
      'default': {
        model: 'CyTOS Industrial CNC Router Series',
        specs: 'Custom Bed Dimensions • Rigid Steel Chassis • Safety Factor 2.0',
        ref: 'Router-Series'
      }
    },
    'custom-spm': {
      'fixture': {
        model: 'CyTOS 90° Rotary Pneumatic Weld Fixture',
        specs: 'Pneumatic Clamp • Repeatable Indexing • Eliminates Manual Flipping',
        ref: 'SPM-WeldFixture'
      },
      'dispensing': {
        model: 'CyTOS 6-Axis Robotic Adhesive Cell',
        specs: 'Sunroof & Sealant Dispensing • Automated Component Placement',
        ref: 'SPM-RoboticCell'
      },
      'default': {
        model: 'CyTOS Bespoke Automation & Turnkey SPM',
        specs: 'Concept to Site Commissioning • In-House Controller & Software',
        ref: 'SPM-Turnkey'
      }
    }
  };

  function updateFinderResult() {
    const req = reqSelect.value;
    const mat = matSelect.value;

    const reqData = machineDatabase[req] || machineDatabase['pcb-prod'];
    const result = reqData[mat] || reqData['default'] || reqData[Object.keys(reqData)[0]];

    if (modelText) modelText.textContent = result.model;
    if (specsText) specsText.textContent = result.specs;

    if (quoteBtn) {
      quoteBtn.onclick = () => {
        openRfqModal(result.model);
      };
    }
  }

  reqSelect.onchange = updateFinderResult;
  matSelect.onchange = updateFinderResult;
  updateFinderResult();
}

/* ==========================================================================
   2b. Verified Client Reviews & Ratings Slider
   ========================================================================== */
function initReviewsSlider() {
  const track = document.getElementById('reviewsSliderTrack');
  const prevBtn = document.getElementById('reviewsPrevBtn');
  const nextBtn = document.getElementById('reviewsNextBtn');
  const currentCounter = document.getElementById('reviewsCurrentIndex');
  const totalCounter = document.getElementById('reviewsTotalCount');
  const dotsContainer = document.getElementById('reviewsSliderDots');
  const dots = dotsContainer ? dotsContainer.querySelectorAll('.review-dot') : [];

  if (!track) return;

  const cards = track.querySelectorAll('.review-testimonial-card');
  const totalCards = cards.length;
  if (!totalCards) return;

  if (totalCounter) {
    totalCounter.textContent = String(totalCards).padStart(2, '0');
  }

  let currentIndex = 0;
  let autoSlideTimer = null;
  const slideIntervalDuration = 5000;

  function getCardsPerView() {
    if (window.innerWidth <= 640) return 1;
    if (window.innerWidth <= 1024) return 2;
    return 3;
  }

  function getMaxIndex() {
    const cpv = getCardsPerView();
    return Math.max(0, totalCards - cpv);
  }

  function updateSlider(animate = true) {
    const maxIdx = getMaxIndex();
    if (currentIndex > maxIdx) currentIndex = maxIdx;
    if (currentIndex < 0) currentIndex = 0;

    const firstCard = cards[0];
    const trackStyle = window.getComputedStyle(track);
    const gap = parseFloat(trackStyle.gap) || 24;
    const cardWidth = firstCard.getBoundingClientRect().width;
    const offset = currentIndex * (cardWidth + gap);

    track.style.transition = animate ? 'transform 0.45s cubic-bezier(0.25, 1, 0.5, 1)' : 'none';
    track.style.transform = `translateX(-${offset}px)`;

    if (currentCounter) {
      currentCounter.textContent = String(currentIndex + 1).padStart(2, '0');
    }

    dots.forEach((dot, idx) => {
      dot.classList.toggle('active', idx === currentIndex);
    });
  }

  function nextSlide() {
    const maxIdx = getMaxIndex();
    if (currentIndex >= maxIdx) {
      currentIndex = 0;
    } else {
      currentIndex++;
    }
    updateSlider(true);
  }

  function prevSlide() {
    const maxIdx = getMaxIndex();
    if (currentIndex <= 0) {
      currentIndex = maxIdx;
    } else {
      currentIndex--;
    }
    updateSlider(true);
  }

  function startAutoSlide() {
    stopAutoSlide();
    autoSlideTimer = setInterval(() => {
      nextSlide();
    }, slideIntervalDuration);
  }

  function stopAutoSlide() {
    if (autoSlideTimer) {
      clearInterval(autoSlideTimer);
      autoSlideTimer = null;
    }
  }

  if (nextBtn) {
    nextBtn.onclick = () => {
      nextSlide();
      startAutoSlide();
    };
  }

  if (prevBtn) {
    prevBtn.onclick = () => {
      prevSlide();
      startAutoSlide();
    };
  }

  dots.forEach((dot, idx) => {
    dot.onclick = () => {
      const maxIdx = getMaxIndex();
      currentIndex = Math.min(idx, maxIdx);
      updateSlider(true);
      startAutoSlide();
    };
  });

  updateSlider(false);
  startAutoSlide();
}

/* ==========================================================================
   3. Interactive Payback & Cycle Time Estimator
   ========================================================================== */
function initRoiCalculator() {
  const boardsSlider = document.getElementById('calcBoards');
  const costSlider = document.getElementById('calcCost');
  const daysSlider = document.getElementById('calcDays');

  const boardsVal = document.getElementById('calcBoardsVal');
  const costVal = document.getElementById('calcCostVal');
  const daysVal = document.getElementById('calcDaysVal');

  const annualSavingsEl = document.getElementById('calcAnnualSavings');
  const paybackMonthsEl = document.getElementById('calcPaybackMonths');
  const timeSavedEl = document.getElementById('calcTimeSaved');
  const sendRoiBtn = document.getElementById('calcSendRoiBtn');

  if (!boardsSlider || !costSlider) return;

  function calculateRoi() {
    const boardsPerMonth = parseInt(boardsSlider.value, 10);
    const costPerBoard = parseInt(costSlider.value, 10);
    const delayDays = parseInt(daysSlider.value, 10);

    if (boardsVal) boardsVal.textContent = `${boardsPerMonth} boards`;
    if (costVal) costVal.textContent = `₹${costPerBoard.toLocaleString('en-IN')}`;
    if (daysVal) daysVal.textContent = `${delayDays} days delay`;

    const monthlyOutsourceCost = boardsPerMonth * costPerBoard;
    const inHouseMonthlyCost = boardsPerMonth * (costPerBoard * 0.15);
    const monthlyNetSavings = monthlyOutsourceCost - inHouseMonthlyCost;
    const annualNetSavings = monthlyNetSavings * 12;

    const estimatedMachineCost = 450000;
    const paybackMonths = Math.max(1.8, (estimatedMachineCost / monthlyNetSavings)).toFixed(1);
    const annualDaysSaved = Math.round(boardsPerMonth * delayDays * 0.85);

    if (annualSavingsEl) {
      annualSavingsEl.textContent = `₹${Math.round(annualNetSavings).toLocaleString('en-IN')}`;
    }
    if (paybackMonthsEl) {
      paybackMonthsEl.textContent = `${paybackMonths} Months`;
    }
    if (timeSavedEl) {
      timeSavedEl.textContent = `${annualDaysSaved} Days / Yr`;
    }
  }

  boardsSlider.oninput = calculateRoi;
  costSlider.oninput = calculateRoi;
  if (daysSlider) daysSlider.oninput = calculateRoi;

  if (sendRoiBtn) {
    sendRoiBtn.onclick = () => {
      const boards = boardsSlider.value;
      const cost = costSlider.value;
      const note = `ROI Estimate: ${boards} boards/mo @ ₹${cost}/board. Requesting feasibility study.`;
      openRfqModal('PCB Rapid Prototyping Machine', note);
    };
  }

  calculateRoi();
}

/* ==========================================================================
   4. Commercial Pillars & Product Tab Switcher
   ========================================================================== */
function initProductTabs() {
  const tabBtns = document.querySelectorAll('.pillar-nav-btn');
  const panels = document.querySelectorAll('.pillar-content-panel');

  if (!tabBtns.length) return;

  tabBtns.forEach(btn => {
    btn.onclick = () => {
      const targetPillar = btn.getAttribute('data-pillar');
      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      panels.forEach(panel => {
        if (panel.id === `pillar-${targetPillar}`) {
          panel.classList.add('active');
        } else {
          panel.classList.remove('active');
        }
      });
    };
  });
}

/* ==========================================================================
   5. Application Matrix Filter
   ========================================================================== */
function initApplicationFilter() {
  const filterBtns = document.querySelectorAll('.app-filter-btn');
  const appCards = document.querySelectorAll('.app-matrix-card');

  if (!filterBtns.length) return;

  filterBtns.forEach(btn => {
    btn.onclick = () => {
      const category = btn.getAttribute('data-filter');
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      appCards.forEach(card => {
        const cardCategory = card.getAttribute('data-category');
        if (category === 'all' || cardCategory === category) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    };
  });
}

/* ==========================================================================
   6. FAQ Accordion
   ========================================================================== */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question-btn');
    if (!questionBtn) return;

    questionBtn.onclick = () => {
      const isOpen = item.classList.contains('active');
      faqItems.forEach(otherItem => {
        otherItem.classList.remove('active');
      });
      if (!isOpen) {
        item.classList.add('active');
      }
    };
  });
}

/* ==========================================================================
   7. Interactive RFQ Modal
   ========================================================================== */
let selectedMachineModel = 'General CNC / Automation RFQ';

function escapeUserHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

export function openRfqModal(modelName = 'CyTOS Machine System', customNotes = '') {
  selectedMachineModel = modelName;
  const modalOverlays = document.querySelectorAll('#rfqModalOverlay, #rfqModal, .rfq-modal-overlay, .modal-backdrop');
  if (!modalOverlays.length) return;

  modalOverlays.forEach(modalOverlay => {
    const machineSelect = modalOverlay.querySelector('#rfqMachineSelect, #rfqMachine, select[name="machine"], select');
    const selectedMachineInput = modalOverlay.querySelector('#rfqSelectedMachine, input[name="machine"]');
    const notesField = modalOverlay.querySelector('#rfqNotes, #rfqDetails, #rfqRequirements, textarea');
    const step1 = modalOverlay.querySelector('#rfqStep1');
    const step2 = modalOverlay.querySelector('#rfqStep2');
    const successState = modalOverlay.querySelector('#rfqSuccessMessage');
    const inpageSuccess = modalOverlay.querySelector('.rfq-inpage-success');
    const form = modalOverlay.querySelector('form');

    if (machineSelect) {
      machineSelect.value = modelName;
      // If exact match not in options, select closest
      if (!machineSelect.value && machineSelect.options && machineSelect.options.length > 0) {
        let matched = false;
        for (let i = 0; i < machineSelect.options.length; i++) {
          if (machineSelect.options[i].value.toLowerCase().includes(modelName.toLowerCase()) ||
              modelName.toLowerCase().includes(machineSelect.options[i].value.toLowerCase())) {
            machineSelect.selectedIndex = i;
            matched = true;
            break;
          }
        }
        if (!matched) machineSelect.selectedIndex = 0;
      }
    }
    if (selectedMachineInput) selectedMachineInput.value = modelName;
    if (notesField && customNotes) notesField.value = customNotes;

    // Restore form visibility if previously hidden by submission
    if (form) form.style.display = '';
    if (inpageSuccess) inpageSuccess.remove();

    if (step1 && step2) {
      step1.style.display = 'block';
      step1.classList.add('active');
      step2.style.display = 'none';
      step2.classList.remove('active');
    }
    if (successState) {
      successState.style.display = 'none';
      successState.classList.remove('active');
    }

    const badge1 = modalOverlay.querySelector('#stepBadge1');
    const badge2 = modalOverlay.querySelector('#stepBadge2');
    if (badge1) badge1.classList.add('active');
    if (badge2) badge2.classList.remove('active');

    modalOverlay.classList.add('active');
  });

  document.body.style.overflow = 'hidden';
}

export function closeRfqModal() {
  document.querySelectorAll('#rfqModalOverlay, #rfqModal, .rfq-modal-overlay, .modal-backdrop').forEach(modal => {
    modal.classList.remove('active');
  });
  document.body.style.overflow = '';
}

function initRfqModal() {
  const modalOverlays = document.querySelectorAll('#rfqModalOverlay, #rfqModal, .rfq-modal-overlay, .modal-backdrop');

  // Wire all modal close buttons
  document.querySelectorAll('.modal-close-btn, .rfq-close-btn, .rfq-modal-close, #rfqModalCloseBtn, #modalCloseBtn, #closeRfqModal').forEach(btn => {
    btn.onclick = (e) => {
      e.preventDefault();
      closeRfqModal();
    };
  });

  // Clicking backdrop outside window closes modal
  modalOverlays.forEach(overlay => {
    overlay.onclick = (e) => {
      if (e.target === overlay) {
        closeRfqModal();
      }
    };
  });

  // ESC key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeRfqModal();
    }
  });

  // Wire all buttons that trigger quote modal
  document.querySelectorAll('[data-open-rfq], [data-open-modal], .btn-request-quote').forEach(btn => {
    btn.onclick = (e) => {
      e.preventDefault();
      const model = btn.getAttribute('data-machine') || btn.getAttribute('data-model') || 'CyTOS Machine System';
      openRfqModal(model);
    };
  });

  // Wire Stepper Next buttons
  document.querySelectorAll('#rfqNextBtn, #rfqNextStepBtn').forEach(nextBtn => {
    nextBtn.onclick = (e) => {
      e.preventDefault();
      const modal = nextBtn.closest('.rfq-modal-overlay, .modal-backdrop, #rfqModalOverlay, #rfqModal') || document;
      const step1 = modal.querySelector('#rfqStep1');
      const step2 = modal.querySelector('#rfqStep2');
      const name = modal.querySelector('#rfqName, [name="name"]')?.value.trim();
      const phone = modal.querySelector('#rfqPhone, [name="phone"]')?.value.trim();
      const email = modal.querySelector('#rfqEmail, [name="email"]')?.value.trim();

      if (!name || (!phone && !email)) {
        alert('Please provide your Full Name and a valid Mobile/WhatsApp number or Email to proceed.');
        return;
      }

      if (step1 && step2) {
        step1.style.display = 'none';
        step1.classList.remove('active');
        step2.style.display = 'block';
        step2.classList.add('active');

        modal.querySelector('#stepBadge1')?.classList.remove('active');
        modal.querySelector('#stepBadge2')?.classList.add('active');
      }
    };
  });

  // Wire Stepper Back buttons
  document.querySelectorAll('#rfqBackBtn, #rfqPrevStepBtn').forEach(backBtn => {
    backBtn.onclick = (e) => {
      e.preventDefault();
      const modal = backBtn.closest('.rfq-modal-overlay, .modal-backdrop, #rfqModalOverlay, #rfqModal') || document;
      const step1 = modal.querySelector('#rfqStep1');
      const step2 = modal.querySelector('#rfqStep2');

      if (step1 && step2) {
        step2.style.display = 'none';
        step2.classList.remove('active');
        step1.style.display = 'block';
        step1.classList.add('active');

        modal.querySelector('#stepBadge2')?.classList.remove('active');
        modal.querySelector('#stepBadge1')?.classList.add('active');
      }
    };
  });

  // Universal RFQ Form Submission Handler
  const handleRfqFormSubmit = async (e) => {
    if (e) e.preventDefault();

    const form = (e?.target?.tagName === 'FORM' ? e.target : e?.target?.closest('form')) || document.querySelector('#rfqForm, .rfq-modal-form');
    if (!form) return;

    const modal = form.closest('#rfqModalOverlay, #rfqModal, .rfq-modal-overlay, .modal-backdrop') || form.parentElement;

    const getVal = (selector, fallback = '') => {
      const el = form.querySelector(selector) || modal?.querySelector(selector);
      return el?.value?.trim() || fallback;
    };

    const name = getVal('#rfqName, [name="name"], [id*="Name"]');
    const company = getVal('#rfqCompany, [name="company"], [id*="Company"]', 'N/A');
    const phone = getVal('#rfqPhone, [name="phone"], [id*="Phone"]');
    const email = getVal('#rfqEmail, [name="email"], [id*="Email"]');
    const city = getVal('#rfqCity, #rfqLocation, [name="city"], [id*="City"]', 'India');
    const model = getVal('#rfqMachineSelect, #rfqSelectedMachine, #rfqMachine, [name="machine"], select', selectedMachineModel || 'CyTOS Machine System');
    const material = getVal('#rfqMaterial, [name="material"], [id*="Material"]', 'N/A');
    const volume = getVal('#rfqVolume, [name="volume"]', 'Standard production');
    const tolerance = getVal('#rfqTolerance, [name="tolerance"]', 'Standard');
    const timeline = getVal('#rfqTimeline, [name="timeline"]', 'Immediate');
    const notes = getVal('#rfqNotes, #rfqDetails, #rfqRequirements, textarea', 'Technical quote and feasibility consultation requested.');

    if (!name || (!phone && !email)) {
      alert('Please provide your Name and a valid Mobile/WhatsApp number or Email.');
      const step1 = modal?.querySelector('#rfqStep1');
      const step2 = modal?.querySelector('#rfqStep2');
      if (step1 && step2) {
        step2.style.display = 'none';
        step2.classList.remove('active');
        step1.style.display = 'block';
        step1.classList.add('active');
        modal?.querySelector('#stepBadge2')?.classList.remove('active');
        modal?.querySelector('#stepBadge1')?.classList.add('active');
      }
      return;
    }

    const submitBtn = form.querySelector('button[type="submit"], #rfqSubmitBtn');
    const originalText = submitBtn ? submitBtn.textContent : 'Submit Technical RFQ';
    if (submitBtn) {
      submitBtn.textContent = 'Transmitting to Pune Engineering Desk...';
      submitBtn.disabled = true;
    }

    const leadPayload = {
      _subject: `New Technical RFQ: ${model} from ${company !== 'N/A' ? company : name}`,
      Client_Name: name,
      Company: company,
      Phone_WhatsApp: phone,
      Email: email,
      City_Location: city,
      Machine_Model: model,
      Workpiece_Material: material,
      Target_Volume: volume,
      Required_Tolerance: tolerance,
      Project_Timeline: timeline,
      Application_Notes: notes,
      Source: 'CyTOS Technical RFQ Portal'
    };

    // 1. Vault lead locally and dispatch email (PHP mailer + FormSubmit fallback)
    await dispatchEmailToInranktech(leadPayload);

    if (submitBtn) {
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
    }

    // 2. Structured WhatsApp message
    const whatsappText = encodeURIComponent(
      `*New Technical RFQ for CyTOS Pune*\n\n` +
      `• *Client Name:* ${name}\n` +
      `• *Company:* ${company}\n` +
      `• *Phone/WhatsApp:* ${phone}\n` +
      `• *Email:* ${email}\n` +
      `• *Location:* ${city}\n` +
      `• *Machine Model:* ${model}\n` +
      `• *Material / Specs:* ${material}\n` +
      `• *Application Notes:* ${notes}\n\n` +
      `_Dispatched via cytos.in Technical RFQ Portal_`
    );
    const waUrl = `https://wa.me/917620414165?text=${whatsappText}`;

    // 3. Automatically launch WhatsApp
    try {
      window.open(waUrl, '_blank');
    } catch (popupErr) {
      console.log('[CyTOS] Popup blocked, WhatsApp button available in UI confirmation');
    }

    // 4. Update UI to success state
    const step1 = modal?.querySelector('#rfqStep1');
    const step2 = modal?.querySelector('#rfqStep2');
    const successState = modal?.querySelector('#rfqSuccessMessage');

    if (step1) {
      step1.style.display = 'none';
      step1.classList.remove('active');
    }
    if (step2) {
      step2.style.display = 'none';
      step2.classList.remove('active');
    }

    if (successState) {
      successState.style.display = 'block';
      successState.classList.add('active');
      successState.innerHTML = `
        <div style="width: 56px; height: 56px; border-radius: 50%; background: #ecfdf5; color: #059669; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.25rem;">
          <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
        </div>
        <h3 style="font-size: 1.35rem; margin-bottom: 0.5rem; color: var(--text-pure, #0f172a);">RFQ Transmitted to Engineering Desk!</h3>
        <p style="font-size: 0.92rem; color: var(--text-secondary, #475569); max-width: 480px; margin: 0 auto 1.25rem; line-height: 1.55;">
          Thank you, <strong>${escapeUserHtml(name)}</strong>! Your technical specifications for <strong>${escapeUserHtml(model)}</strong> have been securely registered with the CyTOS Pune engineering team. An application engineer will review your specs and contact you within 2 business hours.
        </p>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.85rem 1.15rem; margin-bottom: 1.25rem; text-align: left; font-size: 0.85rem; color: #334155;">
          <div style="display: flex; justify-content: space-between; margin-bottom: 0.35rem;">
            <span style="color: #64748b;">Machine:</span>
            <strong>${escapeUserHtml(model)}</strong>
          </div>
          <div style="display: flex; justify-content: space-between; margin-bottom: 0.35rem;">
            <span style="color: #64748b;">Contact:</span>
            <strong>${escapeUserHtml(phone || email)}</strong>
          </div>
          <div style="display: flex; justify-content: space-between;">
            <span style="color: #64748b;">Status:</span>
            <span style="color: #059669; font-weight: 700;">✓ Dispatched to Email &amp; WhatsApp</span>
          </div>
        </div>
        <div style="display: flex; flex-direction: column; gap: 0.75rem;">
          <a href="${waUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="width: 100%; justify-content: center;">
            <svg class="btn-icon-svg whatsapp-icon-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.68C7.02 10.88 7.9 12.04 8.02 12.2C8.14 12.37 9.73 14.95 12.24 15.93C14.33 16.75 14.75 16.59 15.22 16.54C15.69 16.49 16.74 15.91 16.96 15.29C17.18 14.66 17.18 14.13 17.11 14.02C17.05 13.91 16.89 13.84 16.64 13.72C16.39 13.6 15.17 13 14.94 12.92C14.72 12.83 14.56 12.79 14.4 13.04C14.24 13.29 13.77 13.84 13.63 14.01C13.5 14.17 13.36 14.19 13.11 14.07C12.87 13.95 12.08 13.69 11.15 12.86C10.42 12.21 9.93 11.41 9.79 11.17C9.65 10.92 9.78 10.79 9.9 10.67C10.01 10.56 10.15 10.38 10.27 10.23C10.4 10.08 10.44 9.97 10.52 9.81C10.6 9.65 10.56 9.51 10.5 9.39C10.44 9.27 9.97 8.12 9.78 7.65C9.59 7.19 9.39 7.25 9.24 7.24C9.1 7.23 8.94 7.23 8.78 7.23H8.53Z"/></svg>
            <span>Need Urgent Response? Chat on WhatsApp</span>
          </a>
          <button type="button" class="btn btn-outline" id="rfqSuccessCloseBtn" style="width: 100%;">
            <span>Close Window</span>
          </button>
        </div>
      `;
      modal.querySelector('#rfqSuccessCloseBtn')?.addEventListener('click', closeRfqModal);
    } else {
      // For pages without rfqSuccessMessage in DOM (e.g. dedicated machine pages)
      form.style.display = 'none';
      let inpageCard = modal?.querySelector('.rfq-inpage-success');
      if (!inpageCard) {
        inpageCard = document.createElement('div');
        inpageCard.className = 'rfq-inpage-success';
        form.parentElement.appendChild(inpageCard);
      }
      inpageCard.style.display = 'block';
      inpageCard.innerHTML = `
        <div style="text-align: center; padding: 1.5rem 1rem;">
          <div style="width: 52px; height: 52px; border-radius: 50%; background: #ecfdf5; color: #059669; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;">
            <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
          </div>
          <h3 style="font-size: 1.25rem; font-weight: 700; color: #0f172a; margin-bottom: 0.35rem;">RFQ Registered &amp; Dispatched!</h3>
          <p style="font-size: 0.9rem; color: #475569; margin-bottom: 1.15rem; line-height: 1.5;">
            Thank you, <strong>${escapeUserHtml(name)}</strong>! Your quotation request for <strong>${escapeUserHtml(model)}</strong> has been registered with CyTOS Pune engineering desk.
          </p>
          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.75rem 1rem; margin-bottom: 1.25rem; font-size: 0.85rem; text-align: left; color: #334155;">
            <div style="display:flex; justify-content:space-between; margin-bottom: 4px;">
              <span style="color:#64748b;">Machine:</span> <strong>${escapeUserHtml(model)}</strong>
            </div>
            <div style="display:flex; justify-content:space-between; margin-bottom: 4px;">
              <span style="color:#64748b;">Contact:</span> <strong>${escapeUserHtml(phone || email)}</strong>
            </div>
            <div style="display:flex; justify-content:space-between;">
              <span style="color:#64748b;">Direct Helpline:</span> <strong style="color: #d97706;">+91 76204 14165</strong>
            </div>
          </div>
          <div style="display: flex; flex-direction: column; gap: 0.65rem;">
            <a href="${waUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="width: 100%; justify-content: center;">
              <span>Connect on WhatsApp (Direct Engineer Desk)</span>
            </a>
            <button type="button" class="btn btn-outline" style="width: 100%;" onclick="document.querySelectorAll('#rfqModalOverlay, #rfqModal, .rfq-modal-overlay, .modal-backdrop').forEach(m => m.classList.remove('active')); document.body.style.overflow = '';">
              <span>Close Window</span>
            </button>
          </div>
        </div>
      `;
    }

    form.reset();
  };

  // Attach submission handlers to all RFQ forms
  const allRfqForms = document.querySelectorAll('#rfqForm, #rfqModalForm, .rfq-modal-form, .rfq-modal-dialog form, .modal-dialog form, .rfq-modal-window form');
  allRfqForms.forEach(form => {
    form.setAttribute('action', 'javascript:void(0);');
    form.onsubmit = handleRfqFormSubmit;
    const sBtn = form.querySelector('button[type="submit"], #rfqSubmitBtn');
    if (sBtn) {
      sBtn.onclick = (e) => {
        e.preventDefault();
        handleRfqFormSubmit(e);
      };
    }
  });

  // Dedicated WhatsApp direct button
  document.querySelectorAll('#rfqWhatsAppSubmitBtn').forEach(waBtn => {
    waBtn.onclick = (e) => {
      e.preventDefault();
      handleRfqFormSubmit(e);
    };
  });
}

/* ==========================================================================
   Contact Page Form Handler
   ========================================================================== */
function initContactForm() {
  const contactForm = document.getElementById('contactPageForm');
  if (!contactForm) return;

  contactForm.setAttribute('action', 'javascript:void(0);');

  contactForm.onsubmit = async (e) => {
    e.preventDefault();
    const name = document.getElementById('cpName')?.value.trim() || '';
    const company = document.getElementById('cpCompany')?.value.trim() || 'N/A';
    const email = document.getElementById('cpEmail')?.value.trim() || '';
    const phone = document.getElementById('cpPhone')?.value.trim() || '';
    const city = document.getElementById('cpLocation')?.value.trim() || document.getElementById('cpCity')?.value.trim() || 'India';
    const machine = document.getElementById('cpMachine')?.value || 'General CNC Machinery';
    const material = document.getElementById('cpMaterial')?.value.trim() || 'N/A';
    const workArea = document.getElementById('cpWorkArea')?.value.trim() || '';
    const message = document.getElementById('cpMessage')?.value.trim() || 'Technical consultation and quotation inquiry.';

    if (!name || (!email && !phone)) {
      alert('Please provide your Full Name and a valid Mobile/WhatsApp number or Email.');
      return;
    }

    const submitBtn = contactForm.querySelector('button[type="submit"]');
    const originalText = submitBtn ? submitBtn.textContent : 'Submit RFQ to Pune Engineering Desk';
    if (submitBtn) {
      submitBtn.textContent = 'Transmitting to Pune Engineering Desk...';
      submitBtn.disabled = true;
    }

    const payload = {
      _subject: `CyTOS Contact Form: ${machine} from ${company !== 'N/A' ? company : name}`,
      Full_Name: name,
      Client_Name: name,
      Company: company,
      Email: email,
      Phone: phone,
      Phone_WhatsApp: phone,
      City_Location: city,
      Machine_Category: machine,
      Workpiece_Material: material,
      Work_Area_Dimensions: workArea,
      Detailed_Requirements: message,
      Source: 'CyTOS Contact Us Page'
    };

    await dispatchEmailToInranktech(payload);

    if (submitBtn) {
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
    }

    const whatsappText = encodeURIComponent(
      `*New Contact Inquiry for CyTOS Pune*\n\n` +
      `• *Client Name:* ${name}\n` +
      `• *Company:* ${company}\n` +
      `• *Phone/WhatsApp:* ${phone}\n` +
      `• *Email:* ${email}\n` +
      `• *Location:* ${city}\n` +
      `• *Equipment:* ${machine}\n` +
      `• *Material:* ${material}\n` +
      `• *Requirements:* ${message}\n\n` +
      `_Transmitted via cytos.in Contact Portal_`
    );
    const waUrl = `https://wa.me/917620414165?text=${whatsappText}`;

    try {
      window.open(waUrl, '_blank');
    } catch (popupErr) {
      console.log('[CyTOS] Popup blocked, button available on banner');
    }

    // Render prominent in-page success confirmation banner
    let banner = document.getElementById('contactSuccessBanner');
    if (!banner) {
      banner = document.createElement('div');
      banner.id = 'contactSuccessBanner';
      banner.className = 'contact-success-banner';
      contactForm.parentNode.insertBefore(banner, contactForm);
    }

    banner.style.display = 'block';
    banner.innerHTML = `
      <div style="display: flex; align-items: flex-start; gap: 1rem;">
        <div style="width: 44px; height: 44px; min-width: 44px; border-radius: 50%; background: #ecfdf5; color: #059669; display: flex; align-items: center; justify-content: center;">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
        </div>
        <div style="flex: 1;">
          <h4 style="font-size: 1.15rem; font-weight: 700; color: #065f46; margin-bottom: 0.35rem;">Inquiry Successfully Registered &amp; Dispatched!</h4>
          <p style="font-size: 0.92rem; color: #1e293b; line-height: 1.55; margin-bottom: 0.85rem;">
            Thank you, <strong>${escapeUserHtml(name)}</strong>! Your technical inquiry regarding <strong>${escapeUserHtml(machine)}</strong> has been vaulted and transmitted to the CyTOS Pune engineering desk. An application engineer will contact you within 2 business hours.
          </p>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
            <a href="${waUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.55rem 1.15rem; font-size: 0.88rem;">
              <svg class="btn-icon-svg whatsapp-icon-svg" viewBox="0 0 24 24" width="16" height="16" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.68C7.02 10.88 7.9 12.04 8.02 12.2C8.14 12.37 9.73 14.95 12.24 15.93C14.33 16.75 14.75 16.59 15.22 16.54C15.69 16.49 16.74 15.91 16.96 15.29C17.18 14.66 17.18 14.13 17.11 14.02C17.05 13.91 16.89 13.84 16.64 13.72C16.39 13.6 15.17 13 14.94 12.92C14.72 12.83 14.56 12.79 14.4 13.04C14.24 13.29 13.77 13.84 13.63 14.01C13.5 14.17 13.36 14.19 13.11 14.07C12.87 13.95 12.08 13.69 11.15 12.86C10.42 12.21 9.93 11.41 9.79 11.17C9.65 10.92 9.78 10.79 9.9 10.67C10.01 10.56 10.15 10.38 10.27 10.23C10.4 10.08 10.44 9.97 10.52 9.81C10.6 9.65 10.56 9.51 10.5 9.39C10.44 9.27 9.97 8.12 9.78 7.65C9.59 7.19 9.39 7.25 9.24 7.24C9.1 7.23 8.94 7.23 8.78 7.23H8.53Z"/></svg>
              <span>Fast-Track: Connect on WhatsApp</span>
            </a>
          </div>
        </div>
      </div>
    `;
    banner.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    contactForm.reset();
  };
}

/* ==========================================================================
   Newsletter Forms Handler
   ========================================================================== */
function initNewsletterForms() {
  document.querySelectorAll('.newsletter-form-row').forEach(form => {
    form.onsubmit = async (e) => {
      e.preventDefault();
      const emailInput = form.querySelector('input[type="email"]');
      const email = emailInput?.value?.trim();
      if (!email) return;

      const submitBtn = form.querySelector('button[type="submit"]');
      if (submitBtn) submitBtn.disabled = true;

      await dispatchEmailToInranktech({
        _subject: `New Newsletter Subscriber: ${email}`,
        Email: email,
        Source: 'CyTOS Machining Blog Newsletter'
      });

      if (submitBtn) submitBtn.disabled = false;
      alert('Thank you for subscribing! Your CyTOS Engineering Machining Guide has been queued for delivery to ' + email);
      form.reset();
    };
  });
}


/* ==========================================================================
   Metric Counters
   ========================================================================== */
function initMetricCounters() {
  const counters = document.querySelectorAll('.metric-number[data-count]');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = entry.target;
        const targetNumber = parseInt(target.getAttribute('data-count'), 10);
        const prefix = target.getAttribute('data-prefix') || '';
        const suffix = target.getAttribute('data-suffix') || '';
        
        const duration = 1800;
        const startTime = performance.now();

        function updateCounter(currentTime) {
          const elapsed = currentTime - startTime;
          const progress = Math.min(elapsed / duration, 1);
          const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
          const currentVal = Math.floor(easeProgress * targetNumber);

          target.textContent = `${prefix}${currentVal.toLocaleString()}${suffix}`;

          if (progress < 1) {
            requestAnimationFrame(updateCounter);
          } else {
            target.textContent = `${prefix}${targetNumber.toLocaleString()}${suffix}`;
          }
        }

        requestAnimationFrame(updateCounter);
        obs.unobserve(target);
      }
    });
  }, { threshold: 0.3 });

  counters.forEach(counter => observer.observe(counter));
}

/* ==========================================================================
   Sticky Navigation State
   ========================================================================== */
function initStickyHeader() {
  const header = document.querySelector('.main-header');
  if (!header) return;

  window.onscroll = () => {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };
}

/* ==========================================================================
   Mobile Menu Navigation
   ========================================================================== */
function initMobileNav() {
  const menuBtn = document.getElementById('mobileMenuBtn');
  const navLinks = document.querySelector('.nav-links');

  if (!menuBtn || !navLinks) return;

  const burgerSvg = '<svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" fill="none" aria-hidden="true"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
  const closeSvg = '<svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" fill="none" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>';

  menuBtn.onclick = (e) => {
    e.stopPropagation();
    const isActive = navLinks.classList.toggle('active');
    menuBtn.setAttribute('aria-expanded', isActive ? 'true' : 'false');
    document.body.style.overflow = isActive ? 'hidden' : '';
    menuBtn.innerHTML = isActive ? closeSvg : burgerSvg;
  };

  const dropdownTriggers = navLinks.querySelectorAll('.dropdown-trigger');
  dropdownTriggers.forEach(trigger => {
    trigger.onclick = (e) => {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        e.stopPropagation();
        const parentDropdown = trigger.closest('.nav-item-dropdown');
        if (parentDropdown) {
          navLinks.querySelectorAll('.nav-item-dropdown').forEach(item => {
            if (item !== parentDropdown) item.classList.remove('open');
          });
          parentDropdown.classList.toggle('open');
        }
      }
    };
  });

  navLinks.querySelectorAll('a:not(.dropdown-trigger)').forEach(link => {
    link.onclick = () => {
      if (window.innerWidth <= 768) {
        navLinks.classList.remove('active');
        document.body.style.overflow = '';
        menuBtn.innerHTML = burgerSvg;
      }
    };
  });
}

/* ==========================================================================
   Cookie Consent Banner
   ========================================================================== */
function initConsentBanner() {
  const banner = document.getElementById('cookieConsentBanner');
  if (!banner) return;

  const consent = localStorage.getItem('cytos_cookie_consent');
  if (consent) {
    banner.classList.add('consent-hidden');
    return;
  }

  setTimeout(() => {
    banner.classList.remove('consent-hidden');
  }, 600);

  const acceptBtn = document.getElementById('btnAcceptConsent');
  const rejectBtn = document.getElementById('btnRejectConsent');

  if (acceptBtn) {
    acceptBtn.onclick = () => {
      localStorage.setItem('cytos_cookie_consent', 'accepted_all');
      banner.classList.add('consent-hidden');
    };
  }

  if (rejectBtn) {
    rejectBtn.onclick = () => {
      localStorage.setItem('cytos_cookie_consent', 'necessary_only');
      banner.classList.add('consent-hidden');
    };
  }
}

/* ==========================================================================
   Blog Filter
   ========================================================================== */
function initBlogFilter() {
  const filterPills = document.querySelectorAll('.filter-pill');
  const blogCards = document.querySelectorAll('.blog-card');
  const featuredCard = document.querySelector('.featured-blog-card');

  if (!filterPills.length || !blogCards.length) return;

  filterPills.forEach(pill => {
    pill.onclick = () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');

      const category = pill.getAttribute('data-category');

      if (featuredCard) {
        const featCat = featuredCard.getAttribute('data-category');
        if (category === 'all' || featCat === category) {
          featuredCard.style.display = 'grid';
        } else {
          featuredCard.style.display = 'none';
        }
      }

      blogCards.forEach(card => {
        const cardCat = card.getAttribute('data-category');
        if (category === 'all' || cardCat === category) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    };
  });
}

/* ==========================================================================
   Terms TOC ScrollSpy
   ========================================================================== */
function initTermsToc() {
  const links = document.querySelectorAll('.terms-toc-link');
  if (!links.length) return;

  const sections = document.querySelectorAll('.terms-section');

  window.addEventListener('scroll', () => {
    let currentId = '';
    const scrollPos = window.scrollY + 140;

    sections.forEach(sec => {
      const top = sec.offsetTop;
      const height = sec.offsetHeight;
      if (scrollPos >= top && scrollPos < top + height) {
        currentId = sec.getAttribute('id');
      }
    });

    if (currentId) {
      links.forEach(l => {
        if (l.getAttribute('href') === `#${currentId}`) {
          l.classList.add('active');
        } else {
          l.classList.remove('active');
        }
      });
    }
  });
}


/* ==========================================================================
   Video Showcase & Autoplay Modal Player
   ========================================================================== */
export function openVideoModal(vidId, title, specsPath, machineName) {
  const modal = document.getElementById('videoModal');
  const iframe = document.getElementById('videoModalIframe');
  const modalTitle = document.getElementById('videoModalTitle');
  const quoteBtn = document.getElementById('videoModalQuoteBtn');
  const viewSpecsBtn = document.getElementById('videoModalSpecsBtn');

  if (!modal || !iframe || !vidId) return;

  if (modalTitle) modalTitle.textContent = title || 'CyTOS Machine Video Demonstration';
  // Autoplay enabled with rel=0
  iframe.src = `https://www.youtube.com/embed/${vidId}?autoplay=1&rel=0&enablejsapi=1`;

  if (quoteBtn) {
    quoteBtn.setAttribute('data-machine', machineName || title || 'CNC Machine');
  }

  if (viewSpecsBtn) {
    if (specsPath && specsPath !== '#' && specsPath !== 'javascript:void(0);') {
      viewSpecsBtn.href = specsPath;
      viewSpecsBtn.style.display = 'inline-flex';
    } else {
      viewSpecsBtn.style.display = 'none';
    }
  }

  modal.classList.add('active');
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
}

export function closeVideoModal() {
  const modal = document.getElementById('videoModal');
  const iframe = document.getElementById('videoModalIframe');
  if (!modal) return;

  modal.classList.remove('active');
  modal.setAttribute('aria-hidden', 'true');
  if (iframe) iframe.src = '';
  document.body.style.overflow = '';
}

function initVideoShowcase() {
  const tabs = document.querySelectorAll('.video-tab-chip');
  const cards = document.querySelectorAll('.video-card');
  const modal = document.getElementById('videoModal');
  const closeBtn = document.getElementById('videoModalClose');

  // 1. Interactive Category Filter Tabs
  if (tabs.length && cards.length) {
    tabs.forEach(tab => {
      tab.onclick = () => {
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        const filter = tab.getAttribute('data-filter') || 'all';

        cards.forEach(card => {
          const cat = card.getAttribute('data-category') || '';
          if (filter === 'all' || cat === filter) {
            card.style.display = 'flex';
          } else {
            card.style.display = 'none';
          }
        });
      };
    });
  }

  // 2. Video Modal Trigger Handlers (Thumbnails, Buttons, Cards)
  const triggers = document.querySelectorAll('[data-video-id], .video-thumb-box, .inline-video-thumb, .btn-play-trigger');
  triggers.forEach(trigger => {
    trigger.onclick = (e) => {
      // Don't intercept direct specs links
      if (e.target.closest('a') && !e.target.closest('[data-video-id]') && !e.target.closest('.video-thumb-box')) {
        return;
      }
      
      const card = trigger.closest('.video-card') || trigger.closest('article') || trigger.closest('.machine-video-grid') || trigger.parentElement;
      const vidId = trigger.getAttribute('data-video-id') || (card ? card.querySelector('[data-video-id]')?.getAttribute('data-video-id') : null);
      if (!vidId) return;

      e.preventDefault();
      e.stopPropagation();

      const title = trigger.getAttribute('data-video-title') || 
                    trigger.getAttribute('title') || 
                    (card ? (card.querySelector('.video-card-title, h2, h3, h4')?.textContent) : '') ||
                    'CyTOS Machine Video Demonstration';

      const specsPath = trigger.getAttribute('data-video-path') || 
                        (card ? card.querySelector('a[href*="/cnc-"], a[href*="/pcb-"], a[href*="/vdm-"], a[href*="/foam-"], a[href*="/spm-"]')?.getAttribute('href') : '') ||
                        '';

      const machineName = trigger.getAttribute('data-video-machine') || title;

      openVideoModal(vidId, title, specsPath, machineName);
    };
  });

  // Close handlers
  if (closeBtn) {
    closeBtn.onclick = (e) => {
      e.preventDefault();
      closeVideoModal();
    };
  }

  if (modal) {
    modal.onclick = (e) => {
      if (e.target === modal) {
        closeVideoModal();
      }
    };
  }

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal && modal.classList.contains('active')) {
      closeVideoModal();
    }
  });
}

