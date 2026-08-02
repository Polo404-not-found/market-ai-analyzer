from google import genai 
import os

class AI_Analyst:
    def __init__(self):
        self.model = "gemini-3.5-flash"
        self._client = None

    @property 
    def client(self):
        if self._client is None:
            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("API key for Gemini is not set. Please set the GEMINI_API_KEY environment variable.")
            self._client = genai.Client()
        return self._client 
        

    def build_prompt(self, processed_data):
        print("Building prompt for AI analysis...")
        last_days = processed_data[['Close', 'MA5', 'MA20']].tail(7).to_string()
        prompt = f""" Actúa como un Analista Financiero Senior y experto en Trading Cuantitativo.
            Analiza la siguiente tabla de datos históricos recientes que contiene el Precio de Cierre (Close),
            la Media Móvil Rápida (MA5) y la Media Móvil Lenta (MA20).
        
            Datos del mercado:
            {last_days}
        
            Por favor, genera un reporte breve y directo que incluya:
            1. Diagnóstico de la tendencia actual (¿Está alcista, bajista o lateral?). Justifica mirando la relación entre Close, MA5 and MA20.
            2. Análisis económico del comportamiento del precio en los últimos días.
            3. Posibles escenarios o predicciones probabilísticas para las próximas jornadas basándote en la fuerza de los indicadores.
                
            Sé muy profesional, claro y técnico en tu lenguaje y hazlo en Inlés. No incluyas explicaciones sobre cómo generaste el reporte, solo el análisis y las predicciones.
            Al final recomienda el posible escenario mas probable y la acción a tomar (comprar, vender o mantener) con base en tu análisis.
            Responde únicamente utilizando texto plano y formato Markdown estándar. NO utilices LaTeX ni sintaxis como \\text{{}} o $$ para fórmulas matemáticas
            """
        return prompt

    def generate_report(self, financial_prompt):
        print(f"Asking {self.model} for prediction...")
        try:
            response = self.client.models.generate_content(
                model = self.model,
                contents = financial_prompt
            )
            return response.text
        except Exception as e:
            return f"⚠️ Crashed: {e}"