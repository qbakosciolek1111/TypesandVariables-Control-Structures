with open('powers.txt', 'w') as file:  # tworzy plik wynikowy do zapisu (nadpisze go, jeśli już jest), a po bloku sam go zamknie
    for number in range(1, 101):  # bierze po kolei liczby od 1 do 100 (101 nie wchodzi do zakresu)
        line = f'{number},{number ** 2},{number ** 3}'  # składa napis: liczba, jej kwadrat i sześcian, rozdzielone przecinkami
        print(line)  # wypisuje ten napis na ekran
        file.write(line + '\n')  # zapisuje ten sam napis do pliku i kończy linię znakiem nowej linii