from typing import List

from data_sources.data_downloader import DataDownloader


class DataDownloaderManager:
    def __init__(self, downloaders: List[DataDownloader]):
        """
        Initializes the class with a list of objects that inherit from DataDownloader.

        :param downloaders: A list of objects of classes that inherit from DataDownloader
        """
        self.downloaders = downloaders

    def execute_all(self, config) -> None:
        """
        Executes the download_data method on each of the provided downloader objects.

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
        for downloader in self.downloaders:
            for ticker in config['tickers'][downloader.source_name]:
                downloader.download_data(
                    ticker=ticker,
                    start_date=config['time_interval']['start_date'],
                    end_date=config['time_interval']['end_date'],
                )
            downloader.save_data(save_dir=config['save_dir'])
