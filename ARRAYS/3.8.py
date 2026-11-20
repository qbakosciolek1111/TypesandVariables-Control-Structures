###
# Prints array values graphically using asterisks
#
def star(n):  # funkcja własna; parametr n to int (liczba gwiazdek), zwraca str
    return '*' * n  # mnożenie napisu przez liczbę powtarza go n razy, np. '*' * 3 daje '***'; dla n równego 0 wynik to pusty napis

arr = [2, 6, 4, 9, 7]  # typ: list zawierająca 5 elementów typu int

for value in arr:  # pętla for bierze po kolei każdy element listy; value w każdym obrocie jest typu int
    print(f'{value}: {star(value)}')  # print() to funkcja wbudowana; f-string wstawia int (value) i str (zwrócony przez star) do jednego napisu