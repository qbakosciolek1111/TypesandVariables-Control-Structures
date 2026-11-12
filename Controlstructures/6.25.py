###
# Prints a pattern of digits: the digit n is repeated n times in row n
#
for i in range(1, 10):  # 10, bo górna granica range() nie wchodzi do zakresu, a ostatni wiersz ma zawierać dziewiątki
    print(str(i) * i)  # str(i) zamienia liczbę na napis, bo mnożenie napisu przez liczbę powtarza go ('3' * 3 daje '333'); gdyby zostało samo i * i, Python policzyłby iloczyn (9 zamiast '333')