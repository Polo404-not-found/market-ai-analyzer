[Español](README_ES.md)

# Market AI Analyzer

### A quick note before you start

Hi, dear reader, I'm Polo — welcome, and thanks for checking out this project. I put real time and effort into building it. I'm still fairly new to programming, and even newer to Python, but I got it working. I leaned on AI mainly to learn correct syntax and to solve the occasional error along the way. The project comes from my interest in programming and systems combined with my interest in economics and markets, and that's how this tool came to be.

I'd really appreciate any feedback.

---

Financial market analyzer that combines real historical data with 
technical indicators (moving averages) and AI-generated analysis 
(Gemini).

## What it does

- Downloads historical data for any asset available on Yahoo Finance 
  (stocks, cryptocurrencies, futures, ETFs)
- Calculates 5-day and 20-day moving averages (MA5, MA20)
- Generates a professional technical report using AI, including trend 
  diagnosis, price behavior analysis, and probabilistic scenarios for 
  the near future

## Requirements

- Python 3.10+
- A free API key from Google AI Studio: https://aistudio.google.com/

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Its_Juanes/market-ai-analyzer.git
   ```

2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set your own API key as an environment variable:

   Windows (PowerShell):
   ```
   $env:GEMINI_API_KEY="your-key-here"
   ```

4. Run the app:
   ```
   python Backend/main.py
   ```

## Usage

The app will ask you for a ticker (e.g. `BTC-USD`, `AAPL`, `GC=F`) and 
a time period (e.g. `1mo`, `3mo`, `1y`), and it will return the data 
chart along with an AI-generated technical analysis.