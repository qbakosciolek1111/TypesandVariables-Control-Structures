###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
   code = ord(char)         # ord() zamienia znak na jego numer w tablicy znaków, np. 'T' -> 84
   code = code + 1         # przesunięcie o jedną pozycję: 84 -> 85
   new_char = chr(code)           # chr() robi odwrotnie: zamienia numer na znak, np. 85 -> 'U'
   encrypted_text = encrypted_text + new_char
print(plain_text)
print(encrypted_text)