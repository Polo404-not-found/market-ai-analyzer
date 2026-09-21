from Backend.ai import AIAnalyst
from Backend.data import DataManager


class AppController:
    def __init__(self):
        self.data = DataManager()
        self.ai = AIAnalyst()

    def coordinate_data(self, ticker = "BTC-USD", period = "1mo", language = "English", technicality_level = "Medium"):
        raw_prices = self.data.download_prices(ticker, period)
        processed_prices = self.data.process_prices(raw_prices)

        prompt = self.ai.build_prompt(processed_prices, language, technicality_level)
        report = self.ai.generate_report(prompt)
        return processed_prices, report 
    
