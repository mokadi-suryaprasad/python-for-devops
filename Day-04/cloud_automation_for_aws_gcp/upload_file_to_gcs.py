import os
import sys

def upload_file_to_gcs(bucket, source_file, destination_file, region, gcp_project_id, gcp_credentials_path):
    os.environ['GCP_PROJECT_ID'] = gcp_project_id
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = gcp_credentials_path

    # For GCP CLI, region is usually set while creating buckets; not mandatory for upload.
    cmd = f"gcloud storage cp {source_file} gs://{bucket}/{destination_file}"
    print(f"Running command: {cmd}")

    if os.system(cmd) != 0:
        print("GCP Storage upload failed!", file=sys.stderr)
        sys.exit(1)
    print(f"File uploaded successfully to gs://{bucket}/{destination_file}")
