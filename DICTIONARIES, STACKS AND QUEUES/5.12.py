import queue  # wczytuje moduł ze stosem (LifoQueue)

def reverse_string(text):  # zwraca tekst odwrócony za pomocą stosu
    stack = queue.LifoQueue()  # tworzy pusty stos
    for char in text:  # bierze po kolei każdy znak tekstu
        stack.put(char)  # kładzie znak na stos
    reversed_text = ''  # pusty napis na wynik
    while not stack.empty():  # zdejmuje znaki, dopóki stos nie jest pusty
        reversed_text += stack.get()  # zdejmuje wierzch stosu (ostatni znak) i dopisuje go do wyniku
    return reversed_text  # zwraca odwrócony tekst

text = input('Enter text: ')  # pobiera tekst od użytkownika
print('Reversed text:', reverse_string(text))  # wypisuje odwrócony tekst