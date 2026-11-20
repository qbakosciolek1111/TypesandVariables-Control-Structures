###
# Counts negative even numbers in the range <x, y>
#
def f(x, y):
    counter = 0
    for i in range(x, y + 1):  # y + 1, bo górna granica range() nie wchodzi do zakresu, a przedział <x, y> ma obejmować także y
        if i < 0 and i % 2 == 0:  # oba warunki naraz: liczba ujemna ORAZ parzysta; zero jest parzyste, ale nie jest ujemne, więc nie wchodzi; % działa poprawnie także dla ujemnych (np. -6 % 2 daje 0)
            counter += 1
    return counter

x = int(input('Enter x: '))
y = int(input('Enter y: '))
print(f'Negative even numbers in the range <{x},{y}>: {f(x, y)}')