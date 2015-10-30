import bottlenose

access_key = "AKIAICAETJ4OV7TWQKKQ"
secret_key = "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"
associate_id = "funtelligent-20"

amazon = bottlenose.Amazon(access_key, secret_key, associate_id)


def upc_category_lookup(upc):
    """
    Looks up the given UPC in the Amazon database and returns the category hierarchy of the item
    :param upc: 12 digit zero padded upc with checksum digit added
    :return: response: Query response provided by Amazon
    """
    response = amazon.ItemLookup(ItemId=upc, IdType="UPC", SearchIndex="All", ResponseGroup="BrowseNodes")
    return response

if __name__ == "__main__":
    upc = "021000018604"
    response = upc_category_lookup(upc)
    print(response)
