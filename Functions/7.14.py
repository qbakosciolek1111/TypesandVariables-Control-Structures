###
# Returns the result of an arithmetic operation
# for the operators: +, -, *, %, **
#
def f(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '%':  # % to reszta z dzielenia, np. 2 % 3 daje 2, bo 3 nie mieści się w 2 ani razu
        return number1 % number2
    elif operator == '**':  # ** to potęgowanie: 2 ** 3 to 2 do potęgi 3, czyli 8; "**" jest dwuznakowe, ale porównuję je jak każdy inny napis
        return number1 ** number2
    else:  # polecenie podaje tylko pięć operatorów; bez tego inny znak zwróciłby None, a program wypisałby "None" bez wyjaśnienia
        return 'Incorrect operator'

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
operator = input('Enter operator (+, -, *, %, **): ')
print(f'f({number1}, {number2}, "{operator}") returns {f(number1, number2, operator)}')