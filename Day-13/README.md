# EC2 Status Logger - Lambda Function

## Overview

The **EC2 Status Logger** Lambda function retrieves the status of EC2 instances every 12 hours and stores the logs in an **S3 bucket**. This solution automates the monitoring of EC2 instance statuses, making it easier to track their health and status over time.

The function is scheduled to run every 12 hours using **AWS CloudWatch Events**.

---

## Features

- Retrieve EC2 instance status (e.g., running, stopped) for specified instances.
- Store EC2 instance status logs in an **S3 bucket**.
- Automatically run every 12 hours via **CloudWatch Events**.
- Easy-to-use with AWS Lambda and minimal setup.

---

## Prerequisites

Before you begin, you need the following:

- **AWS Account**: You need access to AWS to create resources like Lambda functions, CloudWatch Events, and S3 buckets.
- **EC2 Instance(s)**: The EC2 instances you want to monitor must be running in your AWS account.
- **IAM Role**: Lambda needs the appropriate IAM permissions to interact with EC2 and S3.
- **S3 Bucket**: You must have an S3 bucket to store the logs.

---

## IAM Role Configuration

You need to ensure that your **Lambda execution role** has the appropriate permissions to interact with EC2 and S3. 

### Example IAM Policy for Lambda Execution Role

Attach the following policy to the Lambda execution role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstanceStatus"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::your-s3-bucket/*"
    }
  ]
}

``` 
How to Deploy
Step 1: Create a Lambda Function
Go to the AWS Console and navigate to Lambda.

Click Create Function.

Select Author from Scratch and fill in the following:

Function Name: ec2_status_logger

Runtime: Python 3.8 or later

Execution Role: Select an existing role with the necessary permissions or create a new one with the EC2 and S3 permissions.

Paste the provided Python code into the Lambda code editor.

Click Deploy.

Step 2: Set Up CloudWatch Events Rule
To trigger the Lambda function every 12 hours:

Go to AWS Console → CloudWatch → Rules → Create Rule.

Choose Event Source as Schedule.

Set the schedule to rate(12 hours) or use a cron expression like cron(0 */12 * * ? *).

Add a target and select Lambda function.

Choose your Lambda function (ec2_status_logger).

Create the rule.

Step 3: Verify Lambda Execution
CloudWatch Logs: Go to CloudWatch Logs → Log Groups → Look for your Lambda function log group.

S3 Bucket: Check your S3 bucket to ensure that the EC2 status logs are stored as .json files.