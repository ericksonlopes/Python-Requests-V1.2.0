import requests

r = requests.get('https://github.com/timeline.json')

put = requests.put("http://httpbin.org/put")

delete = requests.delete("http://httpbin.org/delete")

head = requests.head("http://httpbin.org/get")

options = requests.options("http://httpbin.org/get")