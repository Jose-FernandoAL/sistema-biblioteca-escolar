from database import carregar_dados, salvar_dados

from alunos import (
    cadastrar_aluno,
    listar_alunos,
    buscar_alunos_por_nome
)

from livros import (
    cadastrar_livro,
    listar_livros,
    buscar_livros_por_titulo
)

from emprestimos import (
    registrar_emprestimo,
    devolver_livro,
    listar_emprestimos
)


def pausar():
    input("\nPressione Enter para continuar...")


def mostrar_menu():
    print("\n" + "=" * 40)
    print("SISTEMA DE BIBLIOTECA")
    print("=" * 40)
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Buscar aluno")
    print("4. Cadastrar livro")
    print("5. Listar livros")
    print("6. Buscar livro")
    print("7. Registrar empréstimo")
    print("8. Devolver livro")
    print("9. Listar empréstimos ativos")
    print("10. Listar todos os empréstimos")
    print("0. Sair")
    print("=" * 40)


def opcao_cadastrar_aluno(dados):
    nome = input("Nome do aluno: ")
    turma = input("Turma: ")
    matricula = input("Matrícula (opcional): ")

    sucesso, resultado = cadastrar_aluno(
        dados,
        nome=nome,
        turma=turma,
        matricula=matricula
    )

    if sucesso:
        salvar_dados(dados)
        print("\nAluno cadastrado com sucesso!")
        print(resultado)
    else:
        print("\nErro:", resultado)


def opcao_listar_alunos(dados):
    alunos = listar_alunos(dados)

    if not alunos:
        print("\nNenhum aluno cadastrado.")
        return

    print("\nAlunos cadastrados:")
    for aluno in alunos:
        print(
            f'ID: {aluno["id"]} | '
            f'Nome: {aluno["nome"]} | '
            f'Turma: {aluno["turma"]} | '
            f'Matrícula: {aluno["matricula"]}'
        )


def opcao_buscar_aluno(dados):
    nome = input("Digite parte do nome do aluno: ")
    encontrados = buscar_alunos_por_nome(dados, nome)

    if not encontrados:
        print("\nNenhum aluno encontrado.")
        return

    print("\nAlunos encontrados:")
    for aluno in encontrados:
        print(
            f'ID: {aluno["id"]} | '
            f'Nome: {aluno["nome"]} | '
            f'Turma: {aluno["turma"]}'
        )


def opcao_cadastrar_livro(dados):
    titulo = input("Título: ")
    autor = input("Autor: ")
    categoria = input("Categoria: ")
    quantidade = input("Quantidade: ")
    estante = input("Estante (A, B, C...): ")
    prateleira = input("Prateleira (1 a 5): ")
    isbn = input("ISBN (opcional): ")

    sucesso, resultado = cadastrar_livro(
        dados,
        titulo=titulo,
        autor=autor,
        categoria=categoria,
        quantidade=quantidade,
        estante=estante,
        prateleira=prateleira,
        isbn=isbn
    )

    if sucesso:
        salvar_dados(dados)
        print("\nLivro cadastrado com sucesso!")
        print(resultado)
    else:
        print("\nErro:", resultado)


def opcao_listar_livros(dados):
    livros = listar_livros(dados)

    if not livros:
        print("\nNenhum livro cadastrado.")
        return

    print("\nLivros cadastrados:")
    for livro in livros:
        print(
            f'ID: {livro["id"]} | '
            f'Título: {livro["titulo"]} | '
            f'Autor: {livro["autor"]} | '
            f'Categoria: {livro["categoria"]} | '
            f'Disponível: {livro["quantidade_disponivel"]}/{livro["quantidade_total"]} | '
            f'Etiqueta: {livro["etiqueta"]}'
        )


