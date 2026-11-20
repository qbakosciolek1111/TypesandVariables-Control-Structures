###
# Returns a sentence with the spaces removed
#
def f(sentence):
    return sentence.replace(' ', '')  # replace() zamienia każde wystąpienie pierwszego napisu na drugi; zamiana spacji na pusty napis po prostu ją usuwa; oryginał się nie zmienia, bo napisy w Pythonie są niemodyfikowalne, więc wynik trzeba zwrócić

sentence = input('Enter a sentence: ')
print(f'f("{sentence}") returns "{f(sentence)}"')