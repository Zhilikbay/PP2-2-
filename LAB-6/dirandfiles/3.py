import os

path = '\AZ\PP2(2)\LAB-6\dirandfiles\q.txt'

if os.path.exists(path):
    print(f'{path} exists')
    dirname, filename = os.path.split(path)
    print(f'directory: {dirname}')
    print(f'filename: {filename}')
else:
    print(f'{path} does not exist')