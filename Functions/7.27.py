###
# Checks if the product code is correct: the fourth (control) digit
# is the remainder of dividing the sum of the first three digits by 7
#
def f(product_code):
    digits_sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])  # kod to napis, więc każdą z trzech pierwszych cyfr zamieniam przez int() na liczbę, żeby ją dodać
    control_digit = int(product_code[3])  # czwarta cyfra to ta, którą sprawdzamy
    return digits_sum % 7 == control_digit  # reszta z dzielenia sumy przez 7 musi być równa cyfrze kontrolnej; porównanie samo daje True/False

product_code = input('Enter product code: ')
print(f'f("{product_code}") returns {f(product_code)}')