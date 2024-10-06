MINIO_CONFIG = {
    'endpoint_url': 'http://minio-release:9000',  # MinIO server address
    'access_key': 'SC1Vv8nqrMFcxIREnV5M',
    'secret_key': '46nb3NHhhbJswXDlGlbdV9oEtxmDHPhaMOxKzPXg',
    'bucket_name': 'downloaded-data-bucket',  # Bucket name in MinIO
    'region_name': 'us-east-1'  # Region, MinIO does not require this, but boto3 may require it
}