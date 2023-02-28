import pandas as pd
import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine

# Lendo os arquivos excel de vendas e dimensões para dataframes
vendas2017 = pd.read_excel('C:\\Users\\Lucas\\Desktop\\KORE DATA\\Vendas 2017.xlsx')
vendas2018 = pd.read_excel('Vendas 2018.xlsx')
vendas2019 = pd.read_excel('Vendas 2019.xlsx')
dimensoes = pd.read_excel('Dimensões.xlsx')

# Lendo o arquivo excel de metas para um dataframe
metas = pd.read_excel('C:\\Users\\Lucas\\Desktop\\KORE DATA\\Metas.xlsx')

# Convertendo a coluna 'ValorUnitario' dos dataframes de vendas para string
vendas2017['ValorUnitario'] = vendas2017['ValorUnitario'].astype(str)
vendas2018['ValorUnitario'] = vendas2018['ValorUnitario'].astype(str)
vendas2019['ValorUnitario'] = vendas2019['ValorUnitario'].astype(str)

# Substituindo vírgulas por pontos e removendo o caractere 'R$' das colunas 'ValorUnitario' dos dataframes de vendas
vendas2017['ValorUnitario'] = vendas2017['ValorUnitario'].str.replace(',', '.').str.replace('R$', '')
vendas2018['ValorUnitario'] = vendas2018['ValorUnitario'].str.replace(',', '.').str.replace('R$', '')
vendas2019['ValorUnitario'] = vendas2019['ValorUnitario'].str.replace(',', '.').str.replace('R$', '')

# Convertendo a coluna 'ValorUnitario' dos dataframes de vendas para o tipo float
vendas2017['ValorUnitario'] = vendas2017['ValorUnitario'].astype(float)
vendas2018['ValorUnitario'] = vendas2018['ValorUnitario'].astype(float)
vendas2019['ValorUnitario'] = vendas2019['ValorUnitario'].astype(float)

# Conectando ao banco de dados usando o psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="koreData",
    user="postgres",
    password="123"
)

# Criando um engine do SQLAlchemy para se conectar ao banco de dados
engine = create_engine('postgresql://postgres:123@localhost/koreData')

# Escrevendo os dataframes de vendas, metas e dimensões para tabelas no banco de dados
vendas2017.to_sql('vendas2017', engine, if_exists='replace')
vendas2018.to_sql('vendas2018', engine, if_exists='replace')
vendas2019.to_sql('vendas2019', engine, if_exists='replace')
metas.to_sql('metas', engine, if_exists='replace')
dimensoes.to_sql('dimensoes', engine, if_exists='replace')






