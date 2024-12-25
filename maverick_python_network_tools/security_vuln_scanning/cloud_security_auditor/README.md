# Cloud Security Auditor

**Developer**: Ronald Baker  

## Description

This script **audits AWS S3 buckets** for potential misconfigurations, focusing on:
- **Publicly accessible buckets** via ACLs or bucket policies  
- **Weak permissions** (exposing the bucket to `AllUsers` or `AuthenticatedUsers`)  
- **Exposed sensitive files** (e.g., `.pem`, `.key`, `.env`, or `credentials` files)

## Requirements

- Python 3  
- **boto3** (`pip install boto3`)  
- AWS credentials configured locally (run `aws configure`)

## Usage

1. **Configure AWS Credentials**:
   ```bash
   aws configure
   ```
2. **Run**:
   ```bash
   python3 cloud_security_auditor.py
   ```
3. The script will:
   1. **List all** S3 buckets in your AWS account
   2. **Audit** each bucket’s:
      - Bucket **policy** (if available)
      - Bucket **ACL** to check if it’s publicly accessible
      - **Objects** in the bucket, flagging potentially **sensitive files**

**Example session**:
```
Welcome to the Cloud Security Auditor.
Developer: Ronald Baker

Found 3 bucket(s):
- my-example-bucket
- logs-bucket
- private-bucket

Auditing bucket: my-example-bucket
Bucket policy found for my-example-bucket: { ... }
Warning: my-example-bucket is publicly accessible via ACL.
File found: credentials.txt (Size: 244 bytes)
Warning: Sensitive file detected in my-example-bucket: credentials.txt

Auditing bucket: logs-bucket
No bucket policy found for logs-bucket.
No files found in logs-bucket.

Auditing bucket: private-bucket
Bucket policy found for private-bucket: { ... }
File found: config.env (Size: 102 bytes)
Warning: Sensitive file detected in private-bucket: config.env
```

## Notes

- The script can be extended to scan for additional **file patterns** (e.g., `.json`, `.yaml` secrets).  
- Adjust **IAM permissions** and roles as needed for reading bucket policies and object listings.  

## Author

Ronald Baker  

## License & Disclaimer

Use at your own risk. This script is provided “as-is” for educational or investigative purposes.  
See the disclaimer above for complete terms.  
```