"""
This is an example script demonstrating how to download data from Yahoo Finance using a custom data downloader class.
It provides a simple workflow for fetching historical stock data for a specified ticker (in default case: MSFT).

The script integrates the YahooDataDownloader class and fetches data for the given time range. Additionally, it uses the
`yfinance` package to retrieve stock information and historical data.

You are encouraged to use breakpoints to inspect the process step-by-step and gain a better understanding of how the
data is fetched and structured.
"""

import yfinance as yf

from services.data_services.download_data.src.data_sources.yahoo.yahoo_data_downloader import YahooDataDownloader

TICKER = "MSFT"
start_date = '2024-01-01'
END_DATE = '2024-02-01'

if __name__ == '__main__':
    yahoo_data_downloader = YahooDataDownloader()

    yahoo_data_downloader.download_data(
        ticker=TICKER,
        start_date=start_date,
        end_date=END_DATE,
    )

    data = yahoo_data_downloader.datasets[TICKER]
    print(data)

    # Define ticker
    msft = yf.Ticker(TICKER)

    # Get all stock info
    print(msft.info)

    # Get historical market data
    hist = msft.history(period="1mo")

    # Show meta information about the history (requires history() to be called first)
    print(msft.history_metadata)
