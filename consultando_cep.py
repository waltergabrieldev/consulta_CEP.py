import requests

def consulta(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados_endereco = resposta.json()
        if "erro" in dados_endereco:
            sinal = 2
            resposta = "CEP inválido!"
            return sinal, resposta
        else:
            sinal = 1
            return sinal, dados_endereco 
    else:
        sinal = 3
        resposta = "Erro na pesquisa!"
        return sinal, resposta
    
    
