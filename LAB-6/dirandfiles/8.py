import os

filename = '\AZ\PP2(2)\LAB-6\dirandfiles\c.txt'

if os.access(filename, os.F_OK):
    if os.access(filename, os.R_OK) and os.access(filename, os.W_OK):
        os.remove(filename)
        print(f'The file {filename} has been deleted.')
    else:
        print(f'Error: insufficient permissions to delete {filename}.')
else:
    print(f'Error: {filename} does not exist.')