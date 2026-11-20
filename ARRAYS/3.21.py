###
# Checks whether the first array is a subset of the second one
# (whether all elements of the first array appear in the second array)
#
def is_subset(first, second):  # funkcja własna; parametry to dwie list, zwraca bool
    for value in first:  # pętla for bierze po kolei każdy element pierwszej listy; value jest typu int
        if value not in second:  # operator "not in" sprawdza, czy wartości nie ma w liście (bool); wystarczy jeden brakujący element, żeby to nie był podzbiór
            return False  # return kończy funkcję od razu, więc dalsze elementy nie są już sprawdzane
    return True  # pętla przeszła przez wszystkie elementy i każdy znalazł się w drugiej liście; return True musi stać POZA pętlą, bo wewnątrz zakończyłby funkcję po pierwszym elemencie

pairs = [
    ([3, 7, 5], [1, 3, 5, 7, 9]),
    ([3, 8], [1, 3, 5, 7, 9]),
]  # typ: list zawierająca 2 krotki (tuple), a każda krotka to para list z liczbami typu int

for first, second in pairs:  # w każdym obrocie krotka rozpakowuje się na dwie zmienne typu list
    print('First array:', first)  # print() to funkcja wbudowana
    print('Second array:', second)
    if is_subset(first, second):  # is_subset() zwraca bool, więc wystarczy wstawić ją wprost do if
        print('Result: the first array is a subset of the second')
    else:
        print('Result: the first array is not a subset of the second')
    print()  # pusty print() wypisuje pustą linię między parami