from google import genai 
import os

class AnalistaIA:
    def __init__(self):
        self.modelo = "gemini-3.5-flash"
        self._client = None

    @property 
    def client(self):
        if self._client is None:
            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("No se a configurado la API key de Gemini")
            self._client = genai.Client()
        return self._client 
        

    def construir_prompt(self, datos_procesados):
        print("Construyendo prompt para el análisis de IA...")
        ultimos_dias = datos_procesados[['Close', 'MA5', 'MA20']].tail(7).to_string()
        prompt = f""" Actúa como un Analista Financiero Senior y experto en Trading Cuantitativo.
            Analiza la siguiente tabla de datos históricos recientes que contiene el Precio de Cierre (Close),
            la Media Móvil Rápida (MA5) y la Media Móvil Lenta (MA20).
        
            Datos del mercado:
            {ultimos_dias}
        
            Por favor, genera un reporte breve y directo que incluya:
            1. Diagnóstico de la tendencia actual (¿Está alcista, bajista o lateral?). Justifica mirando la relación entre Close, MA5 and MA20.
            2. Análisis económico del comportamiento del precio en los últimos días.
            3. Posibles escenarios o predicciones probabilísticas para las próximas jornadas basándote en la fuerza de los indicadores.
                
            Sé muy profesional, claro y técnico en tu lenguaje.
            Responde únicamente utilizando texto plano y formato Markdown estándar. NO utilices LaTeX ni sintaxis como \\text{{}} o $$ para fórmulas matemáticas
            """
        return prompt

    def generar_reporte(self, prompt_financiero):
        print(f"Consultando modelo {self.modelo} para predicción...")
        try:
            response = self.client.models.generate_content(
                model = self.modelo,
                contents = prompt_financiero
            )
            return response.text
        except Exception as e:
            return f"⚠️ Error al generar reporte: {e}"