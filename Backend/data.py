import pandas as pd
import yfinance as yf


class DataManager:
    def __init__(self):
        self.provider = "Yahoo Finance"

    def download_prices(self, ticker, period):
        clean_ticker = ticker.strip().upper()
        clean_period = period.strip().lower()
        print(f"Downloading data for {clean_ticker} from {self.provider}...")

        interval_map = {
            "1d": "5m",
            "5d": "15m",
            "1mo": "1h",
            "3mo": "1d",
            "6mo": "1d",
            "1y": "1d"
        }
        clean_interval = interval_map.get(clean_period, "1d")
        ticker_data = yf.Ticker(clean_ticker)
        prices_dataframe = ticker_data.history(period=clean_period, interval=clean_interval)

        if prices_dataframe.empty:
            raise ValueError(f" Coudln't reach data {clean_ticker}")
        
        return prices_dataframe

    def process_prices(self, prices_dataframe):
        if prices_dataframe.empty:
            print("⚠️ Empty DataFrame.")
            return prices_dataframe
        df = prices_dataframe.copy()
        df['MA5'] = df['Close'].rolling(window=5).mean()
        df['MA20'] = df['Close'].rolling(window=20).mean()

        return df
    