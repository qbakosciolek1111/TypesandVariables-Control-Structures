###
# Prints a numbered, alphabetically sorted list of popular computer games
#
computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]  # typ: list zawierająca 10 elementów typu str (napisy)

sorted_games = sorted(computer_games)  # sorted() to funkcja wbudowana; zwraca NOWĄ posortowaną listę (typ list) i nie zmienia oryginału; napisy porównuje alfabetycznie, litera po literze

i = 0  # licznik typu int; w while trzeba go ustawić ręcznie przed pętlą
while i < len(sorted_games):  # len() to funkcja wbudowana zwracająca liczbę elementów (int); pętla kręci się, dopóki i jest mniejsze od 10
    print(i + 1, sorted_games[i])  # i + 1, bo numeracja ma zacząć się od 1, a indeksy listy od 0; sorted_games[i] to element typu str
    i += 1  # bez zwiększania licznika warunek byłby zawsze prawdziwy i program zapętliłby się w nieskończoność