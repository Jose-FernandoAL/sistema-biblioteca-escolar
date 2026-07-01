from database import carregar_dados, salvar_dados
from alunos import cadastrar_aluno, listar_alunos, buscar_alunos_por_nome

dados = carregar_dados()

sucesso, resultado = cadastrar_aluno(
    dados,
    nome="Maria Eduarda Silva",
    turma="6º A",
    matricula="2026001"
)

if sucesso:
    salvar_dados(dados)
    print("Aluno cadastrado:")
    print(resultado)
else:
    print("Erro:")
    print(resultado)

print("\nLista de alunos:")
for aluno in listar_alunos(dados):
    print(aluno)

print("\nBusca por Maria:")
print(buscar_alunos_por_nome(dados, "Maria"))