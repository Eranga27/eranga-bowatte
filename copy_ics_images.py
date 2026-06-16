import os
import glob
import shutil

base_dir = r"C:\Users\USER\.gemini\antigravity\brain\4dac71d6-7bdc-441e-9e9d-8cb137452352"
dest_dir = r"c:\Users\USER\Downloads\portfolio3\portfolio\images"

files = glob.glob(os.path.join(base_dir, "media__*.jpg")) + glob.glob(os.path.join(base_dir, "media__*.png"))
files.sort(key=os.path.getmtime, reverse=True)

# The user uploaded 4 new images. They should be the 4 newest ones.
newest_4 = files[:4]

for i, f in enumerate(newest_4):
    dst = os.path.join(dest_dir, f"ics-training-{i+1}.jpg")
    with open(f, "rb") as f1, open(dst, "wb") as f2:
        f2.write(f1.read())
    print(f"Copied {os.path.basename(f)} to ics-training-{i+1}.jpg")
