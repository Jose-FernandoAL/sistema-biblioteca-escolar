import json
import os


CAMINHO_DADOS = os.path.join("data", "dados.json")


ESTRUTURA_INICIAL = {
    "alunos": [],
    "livros": [],
    "emprestimos": []
}


def garantir_arquivo():
    """
    Garante que a pasta data/ e o arquivo dados.json existam.
    Se não existirem, cria com a estrutura inicial.
    """
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(CAMINHO_DADOS):
        salvar_dados(ESTRUTURA_INICIAL)


def carregar_dados():
    """
    Carrega os dados do arquivo JSON.
    Se o arquivo não existir, cria antes.
    """
    garantir_arquivo()

    with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_dados(dados):
    """
    Salva os dados no arquivo JSON.
    """
    os.makedirs("data", exist_ok=True)

    with open(CAMINHO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)