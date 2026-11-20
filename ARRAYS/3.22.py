###
# Prints a few randomly selected array elements
#
import random  # moduł random trzeba zaimportować na początku, inaczej random.randint() zgłosi błąd NameError

def rand_elem(array):  # funkcja własna; parametr to list, zwraca jeden losowy element (jego typ zależy od zawartości listy)
    index = random.randint(0, len(array) - 1)  # randint(a, b) losuje liczbę całkowitą z OBU końcami włącznie, więc górną granicą musi być ostatni indeks, czyli długość minus 1; gdyby było len(array), mógłby wypaść indeks spoza listy i program zgłosiłby IndexError
    return array[index]

fruits = ["apple", "banana", "cherry", "orange", "kiwi"]  # typ: list zawierająca 5 elementów typu str

print('Array:', fruits)  # print() to funkcja wbudowana
for i in range(5):  # range() to funkcja wbudowana; 5 obrotów, więc 5 losowań
    print('Random element:', rand_elem(fruits))  # ten sam element może wypaść kilka razy, bo losowanie jest za każdym razem niezależne