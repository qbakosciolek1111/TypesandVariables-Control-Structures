translations = {  # słownik: słowo angielskie -> polskie
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}
word = input('Enter an English word: ')  # pobiera słowo od użytkownika
if word in translations:  # sprawdza, czy słowo jest wśród kluczy słownika
    print(f'{word} -> {translations[word]}')  # wypisuje słowo i jego tłumaczenie
else:
    print('Translation is unavailable.')  # informuje, że tłumaczenia nie ma