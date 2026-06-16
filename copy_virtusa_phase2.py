import os

base_dir = r"C:\Users\USER\.gemini\antigravity\brain\4dac71d6-7bdc-441e-9e9d-8cb137452352"
dest_dir = r"c:\Users\USER\Downloads\portfolio3\portfolio\images"

src = os.path.join(base_dir, "media__1781475784396.jpg")
dst = os.path.join(dest_dir, "virtusa-training-phase2.jpg")
with open(src, "rb") as f1, open(dst, "wb") as f2:
    f2.write(f1.read())
