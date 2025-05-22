import requests
import pandas as pd
import os

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "coins.csv")
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False,
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    df = pd.DataFrame(data)[
        [
            "id",
            "symbol",
            "name",
            "current_price",
            "market_cap",
            "price_change_percentage_24h",
        ]
    ]
    df.to_csv(output_path, index=False)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
