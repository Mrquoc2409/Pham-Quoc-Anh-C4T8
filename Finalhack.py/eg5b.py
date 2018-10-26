import json
import requests

r = requests.get('https://jsonplaceholder.typicode.com/users')
data = r.json()

for d in data:
    if d['username'] == 'Delphine':
        print (d)
    else:
        pass

