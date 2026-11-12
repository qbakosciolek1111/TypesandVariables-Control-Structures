###
# Shows any amount (natural number) with as few coins as possible,
# using coins of 1, 2 and 5 PLN
#
amount = int(input('Enter the amount in PLN: '))

coins_5 = amount // 5  # dzielenie całkowite mówi, ile razy 5 mieści się w kwocie; zaczynam od największej monety, bo to daje najmniej monet
remaining = amount % 5  # reszta z dzielenia to kwota, której nie pokryły monety 5 zł (zawsze 0-4)
coins_2 = remaining // 2  # z reszty znowu biorę jak najwięcej większych monet, czyli dwuzłotowych
remaining = remaining % 2  # po dwuzłotówkach może zostać tylko 0 albo 1
coins_1 = remaining  # to, co zostało, pokrywam monetami 1 zł (jest ich 0 albo 1)

print(f'The amount of PLN {amount} in coins:')
print(f'5 PLN coins: {coins_5}')
print(f'2 PLN coins: {coins_2}')
print(f'1 PLN coins: {coins_1}')