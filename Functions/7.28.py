###
# Returns the number of points rolled the most times in a row
#
def f(dice):
    best_digit = dice[0]  # oczko z dotąd najdłuższą serią; na start pierwszy rzut
    best_length = 1  # długość najdłuższej dotąd serii
    current_length = 1  # długość serii, którą właśnie liczę
    for i in range(1, len(dice)):  # od drugiego rzutu, bo każdy rzut porównuję z poprzednim
        if dice[i] == dice[i - 1]:  # taki sam rzut jak poprzedni, więc seria się wydłuża
            current_length += 1
        else:  # inny rzut, więc nowa seria zaczyna się od długości 1
            current_length = 1
        if current_length > best_length:  # ostre ">" zamiast ">=", żeby przy remisie zostało oczko, które pierwsze osiągnęło tę długość
            best_length = current_length
            best_digit = dice[i]
    return int(best_digit)  # wynik jako liczba, bo dice to napis, a polecenie pokazuje wynik jako liczbę (5, a nie "5")

dice = input('Enter dice rolls: ')
print(f'f("{dice}") returns {f(dice)}')