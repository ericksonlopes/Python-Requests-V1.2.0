import requests

s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

r = s.get("http://httpbin.org/cookies")

print(r.text)

# Sessões também podem ser usadas para prover dados padrões para os métodos de requisição. Isto é feito
# fornecendo dados para as propriedades de um objeto session:

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-text': 'true'})

s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})

print(s)