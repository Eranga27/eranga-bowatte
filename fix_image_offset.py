js_file = "3d-it-portfolio/assets/index-DDITMpZT.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

# The camera waypoints are at n+3 from each section's 3D object.
# Current: ia.push(new D(Ar?0:-i*1.2,Ar?0:-s*1.2,n+3))
# We need the camera to be at exactly n when the section text is visible.
# Changing the waypoint offset from n+3 to n+8 brings the camera closer to 
# the section before the text triggers, so text and image appear simultaneously.

old_waypoint = "ia.push(new D(Ar?0:-i*1.2,Ar?0:-s*1.2,n+3))"
new_waypoint = "ia.push(new D(0,0,n+8))"

if old_waypoint in content:
    content = content.replace(old_waypoint, new_waypoint)
    print("Waypoint updated.")
else:
    print("Waypoint string not found. Searching...")
    idx = content.find("ia.push")
    while idx != -1:
        print(f"  [{idx}]: {content[idx:idx+80]}")
        idx = content.find("ia.push", idx+1)

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)
print("Done.")
