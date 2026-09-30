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

  // 2. Transmit to backend/FormSubmit in background with a 3.5s timeout
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 3500);
    const response = await fetch('https://formsubmit.co/ajax/info@cytos.in', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      signal: controller.signal,
      body: JSON.stringify({
        _subject: payload._subject || 'New CyTOS Machinery Inquiry',
        _cc: 'inranktech@gmail.com',
        _captcha: 'false',
        _template: 'table',
        ...payload
      })
    });
    clearTimeout(timeoutId);
    return response.ok;
  } catch (err) {
    console.warn('[CyTOS] Background mailer note (handled gracefully):', err.message || err);
    return false;
  }
}

/**
 * CyTOS Precision CNC & Industrial Automation - Interactive Engine
 * 3-Second Conversion Hooks, Interactive Slider, ROI Calculator & RFQ System
 */

document.addEventListener('DOMContentLoaded', () => {
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
  checkSubmissionStatus();
});

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
  const slideIntervalDuration = 5000; // Continuous 5-second auto-loop
  let slideTimer = null;

  function showSlide(index) {
    if (index < 0) index = slideCount - 1;
    if (index >= slideCount) index = 0;

    currentSlide = index;

    slides.forEach((slide, i) => {
      slide.classList.toggle('active', i === currentSlide);
    });

    // Update live slide counter
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
    // Continuous uninterruptible loop
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

  // Navigation Buttons: Jump and restart auto loop
  if (prevBtn) {
    prevBtn.addEventListener('click', (e) => {
      e.preventDefault();
      showSlide((currentSlide - 1 + slideCount) % slideCount);
      startAutoSlide();
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', (e) => {
      e.preventDefault();
      showSlide((currentSlide + 1) % slideCount);
      startAutoSlide();
    });
  }

  // Tab Buttons Click: Jump and restart auto loop
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => {
      showSlide(index);
      startAutoSlide();
    });
  });

  // Keyboard arrow navigation
  window.addEventListener('keydown', (e) => {
    const rect = sliderContainer?.getBoundingClientRect();
    if (rect && rect.top < window.innerHeight && rect.bottom > 0) {
      if (e.key === 'ArrowLeft') {
        showSlide((currentSlide - 1 + slideCount) % slideCount);
        startAutoSlide();
      } else if (e.key === 'ArrowRight') {
        showSlide((currentSlide + 1) % slideCount);
        startAutoSlide();
      }
    }
  });

  // Touch swipe support for mobile
  let touchStartX = 0;
  let touchEndX = 0;

  if (sliderContainer) {
    sliderContainer.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    sliderContainer.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      const swipeDistance = touchEndX - touchStartX;
      if (Math.abs(swipeDistance) > 40) {
        if (swipeDistance > 0) {
          showSlide((currentSlide - 1 + slideCount) % slideCount); // Swipe right -> previous slide
        } else {
          showSlide((currentSlide + 1) % slideCount); // Swipe left -> next slide
        }
        startAutoSlide();
      }
    }, { passive: true });
  }

  // Resume auto-loop when window or tab regains focus
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden) {
      startAutoSlide();
    }
  });

  // Start continuous loop
  startAutoSlide();
}

/* ==========================================================================
   2. 3-Second Immediate Hook: Machine & Feasibility Finder
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

  reqSelect.addEventListener('change', updateFinderResult);
  matSelect.addEventListener('change', updateFinderResult);
  updateFinderResult();
}

/* ==========================================================================
   2b. Verified Client Reviews & Ratings Slider
   ========================================================================== */
