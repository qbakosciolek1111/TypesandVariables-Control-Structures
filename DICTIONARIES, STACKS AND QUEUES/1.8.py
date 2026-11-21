price_list = {'T-shirt': 19.99, 'Jeans': 49.99, 'Jacket': 89.99, 'Sneakers': 59.99, 'Hat': 15.99}  # słownik: produkt -> cena
print("Prices before the discount:")  # nagłówek listy przed przeceną
for product, price in price_list.items():  # bierze po kolei każdą parę produkt-cena
    print(f"{product}: {price}")  # wypisuje produkt i cenę
print("Total value before the discount:", round(sum(price_list.values()), 2))  # sum() dodaje wszystkie ceny, round() zaokrągla do 2 miejsc
for product in price_list:  # bierze po kolei każdy klucz słownika
    price_list[product] = round(price_list[product] * 0.9, 2)  # zmienia cenę na 90% starej, zaokrągloną do 2 miejsc
print("Prices after the 10% discount:")  # nagłówek listy po przecenie
for product, price in price_list.items():  # znów bierze po kolei każdą parę
    print(f"{product}: {price}")  # wypisuje produkt i nową cenę
print("Total value after the discount:", round(sum(price_list.values()), 2))  # sumuje nowe ceny