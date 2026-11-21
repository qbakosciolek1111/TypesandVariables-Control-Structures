import re  # wczytuje moduł do wyrażeń regularnych
with open('files.txt', 'r') as file:  # otwiera plik z nazwami do odczytu, a po bloku sam go zamknie
    for line in file:  # bierze po kolei każdą linię pliku
        name = line.strip()  # usuwa z linii znak nowej linii i spacje na brzegach
        if re.search(r'\.[a-z0-9]{4}$', name):  # sprawdza, czy nazwa kończy się kropką i dokładnie czterema znakami
            print(name)  # wypisuje pasującą nazwę pliku