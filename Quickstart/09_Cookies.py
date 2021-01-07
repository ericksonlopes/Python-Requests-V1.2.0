import requests

url = 'http://example.com/some/cookie/setting/url'

r = requests.get(url)

# Se uma resposta contém alguns cookies, você tem acesso rápido a eles
print(r.cookies)

# Para enviar seus próprios cookies par ao servidor, você pode usar o parâmetro cookies:
url = 'http://httpbin.org/cookies'

cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)

print(r.text)