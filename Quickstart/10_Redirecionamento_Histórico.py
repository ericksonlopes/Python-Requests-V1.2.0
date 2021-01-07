
# Requests irá automaticamente realizar redirecionamentos quando utilizados os verbos GET e OPTIONS.

# GitHub redireciona todas as requisições HTTP para HTTPS. Nós podemos usar o método history do objeto Response
# para acompanhar o redirecionamento. Vamos ver o que o GitHub faz:

import requests

r = requests.get('http://github.com')

print(r.url)

print(r.status_code)

print(r.history, '\n')

r = requests.get('http://github.com', allow_redirects=False)

print(r.status_code)

print(r.history, '\n')

# Se você estiver usando POST, PUT, PATCH, DELETE ou HEAD, você pode habilitar o redirecionamento também:

r = requests.post('http://github.com', allow_redirects=True)

print(r.status_code)

print(r.history, '\n')