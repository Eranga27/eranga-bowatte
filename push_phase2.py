import subprocess

subprocess.run(["git", "add", "images/virtusa-training-phase2.jpg", "experience.html"], check=True)
subprocess.run(["git", "commit", "-m", "Add Speak to Impact Phase 2 session with YouTube Short"], check=True)
subprocess.run(["git", "push", "origin", "main"], check=True)
print("Git push complete.")
