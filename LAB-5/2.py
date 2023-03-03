import re
def f(text):
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return 'Found'
        else:
                return('Not found')
        
a=input()
print(f(a))