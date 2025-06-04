import json

def escrever_json(nome_arquivo, dados):
    """
    Escreve dados (um dicionário ou lista de dicionários) em um arquivo JSON.
    """
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            # json.dump() escreve o dicionário 'dados' no 'arquivo'
            # indent=4 torna o JSON legível com indentação
            # ensure_ascii=False permite caracteres especiais (acentos, ç)
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print(f"Dados salvos com sucesso em '{nome_arquivo}'")
    except IOError as e:
        print(f"Erro de I/O ao escrever no arquivo: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao escrever: {e}")

def ler_json(nome_arquivo):
    """
    Lê dados de um arquivo JSON e os retorna.
    """
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # json.load() lê os dados do 'arquivo' e os converte em um dicionário/lista Python
            dados = json.load(arquivo)
        print(f"Dados lidos com sucesso de '{nome_arquivo}'")
        return dados
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro: Problema ao decodificar o JSON do arquivo '{nome_arquivo}'. O arquivo pode estar corrompido ou mal formatado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler: {e}")
        return None
    
    pessoa_solteira = {
    "nome": "Mariana Silva",
    "idade": 28,
    "cidade": "Belo Horizonte"
}
    lista_pessoas = [
    {"nome": "João Pedro", "idade": 30, "cidade": "São Paulo"},
    {"nome": "Ana Clara", "idade": 25, "cidade": "Rio de Janeiro"},
    {"nome": "Carlos Eduardo", "idade": 42, "cidade": "Curitiba"}
]
    nome_arquivo_json_pessoa = 'pessoa.json'
nome_arquivo_json_lista = 'lista_pessoas.json'

print("\n--- Escrevendo dados ---")
escrever_json(nome_arquivo_json_pessoa, pessoa_solteira)
escrever_json(nome_arquivo_json_lista, lista_pessoas)

print("\n--- Lendo dados ---")
dados_lidos_pessoa = ler_json(nome_arquivo_json_pessoa)
if dados_lidos_pessoa:
    print("\nDados da pessoa:")
    print(dados_lidos_pessoa)

    dados_lidos_lista = ler_json(nome_arquivo_json_lista)
if dados_lidos_lista:
    print("\nDados da lista de pessoas:")
    for p in dados_lidos_lista:
        print(f"  Nome: {p['nome']}, Idade: {p['idade']}, Cidade: {p['cidade']}")