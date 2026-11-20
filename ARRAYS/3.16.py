###
# Prints selected values from a nested tuple
#
data = ("Seven", [10, 20, 30], (5, 15, 25))  # typ: tuple (krotka) z trzema elementami różnych typów: str, list i tuple; to zagnieżdżona struktura, czyli kolekcje w kolekcji

print(data[0])  # data[0] to pierwszy element krotki (str); print() to funkcja wbudowana; wypisze Seven
print(data[1][2])  # dwa indeksy odpowiadają dwóm poziomom: data[1] to cała lista [10, 20, 30] (list), a [2] wybiera z niej trzeci element, bo indeksy zaczynają się od 0 (int); wypisze 30