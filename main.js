/* ---- Preloader Logic ---- */
window.addEventListener('load', () => {
  const preloader = document.getElementById('preloader');
  if (preloader) {
    setTimeout(() => {
      preloader.classList.add('loaded');
      setTimeout(() => {
        preloader.remove();
      }, 800);
    }, 3200); // Wait 3.2s for signature animation to complete
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

  /* ---- Hero Text Scroll Zoom Effect ---- */
  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    if (scrollY < 1500) {
      // Zooms in as you scroll down
      const zoom = 1 + (scrollY * 0.0004);
      document.documentElement.style.setProperty('--scroll-zoom', zoom);
    }
  }, { passive: true });
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

  /* ---- Background Music Toggle ---- */
  const audioToggle = document.getElementById('audioToggle');
  const bgMusic = document.getElementById('bgMusic');
  
  // Set initial volume low so it's subtle
  if(bgMusic) bgMusic.volume = 0.2;

  if(audioToggle) audioToggle.addEventListener('click', () => {
    if (bgMusic.paused) {
      bgMusic.play();
      audioToggle.classList.add('playing');
    } else {
      bgMusic.pause();
      audioToggle.classList.remove('playing');
    }
  });

  /* ---- Custom cursor & Magnetic Effect ---- */
  const dot  = document.getElementById('cursorDot');
  const ring = document.getElementById('cursorRing');
  let mx = window.innerWidth / 2, my = window.innerHeight / 2;
  let rx = mx, ry = my;
  let isMagnetic = false;
  let magneticTarget = null;

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
      requestAnimationFrame(animateRing);
    }
    animateRing();

    // Hover state and magnetic effect
    document.querySelectorAll('nav a, .cta-link, .donut-segment').forEach(el => {
      el.addEventListener('mouseenter', () => {
        document.body.classList.add('cursor-hover');
        isMagnetic = true;
        magneticTarget = el;
        el.style.transition = 'transform 0.1s linear';
      });
      el.addEventListener('mouseleave', () => {
        document.body.classList.remove('cursor-hover');
        isMagnetic = false;
        if(magneticTarget) {
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
    // Create central text element
        // CSS animation handles the rotation now to avoid lag
    // Create central text element
    const centerText = document.createElement('div');
    centerText.className = 'donut-center-text';
    centerText.style.cssText = `
      position: absolute;
      top: 50%; left: 50%;
      transform: translate(-50%, -50%);
      text-align: center;
      color: var(--paper);
      opacity: 1;
      transition: opacity 0.3s ease;
      pointer-events: none;
      z-index: 5;
      font-family: 'Poppins', sans-serif;
      font-size: 1.2rem;
      max-width: 200px;
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
  if(wf) {
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
  const revealEls = document.querySelectorAll('.reveal');
  const revealIO = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        entry.target.classList.remove('out');
      } else {
        // Only fade-out elements that have already been revealed
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
      journeyNodes.forEach((node, i) => {
        const delay = parseInt(node.dataset.delay || 0);
        setTimeout(() => {
          node.classList.add('visible');
          // Light up past nodes
          if (!node.classList.contains('today')) node.classList.add('lit');
        }, delay);
      });
      journeyIO.disconnect();
    }
  }, { threshold: 0.2 });
  const journeyGraphic = document.getElementById('journeyGraphic');
  if (journeyGraphic) journeyIO.observe(journeyGraphic);

  /* ---- Dynamic timeline scroll highlight + fill bar ---- */
  const timelineRows = document.querySelectorAll('.timeline-row');
  const timelineEl   = document.querySelector('.timeline');
  const timelineFill = document.querySelector('.timeline-fill');

  function updateTimeline() {
    if (!timelineRows.length) return;
    const viewMid = window.innerHeight * 0.45;
    let closestDist = Infinity;
    let closestIdx = 0;
    timelineRows.forEach((row, i) => {
      const rect = row.getBoundingClientRect();
      const rowMid = rect.top + rect.height / 2;
      const dist = Math.abs(rowMid - viewMid);
      if (dist < closestDist) { closestDist = dist; closestIdx = i; }
    });
    timelineRows.forEach((row, i) => {
      row.classList.remove('tl-active', 'tl-dim', 'is-current');
      if (i === closestIdx) {
        row.classList.add('tl-active');
      } else {
        row.classList.add('tl-dim');
      }
    });

    // Scroll-driven fill bar
    if (timelineEl && timelineFill) {
      const tlRect    = timelineEl.getBoundingClientRect();
      const tlTop     = tlRect.top;
      const tlHeight  = tlRect.height;
      // Progress: 0 when top of timeline hits bottom of viewport, 1 when bottom of timeline hits viewport center
      const progress  = Math.min(1, Math.max(0, (window.innerHeight * 0.55 - tlTop) / tlHeight));
      timelineFill.style.height = (progress * 100) + '%';
    }
  }

  window.addEventListener('scroll', updateTimeline, { passive: true });
  updateTimeline();

  /* ---- Scroll progress bar ---- */
  const scrollBar = document.getElementById('scrollBar');
  function updateProgress() {
    const scrolled  = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docHeight > 0 ? (scrolled / docHeight) * 100 : 0;
    if(scrollBar) scrollBar.style.width = pct + '%';
  }
  window.addEventListener('scroll', updateProgress, { passive: true });
  updateProgress();

  /* ---- Number Counter Animation ---- */
  const counterSpeed = 40; // controls the medium pace

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
        // Reset to 0 when section leaves the screen to replay on return
        const sectionCounters = entry.target.querySelectorAll('.counter');
        sectionCounters.forEach(counter => {
          counter.innerText = '0';
        });
      }
    });
  }, { threshold: 0.3 });

  const statsSection = document.querySelector('.banner-stats-side');
  const snapshotSection = document.querySelector('.snapshot-cards-col');
  if (statsSection) counterIO.observe(statsSection);
  if (snapshotSection) counterIO.observe(snapshotSection);

  /* ---- Lightbox Logic ---- */
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxClose = document.getElementById('lightboxClose');
  const allImages = document.querySelectorAll('img');

  allImages.forEach(img => {
    img.addEventListener('click', (e) => {
      // Don't lightbox if it's explicitly prevented or part of a component that handles its own clicks
      if (img.closest('.nav-links') || img.closest('header')) return; 
      
      lightbox.classList.add('show');
      lightboxImg.src = img.src;
      document.body.style.overflow = 'hidden'; // Prevent scrolling
    });
  });

  const closeLightbox = () => {
    lightbox.classList.remove('show');
    setTimeout(() => {
      lightboxImg.src = '';
      document.body.style.overflow = '';
    }, 300);
  };

  if(lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if(lightbox) {
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) {
        closeLightbox();
      }
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
          let currentId = entry.target.getAttribute('id');
          
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

  /* ---- Sticky Header Logic ---- */
  const mainNav = document.querySelector('nav');
  const heroSection = document.querySelector('.hero');
  if (mainNav) {
    window.addEventListener('scroll', () => {
      const heroBottom = heroSection ? heroSection.offsetHeight : 300;
      if (window.scrollY > heroBottom - 80) { // Activate slightly before passing the hero
        mainNav.classList.add('sticky');
      } else {
        mainNav.classList.remove('sticky');
      }
    }, { passive: true });
  }