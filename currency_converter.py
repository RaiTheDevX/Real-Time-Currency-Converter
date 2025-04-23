import requests

# Function to get the exchange rate from the API
def get_exchange_rate(base_currency, target_currency):
    api_key = 'your_api_key_here'  # Replace with your actual API key
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Check if the API response is successful
        if data['result'] != 'success':
            print(f"Error: {data['error-type']}")
            return None
        
        # Fetch the exchange rate from the response
        rate = data['conversion_rates'].get(target_currency)
        if rate is None:
            print(f"Error: Currency {target_currency} not found.")
            return None
        return rate

    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return None

# Function to perform the currency conversion
def currency_converter():
    print("Welcome to the Currency Converter!")

    # Get user inputs
    base_currency = input("Enter the base currency (e.g., USD, EUR): ").upper()
    target_currency = input("Enter the target currency (e.g., USD, EUR): ").upper()
    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Invalid amount entered. Please enter a valid number.")
        return
    
    # Fetch the exchange rate
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        # Perform the conversion
        converted_amount = amount * rate
        print(f"\n{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    else:
        print("Unable to perform conversion due to errors.")

# Main function to run the program
if __name__ == "__main__":
    currency_converter()
