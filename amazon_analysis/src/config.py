# config.py
import os

# AWS configuration - use environment variables for security
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_BUCKET_NAME = "tableuproject"
S3_TARGET_PATH = "raw-data/amazon_sales_dataset/"
