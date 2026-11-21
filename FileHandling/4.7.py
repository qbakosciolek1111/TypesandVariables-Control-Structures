import re  # wczytuje moduł do wyrażeń regularnych
text = input('Enter text: ')  # pobiera tekst wpisany przez użytkownika
vowels = re.findall(r'[aeiou]', text, re.IGNORECASE)  # zwraca listę wszystkich samogłosek z tekstu (małych i wielkich)
print('Number of vowels:', len(vowels))  # wypisuje, ile samogłosek jest na liście