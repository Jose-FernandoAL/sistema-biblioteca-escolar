from datetime import date, datetime

from alunos import buscar_aluno_por_id
from livros import buscar_livro_por_id


def gerar_proximo_id(emprestimos):
    if not emprestimos:
        return 1

    maior_id = max(emprestimo["id"] for emprestimo in emprestimos)
    return maior_id + 1


def data_hoje():
    return date.today().isoformat()


def data_valida(data_texto):
    try:
        datetime.strptime(data_texto, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def aluno_ja_tem_livro_emprestado(dados, aluno_id, livro_id):
    for emprestimo in dados["emprestimos"]:
        mesmo_aluno = emprestimo["aluno_id"] == aluno_id
        mesmo_livro = emprestimo["livro_id"] == livro_id
        esta_ativo = emprestimo["status"] == "emprestado"

        if mesmo_aluno and mesmo_livro and esta_ativo:
            return True

    return False


def registrar_emprestimo(dados, aluno_id, livro_id, data_limite):
    try:
        aluno_id = int(aluno_id)
        livro_id = int(livro_id)
    except ValueError:
        return False, "ID do aluno e ID do livro devem ser números."

    if not data_valida(data_limite):
        return False, "Data limite inválida. Use o formato AAAA-MM-DD."

    aluno = buscar_aluno_por_id(dados, aluno_id)

    if aluno is None:
        return False, "Aluno não encontrado."

    if not aluno.get("ativo", True):
        return False, "Aluno está inativo."

    livro = buscar_livro_por_id(dados, livro_id)

    if livro is None:
        return False, "Livro não encontrado."

    if livro["quantidade_disponivel"] <= 0:
        return False, "Livro indisponível para empréstimo."

    if aluno_ja_tem_livro_emprestado(dados, aluno_id, livro_id):
        return False, "Esse aluno já possui empréstimo ativo desse livro."

    emprestimos = dados["emprestimos"]

    novo_emprestimo = {
        "id": gerar_proximo_id(emprestimos),
        "aluno_id": aluno_id,
        "livro_id": livro_id,
        "data_emprestimo": data_hoje(),
        "data_limite": data_limite,
        "data_devolucao": None,
        "status": "emprestado"
    }

    emprestimos.append(novo_emprestimo)

    livro["quantidade_disponivel"] -= 1

    return True, novo_emprestimo


def buscar_emprestimo_por_id(dados, emprestimo_id):
    try:
        emprestimo_id = int(emprestimo_id)
    except ValueError:
        return None

    for emprestimo in dados["emprestimos"]:
        if emprestimo["id"] == emprestimo_id:
            return emprestimo

    return None


def devolver_livro(dados, emprestimo_id):
    emprestimo = buscar_emprestimo_por_id(dados, emprestimo_id)

    if emprestimo is None:
        return False, "Empréstimo não encontrado."

    if emprestimo["status"] == "devolvido":
        return False, "Esse empréstimo já foi devolvido."

    livro = buscar_livro_por_id(dados, emprestimo["livro_id"])

    if livro is None:
        return False, "Livro relacionado ao empréstimo não foi encontrado."

    emprestimo["status"] = "devolvido"
    emprestimo["data_devolucao"] = data_hoje()

    if livro["quantidade_disponivel"] < livro["quantidade_total"]:
        livro["quantidade_disponivel"] += 1

    return True, emprestimo


def listar_emprestimos(dados, apenas_ativos=False):
    if apenas_ativos:
        return [
            emprestimo
            for emprestimo in dados["emprestimos"]
            if emprestimo["status"] == "emprestado"
        ]

    return dados["emprestimos"]