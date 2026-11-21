import json  # wczytuje moduł do obsługi plików JSON

try:  # próbuje wczytać dotychczasowe głosy
    with open('voting.json', 'r', encoding='utf-8') as file:  # otwiera plik z głosami do odczytu
        votes = json.load(file)  # zamienia zawartość pliku na słownik: imię -> liczba głosów
except FileNotFoundError:  # pliku jeszcze nie ma (pierwsze uruchomienie)
    votes = {}  # zaczyna od pustego słownika

person_name = input('Name of the person you are voting for:')  # pobiera imię osoby, na którą oddajesz głos
if person_name in votes:  # sprawdza, czy osoba już ma jakieś głosy
    votes[person_name] += 1  # dodaje jeden głos
else:
    votes[person_name] = 1  # dodaje nową osobę z jednym głosem

with open('voting.json', 'w', encoding='utf-8') as file:  # otwiera plik do zapisu (nadpisze stary)
    json.dump(votes, file, indent=4)  # zapisuje słownik do pliku, indent=4 ładnie go formatuje