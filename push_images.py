import subprocess

subprocess.run(["git", "add", "images/ics-training-1.JPG", "images/ics-training-2.jpeg", "images/ics-training-3.jpg", "images/ics-training-4.jpg", "experience.html"], check=True)
subprocess.run(["git", "commit", "-m", "Fix image extensions for ICS session and add images"], check=True)
subprocess.run(["git", "push", "origin", "main"], check=True)
print("Git push complete.")
