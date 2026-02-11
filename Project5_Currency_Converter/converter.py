import requests

def get_exchange_rate(base_currency, target_currency):
    # A free, no-key-required API for practice
    url = f"https://open.er-api.com/v6/latest/{base_currency.upper()}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["result"] == "success":
            rates = data["rates"]
            return rates.get(target_currency.upper())
        else:
            return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    print("--- Currency Converter (Live Rates) ---")
    base = input("Enter base currency (e.g., USD, GHS, EUR): ")
    target = input("Enter target currency: ")
    amount = float(input(f"Enter amount in {base}: "))

    rate = get_exchange_rate(base, target)

    if rate:
        converted = amount * rate
        print(f"\nResult: {amount} {base} = {converted:.2f} {target}")
        print(f"Current Rate: 1 {base} = {rate:.4f} {target}")
    else:
        print("Could not find that currency or the service is down.")

if __name__ == "__main__":
    main()