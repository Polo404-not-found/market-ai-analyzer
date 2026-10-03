import os

from google import genai
from google.genai import errors

from Backend.errors import (
    AIAnalysisError,
    AIRateLimitError,
    DataProcessingError,
    MissingApiKeyError,
)


class AIAnalyst:

    def __init__(self):
        self.model = "gemini-3.5-flash"
        self._client = None

    @property
    def client(self):
        if self._client is None:
            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key or not api_key.strip():
                raise MissingApiKeyError()
            self._client = genai.Client()
        return self._client

    def build_prompt(
        self, processed_prices, language="Español", technicality="Medium"
    ):
        print("Building prompt for AI analysis...")
        required_cols = ["Close", "MA5", "MA20"]
        missing_cols = [col for col in required_cols if col not in processed_prices.columns]
        if missing_cols:
            raise DataProcessingError(f"Missing required columns for prompt: {missing_cols}")

        last_days = processed_prices[required_cols].tail(7).to_string()

        tech_instructions = {
            "Low": "Aplica un enfoque sencillo, accesible y con conceptos básicos.",
            "Medium": "Usa una terminología técnica equilibrada propia de trading.",
            "High": (
                "Emplea un lenguaje cuantitativo avanzado, análisis institucional y"
                " métricas rigurosas."
            ),
        }
        desc_tech = tech_instructions.get(technicality, tech_instructions["Medium"])

        prompt = f"""Actúa como un Analista Financiero Senior y experto en Trading Cuantitativo.
Analiza la siguiente tabla de datos históricos recientes que contiene el Precio de Cierre (Close), la Media Móvil Rápida (MA5) y la Media Móvil Lenta (MA20).

Datos del mercado:
{last_days}

Por favor, genera un reporte breve y directo que incluya:
1. Diagnóstico de la tendencia actual (¿Está alcista, bajista o lateral?). Justifica mirando la relación entre Close, MA5 y MA20.
2. Análisis económico del comportamiento del precio en los últimos días.
3. Posibles escenarios o predicciones probabilísticas para las próximas jornadas basándote en la fuerza de los indicadores.
4. Recomendación de acción (comprar, vender o mantener) según tu análisis, especificando que el mercado es imposible de predecir al 100%
y que esta sujeto no solo a matematicas sino tambien a emociones humanas

INSTRUCCIONES CLAVE DE FORMATO Y ESTILO:
- Idioma de respuesta: Debe ser estrictamente en {language}.
- Nivel de tecnicismo: {technicality}. ({desc_tech})
- No incluyas explicaciones sobre cómo generaste el reporte, solo el análisis y las predicciones.
- Al final recomienda el posible escenario más probable y la acción a tomar (comprar, vender o mantener) con base en tu análisis.
- Responde únicamente utilizando texto plano y formato Markdown estándar. NO utilices LaTeX ni sintaxis como \\text{{}} o $$ para fórmulas matemáticas.
"""
        return prompt

    def generate_report(self, financial_prompt: str) -> str:
        print(f"Asking {self.model} for prediction...")
        try:
            response = self.client.models.generate_content(
                model=self.model, contents=financial_prompt
            )
            report = getattr(response, "text", None)
            if not report or not report.strip():
                raise AIAnalysisError(
                    "Gemini returned an empty response or content was blocked by safety filters."
                )
            return report
        except errors.APIError as e:
            error_msg = str(e)
            if getattr(e, "code", None) == 429 or "RESOURCE_EXHAUSTED" in error_msg:
                raise AIRateLimitError() from e
            raise AIAnalysisError(f"Gemini API error: {getattr(e, 'message', error_msg)}") from e
        except MissingApiKeyError:
            raise
        except Exception as e:
            raise AIAnalysisError(f"Unexpected error when connecting to AI model: {e}") from e