js_file = "3d-it-portfolio/assets/index-DDITMpZT.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("image:\"./images/")
if idx != -1:
    print(content[max(0, idx-100) : min(len(content), idx+1000)])
