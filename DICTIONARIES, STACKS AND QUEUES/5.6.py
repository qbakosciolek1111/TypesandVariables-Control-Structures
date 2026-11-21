basic_data = {"name": "Barbara", "age": 21}  # pierwszy słownik z danymi podstawowymi
advanced_data = {"status": "student", "married": False, "interest": ["reading", "swimming"]}  # drugi słownik z danymi dodatkowymi
person = {}  # pusty słownik na wszystkie dane
person.update(basic_data)  # kopiuje do niego wszystkie pary z pierwszego słownika
person.update(advanced_data)  # dopisuje do niego wszystkie pary z drugiego słownika
for key, value in person.items():  # bierze po kolei każdą parę klucz-wartość
    print(f"{key}: {value}")  # wypisuje klucz i wartość