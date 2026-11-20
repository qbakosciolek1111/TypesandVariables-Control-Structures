###
# Returns the n-th value of the Fibonacci sequence
# (first value: 0, second value: 1)
#
def f(n):
    a = 0  # pierwszy wyraz ciągu
    b = 1  # drugi wyraz ciągu
    for i in range(n - 1):  # n - 1 przesunięć, bo a na starcie jest już pierwszym wyrazem; po jednym przesunięciu a to drugi wyraz, po dwóch trzeci itd.
        a, b = b, a + b  # nowe a to stare b, a nowe b to suma starych a i b; zapis w jednej linii liczy obie prawe strony ZANIM cokolwiek przypisze, więc nie trzeba zmiennej pomocniczej
    return a  # po n - 1 przesunięciach w a jest n-ty wyraz

n = int(input('Enter n: '))
print(f'f({n}) returns {f(n)}')