from database import carregar_dados
from relatorios import listar_emprestimos_atrasados

dados = carregar_dados()

atrasados = listar_emprestimos_atrasados(dados)

if not atrasados:
    print("Nenhum empréstimo atrasado.")
else:
    print("Empréstimos atrasados:")

    for item in atrasados:
        print(
            f'ID Empréstimo: {item["emprestimo_id"]} | '
            f'Aluno: {item["aluno_nome"]} | '
            f'Turma: {item["turma"]} | '
            f'Livro: {item["livro_titulo"]} | '
            f'Limite: {item["data_limite"]} | '
            f'Dias de atraso: {item["dias_atraso"]}'
        )