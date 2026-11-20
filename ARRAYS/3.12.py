###
# Prints all unique elements in an array
# (elements that appear exactly once)
#
arr = [2, 3, 2, 5, 8, 1, 9, 8]  # typ: list zawierająca 8 elementów typu int

print('Array:', end=' ')  # print() to funkcja wbudowana; end=' ' to parametr nazwany, który zamiast nowej linii wypisuje spację, więc liczby pojawią się w tym samym wierszu
for value in arr:  # pętla for bierze po kolei każdy element listy; value w każdym obrocie jest typu int
    print(value, end=' ')
print()  # pusty print() kończy wiersz

print('Unique elements:', end=' ')
for value in arr:
    if arr.count(value) == 1:  # count() to metoda listy; zwraca, ile razy wartość występuje w całej liście (int); jeśli dokładnie raz, to element jest unikalny
        print(value, end=' ')
print()