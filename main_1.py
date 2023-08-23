import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

# Crie uma tabela chamada "Estudantes"
cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    Ano_ingresso INTEGER
);
""")
# Insira 5 registros de estudantes na tabela.
estudantes = [
    ("Ana Silva", "Computação", 2019),
    ("Pedro Mendes", "Física", 2021),
    ("Carla Souza", "Computação",2020),
    ("João Alves", "Matemática",2018),
    ("Maria Oliveira", "Química",2022)

]
cursor.executemany("""
INSERT INTO Estudantes (Nome, Curso, Ano_ingresso)
VALUES (?, ?, ?);
""", estudantes)
conn.commit()

# Selecione e mostre todos os registros da tabela no console
cursor.execute("SELECT * FROM Estudantes")
print("---")
print(cursor.fetchall())

# Filtre e mostre os estudantes que ingressaram entre 2019 e 2020 (inclusive) e exiba no console. Use o comando WHERE para realizar essa filtragem.
cursor.execute("SELECT * FROM Estudantes WHERE Ano_ingresso >= 2019 AND Ano_ingresso <= 2020")
print("---")
print(cursor.fetchall())

# Atualize o "Ano de Ingresso" de um estudante específico. Mostre por todos estudantes novamente.
cursor.execute("UPDATE Estudantes SET Ano_ingresso = 2023 WHERE Nome='Pedro Mendes'")
cursor.execute("SELECT * FROM Estudantes")
print("---")
print(cursor.fetchall())

# Delete um registro da tabela usando o ID do estudante. Mostre por todos estudantes novamente.
cursor.execute("DELETE FROM Estudantes WHERE ID = 2")
cursor.execute("SELECT * FROM Estudantes")
print("---")
print(cursor.fetchall())

# Filtre e mostre os estudantes do Curso de Computação que ingressaram após 2019. Mostre o resultado.
cursor.execute("SELECT * FROM Estudantes WHERE Curso = 'Computação' AND Ano_ingresso > 2019")
print("---")
print(cursor.fetchall())

# Imagine que alguém errou nos registros de ingresso de todos os alunos do curso de Computação, crie uma query que altere todos os registros dos alunos de Computação, campo ingresso para 2018. Mostre por todos estudantes novamente.

cursor.execute("UPDATE Estudantes SET Ano_ingresso = 2018 WHERE Curso = 'Computação'")
cursor.execute("SELECT * FROM Estudantes")
print("---")
print(cursor.fetchall())




conn.close()

