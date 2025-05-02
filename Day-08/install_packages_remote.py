import paramiko

# List of packages to check and install if missing
packages = ['nginx', 'docker.io', 'git']

# Remote server SSH details
remote_user = 'ubuntu'
remote_host = 'ec2-3-111-187-94.ap-south-1.compute.amazonaws.com'  # Replace with your server's IP or hostname
ssh_key_path = '/root/Pythonkey.pem'  # Adjust this path if needed

# Function to check if a package is installed
def is_installed(ssh_client, package):
    command = f"dpkg-query -W {package} >/dev/null 2>&1; echo $?"
    stdin, stdout, stderr = ssh_client.exec_command(command)
    return stdout.read().decode().strip() == '0'

# Function to install a package
def install_package(ssh_client, package):
    print(f"Installing {package}...")
    # Prepending 'DEBIAN_FRONTEND=noninteractive' prevents some prompts
    command = f"sudo DEBIAN_FRONTEND=noninteractive apt-get update && sudo apt-get install -y {package}"
    stdin, stdout, stderr = ssh_client.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    if exit_status == 0:
        print(f"✅ {package} installed successfully.")
    else:
        print(f"❌ Failed to install {package}. Error: {stderr.read().decode()}")

# Establish SSH connection using SSH key
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh_client.connect(remote_host, username=remote_user, key_filename=ssh_key_path)
    print("✅ Connected successfully using SSH key.")
except paramiko.AuthenticationException:
    print("❌ SSH key authentication failed. Check username or key.")
    exit(1)

# Loop through each package and install if needed
for package in packages:
    if is_installed(ssh_client, package):
        print(f"✅ {package} is already installed.")
    else:
        install_package(ssh_client, package)

# Close SSH connection
ssh_client.close()
