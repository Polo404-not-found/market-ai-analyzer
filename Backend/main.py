from interfaz import selector_mercado
from IA import AnalistaIA    
from datos import GestorDatos

class ControladorApp:
    def __init__(self):
        self.selector = selector_mercado()
        self.datos = GestorDatos()
        self.ia = AnalistaIA()

    def iniciar_aplicacion(self):
        self.selector.renderizar_interfaz()
        ticker_usuario = input("Ingrese el ticker del mercado (por ejemplo, BTC-USD): ")
        periodo_usuario = input("Ingrese el período de tiempo (por ejemplo, 1mo, 3mo, 6mo, 1y): ")
        self.Coordinar_Datos(ticker = ticker_usuario, periodo = periodo_usuario)

    def Coordinar_Datos(self, ticker = "BTC-USD", periodo = "1mo"):        
        data_cruda = self.datos.descargar_datos(ticker, periodo)
        data_lista = self.datos.calcular_indicadores(data_cruda)

        prompt = self.ia.construir_prompt(data_lista)
        reporte = self.ia.generar_reporte(prompt)

        self.selector.mostrar_grafico(data_lista)
        self.selector.mostrar_analisis_ia(reporte)

if __name__ == "__main__":
    app = ControladorApp()
    app.iniciar_aplicacion()
