###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number = abs(number)  # abs() odrzuca znak minus, bo inaczej '-' trafiłby do pętli jako "cyfra" i int('-') zgłosiłoby błąd
    total = 0
    for digit in str(number):  # str() zamienia liczbę na napis, a pętla po napisie bierze po jednym znaku, czyli po jednej cyfrze
        total += int(digit)  # każdy znak jest tekstem, więc przed dodaniem trzeba go zamienić z powrotem na liczbę
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')