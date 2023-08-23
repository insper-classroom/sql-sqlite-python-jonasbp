from db.db_utils import *

# Crie uma tabela chamada "Estudantes"
cria_tabela("Estudantes","ID INTEGER PRIMARY KEY AUTOINCREMENT,Nome TEXT NOT NULL,Curso TEXT NOT NULL,Ano_ingresso INTEGER")

# Insira 5 registros de estudantes na tabela.
estudantes = [
    ("Ana Silva", "Computação", 2019),
    ("Pedro Mendes", "Física", 2021),
    ("Carla Souza", "Computação",2020),
    ("João Alves", "Matemática",2018),
    ("Maria Oliveira", "Química",2022)

]
insere_dados(estudantes)

# Selecione e mostre todos os registros da tabela no console
print("---")
print(seleciona_tudo("Estudantes"))


# Filtre e mostre os estudantes que ingressaram entre 2019 e 2020 (inclusive) e exiba no console. Use o comando WHERE para realizar essa filtragem.
print("---")
print(filtro_tabela_geral("Estudantes","Ano_ingresso >= 2019 AND Ano_ingresso <= 2020"))

# Atualize o "Ano de Ingresso" de um estudante específico. Mostre por todos estudantes novamente.
atualiza_dados("Estudantes","Ano_ingresso = 2023 WHERE Nome='Pedro Mendes'")
print("---")
print(seleciona_tudo("Estudantes"))

# Delete um registro da tabela usando o ID do estudante. Mostre por todos estudantes novamente.
deleta_registro("Estudantes","ID = 2")
print("---")
print(seleciona_tudo("Estudantes"))

# Filtre e mostre os estudantes do Curso de Computação que ingressaram após 2019. Mostre o resultado.
print("**Curso de Computação que ingressaram após 2019**")
print(filtro_tabela_geral("Estudantes","Curso = 'Computação' AND Ano_ingresso > 2019"))

# Imagine que alguém errou nos registros de ingresso de todos os alunos do curso de Computação, crie uma query que altere todos os registros dos alunos de Computação, campo ingresso para 2018. Mostre por todos estudantes novamente.
atualiza_dados("Estudantes","Ano_ingresso = 2018 WHERE Curso = 'Computação'")
print("---")
print(seleciona_tudo("Estudantes"))