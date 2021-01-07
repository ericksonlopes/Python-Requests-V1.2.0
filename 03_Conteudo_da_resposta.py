import requests

r = requests.get('https://github.com/timeline.json')

print(r.text)

# mudando codificação
r.encoding = 'md5'

# exibindo codificação
print(r.encoding)

