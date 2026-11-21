import json  # wczytuje moduł do obsługi plików JSON

# Open the JSON file in read mode
with open('computer.json', 'r', encoding='utf-8') as file:  # otwiera plik JSON do odczytu; utf-8 pozwala poprawnie czytać znaki specjalne
   # Load the data from the JSON file into a variable
   data = json.load(file)  # zamienia zawartość pliku na słownik

# Print the JSON data
for key, value in data.items():  # bierze po kolei każdą parę klucz-wartość ze słownika
   print(key, ':', value)  # wypisuje klucz i wartość