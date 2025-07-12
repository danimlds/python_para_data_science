import sqlite3
import matplotlib.pyplot as plt
import pandas as pd


con = sqlite3.connect('clientes.db')

c = con.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS clientes(
          id INTEGER PRIMARY KEY  AUTOINCREMENT,
          nome TEXT NOT NULL,
          idade INTEGER NOT NULL,
          cidade TEXT NOT NULL
          )''')

# nome = input('Informe o nome: ')
# idade = int(input('Informe a idade: '))
# cidade = input('Informe a cidade: ')

con.execute('''
               INSERT INTO clientes 
               (nome, idade, cidade)
               VALUES ('Jason Bourne', 35, 'UK')
               ''')
con.execute('''
               INSERT INTO clientes
               (nome, idade, cidade)
               VALUES ('Morgan Freeman', 85, 'EUA')
               ''')
con.execute('''
               INSERT INTO clientes 
               (nome, idade, cidade)
               VALUES ('Machado de Assis', 100, 'RJ')
               ''')

con.execute('SELECT * FROM clientes')
clientes = c.fetchall()

for cliente in clientes:
    print(f'''id: {cliente[0]},
          nome:{cliente[1]},
          idade:{cliente[2]},
          cidade:{cliente[3]}''')

df = pd.read_sql_query('SELECT * FROM clientes', con)


#media de idade
media_idade = df['idade'].mean()
print(media_idade)


#descrição
print(df.describe())


#exportar dados para o csv
csvs = 'dados_exportados.csv'
df.to_csv(csvs)



#grafico de barra
plt.figure(figsize=(10, 5))
plt.bar(df['nome'], df['idade'], color='skyblue')
plt.xlabel('nome')
plt.ylabel('idade')
plt.title('Nome x Idade')
plt.show()

# c.commit()

c.close()