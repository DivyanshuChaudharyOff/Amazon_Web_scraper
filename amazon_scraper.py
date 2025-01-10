import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os
import sys
import io

# Force UTF-8 encoding for console output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}

url = "https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX1W1XY/ref=sr_1_1_sspa?s=electronics&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"  # Replace with your target product URL
try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Successfully fetched the URL.")
    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}")
        exit()
except Exception as e:
    print(f"Error fetching the URL: {e}")
    exit()

try:
    soup = BeautifulSoup(response.content, "html.parser")
    print("Successfully parsed the HTML.")
except Exception as e:
    print(f"Error parsing the HTML: {e}")
    exit()

# Extract product title
try:
    title = soup.find("span", {"id": "productTitle"}).get_text(strip=True)
    print(f"Title extracted: {title}")
except AttributeError:
    title = None
    print("Failed to extract title.")

# Extract product price
try:
    price = soup.find("span", {"class": "a-price"}).find("span").get_text(strip=True)
    print(f"Price extracted: {price}")
except AttributeError:
    price = None
    print("Failed to extract price.")

# Extract product rating
try:
    rating = soup.find("i", {"class": "a-icon-star"}).get_text(strip=True)
    print(f"Rating extracted: {rating}")
except AttributeError:
    rating = None
    print("Failed to extract rating.")

# Extract product availability
try:
    availability = soup.find("div", {"id": "availability"}).find("span").get_text(strip=True)
    print(f"Availability extracted: {availability}")
except AttributeError:
    availability = None
    print("Failed to extract availability.")

# Extract product reviews
try:
    reviews = soup.find("span", {"id": "acrCustomerReviewText"}).get_text(strip=True)
    print(f"Reviews extracted: {reviews}")
except AttributeError:
    reviews = None
    print("Failed to extract reviews.")

# Get current date and time
try:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Timestamp generated: {timestamp}")
except Exception as e:
    print(f"Error generating timestamp: {e}")
    exit()

# Compile data into a dictionary
product_data = {
    "Title": title,
    "Price": price,
    "Rating": rating,
    "Availability": availability,
    "Reviews": reviews,
    "Timestamp": timestamp
}

try:
    df = pd.DataFrame([product_data])
    print("DataFrame created successfully.")
except Exception as e:
    print(f"Error creating DataFrame: {e}")
    exit()

# Append to CSV or create a new one
file_path = "data/amazon_product_data.csv"
try:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    if not os.path.exists(file_path):
        df.to_csv(file_path, index=False, encoding='utf-8')
        print(f"Data saved to new file: {file_path}")
    else:
        df.to_csv(file_path, mode='a', header=False, index=False, encoding='utf-8')
        print(f"Data appended to existing file: {file_path}")
except Exception as e:
    print(f"Error saving data to CSV: {e}")
