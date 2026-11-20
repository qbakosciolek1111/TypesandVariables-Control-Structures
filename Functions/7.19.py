###
# Returns the sum of repeated digits in a number
#
def f(number):
    text = str(abs(number))  # str() zamienia liczbę na napis, żeby pętla brała po jednej cyfrze; abs() odrzuca minus, który inaczej trafiłby do pętli jako "cyfra"
    total = 0
    for digit in text:
        if text.count(digit) > 1:  # count() liczy, ile razy dana cyfra występuje w całej liczbie; więcej niż raz oznacza, że cyfra się powtarza
            total += int(digit)  # dodaję KAŻDE wystąpienie powtarzającej się cyfry (a nie tylko jedno), dlatego trzy trójki dają 9
    return total

number = int(input('Enter number: '))
print(f'f({number}) returns {f(number)}')