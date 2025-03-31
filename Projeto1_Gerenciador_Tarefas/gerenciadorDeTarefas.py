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
        
janela_principal = tk.Tk()

app = GerenciadorTarefasApp(janela_principal)

janela_principal.mainloop()