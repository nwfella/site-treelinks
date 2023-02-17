import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

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
        parsed_url = urlparse(href)
        if parsed_url.scheme and parsed_url.netloc:
            full_url = href
        else:
            full_url = urljoin(url, href)
        links.append(full_url)

# Print Em and thats a wrap!! ;)
print("=" * 50)
print("Valid, full URLs found on the page:")
print("-" * 50)
for link in links:
    print(link)
print("=" * 50)
