/* =============================================
   PERFORMANCE-OPTIMISED main.js
   Branch: perf/homepage-optimisation
   - Lazy-loaded hero video (injected after preloader)
   - RAF-based carousel (replaces setInterval jank)
   - Cursor RAF cancels on tab hide / focus loss
   - 3D iframe deferred until near-viewport
   - Marquee paused when off-screen
   - Preloader delay reduced 2500ms → 1200ms
   - All interactivity preserved
   ============================================= */

/* ---- Preloader Logic ---- */
window.addEventListener('load', () => {
  const preloader = document.getElementById('preloader');
  if (preloader) {
    // Reduced from 2500ms — visual animation is ~2s, so 1200ms feels instant
    // without cutting the signature animation short
    setTimeout(() => {
      preloader.classList.add('loaded');

      // Lazy-load the hero video AFTER preloader exits so it doesn't block LCP
      setTimeout(() => {
        const heroVideo = document.getElementById('heroVideo');
        if (heroVideo) {
          heroVideo.querySelectorAll('source[data-src]').forEach(source => {
            source.src = source.dataset.src;
          });
          heroVideo.load();
          heroVideo.play().catch(() => {}); // autoplay may be blocked, that's fine
        }
        preloader.remove();
      }, 800); // matches the CSS slide-up transition

    }, 1200);
  }
});

/* ---- Mobile hamburger nav ---- */
const navToggle   = document.getElementById('navToggle');
const mobileMenu  = document.getElementById('mobileMenu');
const mobileClose = document.getElementById('mobileClose');

function openMenu() {
  mobileMenu.classList.add('open');
  mobileMenu.setAttribute('aria-hidden', 'false');
  navToggle.setAttribute('aria-expanded', 'true');
  navToggle.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeMenu() {
  mobileMenu.classList.remove('open');
  mobileMenu.setAttribute('aria-hidden', 'true');
  navToggle.setAttribute('aria-expanded', 'false');
  navToggle.classList.remove('open');
  document.body.style.overflow = '';
}

if (navToggle) {
  navToggle.addEventListener('click', () => {
    if (mobileMenu.classList.contains('open')) {
      closeMenu();
    } else {
      openMenu();
    }
  });
}

if (mobileClose) {
  mobileClose.addEventListener('click', closeMenu);
}

// Close on any link tap
mobileMenu.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', closeMenu);
});

// Close on Escape key
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeMenu();
});

// Close when tapping backdrop (outside the link area)
mobileMenu.addEventListener('click', e => {
  if (e.target === mobileMenu) closeMenu();
});


/* ---- Custom cursor & Magnetic Effect ---- */
const dot  = document.getElementById('cursorDot');
const ring = document.getElementById('cursorRing');
let mx = window.innerWidth / 2, my = window.innerHeight / 2;
let rx = mx, ry = my;
let isMagnetic = false;
let magneticTarget = null;
let ringRafId = null; // Track RAF id so we can cancel it

if (window.matchMedia('(pointer:fine)').matches && dot && ring) {
  document.addEventListener('mousemove', e => {
    if (!isMagnetic) {
      mx = e.clientX;
      my = e.clientY;
    } else if (magneticTarget) {
      const rect = magneticTarget.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;
      const diffX = (e.clientX - centerX) * 0.2;
      const diffY = (e.clientY - centerY) * 0.2;
      magneticTarget.style.transform = `translate(${diffX}px, ${diffY}px)`;
      mx = centerX + diffX;
      my = centerY + diffY;
    }

    dot.style.left  = (isMagnetic ? e.clientX : mx) + 'px';
    dot.style.top   = (isMagnetic ? e.clientY : my) + 'px';
  });

  function animateRing() {
    rx += (mx - rx) * 0.12;
    ry += (my - ry) * 0.12;
    ring.style.left = rx + 'px';
    ring.style.top  = ry + 'px';
    ringRafId = requestAnimationFrame(animateRing);
  }

  // Start the loop
  animateRing();

  // Cancel RAF when the tab is hidden, resume when visible — avoids wasted GPU cycles
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      if (ringRafId) {
        cancelAnimationFrame(ringRafId);
        ringRafId = null;
      }
    } else {
      if (!ringRafId) animateRing();
    }
  });

  // Hover state and magnetic effect
  document.querySelectorAll('nav a, .cta-link, .donut-segment, .magnetic').forEach(el => {
    el.addEventListener('mouseenter', () => {
      document.body.classList.add('cursor-hover');
      isMagnetic = true;
      magneticTarget = el;
      el.style.transition = 'transform 0.1s linear';
    });
    el.addEventListener('mouseleave', () => {
      document.body.classList.remove('cursor-hover');
      isMagnetic = false;
      if (magneticTarget) {
        magneticTarget.style.transform = '';
        magneticTarget.style.transition = 'all 0.3s ease';
        magneticTarget = null;
      }
    });
  });

  document.querySelectorAll('.film-item, .offer-row, .session-card, .timeline-row, button').forEach(el => {
    el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
    el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
  });
}

