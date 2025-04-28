import os
import sys

def get_cloud_provider():
    cloud_provider = os.getenv('CLOUD_PROVIDER', None)

    if len(sys.argv) > 1:
        cloud_provider = sys.argv[1].lower()

    if not cloud_provider:
        cloud_provider = 'aws'

    return cloud_provider
