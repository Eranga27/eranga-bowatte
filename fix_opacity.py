js_file = "3d-it-portfolio/assets/index-DDITMpZT.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

fixes = [
    # Remove the sRGB hack that's causing additional brightening
    ('sx.load(r.image,a=>{a.colorSpace="srgb";a.encoding=3001;const o=', "sx.load(r.image,a=>{const o="),
    # Dial opacity down to 0.65 — visible but not blown out
    ("opacity:1", "opacity:.65"),
]

for old, new in fixes:
    if old in content:
        content = content.replace(old, new)
        print("Patched: " + old[:50])
    else:
        print("NOT FOUND: " + old[:50])

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)
