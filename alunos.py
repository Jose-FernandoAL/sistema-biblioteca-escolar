def gerar_proximo_id(alunos):
    if not alunos:
        return 1

    maior_id = max(aluno["id"] for aluno in alunos)
    return maior_id + 1


def aluno_existe(alunos, nome, turma):
    nome = nome.strip().lower()
    turma = turma.strip().lower()

    for aluno in alunos:
        mesmo_nome = aluno["nome"].strip().lower() == nome
        mesma_turma = aluno["turma"].strip().lower() == turma

        if mesmo_nome and mesma_turma and aluno.get("ativo", True):
            return True

    return False


def cadastrar_aluno(dados, nome, turma, matricula=""):
    nome = nome.strip()
    turma = turma.strip()
    matricula = matricula.strip()

    if not nome:
        return False, "Nome do aluno é obrigatório."

    if not turma:
        return False, "Turma é obrigatória."

    alunos = dados["alunos"]

    if aluno_existe(alunos, nome, turma):
        return False, "Aluno já cadastrado nessa turma."

    novo_aluno = {
        "id": gerar_proximo_id(alunos),
        "nome": nome,
        "turma": turma,
        "matricula": matricula,
        "ativo": True
    }

    alunos.append(novo_aluno)

    return True, novo_aluno


def listar_alunos(dados, apenas_ativos=True):
    alunos = dados["alunos"]

    if apenas_ativos:
        return [aluno for aluno in alunos if aluno.get("ativo", True)]

    return alunos


def buscar_aluno_por_id(dados, aluno_id):
    for aluno in dados["alunos"]:
        if aluno["id"] == aluno_id:
            return aluno

    return None


def buscar_alunos_por_nome(dados, nome):
    nome = nome.strip().lower()

    encontrados = []

    for aluno in dados["alunos"]:
        if nome in aluno["nome"].lower():
            encontrados.append(aluno)

    return encontrados