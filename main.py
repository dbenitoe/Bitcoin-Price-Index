import requests

def fetch_bitcoin_prices():
    try:
        # Fetch the Bitcoin price data
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Check if the request was successful
        data = response.json()

        # Extract the prices in multiple currencies
        prices = {
            "USD": float(data["bpi"]["USD"]["rate_float"]),
            "EUR": float(data["bpi"]["EUR"]["rate_float"]),
            "GBP": float(data["bpi"]["GBP"]["rate_float"])
        }

        return prices

    except requests.RequestException:
        print("An error has occurred while fetching the Bitcoin prices.")
        return None


def get_user_input():
    amount = input("Enter the amount of Bitcoin you have: ")
    currency = input("Enter the currency code (USD, EUR, GBP): ").upper()
    return amount, currency


def calculate_price(prices, amount, currency):
    try:
        if currency not in prices:
            print("Invalid currency code.")
            return

        amount = float(amount)
        coin_price = prices[currency]
        price = amount * coin_price

        # Currency symbol mapping
        currency_symbols = {
            'USD': '$',
            'EUR': '€',
            'GBP': '£'
        }

        currency_symbol = currency_symbols.get(currency, '$')

        print(f"The current price per coin in {currency} is {currency_symbol}{coin_price:,.4f}")
        print(f"The total value of your Bitcoin in {currency} is: {currency_symbol}{price:,.4f}")

    except ValueError:
        print("The input is not a valid number.")
    except TypeError:
        print("Invalid type for coin_price or amount.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    # Fetch the current Bitcoin prices
    prices = fetch_bitcoin_prices()
    if prices is None:
        return

    # Get user input
    amount, currency = get_user_input()

    # Calculate and display the result
    calculate_price(prices, amount, currency)


# Execute the main function
if __name__ == "__main__":
    main()
