import queue  # wczytuje moduł ze stosem (LifoQueue)

number = int(input('Natural number: '))  # pobiera liczbę naturalną od użytkownika
stack = queue.LifoQueue()  # tworzy pusty stos na reszty z dzielenia

n = number  # kopia liczby, bo w pętli będzie się zmniejszać, a oryginał jest potrzebny do wypisania
if n == 0:  # dla zera pętla poniżej by się nie wykonała
    stack.put(0)  # kładzie 0 na stos, żeby wynik nie był pusty
while n > 0:  # dzieli, dopóki liczba nie spadnie do zera
    stack.put(n % 2)  # kładzie na stos resztę z dzielenia przez 2 (0 albo 1)
    n = n // 2  # dzieli liczbę całkowicie przez 2

binary = ''  # pusty napis na wynik
while not stack.empty():  # zdejmuje elementy, dopóki stos nie jest pusty
    binary += str(stack.get())  # zdejmuje wierzch stosu i dopisuje go do wyniku; ostatnia reszta wychodzi pierwsza, więc kolejność jest odwrócona jak trzeba

print('Binary number:', binary)  # wypisuje wynik