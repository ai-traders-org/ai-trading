import os

import boto3
from botocore.client import Config
import yfinance as yf

from ..data_downloader import DataDownloader
from ..minio_config import MINIO_CONFIG


class YahooDataDownloader(DataDownloader):
    source_name = 'yahoo'

    def __init__(self):
        super().__init__()
        self.datasets = {}

        # Initialize MinIO client (S3)
        self.s3_client = boto3.client(
            's3',
            endpoint_url=MINIO_CONFIG['endpoint_url'],
            aws_access_key_id=MINIO_CONFIG['access_key'],
            aws_secret_access_key=MINIO_CONFIG['secret_key'],
            config=Config(signature_version='s3v4'),
            region_name=MINIO_CONFIG['region_name']
        )

        #TODO: define bucket from python code. maybe in upper class

    def download_data(self, ticker, start_date, end_date, *args, **kwargs) -> None:
        data = yf.download(ticker, start=start_date, end=end_date)
        data.drop('Adj Close', axis=1, inplace=True)

        self.datasets[ticker] = data

    def save_data(self, save_dir: str, *args, **kwargs) -> None:
        bucket_name = MINIO_CONFIG['bucket_name']

        for ticker, dataset in self.datasets.items():
            # Convert dataset to CSV
            csv_data = dataset.to_csv(index=False)

            # Creating a path to a file in the bucket
            save_path = os.path.join(save_dir, ticker + '.csv')

            # Sending data to MinIO
            self.s3_client.put_object(
                Bucket=bucket_name,
                Key=save_path,
                Body=csv_data.encode('utf-8')
            )

            print(f'Saved {ticker} data to bucket {bucket_name} as {save_path}')

    @classmethod
    def get_source_name(cls) -> str:
        return cls.source_name
