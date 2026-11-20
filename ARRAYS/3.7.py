###
# Finds the longest name in an array
#
names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]  # typ: list zawierająca 5 elementów typu str (imiona)

longest = names[0]  # typ: str; zaczynam od pierwszego imienia jako dotychczas najdłuższego
for name in names:  # pętla for bierze po kolei każdy element listy; name w każdym obrocie jest typu str
    if len(name) > len(longest):  # len() to funkcja wbudowana; dla napisu zwraca liczbę znaków (int); ostre ">" zamiast ">=", więc przy remisie zostaje imię, które było pierwsze
        longest = name

print('Names:', end=' ')  # print() to funkcja wbudowana; end=' ' to parametr nazwany, który zamiast nowej linii wypisuje spację, więc imiona pojawią się w tym samym wierszu
for name in names:
    print(name, end=' ')
print()  # pusty print() kończy wiersz
print('Longest name:', longest)