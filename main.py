import requests


# Fetch Bitcoin price from API
def fetch_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        return float(data["bpi"]["USD"]["rate_float"])
    except requests.RequestException:
        print("An error has occurred while fetching the Bitcoin price.")
        return None


# Get user input
def get_user_input():
    user_input = input("Enter the amount of Bitcoin you have: ")
    return user_input


# Calculate and display the equivalent USD price
def calculate_price(coin_price, amount):
    try:
        amount = float(amount)
        price = amount * coin_price
        print(f"The current price per coin is ${coin_price:,.4f}")
        print(f"The total value of your Bitcoin in USD is: ${price:,.4f}")
    except ValueError:
        print("The input is not a valid number.")


# Main function
def main():
    # Fetch the current Bitcoin price
    coin_price = fetch_bitcoin_price()
    if coin_price is None:
        return

    # Get user input
    user_input = get_user_input()

    # Calculate and display the result
    calculate_price(coin_price, user_input)


# Execute the main function
if __name__ == "__main__":
    main()