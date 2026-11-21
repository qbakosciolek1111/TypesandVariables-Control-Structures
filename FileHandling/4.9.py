import csv  # wczytuje moduł do obsługi plików CSV
print('GRAPHIC DESIGNERS')  # wypisuje nagłówek listy
print('=================')  # wypisuje linię pod nagłówkiem
with open('it_company.csv', 'r', newline='') as file:  # otwiera plik CSV do odczytu, a po bloku sam go zamknie
    reader = csv.DictReader(file)  # czyta wiersze jako słowniki, gdzie kluczami są nazwy kolumn z nagłówka
    for row in reader:  # bierze po kolei każdy wiersz pliku (bez nagłówka)
        if row['Job Title'] == 'Graphic Designer':  # sprawdza, czy w kolumnie stanowiska jest dokładnie Graphic Designer
            print(f"{row['First Name']} {row['Last Name']},{row['Email']}")  # wypisuje imię, nazwisko i e-mail w podanej kolejności