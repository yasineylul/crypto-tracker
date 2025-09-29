import requests

API_URL = "https://api.coingecko.com/api/v3/simple/price"
CRYPTOCURRENCIES = ["bitcoin", "ethereum", "solana"]
CURRENCY = "usd"

def get_prices():
    try:
        response = requests.get(API_URL, params={
            "ids": ",".join(CRYPTOCURRENCIES),
            "vs_currencies": CURRENCY
        })
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None

def main():
    print("📊 Kripto Fiyat Takip")
    prices = get_prices()
    if prices:
        for coin in CRYPTOCURRENCIES:
            price = prices[coin][CURRENCY]
            print(f"{coin.capitalize()}: {price} {CURRENCY.upper()}")

if __name__ == "__main__":
    main()
