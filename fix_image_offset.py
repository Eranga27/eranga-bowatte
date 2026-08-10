import re

js_file = "3d-it-portfolio/assets/index-DDITMpZT.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

# The image plane is positioned at n-3 (behind the 3D object).
# This causes it to appear when scrolling INTO the NEXT section, not the current one.
# Fix: move to n+10 so it's in front of the object, aligning with the current section's text.

old = "h.position.set(Ar?0:i*.5,s,n-3),h.lookAt(0,0,n)"
new = "h.position.set(Ar?0:i*.5,s,n+10),h.lookAt(0,0,n+10)"

if old in content:
    content = content.replace(old, new)
    print("Image Z-position fixed successfully.")
else:
    print("ERROR: target string not found. Searching for nearby pattern...")
    # Try to find it
    idx = content.find("h.position.set")
    while idx != -1:
        snippet = content[idx:idx+80]
        print(f"Found at {idx}: {snippet}")
        idx = content.find("h.position.set", idx+1)

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)
