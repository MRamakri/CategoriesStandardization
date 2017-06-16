import json
import re
from bs4 import BeautifulSoup
from amazonAPI import upc_attributes_lookup, asin_description_lookup
from convertToUPCA import pad_zeroes, add_check_digit

upcs = ["1862751003", "1862738689", "7834776530", "7870080160"]

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


def extract_attributes():
    global department
    features_to_find = ['Non GMO',
                        'Organic',
                        'Kosher',
                        'Low Sodium',
                        'Antioxidants',
                        'Whole Grain']
    feature_list = set([])
    items = soup.findAll('item')
    for item in items:
        print(item.find('title').text)
        features = item.findAll('feature')
        if features != []:
            for feature in features:
                for key_feature in features_to_find:
                    if bool(re.search(key_feature, feature.text, re.IGNORECASE)):
                        feature_list.add(key_feature)
    print(feature_list)
    print('====================================')

for upc in upcs:
    upc_clean = upc
    if len(upc) < 12:
        upc_clean = add_check_digit(pad_zeroes(upc))
    print(upc_clean)
    response = upc_attributes_lookup(upc_clean)
    if valid_api_response(response):
        extract_attributes()
