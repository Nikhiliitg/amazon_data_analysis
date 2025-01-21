# utils.py
import boto3
from pathlib import Path
from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME, S3_TARGET_PATH

def get_s3_client():
    """Create an S3 client using the provided AWS credentials."""
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
    )
    return s3_client

def upload_file_to_s3(file_path, bucket_name, s3_key):
    """Uploads a file to S3."""
    s3_client = get_s3_client()
    s3_client.upload_file(file_path, bucket_name, s3_key)
    print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_key}")

def upload_dataset_to_s3(local_path, bucket_name, s3_target_path):
    """Uploads all files from a local directory to an S3 bucket."""
    for file in Path(local_path).rglob("*"):
        if file.is_file():
            s3_key = s3_target_path + file.name
            upload_file_to_s3(str(file), bucket_name, s3_key)
