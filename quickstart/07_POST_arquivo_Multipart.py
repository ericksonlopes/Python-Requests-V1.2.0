import requests

url = 'http://httpbin.org/post'

files = {'file': open('07_text.txt', 'rb')}

r = requests.post(url, files=files)

print(r.text)