###
# Checks if the expression is a palindrome
#
def f(palindrome):
    return palindrome == palindrome[::-1]  # [::-1] to wycinek z krokiem -1, który odwraca napis (np. 'book' daje 'koob'); jeśli odwrócony napis jest taki sam jak oryginał, to jest palindrom; porównanie samo zwraca True/False

text = input('Enter an expression: ')
print(f'f("{text}") returns {f(text)}')