import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('chacara.db')

# Ler dados de vendas e produtos
vendas_df = pd.read_sql_query('SELECT * FROM vendas', conn)
produtos_df = pd.read_sql_query('SELECT * FROM produtos', conn)

# Juntar vendas com produtos para obter mais informações sobre cada venda
df_completo = pd.merge(vendas_df, produtos_df, left_on='produto_id', right_on='id')

# Análise simples: produtos mais vendidos
produtos_mais_vendidos = df_completo.groupby('nome')['quantidade'].sum().sort_values(ascending=False)
print("Produtos mais vendidos:")
print(produtos_mais_vendidos)

# Análise de valores totais de vendas
vendas_por_data = df_completo.groupby('data')['valor_total'].sum()
print("\nTotal de vendas por dia:")
print(vendas_por_data)

# Fechar conexão
conn.close()
