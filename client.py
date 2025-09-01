import requests

URL = "http://localhost:8000"
#requisicao GET
try:
    response_get = requests.get(URL)
    print("----Requisição GET --- ")
    print (f"status code: {response_get.status_code}")
    print("conteudo da resposta:")
    print(response_get)

# requisição POST
    data = {'nome': 'Fulano', 'idade':30}
    response_post = requests.post(URL, data=data)
    print("\n---Requisição POST---")
    print(f"Status Code: {response_post.status_code}")
    print("conteudo da resposta:")
    print(response_post.text)
except requests.exceptions.RequestsException as e:
    print(f"erro ao conectar com o servidor:{e}")
