import json  # wczytuje moduł do obsługi JSON

text = '{"name": "Anna", "age": 21, "student": true, "hobby": ["reading", "swimming"], "phone": null}'  # dane w formacie JSON zapisane jako zwykły napis
data = json.loads(text)  # zamienia napis JSON na słownik Pythona
print(data)  # wypisuje słownik
print(type(data))  # wypisuje typ danych
print(data["name"], data["student"], data["phone"])  # wypisuje wybrane wartości

back = json.dumps(data, indent=4)  # zamienia słownik z powrotem na napis JSON, indent=4 ładnie go formatuje
print(back)  # wypisuje napis JSON