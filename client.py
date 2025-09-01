import requests

URL = "http://localhost:8000"
#requisicao GET
try:
    response_get = requests.get(URL)
    print("----Requisição GET --- ")
    print (f"status code: {response_get.status_code}")
    print("conteudo da resposta:")
    print(response_get)
