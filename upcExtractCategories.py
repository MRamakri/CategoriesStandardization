from bs4 import BeautifulSoup

from amazonAPI import upc_category_lookup
from convertToUPCA import pad_zeroes, add_check_digit

upc = "3120001605"


def valid_api_response(api_response):
    global soup
    soup = BeautifulSoup(api_response, "html.parser")
    fail_message = soup.find('errors')
    if fail_message is None:
        print("Found!")
        print(response)
        print(type(soup))
        return 1
        # print(soup.prettify())
    else:
        print("Failed!")
        return 0


def extract_category_hierarchy():
    first_item = soup.find('item')
    print(first_item.prettify())
    categories = first_item.findAll('name')
    for category in categories:
        print(category.text)


padded_upc = pad_zeroes(upc)
end_padded_upc = add_check_digit(padded_upc)
print(end_padded_upc)
response = upc_category_lookup(end_padded_upc)
if valid_api_response(response):
    extract_category_hierarchy()
