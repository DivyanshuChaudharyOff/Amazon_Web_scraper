import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}


url = "https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX1W1XY/ref=sr_1_1_sspa?s=electronics&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"  # Replace with your target product URL
response = requests.get(url, headers=headers)


soup = BeautifulSoup(response.content, "html.parser")


# Extract product title
try:
    title = soup.find("span", {"id": "productTitle"}).get_text(strip=True)
except AttributeError:
    title = None

# Extract product price
try:
    price = soup.find("span", {"class": "a-price"}).find("span").get_text(strip=True)
except AttributeError:
    price = None

# Extract product rating
try:
    rating = soup.find("i", {"class": "a-icon-star"}).get_text(strip=True)
except AttributeError:
    rating = None

# Compile data into a dictionary
product_data = {"Title": title, "Price": price, "Rating": rating}


df = pd.DataFrame([product_data])
df.to_csv("data/amazon_product_data.csv", index=False)
