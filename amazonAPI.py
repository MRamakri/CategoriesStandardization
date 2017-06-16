import bottlenose
from bs4 import BeautifulSoup
from settings_local import access_key, secret_key, associate_id

amazon = bottlenose.Amazon(access_key, secret_key, associate_id)

def upc_category_lookup(upc):
    """
    Looks up the given UPC in the Amazon database and returns the category hierarchy of the item
    :param upc: 12 digit zero padded upc with checksum digit added
    :return: response: Query response provided by Amazon
    """
    response = amazon.ItemLookup(ItemId=upc, IdType="UPC", SearchIndex="All", ResponseGroup="BrowseNodes")
    return response

def upc_attributes_lookup(upc):
    response = amazon.ItemLookup(ItemId=upc, IdType="UPC", SearchIndex="All", ResponseGroup="ItemAttributes")
    #print(response)
    return response

def asin_description_lookup(asin):
    """
    Looks up the given ASIN in the Amazon database and returns the descripiton of the item
    :param asin: ASIN of the item
    :return: response: Query response provided by Amazon
    """
    response = amazon.ItemLookup(ItemId=asin, IdType="ASIN", ResponseGroup="ItemAttributes")
    soup = BeautifulSoup(response, "html.parser")
    #print(soup)
    description = soup.find('title').text
    return description

if __name__ == "__main__":
    upc = "1862770321"
    asin = "B00CHU3XW8"
    response = upc_category_lookup(upc)
    response2 = asin_description_lookup(asin)
    response3 = upc_attributes_lookup(upc)
    print(response)
    print(response2)
    print(response3)
