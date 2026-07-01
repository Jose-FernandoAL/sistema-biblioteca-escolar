from database import carregar_dados, salvar_dados
from livros import cadastrar_livro, listar_livros, buscar_livros_por_titulo

dados = carregar_dados()

sucesso, resultado = cadastrar_livro(
    dados,
    titulo="Dom Casmurro",
    autor="Machado de Assis",
    categoria="Literatura",
    quantidade=3,
    estante="B",
    prateleira=2,
    isbn=""
)

if sucesso:
    salvar_dados(dados)
    print("Livro cadastrado:")
    print(resultado)
else:
    print("Erro:")
    print(resultado)

print("\nLista de livros:")
for livro in listar_livros(dados):
    print(livro)

print("\nBusca por Dom:")
print(buscar_livros_por_titulo(dados, "Dom"))