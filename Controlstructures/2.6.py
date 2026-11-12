###
# Checks what number was entered from the keyboard
# and prints whether it is positive, negative or zero
#
number = int(input('Enter number: '))
if number > 0:
    print(f'{number} is positive') 
elif number < 0:
    print(f'{number} is negative')
else:
    print(f'{number} is zero')