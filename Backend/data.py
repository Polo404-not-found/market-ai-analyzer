import yfinance as yf

from Backend.errors import DataFetchError, DataProcessingError, TickerNotFoundError


class DataManager:
    INTERVAL_MAP = {  # noqa: RUF012
        "1d": "5m",
        "5d": "15m",
        "1mo": "1h",
        "3mo": "1d",
        "6mo": "1d",
        "1y": "1d"
    }

    def __init__(self):
        self.provider = "Yahoo Finance"

    def download_prices(self, ticker: str, period: str):
        clean_ticker = ticker.strip().upper()
        clean_period = period.strip().lower()
        print(f"Downloading data for {clean_ticker} from {self.provider}...")

        clean_interval = self.INTERVAL_MAP.get(clean_period, "1d")

        try:
            ticker_data = yf.Ticker(clean_ticker)
            prices_dataframe = ticker_data.history(period=clean_period, interval=clean_interval)
        except Exception as e:
            raise DataFetchError(f"Failed to connect to {self.provider} for '{clean_ticker}': {e}") from e

        if prices_dataframe is None or prices_dataframe.empty:
            raise TickerNotFoundError(clean_ticker)

        return prices_dataframe

    def process_prices(self, prices_dataframe):
        if prices_dataframe is None or prices_dataframe.empty:
            raise DataProcessingError("Cannot calculate moving averages on an empty dataset.")

        if "Close" not in prices_dataframe.columns:
            raise DataProcessingError("Data does not contain the required 'Close' column for analysis.")

        df = prices_dataframe.copy()
        df["MA5"] = df["Close"].rolling(window=5).mean()
        df["MA20"] = df["Close"].rolling(window=20).mean()

        return df