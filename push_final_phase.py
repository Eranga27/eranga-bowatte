import subprocess

subprocess.run(["git", "add", "images/virtusa-training-final-phase.jpg", "experience.html"], check=True)
subprocess.run(["git", "commit", "-m", "Add Speak to Impact Final Phase session"], check=True)
subprocess.run(["git", "push", "origin", "main"], check=True)
print("Git push complete.")
