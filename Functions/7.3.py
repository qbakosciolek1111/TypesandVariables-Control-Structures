###
# Returns a month name based on the month number (1..12)
#
def month(n):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    if n < 1 or n > 12:  # bez tego numer spoza zakresu dałby błąd IndexError albo (dla ujemnych) zły miesiąc liczony od końca listy
        return 'Incorrect month number'
    return months[n - 1]  # indeksy listy zaczynają się od 0, a numery miesięcy od 1, więc trzeba odjąć 1 (np. miesiąc 9 to months[8])

month_number = int(input('Enter month number: '))
print(f'The name of month {month_number} is {month(month_number)}')