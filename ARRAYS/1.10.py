###
# Prints test statistics
#
test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False]  # typ: list zawierająca 15 elementów typu bool (True/False)

# calculates the number of test questions
question_number = len(test_results)  # len() to funkcja wbudowana; zwraca liczbę elementów listy (typ int)

# calculates the number of correct answers
correct_answers = 0  # typ int; licznik poprawnych odpowiedzi
for answer in test_results:  # pętla for bierze po kolei każdy element listy; answer w każdym obrocie jest typu bool
    if answer:  # bool można wstawić wprost do if, bez pisania == True; warunek jest prawdziwy tylko dla True
        correct_answers += 1

# calculates the number of incorrect answers
incorrect_answers = question_number - correct_answers  # int minus int daje int; nie trzeba drugiej pętli, bo odpowiedzi są albo poprawne, albo błędne

# calculates the percentage of correct answers
percentage = correct_answers / question_number * 100  # operator / zawsze zwraca float (liczbę zmiennoprzecinkową), nawet gdy wynik wychodzi całkowity

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Percentage of correct answers:', round(percentage, 2))  # round() to funkcja wbudowana; drugi argument 2 oznacza dwa miejsca po przecinku, żeby nie wypisywać 66.66666666666667