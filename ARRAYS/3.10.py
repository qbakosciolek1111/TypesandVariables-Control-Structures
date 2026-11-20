###
# Prints the numbers from the first array that do not appear in the second array
#
array1 = [4, 36, 12, 28, 9, 44, 5]  # typ: list zawierająca 7 elementów typu int
array2 = [5, 1, 36]  # typ: list zawierająca 3 elementy typu int

print('Numbers from the first array that are not in the second:', end=' ')  # print() to funkcja wbudowana; end=' ' to parametr nazwany, który zamiast nowej linii wypisuje spację, więc liczby pojawią się w tym samym wierszu
for number in array1:  # pętla for bierze po kolei każdy element pierwszej listy; number w każdym obrocie jest typu int
    if number not in array2:  # operator "not in" sprawdza, czy wartości nie ma w liście, i zwraca bool; Python sam przeszukuje całą drugą listę, więc nie trzeba drugiej pętli
        print(number, end=' ')
print()  # pusty print() kończy wiersz