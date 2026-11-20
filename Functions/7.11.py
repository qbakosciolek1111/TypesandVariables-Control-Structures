###
# Checks if at least one of three numbers is negative
#
def f(n1, n2, n3):
    return n1 < 0 or n2 < 0 or n3 < 0  # "or" daje True, gdy choć jedno porównanie jest prawdziwe; porównanie samo zwraca True/False, więc nie trzeba pisać if/else ani return True / return False

n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))
print(f'At least one of {n1}, {n2}, {n3} is negative: {f(n1, n2, n3)}')