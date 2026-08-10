import os

js_file = "3d-it-portfolio/assets/index-DDITMpZT.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

fixes = [
    # Restore i and s calculation
    ("i=Ar?0:2.5,s=Ar?1.6:0", "i=Ar?0:t%2===0?2:-2,s=Ar?1.2:t%2===0?.5:-.5"),
    # Restore h.position.set (the image plane)
    ("h.position.set(Ar?0:i*.5,s,n),h.lookAt(0,0,n)", "h.position.set(Ar?0:i*.5,s,n-3),h.lookAt(0,0,n)"),
    # Restore camera waypoint
    ("ia.push(new D(0,0,n+3))", "ia.push(new D(Ar?0:-i*1.2,Ar?0:-s*1.2,n+3))")
]

for old, new in fixes:
    if old in content:
        content = content.replace(old, new)
        print("Restored: " + old[:50])
    else:
        print("NOT FOUND: " + old[:50])

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)
