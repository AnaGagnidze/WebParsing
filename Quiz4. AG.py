import requests
from bs4 import BeautifulSoup
from time import sleep
import csv

# I create a new csv file so that i can save parsed information in it later
file = open("lorealProducts.csv", 'w', newline='\n')
# I user csv module, because I wanted saved information to be cleaner.
csv_file = csv.writer(file)
csv_file.writerow(["Brand", "Name", "Description"])

# This index grows by one every time a page is parsed
index = 1
# In this example I parsed 5 pages of Loreal paris usa web page
while index <= 5:
    url = 'https://www.lorealparisusa.com/products/skin-care/shop-all-products.aspx?size=21&page=' + str(index)
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    all_products = soup.find('div', {'id': 'all-moisturizers'})
    products = all_products.findAll('div', {'class': 'product-container'})

    for each in products:
        brand = each.h4.text
        name = each.h3.text
        description = each.p.text
        csv_file.writerow([brand, name, description])
        print(brand, name, description)

    index += 1
    # I use sleep function from time module so that pages can be parsed in logical time spans
    sleep(15)

