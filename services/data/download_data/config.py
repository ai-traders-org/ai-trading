import os

DOWNLOAD_DATA_CONFIG = {
    'tickers': {
        'yahoo': {'BABA', 'MSFT', 'NKE'},
    },
    'time_interval': {
        'start_date': '2024-01-01',
        'end_date': '2024-02-01',
    },
    'save_dir': os.path.join('resources', 'datasets'),
}

MINIO_CONFIG = {
    'endpoint_url': 'http://localhost:9000',  # Adres serwera MinIO
    'access_key': 'minio-access-key',
    'secret_key': 'minio-secret-key',
    'bucket_name': 'my-bucket',  # Nazwa bucketu w MinIO
    'region_name': 'us-east-1'  # Region, MinIO nie wymaga tego, ale boto3 może to wymagać
}