import requests

# da erro por nao ter dominio
# print(requests.get('https://kennethreitz.com', verify=True))
# print(requests.get('https://kennethreitz.com', verify=False))

print(requests.get('https://github.com', verify=True))

# Por padrão, verify está definido como True. A opção verify é somente aplicada para certificados de hosts.
# Você também pode especificar um certificado local para ser usado como certificado do lado do cliente, como
# um único arquivo (contendo a chave privada e o certificado) ou como uma tupla do caminho de ambos arquivos:

print(requests.get('https://kennethreitz.com', cert=('/path/server.crt', '/path/key')))

print(requests.get('https://kennethreitz.com', cert='/wrong_path/server.pem'))