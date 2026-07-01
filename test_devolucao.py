from database import carregar_dados, salvar_dados
from emprestimos import devolver_livro, listar_emprestimos

dados = carregar_dados()

print("Empréstimos cadastrados:")
for emprestimo in listar_emprestimos(dados):
    print(emprestimo)

emprestimo_id = input("\nDigite o ID do empréstimo para devolver: ")

sucesso, resultado = devolver_livro(dados, emprestimo_id)

if sucesso:
    salvar_dados(dados)
    print("\nLivro devolvido com sucesso:")
    print(resultado)
else:
    print("\nErro:")
    print(resultado)

print("\nEmpréstimos após devolução:")
for emprestimo in listar_emprestimos(dados):
    print(emprestimo)