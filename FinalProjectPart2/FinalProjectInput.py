"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""

# get manufacturer information
mf_data = open("ManufacturerList.csv", 'r').read().strip().split('\n')

price_data = open("PriceList.csv", 'r').read().strip().split('\n')

service_date_data = open("ServiceDatesList.csv", 'r').read().strip().split('\n')

product_dict = dict()

for items in mf_data:
    item_split = items.split(",")
    if items[0] not in product_dict:
        product_dict[item_split[0]] = {
            "product_brand": item_split[1],
            "product_type": item_split[2]
        }

for prices in price_data:
    price_split = prices.split(",")
    product_dict[price_split[0]]["product_price"] = int(price_split[1])

for dates in service_date_data:
    date_data = dates.split(",")
    product_dict[date_data[0]]["service_date"] = date_data[1]


def print_product(id):
    data = product_dict[id]

    for k in data:
        print("[", k, data[k], end=" ]")
    print("\n")


while True:
    query = input("What manufacturer or item type you are looking for(enter q to break ):  ")
    if query.lower().strip() == "q":
        break
    tokens = query.split(" ")

    # match token for items
    items_matched = []
    recommendation = []

    for token in tokens:

        # check for product brands
        for product_data in product_dict:
            if product_dict[product_data]["product_brand"].lower().strip() == token.lower():
                if product_data not in items_matched:
                    items_matched.append(product_data)
                    recommendation.append(product_dict[product_data]["product_type"].lower().strip())

        # check for product type
        for product_data in product_dict:
            if product_dict[product_data]["product_type"].lower().strip() == token.lower():
                if product_data not in items_matched:
                    items_matched.append(product_data)
                    recommendation.append(product_dict[product_data]["product_brand"].lower().strip())

        # check for service date
        for product_data in product_dict:
            if product_dict[product_data]["service_date"].lower().strip() == token.lower():
                if product_data not in items_matched:
                    items_matched.append(product_data)

        # check for product price
        for product_data in product_dict:
            if token.isdigit():
                if product_dict[product_data]["product_price"] > int(token.lower()):
                    if product_data not in items_matched:
                        items_matched.append(product_data)

        # find recommendation
        for items in items_matched:
            print()
            print_product(items)

        print("\nYou may also consider:\n")
        ids = []
        for items in recommendation:

            for product_data in product_dict:
                if product_dict[product_data]["product_brand"].lower().strip() == items:
                    if product_data not in items_matched and product_data not in ids:
                        print_product(product_data)
                        ids.append(product_data)

            # check for product type
            for product_data in product_dict:
                if product_dict[product_data]["product_type"].lower().strip() == items:
                    if product_data not in items_matched and product_data not in ids:
                        print_product(product_data)
                        ids.append(product_data)

        items_matched = []
        recommendation = []
        ids = []