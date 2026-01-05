import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("tarefas.db")
        self.cursor = self.conn.cursor()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                descricao TEXT,
                prioridade TEXT NOT NULL,
                cor TEXT NOT NULL,
                status TEXT NOT NULL,
                data_criacao TEXT NOT NULL,
                data_conclusao TEXT
            )
        """)
        self.conn.commit()

    def fechar(self):
        self.conn.close()
