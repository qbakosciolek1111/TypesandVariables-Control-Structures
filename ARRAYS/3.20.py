###
# Separates even and odd numbers of an array: all even numbers first, then odd ones
#
arr = [7, 9, 2, 4, 5, 6]  # typ: list zawierająca 6 elementów typu int
print('arr =', arr)  # print() to funkcja wbudowana

evens = []  # typ: pusta list; trafią do niej liczby parzyste
odds = []  # typ: pusta list; trafią do niej liczby nieparzyste
for number in arr:  # pętla for bierze po kolei każdy element listy; number w każdym obrocie jest typu int
    if number % 2 == 0:  # % zwraca resztę z dzielenia, a reszta 0 przy dzieleniu przez 2 oznacza liczbę parzystą; porównanie zwraca bool
        evens.append(number)  # append() to metoda listy; dopisuje element na koniec, więc zachowana jest kolejność z oryginału
    else:
        odds.append(number)

arr = evens + odds  # operator + dla dwóch list skleja je w nową listę (list), więc parzyste stoją przed nieparzystymi
print('arr =', arr)