filename = '\AZ\PP2(2)\LAB-6\dirandfiles\q.txt'
my_list = ['apple', 'banana', 'cherry', 'date']

with open(filename, 'w') as file:
    for item in my_list:
        file.write(item + '\n')

print(f'The list {my_list} has been written to {filename}.')