###
# Calculates the amount to pay: a 25% discount
# is charged for each product purchased over two
#
quantity = int(input('Number of products purchased: '))
price = float(input('Product price: '))

if quantity <= 2:
    amount = quantity * price
else:
    discounted = quantity - 2
    amount = 2 * price + discounted * price * 0.75
    
print(f'Amount to pay: {amount:.2f}') 