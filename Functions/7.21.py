###
# Returns the difference between the largest and smallest
# of three numbers
#
def f(number1, number2, number3):
    return max(number1, number2, number3) - min(number1, number2, number3)  # max() i min() to wbudowane funkcje (jak w 2.1), więc nie trzeba samemu porównywać trzech liczb; od największej odejmuję najmniejszą, więc wynik nigdy nie jest ujemny

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
number3 = int(input('Enter third number: '))
print(f'f({number1}, {number2}, {number3}) returns {f(number1, number2, number3)}')