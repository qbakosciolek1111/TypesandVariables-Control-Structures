###
# Prints a survey of three yes-no questions,
# saves the answers in logical variables and prints the results
#
print('SURVEY')
computer_science = input('Are you interested in computer science? (y/n): ') == 'y'  # porównanie z 'y' daje True albo False, więc od razu zapisuję odpowiedź jako zmienną logiczną; każda inna odpowiedź niż 'y' (też 'Y') da False
games = input('Do you like playing computer games? (y/n): ') == 'y'
instagram = input('Do you have an Instagram account? (y/n): ') == 'y'

print()  # pusta linia oddziela pytania od wyników
print('SURVEY RESULTS')
print(f'Interested in computer science: {"Yes" if computer_science else "No"}')  # "Yes" if ... else "No" to skrócony zapis if/else w jednej linii; wybiera napis w zależności od wartości logicznej; cudzysłowy w środku są inne niż na zewnątrz, żeby nie zakończyć napisu
print(f'Playing computer games: {"Yes" if games else "No"}')
print(f'Has an Instagram account: {"Yes" if instagram else "No"}')