import os
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
import pandas as pd

class MinIOManager:
    def __init__(self, bucket_name: str):
        """
        Initializes the MinIOManager with a specified bucket.
        """
        self.s3_client = boto3.client(
            's3',
            endpoint_url=os.getenv('MINIO_ENDPOINT_URL', 'default-endpoint-url'),
            aws_access_key_id=os.getenv('MINIO_ACCESS_KEY', 'default-access-key'),
            aws_secret_access_key=os.getenv('MINIO_SECRET_KEY', 'default-secret-key'),
            config=Config(signature_version='s3v4'),
            region_name=os.getenv('MINIO_REGION_NAME', 'default-region-name'),
        )
        self.bucket_name = bucket_name
        self._ensure_bucket_exists()

    def _ensure_bucket_exists(self):
        try:
            self.s3_client.head_bucket(Bucket=self.bucket_name)
            print(f'Bucket "{self.bucket_name}" already exists.')
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                print(f'Bucket "{self.bucket_name}" does not exist. Creating a new one.')
                self.s3_client.create_bucket(Bucket=self.bucket_name)
                print(f'Bucket "{self.bucket_name}" created.')
            else:
                raise

    def save_dataframe(self, df: pd.DataFrame, save_path: str):
        csv_data = df.to_csv(index=False)
        self.s3_client.put_object(
            Bucket=self.bucket_name,
            Key=save_path,
            Body=csv_data.encode('utf-8')
        )
