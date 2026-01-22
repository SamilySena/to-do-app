import tkinter as tk  #esse tkinter é biblioteca de interface grafica, da pra gente aproveitar alguas coisas 
from tkinter import ttk, messagebox
from datetime import datetime
from create_database import Database

class ToDo:
    def __init__(self, root):
        self.root = root
        self.root.title("Minhas Tarefas")
        self.root.goemetry("400x600")
        self.root.configure(bg="fafafa")
        
        self.db = Database()
        self.db.criar_tabela()
        
        self.db.painel_principal()
    
    def painel_principal(self):
         
         #limpar a tela principal
        for widget in self.root.winfo_children():
            widget.destroy()  
        
        tk.label(
            self.root,
            text="Minhas Tarefas",
            font=("Arial", 20, "bold", "italic"),
            bg="ffffff",
            fg="333333"
        ).pack(pady=20)   

    