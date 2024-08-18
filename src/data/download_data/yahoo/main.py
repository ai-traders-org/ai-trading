import yfinance as yf

if __name__ == '__main__':
    msft = yf.Ticker("MSFT")

    # get all stock info
    print(msft.info)

    # get historical market data
    hist = msft.history(period="1mo")

    # show meta information about the history (requires history() to be called first)
    print(msft.history_metadata)
