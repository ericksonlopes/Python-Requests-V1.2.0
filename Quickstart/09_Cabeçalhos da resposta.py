# Nós podemos visualizar os cabeçalhos da resposta do servidor usando um dicionário Python:

import requests

r = requests.get('http://httpbin.org/get')

print(r.headers['Date'])

print(r.headers.get('content-type'))
