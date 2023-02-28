import pandas as pd
import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine

# Conectando ao banco de dados usando o psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="koreData",
    user="postgres",
    password="123"
)

# Criando um engine do SQLAlchemy para se conectar ao banco de dados
engine = create_engine('postgresql://postgres:123@localhost/koreData')

# Query para obter a lista de produtos vendidos em 2019 e 2020
query_faturamento = """
    SELECT * FROM vendas2019
"""

# Executando a query e armazenando o resultado em um dataframe
faturamento_por_trimestre = pd.read_sql_query(sql=query_faturamento, con=engine)
# Imprimindo o dataframe
print(faturamento_por_trimestre)