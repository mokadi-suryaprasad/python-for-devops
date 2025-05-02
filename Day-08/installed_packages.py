import subprocess  # ✅ Imports the 'subprocess' module which lets Python run external system commands (like 'ls', 'which', 'apt-get', etc.)
import os

# List of packages to check and install if missing
packages = ['nginx', 'docker.io', 'git']

# Function to check if a command is available (installed)
def is_installed(command):
    # 'which' returns 0 if the command is found, 1 if not
    return subprocess.call(['which', command], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

# Loop through each package
for package in packages:
    # Use the command name for checking (strip ".io" etc if needed)
    command_name = package.split('.')[0]
    
    if is_installed(command_name):
        print(f"✅ {package} is already installed.")
    else:
        print(f"⚠️ {package} is not installed. Installing...")
        os.system(f"sudo apt update && sudo apt install -y {package}")
