import yfinance as yf 
import pandas as pd

class Data_Manager:
    def __init__(self):
        self.proveedor = "Yahoo Finance"

    def download_data(self, ticker, periodo):
        clean_ticker = ticker.strip().upper()
        clean_period = periodo.strip().lower()
        print(f"Downloading data for {clean_ticker} from {self.proveedor}...")

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
        raw_dataframe = ticker_data.history(period=clean_period, interval=clean_interval)

        if raw_dataframe.empty:
            raise ValueError(f" Coudln't reach data {clean_ticker}")
        
        return raw_dataframe

    def process_data(self, raw_dataframe):
        if raw_dataframe.empty:
            print("⚠️ Empty DataFrame.")
            return raw_dataframe
        df = raw_dataframe.copy()
        df['MA5'] = df['Close'].rolling(window=5).mean()
        df['MA20'] = df['Close'].rolling(window=20).mean()

        return df
    