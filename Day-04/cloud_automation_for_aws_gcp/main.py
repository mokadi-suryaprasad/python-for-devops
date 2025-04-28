import sys
import os
from config import get_cloud_provider
from upload_file_to_s3 import upload_file_to_s3
from upload_file_to_gcs import upload_file_to_gcs

def main():
    cloud_provider = get_cloud_provider()
    print(f"Selected Cloud Provider: {cloud_provider.upper()}")

    if cloud_provider == 'aws':
        if len(sys.argv) < 5:
            print("Usage: python main.py aws <bucket-name> <source-file> <destination-file> [<AWS_REGION> <AWS_ACCESS_KEY> <AWS_SECRET_KEY>]")
            sys.exit(1)

        _, _, bucket, source_file, destination_file = sys.argv[:5]

        # Load credentials from environment variables if available
        aws_region = os.getenv('AWS_DEFAULT_REGION')
        aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
        aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

        # If not available in environment, take from command-line arguments
        if not (aws_region and aws_access_key and aws_secret_key):
            if len(sys.argv) < 8:
                print("Error: Missing AWS credentials.")
                print("Usage: python main.py aws <bucket-name> <source-file> <destination-file> <AWS_REGION> <AWS_ACCESS_KEY> <AWS_SECRET_KEY>")
                sys.exit(1)
            aws_region, aws_access_key, aws_secret_key = sys.argv[5:8]

        upload_file_to_s3(bucket, source_file, destination_file, aws_region, aws_access_key, aws_secret_key)

    elif cloud_provider == 'gcp':
        if len(sys.argv) < 5:
            print("Usage: python main.py gcp <bucket-name> <source-file> <destination-file> [<GCP_REGION> <GCP_PROJECT_ID> <GCP_CREDENTIALS_PATH>]")
            sys.exit(1)

        _, _, bucket, source_file, destination_file = sys.argv[:5]

        # Load credentials from environment variables if available
        gcp_region = os.getenv('GCP_DEFAULT_REGION')
        gcp_project_id = os.getenv('GCP_PROJECT_ID')
        gcp_credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

        # If not available in environment, take from command-line arguments
        if not (gcp_region and gcp_project_id and gcp_credentials_path):
            if len(sys.argv) < 8:
                print("Error: Missing GCP credentials.")
                print("Usage: python main.py gcp <bucket-name> <source-file> <destination-file> <GCP_REGION> <GCP_PROJECT_ID> <GCP_CREDENTIALS_PATH>")
                sys.exit(1)
            gcp_region, gcp_project_id, gcp_credentials_path = sys.argv[5:8]

        upload_file_to_gcs(bucket, source_file, destination_file, gcp_region, gcp_project_id, gcp_credentials_path)

    else:
        print("Unsupported cloud provider! Choose 'aws' or 'gcp'.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
