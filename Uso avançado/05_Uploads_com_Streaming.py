import requests

with open('massive-body') as f:
    requests.post('http://some.url/streamed', data=f)
