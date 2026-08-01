from Backend.ia import AnalistaIA    
from Backend.datos import GestorDatos

class ControladorApp:
    def __init__(self):
        self.datos = GestorDatos()
        self.ia = AnalistaIA()

    def Coordinar_Datos(self, ticker = "BTC-USD", periodo = "1mo"):        
        data_cruda = self.datos.descargar_datos(ticker, periodo)
        data_lista = self.datos.calcular_indicadores(data_cruda)

        prompt = self.ia.construir_prompt(data_lista)
        reporte = self.ia.generar_reporte(prompt)
        return data_lista, reporte 
    
