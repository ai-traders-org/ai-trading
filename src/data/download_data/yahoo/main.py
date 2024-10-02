import yfinance as yf

from src.data.download_data.yahoo.yahoo_data_downloader import YahooDataDownloader

if __name__ == '__main__':
    yahoo_data_downloader = YahooDataDownloader

    data = yahoo_data_downloader.download_data("MSFT", '2024-01-01', '2024-02-01')


    print(data)

    msft = yf.Ticker("MSFT")

    # get all stock info
    print(msft.info)

    # get historical market data
    hist = msft.history(period="1mo")

    # show meta information about the history (requires history() to be called first)
    print(msft.history_metadata)