def opcao_buscar_livro(dados):
    titulo = input("Digite parte do título do livro: ")
    encontrados = buscar_livros_por_titulo(dados, titulo)

    if not encontrados:
        print("\nNenhum livro encontrado.")
        return

    print("\nLivros encontrados:")
    for livro in encontrados:
        print(
            f'ID: {livro["id"]} | '
            f'Título: {livro["titulo"]} | '
            f'Autor: {livro["autor"]} | '
            f'Disponível: {livro["quantidade_disponivel"]}/{livro["quantidade_total"]} | '
            f'Etiqueta: {livro["etiqueta"]}'
        )


def opcao_registrar_emprestimo(dados):
    print("\nAlunos:")
    for aluno in listar_alunos(dados):
        print(f'ID: {aluno["id"]} | {aluno["nome"]} | {aluno["turma"]}')

    print("\nLivros:")
    for livro in listar_livros(dados):
        print(
            f'ID: {livro["id"]} | '
            f'{livro["titulo"]} | '
            f'Disponível: {livro["quantidade_disponivel"]}/{livro["quantidade_total"]}'
        )

    aluno_id = input("\nID do aluno: ")
    livro_id = input("ID do livro: ")
    data_limite = input("Data limite de devolução (AAAA-MM-DD): ")

    sucesso, resultado = registrar_emprestimo(
        dados,
        aluno_id=aluno_id,
        livro_id=livro_id,
        data_limite=data_limite
    )

    if sucesso:
        salvar_dados(dados)
        print("\nEmpréstimo registrado com sucesso!")
        print(resultado)
    else:
        print("\nErro:", resultado)


def opcao_devolver_livro(dados):
    ativos = listar_emprestimos(dados, apenas_ativos=True)

    if not ativos:
        print("\nNenhum empréstimo ativo.")
        return

    print("\nEmpréstimos ativos:")
    for emprestimo in ativos:
        print(
            f'ID: {emprestimo["id"]} | '
            f'Aluno ID: {emprestimo["aluno_id"]} | '
            f'Livro ID: {emprestimo["livro_id"]} | '
            f'Data limite: {emprestimo["data_limite"]}'
        )

    emprestimo_id = input("\nID do empréstimo para devolver: ")

    sucesso, resultado = devolver_livro(dados, emprestimo_id)

    if sucesso:
        salvar_dados(dados)
        print("\nLivro devolvido com sucesso!")
        print(resultado)
    else:
        print("\nErro:", resultado)


def opcao_listar_emprestimos(dados, apenas_ativos=False):
    emprestimos = listar_emprestimos(dados, apenas_ativos=apenas_ativos)

    if not emprestimos:
        print("\nNenhum empréstimo encontrado.")
        return

    print("\nEmpréstimos:")
    for emprestimo in emprestimos:
        print(
            f'ID: {emprestimo["id"]} | '
            f'Aluno ID: {emprestimo["aluno_id"]} | '
            f'Livro ID: {emprestimo["livro_id"]} | '
            f'Empréstimo: {emprestimo["data_emprestimo"]} | '
            f'Limite: {emprestimo["data_limite"]} | '
            f'Devolução: {emprestimo["data_devolucao"]} | '
            f'Status: {emprestimo["status"]}'
        )


def main():
    dados = carregar_dados()

    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            opcao_cadastrar_aluno(dados)

        elif opcao == "2":
            opcao_listar_alunos(dados)

        elif opcao == "3":
            opcao_buscar_aluno(dados)

        elif opcao == "4":
            opcao_cadastrar_livro(dados)

        elif opcao == "5":
            opcao_listar_livros(dados)

        elif opcao == "6":
            opcao_buscar_livro(dados)

        elif opcao == "7":
            opcao_registrar_emprestimo(dados)

        elif opcao == "8":
            opcao_devolver_livro(dados)

        elif opcao == "9":
            opcao_listar_emprestimos(dados, apenas_ativos=True)

        elif opcao == "10":
            opcao_listar_emprestimos(dados, apenas_ativos=False)

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")

        pausar()


if __name__ == "__main__":
    main()