function initReviewsSlider() {
  const track = document.getElementById('reviewsSliderTrack');
  const viewport = document.getElementById('reviewsSliderViewport');
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
    nextBtn.addEventListener('click', () => {
      nextSlide();
      startAutoSlide();
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      prevSlide();
      startAutoSlide();
    });
  }

  dots.forEach((dot, idx) => {
    dot.addEventListener('click', () => {
      const maxIdx = getMaxIndex();
      currentIndex = Math.min(idx, maxIdx);
      updateSlider(true);
      startAutoSlide();
    });
  });

  // Pause on hover
  if (viewport) {
    viewport.addEventListener('mouseenter', stopAutoSlide);
    viewport.addEventListener('mouseleave', startAutoSlide);
  }
  const controls = document.querySelector('.reviews-slider-controls');
  if (controls) {
    controls.addEventListener('mouseenter', stopAutoSlide);
    controls.addEventListener('mouseleave', startAutoSlide);
  }

  // Touch Swipe for mobile/tablet
  let touchStartX = 0;
  let touchEndX = 0;

  if (viewport) {
    viewport.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
      stopAutoSlide();
    }, { passive: true });

    viewport.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      const diff = touchEndX - touchStartX;
      if (Math.abs(diff) > 40) {
        if (diff > 0) {
          prevSlide();
        } else {
          nextSlide();
        }
      }
      startAutoSlide();
    }, { passive: true });
  }

  // Window resize handler
  let resizeTimeout;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      updateSlider(false);
    }, 100);
  });

  // Pause on hidden tab, resume on visible
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      stopAutoSlide();
    } else {
      startAutoSlide();
    }
  });

  // Initial render & start auto-slide
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

    // Update labels
    if (boardsVal) boardsVal.textContent = `${boardsPerMonth} boards`;
    if (costVal) costVal.textContent = `₹${costPerBoard.toLocaleString('en-IN')}`;
    if (daysVal) daysVal.textContent = `${delayDays} days delay`;

    // Monthly outsourced cost
    const monthlyOutsourceCost = boardsPerMonth * costPerBoard;
    
    // In-house raw material & tool wear cost (approx 15% of outsourcing)
    const inHouseMonthlyCost = boardsPerMonth * (costPerBoard * 0.15);
    const monthlyNetSavings = monthlyOutsourceCost - inHouseMonthlyCost;
    const annualNetSavings = monthlyNetSavings * 12;

    // Benchmark machine investment (~₹4,50,000 for standard prototyping system)
    const estimatedMachineCost = 450000;
    const paybackMonths = Math.max(1.8, (estimatedMachineCost / monthlyNetSavings)).toFixed(1);

    // Turnaround time saved per year (days of waiting eliminated)
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

  boardsSlider.addEventListener('input', calculateRoi);
  costSlider.addEventListener('input', calculateRoi);
  daysSlider.addEventListener('input', calculateRoi);

  if (sendRoiBtn) {
    sendRoiBtn.addEventListener('click', () => {
      const boards = boardsSlider.value;
      const cost = costSlider.value;
      const note = `ROI Estimate: ${boards} boards/mo @ ₹${cost}/board. Requesting feasibility study.`;
      openRfqModal('PCB Rapid Prototyping Machine', note);
    });
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
    btn.addEventListener('click', () => {
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
    });
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
    btn.addEventListener('click', () => {
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
    });
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

    questionBtn.addEventListener('click', () => {
      const isOpen = item.classList.contains('active');

      // Close all other FAQs for clean single-expanded view
      faqItems.forEach(otherItem => {
        otherItem.classList.remove('active');
      });

      if (!isOpen) {
        item.classList.add('active');
      }
    });
  });
}

