# scrape_csv.py
# ST2195 Assignment 2 – Python part
# This script scrapes the CSV example from Wikipedia and saves it locally

from bs4 import BeautifulSoup
import requests
import pandas as pd

# 1. Define target URL
url = "https://en.wikipedia.org/wiki/Delimiter-separated_values"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
}

# 2. Send HTTP request to fetch the page
response = requests.get(url,headers=headers)
response.raise_for_status()  # Ensures it stops if connection fails
# print("raw response:", response.text[:500])  # Print first 500 characters of raw response
# 3. Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
# 4. Find all tables on the page
tables = soup.find_all("table")
print(f"Found {len(tables)} tables on the page.")
# 5. Convert the first table into a pandas DataFrame
try:
    #convert the first table to a DataFrame
    df = pd.read_html(str(tables[0]))[0]
    print(df.head())  # Print first few rows of the DataFrame
    
except IndexError as e:
    print("No tables found on the page.")

# 6. Save the table as CSV
df.to_csv("csv_example_py.csv", index=False)

# 7. Verify by reading it back
verified = pd.read_csv("csv_example_py.csv")
print(verified.head())
