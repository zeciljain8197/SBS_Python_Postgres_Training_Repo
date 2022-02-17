import requests

r = requests.get("http://skyscendbs.com")
print(r, type(r))
print(r.text)
print(r.url)

user_dict = {
    "jsonrpc": "2.0",
    "params": {
        "db": "pharmacy",
        "login": "admin",
        "password": "a"
    }
}

r = requests.post('http://0.0.0.0:8000/web/session/authenticate', json=user_dict)
print(r.json())
