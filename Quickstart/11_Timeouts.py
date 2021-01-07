import requests

# timeout somente afeta o processo da conexão, não o download do corpo da resposta.
requests.get('http://github.com', timeout=0.001)