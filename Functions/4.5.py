###
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):
    grade = ''
    if points >= 18:  # progi sprawdzam od najwyższego w dół, bo 20 pkt spełnia też warunki >= 14 i >= 10; elif wykona tylko pierwszy pasujący, więc kolejność jest tu kluczowa
        grade = 'Excellent'
    elif points >= 14:  # tu trafia już tylko 14-17, bo 18+ zostało obsłużone wyżej, więc nie trzeba pisać "points < 18"
        grade = 'Good'
    elif points >= 10:
        grade = 'Satisfactory'
    else:  # zostaje wszystko poniżej 10
        grade = 'Fail'
    return grade  # return stoi poza if/elif, więc działa dla każdej gałęzi

test_result = 15
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')