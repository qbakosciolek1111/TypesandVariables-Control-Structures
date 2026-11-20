###
# Calculates the value of all the goods available in the store
#
# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]  # typ: list zawierająca elementy typu float (liczby z częścią ułamkową)

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]  # typ: list zawierająca elementy typu int; ilość na pozycji i należy do ceny na tej samej pozycji i

total_value = 0  # typ int na starcie; po dodaniu pierwszej ceny razy ilość zmieni się w float (int + float daje float)
for i in range(len(product_prices)):  # len() to funkcja wbudowana, zwraca 10 (int); range(10) daje indeksy 0-9, a indeks jest potrzebny, żeby wziąć cenę i ilość z tej samej pozycji obu list
    total_value += product_prices[i] * product_quantities[i]  # float * int daje float; wartość jednego towaru to cena razy liczba sztuk, a wszystkie dodaję do sumy

print('Total value of the goods:', round(total_value, 2))  # round() to funkcja wbudowana; zaokrągla do 2 miejsc, bo suma liczb float potrafi wyjść z długim ogonem (tu 49748.74999999999)