###
# Checks if at least 3 people were in the room at the same time
#
def f(detector):
    people = 0  # aktualna liczba osób w pokoju; zaczynam od pustego pokoju
    for sign in detector:  # pętla po napisie bierze po jednym znaku, czyli po jednym zdarzeniu
        if sign == '+':
            people += 1  # ktoś wszedł
        elif sign == '-':
            people -= 1  # ktoś wyszedł
        if people >= 3:  # sprawdzam po KAŻDEJ zmianie, bo liczy się moment, w którym w pokoju było 3 osoby naraz, a nie liczba plusów w całym napisie
            return True  # return kończy funkcję od razu, więc dalsze znaki nie są już potrzebne
    return False  # pętla przeszła cały napis i nigdy nie było 3 osób

detector = input('Enter detector readings (+ and -): ')
print(f'f("{detector}") returns {f(detector)}')