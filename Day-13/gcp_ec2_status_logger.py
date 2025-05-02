import google.cloud.compute_v1 as compute
import json
import datetime
from google.cloud import storage
import logging

# Configuration (Update these values)
project_id = 'your-gcp-project-id'  # Your GCP Project ID
zone = 'us-central1-a'  # Zone where the instances are located
instance_ids = ['instance-id-1', 'instance-id-2']  # List of instance IDs to monitor
bucket_name = 'your-gcs-bucket-name'  # GCS bucket name where logs will be stored

# Initialize Google Cloud clients
compute_client = compute.InstancesClient()
storage_client = storage.Client()

def get_instance_status(project_id, zone, instance_ids):
    """Fetches the status of the provided instances."""
    instance_status_data = []
    
    # Get the status of each instance
    for instance_id in instance_ids:
        instance = compute_client.get(project=project_id, zone=zone, instance=instance_id)
        instance_info = {
            'instance_id': instance.id,
            'instance_name': instance.name,
            'instance_status': instance.status,
            'creation_timestamp': instance.creation_timestamp,
        }
        instance_status_data.append(instance_info)
    
    return instance_status_data

def store_log_in_gcs(log_data, bucket_name):
    """Stores the log data in Google Cloud Storage."""
    try:
        # Create a unique file name for the logs
        current_time = datetime.datetime.utcnow()
        file_name = f"instance_status_{current_time.strftime('%Y-%m-%d_%H-%M-%S')}.json"

        # Upload logs to GCS
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        blob.upload_from_string(json.dumps(log_data, indent=4), content_type='application/json')
        logging.info(f"Logs successfully stored in GCS bucket {bucket_name} as {file_name}")
    except Exception as e:
        logging.error(f"Failed to store log in GCS: {str(e)}")
        raise e

def cloud_function(request):
    """Main function for Google Cloud Function."""
    try:
        # Get Compute Engine instance status
        instance_status_data = get_instance_status(project_id, zone, instance_ids)

        # Store log data in Google Cloud Storage
        store_log_in_gcs(instance_status_data, bucket_name)

        return "Logs successfully stored in GCS!", 200

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return f"Error: {str(e)}", 500
