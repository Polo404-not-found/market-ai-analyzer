# Market AI Analyzer

### A quick note before you start

Hi, dear reader, I'm Polo — welcome, and thanks for checking out this project. I put real time and effort into building it. I'm still fairly new to programming, and even newer to Python, but I got it working. I leaned on AI mainly to learn correct syntax, connect to external libraries correctly, and solve occasional errors along the way — every line was written with a clear understanding of what it does and why. The project comes from my interest in programming and systems combined with my interest in economics and markets, and that's how this tool came to be.

I'd really appreciate any feedback.

Financial market analyzer that combines real historical data with technical indicators (moving averages) and AI-generated analysis (Gemini), now with a basic desktop GUI built with PySide6.

Financial market analyzer that combines real historical data with technical indicators (moving averages) and AI-generated analysis (Gemini), now with a basic desktop GUI built with PySide6.

Or the original command-line version:

- Downloads historical data for any asset available on Yahoo Finance (stocks, cryptocurrencies, futures, ETFs)
- Calculates 5-day and 20-day moving averages (MA5, MA20)
- Generates a professional technical report using AI, including trend diagnosis, price behavior analysis, and probabilistic scenarios for the near future
- Provides a basic desktop GUI (PySide6) to enter a ticker and time period and view results without using the terminal

## Project structure

```
Backend/       # Core logic: data fetching, indicators, Gemini integration (OOP)
GUI.py         # Desktop interface built with PySide6
requirements.txt
```

## Requirements

- Python 3.10+
- A free API key from Google AI Studio: https://aistudio.google.com/
- PySide6 (included in requirements.txt)

## Installation

1. Clone this repository:

```
git clone https://github.com/Polo404-not-found/market-ai-analyzer.git
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

   Desktop GUI:
   ```
   python GUI.py
   ```

   Or the original command-line version:
   ```
   python Backend/main.py
Usage

Enter a ticker (e.g. BTC-USD, AAPL, GC=F) and a time period (e.g. 1mo, 3mo, 1y) in the GUI, or when prompted in the terminal version, and the app will return the data chart along with an AI-generated technical analysis.

Enter a ticker (e.g. `BTC-USD`, `AAPL`, `GC=F`) and a time period (e.g. `1mo`, `3mo`, `1y`) in the GUI, or when prompted in the terminal version, and the app will return the data chart along with an AI-generated technical analysis.

## Development notes

This project was built in stages rather than all at once:

- **Backend first**: the data-fetching, indicator calculation, and Gemini integration were designed with an object-oriented structure from the start.
- **GUI, iteratively**: I spent time working directly from the official PySide6 documentation before writing any GUI code. Where the docs were unclear or too sparse to get unstuck, I used AI to clarify exact syntax for connecting widgets to the backend logic — never to generate logic I didn't understand. The current `GUI.py` is a first working version; a refactor into separate, OOP-based modules (mirroring the backend's structure) is planned next.
- **AI as a tool, not a shortcut**: throughout the project, AI was used to speed up learning correct library syntax and debug specific errors — every line was reviewed and understood before being committed.

## Roadmap

- [ ] Refactor `GUI.py` into modular, OOP-based components
- [ ] Add candlestick chart visualization
- [ ] Improve GUI style and overall visual design
- [ ] Package the app as a standalone executable (.exe)
- [ ] Create a setup/installer to remove the need for manual `pip install -r requirements.txt`, making the app easier to access and use for any user
