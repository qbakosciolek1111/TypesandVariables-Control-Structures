products = {  # słownik: produkt -> liczba sztuk
    'Laptop': 15, 'Desktop PC': 10, 'Monitor': 25, 'Keyboard': 50, 'Mouse': 60,
    'External Hard Drive': 30, 'Printer': 12, 'Router': 20, 'USB Flash Drive': 100, 'Graphics Card': 8
}
total = 0  # suma wszystkich sztuk, na start 0
for product, quantity in products.items():  # bierze po kolei każdą parę produkt-ilość
    print(f"{product}: {quantity}")  # wypisuje produkt i jego ilość
    total += quantity  # dodaje ilość do sumy
print("Total number of products:", total)  # wypisuje sumę