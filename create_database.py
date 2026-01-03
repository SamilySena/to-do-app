import sqlite3

conn = sqlite3.connect('tarefas.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas(
        id INTERGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        descricao TEXT,
        prioridade TEXT NOT NULL,
        cor TEXT NOT NULL,
        status TEXT NOT NULL,
        data_criacao TEXT NOT NULL,
        data_conclusao TEXT
    )                  
''')

conn.commit()
conn.close()
print("Banco de dados criado com sucesso!")