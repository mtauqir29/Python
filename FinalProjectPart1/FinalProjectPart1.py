"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""
import pandas as pd
import operator
import datetime

#open the manufacturers list
mf_headers = ['item_id', "mf_name", "item_type", "damaged"]
mf_list = pd.read_csv("ManufacturerList.csv", names = mf_headers)

# open the PriceList
price_list_headers = ['item_id', 'price']
price_list = pd.read_csv("PriceList.csv", names = price_list_headers)
price_list_array = list(price_list['item_id'])

#load service data info
service_date_headers = ['item_id', 'date']
service_date = pd.read_csv("ServiceDatesList.csv", names = service_date_headers)
service_date_array = list(service_date['item_id'])


# prepare the full inventory data
full_inventory = mf_list.to_numpy().tolist()

for item in full_inventory:
    damaged = item.pop()
    item_id = item[0]
    price = price_list['price'][price_list_array.index(item_id)]
    date = service_date['date'][service_date_array.index(item_id)]

    item.append(price) #add price to inventory
    item.append(date) #add service date ''
    item.append(damaged)

full_inventory = sorted(full_inventory, key=operator.itemgetter(1)) #sort alphabetically by manufacturer
full_inventory_columns = ['item_id', 'mf_name', 'item_type', 'price', 'service_date', 'damaged']
full_inventory = pd.DataFrame(full_inventory, columns = full_inventory_columns) #convert the inventory to pandas dataframe
full_inventory.to_csv("FullInventory.csv", index = False)



item_types = list(set(full_inventory['item_type'])) #get all unique product types
full_inventory = full_inventory.to_numpy().tolist()
for type in item_types:
    type_items = []
    for item in full_inventory:
        if item[2] == type:
            type_items.append(item)
    sorted(type_items, key=operator.itemgetter(0)) #sort by item id
    df = pd.DataFrame(type_items, columns=full_inventory_columns)
    df.to_csv(f"{type}_items.csv", index = False)


today = datetime.datetime.today()

past_service = []
for item in full_inventory:
    service_date = item[4]
    service_date = datetime.datetime.strptime(service_date,'%m/%d/%Y')
    if service_date < today:
        past_service.append(item)

sorted(past_service, key=operator.itemgetter(4)) #sort by item id
df = pd.DataFrame(past_service, columns=full_inventory_columns)
df.to_csv(f"PastServiceDateInventory.csv", index = False)



damaged_items = []
for item in full_inventory:
    if item[5] == "damaged":
        damaged_items.append(item)
sorted(damaged_items, key=operator.itemgetter(3), reverse=True) #sort by item id
df = pd.DataFrame(damaged_items, columns=full_inventory_columns)
df.to_csv(f"DamagedInventory.csv", index = False)

