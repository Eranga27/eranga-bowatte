js_file = "3d-it-portfolio/assets/index-DDITMpZT.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

# Fix texture being blown out/over-bright due to missing sRGB color space conversion
fixes = [
    ("sx.load(r.image,a=>{const o=", "sx.load(r.image,a=>{a.colorSpace=\"srgb\";a.encoding=3001;const o=")
]

for old, new in fixes:
    if old in content:
        content = content.replace(old, new)
        print("Patched: colorSpace and encoding applied to texture.")
    else:
        print("NOT FOUND: " + old[:30])

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)
