stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320,
    "AMZN": 170
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

n = int(input("\nHow many different stocks do you own? "))

for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"Investment in {stock_name}: ${investment}")

    else:
        print("Stock not found!")

print(f"Total Investment Value = ${total_investment}")

# Optional: Save result to a text file
choice = input("\nDo you want to save the result? (yes/no): ").lower()

if choice == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Tracker\n")
        file.write(f"Total Investment Value = ${total_investment}")

    print("Result saved successfully in 'portfolio.txt'")
else:
    print("Result not saved.")