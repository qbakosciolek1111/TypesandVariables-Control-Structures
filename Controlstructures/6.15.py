###
# Checks whether the EAN-13 number consists of exactly 13 digits
# and whether the product was manufactured in Poland (starts with 590)
#
ean = input('Enter EAN-13 article number: ')

if len(ean) == 13 and ean.isdigit():
    print('Article number is correct')  
    if ean.startswith('590'):  
        print('Article manufactured in Poland')  
else:
    print('Article number is incorrect')