import os

base_dir = r"C:\Users\USER\.gemini\antigravity\brain\4dac71d6-7bdc-441e-9e9d-8cb137452352"
dest_dir = r"c:\Users\USER\Downloads\portfolio3\portfolio\images"

files = [
    ("1781477812595", "nma-ceremony-1.jpg"),
    ("1781477812681", "nma-ceremony-2.jpg")
]

for f_id, dest_name in files:
    src = os.path.join(base_dir, f"media__{f_id}.jpg")
    dst = os.path.join(dest_dir, dest_name)
    with open(src, "rb") as f1, open(dst, "wb") as f2:
        f2.write(f1.read())
