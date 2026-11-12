###
# Prints the numeric keyboard layout (version with while loops)
#
i = 6  # w pętli for range(6, -1, -3) licznik ustawiał się sam; w while muszę ustawić go ręcznie przed pętlą
while i >= 0:  # range(6, -1, -3) kończy się na 0 włącznie, więc warunek to i >= 0 (przy liczeniu w dół zmienia się kierunek nierówności)
    j = 1  # NAJWAŻNIEJSZA LINIA: licznik wewnętrzny trzeba zerować w każdym obrocie zewnętrznej pętli; for robił to sam, a w while bez tego druga i trzecia linia byłyby puste, bo j zostałoby na 4
    while j <= 3:  # range(1, 4) daje 1, 2, 3, więc warunek to j <= 3
        print(f'{i+j}', end=' ')
        j += 1  # bez zwiększania licznika pętla wewnętrzna zapętliłaby się w nieskończoność
    print()  # kończy wiersz po wypisaniu trzech cyfr
    i -= 3  # zmniejszam o 3, bo oryginał liczył w dół co 3; bez tego pętla zewnętrzna też byłaby nieskończona