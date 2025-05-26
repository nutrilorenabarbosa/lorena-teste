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