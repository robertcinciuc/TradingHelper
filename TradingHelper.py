import yfinance as yf
from datetime import datetime


if __name__ == '__main__':
    
    # CREATE TICKER INSTANCE FOR AMAZON
    amzn = yf.Ticker("AMZN")

    # GET TODAYS DATE AND CONVERT IT TO A STRING WITH YYYY-MM-DD FORMAT (YFINANCE EXPECTS THAT FORMAT)
    end_date = datetime.now().strftime('%Y-%m-%d')
    amzn_hist = amzn.history(interval="1m", period = "1d")
    print(amzn_hist)