###
# Checks if the password is correct: at least six characters,
# each character appears only once
#
def f(password):
    return len(password) >= 6 and len(set(password)) == len(password)  # set() tworzy zbiór, który zostawia każdy znak tylko raz, więc jeśli zbiór ma tyle samo elementów co hasło, to żaden znak się nie powtórzył; "and" wymaga, żeby oba warunki były spełnione naraz

password = input('Enter password: ')
print(f'f("{password}") returns {f(password)}')