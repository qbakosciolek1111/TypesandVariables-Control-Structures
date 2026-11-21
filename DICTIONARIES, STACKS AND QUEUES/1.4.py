person = {  # tworzy słownik z danymi osoby
    "name": "Marek",  # napis
    "surname": "Banach",  # napis
    "age": 25,  # liczba całkowita
    "hobby": ["swimming","excursions"],  # lista napisów
    "married": True,  # wartość logiczna
    "phone":{"landline":"123444321","mobile":"777888999"}  # zagnieżdżony słownik z telefonami
}
print(person["name"])  # 1. wypisuje imię
print(person["hobby"])  # 2. wypisuje hobby
print(person)  # 3. wypisuje cały słownik
person["surname"] = "Nowak"  # 4. zmienia nazwisko
person["married"] = not person["married"]  # 5. odwraca stan cywilny (True na False)
person["gender"] = "male"  # 6. dodaje nowy klucz gender
person["hobby"].append("bicycle")  # 7. dopisuje nowe hobby do listy
person["phone"]["work"] = "313131444"  # 8. dodaje telefon służbowy do zagnieżdżonego słownika
for key, value in person.items():  # 9. bierze po kolei każdą parę klucz-wartość
    print(key, ":", value)  # wypisuje klucz i wartość