import subprocess

subprocess.run(["git", "add", "images/virtusa-training-1.jpg", "images/virtusa-training-2.jpg", "images/virtusa-training-3.jpg", "images/virtusa-training-4.jpg", "images/virtusa-training-5.jpg", "experience.html"], check=True)
subprocess.run(["git", "commit", "-m", "Add Speak to Impact - Virtusa Training session"], check=True)
subprocess.run(["git", "push", "origin", "main"], check=True)
print("Git push complete.")