/* ---- Portfolio Donut Idle Rotation & Center Text ---- */
const donutContainer = document.querySelector('.portfolio-circle-container');
const donutSvg = document.querySelector('.portfolio-donut');
if (donutSvg && donutContainer) {
  const centerText = document.createElement('div');
  centerText.className = 'donut-center-text';
  centerText.style.cssText = `
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: var(--paper);
    opacity: 1;
    transition: opacity 0.3s ease;
    pointer-events: none;
    z-index: 5;
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 1.4rem;
    letter-spacing: 0.05em;
    line-height: 1.3;
    max-width: 220px;
  `;
  centerText.innerHTML = 'Hover to<br>Explore Portfolios';
  donutContainer.appendChild(centerText);

  const segmentDescriptions = {
    0: 'Communication<br><span style="font-size:0.8rem;opacity:0.7">Voice & Influence</span>',
    1: 'Leadership<br><span style="font-size:0.8rem;opacity:0.7">AIESEC & Beyond</span>',
    2: 'Creative<br><span style="font-size:0.8rem;opacity:0.7">Creative Designing</span>',
    3: 'HR Practices<br><span style="font-size:0.8rem;opacity:0.7">People & Culture</span>',
    4: 'Business Dev<br><span style="font-size:0.8rem;opacity:0.7">Growth & Strategy</span>',
    5: 'Technology<br><span style="font-size:0.8rem;opacity:0.7">Engineering & Architecture</span>'
  };

  document.querySelectorAll('.donut-segment').forEach(seg => {
    seg.addEventListener('mouseenter', () => {
      donutSvg.classList.add('paused');
      centerText.style.opacity = '0';
      setTimeout(() => {
        centerText.innerHTML = segmentDescriptions[seg.dataset.index];
        centerText.style.opacity = '1';
      }, 150);
    });
    seg.addEventListener('mouseleave', () => {
      donutSvg.classList.remove('paused');
      centerText.style.opacity = '0';
      setTimeout(() => {
        centerText.innerHTML = 'Hover to<br>Explore Portfolios';
        centerText.style.opacity = '1';
      }, 150);
    });
  });
}

/* ---- Hero waveform generation ---- */
const wf = document.getElementById('heroWaveform');
if (wf) {
  const heights = [10,28,16,38,22,40,18,34,26,40,14,30,20,38,24,40,16,32,28,38,18,34];
  heights.forEach((h, i) => {
    const bar = document.createElement('div');
    bar.className = 'bar';
    bar.style.height = h + 'px';
    bar.style.animationDelay = (i * 0.07) + 's';
    wf.appendChild(bar);
  });
}

/* ---- Scroll reveal with fade-out ---- */
const revealEls = document.querySelectorAll('.reveal, .reveal-zoom');
const revealIO = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in');
      entry.target.classList.remove('out');
    } else {
      if (entry.target.classList.contains('in')) {
        entry.target.classList.add('out');
      }
    }
  });
}, { threshold: 0.08, rootMargin: '0px 0px -60px 0px' });
revealEls.forEach(el => revealIO.observe(el));

