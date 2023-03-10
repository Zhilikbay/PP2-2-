f = '\AZ\PP2(2)\LAB-6\dirandfiles\s.txt'
d = '\AZ\PP2(2)\LAB-6\dirandfiles\c.txt'

with open(f, 'r') as source:
    with open(d, 'w') as destination:
        destination.write(source.read())

print(f'The contents of {f} have been copied to {d}.')