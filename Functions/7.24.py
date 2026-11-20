###
# Returns the value of an expression with single-digit numbers
# joined by the + and - operators
#
def f(expression):
    result = int(expression[0])  # wyrażenie zawsze zaczyna się od cyfry, więc pierwszy znak to początkowa wartość wyniku
    for i in range(1, len(expression), 2):  # krok 2, bo znaki w wyrażeniu na przemian: operator, cyfra, operator, cyfra; zaczynam od indeksu 1, czyli od pierwszego operatora
        operator = expression[i]  # znak na pozycji i to + albo -
        digit = int(expression[i + 1])  # cyfra tuż za operatorem, zamieniona z tekstu na liczbę
        if operator == '+':
            result += digit
        else:  # jedyny inny operator to -
            result -= digit
    return result

expression = input('Enter an expression: ')
print(f'f("{expression}") returns {f(expression)}')