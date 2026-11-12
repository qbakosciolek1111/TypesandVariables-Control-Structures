###
# Converts a decimal number into a binary number
# by repeatedly dividing by 2 and noting the remainders
#
number = int(input('Enter decimal number: '))
quotient = number  # kopia liczby, bo w pętli będę ją zmniejszać, a oryginał jest potrzebny do wypisania na końcu
binary = ''  # wynik budowany jako tekst, żeby łatwo dopisywać cyfry

if quotient == 0:  # dla zera pętla poniżej w ogóle by się nie wykonała i wynik byłby pusty, więc obsługuję ten przypadek osobno
    binary = '0'

while quotient > 0:  # dzielę, dopóki iloraz nie spadnie do 0 (krok 4 z polecenia)
    remainder = quotient % 2  # reszta z dzielenia przez 2 to kolejna cyfra binarna (0 albo 1)
    binary = str(remainder) + binary  # dopisuję cyfrę NA POCZĄTKU, bo reszty powstają od końca; to samo robi krok 5 z polecenia ("od dołu do góry")
    quotient = quotient // 2  # // to dzielenie całkowite, które odrzuca część ułamkową (np. 7 // 2 = 3)

print(f'{number}(10) = {binary}(2)')