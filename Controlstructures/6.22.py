###
# Prints numbers from 1 to 30; THREE for multiples of 3,
# FIVE for multiples of 5, BINGO for multiples of both
#
for i in range(1, 31):  # 31, bo górna granica range() nie wchodzi do zakresu, a 30 ma się wypisać
    if i % 3 == 0 and i % 5 == 0:  # ten warunek MUSI być pierwszy: liczba podzielna przez 3 i 5 (np. 15) spełnia też warunki z kolejnych gałęzi, a elif wykona tylko pierwszą pasującą
        print('BINGO', end=' ')  # end=' ' zamienia domyślny koniec linii na spację, żeby wszystko było w jednym wierszu jak w przykładzie
    elif i % 3 == 0:
        print('THREE', end=' ')
    elif i % 5 == 0:
        print('FIVE', end=' ')
    else:
        print(i, end=' ')

print()  # kończy wiersz, żeby kolejny tekst w terminalu nie dopisał się do tej samej linii