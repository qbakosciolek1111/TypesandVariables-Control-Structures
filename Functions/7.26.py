###
# Returns the text with all characters separated by a dash sign
#
def f(text):
    return '-'.join(text)  # join() wstawia '-' pomiędzy każde dwa kolejne znaki napisu, więc myślnik nie pojawia się na początku ani na końcu; dla jednego znaku nie ma czego rozdzielać, a dla pustego napisu wynik jest pusty, więc oba skrajne przypadki działają bez osobnego if

text = input('Enter a text: ')
print(f'f("{text}") returns "{f(text)}"')