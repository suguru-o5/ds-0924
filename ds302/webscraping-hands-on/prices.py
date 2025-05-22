import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Part 1: Web Scraping Smartphone Prices
base_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(base_dir, "prices.csv")
url = "https://books.toscrape.com/"
data = []
try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    products = soup.find_all("article", class_="product_pod")
    for product in products:
        name = product.h3.a["title"]
        price = (
            product.find("div", class_="product_price")
            .find("p", class_="price_color")
            .text.strip()
        )
        data.append([name, price])
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
df_prices = pd.DataFrame(data, columns=["Title", "Price"])
print(df_prices.head())
df_prices.to_csv(output_path, index=False)
