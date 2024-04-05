import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_price(url):
    """
    Crawls the given URL, extracts the price from the HTML content, and returns it.

    Args:
        url (str): The URL to crawl.

    Returns:
        str: The price of the property.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('p', class_='text-blue-900 text-base font-bold text-right').text 
    return price

def get_postal(url):
    """
    Crawls the given URL, extracts the postal code from the HTML content, and returns it.

    Args:
        url (str): The URL to crawl.

    Returns:
        str: The postal code of the property.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    postal = soup.find('div', class_='mt-1 text-xs md:text-sm text-gray-600').text
    return postal


def create_data_frame(filename):
    """
    Reads the addresses from the given file and creates a pandas DataFrame.

    Args:
        filename (str): The name of the file containing the addresses.

    Returns:
        pandas.DataFrame: A DataFrame containing the addresses, prices, and postal codes.
    """
    with open(filename, 'r') as file:
        addresses = file.readlines()
    
    df = (pd.DataFrame(addresses, columns=['Address'])
          .drop_duplicates()
          .reset_index(drop=True))

    price_lst = [get_price(address) for address in df['Address']]
    postal_lst = [get_postal(address) for address in df['Address']]
    
    df['Price'] = price_lst
    df['Postal'] = postal_lst
    
    return df

# Example usage
if __name__ == '__main__':
    #filename = 'addresses.txt'  # Assuming you have a file containing addresses
    #df = create_data_frame(filename)
    url="https://www.boligsiden.dk/adresse/baeltet-4-9800-hjoerring-08600462___4_______?udbud=ac9e19d2-0b71-4b11-b808-2f997f0e4b95"
    postal=get_postal(url)
    print(postal)
