import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_addresses(url):
    """
    Scrapes the addresses from the given URL.

    Args:
        url (str): The URL to scrape.

    Returns:
        list: A list of addresses.
    """
    addresses = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for address in soup.select('div.sc-eEieub > a'):
            addresses.append(address.get_text(strip=True))
    return addresses

def save_to_excel(addresses, filename):
    """
    Saves the addresses to an Excel file.

    Args:
        addresses (list): A list of addresses.
        filename (str): The name of the Excel file.

    Returns:
        None
    """
    df = pd.DataFrame({'Address': addresses})
    df.to_excel(filename, index=False)
    print(f"Addresses saved to {filename}")

if __name__ == "__main__":
    url = 'https://www.boligsiden.dk/tilsalg?page=1'
    addresses = scrape_addresses(url)
    save_to_excel(addresses, 'addresses.xlsx')