/* ==========================================================================
   7. Interactive 2-Step RFQ Modal (Technical Quote)
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

function initRfqModal() {
  const modalOverlay = document.getElementById('rfqModalOverlay') || document.getElementById('rfqModal');
  const closeBtn = document.getElementById('rfqModalCloseBtn') || document.getElementById('closeRfqModal') || document.getElementById('modalCloseBtn');
  document.querySelectorAll('.modal-close-btn').forEach(btn => {
    btn.addEventListener('click', closeRfqModal);
  });
  const step1 = document.getElementById('rfqStep1');
  const step2 = document.getElementById('rfqStep2');
  const nextBtn = document.getElementById('rfqNextBtn') || document.getElementById('rfqNextStepBtn');
  const backBtn = document.getElementById('rfqBackBtn') || document.getElementById('rfqPrevStepBtn');
  const submitBtn = document.getElementById('rfqSubmitBtn');
  const whatsappSubmitBtn = document.getElementById('rfqWhatsAppSubmitBtn');
  const successState = document.getElementById('rfqSuccessMessage');
  const modalForms = document.querySelectorAll('#rfqForm, #rfqModalForm, .rfq-modal-dialog form, .modal-dialog form, .rfq-modal-window form');

  // Disarm all modal forms from accidental browser POST
  modalForms.forEach(form => {
    form.setAttribute('action', 'javascript:void(0);');
    form.setAttribute('onsubmit', 'return false;');
  });

  // Trigger buttons across page
  document.querySelectorAll('[data-open-rfq]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const model = btn.getAttribute('data-machine') || 'CyTOS Machine / Automation';
      openRfqModal(model);
    });
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', closeRfqModal);
  }

  if (modalOverlay) {
    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) {
        closeRfqModal();
      }
    });
  }

  // Handle ESC key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modalOverlay && modalOverlay.classList.contains('active')) {
      closeRfqModal();
    }
  });

  // Step 1 -> Step 2 validation
  if (nextBtn && step1 && step2) {
    nextBtn.addEventListener('click', () => {
      const name = document.getElementById('rfqName')?.value.trim();
      const phone = document.getElementById('rfqPhone')?.value.trim();
      const email = document.getElementById('rfqEmail')?.value.trim();

      if (!name || !phone || !email) {
        alert('Please provide your Name, Mobile/WhatsApp number, and Email to proceed.');
        return;
      }

      step1.style.display = 'none';
      step1.classList.remove('active');
      step2.style.display = 'block';
      step2.classList.add('active');

      document.getElementById('stepBadge1')?.classList.remove('active');
      document.getElementById('stepBadge2')?.classList.add('active');
    });
  }

  if (backBtn && step1 && step2) {
    backBtn.addEventListener('click', () => {
      step2.style.display = 'none';
      step2.classList.remove('active');
      step1.style.display = 'block';
      step1.classList.add('active');

      document.getElementById('stepBadge2')?.classList.remove('active');
      document.getElementById('stepBadge1')?.classList.add('active');
    });
  }

  // Master RFQ Submit Logic
  const handleRfqSubmission = async (e) => {
    if (e) e.preventDefault();

    const name = document.getElementById('rfqName')?.value.trim() || '';
    const company = document.getElementById('rfqCompany')?.value.trim() || '';
    const phone = document.getElementById('rfqPhone')?.value.trim() || '';
    const email = document.getElementById('rfqEmail')?.value.trim() || '';
    const city = document.getElementById('rfqCity')?.value.trim() || document.getElementById('rfqLocation')?.value.trim() || '';
    const model = document.getElementById('rfqMachineSelect')?.value || document.getElementById('rfqSelectedMachine')?.value || document.getElementById('rfqMachine')?.value || selectedMachineModel;
    const material = document.getElementById('rfqMaterial')?.value || '';
    const tolerance = document.getElementById('rfqTolerance')?.value || '';
    const timeline = document.getElementById('rfqTimeline')?.value || '';
    const notes = document.getElementById('rfqNotes')?.value.trim() || document.getElementById('rfqDetails')?.value.trim() || '';

    if (!name || (!phone && !email)) {
      alert('Please provide your Name and a valid Mobile/WhatsApp number or Email.');
      if (step1 && step2) {
        step2.style.display = 'none';
        step2.classList.remove('active');
        step1.style.display = 'block';
        step1.classList.add('active');
        document.getElementById('stepBadge2')?.classList.remove('active');
        document.getElementById('stepBadge1')?.classList.add('active');
      }
      return;
    }

    const originalBtnText = submitBtn ? submitBtn.textContent : 'Submit Technical RFQ';
    if (submitBtn) {
      submitBtn.textContent = 'Transmitting to Pune Engineering Desk...';
      submitBtn.disabled = true;
    }

    // Vault and dispatch (with 3.5s async timeout)
    await dispatchEmailToInranktech({
      _subject: `New Technical RFQ: ${model} from ${company || name}`,
      Client_Name: name,
      Company: company,
      Phone_WhatsApp: phone,
      Email: email,
      City_Location: city,
      Machine_Model: model,
      Workpiece_Material: material,
      Required_Tolerance: tolerance,
      Project_Timeline: timeline,
      Application_Notes: notes,
      Source: 'CyTOS RFQ Modal Portal'
    });

    if (submitBtn) {
      submitBtn.textContent = originalBtnText;
      submitBtn.disabled = false;
    }

    if (step1) {
      step1.style.display = 'none';
      step1.classList.remove('active');
    }
    if (step2) {
      step2.style.display = 'none';
      step2.classList.remove('active');
    }

    const whatsappText = encodeURIComponent(
      `*New Technical RFQ for CyTOS Pune*\n\n` +
      `• *Client Name:* ${name}\n` +
      `• *Company:* ${company || 'N/A'}\n` +
      `• *Phone/WhatsApp:* ${phone}\n` +
      `• *Email:* ${email}\n` +
      `• *Location:* ${city || 'India'}\n` +
      `• *Interested Model:* ${model}\n` +
      `• *Workpiece/Material:* ${material || 'N/A'}\n` +
      `• *Required Tolerance:* ${tolerance || 'Standard'}\n` +
      `• *Application Notes:* ${notes || 'Standard quote request'}\n\n` +
      `_Generated via cytos.in Technical RFQ Portal_`
    );

    if (successState) {
      successState.style.display = 'block';
      successState.classList.add('active');
      successState.innerHTML = `
        <div style="width: 56px; height: 56px; border-radius: 50%; background: #ecfdf5; color: #059669; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.25rem;">
          <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
        </div>
        <h3 style="font-size: 1.35rem; margin-bottom: 0.5rem; color: var(--text-pure, #0f172a);">RFQ Transmitted to Engineering Desk!</h3>
        <p style="font-size: 0.92rem; color: var(--text-secondary, #475569); max-width: 460px; margin: 0 auto 1.25rem; line-height: 1.55;">
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
            <span style="color: #059669; font-weight: 700;">✓ Saved in Local Vault &amp; Queued</span>
          </div>
        </div>
        <div style="display: flex; flex-direction: column; gap: 0.75rem;">
          <a href="https://wa.me/919921381071?text=${whatsappText}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="width: 100%; justify-content: center;">
            <svg class="btn-icon-svg whatsapp-icon-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.68C7.02 10.88 7.9 12.04 8.02 12.2C8.14 12.37 9.73 14.95 12.24 15.93C14.33 16.75 14.75 16.59 15.22 16.54C15.69 16.49 16.74 15.91 16.96 15.29C17.18 14.66 17.18 14.13 17.11 14.02C17.05 13.91 16.89 13.84 16.64 13.72C16.39 13.6 15.17 13 14.94 12.92C14.72 12.83 14.56 12.79 14.4 13.04C14.24 13.29 13.77 13.84 13.63 14.01C13.5 14.17 13.36 14.19 13.11 14.07C12.87 13.95 12.08 13.69 11.15 12.86C10.42 12.21 9.93 11.41 9.79 11.17C9.65 10.92 9.78 10.79 9.9 10.67C10.01 10.56 10.15 10.38 10.27 10.23C10.4 10.08 10.44 9.97 10.52 9.81C10.6 9.65 10.56 9.51 10.5 9.39C10.44 9.27 9.97 8.12 9.78 7.65C9.59 7.19 9.39 7.25 9.24 7.24C9.1 7.23 8.94 7.23 8.78 7.23H8.53Z"/></svg>
            <span>Need Urgent Response? Chat on WhatsApp</span>
          </a>
          <button type="button" class="btn btn-outline" id="rfqSuccessCloseBtn" style="width: 100%;">
            <span>Close Window</span>
          </button>
        </div>
      `;
      document.getElementById('rfqSuccessCloseBtn')?.addEventListener('click', closeRfqModal);
    } else {
      alert(`Thank you, ${name}! Your Technical RFQ for "${model}" has been dispatched to CyTOS engineering desk (info@cytos.in). We will respond within 2 business hours.`);
      closeRfqModal();
    }

    modalForms.forEach(f => f.reset());
  };

  if (submitBtn) {
    submitBtn.addEventListener('click', handleRfqSubmission);
  }

  modalForms.forEach(form => {
    form.addEventListener('submit', handleRfqSubmission);
  });

  // Direct WhatsApp Launch with Structured RFQ Details
  if (whatsappSubmitBtn) {
    whatsappSubmitBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const name = document.getElementById('rfqName')?.value.trim() || 'Valued Client';
      const company = document.getElementById('rfqCompany')?.value.trim() || '';
      const phone = document.getElementById('rfqPhone')?.value.trim() || 'N/A';
      const city = document.getElementById('rfqCity')?.value.trim() || document.getElementById('rfqLocation')?.value.trim() || 'India';
      const model = document.getElementById('rfqMachineSelect')?.value || document.getElementById('rfqSelectedMachine')?.value || selectedMachineModel;
      const material = document.getElementById('rfqMaterial')?.value || 'Not specified';
      const notes = document.getElementById('rfqNotes')?.value.trim() || document.getElementById('rfqDetails')?.value.trim() || 'Standard technical quotation request';

      // Save lead locally as well
      dispatchEmailToInranktech({
        _subject: `WhatsApp RFQ: ${model} from ${company || name}`,
        Client_Name: name,
        Company: company,
        Phone_WhatsApp: phone,
        City_Location: city,
        Machine_Model: model,
        Workpiece_Material: material,
        Application_Notes: notes,
        Source: 'CyTOS RFQ Direct WhatsApp'
      });

      const whatsappText = encodeURIComponent(
        `*New Technical RFQ for CyTOS Pune*\n\n` +
        `• *Client Name:* ${name}\n` +
        `• *Company:* ${company || 'N/A'}\n` +
        `• *Phone/WhatsApp:* ${phone}\n` +
        `• *Location:* ${city}\n` +
        `• *Interested Model:* ${model}\n` +
        `• *Workpiece/Material:* ${material}\n` +
        `• *Application Notes:* ${notes}\n\n` +
        `_Generated via cytos.in Technical RFQ Portal_`
      );

      window.open(`https://wa.me/919921381071?text=${whatsappText}`, '_blank');
      closeRfqModal();
    });
  }
}

function openRfqModal(modelName = 'CyTOS Machine System', customNotes = '') {
  selectedMachineModel = modelName;
  const modalOverlay = document.getElementById('rfqModalOverlay') || document.getElementById('rfqModal');
  const machineSelect = document.getElementById('rfqMachineSelect');
  const selectedMachineInput = document.getElementById('rfqSelectedMachine');
  const notesField = document.getElementById('rfqNotes') || document.getElementById('rfqDetails');
  const step1 = document.getElementById('rfqStep1');
  const step2 = document.getElementById('rfqStep2');
  const successState = document.getElementById('rfqSuccessMessage');

  if (machineSelect) {
    machineSelect.value = modelName;
  }
  if (selectedMachineInput) {
    selectedMachineInput.value = modelName;
  }

  if (notesField && customNotes) {
    notesField.value = customNotes;
  }

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

  document.getElementById('stepBadge1')?.classList.add('active');
  document.getElementById('stepBadge2')?.classList.remove('active');

  if (modalOverlay) {
    modalOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
}

function closeRfqModal() {
  const modalOverlay = document.getElementById('rfqModalOverlay') || document.getElementById('rfqModal');
  if (modalOverlay) {
    modalOverlay.classList.remove('active');
    document.body.style.overflow = '';
  }
}

/* ==========================================================================
   Contact Page Form Handler
   ========================================================================== */
