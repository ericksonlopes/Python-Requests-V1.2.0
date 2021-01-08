# Por padrão, quando você faz uma requisição, o corpo da resposta é baixado imediatamente. Você pode mudar este
# comportamento e prevenir o download do corpo da resposta até que você acesse o atribute Response.content com o
# parâmetro stream:
import requests

tarball_url = 'https://github.com/kennethreitz/requests/tarball/master'

r = requests.get(tarball_url, stream=True)

print(r.content)

