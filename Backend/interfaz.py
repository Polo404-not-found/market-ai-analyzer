import pandas as pd

class selector_mercado:
    def __init__(self):
        self.ticker = ""
        self.periodo = "1mo"

    def renderizar_interfaz(self):
        print("Renderizando barra de búsqueda y botones...")

    def mostrar_grafico(self, datos_procesados):
        print("Dibujando gráfico de velas interactivas con los datos...")
        if datos_procesados is None or datos_procesados.empty:
            print("⚠️ No hay datos para mostrar en el gráfico.")
            return
        try:
            if isinstance(datos_procesados.columns, pd.MultiIndex):
                datos_procesados.columns = datos_procesados.columns.get_level_values(0)
        except Exception as e:
            print(f"Error al formatear las columnas: {e}")
            print("Mostrando lista de columnas disponibles:")
            print(datos_procesados.head(2))

        print(datos_procesados[['Close', 'MA5', 'MA20']].tail(3))

    def mostrar_analisis_ia(self, reporte_texto):
        print("mostrando reporte en pantalla \n")
        print(reporte_texto)