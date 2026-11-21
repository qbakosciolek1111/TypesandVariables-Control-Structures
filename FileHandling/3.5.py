###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('Enter username: ')  # typ: str; input() to funkcja wbudowana, która zwraca to, co wpisał użytkownik
password = input('Enter password: ')  # typ: str

# pattern (criteria) for username and password
username_pattern = r'^[a-z]{6,}$'  # ^ to początek napisu, a $ to jego koniec, więc cały napis musi pasować (inaczej re.match sprawdzałby tylko początek); [a-z] to jedna mała litera; {6,} oznacza "6 lub więcej" razy, więc login ma co najmniej 6 znaków i tylko małe litery
password_pattern = r'^[A-Za-z0-9_]{8,}$'  # [A-Za-z0-9_] to dozwolone znaki: małe i wielkie litery, cyfry i podkreślenie; {8,} oznacza co najmniej 8 znaków; użyłem jawnej listy znaków zamiast \w, bo \w w Pythonie przepuszcza też polskie litery (ą, ę, ś), a polecenie ich nie dopuszcza

# check if username and password are ok
username_match = re.match(username_pattern, username)  # re.match() sprawdza wzorzec od początku napisu; zwraca obiekt dopasowania, a jeśli nie pasuje, zwraca None
password_match = re.match(password_pattern, password)

# print results
if username_match and password_match:  
    print('Username and password are correct')
else:
    print('Incorrect username or password')