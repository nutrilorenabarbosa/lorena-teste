# Taxa de cambio

Dolar = 5.20
Euro = 6.15
valor_reais = 100.0

valor_em_dolar = valor_reais / Dolar
valor_em_euro = valor_reais / Euro

print(f"O valor do dolar é:, {valor_em_euro:.2f}")
print(f"O valor do euro é:, {valor_em_dolar:.2f}")
print(f"Valor em reais: {valor_reais:.2f}")

# Calcular desconto e preco final 

Produto = "Camiseta"
Preco_produto = 50
Desconto = 20

Valor_desconto = Preco_produto * (Desconto/100)
Valor_final = Preco_produto - Desconto

print(f"O valor do desconto é:, {Valor_desconto:.2f}")
print(f"O valor da camiseta com desconto é:, {Valor_final:.2f}")

# Média escolar 

Nota1 = 7.5
Nota2 = 8.0
Nota3 = 6.5

Média_nota = (Nota1 + Nota2 + Nota3) / 3

print(f"A nota 1 é:, {Nota1}")
print(f"A nota 2 é:, {Nota2}")
print(f"A nota 3 é:, {Nota3}")
print(f"A médias escolar é:, {Média_nota:.2f}")

Lorena = input("Olá, qual o seu nome?")
print("Nome inválido")

idade = int(input("Qual a sua idade?"))
if idade < 13:
    print("Crianca")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")

