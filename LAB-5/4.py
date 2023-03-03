import re
def f(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found '
        else:
                return('Not found')
a=input()
print(f(a))