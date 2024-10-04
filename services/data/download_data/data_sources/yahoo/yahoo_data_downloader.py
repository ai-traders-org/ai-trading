import os

import yfinance as yf

from ..data_downloader import DataDownloader


class YahooDataDownloader(DataDownloader):
    source_name = 'yahoo'

    def __init__(self):
        super().__init__()
        self.datasets = {}

    def download_data(self, ticker, start_date, end_date, *args, **kwargs) -> None:
        data = yf.download(ticker, start=start_date, end=end_date)
        data.drop('Adj Close', axis=1, inplace=True)

        self.datasets[ticker] = data

    def save_data(self, save_dir: str, *args, **kwargs) -> None:
        os.makedirs(save_dir, exist_ok=True)
        for ticker, dataset in self.datasets.items():
            save_path = os.path.join(save_dir, ticker + '.csv')
            dataset.to_csv(save_path)
            print(f'Saved {ticker} to {save_path}')

    @classmethod
    def get_source_name(cls) -> str:
        return cls.source_name