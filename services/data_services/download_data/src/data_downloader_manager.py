import os
from typing import List, Dict

import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
import pandas as pd

from .data_sources.data_downloader import DataDownloader
from minio_manager import MinIOManager


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
            self.minio_manager = MinIOManager(kwargs['bucket_name'])

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

        save_path = os.path.join(self.save_dir, ticker_name + '.csv')

        if self.save_type == 's3':
            self.minio_manager.save_dataframe(df, save_path)
            print(f'Saved {ticker_name} data to bucket {self.minio_manager.bucket_name} as {save_path}')
        elif self.save_type == 'local':
            self._save_dataframe_locally(df=df, save_path=save_path)
            print(f'Saved {ticker_name} on path: {save_path}')
        else:
            raise ValueError(f'Save type {self.save_type} not handled!')


    @staticmethod
    def _save_dataframe_locally(df: pd.DataFrame, save_path: str) -> None:
        # Ensure the directory exists
        directory = os.path.dirname(save_path)
        os.makedirs(directory, exist_ok=True)

        # Save
        df.to_csv(save_path, index=True)
