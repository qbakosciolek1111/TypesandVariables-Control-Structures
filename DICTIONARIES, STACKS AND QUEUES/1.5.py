countries = [  # lista pięciu słowników
    {"name": "Poland", "population": 38000000},  # kraj i liczba mieszkańców
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 68000000},
    {"name": "Italy", "population": 59000000},
    {"name": "Spain", "population": 48000000}
]
print(f"{'COUNTRY':<10}POPULATION")  # wypisuje nagłówek, :<10 wyrównuje kolumnę do lewej na 10 znaków
for country in countries:  # bierze po kolei każdy słownik z listy
    print(f"{country['name']:<10}{country['population']}")  # wypisuje nazwę i liczbę mieszkańców w równych kolumnach