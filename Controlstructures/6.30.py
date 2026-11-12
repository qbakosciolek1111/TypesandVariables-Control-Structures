###
# A program thtt prints a lottery coupon (numbers from 1 to 49)
###
for row in range(1,8):
    for col in range(7):
        print(f'{row+col*7:2}', end='')
    print()
    