# MELHOR CRIAR UM CURSOR E UMA CONEXÃO EM CADA FUNÇÃO OU GERAL?
import sqlite3

def cria_tabela(query_dados):
    conn = sqlite3.connect('db/database_alunos.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Livros ( ?
    );
    """), query_dados
    conn.commit()
    conn.close()

def insere_dados(lista_dados):
    conn = sqlite3.connect('db/database_alunos.db')
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT INTO Livros (Titulo, Autor, AnoPublicacao, Genero)
    VALUES (?, ?, ?, ?);
    """, lista_dados)
    conn.commit()
    conn.close()

def seleciona_tudo(tabela):
    conn = sqlite3.connect('db/database_alunos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tabela")   
    conn.commit()
    conn.close()
    return cursor.fetchall()

def filtro_tabela_geral(tabela, coluna, valor):
    conn = sqlite3.connect('db/database_alunos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tabela WHERE coluna = valor")
    conn.commit()
    conn.close()
    return cursor.fetchall()

# Atualiza dados de estudante específico
def atualiza_dados(tabela, coluna, valor, coluna_mudar, valor_mudar):
    conn = sqlite3.connect('db/database_alunos.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tabela SET coluna_mudar = valor_mudar WHERE coluna = valor")
    conn.commit()
    conn.close()