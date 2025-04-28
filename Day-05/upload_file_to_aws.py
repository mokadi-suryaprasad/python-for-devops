import os
import sys

# Set credentials (assume already exported in environment variables)
aws_access = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret = os.getenv("AWS_SECRET_ACCESS_KEY")

if not aws_access or not aws_secret:
    print("AWS credentials not found!", file=sys.stderr)
    sys.exit(1)

# Get bucket name from script argument
if len(sys.argv) < 2:
    print("Usage: python upload.py <bucket-name>", file=sys.stderr)
    sys.exit(1)

bucket_name = sys.argv[1]

# Write a temp file
file_path = "/tmp/upload.txt"
with open(file_path, "w") as f:
    f.write("Hello AWS or GCP!")

# Upload using AWS CLI (example)
os.system(f"aws s3 cp {file_path} s3://{bucket_name}/upload.txt")

print(f"File uploaded to {bucket_name} successfully!")
