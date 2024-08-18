import yfinance as yf

from src.data.download_data.data_downloader import DataDownloader


class YahooDataDownloader(DataDownloader):

    def __init__(self, ticker, start_date, end_date):
        super().__init__()
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def download_data(self):
        data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
        return data
