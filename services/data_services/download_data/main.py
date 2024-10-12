from config import DOWNLOAD_DATA_CONFIG
from data_downloader_manager import DataDownloaderManager
from data_sources.yahoo.yahoo_data_downloader import YahooDataDownloader

if __name__ == '__main__':

    data_downloaders = [
        YahooDataDownloader(),
    ]

    data_downloader_manager = DataDownloaderManager(data_downloaders)
    data_downloader_manager.execute_all(config=DOWNLOAD_DATA_CONFIG)
