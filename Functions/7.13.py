###
# Returns numbers from 1 to n as a string
#
def f(n):
    result = ''  # pusty napis na start; do niego dopisuję kolejne liczby
    for i in range(1, n + 1):  # n + 1, bo górna granica range() nie wchodzi do zakresu, a n ma się znaleźć w wyniku
        result += str(i)  # str() zamienia liczbę na napis; bez tego Python próbowałby dodać liczbę do napisu i zgłosiłby TypeError
    return result

n = int(input('Enter n: '))
print(f'f({n}) returns "{f(n)}"')