js_file = "3d-it-portfolio/assets/index-DDITMpZT.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

fixes = [
    ("ia.push(new D(0,0,n+8))", "ia.push(new D(0,0,n+3))"),
    ("./images/mic4.jpg",        "./images/Sentinalpreview.png"),
    ("./images/creative-art.png","./images/Kamilaportfoliopreview.png"),
]

for old, new in fixes:
    if old in content:
        content = content.replace(old, new)
        print("OK: " + old[:50])
    else:
        print("NOT FOUND: " + old[:50])

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
