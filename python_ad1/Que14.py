import requests
r = requests.get("https://www.google.com/")
print(r.text)
print(r.url)