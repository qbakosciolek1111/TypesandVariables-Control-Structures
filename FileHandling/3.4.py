###
# Calculates the total value of money spent
#
import re  # module for regular expressions

# file name with shopping report
email_file = 'report.txt'  # typ: str

# read the content of email
with open(email_file, 'r', encoding='utf-8') as file:  # encoding='utf-8' jest potrzebne, bo mail zawiera znak € i myślniki
    email = file.read()  

# regular expression pattern
# for amounts
pattern = r'€(\d+)'  

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email) 

# calculate the total purchases
total = 0 
for amount in amounts: 
    total += int(amount)  

# print result
print('Total spent:', total, '€')  # print() to funkcja wbudowana