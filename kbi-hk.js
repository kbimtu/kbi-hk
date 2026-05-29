/* =============================================================
   KBI Hong Kong — kbi-hk.js v5 · 2026
   Interactions · Animations · Reveals · Counters · Carousel
   ============================================================= */

(function () {
  'use strict';

  /* ----------------------------------------------------------
     UTILITIES
  ---------------------------------------------------------- */
  function $(sel, ctx)  { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.from((ctx || document).querySelectorAll(sel)); }
  function on(el, ev, fn, opts) { if (el) el.addEventListener(ev, fn, opts || false); }

  var supportsIO = 'IntersectionObserver' in window;

  /* ----------------------------------------------------------
     ANNOUNCEMENT BAR
  ---------------------------------------------------------- */
  var annBar   = $('#announcementBar');
  var annClose = $('#announcementClose');
  if (annBar) {
    document.documentElement.classList.add('has-announcement-bar');
  }
  if (annBar && annClose) {
    on(annClose, 'click', function () {
      document.documentElement.classList.add('announcement-bar-hidden');
      annBar.style.maxHeight  = annBar.offsetHeight + 'px';
      requestAnimationFrame(function () {
        annBar.style.transition = 'max-height 0.4s ease, opacity 0.3s ease, padding 0.4s ease';
        annBar.style.maxHeight  = '0';
        annBar.style.opacity    = '0';
        annBar.style.padding    = '0';
        annBar.style.overflow   = 'hidden';
      });
      var nav = $('#siteNav');
      if (nav) { setTimeout(function () { nav.style.top = '0'; }, 420); }
    });
  }

  /* ----------------------------------------------------------
     HERO PARTICLES (lightweight CSS-driven)
  ---------------------------------------------------------- */
  var particleWrap = $('#heroParticles');
  if (particleWrap) {
    var count = window.innerWidth > 768 ? 18 : 9;
    for (var i = 0; i < count; i++) {
      var p = document.createElement('div');
      p.className = 'hero-particle';
      var size = Math.random() * 3 + 1.5;
      p.style.cssText = [
        'width:'  + size + 'px',
        'height:' + size + 'px',
        'left:'   + Math.random() * 100 + '%',
        'top:'    + (Math.random() * 60 + 30) + '%',
        'animation-duration:' + (Math.random() * 8 + 6) + 's',
        'animation-delay:'    + (Math.random() * 6)     + 's'
      ].join(';');
      particleWrap.appendChild(p);
    }
  }

  /* ----------------------------------------------------------
     NAVIGATION — sticky / colour swap
  ---------------------------------------------------------- */
  var nav      = $('#siteNav');
  var ticking  = false;

  function handleNavScroll() {
    if (!nav) return;
    var scrollY = window.scrollY;
    nav.classList.toggle('nav-scrolled', scrollY > 60);
    if (nav.classList.contains('nav-dark')) {
      var threshold = window.innerHeight * 0.72;
      if (scrollY > threshold) {
        nav.style.background       = 'rgba(255,255,255,0.97)';
        nav.style.borderBottomColor = 'var(--stone)';
        $$('.nav-wordmark-name', nav).forEach(function (el) { el.style.color = 'var(--text-main)'; });
        $$('.nav-wordmark-sub',  nav).forEach(function (el) { el.style.color = 'var(--text-faint)'; });
        $$('.nav-links > li > a, .nav-links > li > button', nav).forEach(function (el) { el.style.color = ''; });
        $$('.nav-hamburger span', nav).forEach(function (el) { el.style.background = 'var(--text-main)'; });
      } else {
        nav.style.background        = '';
        nav.style.borderBottomColor = '';
        $$('.nav-wordmark-name', nav).forEach(function (el) { el.style.color = ''; });
        $$('.nav-wordmark-sub',  nav).forEach(function (el) { el.style.color = ''; });
        $$('.nav-hamburger span',nav).forEach(function (el) { el.style.background = ''; });
      }
    }
    ticking = false;
  }

  on(window, 'scroll', function () {
    if (!ticking) { requestAnimationFrame(handleNavScroll); ticking = true; }
  }, { passive: true });
  handleNavScroll();

  /* ----------------------------------------------------------
     ACTIVE NAV LINK
  ---------------------------------------------------------- */
  (function setActive() {
    var page = window.location.pathname.split('/').pop() || 'index.html';
    if (!page) page = 'index.html';
    $$('.nav-links a, .nav-mobile-link').forEach(function (a) {
      var href = (a.getAttribute('href') || '').split('#')[0];
      if (href === page || (page === 'index.html' && href === '')) {
        a.classList.add('active');
        var li = a.closest('.has-dropdown');
        if (li) {
          var trigger = li.querySelector('.nav-dropdown-trigger');
          if (trigger) trigger.classList.add('active');
        }
      }
    });
  }());

  /* ----------------------------------------------------------
     DROPDOWNS
  ---------------------------------------------------------- */
  $$('.has-dropdown').forEach(function (li) {
    var btn  = li.querySelector('.nav-dropdown-trigger');
    var menu = li.querySelector('.nav-dropdown');
    if (!btn || !menu) return;

    on(btn, 'click', function (e) {
      e.stopPropagation();
      var wasOpen = li.classList.contains('open');
      $$('.has-dropdown.open').forEach(function (other) {
        other.classList.remove('open');
        var t = other.querySelector('.nav-dropdown-trigger');
        if (t) t.setAttribute('aria-expanded', 'false');
      });
      if (!wasOpen) {
        li.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });

    on(btn, 'keydown', function (e) {
      if (e.key === 'Escape') {
        li.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
        btn.focus();
      }
    });
  });

  on(document, 'click', function () {
    $$('.has-dropdown.open').forEach(function (li) {
      li.classList.remove('open');
      var t = li.querySelector('.nav-dropdown-trigger');
      if (t) t.setAttribute('aria-expanded', 'false');
    });
  });

  /* ----------------------------------------------------------
     MOBILE MENU
  ---------------------------------------------------------- */
  var hamburger = $('#navHamburger');
  var mobileNav = $('#navMobile');

  on(hamburger, 'click', function () {
    var isOpen = mobileNav && mobileNav.classList.toggle('open');
    if (hamburger) {
      hamburger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      hamburger.classList.toggle('open', !!isOpen);
    }
    document.body.style.overflow = isOpen ? 'hidden' : '';
  });

  $$('#navMobile a').forEach(function (a) {
    on(a, 'click', function () {
      if (mobileNav) mobileNav.classList.remove('open');
      if (hamburger) { hamburger.classList.remove('open'); hamburger.setAttribute('aria-expanded', 'false'); }
      document.body.style.overflow = '';
    });
  });

  on(document, 'keydown', function (e) {
    if (e.key === 'Escape' && mobileNav && mobileNav.classList.contains('open')) {
      mobileNav.classList.remove('open');
      if (hamburger) { hamburger.classList.remove('open'); hamburger.setAttribute('aria-expanded', 'false'); hamburger.focus(); }
      document.body.style.overflow = '';
    }
  });

  /* ----------------------------------------------------------
     SMOOTH SCROLL
  ---------------------------------------------------------- */
  on(document, 'click', function (e) {
    var a = e.target.closest('a[href^="#"]');
    if (!a) return;
    var id = a.getAttribute('href').slice(1);
    if (!id) return;
    var target = document.getElementById(id);
    if (target) {
      e.preventDefault();
      var navH   = nav ? nav.offsetHeight : 68;
      var annH   = annBar && annBar.offsetHeight > 0 ? annBar.offsetHeight : 0;
      var top    = target.getBoundingClientRect().top + window.scrollY - navH - annH - 16;
      window.scrollTo({ top: top, behavior: 'smooth' });
    }
  });

  /* ----------------------------------------------------------
     SCROLL REVEAL (IntersectionObserver)
  ---------------------------------------------------------- */
  function initReveal() {
    var els = $$('.reveal');
    if (!els.length) return;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.07, rootMargin: '0px 0px -28px 0px' });

    els.forEach(function (el) { io.observe(el); });
  }

  if (supportsIO) {
    initReveal();
  } else {
    $$('.reveal').forEach(function (el) { el.classList.add('revealed'); });
  }

  /* ----------------------------------------------------------
     STAGGER CHILDREN REVEAL
  ---------------------------------------------------------- */
  $$('.stagger-children').forEach(function (parent) {
    Array.from(parent.children).forEach(function (child, i) {
      child.classList.add('reveal');
      child.style.transitionDelay = (i * 0.08) + 's';
    });
  });

  /* ----------------------------------------------------------
     ANIMATED COUNTERS
  ---------------------------------------------------------- */
  function animateCounter(el) {
    var suffix    = el.querySelector('span');
    var suffixTxt = suffix ? suffix.textContent : '';
    var raw       = el.textContent.replace(suffixTxt, '').trim();
    var num       = parseFloat(raw.replace(/[^0-9.]/g, ''));
    if (isNaN(num)) return;
    var hasComma = raw.includes(',');
    var duration = 1800;
    var start    = null;

    function step(ts) {
      if (!start) start = ts;
      var prog   = Math.min((ts - start) / duration, 1);
      var eased  = 1 - Math.pow(1 - prog, 3);
      var val    = Math.round(num * eased);
      var disp   = (num >= 1000 || hasComma) ? val.toLocaleString() : String(val);
      el.textContent = disp;
      if (suffix) el.appendChild(suffix);
      if (prog < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  var counterEls = $$('.stats-bar-number, .impact-stat-n');
  if (counterEls.length && supportsIO) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { animateCounter(entry.target); cio.unobserve(entry.target); }
      });
    }, { threshold: 0.5 });
    counterEls.forEach(function (el) { cio.observe(el); });
  }

  /* ----------------------------------------------------------
     PROGRAMME TABS
  ---------------------------------------------------------- */
  var progTabBtns   = $$('.prog-tab');
  var progTabPanels = $$('.prog-tab-panel');

  if (progTabBtns.length) {
    function showProgTab(target) {
      progTabBtns.forEach(function (b) {
        b.classList.toggle('active', b.dataset.tab === target);
        b.setAttribute('aria-selected', b.dataset.tab === target ? 'true' : 'false');
      });
      progTabPanels.forEach(function (p) {
        p.classList.toggle('active', p.id === 'prog-' + target);
      });
    }
    progTabBtns.forEach(function (btn) {
      on(btn, 'click', function () { showProgTab(btn.dataset.tab); });
    });

    /* Deep-link: activate correct tab based on URL hash
       e.g. programmes.html#ibcol  → switch to "olympiads" tab
            programmes.html#idsol  → switch to "olympiads" tab
            programmes.html#iqcol  → switch to "olympiads" tab
            programmes.html#eto    → switch to "flagship" tab
            programmes.html#training → switch to "training" tab
            programmes.html#community → switch to "community" tab          */
    var hashTabMap = {
      'eto':       'flagship',
      'eto-tracks':'flagship',
      'eto-streams':'flagship',
      'ibcol':     'olympiads',
      'idsol':     'olympiads',
      'iqcol':     'olympiads',
      'training':  'training',
      'community': 'community',
      'groups':    'community'
    };
    function applyHashTab() {
      var hash = (window.location.hash || '').replace('#', '');
      if (hash && hashTabMap[hash]) {
        showProgTab(hashTabMap[hash]);
        var target = document.getElementById(hash);
        if (target) { setTimeout(function () { target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 100); }
      }
    }
    applyHashTab();
    on(window, 'hashchange', applyHashTab);
  }

  /* ----------------------------------------------------------
     AUDIENCE / STAKEHOLDER TABS
  ---------------------------------------------------------- */
  var audTabs   = $$('.audience-tab');
  var audPanels = $$('.audience-panel');

  if (audTabs.length) {
    function showAudTab(target) {
      audTabs.forEach(function (b) {
        b.classList.toggle('active', b.dataset.audience === target);
      });
      audPanels.forEach(function (p) {
        p.classList.toggle('active', p.dataset.audience === target);
      });
    }
    audTabs.forEach(function (btn) {
      on(btn, 'click', function () { showAudTab(btn.dataset.audience); });
    });
  }

  /* ----------------------------------------------------------
     EVENTS TABS
  ---------------------------------------------------------- */
  var evtTabs   = $$('.events-tab');
  var evtPanels = $$('.events-tab-panel');

  if (evtTabs.length) {
    function showEvtTab(target) {
      evtTabs.forEach(function (b) {
        b.classList.toggle('active', b.dataset.tab === target);
      });
      evtPanels.forEach(function (p) {
        p.classList.toggle('active', p.id === 'evt-' + target);
      });
    }
    evtTabs.forEach(function (btn) {
      on(btn, 'click', function () { showEvtTab(btn.dataset.tab); });
    });
  }

  /* ----------------------------------------------------------
     EVENTS CAROUSEL
  ---------------------------------------------------------- */
  $$('.events-carousel').forEach(function (carousel) {
    var track  = carousel.querySelector('.events-carousel-track');
    var cards  = carousel.querySelectorAll('.event-card');
    var dotsEl = carousel.querySelector('.carousel-dots');
    var prevBtn= carousel.querySelector('.carousel-btn-prev');
    var nextBtn= carousel.querySelector('.carousel-btn-next');

    if (!track || cards.length < 2) return;

    var current    = 0;
    var perPage    = window.innerWidth > 1023 ? 3 : window.innerWidth > 700 ? 2 : 1;
    var total      = Math.ceil(cards.length / perPage);
    var autoTimer  = null;
    var touchStartX = 0;

    // Build dots
    if (dotsEl) {
      dotsEl.innerHTML = '';
      for (var d = 0; d < total; d++) {
        var dot = document.createElement('button');
        dot.className = 'carousel-dot' + (d === 0 ? ' active' : '');
        dot.setAttribute('aria-label', 'Go to slide ' + (d + 1));
        (function(idx) { on(dot, 'click', function () { goTo(idx); }); }(d));
        dotsEl.appendChild(dot);
      }
    }

    function updateDots() {
      if (!dotsEl) return;
      $$('.carousel-dot', dotsEl).forEach(function (dot, i) {
        dot.classList.toggle('active', i === current);
      });
    }

    function goTo(idx) {
      current = (idx + total) % total;
      var cardW   = cards[0].offsetWidth + 20;
      var offset  = current * perPage * cardW;
      track.style.transform = 'translateX(-' + offset + 'px)';
      updateDots();
    }

    if (prevBtn) on(prevBtn, 'click', function () { goTo(current - 1); });
    if (nextBtn) on(nextBtn, 'click', function () { goTo(current + 1); });

    // Touch / swipe
    on(track, 'touchstart', function (e) { touchStartX = e.touches[0].clientX; }, { passive: true });
    on(track, 'touchend',   function (e) {
      var diff = touchStartX - e.changedTouches[0].clientX;
      if (Math.abs(diff) > 40) goTo(diff > 0 ? current + 1 : current - 1);
    });

    // Auto-rotate
    function startAuto() { autoTimer = setInterval(function () { goTo(current + 1); }, 5000); }
    function stopAuto()  { clearInterval(autoTimer); }
    startAuto();
    on(carousel, 'mouseenter', stopAuto);
    on(carousel, 'mouseleave', startAuto);

    on(window, 'resize', function () {
      perPage = window.innerWidth > 1023 ? 3 : window.innerWidth > 700 ? 2 : 1;
      total   = Math.ceil(cards.length / perPage);
      current = 0;
      track.style.transform = 'translateX(0)';
      if (dotsEl) {
        dotsEl.innerHTML = '';
        for (var d = 0; d < total; d++) {
          var dot2 = document.createElement('button');
          dot2.className = 'carousel-dot' + (d === 0 ? ' active' : '');
          (function(idx) { on(dot2, 'click', function () { goTo(idx); }); }(d));
          dotsEl.appendChild(dot2);
        }
      }
    });
  });

  /* ----------------------------------------------------------
     NEWS FILTERS
  ---------------------------------------------------------- */
  var newsFilterBtns = $$('.news-filter-btn');
  var newsCards      = $$('.news-all-card[data-category], .news-card[data-category]');

  if (newsFilterBtns.length) {
    newsFilterBtns.forEach(function (btn) {
      on(btn, 'click', function () {
        newsFilterBtns.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        var cat = btn.dataset.filter;
        newsCards.forEach(function (card) {
          var show = cat === 'all' || card.dataset.category === cat;
          card.style.display = show ? '' : 'none';
          if (show) {
            card.style.animation = 'fadeIn 0.3s ease both';
          }
        });
      });
    });
  }

  /* ----------------------------------------------------------
     TIMELINE REVEAL
  ---------------------------------------------------------- */
  var timelineItems = $$('.timeline-item');
  if (timelineItems.length && supportsIO) {
    var tio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          tio.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 });
    timelineItems.forEach(function (el, i) {
      el.style.transitionDelay = (i * 0.1) + 's';
      tio.observe(el);
    });
  } else {
    timelineItems.forEach(function (el) { el.classList.add('revealed'); });
  }

  /* ----------------------------------------------------------
     FORM HANDLING (contact, sponsor enquiry, membership, newsletter)
  ---------------------------------------------------------- */
  function handleForm(formId, successId) {
    var form    = $('#' + formId);
    var success = $('#' + successId);
    if (!form) return;

    on(form, 'submit', function (e) {
      e.preventDefault();
      var inputs = $$('input[required], textarea[required], select[required]', form);
      var valid  = true;
      inputs.forEach(function (inp) {
        inp.style.borderColor = '';
        if (!inp.value.trim()) {
          inp.style.borderColor = '#ef4444';
          valid = false;
        }
        if (inp.type === 'email' && inp.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(inp.value)) {
          inp.style.borderColor = '#ef4444';
          valid = false;
        }
      });
      if (!valid) return;

      if (formId === 'contactForm') {
        var contactName    = (form.querySelector('#ct-name') || {}).value || '';
        var contactEmail   = (form.querySelector('#ct-email') || {}).value || '';
        var contactOrg     = (form.querySelector('#ct-org') || {}).value || '';
        var enquiryType    = (form.querySelector('#ct-subject') || {}).value || 'General Enquiry';
        var contactMessage = (form.querySelector('#ct-msg') || {}).value || '';
        var subject = enquiryType.trim() || 'General Enquiry';
        var body =
          'Name: ' + contactName + '\n' +
          'Email: ' + contactEmail + '\n' +
          'Organisation: ' + (contactOrg || '-') + '\n' +
          'Enquiry Type: ' + subject + '\n\n' +
          'Message:\n' + contactMessage;
        var mailtoHref =
          'mailto:hongkong@kb.institute' +
          '?subject=' + encodeURIComponent(subject) +
          '&body=' + encodeURIComponent(body);
        window.location.href = mailtoHref;
      }

      if (formId === 'membershipForm') {
        var memName        = (form.querySelector('#mem-name') || {}).value || '';
        var memEmail       = (form.querySelector('#mem-email') || {}).value || '';
        var memInstitution = (form.querySelector('#mem-institution') || {}).value || '';
        var memInvolvement = (form.querySelector('#mem-involvement') || {}).value || '';
        var memMessage     = (form.querySelector('#mem-msg') || {}).value || '';
        var interests = [];
        form.querySelectorAll('input[name="interest"]:checked').forEach(function (cb) {
          interests.push(cb.value);
        });
        var subject = 'KBI Membership Application';
        var body =
          'Name: ' + memName + '\n' +
          'Email: ' + memEmail + '\n' +
          'School / University / Organisation: ' + (memInstitution || '-') + '\n' +
          'How involved: ' + (memInvolvement || '-') + '\n' +
          'Areas of interest: ' + (interests.length ? interests.join(', ') : '-') + '\n\n' +
          'About:\n' + (memMessage || '-');
        var memMailto =
          'mailto:kbi-hongkong@kb.institute' +
          '?subject=' + encodeURIComponent(subject) +
          '&body=' + encodeURIComponent(body);
        window.location.href = memMailto;
      }

      var btn = form.querySelector('[type="submit"]');
      if (btn) {
        var orig = btn.textContent;
        btn.disabled    = true;
        btn.textContent = 'Sending…';
        setTimeout(function () {
          btn.disabled    = false;
          btn.textContent = orig;
          form.reset();
          if (success) { success.classList.add('visible'); setTimeout(function () { success.classList.remove('visible'); }, 5000); }
        }, 1200);
      }
    });
  }

  handleForm('contactForm',        'contactSuccess');
  handleForm('contactForm',        'contactFormSuccess');
  handleForm('enquiryForm',        'enquirySuccess');
  handleForm('sponsorEnquiryForm', 'sponsorEnquirySuccess');
  handleForm('membershipForm',     'membershipSuccess');
  handleForm('membershipForm',     'membershipFormSuccess');

  /* Newsletter */
  var nlForm = $('#newsletterForm');
  if (nlForm) {
    on(nlForm, 'submit', function (e) {
      e.preventDefault();
      var inp = nlForm.querySelector('input[type="email"]');
      var btn = nlForm.querySelector('[type="submit"]');
      if (!inp || !inp.value.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(inp.value)) {
        if (inp) { inp.style.borderColor = '#ef4444'; setTimeout(function () { inp.style.borderColor = ''; }, 2000); }
        return;
      }
      if (btn) {
        var origText = btn.textContent.trim() || 'Subscribe';
        btn.disabled    = true;
        btn.textContent = '✓ Subscribed';
        btn.style.background = '#22c55e';
        btn.style.borderColor= '#22c55e';
        inp.value = '';
        setTimeout(function () {
          btn.disabled    = false;
          btn.textContent = origText;
          btn.style.background = '';
          btn.style.borderColor= '';
        }, 3500);
      }
    });
  }

  /* ----------------------------------------------------------
     BACK TO TOP
  ---------------------------------------------------------- */
  var btt = $('#backToTop');
  if (btt) {
    on(window, 'scroll', function () {
      btt.classList.toggle('visible', window.scrollY > 400);
    }, { passive: true });
    on(btt, 'click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ----------------------------------------------------------
     HERO VIDEO FALLBACK
  ---------------------------------------------------------- */
  var heroVideo = $('.hero-video');
  if (heroVideo) {
    on(heroVideo, 'error', function () {
      var wrap = heroVideo.closest('.hero-video-wrap');
      if (wrap) wrap.style.background = 'var(--night)';
      heroVideo.style.display = 'none';
    });
  }

  /* ----------------------------------------------------------
     HOVER TILT on cards (subtle 3D)
  ---------------------------------------------------------- */
  $$('.what-card, .prog-card, .event-card, .news-all-card').forEach(function (card) {
    on(card, 'mousemove', function (e) {
      var rect = card.getBoundingClientRect();
      var x    = (e.clientX - rect.left) / rect.width  - 0.5;
      var y    = (e.clientY - rect.top)  / rect.height - 0.5;
      card.style.transform = 'translateY(-4px) rotateX(' + (-y * 4) + 'deg) rotateY(' + (x * 4) + 'deg)';
    });
    on(card, 'mouseleave', function () {
      card.style.transform = '';
      card.style.transition = 'transform 0.5s cubic-bezier(0.34,1.56,0.64,1)';
    });
  });

  /* ----------------------------------------------------------
     SPONSOR LOGO MARQUEE (trust band)
  ---------------------------------------------------------- */
  var trustLogos = $('.trust-logos');
  if (trustLogos && trustLogos.children.length) {
    // No JS required — CSS animation via .trust-band handles display
  }

  /* ----------------------------------------------------------
     SECTION PROGRESS INDICATOR (thin line at top of viewport)
  ---------------------------------------------------------- */
  var progressBar = document.createElement('div');
  progressBar.style.cssText = 'position:fixed;top:0;left:0;height:2px;background:linear-gradient(90deg,var(--prussian),var(--cyan));z-index:9999;transition:width 0.1s linear;width:0%;pointer-events:none;';
  document.body.appendChild(progressBar);

  on(window, 'scroll', function () {
    var doc  = document.documentElement;
    var winH = doc.scrollHeight - doc.clientHeight;
    var pct  = winH > 0 ? (window.scrollY / winH) * 100 : 0;
    progressBar.style.width = pct + '%';
  }, { passive: true });

  /* Language switcher disabled until translation rollout. */
  (function initLangSwitcher_DISABLED() {
    return;
    var LANG_KEY  = 'kbi-lang';
    var LANGS     = ['en', 'tc', 'sc'];
    var DEFAULT   = 'en';

    /* Read persisted preference */
    var current = (localStorage.getItem(LANG_KEY) || DEFAULT);
    if (LANGS.indexOf(current) === -1) current = DEFAULT;

    /* Apply translations to all data-en/data-tc/data-sc nodes */
    function applyLang(lang) {
      $$('[data-en]').forEach(function (el) {
        var text = el.getAttribute('data-' + lang) || el.getAttribute('data-en') || '';
        /* Preserve child elements — only replace if element has no child elements */
        if (!el.children.length) {
          el.textContent = text;
        }
      });
      /* Update html[lang] attribute */
      var htmlEl = document.documentElement;
      if (lang === 'tc') htmlEl.setAttribute('lang', 'zh-Hant');
      else if (lang === 'sc') htmlEl.setAttribute('lang', 'zh-Hans');
      else htmlEl.setAttribute('lang', 'en');
    }

    /* Update all switcher buttons (desktop + mobile) */
    function updateButtons(lang) {
      $$('.lang-btn').forEach(function (btn) {
        btn.classList.toggle('active', btn.dataset.lang === lang);
        btn.setAttribute('aria-pressed', btn.dataset.lang === lang ? 'true' : 'false');
      });
    }

    /* Switch to a language */
    function switchLang(lang) {
      if (LANGS.indexOf(lang) === -1) return;
      current = lang;
      localStorage.setItem(LANG_KEY, lang);
      applyLang(lang);
      updateButtons(lang);
    }

    /* Wire up all .lang-btn clicks */
    function bindButtons() {
      $$('.lang-btn').forEach(function (btn) {
        on(btn, 'click', function () {
          switchLang(btn.dataset.lang);
        });
      });
    }

    /* Inject the switcher HTML into every .nav-inner that doesn't already have one */
    function injectSwitcher() {
      $$('.nav-inner').forEach(function (inner) {
        if (inner.querySelector('.lang-switcher')) return; /* already present */
        var sw = document.createElement('div');
        sw.className = 'lang-switcher';
        sw.setAttribute('role', 'group');
        sw.setAttribute('aria-label', 'Language');
        sw.innerHTML =
          '<button class="lang-btn" data-lang="en"  aria-pressed="false">EN</button>' +
          '<button class="lang-btn" data-lang="tc"  aria-pressed="false">繁中</button>' +
          '<button class="lang-btn" data-lang="sc"  aria-pressed="false">简中</button>';
        /* Insert before .nav-ctas if it exists, else append */
        var ctas = inner.querySelector('.nav-ctas');
        if (ctas) { inner.insertBefore(sw, ctas); }
        else       { inner.appendChild(sw); }
      });

      /* Mobile nav lang strip */
      $$('.nav-mobile').forEach(function (mob) {
        if (mob.querySelector('.nav-mobile-lang')) return;
        var strip = document.createElement('div');
        strip.className = 'nav-mobile-lang';
        strip.setAttribute('role', 'group');
        strip.setAttribute('aria-label', 'Language');
        strip.innerHTML =
          '<button class="lang-btn" data-lang="en"  aria-pressed="false">EN — English</button>' +
          '<button class="lang-btn" data-lang="tc"  aria-pressed="false">繁中 — 繁體</button>' +
          '<button class="lang-btn" data-lang="sc"  aria-pressed="false">简中 — 简体</button>';
        mob.appendChild(strip);
      });
    }

    /* Run */
    injectSwitcher();
    bindButtons();
    applyLang(current);
    updateButtons(current);
  }());

  /* ----------------------------------------------------------
     EVENT GALLERY — horizontal photo strips + lightbox
  ---------------------------------------------------------- */
  function ensureGalleryLightbox() {
    var lb = $('#lightbox');
    if (lb) return lb;
    lb = document.createElement('div');
    lb.id = 'lightbox';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-label', 'Photo viewer');
    lb.innerHTML =
      '<button id="lightboxClose" type="button" aria-label="Close photo viewer">\u2715</button>' +
      '<button id="lightboxPrev" type="button" class="lightbox-nav lightbox-nav--prev" aria-label="Previous photo">\u2039</button>' +
      '<button id="lightboxNext" type="button" class="lightbox-nav lightbox-nav--next" aria-label="Next photo">\u203A</button>' +
      '<img id="lightboxImg" src="" alt="">' +
      '<p id="lightboxCaption"></p>';
    document.body.appendChild(lb);
    return lb;
  }

  var galleryLightbox = ensureGalleryLightbox();
  var lightboxItems = [];
  var lightboxIndex = 0;

  function photoItemFrom(el) {
    if (!el) return null;
    if (el.classList.contains('photo-strip-item') || el.classList.contains('photo-card')) return el;
    return el.closest('.photo-strip-item, .photo-card');
  }

  function collectLightboxGroup(item) {
    if (!item) return [];
    var track = item.closest('.photo-strip-track');
    if (track) return $$('.photo-strip-item', track);
    var grid = item.closest('.photo-grid');
    if (grid) return $$('.photo-card', grid);
    return [item];
  }

  function lightboxItemData(item) {
    var img = item.querySelector('img');
    if (!img) return null;
    return {
      src: img.currentSrc || img.src,
      alt: img.alt || '',
      caption: item.getAttribute('data-caption') || img.alt || ''
    };
  }

  function showLightboxAt(index) {
    if (!galleryLightbox || !lightboxItems.length) return;
    var galleryLightboxImg = $('#lightboxImg');
    var galleryLightboxCaption = $('#lightboxCaption');
    var galleryLightboxPrev = $('#lightboxPrev');
    var galleryLightboxNext = $('#lightboxNext');
    lightboxIndex = (index + lightboxItems.length) % lightboxItems.length;
    var data = lightboxItems[lightboxIndex];
    if (galleryLightboxImg) {
      galleryLightboxImg.src = data.src;
      galleryLightboxImg.alt = data.alt;
    }
    if (galleryLightboxCaption) galleryLightboxCaption.textContent = data.caption;
    var multi = lightboxItems.length > 1;
    if (galleryLightboxPrev) galleryLightboxPrev.disabled = !multi;
    if (galleryLightboxNext) galleryLightboxNext.disabled = !multi;
    galleryLightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  if (galleryLightbox && !galleryLightbox.dataset.lightboxInit) {
    galleryLightbox.dataset.lightboxInit = '1';
    var galleryLightboxClose = $('#lightboxClose');
    var galleryLightboxPrev = $('#lightboxPrev');
    var galleryLightboxNext = $('#lightboxNext');

    window.openLightbox = function (card) {
      var item = photoItemFrom(card);
      if (!item) return;
      var group = collectLightboxGroup(item);
      lightboxItems = group.map(lightboxItemData).filter(Boolean);
      if (!lightboxItems.length) return;
      var start = group.indexOf(item);
      showLightboxAt(start >= 0 ? start : 0);
      if (galleryLightboxClose) galleryLightboxClose.focus();
    };

    function closeGalleryLightbox() {
      galleryLightbox.classList.remove('active');
      document.body.style.overflow = '';
      lightboxItems = [];
    }

    function stepLightbox(delta) {
      if (!galleryLightbox.classList.contains('active') || lightboxItems.length < 2) return;
      showLightboxAt(lightboxIndex + delta);
    }

    if (galleryLightboxClose) on(galleryLightboxClose, 'click', closeGalleryLightbox);
    if (galleryLightboxPrev) on(galleryLightboxPrev, 'click', function (e) { e.stopPropagation(); stepLightbox(-1); });
    if (galleryLightboxNext) on(galleryLightboxNext, 'click', function (e) { e.stopPropagation(); stepLightbox(1); });
    on(galleryLightbox, 'click', function (e) {
      if (e.target === galleryLightbox) closeGalleryLightbox();
    });
    on(document, 'keydown', function (e) {
      if (!galleryLightbox.classList.contains('active')) return;
      if (e.key === 'Escape') closeGalleryLightbox();
      if (e.key === 'ArrowLeft') stepLightbox(-1);
      if (e.key === 'ArrowRight') stepLightbox(1);
    });
  }

  $$('.photo-strip-wrap').forEach(function (wrap) {
    var scroll = $('.photo-strip-scroll', wrap);
    var track = $('.photo-strip-track', wrap);
    if (!scroll || !track) return;

    function updateStripLayout() {
      var overflows = scroll.scrollWidth > scroll.clientWidth + 2;
      scroll.classList.toggle('photo-strip-scroll--center', !overflows);
    }

    on(scroll, 'scroll', updateStripLayout, { passive: true });
    on(window, 'resize', updateStripLayout);
    updateStripLayout();

    on(scroll, 'wheel', function (e) {
      if (scroll.scrollWidth <= scroll.clientWidth + 2) return;
      var delta = Math.abs(e.deltaX) > Math.abs(e.deltaY) ? e.deltaX : e.deltaY;
      if (!delta) return;
      e.preventDefault();
      scroll.scrollLeft += delta;
    }, { passive: false });

    var drag = { active: false, startX: 0, startScroll: 0, moved: false, suppressClick: false };
    on(scroll, 'pointerdown', function (e) {
      if (e.button !== 0) return;
      drag.active = true;
      drag.moved = false;
      drag.suppressClick = false;
      drag.startX = e.clientX;
      drag.startScroll = scroll.scrollLeft;
      scroll.classList.add('is-dragging');
      if (scroll.setPointerCapture) scroll.setPointerCapture(e.pointerId);
    });
    on(scroll, 'pointermove', function (e) {
      if (!drag.active) return;
      var dx = e.clientX - drag.startX;
      if (Math.abs(dx) > 4) drag.moved = true;
      scroll.scrollLeft = drag.startScroll - dx;
    });
    on(scroll, 'pointerup', function (e) {
      if (!drag.active) return;
      drag.suppressClick = drag.moved;
      drag.active = false;
      drag.moved = false;
      scroll.classList.remove('is-dragging');
      if (scroll.releasePointerCapture) {
        try { scroll.releasePointerCapture(e.pointerId); } catch (err) { /* noop */ }
      }
      updateStripLayout();
    });
    on(scroll, 'pointercancel', function () {
      drag.active = false;
      drag.moved = false;
      drag.suppressClick = false;
      scroll.classList.remove('is-dragging');
    });

    $$('.photo-strip-item', track).forEach(function (btn) {
      on(btn, 'click', function () {
        if (drag.suppressClick) {
          drag.suppressClick = false;
          return;
        }
        if (typeof window.openLightbox === 'function') window.openLightbox(btn);
      });
    });

    track.querySelectorAll('img').forEach(function (img) {
      if (img.complete) return;
      on(img, 'load', updateStripLayout, { once: true });
    });
  });

  /* ----------------------------------------------------------
     BRAND — favicon + logo paths from kbi-hk.js location
  ---------------------------------------------------------- */
  (function initBrandAssets() {
    var script = document.querySelector('script[src*="kbi-hk.js"]');
    if (!script) return;
    var root = script.getAttribute('src').replace(/kbi-hk\.js(\?.*)?$/, '');
    var brand = root + 'assets/brand/';

    if (!document.querySelector('link[rel="icon"]')) {
      var icon = document.createElement('link');
      icon.rel = 'icon';
      icon.type = 'image/png';
      icon.sizes = '32x32';
      icon.href = brand + 'favicon-32.png';
      document.head.appendChild(icon);
    }
    if (!document.querySelector('link[rel="apple-touch-icon"]')) {
      var apple = document.createElement('link');
      apple.rel = 'apple-touch-icon';
      apple.href = brand + 'apple-touch-icon.png';
      document.head.appendChild(apple);
    }

    $$('.brand-mark-img').forEach(function (img) {
      if (!img.getAttribute('src') || img.getAttribute('src') === '') {
        img.src = brand + 'logo-icon.png';
      }
    });
  })();

  /* ----------------------------------------------------------
     INIT — announce active page on load
  ---------------------------------------------------------- */
  document.documentElement.classList.add('js-loaded');

}());
