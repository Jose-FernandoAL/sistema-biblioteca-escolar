
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

import os

PASTA_DADOS = os.path.join(os.path.expanduser("~"), "Documents", "Biblioteca")

os.makedirs(PASTA_DADOS, exist_ok=True)

ARQUIVO_LIVROS = os.path.join(PASTA_DADOS, "livros.json")
ARQUIVO_ALUNOS = os.path.join(PASTA_DADOS, "alunos.json")
ARQUIVO_EMPRESTIMOS = os.path.join(PASTA_DADOS, "emprestimos.json")


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.alunos = []
        self.emprestimos = []
        self.carregar_dados()

    def carregar_json(self, arquivo):
        if os.path.exists(arquivo):
            try:
                with open(arquivo, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return []
        return []

    def salvar_json(self, arquivo, dados):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

    def carregar_dados(self):
        self.livros = self.carregar_json(ARQUIVO_LIVROS)
        self.alunos = self.carregar_json(ARQUIVO_ALUNOS)
        self.emprestimos = self.carregar_json(ARQUIVO_EMPRESTIMOS)

    def gerar_id(self, lista):
        if not lista:
            return 1
        return max(item["id"] for item in lista) + 1

    def adicionar_livro(self, titulo, autor):
        self.livros.append({
            "id": self.gerar_id(self.livros),
            "titulo": titulo,
            "autor": autor
        })
        self.salvar_json(ARQUIVO_LIVROS, self.livros)

    def adicionar_aluno(self, nome, turma):
        self.alunos.append({
            "id": self.gerar_id(self.alunos),
            "nome": nome,
            "turma": turma
        })
        self.salvar_json(ARQUIVO_ALUNOS, self.alunos)

    def emprestar(self, aluno_id, livro_id):
        self.emprestimos.append({
            "id": self.gerar_id(self.emprestimos),
            "aluno_id": aluno_id,
            "livro_id": livro_id,
            "status": "Emprestado"
        })
        self.salvar_json(ARQUIVO_EMPRESTIMOS, self.emprestimos)

    def devolver(self, emp_id):
        for emp in self.emprestimos:
            if emp["id"] == emp_id:
                emp["status"] = "Devolvido"
        self.salvar_json(ARQUIVO_EMPRESTIMOS, self.emprestimos)


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Biblioteca")
        self.root.geometry("900x600")

        self.bib = Biblioteca()

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        self.aba_livros = ttk.Frame(self.notebook)
        self.aba_alunos = ttk.Frame(self.notebook)
        self.aba_emprestimos = ttk.Frame(self.notebook)

        self.notebook.add(self.aba_livros, text="Livros")
        self.notebook.add(self.aba_alunos, text="Alunos")
        self.notebook.add(self.aba_emprestimos, text="Empréstimos")

        self.criar_aba_livros()
        self.criar_aba_alunos()
        self.criar_aba_emprestimos()

    def criar_aba_livros(self):
        tk.Label(self.aba_livros, text="Título").pack()
        self.titulo = tk.Entry(self.aba_livros)
        self.titulo.pack()

        tk.Label(self.aba_livros, text="Autor").pack()
        self.autor = tk.Entry(self.aba_livros)
        self.autor.pack()

        tk.Button(self.aba_livros, text="Cadastrar Livro",
                  command=self.add_livro).pack(pady=5)

        self.lista_livros = tk.Listbox(self.aba_livros, width=100)
        self.lista_livros.pack(fill="both", expand=True)

        self.atualizar_livros()

    def criar_aba_alunos(self):
        tk.Label(self.aba_alunos, text="Nome").pack()
        self.nome = tk.Entry(self.aba_alunos)
        self.nome.pack()

        tk.Label(self.aba_alunos, text="Turma").pack()
        self.turma = tk.Entry(self.aba_alunos)
        self.turma.pack()

        tk.Button(self.aba_alunos, text="Cadastrar Aluno",
                  command=self.add_aluno).pack(pady=5)

        self.lista_alunos = tk.Listbox(self.aba_alunos, width=100)
        self.lista_alunos.pack(fill="both", expand=True)

        self.atualizar_alunos()

    def criar_aba_emprestimos(self):
        tk.Label(self.aba_emprestimos, text="Aluno").pack()

        self.cb_aluno = ttk.Combobox(self.aba_emprestimos, state="readonly")
        self.cb_aluno.pack()

        tk.Label(self.aba_emprestimos, text="Livro").pack()

        self.cb_livro = ttk.Combobox(self.aba_emprestimos, state="readonly")
        self.cb_livro.pack()

        tk.Button(self.aba_emprestimos,
                  text="Registrar Empréstimo",
                  command=self.registrar_emprestimo).pack(pady=5)

        tk.Button(self.aba_emprestimos,
                  text="Marcar como Devolvido",
                  command=self.devolver).pack(pady=5)

        self.lista_emp = tk.Listbox(self.aba_emprestimos, width=120)
        self.lista_emp.pack(fill="both", expand=True)

        self.atualizar_combos()
        self.atualizar_emprestimos()

    def add_livro(self):
        if not self.titulo.get() or not self.autor.get():
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        self.bib.adicionar_livro(self.titulo.get(), self.autor.get())
        self.titulo.delete(0, tk.END)
        self.autor.delete(0, tk.END)

        self.atualizar_livros()
        self.atualizar_combos()

    def add_aluno(self):
        if not self.nome.get() or not self.turma.get():
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        self.bib.adicionar_aluno(self.nome.get(), self.turma.get())
        self.nome.delete(0, tk.END)
        self.turma.delete(0, tk.END)

        self.atualizar_alunos()
        self.atualizar_combos()

    def atualizar_livros(self):
        self.lista_livros.delete(0, tk.END)
        for l in self.bib.livros:
            self.lista_livros.insert(tk.END, f'{l["id"]} - {l["titulo"]} ({l["autor"]})')

    def atualizar_alunos(self):
        self.lista_alunos.delete(0, tk.END)
        for a in self.bib.alunos:
            self.lista_alunos.insert(tk.END, f'{a["id"]} - {a["nome"]} ({a["turma"]})')

    def atualizar_combos(self):
        self.cb_aluno["values"] = [
            f'{a["id"]} - {a["nome"]}' for a in self.bib.alunos
        ]
        self.cb_livro["values"] = [
            f'{l["id"]} - {l["titulo"]}' for l in self.bib.livros
        ]

    def registrar_emprestimo(self):
        if not self.cb_aluno.get() or not self.cb_livro.get():
            messagebox.showwarning("Aviso", "Selecione aluno e livro.")
            return

        aluno_id = int(self.cb_aluno.get().split(" - ")[0])
        livro_id = int(self.cb_livro.get().split(" - ")[0])

        self.bib.emprestar(aluno_id, livro_id)
        self.atualizar_emprestimos()

    def atualizar_emprestimos(self):
        self.lista_emp.delete(0, tk.END)

        for e in self.bib.emprestimos:
            aluno = next((a["nome"] for a in self.bib.alunos if a["id"] == e["aluno_id"]), "?")
            livro = next((l["titulo"] for l in self.bib.livros if l["id"] == e["livro_id"]), "?")

            self.lista_emp.insert(
                tk.END,
                f'ID:{e["id"]} | {aluno} -> {livro} | {e["status"]}'
            )

    def devolver(self):
        sel = self.lista_emp.curselection()
        if not sel:
            messagebox.showwarning("Aviso", "Selecione um empréstimo.")
            return

        texto = self.lista_emp.get(sel[0])
        emp_id = int(texto.split("|")[0].replace("ID:", "").strip())

        self.bib.devolver(emp_id)
        self.atualizar_emprestimos()


root = tk.Tk()
app = App(root)
root.mainloop()
