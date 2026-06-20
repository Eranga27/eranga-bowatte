import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Swap order
css = css.replace('.creative-text-col {\n    flex: 1;\n    z-index: 2;\n  }', '.creative-text-col {\n    flex: 1;\n    z-index: 2;\n    order: 2;\n  }')
css = css.replace('.creative-images-col {\n    flex: 1.2;\n    position: relative;\n    height: 500px;\n  }', '.creative-images-col {\n    flex: 1.2;\n    position: relative;\n    height: 500px;\n    order: 1;\n  }')

# Add colorful blurred background to creative-images-col
if ".creative-images-col::before" not in css:
    css = css.replace('.creative-images-col {', '.creative-images-col::before {\n    content: "";\n    position: absolute;\n    top: 10%; left: 10%; right: 10%; bottom: 10%;\n    background: linear-gradient(60deg, #FF6A1A, #b732c2, #1f6ce8);\n    filter: blur(70px);\n    opacity: 0.45;\n    z-index: 1;\n    transform: rotate(-15deg);\n  }\n  .creative-images-col {')

# 2. Add the artistic mask to creative-img-wrapper and change clip-path
mask_css = """  .creative-img-wrapper {
    position: absolute;
    background-size: cover;
    background-position: center;
    box-shadow: 0 20px 40px rgba(0,0,0,0.8);
    clip-path: polygon(15% 0%, 100% 0%, 85% 100%, 0% 100%);
    -webkit-mask-image: repeating-linear-gradient(
      55deg,
      #000 0px, #000 25px,
      transparent 25px, transparent 29px,
      #000 29px, #000 70px,
      transparent 70px, transparent 76px,
      rgba(0,0,0,0.75) 76px, rgba(0,0,0,0.75) 90px,
      transparent 90px, transparent 93px,
      #000 93px, #000 130px,
      transparent 130px, transparent 136px
    );
    mask-image: repeating-linear-gradient(
      55deg,
      #000 0px, #000 25px,
      transparent 25px, transparent 29px,
      #000 29px, #000 70px,
      transparent 70px, transparent 76px,
      rgba(0,0,0,0.75) 76px, rgba(0,0,0,0.75) 90px,
      transparent 90px, transparent 93px,
      #000 93px, #000 130px,
      transparent 130px, transparent 136px
    );
    transition: transform 1.2s cubic-bezier(0.16, 1, 0.3, 1), opacity 1.2s ease, filter 0.3s ease;
    overflow: hidden;
    cursor: pointer;
  }"""

css = re.sub(r'\.creative-img-wrapper\s*\{[^}]+\}', mask_css, css)

# 3. Tone down the wiggle
new_wiggle = """  @keyframes creativeWiggle {
    0% { transform: rotate(0deg) scale(1.02); }
    25% { transform: rotate(1deg) scale(1.02); }
    50% { transform: rotate(-1deg) scale(1.02); }
    75% { transform: rotate(0.5deg) scale(1.02); }
    100% { transform: rotate(0deg) scale(1.02); }
  }"""

css = re.sub(r'@keyframes creativeWiggle\s*\{[^}]+\}', new_wiggle, css)

# Also fix media query order for mobile
css = css.replace('.creative-images-col { height: 400px; width: 100%; margin-top: 40px; }', '.creative-images-col { height: 400px; width: 100%; margin-top: 40px; order: 2; }\n    .creative-text-col { order: 1; }')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Styles updated successfully.")
