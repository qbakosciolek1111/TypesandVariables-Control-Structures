prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}  # cennik: produkt -> cena za sztukę
cart = {'juice': 3, 'bread': 1, 'milk': 2}  # koszyk: produkt -> liczba sztuk
total = 0  # suma kosztów, na start 0
for product, quantity in cart.items():  # bierze po kolei każdą parę produkt-ilość z koszyka
    total += prices[product] * quantity  # mnoży cenę produktu z cennika przez ilość i dodaje do sumy
print(f'Total cost: {total:.2f}')  # wypisuje sumę z dwoma miejscami po przecinku