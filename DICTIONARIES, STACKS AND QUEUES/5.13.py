import queue  # wczytuje moduł ze stosem (LifoQueue)

stack = queue.LifoQueue()  # stos na liczby i wyniki pośrednie

while True:  # pętla działa, dopóki nie wpiszesz znaku =
    value = input('Enter a number, an operator (+ - * /) or = : ')  # pobiera liczbę, operator albo =
    if value == '=':  # użytkownik chce zobaczyć wynik
        result = stack.get()  # zdejmuje wynik ze stosu
        if result == int(result):  # sprawdza, czy wynik jest liczbą całkowitą
            result = int(result)  # zamienia 10.0 na 10, żeby wynik ładnie wyglądał
        print('Result:', result)  # wypisuje wynik
        break  # kończy program
    elif value in ('+', '-', '*', '/'):  # użytkownik wpisał operator
        b = stack.get()  # zdejmuje drugą liczbę (ta, którą położono ostatnio)
        a = stack.get()  # zdejmuje pierwszą liczbę
        if value == '+':
            stack.put(a + b)  # kładzie z powrotem wynik dodawania
        elif value == '-':
            stack.put(a - b)  # kolejność ma znaczenie: a minus b, a nie b minus a
        elif value == '*':
            stack.put(a * b)  # kładzie wynik mnożenia
        else:
            stack.put(a / b)  # kładzie wynik dzielenia: a przez b
    else:  # w pozostałych przypadkach to liczba
        stack.put(float(value))  # zamienia tekst na liczbę i kładzie ją na stos