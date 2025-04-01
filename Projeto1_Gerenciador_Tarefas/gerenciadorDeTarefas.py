import tkinter as tk
from tkinter import messagebox, ttk
from bson.objectid import ObjectId
from pymongo import MongoClient


class GerenciadorTarefasApp:
    def __init__(self, janela):
        self.janela = janela

        self.janela.title("Gerenciador de Tarefas")

        self.janela.geometry("950x700")

        self.janela.configure(bg="#f0f0f0")

        self.cliente = MongoClient("mongodb://localhost:27017")

        self.bd = self.cliente["gerenciador_tarefas_db"]

        self.colecao = self.bd["tarefas"]

        estilo = ttk.Style()

        estilo.theme_use("default")

        estilo.configure(
            "Treeview",
            background="#ffffff",
            foreground="black",
            rowheight=25,
            fieldbackground="#ffffff",
            font=("Arial", 11),
        )

        estilo.configure("Treeview.Heading", font=("Arial", 12, "bold"))

        estilo.map(
            "Treeview",
            background=[("selected", "black")],
            foreground=[("selected", "white")],
        )

        quadro_entrada = tk.Frame(self.janela, bg="#f0f0f0")
        quadro_entrada.pack(pady=10, padx=10, fill="x")

        rotulo_titulo = tk.Label(
            quadro_entrada, text="Título da Tarefa", bg="#f0f0f0", font=("Arial", 12)
        )

        rotulo_titulo.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.entrada_titulo = tk.Entry(quadro_entrada, font=("Arial", 11), width=55)

        self.entrada_titulo.grid(
            row=0, column=1, padx=5, pady=5, sticky="w", columnspan=3
        )

        rotulo_descricao = tk.Label(
            quadro_entrada, text="Descrição da Tarefa", bg="#f0f0f0", font=("Arial", 12)
        )

        rotulo_descricao.grid(row=1, column=0, padx=5, pady=5, sticky="ne")

        self.texto_descricao = tk.Text(
            quadro_entrada, font=("Arial", 11), width=55, height=5
        )

        self.texto_descricao.grid(
            row=1, column=1, padx=5, pady=5, sticky="w", columnspan=3
        )

        rotulo_status = tk.Label(
            quadro_entrada, text="Status da Tarefa", bg="#f0f0f0", font=("Arial", 12)
        )
        rotulo_status.grid(row=2, column=0, padx=5, pady=5, sticky="we")

        self.var_status = tk.StringVar()

        self.combo_status = ttk.Combobox(
            quadro_entrada,
            textvariable=self.var_status,
            font=("Arial", 11),
            width=53,
            values=["Pendente", "Em Andamento", "Concluída"],
            state="readonly",
        )

        self.combo_status.grid(row=2, column=1, padx=5, pady=5)

        self.combo_status.current(0)

        quadro_botoes = tk.Frame(self.janela, bg="#f0f0f0")
        quadro_botoes.pack(pady=10)

        botao_adicionar = tk.Button(
            quadro_botoes,
            text="Adicionar Tarefa",
            command=self.adicionar_tarefa,
            bg="#a5d6a7",
            font=("Arial", 12, "bold"),
            width=18,
        )

        botao_adicionar.grid(row=0, column=0, padx=10, pady=5)

        botao_atualizar = tk.Button(
            quadro_botoes,
            text="Atualizar Tarefa",
            command=self.atualizar_tarefa,
            bg="#fff59d",
            font=("Arial", 12, "bold"),
            width=18,
        )

        botao_atualizar.grid(row=0, column=1, padx=10, pady=5)

        botao_excluir = tk.Button(
            quadro_botoes,
            text="Excluir Tarefa",
            command=self.excluir_tarefa,
            bg="red",
            font=("Arial", 12, "bold"),
            width=18,
        )

        botao_excluir.grid(row=0, column=2, padx=10, pady=5)

    def adicionar_tarefa(self):
        print("Adicionando tarefa...")

    def atualizar_tarefa(self):
        print("Atualizando tarefa...")

    def excluir_tarefa(self):
        print("Excluindo tarefa...")


janela_principal = tk.Tk()

app = GerenciadorTarefasApp(janela_principal)

janela_principal.mainloop()
