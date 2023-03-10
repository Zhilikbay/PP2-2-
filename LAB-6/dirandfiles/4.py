filename = '\AZ\PP2(2)\LAB-6\dirandfiles\q.txt'
with open(filename, 'r') as file:
    line_count = 0
    for line in file:
        line_count += 1

print(f'The file {filename} has {line_count} lines.')