import queue  # wczytuje moduł ze stosem (LifoQueue)

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # nawiasy poprawne
expression2 = "[(2+3]/4)"  # nawiasy niepoprawne
expression3 = "(2-3*4+(5/6)"  # nawiasy niepoprawne

def brackets_ok(expression):  # zwraca True, jeśli nawiasy w wyrażeniu są poprawne, a False w przeciwnym razie
    stack = queue.LifoQueue()  # tworzy pusty stos na nawiasy otwierające
    pairs = {')': '(', ']': '[', '}': '{'}  # słownik: nawias zamykający -> pasujący do niego otwierający
    for char in expression:  # bierze po kolei każdy znak wyrażenia
        if char in '([{':  # to nawias otwierający
            stack.put(char)  # kładzie go na stos
        elif char in ')]}':  # to nawias zamykający
            if stack.empty():  # nie ma nawiasu otwierającego, z którym można go sparować
                return False  # nawiasy niepoprawne
            if stack.get() != pairs[char]:  # zdejmuje wierzch stosu i sprawdza, czy pasuje do nawiasu zamykającego
                return False  # nawiasy się nie zgadzają
    return stack.empty()  # poprawne tylko wtedy, gdy na stosie nie zostały niezamknięte nawiasy

if brackets_ok(expression1):  # sprawdza pierwsze wyrażenie
    print('Brackets in expression1 are correct')  # komunikat dla poprawnych nawiasów
else:
    print('Brackets in expression1 are not correct')  # komunikat dla niepoprawnych nawiasów

if brackets_ok(expression2):  # sprawdza drugie wyrażenie
    print('Brackets in expression2 are correct')
else:
    print('Brackets in expression2 are not correct')

if brackets_ok(expression3):  # sprawdza trzecie wyrażenie
    print('Brackets in expression3 are correct')
else:
    print('Brackets in expression3 are not correct')