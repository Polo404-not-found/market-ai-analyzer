import yfinance as yf 
import pandas as pd

class GestorDatos:
    def __init__(self):
        self.proveedor = "Yahoo Finance"

    def descargar_datos(self, ticker, periodo):
        print(f"Descargando datos de {ticker} desde {self.proveedor}...")
        ticker_data = yf.Ticker(ticker)
        dataframe_crudo = ticker_data.history(period=periodo)

        if dataframe_crudo.empty:
            raise ValueError(f" No se pudieron descargar datos para {ticker}")
        
        return dataframe_crudo

    def calcular_indicadores(self, dataframe_crudo):
        print("Calculando Medias Móviles de 5 y 20 días con Pandas...")
        if dataframe_crudo.empty:
            print("⚠️ El DataFrame está vacío. No se pueden calcular indicadores.")
            return dataframe_crudo
        dataframe_crudo['MA5'] = dataframe_crudo['Close'].rolling(window=5).mean()
        dataframe_crudo['MA20'] = dataframe_crudo['Close'].rolling(window=20).mean()

        return dataframe_crudo
    