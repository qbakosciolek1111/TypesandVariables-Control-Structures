###
# Checking login and password
#
login = 'joe'
password = 'abcd'
entered_login = input('Login: ')
entered_password = input('Password: ')
if login == entered_login and password == entered_password:   # "and" wymaga, żeby oba porównania były prawdziwe naraz; wystarczy jedno błędne i całość jest fałszem
    print('You are logged in')
else:
    print('Incorrect login or password!!')