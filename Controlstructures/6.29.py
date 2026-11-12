###
# Finds the first N prime numbers
#
N = int(input('Enter N: '))
found = 0  # ile liczb pierwszych już znaleziono; pętla główna kończy się, gdy found dojdzie do N
candidate = 2  # sprawdzam kolejne liczby od 2, bo 2 jest najmniejszą liczbą pierwszą (1 nią nie jest)

print('Prime numbers:', end=' ')
while found < N:  # nie wiadomo z góry, jak daleko trzeba szukać, żeby znaleźć N liczb, więc to while, a nie for
    is_prime = True  # zakładam, że kandydat jest pierwszy, i odwołuję to, gdy znajdę dzielnik; flagę trzeba ustawiać od nowa dla każdego kandydata
    for divisor in range(2, candidate):  # dzielniki od 2 do candidate - 1; 1 i sama liczba są dozwolone, więc ich nie sprawdzam
        if candidate % divisor == 0:  # reszta 0 oznacza, że divisor dzieli kandydata, czyli kandydat ma dodatkowy dzielnik
            is_prime = False
            break  # wystarczy jeden dzielnik, żeby odrzucić kandydata; dalsze sprawdzanie jest zbędne
    if is_prime:
        print(candidate, end=' ')
        found += 1  # licznik rośnie tylko, gdy znaleziono liczbę pierwszą; inaczej pętla nigdy by się nie zakończyła we właściwym momencie
    candidate += 1  # przechodzę do następnej liczby niezależnie od wyniku

print()  # kończy wiersz