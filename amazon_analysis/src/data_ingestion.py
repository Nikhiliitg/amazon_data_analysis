# data_ingestion.py
import kagglehub
import os
from config import AWS_BUCKET_NAME, S3_TARGET_PATH
from utils import upload_dataset_to_s3

def download_dataset(dataset_name):
    """Download the dataset from Kaggle."""
    path = kagglehub.dataset_download(dataset_name)
    print(f"Dataset downloaded to {path}")
    return path

def main():
    # Step 1: Download the dataset from Kaggle
    dataset_name = "karkavelrajaj/amazon-sales-dataset"
    local_path = download_dataset(dataset_name)
    
    # Step 2: Upload the downloaded dataset to S3
    upload_dataset_to_s3(local_path, AWS_BUCKET_NAME, S3_TARGET_PATH)

if __name__ == "__main__":
    main()
