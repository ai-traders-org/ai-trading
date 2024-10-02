import yfinance as yf

from src.data.download_data.data_downloader import DataDownloader


class YahooDataDownloader(DataDownloader):

    def __init__(self):
        super().__init__()

    @staticmethod
    def download_data(ticker, start_date, end_date):
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