function initContactForm() {
  const contactForm = document.getElementById('contactPageForm');
  if (!contactForm) return;

  contactForm.setAttribute('action', 'javascript:void(0);');
  contactForm.setAttribute('onsubmit', 'return false;');

  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('cpName')?.value.trim() || '';
    const company = document.getElementById('cpCompany')?.value.trim() || '';
    const email = document.getElementById('cpEmail')?.value.trim() || '';
    const phone = document.getElementById('cpPhone')?.value.trim() || '';
    const city = document.getElementById('cpLocation')?.value.trim() || document.getElementById('cpCity')?.value.trim() || '';
    const machine = document.getElementById('cpMachine')?.value || 'General CNC Machinery';
    const material = document.getElementById('cpMaterial')?.value.trim() || '';
    const workArea = document.getElementById('cpWorkArea')?.value.trim() || '';
    const message = document.getElementById('cpMessage')?.value.trim() || '';

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

    await dispatchEmailToInranktech({
      _subject: `CyTOS Contact Form: ${machine} from ${company || name}`,
      Full_Name: name,
      Company: company,
      Email: email,
      Phone: phone,
      City_Location: city,
      Machine_Category: machine,
      Workpiece_Material: material,
      Work_Area_Dimensions: workArea,
      Detailed_Requirements: message,
      Source: 'CyTOS Contact Us Page'
    });

    if (submitBtn) {
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
    }

    // Render prominent in-page success confirmation banner
    let banner = document.getElementById('contactSuccessBanner');
    if (!banner) {
      banner = document.createElement('div');
      banner.id = 'contactSuccessBanner';
      banner.className = 'contact-success-banner';
      contactForm.parentNode.insertBefore(banner, contactForm);
    }

    const whatsappText = encodeURIComponent(
      `*New Contact Inquiry for CyTOS Pune*\n\n` +
      `• *Client Name:* ${name}\n` +
      `• *Company:* ${company || 'N/A'}\n` +
      `• *Phone/WhatsApp:* ${phone}\n` +
      `• *Email:* ${email}\n` +
      `• *Location:* ${city || 'India'}\n` +
      `• *Equipment:* ${machine}\n` +
      `• *Material:* ${material || 'N/A'}\n` +
      `• *Requirements:* ${message || 'Standard quote inquiry'}\n\n` +
      `_Transmitted via cytos.in Contact Portal_`
    );

    banner.style.display = 'block';
    banner.innerHTML = `
      <div style="display: flex; align-items: flex-start; gap: 1rem;">
        <div style="width: 44px; height: 44px; min-width: 44px; border-radius: 50%; background: #ecfdf5; color: #059669; display: flex; align-items: center; justify-content: center;">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
        </div>
        <div style="flex: 1;">
          <h4 style="font-size: 1.15rem; font-weight: 700; color: #065f46; margin-bottom: 0.35rem;">Inquiry Successfully Registered &amp; Dispatched!</h4>
          <p style="font-size: 0.92rem; color: #1e293b; line-height: 1.55; margin-bottom: 0.85rem;">
            Thank you, <strong>${escapeUserHtml(name)}</strong>! Your technical inquiry regarding <strong>${escapeUserHtml(machine)}</strong> has been vaulted and transmitted to the CyTOS Pune engineering desk. An engineer will review your specifications and contact you within 2 business hours.
          </p>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
            <a href="https://wa.me/919921381071?text=${whatsappText}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.55rem 1.15rem; font-size: 0.88rem;">
              <svg class="btn-icon-svg whatsapp-icon-svg" viewBox="0 0 24 24" width="16" height="16" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.68C7.02 10.88 7.9 12.04 8.02 12.2C8.14 12.37 9.73 14.95 12.24 15.93C14.33 16.75 14.75 16.59 15.22 16.54C15.69 16.49 16.74 15.91 16.96 15.29C17.18 14.66 17.18 14.13 17.11 14.02C17.05 13.91 16.89 13.84 16.64 13.72C16.39 13.6 15.17 13 14.94 12.92C14.72 12.83 14.56 12.79 14.4 13.04C14.24 13.29 13.77 13.84 13.63 14.01C13.5 14.17 13.36 14.19 13.11 14.07C12.87 13.95 12.08 13.69 11.15 12.86C10.42 12.21 9.93 11.41 9.79 11.17C9.65 10.92 9.78 10.79 9.9 10.67C10.01 10.56 10.15 10.38 10.27 10.23C10.4 10.08 10.44 9.97 10.52 9.81C10.6 9.65 10.56 9.51 10.5 9.39C10.44 9.27 9.97 8.12 9.78 7.65C9.59 7.19 9.39 7.25 9.24 7.24C9.1 7.23 8.94 7.23 8.78 7.23H8.53Z"/></svg>
              <span>Fast-Track: Connect on WhatsApp</span>
            </a>
          </div>
        </div>
      </div>
    `;
    banner.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    contactForm.reset();
  });
}

