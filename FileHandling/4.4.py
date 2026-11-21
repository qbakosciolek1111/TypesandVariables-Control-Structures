###
# Prints the file it_company.csv five lines at a time;
# waits for the Enter key after each portion
#
with open('it_company.csv', 'r') as file:  
    lines = file.read().splitlines()  

for start in range(0, len(lines), 5):  
    for line in lines[start:start + 5]:  
        print(line)  
    if start + 5 < len(lines):  #
        print('Press Enter key...')
        input()  