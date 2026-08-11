js_file = "3d-it-portfolio/assets/index-DDITMpZT.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

fixes = [
    # 1. Re-add lookAt so the image plane always faces the camera (fixes invisible Lyricist Journey)
    (
        "h.position.set(Ar?0:i*.5,s,n-3),pr.add(h)",
        "h.position.set(Ar?0:i*.5,s,n-3),h.lookAt(0,0,n),pr.add(h)"
    ),
    # 2. Use a neutral grey color tint to naturally darken bright/white images without affecting dark ones
    # Switch from plain opacity to opacity + a grey multiplier color
    (
        "new js({map:a,transparent:!0,opacity:.65,depthWrite:!1})",
        "new js({map:a,transparent:!0,opacity:.9,color:0x999999,depthWrite:!1})"
    ),
]

for old, new in fixes:
    if old in content:
        content = content.replace(old, new)
        print("Patched: " + old[:60])
    else:
        print("NOT FOUND: " + old[:60])

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)
