import csv  # wczytuje moduł do obsługi plików CSV
with open('clothing.csv', 'r', newline='') as file:  # otwiera plik CSV do odczytu, a po bloku sam go zamknie
    reader = csv.DictReader(file)  # czyta wiersze jako słowniki, gdzie kluczami są nazwy kolumn z nagłówka
    for row in reader:  # bierze po kolei każdy wiersz pliku (bez nagłówka)
        price = float(row['Price'])  # zamienia cenę z tekstu na liczbę z częścią ułamkową
        stock = int(row['Stock_Quantity'])  # zamienia zapas z tekstu na liczbę całkowitą
        if price < 60 and stock < 40:  # sprawdza oba warunki naraz: cena poniżej 60 i zapas poniżej 40
            print(row['Product_ID'], row['Product_Name'], row['Size'], row['Color'], price, stock)  # wypisuje dane pasującego produktu