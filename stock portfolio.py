# Stock Portfolio Tracker — CodeAlpha Internship Task

# Hardcoded stock price dictionary
STOCK_PRICES = {
    "AAPL": 180, "TSLA": 250, "GOOGL": 175, "AMZN": 190,
    "MSFT": 415, "NVDA": 875, "META": 485, "NFLX": 640,
    "AMD":  160, "INTC":  28,
}

portfolio = {}

print("=== Stock Portfolio Tracker ===")
print("Available:", ", ".join(STOCK_PRICES.keys()))
print("Type 'done' when finished.\n")

while True:
    ticker = input("Enter stock ticker (or 'done'): ").upper().strip()
    if ticker == "DONE":
        break
    if ticker not in STOCK_PRICES:
        print(f"  '{ticker}' not found. Try again.")
        continue
    try:
        qty = int(input(f"  Quantity of {ticker}: "))
        portfolio[ticker] = portfolio.get(ticker, 0) + qty
    except ValueError:
        print("  Invalid quantity. Try again.")

# Calculate and display
print("\n--- Portfolio Summary ---")
total = 0
for ticker, qty in portfolio.items():
    value = qty * STOCK_PRICES[ticker]
    total += value
    print(f"  {ticker:6} {qty:4} shares × ${STOCK_PRICES[ticker]:>6} = ${value:>10,.2f}")

print(f"\n  Total Investment Value: ${total:,.2f}")

# Optional: save to CSV
save = input("\nSave to file? (csv/txt/no): ").lower()
if save == "csv":
    with open("portfolio.csv", "w") as f:
        f.write("Ticker,Shares,Price,Value\n")
        for t, q in portfolio.items():
            v = q * STOCK_PRICES[t]
            f.write(f"{t},{q},{STOCK_PRICES[t]},{v:.2f}\n")
        f.write(f"\nTotal,,,{total:.2f}\n")
    print("Saved to portfolio.csv")
elif save == "txt":
    with open("portfolio.txt", "w") as f:
        f.write("=== Stock Portfolio Report ===\n\n")
        for t, q in portfolio.items():
            v = q * STOCK_PRICES[t]
            f.write(f"{t}: {q} shares × ${STOCK_PRICES[t]} = ${v:,.2f}\n")
        f.write(f"\nTotal Investment: ${total:,.2f}\n")
    print("Saved to portfolio.txt")