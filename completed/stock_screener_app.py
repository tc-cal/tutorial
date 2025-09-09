
import yfinance as yf
import pandas as pd
import ta

# 1. List of stocks to check
tickers = ["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN"]

# 2. Empty list to store results
results = []

# 3. Loop through each stock
for ticker in tickers:
    stock = yf.download(ticker, period="6mo")  # 6 months of data

    # 4. Add RSI indicator
    # Convert Close to Series if DataFrame
    close_series = stock["Close"].squeeze()  # ensures 1D Series
    # Add RSI
    stock["RSI"] = ta.momentum.RSIIndicator(close_series).rsi()

    latest = stock.iloc[-1]

    price = latest["Close"].item()  # ensure float
    volume = latest["Volume"].item()  # ensure int
    rsi = latest["RSI"].item()  # ensure float

    # 5. Example filter: Price > 100, Volume > 10M, RSI < 30 (oversold)
    if (
            pd.notna(rsi)
            and price > 100
            and volume > 10_000_000
            and rsi < 100
    ):
        results.append({
            "Ticker": ticker,
            "Price": round(price, 2),
            "Volume": int(volume),
            "RSI": round(rsi, 2)
        })

# 6. Convert to DataFrame for easy viewing
df = pd.DataFrame(results)

# 7. Save results to Excel
#df.to_excel("stock_screener_results.xlsx", index=False)

#print("Screening complete! Results saved to stock_screener_results.xlsx")
print(df.head())