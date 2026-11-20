###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)  # len() liczy też spację, więc wychodzi 16, a nie 15

letter = input('Enter a letter: ')  # input() zawsze zwraca tekst, więc nie trzeba nic zamieniać
print('The letter you entered is', letter)

number = int("20303")  # int() zamienia napis na liczbę; w wyniku znika cudzysłów, więc to już liczba, a nie tekst
print('The number representing the string "20303" is', number)

binary = bin(304)  # bin() zwraca napis z przedrostkiem 0b, który oznacza system binarny, a nie część liczby
print('Binary string for decimal 304 is', binary)

hexadecimal = hex(304)  # tak samo: 0x oznacza system szesnastkowy
print('Hexadecimal string for decimal 304 is', hexadecimal)

unicode_code = ord('€')  # ord() jest odwrotnością chr(): zamienia znak na jego numer w tablicy Unicode
print('The Unicode code of the € sign is', unicode_code)

absolute = abs(-17)  # abs() odrzuca znak minus
print('The absolute value of -17 is', absolute)