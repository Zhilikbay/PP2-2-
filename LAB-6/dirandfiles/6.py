import string

for letter in string.ascii_uppercase:
    filename = letter + '.txt'
    with open(filename, 'w') as file:
        file.write(f'This is the file {filename}.\n')
    print(f'The file {filename} has been created.')