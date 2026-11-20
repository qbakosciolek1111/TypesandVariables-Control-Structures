###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
def input_string(message):
    text = input(message)
    return text

def input_integer(message):
    number = int(input(message))  # int() zamienia wpisany tekst na liczbę całkowitą
    return number

def input_real(message):
    number = float(input(message))  # float() przyjmuje liczby z kropką, np. 5400.50 (przecinek nie zadziała)
    return number

def input_boolean(message):
    answer = input(message)
    return answer == 'y'  # daje od razu True albo False; każda odpowiedź inna niż 'y' (też 'Y') da False

# Reads employee's data from keyboard
first_name = input_string('Enter name: ')
last_name = input_string('Enter last name: ')
age = input_integer('Enter age: ')
salary = input_real('Enter salary: ')
is_salary_hidden = input_boolean('Hide salary? (y/n): ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Last name:', last_name)
print('Age:', age)
if not is_salary_hidden:  # pensję wypisuję tylko wtedy, gdy użytkownik NIE kazał jej ukrywać
    print('Salary:', salary)