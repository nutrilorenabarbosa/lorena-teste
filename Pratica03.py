# 1 - Classificador de idade 

idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Classificação: Criança")
elif idade <= 17:
    print("Classificação: Adolescente")
elif idade <= 59:
    print("Classificação: Adulto")
else:
    print("Classificação: Idoso")

    # 2 - Calculadora de IMC

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso/(altura ** 2)

print(f"Seu IMC é:{imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obeso")

    # 3 - Conversor de temperatura 

temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C/F/K): ").upper()
destino = input("Digite a unidade de destino (C/F/K): ").upper()

resultado = None

if origem == "C":
    if destino == "F":
        resultado = (temp * 9/5) + 32
    elif destino == "K":
        resultado = temp + 273.15
    else:
        resultado = temp

elif origem == "F":
    if destino == "C":
        resultado = (temp - 32) * 5/9
    elif destino == "K":
        resultado = (temp - 32) * 5/9 + 273.15
    else:
        resultado = temp

elif origem == "K":
    if destino == "C":
        resultado = temp - 273.15
    elif destino == "F":
        resultado = (temp - 273.15) * 9/5 + 32
    else:
        resultado = temp

else:
    print("Unidade de origem inválida!")

if resultado is not None:
    print(f"Temperatura convertida: {round(resultado, 2)}°{destino}")

    # 4 - Verificador de ano bissexto 

    ano = int(input("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")