import json

product = {}

# read product data from keyboard
product['name'] = input('Product name: ')
product['price'] = round(float(input('Price: ')), 2)

paid_answer = input('Paid (yes/no): ').strip().lower()
product['paid'] = paid_answer == 'yes'

# save product data to json file
with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4, ensure_ascii=False)

print('Product data has been written to product.json')