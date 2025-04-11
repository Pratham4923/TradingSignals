📊 TradingSignals
An interactive trading signals dashboard for Indian NSE stocks using price action breakout strategy combined with Average True Range (ATR). Built with Python, Streamlit, Plotly, and Yahoo Finance.

🚀 Features
📈 Real-time charts with candlestick + ATR overlay

🇮🇳 Supports a wide list of NSE-listed Indian stocks

🔍 Generates BUY / SELL signals using price + ATR logic

🔁 Optional auto-refresh for live dashboards

🎯 Dynamic SL/TP based on ATR multiplier

⚡ Caching & efficient data fetching

🛠️ Tech Stack
UI/Frontend: Streamlit, Plotly

Data: yfinance, pandas

Utilities: logging, datetime, functools

📦 Installation
Clone the repository

bash
Copy

Edit

git clone https://github.com/Pratham4923/TradingSignals.git

cd TradingSignals

Install the dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
streamlit run main.py
📈 Strategy Overview
This tool uses a price breakout strategy confirmed by ATR-based volatility to generate signals:

🔹 BUY Signal
Current Open & Close > Previous High

Entry: Current Open

Stop Loss: Entry − ATR × Multiplier

Take Profit: Entry + ATR × Multiplier × 2

🔸 SELL Signal
Current Open & Close < Previous Low

Entry: Current Open

Stop Loss: Entry + ATR × Multiplier

Take Profit: Entry − ATR × Multiplier × 2

⚙️ App Settings
📊 Select Stock from NSE list

📅 Days of History (1–365 days)

📐 ATR Multiplier (0.5–3.0)

🔄 Enable Auto Refresh with custom interval

🔮 Future Improvements
Backtesting performance metrics

Support for intraday timeframes (e.g. 15m, 1h)

Export signals to CSV/Excel

Alerts via Telegram/Email

📝 License
MIT License.
For educational & personal use. Not financial advice.
