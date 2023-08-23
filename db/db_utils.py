# MELHOR CRIAR UM CURSOR E UMA CONEXÃO EM CADA FUNÇÃO OU GERAL?
import sqlite3

def cria_tabela(nome_tabela,query_dados):
    conn = sqlite3.connect('db/database_alunos.db')
    cursor = conn.cursor()
    comando_sql = f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({query_dados})"
    cursor.execute(comando_sql)
    conn.commit()
    conn.close()

def insere_dados(lista_dados):
    conn = sqlite3.connect('db/database_alunos.db')
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT INTO Estudantes (Nome, Curso, Ano_ingresso)
    VALUES (?, ?, ?);
    """, lista_dados)
    conn.commit()
    conn.close()

def seleciona_tudo(tabela):
    conn = sqlite3.connect('db/database_alunos.db')
    cursor = conn.cursor()
    sql = f"SELECT * FROM {tabela}"
    cursor.execute(sql)
    dados = cursor.fetchall()
    conn.close()
    return dados

def filtro_tabela_geral(tabela,query):
    conn = sqlite3.connect('db/database_alunos.db')
    cursor = conn.cursor()
    sql = f"SELECT * FROM {tabela} WHERE {query}"
    cursor.execute(sql)
    filtro = cursor.fetchall()
    conn.commit()
    conn.close()
    return filtro

# Atualiza dados de estudante específico
def atualiza_dados(tabela, query):
    conn = sqlite3.connect('db/database_alunos.db')
    cursor = conn.cursor()
    sql = f"UPDATE {tabela} SET {query}"
    cursor.execute(sql)
    conn.commit()
    conn.close()

# Deleta um registro da tabela
def deleta_registro(tabela, query):
    conn = sqlite3.connect('db/database_alunos.db')
    cursor = conn.cursor()
    sql = f"DELETE FROM {tabela} WHERE {query}"
    cursor.execute(sql)
    conn.commit()
    conn.close()
