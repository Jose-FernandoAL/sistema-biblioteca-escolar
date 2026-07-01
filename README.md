# Sistema Biblioteca Escolar

Sistema de gerenciamento de biblioteca escolar desenvolvido em Python, com foco no cadastro de alunos, cadastro de livros, controle de empréstimos, devoluções e organização dos exemplares por etiquetas.

O projeto foi desenvolvido inicialmente em versão de terminal, priorizando a lógica do sistema, organização modular e persistência dos dados em JSON.

---

## Objetivo

O objetivo do sistema é facilitar o controle de uma biblioteca escolar, permitindo registrar alunos, livros e empréstimos de forma organizada.

A ideia é evoluir futuramente para uma versão com interface gráfica, geração de relatórios, etiquetas imprimíveis e possível leitura de códigos para agilizar empréstimos e devoluções.

---

## Funcionalidades atuais

* Cadastro de alunos
* Bloqueio de alunos duplicados na mesma turma
* Cadastro de livros
* Bloqueio de livros duplicados por título e autor
* Registro de quantidade total e quantidade disponível
* Geração automática de etiqueta para cada livro
* Registro de empréstimos
* Controle de data de empréstimo e data limite de devolução
* Devolução de livros
* Atualização automática da quantidade disponível
* Listagem de alunos
* Listagem de livros
* Busca de alunos por nome
* Busca de livros por título
* Listagem de empréstimos ativos
* Listagem de todos os empréstimos
* Persistência dos dados em arquivo JSON

---

## Exemplo de etiqueta

Cada livro recebe uma etiqueta gerada automaticamente a partir da categoria, estante, prateleira e ID do livro.

Exemplo:

```text
LIT-B-02-0001
```

Significado:

```text
LIT  → Categoria Literatura
B    → Estante B
02   → Prateleira 2
0001 → ID do livro
```

Essa estrutura foi pensada para permitir, no futuro, a integração com códigos impressos ou escaneáveis.

---

## Tecnologias utilizadas

* Python 3
* JSON
* Programação modular
* Terminal/CLI

---

## Estrutura do projeto

```text
biblioteca/
│
├── main.py
├── database.py
├── alunos.py
├── livros.py
├── emprestimos.py
│
└── data/
    └── dados.json
```

---

## Responsabilidade dos módulos

### `main.py`

Controla o fluxo principal do sistema por meio de um menu no terminal.
Ele apenas chama as funções dos outros módulos.

### `database.py`

Responsável por carregar, criar e salvar os dados no arquivo JSON.

### `alunos.py`

Responsável pelo cadastro, listagem e busca de alunos.

### `livros.py`

Responsável pelo cadastro, listagem, busca de livros e geração de etiquetas.

### `emprestimos.py`

Responsável pelo registro de empréstimos, devoluções e controle da quantidade disponível dos livros.

---

## Estrutura dos dados

O sistema armazena os dados em um arquivo JSON com três listas principais:

```json
{
  "alunos": [],
  "livros": [],
  "emprestimos": []
}
```

---

## Exemplo de livro cadastrado

```json
{
  "id": 1,
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "categoria": "Literatura",
  "isbn": "",
  "estante": "B",
  "prateleira": 2,
  "quantidade_total": 3,
  "quantidade_disponivel": 3,
  "etiqueta": "LIT-B-02-0001"
}
```

---

## Exemplo de aluno cadastrado

```json
{
  "id": 1,
  "nome": "Maria Eduarda Silva",
  "turma": "6º A",
  "matricula": "2026001",
  "ativo": true
}
```

---

## Exemplo de empréstimo

```json
{
  "id": 1,
  "aluno_id": 1,
  "livro_id": 1,
  "data_emprestimo": "2026-07-01",
  "data_limite": "2026-07-08",
  "data_devolucao": null,
  "status": "emprestado"
}
```

---

## Como executar

Clone o repositório:

```bash
git clone https://github.com/Jose-FernandoAL/sistema-biblioteca-escolar.git
```

Entre na pasta do projeto:

```bash
cd sistema-biblioteca-escolar
```

Execute o sistema:

```bash
python main.py
```

---

## Menu atual

```text
1. Cadastrar aluno
2. Listar alunos
3. Buscar aluno
4. Cadastrar livro
5. Listar livros
6. Buscar livro
7. Registrar empréstimo
8. Devolver livro
9. Listar empréstimos ativos
10. Listar todos os empréstimos
0. Sair
```

---

## Roadmap

Funcionalidades planejadas:

* [x] Cadastro de alunos
* [x] Cadastro de livros
* [x] Registro de empréstimos
* [x] Devolução de livros
* [x] Controle de exemplares disponíveis
* [x] Geração automática de etiquetas
* [x] Persistência em JSON
* [ ] Relatório de livros atrasados
* [ ] Listagem de empréstimos com nome do aluno e título do livro
* [ ] Interface gráfica com Tkinter
* [ ] Geração de etiquetas em PDF
* [ ] Exportação para Excel
* [ ] Leitura de código/etiqueta para empréstimos
* [ ] Histórico por aluno

---

## Objetivo futuro

A evolução do projeto é transformar a versão de terminal em uma aplicação desktop para uso em ambiente escolar, com interface simples, relatórios e suporte à impressão de etiquetas para os livros.

---

## Autor

José Fernando Alves Leite

Estudante de Ciência da Computação

GitHub: https://github.com/Jose-FernandoAL
