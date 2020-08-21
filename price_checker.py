import requests
from bs4 import BeautifulSoup

import re



headers = { "User-Agent" : "Mozilla/5.0" }


def get_product_id(amazon_url):
    #Returns the product id from the amazon URL
    try:
        product_id = re.search('product/(.+?)/', amazon_url).group(1)
    except AttributeError:
        product_id = amazon_url  #Returns amazon URL if the inp is already the product ID
    return product_id


def get_price(amazon_url):
    """This function takes an amazon product url and returns its current price"""

    #product id is extracted form amazon url
    product_id = get_product_id(amazon_url)

    #product id is added to the camel site
    URL = f'https://uk.camelcamelcamel.com/product/{product_id}'
    
    #request for the webpage content
    response = requests.get(URL, headers = headers)
    #parse webpage content
    soup = BeautifulSoup(response.content, "html.parser")  
    #find amazon price table
    price_table = soup.find("table" , class_="product_pane")
    #return current price
    price = price_table.find_all("td")[1]

    return price.text


amazon_url = input("Enter amazon link: ")   #input amazon url
price = get_price(amazon_url)   #get its current price

print(price)    