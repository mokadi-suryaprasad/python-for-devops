import os
import sys

def upload_file_to_s3(bucket, source_file, destination_file, region, aws_access_key, aws_secret_key):
    os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key
    os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_key
    os.environ['AWS_DEFAULT_REGION'] = region

    cmd = f"aws s3 cp {source_file} s3://{bucket}/{destination_file} --region {region}"
    print(f"Running command: {cmd}")

    if os.system(cmd) != 0:
        print("AWS S3 upload failed!", file=sys.stderr)
        sys.exit(1)
    print(f"File uploaded successfully to s3://{bucket}/{destination_file}")
