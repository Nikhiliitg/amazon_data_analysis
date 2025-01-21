import boto3
import pandas as pd
from io import StringIO
import os

class ETLPipeline:
    def __init__(self, aws_access_key, aws_secret_key, bucket_name, input_path, output_path):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )
        self.bucket_name = bucket_name
        self.input_path = input_path
        self.output_path = output_path

    def read_csv_from_s3(self):
        """Reads a CSV file from S3 and loads it into a pandas DataFrame."""
        try:
            obj = self.s3_client.get_object(Bucket=self.bucket_name, Key=self.input_path)
            data = obj['Body'].read().decode('utf-8')
            df = pd.read_csv(StringIO(data))
            return df
        except Exception as e:
            print(f"Error reading CSV from S3: {e}")
            return None

    def transform_data(self, df):
        """Transforms the raw data."""
        try:
            df.columns = df.columns.astype(str).str.lower().str.replace(' ', '_')

            # Retain only relevant columns for analysis
            columns_to_keep = [
                'category', 
                'discounted_price', 
                'actual_price', 
                'discount_percentage', 
                'rating', 
                'rating_count'
            ]
            df = df.loc[:, columns_to_keep]

            # Clean up pricing and discount data
            df['discounted_price'] = df['discounted_price'].str.replace('₹', '').str.replace(',', '').astype(float)
            df['actual_price'] = df['actual_price'].str.replace('₹', '').str.replace(',', '').astype(float)
            df['discount_percentage'] = df['discount_percentage'].str.replace('%', '').astype(float)

            # Convert ratings and rating_count to numeric
            df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
            df['rating_count'] = pd.to_numeric(df['rating_count'].str.replace(',', ''), errors='coerce')

            # Handle missing values (fill numeric columns with mean or 0)
            numeric_columns = ['discounted_price', 'actual_price', 'discount_percentage', 'rating', 'rating_count']
            for col in numeric_columns:
                if df[col].isnull().any():
                    fill_value = 0 if df[col].dtype == 'int64' else df[col].mean()
                    df[col].fillna(fill_value, inplace=True)

            # Drop duplicate rows
            df.drop_duplicates(inplace=True)

            return df
        except Exception as e:
            print(f"Error transforming data: {e}")
            return None

    def upload_df_to_s3(self, df):
        """Uploads a DataFrame to S3 as a CSV file."""
        try:
            csv_buffer = StringIO()
            df.to_csv(csv_buffer, index=False)

            self.s3_client.put_object(Bucket=self.bucket_name, Key=self.output_path, Body=csv_buffer.getvalue())
            print(f"Transformed data uploaded to s3://{self.bucket_name}/{self.output_path}")
        except Exception as e:
            print(f"Error uploading data to S3: {e}")

    def run_pipeline(self):
        """Full ETL pipeline execution."""
        print("Reading data from S3...")
        raw_data = self.read_csv_from_s3()
        if raw_data is None:
            return 
        
        print("Transforming data...")
        transformed_data = self.transform_data(raw_data)
        if transformed_data is None:
            return 
        
        print("Uploading transformed data to S3...")
        self.upload_df_to_s3(transformed_data)

if __name__ == "__main__":
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_BUCKET_NAME = 'tableuproject'
    S3_INPUT_PATH = 'raw-data/amazon_sales_dataset/amazon.csv'
    S3_OUTPUT_PATH = 'transformed-data/amazon_sales_dataset/transformed_amazon.csv'

    etl = ETLPipeline(
        aws_access_key=AWS_ACCESS_KEY,
        aws_secret_key=AWS_SECRET_KEY,
        bucket_name=AWS_BUCKET_NAME,
        input_path=S3_INPUT_PATH,
        output_path=S3_OUTPUT_PATH
    )
    etl.run_pipeline()
