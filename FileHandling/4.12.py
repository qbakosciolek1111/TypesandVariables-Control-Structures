import csv  # wczytuje moduł do obsługi plików CSV

genre_files = {  # słownik: gatunek -> nazwa pliku wynikowego
    'Fantasy': 'books_fantasy.txt',  # książki fantasy trafiają do tego pliku
    'Historical': 'books_historical.txt',  # książki historyczne trafiają do tego pliku
    'Romance': 'books_romance.txt',  # romanse trafiają do tego pliku
    'Classic': 'books_classic.txt'  # klasyka trafia do tego pliku
}

def get_file_name(genre):  # zwraca nazwę pliku dla podanego gatunku
    return genre_files.get(genre)  # get() zwraca None zamiast błędu, gdy gatunku nie ma w słowniku

def copy_books(genre, file_name):  # kopiuje książki danego gatunku do podanego pliku
    with open('books.csv', 'r', newline='') as source:  # otwiera plik z książkami do odczytu
        reader = csv.DictReader(source)  # czyta wiersze jako słowniki, kluczami są nazwy kolumn
        with open(file_name, 'w', newline='') as target:  # otwiera plik wynikowy do zapisu
            writer = csv.DictWriter(target, fieldnames=reader.fieldnames)  # tworzy zapisywacz z tymi samymi kolumnami co w oryginale
            writer.writeheader()  # zapisuje wiersz nagłówka
            for row in reader:  # bierze po kolei każdą książkę
                if row['Genre'] == genre:  # sprawdza, czy gatunek książki zgadza się z wybranym
                    writer.writerow(row)  # zapisuje całą książkę do pliku wynikowego

def main():  # główna część programu
    genre = input('Enter genre (Fantasy, Historical, Romance, Classic): ')  # pobiera gatunek od użytkownika
    file_name = get_file_name(genre)  # sprawdza, do jakiego pliku trafią książki
    if file_name is None:  # gatunku nie ma w słowniku
        print('Unknown genre.')  # informuje o nieznanym gatunku
    else:
        copy_books(genre, file_name)  # kopiuje książki do pliku
        print(f'Books copied to {file_name}.')  # potwierdza zapis

main()  # uruchamia program