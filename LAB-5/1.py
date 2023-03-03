import re
def pat(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'Found!'
        else:
                return('Not found')
a= input()
print(pat(a))