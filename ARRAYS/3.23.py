###
# Functions that operate on a text (module MyText in one file)
#
def count_words(text):  # 1. funkcja własna; parametr to str, zwraca int (liczbę słów)
    return len(text.split())  # split() to metoda napisu; bez argumentu tnie tekst po spacjach i zwraca listę słów (list), a len() to funkcja wbudowana, która zlicza jej elementy

def words_by_length(text):  # 2. funkcja własna; zwraca list ze słowami od najdłuższego do najkrótszego
    return sorted(text.split(), key=len, reverse=True)  # sorted() to funkcja wbudowana zwracająca nową posortowaną listę; key=len każe porównywać słowa po długości, a nie alfabetycznie; reverse=True (bool) ustawia kolejność malejącą; słowa o tej samej długości zostają w kolejności z tekstu

def words_alphabetical(text):  # 3. funkcja własna; zwraca list ze słowami w kolejności alfabetycznej
    return sorted(text.split(), key=str.lower)  # key=str.lower porównuje słowa po zamianie na małe litery, więc "a" i "An" są ułożone razem, a nie wielkie litery przed wszystkimi małymi (bez tego "An" stałoby przed "a")

text = 'An apple a day keeps the doctor away'  # typ: str
print('Text:', text)  # print() to funkcja wbudowana
print('Number of words:', count_words(text))
print('Words from the longest:', ','.join(words_by_length(text)))  # join() to metoda napisu; skleja elementy listy (str) w jeden napis, wstawiając przecinek
print('Words ordered alphabetically:', ','.join(words_alphabetical(text)))