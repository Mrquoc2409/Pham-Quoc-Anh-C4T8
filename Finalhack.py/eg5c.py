import json
import requests

r = requests.get('https://jsonplaceholder.typicode.com/users')
data = r.json()
n = input('The username you want to find')
found = False
user = None
for d in data:
    
    if d['username'] == n:
        user = d
        found = True
        break
    else:
        found = False

if found == False:
    print("not found")
else: 
    print(user)