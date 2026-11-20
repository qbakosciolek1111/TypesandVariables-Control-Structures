def add(a, b):  # a i b to parametry; wartości dostaną dopiero przy wywołaniu
    result = a + b  # zmienna result istnieje tylko wewnątrz funkcji i nie jest widoczna poza nią
    return result  # bez tej linii sum_value poniżej zawierałoby None zamiast 8

sum_value = add(5, 3)  # wywołanie: 5 trafia do a, 3 do b, a zwrócony wynik zapisuję w zmiennej
print(sum_value)  # Output: 8