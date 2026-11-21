###
# Reads the entire contents of a file and prints the lines sorted alphabetically
#
def read_from_file(name):  # name to parametr, czyli dowolna nazwa bez kropki; dostanie wartość 'countries.txt' przy wywołaniu poniżej
    with open(name, 'r') as file: 
        content = file.read()
    return content  

# reads the entire file
file_content = read_from_file('countries.txt')  
file_lines = file_content.splitlines()  # splitlines() to metoda napisu; dzieli tekst na linie i zwraca list z elementami typu str, już BEZ znaków \n na końcu

sorted_lines = sorted(file_lines)  # sorted() to funkcja wbudowana; zwraca NOWĄ posortowaną list i nie zmienia oryginału; napisy porównuje alfabetycznie, litera po literze, więc o kolejności decyduje nazwa kraju na początku linii

for line in sorted_lines:
    print(line)