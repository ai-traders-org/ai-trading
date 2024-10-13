import os
from typing import List, Dict

import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
import pandas as pd

from .data_sources.data_downloader import DataDownloader


class DataDownloaderManager:
    def __init__(self, downloaders: List[DataDownloader], config: Dict, save_type: str = 's3', **kwargs):
        """
        Initializes the class with a list of objects that inherit from DataDownloader.

        :param downloaders: A list of objects of classes that inherit from DataDownloader
        :param save_type: Type of saving mechanism ('s3' or 'local')
        :param config: Dictionary containing configuration for downloading data. The structure of the config is as follows:

        config = {
            'tickers': {
                <source_name>: {<ticker_symbol_1>, <ticker_symbol_2>, ...},
                # For example:
                # 'yahoo': {'BABA', 'MSFT', 'NKE'},
            },
            'time_interval': {
                'start_date': <YYYY-MM-DD>,  # Start date of the data retrieval period
                'end_date': <YYYY-MM-DD>,    # End date of the data retrieval period
            },
            'save_dir': <pathlib.Path object>,  # Directory where downloaded data will be saved
        }
        """
        self.downloaders = downloaders

        self.save_type = save_type

        if 'tickers' not in config or 'time_interval' not in config or 'save_dir' not in config:
            raise ValueError("Config must contain 'tickers', 'time_interval', and 'save_dir'.")

        self.tickers = config['tickers']
        self.save_dir = config['save_dir']
        self.start_date = config['time_interval']['start_date']
        self.end_date = config['time_interval']['end_date']

        if self.save_type == 's3':
            if 'bucket_name' not in kwargs:
                raise ValueError("Missing 'bucket_name' in kwargs for S3 initialization.")

            # initialize MinIO client (S3)
            self.s3_client = boto3.client(
                's3',
                endpoint_url=os.getenv('MINIO_ENDPOINT_URL', 'default-endpoint-url'),
                aws_access_key_id=os.getenv('MINIO_ACCESS_KEY', 'default-access-key'),
                aws_secret_access_key=os.getenv('MINIO_SECRET_KEY', 'default-secret-key'),
                config=Config(signature_version='s3v4'),
                region_name=os.getenv('MINIO_REGION_NAME', 'default-region-name'),
            )

            # ensure bucket exists or create it
            self.bucket_name = kwargs['bucket_name']
            self._ensure_bucket_exists(self.bucket_name)

    def execute_all(self) -> None:
        """
        Executes the download_data method on each of the provided downloader objects.
        """
        for downloader in self.downloaders:
            for ticker in self.tickers[downloader.source_name]:
                downloader.download_data(
                    ticker=ticker,
                    start_date=self.start_date,
                    end_date=self.end_date,
                )
                self._save_dataframe(df=downloader.datasets[ticker], ticker_name=ticker)

    def _save_dataframe(self, df: pd.DataFrame, ticker_name: str) -> None:
        if df is None or df.empty:
            raise ValueError(f"The DataFrame for ticker {ticker_name} is empty or None.")

        # creating a path to a file in the bucket
        save_path = os.path.join(self.save_dir, ticker_name + '.csv')

        if self.save_type == 's3':
            self._save_dataframe_on_minio(df=df, save_path=save_path)
            print(f'Saved {ticker_name} data to bucket {self.bucket_name} as {save_path}')
        elif self.save_type == 'local':
            self._save_dataframe_locally(df=df, save_path=save_path)
            print(f'Saved {ticker_name} on path: {save_path}')
        else:
            raise ValueError(f'Save type {self.save_type} not handled!')

    def _save_dataframe_on_minio(self, df: pd.DataFrame, save_path: str) -> None:
        # convert dataset to CSV
        csv_data = df.to_csv(index=False)

        # sending data to MinIO
        self.s3_client.put_object(
            Bucket=self.bucket_name,
            Key=save_path,
            Body=csv_data.encode('utf-8')
        )

    def _ensure_bucket_exists(self, bucket_name):
        try:
            # check if the bucket exists by trying to list its contents
            self.s3_client.head_bucket(Bucket=bucket_name)
            print(f'Bucket "{bucket_name}" already exists.')
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == '404':
                print(f'Bucket "{bucket_name}" does not exist. Creating a new one.')
                self.s3_client.create_bucket(Bucket=bucket_name)
                print(f'Bucket "{bucket_name}" created.')
            else:
                raise

    @staticmethod
    def _save_dataframe_locally(df: pd.DataFrame, save_path: str) -> None:
        # Ensure the directory exists
        directory = os.path.dirname(save_path)
        os.makedirs(directory, exist_ok=True)

        # Save
        df.to_csv(save_path, index=False)
