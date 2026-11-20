###
# Counts how many times the given letter appears in a text
#
def count_letter(letter, text):
    counter = 0
    for char in text.lower():  # lower() zamienia cały tekst na małe litery, żeby 'E' i 'e' liczyły się tak samo
        if char == letter.lower():  # to samo robię z szukaną literą, żeby porównanie nie zależało od wielkości liter
            counter += 1  # licznik rośnie tylko przy trafieniu
    return counter

text = 'You never get a second chance to make a first impression'
letter = input('Enter a letter: ')  
print(text)
print(f"The number of letter '{letter}': {count_letter(letter, text)}")