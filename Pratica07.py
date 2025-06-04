# Crie um script em Python que escreva dados em um arquivo CSV 

import csv 

def escrever_csv(nome_arquivo, dados):

    colunas = ["Nome", "Idade", "Cidade"]

    with open(nome_arquivo, mode="w", newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(dados)

    print(f"Arquivo '{nome_arquivo}'criado com sucesso")

dados_pessoas = [
{"Nome": "Lorena", "Idade": 34, "Cidade": "Recife"},
{"Nome": "Douglas", "Idade": 35, "Cidade": "Barreiros"},
{"Nome": "Bailey", "Idade": 2, "Cidade": "Itacaré"}
]
escrever_csv("pesoas.csv", dados_pessoas)

# Crie um script em Python que leia um arquivo CSV e exiba os dados na tela.

import csv

# Nome do arquivo CSV
nome_arquivo = 'pessoas.csv'

# Lê o arquivo CSV e exibe os dados
try:
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)

        print(f"\n{'Nome':<20}{'Idade':<10}{'Cidade':<20}")
        print("-" * 50)

        for linha in leitor:
            nome = linha['Nome']
            idade = linha['Idade']
            cidade = linha['Cidade']
            print(f"{nome:<20}{idade:<10}{cidade:<20}")

except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")

