import requests

r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')

print(r.headers, '\n')

print(r.request.headers)

