import os
import sys

def get_cloud_provider():
    """
    Determine the cloud provider to use.
    Priority:
    1. Command-line argument (sys.argv[1])
    2. Environment variable (CLOUD_PROVIDER)
    3. Default to 'aws'
    """
    # Priority 1: Check command-line argument
    if len(sys.argv) > 1 and sys.argv[1]:
        cloud_provider = sys.argv[1].lower()
        if cloud_provider in ['aws', 'gcp']:
            return cloud_provider
        else:
            print(f"Invalid cloud provider '{cloud_provider}'. Please choose 'aws' or 'gcp'.", file=sys.stderr)
            sys.exit(1)

    # Priority 2: Check environment variable
    cloud_provider = os.getenv('CLOUD_PROVIDER')
    if cloud_provider and cloud_provider.lower() in ['aws', 'gcp']:
        return cloud_provider.lower()

    # Priority 3: Default to AWS
    return 'aws'
