###
# Prints the number of array elements greater than a value entered from the keyboard
#
arr = [3.5, 7.2, 1.8, 9.4, 5.0, 2.6]  # typ: list zawierająca 6 elementów typu float (liczby rzeczywiste)
value = float(input('Enter a value: '))  # input() zwraca str, a float() zamienia go na liczbę rzeczywistą, bo porównujemy z liczbami z częścią ułamkową; przyjmie też zapis całkowity, np. 4

counter = 0  # typ: int; licznik elementów większych od value
for number in arr:  # pętla for bierze po kolei każdy element listy; number w każdym obrocie jest typu float
    if number > value:  # porównanie zwraca bool; ostre ">" oznacza "większe", więc element równy value się nie liczy
        counter += 1

print('Array:', arr)  # print() to funkcja wbudowana
print(f'Number of elements greater than {value}: {counter}')