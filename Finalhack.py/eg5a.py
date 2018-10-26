import json
import requests

r = requests.get('https://jsonplaceholder.typicode.com/users')
r.json()
print (r.json())
