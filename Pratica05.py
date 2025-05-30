# 1 - Conta e gorjeta de um restaurante 

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

valor = float(input("Digite o valor da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta (%): "))
valor_gorjeta = calcular_gorjeta(valor, porcentagem)
print(f"Gorjeta: R$ {valor_gorjeta:.2f}")

# 2 - Verificar se uma palavra ou frase é um palídromo

def eh_palindromo(texto):
    texto = ''.join(c for c in texto.lower() if c.isalnum())  # Remove espaços e pontuações
    return texto == texto[::-1]

# Exemplo de uso:
entrada = input("Digite uma palavra ou frase: ")
if eh_palindromo(entrada):
    print("Sim")
else:
    print("Não")

# 3 - Calculo idade em dias:

from datetime import date

def idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    return idade_anos * 365  # Aproximado, sem contar anos bissextos

# Exemplo de uso:
ano = int(input("Digite seu ano de nascimento: "))
dias = idade_em_dias(ano)
print(f"Você tem aproximadamente {dias} dias de vida.")

