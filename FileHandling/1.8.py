###
# Prints the text of a file and counts the number of words in it
#
total_words = 0  

with open('pets.txt', 'r') as file:  
    for line in file:  
        print(line, end="") 
        total_words += len(line.split())  
print()  
print('Number of words:', total_words)