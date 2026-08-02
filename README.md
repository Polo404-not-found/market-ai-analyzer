# Market AI Analyzer

### A quick note before you start

Hi, dear reader, I'm Polo — welcome, and thanks for checking out this project. I put real time and effort into building it. I'm still fairly new to programming, and even newer to Python, but I got it working. I leaned on AI mainly to learn correct syntax, connect to external libraries correctly, and solve occasional errors along the way — every line was written with a clear understanding of what it does and why. The project comes from my interest in programming and systems combined with my interest in economics and markets, and that's how this tool came to be.

I'd really appreciate any feedback.

Financial market analyzer that combines real historical data with technical indicators (moving averages) and AI-generated analysis (Gemini), now with a basic desktop GUI built with PySide6.

Or the original command-line version:

- Downloads historical data for any asset available on Yahoo Finance (stocks, cryptocurrencies, futures, ETFs)
- Calculates 5-day and 20-day moving averages (MA5, MA20)
- Generates a professional technical report using AI, including trend diagnosis, price behavior analysis, and probabilistic scenarios for the near future
- Provides a basic desktop GUI (PySide6) to enter a ticker and time period and view results without using the terminal

## Project structure

```
Backend/       # Core logic: data fetching, indicators, Gemini integration (OOP)
Frontend/      # Desktop interface built with PySide6 (OOP)
app.py         # Main file
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

```
Get your API Key from Google AI Studio and enter it directly inside the GUI application settings.
```

4. Run the app:

   Desktop GUI:
   ```
   python app.py
   ```

5. (Optional) creating the .exe

```
pyinstaller --noconfirm --onedir --windowed --name="Market AI Analyzer" --icon="Market_AI_Analyze.ico" --add-data "Market_AI_Analyze.ico;." app.py
```

Usage
Enter the API Key in the assigned space.
Enter a ticker (e.g. `BTC-USD`, `AAPL`, `GC=F`) and a time period (e.g. `1mo`, `3mo`, `1y`) in the GUI, or when prompted in the terminal version, and the app will return the data chart along with an AI-generated technical analysis.

## Development notes
- **Fixed minor issues**: Added Threading (QThread) to the app to fix unexpected UI freezes/crashes while waiting for the AI response and resolved candlestick chart rendering bugs.

- **AI as a tool, not a shortcut**: Throughout the project, AI was used to speed up learning correct library syntax and debug specific errors — every line was reviewed and understood before being committed.

- **New .exe file**: Configured app.py with dynamic resource paths to support standalone executable packaging.

- **Official release: Market AI Analyzer 1.0 is ready for publication!**

## Roadmap

- [x] Refactor `GUI.py` into modular, OOP-based components
- [x] Add candlestick chart visualization
- [x] Package the app as a standalone executable (.exe)
- [ ] Create a setup/installer to remove the need for manual `pip install -r requirements.txt`, making the app easier to access and use for any user
- [ ] Improve GUI style and overall visual design
