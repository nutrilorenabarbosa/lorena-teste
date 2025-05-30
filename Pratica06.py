# 1 - Gerador de senha aleatório

import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Uso:
tamanho = int(input("Digite a quantidade de caracteres da senha: "))
senha = gerar_senha(tamanho)
print(f"Senha gerada: {senha}")

# 2 - Gerar perfil aleatório 

import requests

def gerar_perfil_aleatorio():
    url = "https://randomuser.me/api/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        usuario = data['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    else:
        print("Erro ao acessar a API.")

# Uso:
gerar_perfil_aleatorio()

# 3 - Consulta de endereco

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if 'erro' in data:
            print("CEP não encontrado.")
        else:
            print(f"Logradouro: {data.get('logradouro', 'N/A')}")
            print(f"Bairro: {data.get('bairro', 'N/A')}")
            print(f"Cidade: {data.get('localidade', 'N/A')}")
            print(f"Estado: {data.get('uf', 'N/A')}")
    else:
        print("Erro ao acessar a API.")

# Uso:
cep = input("Digite o CEP (somente números): ")
consultar_cep(cep)

# 4 - Cotacao de moeda 

import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        chave = f"{moeda}BRL"

        if chave in data:
            cotacao = data[chave]
            print(f"Moeda: {cotacao['name']}")
            print(f"Valor Atual: R$ {cotacao['bid']}")
            print(f"Máximo: R$ {cotacao['high']}")
            print(f"Mínimo: R$ {cotacao['low']}")
            print(f"Última Atualização: {cotacao['create_date']}")
        else:
            print("Moeda não encontrada.")
    else:
        print("Erro ao acessar a API.")

# Uso:
moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
consultar_cotacao(moeda)


