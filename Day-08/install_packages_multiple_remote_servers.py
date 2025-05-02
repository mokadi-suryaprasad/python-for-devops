import paramiko

# List of packages to check and install if missing
packages = ['nginx', 'docker.io', 'git']

# List of servers to connect to
servers = [
    {
        'host': 'ec2-3-111-187-94.ap-south-1.compute.amazonaws.com',
        'user': 'ubuntu',
        'key': '/root/Pythonkey.pem'
    },
    {
        'host': 'ec2-13-232-100-23.ap-south-1.compute.amazonaws.com',
        'user': 'ubuntu',
        'key': '/root/Pythonkey.pem'
    },
    # Add more servers here as needed
]

# Function to check if a package is installed
def is_installed(ssh_client, package):
    command = f"dpkg-query -W {package} >/dev/null 2>&1; echo $?"
    stdin, stdout, stderr = ssh_client.exec_command(command)
    return stdout.read().decode().strip() == '0'

# Function to install a package
def install_package(ssh_client, package):
    print(f"Installing {package}...")
    command = f"sudo DEBIAN_FRONTEND=noninteractive apt-get update && sudo apt-get install -y {package}"
    stdin, stdout, stderr = ssh_client.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    if exit_status == 0:
        print(f"✅ {package} installed successfully.")
    else:
        print(f"❌ Failed to install {package}. Error: {stderr.read().decode()}")

# Loop through each server
for server in servers:
    print(f"\n🔗 Connecting to {server['host']} ...")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(
            hostname=server['host'],
            username=server['user'],
            key_filename=server['key']
        )
        print("✅ Connected successfully.")

        for package in packages:
            if is_installed(ssh_client, package):
                print(f"✅ {package} is already installed.")
            else:
                install_package(ssh_client, package)

    except paramiko.AuthenticationException:
        print(f"❌ Authentication failed for {server['host']}. Check credentials.")
    except Exception as e:
        print(f"❌ Connection error for {server['host']}: {str(e)}")
    finally:
        ssh_client.close()
        