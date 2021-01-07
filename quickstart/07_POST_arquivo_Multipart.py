import requests

url = 'http://httpbin.org/post'

# Você pode definir o nome do arquivo explicitamente:
# files = {'file': ('report.xls', open('report.xls', 'rb'))}

# Se você quiser, você pode enviar strings para serem recebidas como arquivos:
# files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}

files = {'file': open('07_text.txt', 'rb')}

r = requests.post(url, files=files)

print(r.text)