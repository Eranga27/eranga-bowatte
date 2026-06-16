import re

with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_logic = """    // CSS animation handles the rotation now to avoid lag
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
      0: 'Communication<br><span style="font-size:0.8rem;opacity:0.7">Public Speaking & Confidence</span>',
      1: 'Leadership<br><span style="font-size:0.8rem;opacity:0.7">Corporate & Team Dynamics</span>',
      2: 'HR Practices<br><span style="font-size:0.8rem;opacity:0.7">Employee Engagement</span>',
      3: 'Creative Arts<br><span style="font-size:0.8rem;opacity:0.7">Content Production</span>',
      4: 'IT Projects<br><span style="font-size:0.8rem;opacity:0.7">Technical & Software</span>'
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
  }"""

js = re.sub(r'const centerText = document\.createElement\(\'div\'\);.*?\}\);\n  \}', new_logic, js, flags=re.DOTALL)
js = re.sub(r'let rotation = 0;\s*let rotationSpeed = 0\.05;\s*let isHoveringDonut = false;\s*let animationFrameId;\s*', '', js)

with open('main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('main.js updated')
