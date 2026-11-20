###
# Masks a credit card number: only the first two
# and the last four digits remain visible
#
def hide(card_number):
    stars = '*' * (len(card_number) - 6)  # liczba gwiazdek to długość numeru minus 2 widoczne cyfry z przodu i 4 z tyłu, czyli dla 16 cyfr wychodzi 10; napis razy liczba powtarza ten napis
    return card_number[:2] + stars + card_number[-4:]  # [:2] to dwa pierwsze znaki, a [-4:] to cztery ostatnie (minus liczy od końca)

card_number = input('Enter credit card number: ')  # zostaje tekstem, bo gdyby to było int(), ewentualne zero z początku numeru by zniknęło
print(f'Credit card number: {hide(card_number)}')