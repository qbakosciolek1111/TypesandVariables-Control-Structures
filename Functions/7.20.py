###
# Returns the n-th prime number
#
def f(n):
    found = 0  # ile liczb pierwszych już znaleziono
    candidate = 1  # zaczynam od 1, bo na początku pętli zwiększam kandydata, więc pierwszym sprawdzanym będzie 2
    while found < n:  # nie wiadomo z góry, jak daleko trzeba szukać, więc while, a nie for
        candidate += 1
        is_prime = True  # zakładam, że kandydat jest pierwszy, i odwołuję to, gdy znajdę dzielnik; flagę trzeba ustawiać od nowa dla każdego kandydata
        for divisor in range(2, candidate):  # dzielniki od 2 do candidate - 1; dla 2 zakres jest pusty, więc 2 zostaje pierwsza
            if candidate % divisor == 0:  # reszta 0 oznacza, że divisor dzieli kandydata, czyli kandydat ma dodatkowy dzielnik
                is_prime = False
                break  # jeden dzielnik wystarczy, żeby odrzucić kandydata
        if is_prime:
            found += 1  # licznik rośnie tylko przy znalezieniu liczby pierwszej
    return candidate  # po wyjściu z pętli candidate to właśnie n-ta liczba pierwsza

n = int(input('Enter n: '))
print(f'f({n}) returns {f(n)}')