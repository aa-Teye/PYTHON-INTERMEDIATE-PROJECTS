import requests

def get_exchange_rate(base_currency, target_currency):
    # Using a free, no-key-required API for teaching purposes
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            rate = data['rates'][target_currency]
            return rate
        else:
            print("Error: Could not fetch data.")
            return None
    except Exception as e:
        print(f"Connection Error: {e}")
        return None

def main():
    print("--- Project 21: Live FX Tracker ---")
    
    base = input("Enter base currency (e.g., USD): ").upper()
    target = input("Enter target currency (e.g., GHS): ").upper()
    amount = float(input(f"Enter amount in {base}: "))

    rate = get_exchange_rate(base, target)

    if rate:
        converted = amount * rate
        print(f"\nLive Rate: 1 {base} = {rate:.2f} {target}")
        print(f"{amount} {base} is equal to {converted:.2f} {target}")
    else:
        print("Invalid currency code or network issue.")

if __name__ == "__main__":
    main()