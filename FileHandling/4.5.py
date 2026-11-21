###
# Fetches and prints the sender, recipient, subject and body of an email
# using regular expressions
#
import re  

def email_sender(email):  
    return re.search(r'^From:.*<(.+?)>', email, re.MULTILINE).group(1) 
def email_recipient(email): 
    return re.search(r'^To:.*<(.+?)>', email, re.MULTILINE).group(1)  

def email_subject(email): 
    return re.search(r'^Subject: (.+)$', email, re.MULTILINE).group(1) 

def email_body(email):  
    return re.search(r'\n\s*\n(.*)', email, re.DOTALL).group(1) 
with open('email.txt', 'r', encoding='utf-8') as file:  
    email = file.read()  

print('Sender:', email_sender(email))  
print('Recipient:', email_recipient(email))
print('Subject:', email_subject(email))
print('Body:')
print(email_body(email))