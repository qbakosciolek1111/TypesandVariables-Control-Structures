###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'  # typ: str; plik, z którego czytam
position_file = 'software_engineer.txt'  # typ: str; plik, do którego zapisuję

# Position
job_title = 'Software Engineer'  # typ: str; szukany fragment tekstu

# write selected employees to a file
with open(employees_file, 'r') as source: 
    with open(position_file, 'w') as target: 
        for line in source:  
            if job_title in line:  
                target.write(line)  