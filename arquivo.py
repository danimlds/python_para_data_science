import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

con = sqlite3.connect('meu_banco_de_dados.db')
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        cidade TEXT NOT NULL
    )
''')


nome = input('Informe um nome: ')
idade = int(input('Informe a idade: '))
cidade = input('Informe a cidade: ')

cursor.execute('''
               INSERT INTO pessoas 
               (nome, idade, cidade)
               VALUES (?,?,?)
               ''', (nome, idade, cidade))

cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()

for pessoa in pessoas:
    print(f'''id: {pessoa[0]},
            nome: {pessoa[1]},
            idade:{pessoa[2]},
            cidade:{pessoa[3]}''')

df = pd.read_sql_query('SELECT nome, idade FROM pessoas', con)
plt.figure(figsize=(10, 5))
plt.bar(df['nome'], df['idade'], color='skyblue')
plt.xlabel('nome')
plt.ylabel('idade')
plt.title('Nome x Idade')
plt.show()


con.commit()
con.close()