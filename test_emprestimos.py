from database import carregar_dados, salvar_dados
from emprestimos import (
    registrar_emprestimo,
    devolver_livro,
    listar_emprestimos
)

dados = carregar_dados()

print("Alunos cadastrados:")
for aluno in dados["alunos"]:
    print(aluno)

print("\nLivros cadastrados:")
for livro in dados["livros"]:
    print(livro)

print("\nRegistrando empréstimo...")

sucesso, resultado = registrar_emprestimo(
    dados,
    aluno_id=1,
    livro_id=1,
    data_limite="2026-07-08"
)

if sucesso:
    salvar_dados(dados)
    print("Empréstimo registrado:")
    print(resultado)
else:
    print("Erro:")
    print(resultado)

print("\nEmpréstimos ativos:")
for emprestimo in listar_emprestimos(dados, apenas_ativos=True):
    print(emprestimo)