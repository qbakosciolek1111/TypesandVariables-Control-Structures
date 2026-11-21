import csv  # wczytuje moduł do obsługi plików CSV

provinces = {}  # słownik: litera -> nazwa województwa
with open('province.csv', 'r', newline='', encoding='utf-8') as file:  # otwiera plik z województwami; utf-8, bo są w nim polskie litery
    reader = csv.DictReader(file)  # czyta wiersze jako słowniki z kluczami Letter i Name
    for row in reader:  # bierze po kolei każde województwo
        provinces[row['Letter']] = row['Name']  # zapisuje: litera -> nazwa

counts = {}  # słownik: nazwa województwa -> liczba pojazdów
for name in provinces.values():  # bierze po kolei każdą nazwę województwa
    counts[name] = 0  # ustawia licznik na 0, żeby województwa bez pojazdów też były na liście

with open('vehicle.txt', 'r', encoding='utf-8') as file:  # otwiera plik z numerami rejestracyjnymi
    for line in file:  # bierze po kolei każdą linię
        plate = line.strip()  # usuwa z linii znak nowej linii i spacje na brzegach
        if plate != '' and plate[0] in provinces:  # pomija puste linie i litery, których nie ma w pliku województw
            counts[provinces[plate[0]]] += 1  # zamienia pierwszą literę na nazwę województwa i zwiększa jego licznik o 1

for name, count in counts.items():  # bierze po kolei każde województwo i jego licznik
    print(f'{name}: {count}')  # wypisuje nazwę i liczbę pojazdów