###
# Counts the number of lines, characters and words in any text file
#
file_name = input('File name: ')  # typ: str; input() to funkcja wbudowana, która zwraca nazwę pliku wpisaną przez użytkownika

try:  
    with open(file_name, 'r', encoding='utf-8') as file:  
        content = file.read()  

    lines = len(content.splitlines())  # splitlines() dzieli tekst na list z liniami, a len() to funkcja wbudowana, która zlicza jej elementy (int)
    characters = len(content)  
    words = len(content.split())  

    print('Number of lines:', lines)  
    print('Number of characters:', characters)
    print('Number of words:', words)
except FileNotFoundError: 
    print(f"File '{file_name}' does not exist.")  