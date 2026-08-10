import os

js_file = "3d-it-portfolio/assets/index-DDITMpZT.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

# Original string for positioning
old_pos = "i=Ar?0:t%2===0?2:-2,s=Ar?1.2:t%2===0?.5:-.5"
# New positioning: 
# Desktop (not Ar): x = 2.5 (right side), y = 0 (centered)
# Mobile (Ar): x = 0 (centered), y = 1.6 (moved up to avoid bottom text)
new_pos = "i=Ar?0:2.5,s=Ar?1.6:0"

if old_pos in content:
    content = content.replace(old_pos, new_pos)
    print("JS alignment updated successfully.")
else:
    print("Warning: old_pos string not found in JS.")

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)

# Also let's fix CSS so text doesn't span full width on desktop
css_file = "3d-it-portfolio/assets/index-C22DXFAK.css"
with open(css_file, "r", encoding="utf-8") as f:
    css_content = f.read()

# The css is minified. We can just append a rule to the end to override:
css_override = """
@media (min-width: 769px) {
  .section {
    width: 50vw;
  }
}
@media (max-width: 768px) {
  .section {
    padding-bottom: 20vh; /* more space for mobile controls */
  }
}
"""

with open(css_file, "a", encoding="utf-8") as f:
    f.write(css_override)
print("CSS updated successfully.")
