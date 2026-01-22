import sqlite3
from datetime import datetime

class Database:
    #basicamente funções de CRUD aqui
    def __init__(self, db_name='tarefas.db'):
        #inicia o bd
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        
    def conectar (self): 
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
    
    def desconectar (self):
        if self.conn: 
            self.conn.close()

    def criar_tabela(self):
        self.conectar()
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                descricao TEXT,
                prioridade TEXT NOT NULL,
                cor TEXT,
                status TEXT DEFAULT 'Pendente',
                data_criacao TEXT NOT NULL,
                data_conclusao TEXT
            )
        """)
        
        self.conn.commit()
        self.desconectar()
        print("Banco de dados criado!")
        
    def add_tarefa(self, titulo, descricao="", prioridade="Média",
                   cor="blue", prazo=""):
        self.conectar()
        
        data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        self.cursor.execute('''
            INSERT INTO tarefas (titulo, descricao, prioridade, cor, data_criacao, prazo)
            VALUES(?, ?, ?, ?, ?, ?)                    
        ''', (titulo, descricao, prioridade, cor, data_criacao, prazo))
        
        self.conn.commit()
        tarefa_id = self.cursor.lastrowid
        self.desconectar()
        
        print(f"Tarefa '{titulo}' adicionada")
        return tarefa_id
    
    def listar_tarefas(self):
        
        self.conectar()
        
        self.cursor.execute('SELECT * FROM tarefas ORDER BY id DESC')
        tarefas = self.cursor.fetchall()
        
        self.desconectar()
        return tarefas
    
if __name__ == "__main__":
    db = Database()
    db.criar_tabela()
    print("Banco pronto para usar")    
    


