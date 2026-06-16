import subprocess

subprocess.run(["git", "commit", "-m", "Add ICS session to Communication Trainings"], check=True)
subprocess.run(["git", "push", "origin", "main"], check=True)
print("Git push complete.")
