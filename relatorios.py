from datetime import date, datetime

from alunos import buscar_aluno_por_id
from livros import buscar_livro_por_id


def converter_data(data_texto):
    return datetime.strptime(data_texto, "%Y-%m-%d").date()

def listar_emprestimos_detalhados(dados, apenas_ativos=False):
    lista = []

    for emprestimo in dados["emprestimos"]:
        if apenas_ativos and emprestimo["status"] != "emprestado":
            continue

        aluno = buscar_aluno_por_id(dados, emprestimo["aluno_id"])
        livro = buscar_livro_por_id(dados, emprestimo["livro_id"])

        lista.append({
            "emprestimo_id": emprestimo["id"],
            "aluno_nome": aluno["nome"] if aluno else "Aluno não encontrado",
            "turma": aluno["turma"] if aluno else "",
            "livro_titulo": livro["titulo"] if livro else "Livro não encontrado",
            "livro_autor": livro["autor"] if livro else "",
            "data_emprestimo": emprestimo["data_emprestimo"],
            "data_limite": emprestimo["data_limite"],
            "data_devolucao": emprestimo["data_devolucao"],
            "status": emprestimo["status"]
        })

    return lista

def listar_emprestimos_atrasados(dados):
    hoje = date.today()
    atrasados = []

    for emprestimo in dados["emprestimos"]:
        if emprestimo["status"] != "emprestado":
            continue

        data_limite = converter_data(emprestimo["data_limite"])

        if data_limite < hoje:
            aluno = buscar_aluno_por_id(dados, emprestimo["aluno_id"])
            livro = buscar_livro_por_id(dados, emprestimo["livro_id"])

            atrasados.append({
                "emprestimo_id": emprestimo["id"],
                "aluno_id": emprestimo["aluno_id"],
                "aluno_nome": aluno["nome"] if aluno else "Aluno não encontrado",
                "turma": aluno["turma"] if aluno else "",
                "livro_id": emprestimo["livro_id"],
                "livro_titulo": livro["titulo"] if livro else "Livro não encontrado",
                "data_emprestimo": emprestimo["data_emprestimo"],
                "data_limite": emprestimo["data_limite"],
                "dias_atraso": (hoje - data_limite).days
            })

    return atrasados