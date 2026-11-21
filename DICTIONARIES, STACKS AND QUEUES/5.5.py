paragraph = "cat dog mouse cat rat cat mouse"  # tekst do przeanalizowania
word_count = {}  # pusty słownik: słowo -> liczba wystąpień
for word in paragraph.split():  # split() dzieli tekst na słowa, a pętla bierze po kolei każde
    if word in word_count:  # sprawdza, czy słowo już jest w słowniku
        word_count[word] += 1  # zwiększa jego licznik o 1
    else:
        word_count[word] = 1  # dodaje słowo z licznikiem 1
for word, count in word_count.items():  # bierze po kolei każdą parę słowo-licznik
    print(f"{word}: {count}")  # wypisuje słowo i liczbę wystąpień