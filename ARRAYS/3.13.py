###
# Checks whether a number entered from the keyboard is present in an array
#
def occurs(number, array):  # funkcja własna; parametry: int i list, zwraca bool
    for value in array:  # pętla for bierze po kolei każdy element listy; value w każdym obrocie jest typu int
        if value == number:  # porównanie zwraca bool; trafienie oznacza, że liczba jest w tablicy
            return True  # return kończy funkcję od razu, więc dalsze elementy nie są już sprawdzane
    return False  # pętla przeszła przez całą tablicę i nic nie znalazła; return False musi stać POZA pętlą, bo wewnątrz zakończyłby funkcję już po pierwszym elemencie

arr = [15, 38, 7, 23, 14]  # typ: list zawierająca 5 elementów typu int
number = int(input('Number: '))  # input() zwraca str, a int() zamienia go na liczbę, bo porównujemy z liczbami w tablicy

print('Array:', end=' ')  # print() to funkcja wbudowana; end=' ' to parametr nazwany, który zamiast nowej linii wypisuje spację
for value in arr:
    print(value, end=' ')
print()  # pusty print() kończy wiersz

if occurs(number, arr):  # occurs() zwraca bool, więc wystarczy wstawić ją wprost do if
    print(f'Result: number {number} appears in the array')
else:
    print(f'Result: number {number} does not appear in the array')