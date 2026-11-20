###
# Sum of the even or odd digits of a number
#
def f(number, even):
    total = 0
    for digit in str(abs(number)):  # str() zamienia liczbę na napis, żeby pętla brała po jednej cyfrze; abs() odrzuca minus, który inaczej trafiłby do pętli jako "cyfra"
        d = int(digit)  # znak z napisu trzeba zamienić z powrotem na liczbę, żeby sprawdzić parzystość i dodać
        if (d % 2 == 0) == even:  # porównanie d % 2 == 0 daje True dla cyfry parzystej; jeśli zgadza się z parametrem even, cyfra jest tego rodzaju, jakiego szukamy (True szuka parzystych, False nieparzystych)
            total += d
    return total

number = int(input('Enter number: '))
print(f'Sum of even digits of {number}: {f(number, True)}')
print(f'Sum of odd digits of {number}: {f(number, False)}')