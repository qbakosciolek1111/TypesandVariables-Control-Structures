###
# Calculates the factorial recursively
#
def factorial(n):
    # 0! = 1, 1! = 1
    if n == 0 or n == 1:  # przypadek bazowy: bez niego funkcja wywoływałaby samą siebie w nieskończoność i program zakończyłby się błędem RecursionError
        return 1

    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n - 1)  # rekurencja: funkcja wywołuje samą siebie dla mniejszej liczby, aż dojdzie do przypadku bazowego; dopiero wtedy wyniki "wracają" i się mnożą

n = 5
print(f'{n}! = {factorial(n)}')