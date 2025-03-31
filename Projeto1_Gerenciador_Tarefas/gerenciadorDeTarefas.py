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
        
        estilo.theme_use('default')
        
        estilo.configure("Treeview",
                         background="#ffffff", 
                         foreground="black",
                         rowheight=25, 
                         fieldbackground="#ffffff",
                         font=("Arial", 11))
        
        estilo.configure("Treeview.Heading",
                         font=("Arial", 12, "bold"))
        
        estilo.map("Treeview",
                   background=[("selected", "black")],
                   foreground=[("selected", "white")])
        
        quadro_entrada = tk.Frame(self.janela, bg="#f0f0f0")
        quadro_entrada.pack(pady=10, padx=10, fill="x")
        
        rotulo_titulo = tk.Label(quadro_entrada, text="Título da Tarefa", bg="#f0f0f0", font=("Arial", 12))
        
        rotulo_titulo.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        
        self.entrada_titulo = tk.Entry(quadro_entrada, font=("Arial", 11), width=55)
        
        self.titulo.grid(row=0, column=1, padx=5, pady=5, sticky="w", columnspan=3)
                   
        
janela_principal = tk.Tk()

app = GerenciadorTarefasApp(janela_principal)

janela_principal.mainloop()