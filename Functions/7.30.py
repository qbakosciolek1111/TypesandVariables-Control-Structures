###
# Calculates the sum of natural numbers from 1 to n recursively
#
def sum_natural(n):
    if n == 1:  # przypadek bazowy: suma liczb od 1 do 1 to po prostu 1; bez niego funkcja wywoływałaby samą siebie w nieskończoność i program zakończyłby się błędem RecursionError
        return 1
    return n + sum_natural(n - 1)  # rekurencja: suma od 1 do n to n plus suma od 1 do n-1; funkcja wywołuje samą siebie dla mniejszej liczby, aż dojdzie do przypadku bazowego

n = 10
print(f'The sum of natural numbers in the range <1,{n}> is {sum_natural(n)}')