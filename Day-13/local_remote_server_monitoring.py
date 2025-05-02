import paramiko
import psutil
import time

# ===========================
# 1. Local System Monitoring
# ===========================
def check_local_usage():
    print("🖥️ Local System:")
    
    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage over 1 second
    print(f"  🔧 CPU Usage: {cpu_usage:.2f}%")
    
    # Disk usage
    disk = psutil.disk_usage('/')
    print(f"  💽 Disk Usage: {disk.percent:.2f}% of {disk.total // (1024**3)} GB")
    
    # Memory usage
    memory = psutil.virtual_memory()
    print(f"  💾 Memory Usage: {memory.percent:.2f}% of {memory.total // (1024**3)} GB\n")


# ==============================
# 2. Remote Server Monitoring
# ==============================
def check_remote_usage(host, user, key_path):
    print(f"🔗 Connecting to {host}...")
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=host, username=user, key_filename=key_path)

        # CPU Usage (using 'top' command)
        stdin, stdout, _ = ssh.exec_command("top -bn2 | grep 'Cpu(s)' | tail -n1")
        cpu_line = stdout.read().decode()
        cpu_idle = float(cpu_line.split(',')[3].split()[0])
        cpu_usage = 100 - cpu_idle

        # Disk Usage (using 'df' command)
        stdin, stdout, _ = ssh.exec_command("df -h / | tail -1")
        disk_line = stdout.read().decode().split()
        disk_usage = disk_line[4]  # like '37%'

        # Memory Usage (using 'free' command)
        stdin, stdout, _ = ssh.exec_command("free -h | grep Mem | awk '{print $3}'")
        memory_usage = stdout.read().decode().strip()
        
        print(f"  🔧 CPU Usage: {cpu_usage:.2f}%")
        print(f"  💽 Disk Usage: {disk_usage}")
        print(f"  💾 Memory Usage: {memory_usage}\n")

        ssh.close()
    except Exception as e:
        print(f"  ❌ Error connecting to {host}: {e}\n")


# ===========================
# Server Configuration
# ===========================
remote_servers = [
    {
        'host': 'ec2-3-111-187-94.ap-south-1.compute.amazonaws.com',
        'user': 'ubuntu',
        'key': '/path/to/your/Pythonkey.pem'
    },
    {
        'host': 'ec2-13-232-100-23.ap-south-1.compute.amazonaws.com',
        'user': 'ubuntu',
        'key': '/path/to/your/Pythonkey.pem'
    }
    # Add more servers here if needed
]

# ===========================
# Run the Monitoring Script
# ===========================
if __name__ == "__main__":
    check_local_usage()  # Check local system usage
    
    # Check remote servers
    for server in remote_servers:
        check_remote_usage(server['host'], server['user'], server['key'])
