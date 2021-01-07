import requests

r = requests.get('http://httpbin.org/post')
print(r.status_code)


if r.status_code == requests.codes.ok:
    print('Status code correto', r.status_code)
else:
    print('Status code incorreto', r.status_code)
