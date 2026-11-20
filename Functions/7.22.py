###
# Returns the acronym of a text (first letters of all words)
#
def f(name):
    acronym = ''
    for word in name.split():  # split() bez argumentu tnie tekst po spacjach i ignoruje podwójne spacje oraz spacje na brzegach, więc nie trafi tu pusty "wyraz", który wywołałby błąd przy word[0]
        acronym += word[0]  # word[0] to pierwszy znak słowa; wielkość liter zostaje bez zmian, dlatego "of" daje małe o
    return acronym

name = input('Enter a text: ')
print(f'f("{name}") returns "{f(name)}"')