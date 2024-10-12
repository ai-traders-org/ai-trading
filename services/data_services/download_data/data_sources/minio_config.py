import os

MINIO_CONFIG = {
    'endpoint_url': 'http://minio-release:9000',  # MinIO server address
    'access_key': os.getenv('MINIO_ACCESS_KEY', 'default-access-key'),
    'secret_key': os.getenv('MINIO_SECRET_KEY', 'default-secret-key'),
    'bucket_name': 'downloaded-data-bucket',  # Bucket name in MinIO
    'region_name': 'us-east-1'  # Region, MinIO does not require this, but boto3 may require it
}