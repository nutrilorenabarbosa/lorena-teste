# 1 - Conversor de moeda

Valor_em_reais = 100.00
Taxa_do_dolar = 5.20
Taxa_do_euro = 6.15

valor_em_dolares = Valor_em_reais/ Taxa_do_dolar
valor_em_euros = Valor_em_reais/ Taxa_do_euro

print(f"Valor em reais: R$ {Valor_em_reais:.2f}")
print(f"Valor em dolares: US$ {valor_em_dolares:.2f}")
print(f"Valor em euros: {valor_em_euros:.2f}")


# 2 - Calculadora de desconto

Nome_do_produto = "Camiseta"
preco_original = 50.00
Porcentagem_de_desconto = 20

valor_desconto = preco_original * (Porcentagem_de_desconto/100)
preco_final = preco_original - valor_desconto 

print(f"Produto: {Nome_do_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: {Porcentagem_de_desconto:.2f}")
print(f"valor do desconto: R$ {valor_desconto:.2f}")
print(f"preco final: R$ {preco_final:.2f}")

# 3 - Calculadora de média escolar

Nota_1 = 7.5
Nota_2 = 8.0
Nota_3 = 6.5

média = (Nota_1 + Nota_2 + Nota_3)/ 3

print(f"nota 1: {Nota_1}")
print(f"nota 2: {Nota_2}")
print(f"nota 3: {Nota_3}")
print(f"Média final: {média:.2f}")

# 4 - Calculadora de consumo de combustível 

Distancia_percorrida = 300
Combustivel_gasto = 25 
consumo_médio = Distancia_percorrida / Combustivel_gasto

print(f"Distancia percorrida: {Distancia_percorrida} quilometros")
print(f"combustivel gasto:{combustivel_gasto} litros")
print(f"consumo médio:{consumo_médio:.2f}km/l")
