import os

js_file = "3d-it-portfolio/assets/index-DDITMpZT.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    "./images/gitcamp-2022.png": "./images/Eloquentonepreview.png",
    "./images/team.jpg": "./images/Smartagrisuitepreview.png",
    "./images/iit-business-1.jpg": "./images/Lankaclimatehubpreview.png",
    # mic4.jpg -> Sentinel Access (no image provided, skipping)
    "./images/nma-ceremony-2.jpg": "./images/Boamrealestatespreview.png"
    # creative-art.png -> Lyricist Journey (no image provided, skipping)
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Images replaced in JS file.")
