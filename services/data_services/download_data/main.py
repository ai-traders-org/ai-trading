from src.download_data_config import DOWNLOAD_DATA_CONFIG
from src.data_downloader_manager import DataDownloaderManager
from src.data_sources.yahoo.yahoo_data_downloader import YahooDataDownloader

if __name__ == '__main__':
    data_downloaders = [
        YahooDataDownloader(),
    ]

    data_downloader_manager = DataDownloaderManager(
        downloaders=data_downloaders,
        config=DOWNLOAD_DATA_CONFIG,
        save_type='s3',  # 's3' or 'locally'
        bucket_name='downloaded-data-bucket',  # bucket name in MinIO (in kwargs)
    )
    data_downloader_manager.execute_all()
