###
# Prints the first twenty terms of the Fibonacci sequence
#
a = 0  # pierwszy wyraz ciągu
b = 1  # drugi wyraz ciągu

for i in range(20):  # 20 obrotów, bo mamy wypisać dwadzieścia wyrazów; w każdym obrocie wypisuję jeden wyraz
    print(a, end=' ')  # wypisuję zawsze a, czyli bieżący wyraz; end=' ' trzyma wszystko w jednym wierszu
    a, b = b, a + b  # przesunięcie ciągu o jeden krok: nowe a to stare b, a nowe b to suma starych a i b; zapis w jednej linii liczy obie prawe strony ZANIM cokolwiek przypisze, więc nie trzeba zmiennej pomocniczej

print()  # kończy wiersz