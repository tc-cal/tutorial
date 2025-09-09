import yfinance as yf
import pandas as pd

# 1. List of stocks to check
tickers = ["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN"]

# 2. Empty list to store results
results = []

# 3. Loop through each stock
for ticker in tickers:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="5d")  # last 5 days of data
    latest = hist.iloc[-1]  # most recent row

    price = latest['Close']
    volume = latest['Volume']

    # 4. Filter: Example - price > 100 and volume > 10 million
    if price > 100 and volume > 10_000_000:
        results.append({"Ticker": ticker, "Price": price, "Volume": volume})

# 5. Convert to DataFrame for easy viewing
df = pd.DataFrame(results)

# 6. Save results to Excel
df.to_csv("stock_screener_results.csv", index=False)

print("Screening complete! Results saved to stock_screener_results.xlsx")
#print(df.head())
