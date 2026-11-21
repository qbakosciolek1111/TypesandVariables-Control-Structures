###
# Reads from file, line by line, and prints a numbered list of countries
#
number = 1  # typ: int; numer pozycji na liście, zaczynam od 1, bo lista ma być ponumerowana od jedynki

with open('countries.txt', 'r') as file:  # open() to funkcja wbudowana; zwraca obiekt pliku, a 'r' to tryb odczytu; with zamyka plik automatycznie po wyjściu z bloku
    for line in file:  # pętla po pliku bierze po kolei każdą linię; line jest typu str i KOŃCZY SIĘ znakiem nowej linii \n
        print(f'{number}. {line}', end="")  # f-string wstawia int (number) i str (line) do jednego napisu; end="" wyłącza dodatkowe przejście do nowej linii, bo line już ma na końcu \n, więc bez tego byłyby puste linie między krajami
        number += 1  # zwiększam numer tylko po wypisaniu linii, więc numeracja idzie 1, 2, 3, 