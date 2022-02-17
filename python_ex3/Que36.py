import re

regex = r'\b[(a-z)(0-9)._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email = 'zeciljain01@gmail.com'

if re.fullmatch(regex, email):
    print("Valid Email!")
else:
    print("Invalid!")
