Here’s the README rewritten in GitHub-friendly code block format:

```markdown
# Amazon Product Data Scraper

A Python script to scrape product details from Amazon and save the data into a CSV file. This tool is ideal for tracking product prices, ratings, and availability over time.

---

## Features

- **Extracts Key Product Details**:
  - Title
  - Price
  - Rating
  - Availability
  - Number of Reviews
  - Timestamp of the scrape

- **Error Handling**: Gracefully manages missing data or connection issues.
- **CSV Storage**: Appends new data to an existing CSV or creates a new one if it doesn’t exist.
- **UTF-8 Encoding**: Supports international characters in product details.

---

## Prerequisites

### Python Libraries
Install the required libraries using pip:

```bash
pip install requests beautifulsoup4 pandas
```

### Other Requirements
- Python 3.6 or higher
- A valid Amazon product URL

---

## Usage

1. **Modify the Target URL**
   Update the `url` variable in the script with the Amazon product URL you want to scrape.

   Example:
   ```python
   url = "https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX1W1XY"
   ```

2. **Run the Script**
   Execute the script using Python:

   ```bash
   python amazon_scraper.py
   ```

3. **View Results**
   The extracted data will be displayed in the console and saved to a CSV file (`data/amazon_product_data.csv`).

---

## Output

The script saves the data in the following CSV format:

| Title                     | Price   | Rating | Availability | Reviews  | Timestamp           |
|---------------------------|---------|--------|--------------|----------|---------------------|
| Apple iPhone 15 (128 GB)  | ₹79,900 | 4.5    | In Stock     | 10,000+ | 2025-01-10 12:30:45 |

---

## File Structure

```
project/
│
├── amazon_scraper.py         # Main Python script
├── data/
│   └── amazon_product_data.csv  # Output CSV file
└── README.md                 # Documentation
```

---

## Error Handling

The script handles the following potential issues:
1. **Missing HTML Elements**: If a product detail (e.g., price, rating) is unavailable, it logs an appropriate message and stores `None` for that field.
2. **Connection Errors**: If the target URL cannot be fetched, the script logs the error and exits gracefully.
3. **File I/O Errors**: Ensures the CSV file is created or appended without overwriting existing data.

---

## Limitations

1. **Dynamic Content**: Some Amazon pages load data dynamically using JavaScript. This script may not capture such data.
2. **Amazon Anti-Scraping Measures**: Amazon may block requests if scraping is detected. Use headers to mimic a browser, and avoid frequent requests.

---

## Future Improvements

1. **Dynamic Price Selector**: Handle changes in Amazon's HTML structure by dynamically identifying price elements.
2. **Proxy Support**: Add support for proxies to avoid IP bans.
3. **Multi-Product Scraping**: Extend functionality to scrape multiple product URLs from a list.

---

## License

This project is licensed under the MIT License.

---

## Author

Developed by Divyanshu Chaudhary. Feel free to reach out for improvements or suggestions!
