###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#
def weekday(n):  # funkcja zdefiniowana przez nas; parametr n to int (numer dnia 1-7), zwraca str (nazwę dnia)
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]  # typ: list zawierająca elementy typu str (napisy)
    return weekdays[n - 1]  # indeksy listy zaczynają się od 0, a numery dni od 1, więc odejmuję 1 (dzień 1 to weekdays[0]); zwracany jest element typu str

for day_number in [1, 4, 7]:  # lista int z numerami dni z polecenia; pętla for bierze po kolei każdy element
    print(f'Day {day_number}: {weekday(day_number)}')  # print() to funkcja wbudowana; f-string wstawia int i str do napisu