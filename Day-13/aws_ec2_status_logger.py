import boto3
import json
import datetime

# Initialize AWS clients
ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

# Configuration (Update these values)
instance_ids = ['i-xxxxxxxxxxxxxxxxx']  # EC2 instance IDs to monitor
s3_bucket_name = 'your-s3-bucket'  # S3 bucket name where logs will be stored

def lambda_handler(event, context):
    try:
        # Fetch EC2 instance status
        response = ec2.describe_instance_status(InstanceIds=instance_ids, IncludeAllInstances=True)

        # Create log data (instance status)
        instance_status_data = []
        if 'InstanceStatuses' in response:
            for instance in response['InstanceStatuses']:
                instance_info = {
                    'instance_id': instance['InstanceId'],
                    'instance_state': instance['InstanceState']['Name'],
                    'availability_zone': instance['AvailabilityZone'],
                    'status': instance['InstanceStatus']['Status'],
                    'last_updated': instance['InstanceStatus']['Details'][0]['Timestamp'].strftime('%Y-%m-%d %H:%M:%S')
                }
                instance_status_data.append(instance_info)
        
        # Format data as JSON
        log_data = json.dumps(instance_status_data, indent=4)

        # Create a unique file name for the logs
        current_time = datetime.datetime.utcnow()
        file_name = f"ec2_instance_status_{current_time.strftime('%Y-%m-%d_%H-%M-%S')}.json"

        # Upload logs to S3
        s3.put_object(
            Bucket=s3_bucket_name,
            Key=file_name,
            Body=log_data,
            ContentType='application/json'
        )
        print(f"Logs successfully stored in S3 bucket {s3_bucket_name} as {file_name}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
