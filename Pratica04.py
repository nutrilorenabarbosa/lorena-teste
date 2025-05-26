
# 1 - Calculadora em 4 operacoes (+, -, ,/)

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: divisão por zero.")
                continue
            resultado = num1 / num2
        else:
            print("Operação inválida. Tente novamente.")
            continue

        print(f"Resultado: {resultado}")
        break

    except ValueError:
        print("Erro: digite apenas números válidos.")

        # 2 - Registro de notas da turma e calculo da media

        notas = []

while True:
    entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {round(media, 2)}")
else:
    print("Nenhuma nota válida foi registrada.")


    # 3 - Verificador de senha forte 

    while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha.lower() == 'sair':
        print("Encerrado.")
        break

    tem_numero = any(char.isdigit() for char in senha)

    if len(senha) >= 8 and tem_numero:
        print("Senha forte!")
        break
    else:
        print("Senha fraca. Ela deve ter pelo menos 8 caracteres e pelo menos 1 número.")


        # 4 - Par ou impar + contador final 

        pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print("Número par.")
            pares += 1
        else:
            print("Número ímpar.")
            impares += 1
    except ValueError:
        print("Erro: isso não é um número inteiro.")

print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")