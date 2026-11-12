###
# Parking meter: calculates the parking fee
# based on the number of hours the car was parked
#
hours = int(input('Enter number of hours parked: '))

if hours < 1:
    fee = 0
    print('Parking fee: 0 PLN')
elif hours <= 2:
    fee = 5
elif hours <= 6:
    fee = 15
else:
    fee = 20
print(f'Parking fee: for {hours} hours is {fee} PLN')
