import argparse

from src.config import DOWNLOAD_DATA_CONFIG
from src.data_downloader_manager import DataDownloaderManager
from src.data_sources.yahoo.yahoo_data_downloader import YahooDataDownloader

parser = argparse.ArgumentParser(description="Download data using different save types")
parser.add_argument('--save-type', type=str, choices=['s3', 'local'],
                    help="Specify the save type: 's3' or 'local'")

if __name__ == '__main__':
    args = parser.parse_args()

    data_downloaders = [
        YahooDataDownloader(),
    ]

    data_downloader_manager = DataDownloaderManager(
        downloaders=data_downloaders,
        config=DOWNLOAD_DATA_CONFIG,
        save_type=args.save_type,
        bucket_name='downloaded-data-bucket',  # bucket name in MinIO (in kwargs)
    )
    data_downloader_manager.execute_all()
