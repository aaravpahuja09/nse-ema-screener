# 📈 NSE 9 EMA Momentum & Crossover Screener

An automated Python tool that fetches real-time market data for top National Stock Exchange (NSE) listed stocks using `yfinance` to detect 9-day Exponential Moving Average (EMA) bullish and bearish momentum crossovers.

## 🌟 Key Features
- **Real-Time Data Retrieval**: Automatically pulls historical price data for 150+ NSE tickers using `yfinance`.
- **Custom Indicator Logic**: Calculates 9-day EMA values directly from historical close prices.
- **Trend Categorization**: Identifies whether a stock is currently in a Bullish or Bearish trend relative to its 9 EMA.
- **Breakout Timing Breakdown**: Groups bullish stocks based on how recently the crossover occurred (1 day ago, 2 days ago, 3 days ago, or >3 days ago) to highlight fresh trading setups.

## 🛠️ How to Run
1. **Clone this repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/nse-ema-screener.git](https://github.com/YOUR_USERNAME/nse-ema-screener.git)
   cd nse-ema-screener