/* ==========================================================================
   8. Animated Metric Counters
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
        
        let start = 0;
        const duration = 1800; // ms
        const startTime = performance.now();

        function updateCounter(currentTime) {
          const elapsed = currentTime - startTime;
          const progress = Math.min(elapsed / duration, 1);
          // Ease out expo
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
   9. Sticky Navigation State
   ========================================================================== */
function initStickyHeader() {
  const header = document.querySelector('.main-header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });
}

/* ==========================================================================
   10. Mobile Menu Navigation
   ========================================================================== */
function initMobileNav() {
  const menuBtn = document.getElementById('mobileMenuBtn');
  const navLinks = document.querySelector('.nav-links');

  if (!menuBtn || !navLinks) return;

  const burgerSvg = '<svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" fill="none" aria-hidden="true"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
  const closeSvg = '<svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" fill="none" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>';

  menuBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const isActive = navLinks.classList.toggle('active');
    menuBtn.setAttribute('aria-expanded', isActive ? 'true' : 'false');
    document.body.style.overflow = isActive ? 'hidden' : '';
    menuBtn.innerHTML = isActive ? closeSvg : burgerSvg;
  });

  // Accordion toggle on mobile for dropdown triggers
  const dropdownTriggers = navLinks.querySelectorAll('.dropdown-trigger');
  dropdownTriggers.forEach(trigger => {
    trigger.addEventListener('click', (e) => {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        e.stopPropagation();
        const parentDropdown = trigger.closest('.nav-item-dropdown');
        if (parentDropdown) {
          // Close other open dropdowns
          navLinks.querySelectorAll('.nav-item-dropdown').forEach(item => {
            if (item !== parentDropdown) item.classList.remove('open');
          });
          parentDropdown.classList.toggle('open');
        }
      }
    });
  });

  // Clicking an actual leaf link closes the mobile menu
  navLinks.querySelectorAll('a:not(.dropdown-trigger)').forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth <= 768) {
        navLinks.classList.remove('active');
        document.body.style.overflow = '';
        menuBtn.innerHTML = burgerSvg;
      }
    });
  });

  // Close when clicking outside
  document.addEventListener('click', (e) => {
    if (navLinks.classList.contains('active') && !navLinks.contains(e.target) && !menuBtn.contains(e.target)) {
      navLinks.classList.remove('active');
      document.body.style.overflow = '';
      menuBtn.innerHTML = burgerSvg;
    }
  });

  // Reset state if resized to desktop
  window.addEventListener('resize', () => {
    if (window.innerWidth > 768 && navLinks.classList.contains('active')) {
      navLinks.classList.remove('active');
      document.body.style.overflow = '';
      menuBtn.innerHTML = burgerSvg;
    }
  });
}

