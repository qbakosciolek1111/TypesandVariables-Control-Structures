winter_semester = {"math": 60, "programming": 30, "history": 15}  # słownik: kurs -> liczba godzin
total_hours = 0  # suma godzin, na start 0
for course, hours in winter_semester.items():  # bierze po kolei każdą parę kurs-godziny
    total_hours += hours  # dodaje godziny kursu do sumy
print(f"The total number of hours in the winter semester is {total_hours}")  # wypisuje wynik