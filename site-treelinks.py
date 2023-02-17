import requests
from bs4 import BeautifulSoup

# User inputs URL to scrape
url = input("Enter a website URL to scrape: ")

# GET request to user-specified URL
response = requests.get(url)

# Parse page and convert to BeautifulSoup object
soup = BeautifulSoup(response.content, "html.parser")

# Filter out all website links
links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href is not None:
        links.append(href)

# Print Em and thats a wrap!! ;)
print("=" * 50)
print("Links found on the page:")
print("-" * 50)
for link in links:
    print(link)
print("=" * 50)
