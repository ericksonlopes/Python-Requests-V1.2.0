import requests

bytes = requests.get('https://github.com/timeline.json')

# Você pode acessar o corpo da resposta como bytes, para requisições que não são textos:
print(bytes.content, '\n')


# Respota JSON
json = requests.get('https://github.com/timeline.json')
print(json.json(), '\n')