/* ---- Journey nodes animate in ---- */
const journeyNodes = document.querySelectorAll('.journey-node');
const journeyIO = new IntersectionObserver((entries) => {
  if (entries[0].isIntersecting) {
    journeyNodes.forEach((node) => {
      const delay = parseInt(node.dataset.delay || 0);
      setTimeout(() => {
        node.classList.add('visible');
        if (!node.classList.contains('today')) node.classList.add('lit');
      }, delay);
    });
    journeyIO.disconnect();
  }
}, { threshold: 0.2 });
const journeyGraphic = document.getElementById('journeyGraphic');
if (journeyGraphic) journeyIO.observe(journeyGraphic);

/* ---- Dynamic timeline scroll highlight + fill bar ---- */
// Cache the bounding rects once on mount; update only when window resizes
// This eliminates per-scroll getBoundingClientRect reflows
const timelineRows = document.querySelectorAll('.timeline-row');
const timelineEl   = document.querySelector('.timeline');
const timelineFill = document.querySelector('.timeline-fill');
let timelineRowRects = [];

function cacheTimelineRects() {
  timelineRowRects = Array.from(timelineRows).map(row => ({
    el: row,
    // We store the offsetTop from documentElement so we don't need getBCR on scroll
    top: row.getBoundingClientRect().top + window.scrollY,
    height: row.offsetHeight,
  }));
}

function updateTimeline() {
  if (!timelineRows.length) return;
  const viewMid = window.scrollY + window.innerHeight * 0.45;
  let closestDist = Infinity;
  let closestIdx = 0;

  timelineRowRects.forEach((rect, i) => {
    const rowMid = rect.top + rect.height / 2;
    const dist = Math.abs(rowMid - viewMid);
    if (dist < closestDist) { closestDist = dist; closestIdx = i; }
  });

  timelineRows.forEach((row, i) => {
    row.classList.remove('tl-active', 'tl-dim', 'is-current');
    if (i === closestIdx) row.classList.add('tl-active');
    else row.classList.add('tl-dim');
  });

  // Scroll-driven fill bar
  if (timelineEl && timelineFill) {
    const tlRect    = timelineEl.getBoundingClientRect();
    const tlTop     = tlRect.top;
    const tlHeight  = tlRect.height;
    const progress  = Math.min(1, Math.max(0, (window.innerHeight * 0.55 - tlTop) / tlHeight));
    timelineFill.style.height = (progress * 100) + '%';
  }
}

if (timelineRows.length) {
  cacheTimelineRects();
  window.addEventListener('resize', cacheTimelineRects, { passive: true });
}

/* ---- Consolidated Scroll Handler (RAF-based) ---- */
const scrollBar = document.getElementById('scrollBar');
const mainNav = document.querySelector('nav');
const heroSection = document.querySelector('.hero');
let scrollTicking = false;

function onScrollFrame() {
  const scrollY = window.scrollY;

  // Hero zoom effect
  if (scrollY < 1500) {
    const zoom = 1 + (scrollY * 0.0004);
    document.documentElement.style.setProperty('--scroll-zoom', zoom);
  }

  // Timeline (only if timeline exists on this page)
  if (timelineRows.length) updateTimeline();

  // Progress bar
  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  const pct = docHeight > 0 ? (scrollY / docHeight) * 100 : 0;
  if (scrollBar) scrollBar.style.width = pct + '%';

  // Sticky nav
  if (mainNav) {
    const heroBottom = heroSection ? heroSection.offsetHeight : 300;
    if (scrollY > heroBottom - 80) {
      mainNav.classList.add('sticky');
    } else {
      mainNav.classList.remove('sticky');
    }
  }

  scrollTicking = false;
}

window.addEventListener('scroll', () => {
  if (!scrollTicking) {
    requestAnimationFrame(onScrollFrame);
    scrollTicking = true;
  }
}, { passive: true });
onScrollFrame();

/* ---- Number Counter Animation ---- */
const counterSpeed = 40;