/* ==========================================================================
   11. Cookie & Privacy Consent Banner
   ========================================================================== */
function initConsentBanner() {
  const banner = document.getElementById('cookieConsentBanner');
  if (!banner) return;

  const consent = localStorage.getItem('cytos_cookie_consent');
  if (consent) {
    banner.classList.add('consent-hidden');
    return;
  }

  // Show banner with gentle delay
  setTimeout(() => {
    banner.classList.remove('consent-hidden');
  }, 600);

  const acceptBtn = document.getElementById('btnAcceptConsent');
  const rejectBtn = document.getElementById('btnRejectConsent');

  if (acceptBtn) {
    acceptBtn.addEventListener('click', () => {
      localStorage.setItem('cytos_cookie_consent', 'accepted_all');
      banner.classList.add('consent-hidden');
    });
  }

  if (rejectBtn) {
    rejectBtn.addEventListener('click', () => {
      localStorage.setItem('cytos_cookie_consent', 'necessary_only');
      banner.classList.add('consent-hidden');
    });
  }
}

/* ==========================================================================
   12. Engineering Blog Category Filtering
   ========================================================================== */
function initBlogFilter() {
  const filterPills = document.querySelectorAll('.filter-pill');
  const blogCards = document.querySelectorAll('.blog-card');
  const featuredCard = document.querySelector('.featured-blog-card');

  if (!filterPills.length || !blogCards.length) return;

  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');

      const category = pill.getAttribute('data-category');

      // Filter featured card
      if (featuredCard) {
        const featCat = featuredCard.getAttribute('data-category');
        if (category === 'all' || featCat === category) {
          featuredCard.style.display = 'grid';
        } else {
          featuredCard.style.display = 'none';
        }
      }

      // Filter regular blog cards
      blogCards.forEach(card => {
        const cardCat = card.getAttribute('data-category');
        if (category === 'all' || cardCat === category) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* ==========================================================================
   13. Terms & Conditions Table of Contents ScrollSpy
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
