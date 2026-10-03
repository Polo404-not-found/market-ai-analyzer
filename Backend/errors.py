class CustomError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class ConfigurationError(CustomError):
    def __init__(self, message: str = "Failed to access system configuration."):
        super().__init__(message)


class MissingApiKeyError(ConfigurationError):
    def __init__(self, message: str = "Gemini API key not found. Please provide it in the panel."):
        super().__init__(message)


class DataFetchError(CustomError):
    def __init__(self, message: str = "Failed to fetch market data."):
        super().__init__(message)


class TickerNotFoundError(DataFetchError):
    def __init__(self, ticker: str):
        message = f"No data found for ticker '{ticker}'. Please verify the symbol."
        super().__init__(message)
        self.ticker = ticker


class DataProcessingError(CustomError):
    def __init__(self, message: str = "Failed to calculate technical indicators on prices."):
        super().__init__(message)


class AIAnalysisError(CustomError):
    def __init__(self, message: str = "Error during AI analysis."):
        super().__init__(message)


class AIRateLimitError(AIAnalysisError):
    def __init__(self, message: str = "Gemini API rate limit exceeded. Please wait a few seconds before retrying."):
        super().__init__(message)