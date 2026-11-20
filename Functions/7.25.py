###
# Returns the sum of numbers in the range <x, y> that are divisible
# by 2 and 3 and not divisible by 4
#
def f(x, y):
    total = 0
    for i in range(x, y + 1):  # y + 1, bo górna granica range() nie wchodzi do zakresu, a przedział <x, y> ma obejmować także y (w drugim przykładzie 30 musi się liczyć)
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:  # trzy warunki naraz: podzielna przez 2, przez 3 i NIE przez 4; "and" wymaga, żeby wszystkie były prawdziwe
            total += i
    return total

x = int(input('Enter x: '))
y = int(input('Enter y: '))
print(f'f({x},{y}) returns {f(x, y)}')