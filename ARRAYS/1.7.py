###
# Prints shopping list
#
shopping_list = [
    "milk", "bread", "eggs", "butter", "cheese",
    "tomatoes", "potatoes", "carrots", "onions", "garlic"
]  # typ: list zawierająca 10 elementów typu str (napisy)

for item in shopping_list:  # pętla for bierze po kolei każdy element listy; item w każdym obrocie jest typu str
    print(item)  # print() to funkcja wbudowana; domyślnie kończy każdy napis nową linią, więc każdy produkt trafia do osobnej linii