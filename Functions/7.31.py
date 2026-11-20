###
# Calculates x to the power of n recursively
#
def power(x, n):
    if n == 0:  # przypadek bazowy: każda liczba do potęgi 0 to 1; bez niego funkcja wywoływałaby samą siebie w nieskończoność i program zakończyłby się błędem RecursionError
        return 1
    return x * power(x, n - 1)  # rekurencja z podpowiedzi: x^n = x * x^(n-1); funkcja wywołuje samą siebie z mniejszym wykładnikiem, aż dojdzie do przypadku bazowego

x = 5
n = 3
print(f'{x}^{n} = {power(x, n)}')