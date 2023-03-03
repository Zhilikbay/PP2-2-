import re
def f(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found'
        else:
                return('Not Found')

a=input()
print(f(a))