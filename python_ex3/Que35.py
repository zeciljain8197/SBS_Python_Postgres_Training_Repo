import re

regex = re.compile('(http|https)://(www.)')
res = regex.match('https://www.google.com')
print(res)
