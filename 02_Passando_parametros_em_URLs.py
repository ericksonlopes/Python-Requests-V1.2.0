# Você geralmente quer mandar algum tipo de dado na query string da URL. Se você estivesse construindo a URL
# manualmente, este dado seria dado como pares chave/valor na URL após um ponto de interrogação, por exemplo
# httpbin.org/get?key=val. Requests permite que você forneça estes argumentos como um dicionário, usando o
# argumento params. Por exemplo, se você quisesse passar key1=vaue1 e key2=value2 para httpbin.org/get,
# você usaria o seguinte código:

import requests

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.get("http://httpbin.org/get", params=payload)

print(r.url)


