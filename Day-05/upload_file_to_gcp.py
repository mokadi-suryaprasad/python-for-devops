import os
import sys

# Set credentials (assume already exported in environment variables)
gcp_project = os.getenv("GCP_PROJECT_ID")
gcp_credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

if not gcp_project or not gcp_credentials:
    print("GCP credentials or project ID not found!", file=sys.stderr)
    sys.exit(1)

# Get bucket name from script argument
if len(sys.argv) < 2:
    print("Usage: python upload_gcp.py <bucket-name>", file=sys.stderr)
    sys.exit(1)

bucket_name = sys.argv[1]

# Write a temp file
file_path = "/tmp/upload.txt"
with open(file_path, "w") as f:
    f.write("Hello AWS or GCP!")

# Upload using gcloud CLI (example)
os.system(f"gcloud storage cp {file_path} gs://{bucket_name}/upload.txt")

print(f"File uploaded to {bucket_name} successfully!")
