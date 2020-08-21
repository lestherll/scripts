import requests
from bs4 import BeautifulSoup

import re



headers = { "User-Agent" : "Mozilla/5.0" }


def get_product_id(amazon_url):
    try:
        found = re.search('product/(.+?)/', amazon_url).group(1)
    except AttributeError:
        found = amazon_url
    return found


def get_price(amazon_url):

    found = get_product_id(amazon_url)

    URL = f'https://uk.camelcamelcamel.com/product/{found}'
    response = requests.get(URL, headers = headers)
    soup = BeautifulSoup(response.content, "html.parser")  
    price_table = soup.find("table" , class_="product_pane")
    price = price_table.find_all("td")[1]

    return price.text

def to_table(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]


amazon_url = input("Enter amazon link: ")
price = get_price(amazon_url)
print(price)