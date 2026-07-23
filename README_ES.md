[English](README.md)

# Market AI Analyzer

Un saludo antes de iniciar.

Hola, Querido usuario soy Polo, un placer tenerte aquí leyendo esto, quería agradecerte por descargar este proyecto el cual le e invertido un tiempo, soy bastante novato en el ámbito de la programación y mas en Python pero, lo logre, me apoye en la IA principalmente para conocer el sintaxis correcto y la solución de un que otro error, el proyecto nace de mi gusto por la programación y sistemas junto con el gusto a la economía y mercados, y se me ideo esta herramienta.
Te agradecería cualquier feedback.

Analizador de mercados financieros que combina datos históricos reales 
con indicadores técnicos (medias móviles) y análisis generado por 
inteligencia artificial (Gemini).

## ¿Qué hace?

- Descarga datos históricos de cualquier activo disponible en Yahoo Finance 
  (acciones, criptomonedas, futuros, ETFs)
- Calcula medias móviles de 5 y 20 días (MA5, MA20)
- Genera un reporte técnico profesional usando IA, con diagnóstico de 
  tendencia, análisis del comportamiento del precio, y escenarios 
  probabilísticos a futuro

## Requisitos

- Python 3.10+
- Una API key gratuita de Google AI Studio: https://aistudio.google.com/

## Instalación

1. Clona este repositorio:
git clone https://github.com/Its-Juanes/market-ai-analyzer.git

2. Instala las dependencias:
pip install -r requirements.txt

3. Configura tu propia API key como variable de entorno:

Windows (PowerShell):
$env:GEMINI_API_KEY="tu-key-aqui"

4. Corre la app:
python Backend/main.py

## Uso

La app te va a pedir un ticker (ej: BTC-USD, AAPL, GC=F) y un 
periodo de tiempo (ej: 1mo, 3mo, 1y), y te devolverá el gráfico 
de datos junto con un análisis técnico generado por IA.
