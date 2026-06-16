import os

base_dir = r"C:\Users\USER\.gemini\antigravity\brain\4dac71d6-7bdc-441e-9e9d-8cb137452352"
dest_dir = r"c:\Users\USER\Downloads\portfolio3\portfolio\images"
files = [
    "1781470048120",
    "1781470048252",
    "1781470048311",
    "1781470048347",
    "1781470048590"
]

for i, f in enumerate(files):
    src = os.path.join(base_dir, f"media__{f}.jpg")
    dst = os.path.join(dest_dir, f"iit-orientation-{i+1}.jpg")
    with open(src, "rb") as f1, open(dst, "wb") as f2:
        f2.write(f1.read())
