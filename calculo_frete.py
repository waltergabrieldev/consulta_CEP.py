import json
import math

def frete(bairro):
    try:
        with open("bairros.json", "r", encoding="utf-8") as file:  
            bairros = json.load(file)
            for regionais, bairros in bairros.items():
                if bairro in bairros:
                        preço_frete = int(regionais[9:]) * 1.5 + 10
                        return (math.floor(preço_frete))        
    except FileNotFoundError:
        print("Erro: O arquivo 'bairros.json' não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro: O arquivo 'bairros.json' está corrompido ou mal formatado.")
    except UnicodeDecodeError:
        print("Erro: Problema de codificação ao ler 'bairros.json'. Tente salvar o arquivo em UTF-8.")
