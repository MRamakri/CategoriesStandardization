import json
from bs4 import BeautifulSoup
from amazonAPI import upc_category_lookup, asin_description_lookup
from convertToUPCA import pad_zeroes, add_check_digit

upc = "3800032410"


# TODO: Read UPCs from file
# TODO: Write Categories into file
# TODO: Read UPCs from DPN using PyHive
# TODO: Write Categories into HDFS using PyHive

def valid_api_response(api_response):
    global soup
    soup = BeautifulSoup(api_response, "html.parser")
    fail_message = soup.find('errors')
    if fail_message is None:
        print("Found!")
        #print(response)
        return 1
        # print(soup.prettify())
    else:
        print("Failed!")
        return 0


def extract_category_hierarchy():
    global department
    category_list = []
    items = soup.findAll('item')
    for item in items:
        description = asin_description_lookup(item.find('asin').text)
        nodes = item.findAll('browsenodes')
        for node in nodes:
            category_list = []
            categories = node.findAll('name')
            #print(categories)
            for index, category in enumerate(categories):
                if category.text == 'Categories':
                    department = categories[index + 1].text
                    while index > 0:
                        category_list.append(categories[index - 1].text)
                        index -= 1
                    break
            upc_category = {
                'UPC': upc,
                'Description': description,
                'Source': 'Amazon',
                'Department': department,
                'Category': category_list
            }
            upc_category_json  = json.dumps(upc_category)
            print(upc_category_json)
            print('------------')


padded_upc = pad_zeroes(upc)
end_padded_upc = add_check_digit(padded_upc)
print(end_padded_upc)
response = upc_category_lookup(end_padded_upc)
if valid_api_response(response):
    extract_category_hierarchy()
