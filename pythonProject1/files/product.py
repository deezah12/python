import json
import pprint
from decimal import Decimal
import pickle
import yaml

products = {'p1': [
    {'name': 'Soap', 'Quantity': 3, 'price': '23.50', 'is_expired': False},
    {'name': 'Tissue', 'Quantity': 6, 'price': '20.00', 'is_expired': False},
    {'name': 'Durex', 'Quantity': 2, 'price': '123.99', 'is_expired': False},
    {'name': 'Neck choke', 'Quantity': 1, 'price':'239.99', 'is_expired': True}
]}

# with open('pickled_object.txt', mode='wb') as file:
#     pickle.dump(products, file)

with open('pickled_object.txt', mode='rb')as file:
    x = pickle.load(file)
    pprint.pprint(x, indent=4)

with open('json_object.json', mode='w')as file:
    json.dump(products, file, indent=4)


with open('yaml_object.yaml', mode='w')as file:
    yaml.dump(products, file, indent=4, sort_keys=False)



