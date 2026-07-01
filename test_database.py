from database import carregar_dados, salvar_dados

dados = carregar_dados()

print(dados)

dados["alunos"].append({
    "id": 1,
    "nome": "Aluno Teste",
    "turma": "6º A",
    "matricula": "",
    "ativo": True
})

salvar_dados(dados)

print("Dados salvos com sucesso.")