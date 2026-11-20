###
# Returns a string of n asterisks separated by a slash sign
#
def f(n):
    return '/'.join('*' * n)  

n = int(input('Enter n: '))
print(f'f({n}) returns "{f(n)}"')