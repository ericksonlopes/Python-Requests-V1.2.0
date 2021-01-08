import requests


def gen():
    yield 'olá'
    yield 'você'


requests.post('http://some.url/chunked', data=gen())
