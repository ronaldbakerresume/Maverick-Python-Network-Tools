"""
Cloud Security Auditor
Developer: Ronald Baker

This script audits AWS S3 buckets for misconfigurations, including:
- Publicly accessible buckets
- Weak permissions
- Exposed sensitive files

Instructions:
1. Ensure you have AWS credentials configured locally (e.g., using `aws configure`).
2. Run the script from the terminal.
3. The script will audit S3 buckets and display results.
4. Modify this script to extend functionality as needed.

Required Libraries:
- boto3 (Install with `pip install boto3`)

Usage:
python3 cloud_security_auditor.py
"""

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_buckets():
    """
    Lists all S3 buckets in the AWS account.

    :return: A list of bucket names.
    """
    try:
        s3 = boto3.client("s3")
        response = s3.list_buckets()
        buckets = [bucket["Name"] for bucket in response.get("Buckets", [])]
        return buckets
    except (NoCredentialsError, PartialCredentialsError):
        print("Error: AWS credentials not configured. Run 'aws configure' to set up credentials.")
        exit(1)
    except Exception as e:
        print(f"Error listing buckets: {e}")
        return []

def audit_bucket(bucket_name):
    """
    Audits a specific S3 bucket for public access and sensitive files.

    :param bucket_name: The name of the bucket to audit.
    """
    print(f"\nAuditing bucket: {bucket_name}")

    s3 = boto3.client("s3")
    try:
        # Check bucket policy
        policy = s3.get_bucket_policy(Bucket=bucket_name)
        print(f"Bucket policy found for {bucket_name}: {policy['Policy']}")
    except s3.exceptions.ClientError:
        print(f"No bucket policy found for {bucket_name}.")

    try:
        # Check public ACL
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        for grant in acl["Grants"]:
            if "AllUsers" in str(grant["Grantee"]) or "AuthenticatedUsers" in str(grant["Grantee"]):
                print(f"Warning: {bucket_name} is publicly accessible via ACL.")
    except Exception as e:
        print(f"Error checking ACL for {bucket_name}: {e}")

    try:
        # List and check files for sensitive information
        objects = s3.list_objects_v2(Bucket=bucket_name)
        if "Contents" in objects:
            for obj in objects["Contents"]:
                print(f"File found: {obj['Key']} (Size: {obj['Size']} bytes)")
                if obj["Key"].lower().endswith((".pem", ".key", ".env", "credentials")):
                    print(f"Warning: Sensitive file detected in {bucket_name}: {obj['Key']}")
        else:
            print(f"No files found in {bucket_name}.")
    except Exception as e:
        print(f"Error listing objects in {bucket_name}: {e}")

if __name__ == "__main__":
    print("Welcome to the Cloud Security Auditor.")
    print("Developer: Ronald Baker\n")

    # List all buckets
    buckets = list_buckets()
    if not buckets:
        print("No S3 buckets found.")
        exit(0)

    print(f"Found {len(buckets)} bucket(s):")
    for bucket in buckets:
        print(f"- {bucket}")

    # Audit each bucket
    for bucket in buckets:
        audit_bucket(bucket)

