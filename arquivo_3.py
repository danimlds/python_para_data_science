import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

con = sqlite3.connect('vendas.db')

c = con.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS vendas(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          vendas FLOAT NOT NULL,
          vendedor TEXT NOT NULL,
          cidade TEXT NOT NULL
          )''')
con.commit()


c.execute('DELETE FROM vendas')
con.commit()

# vendas = float(input('Informe o valor das vendas: '))
# vendedor = input('Informe o nome do vendedor: ')
# cidade = input('Informe a cidade: ')
c.execute('''
               INSERT INTO vendas
               (vendas, vendedor, cidade)
               VALUES (2000, 'a', 'São Paulo')
               ''')

c.execute('''
               INSERT INTO vendas
               (vendas, vendedor, cidade)
               VALUES (2000300, 'b', 'Rio de Janeiro')
               ''')
c.execute('''
               INSERT INTO vendas
               (vendas, vendedor, cidade)
               VALUES (30000, 'c', 'Belo Horizonte')
               ''')
c.execute('''
               INSERT INTO vendas
               (vendas, vendedor, cidade)
               VALUES (3000, 'd', 'Curitiba')
               ''')

con.commit()

# con.execute('''
#             INSERT INTO vendas
#             (vendas, vendedor, cidade)
#             VALUES (?,?,?)
#             ''', (vendas, vendedor, cidade))

# c.execute("SELECT * FROM vendas")
# vendas = c.fetchall()
# print(vendas)



# for venda in vendas:
#     print(f'''id:{vendas[0]},
#           vendas:{vendas[1]},
#           vendedor:{vendas[2]},
#           cidade:{vendas[3]}
#           ''')


df = pd.read_sql_query('SELECT * FROM vendas', con)

# media_de_vendas = df[vendas].mean()
# print(media_de_vendas)
print(df)
# print(df.describe())


# csvs = 'dados_exportados_2.csv'
# df.to_csv(csvs)

plt.figure(figsize=(10, 5))
plt.bar(df['vendas'], df['vendedor'], color='skyblue')
plt.xlabel('vendas')
plt.ylabel('vendedor')
plt.title('VENDAS X VENDEDOR')
plt.tight_layout()
plt.show()

c.close()
# Criar um DataFrame
# data = {'Vendas': [2000,2000300,30000,3000],
# 	      'Vendedor': ['a','b','c','d'],
#         'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']}
# df = pd.DataFrame(data)
# print(df)

# 1 Transfome em um banco de dados
# 2 leitura de Dados de Arquivos
# 3 Visualização de Dados
# 4 seleção e Indexação
# 5 Filtragem de Dados
# 6.Manipulação de Dados