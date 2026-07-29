import yfinance as yf 
import pandas as pd

class GestorDatos:
    def __init__(self):
        self.proveedor = "Yahoo Finance"

    def descargar_datos(self, ticker, periodo):
        ticker_limpio = ticker.strip().upper()
        periodo_limpio = periodo.strip().lower()
        print(f"Descargando datos de {ticker} desde {self.proveedor}...")
        ticker_data = yf.Ticker(ticker_limpio)
        dataframe_crudo = ticker_data.history(period=periodo_limpio)

        if dataframe_crudo.empty:
            raise ValueError(f" No se pudieron descargar datos para {ticker_limpio}")
        
        return dataframe_crudo

    def calcular_indicadores(self, dataframe_crudo):
        print("Calculando Medias Móviles de 5 y 20 días con Pandas...")
        if dataframe_crudo.empty:
            print("⚠️ El DataFrame está vacío. No se pueden calcular indicadores.")
            return dataframe_crudo
        df = dataframe_crudo.copy()
        df['MA5'] = df['Close'].rolling(window=5).mean()
        df['MA20'] = df['Close'].rolling(window=20).mean()

        return df
    