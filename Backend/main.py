from Backend.ai import AI_Analyst   
from Backend.data import Data_Manager

class App_Controller:
    def __init__(self):
        self.data = Data_Manager()
        self.ai = AI_Analyst()

    def Coordinate_Data(self, ticker = "BTC-USD", period = "1mo"):        
        raw_data = self.data.download_data(ticker, period)
        processed_data = self.data.process_data(raw_data)

        prompt = self.ai.build_prompt(processed_data)
        report = self.ai.generate_report(prompt)
        return processed_data, report 
    