const counterIO = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const sectionCounters = entry.target.querySelectorAll('.counter');
      sectionCounters.forEach(counter => {
        const updateCount = () => {
          const target = +counter.getAttribute('data-target');
          const currentString = counter.innerText.replace(/,/g, '');
          const count = +currentString;
          const inc = target / counterSpeed;
          if (count < target) {
            counter.innerText = Math.ceil(count + inc).toLocaleString();
            setTimeout(updateCount, 30);
          } else {
            counter.innerText = target.toLocaleString();
          }
        };
        updateCount();
      });
    } else {
      const sectionCounters = entry.target.querySelectorAll('.counter');
      sectionCounters.forEach(counter => {
        counter.innerText = '0';
      });
    }
  });
}, { threshold: 0.3 });

const statsSection    = document.querySelector('.banner-stats-side');
const snapshotSection = document.querySelector('.snapshot-cards-col');
const commStatsCompact = document.querySelector('.comm-stats-compact');
if (statsSection) counterIO.observe(statsSection);
if (snapshotSection) counterIO.observe(snapshotSection);
if (commStatsCompact) counterIO.observe(commStatsCompact);

/* ---- Lightbox Logic ---- */
const lightbox      = document.getElementById('lightbox');
const lightboxImg   = document.getElementById('lightboxImg');
const lightboxClose = document.getElementById('lightboxClose');
const allImages     = document.querySelectorAll('img');

allImages.forEach(img => {
  img.addEventListener('click', () => {
    if (img.closest('.nav-links') || img.closest('header')) return;
    lightbox.classList.add('show');
    lightboxImg.src = img.src;
    document.body.style.overflow = 'hidden';
  });
});

const closeLightbox = () => {
  lightbox.classList.remove('show');
  setTimeout(() => {
    lightboxImg.src = '';
    document.body.style.overflow = '';
  }, 300);
};

if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
if (lightbox) {
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });
}
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && lightbox && lightbox.classList.contains('show')) {
    closeLightbox();
  }
});

/* ---- Side Navigation Active State ---- */
const sideNavDots = document.querySelectorAll('.side-nav-dot');
if (sideNavDots.length > 0) {
  const sections = document.querySelectorAll('header.hero, section, .banner-split');
  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const currentId = entry.target.getAttribute('id');
        sideNavDots.forEach(dot => {
          dot.classList.remove('active');
          if (dot.getAttribute('data-section') === currentId) {
            dot.classList.add('active');
          }
        });
      }
    });
  }, { threshold: 0.3 });

  sections.forEach(sec => sectionObserver.observe(sec));
}

/* ---- 3D Tilt Card Effect ---- */
const tiltCards = document.querySelectorAll('.tilt-card');
tiltCards.forEach(card => {
  card.addEventListener('mousemove', e => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    const rotateX = ((y - centerY) / centerY) * -10;
    const rotateY = ((x - centerX) / centerX) * 10;
    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
    card.style.transition = 'none';
  });

  card.addEventListener('mouseleave', () => {
    card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
    card.style.transition = 'transform 0.5s ease';
  });
});

/* ---- Creative Section Slide-In ---- */
const creativeTeaser = document.getElementById('creative-teaser');
if (creativeTeaser) {
  const creativeIO = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
      } else {
        entry.target.classList.remove('in-view');
      }
    });
  }, { threshold: 0.2 });
  creativeIO.observe(creativeTeaser);
}

