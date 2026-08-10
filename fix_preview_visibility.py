js_file = "3d-it-portfolio/assets/index-DDITMpZT.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

fixes = [
    # 1. Scale down on mobile (Ar is true)
    ("l=new Zs(3*o,3)", "l=new Zs(Ar?1.5*o:3*o,Ar?1.5:3)"),
    # 2. Increase opacity from .25 to .8
    ("opacity:.25", "opacity:.8"),
    # 3. Remove inward angling (h.lookAt(0,0,n)) so the image is flat and readable
    ("h.position.set(Ar?0:i*.5,s,n-3),h.lookAt(0,0,n)", "h.position.set(Ar?0:i*.5,s,n-3)")
]

for old, new in fixes:
    if old in content:
        content = content.replace(old, new)
        print("Patched: " + old[:30])
    else:
        print("NOT FOUND: " + old[:30])

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)
