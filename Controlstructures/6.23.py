###
# Creates a multiplication table in the range 1 to 10
# for any number entered by the user
#
number = int(input('Enter number: '))

for i in range(1, 11):  # 11, bo górna granica range() nie wchodzi do zakresu, a ostatni mnożnik ma być 10
    print(f'{number} x {i} = {number * i}')  # w f-stringu można wstawić wprost wyrażenie, więc iloczyn liczę w środku nawiasów klamrowych, bez osobnej zmiennej