/* ---- Highlight Reel Carousel (RAF-based, replaces setInterval) ---- */
const highlightReel = document.getElementById('highlight-reel');
if (highlightReel) {
  const reelContainer = document.getElementById('reelContainer');
  const slides        = document.querySelectorAll('.reel-slide');
  const prevBtn       = document.getElementById('reelPrev');
  const nextBtn       = document.getElementById('reelNext');
  const indicator     = document.getElementById('reelIndicator');
  const progressFill  = document.getElementById('reelProgress');

  let currentSlide  = 0;
  const totalSlides = slides.length;
  const slideDuration = 5000; // ms per slide
  let progressPct   = 0;
  let lastTimestamp  = null;
  let isPaused      = false;
  let carouselRafId = null;

  function updateSlide(index) {
    currentSlide = ((index % totalSlides) + totalSlides) % totalSlides;

    reelContainer.style.transform = `translateX(-${currentSlide * (100 / totalSlides)}%)`;

    slides.forEach((s, i) => {
      if (i === currentSlide) s.classList.add('active');
      else s.classList.remove('active');
    });

    if (indicator) indicator.textContent = `0${currentSlide + 1} / 0${totalSlides}`;
    progressPct   = 0;
    lastTimestamp = null; // reset timer on manual advance
    if (progressFill) progressFill.style.width = '0%';
  }

  function carouselTick(timestamp) {
    if (!isPaused) {
      if (lastTimestamp === null) lastTimestamp = timestamp;
      const delta = timestamp - lastTimestamp;
      lastTimestamp = timestamp;

      progressPct += (delta / slideDuration) * 100;
      if (progressPct >= 100) {
        progressPct = 0;
        updateSlide(currentSlide + 1);
      }
      if (progressFill) progressFill.style.width = `${Math.min(progressPct, 100)}%`;
    } else {
      lastTimestamp = null; // reset so no big jump when resuming
    }
    carouselRafId = requestAnimationFrame(carouselTick);
  }

  // Start RAF loop
  carouselRafId = requestAnimationFrame(carouselTick);

  if (prevBtn) prevBtn.addEventListener('click', () => updateSlide(currentSlide - 1));
  if (nextBtn) nextBtn.addEventListener('click', () => updateSlide(currentSlide + 1));

  // Pause on hover — just flip the flag, RAF loop keeps running so no jank on resume
  highlightReel.addEventListener('mouseenter', () => { isPaused = true; });
  highlightReel.addEventListener('mouseleave', () => { isPaused = false; });

  // Also cancel RAF when tab is hidden (carousel is below the fold anyway)
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      cancelAnimationFrame(carouselRafId);
      carouselRafId = null;
      lastTimestamp = null;
    } else {
      if (!carouselRafId) carouselRafId = requestAnimationFrame(carouselTick);
    }
  });
}

/* ---- Testimonials Marquee: Pause when off-screen ---- */
// Uses CSS animation-play-state to pause the GPU-animated track
// when the section is not in view — frees up compositor thread
const testiTrack = document.getElementById('testiTrack1');
if (testiTrack) {
  const marqueeObserver = new IntersectionObserver(([entry]) => {
    testiTrack.style.animationPlayState = entry.isIntersecting ? 'running' : 'paused';
  }, { rootMargin: '100px' }); // start slightly before to avoid pop-in
  marqueeObserver.observe(testiTrack);
}

/* ---- Partners Marquee: Same treatment ---- */
const partnersTrack = document.querySelector('.partners-track');
if (partnersTrack) {
  const partnersMarqueeObserver = new IntersectionObserver(([entry]) => {
    partnersTrack.style.animationPlayState = entry.isIntersecting ? 'running' : 'paused';
  }, { rootMargin: '100px' });
  partnersMarqueeObserver.observe(partnersTrack);
}

/* ---- 3D Disciplines iframe: Deferred load ---- */
// The Three.js scene is heavy. We load it only when the user is 300px
// away from scrolling to the portfolio section — keeps initial load fast.
const disciplinesIframe = document.getElementById('disciplinesIframe');
if (disciplinesIframe) {
  const iframeObserver = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      disciplinesIframe.src = disciplinesIframe.dataset.src;
      iframeObserver.disconnect();
    }
  }, { rootMargin: '300px' }); // preload 300px before viewport
  iframeObserver.observe(disciplinesIframe);
}

/* ---- 3D Disciplines Mobile Nav Button ---- */
const disciplinesNavBtn = document.getElementById('disciplinesNavBtn');
if (disciplinesNavBtn && disciplinesIframe) {
  disciplinesNavBtn.addEventListener('click', (e) => {
    e.preventDefault();
    try {
      const iframeWindow = disciplinesIframe.contentWindow;
      if (iframeWindow) {
        iframeWindow.scrollBy({ top: iframeWindow.innerHeight * 0.8, behavior: 'smooth' });
        iframeWindow.dispatchEvent(new WheelEvent('wheel', {
          deltaY: iframeWindow.innerHeight * 0.8,
          bubbles: true
        }));
      }
    } catch (err) {
      console.warn('Could not scroll iframe programmatically.', err);
    }
  });
}