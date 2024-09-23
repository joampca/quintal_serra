import sqlite3
from datetime import datetime

# Conectar ao banco de dados (ou criar, se não existir)
conn = sqlite3.connect('chacara.db')
cursor = conn.cursor()

# Criar tabelas de produtos e vendas
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preco REAL,
    estoque INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER,
    quantidade INTEGER,
    data TEXT,
    valor_total REAL,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
)
''')

# Função para registrar venda e atualizar estoque
def registrar_venda(produto_id, quantidade):
    cursor.execute("SELECT preco, estoque FROM produtos WHERE id=?", (produto_id,))
    produto = cursor.fetchone()

    if produto and produto[1] >= quantidade:
        preco = produto[0]
        valor_total = preco * quantidade
        nova_quantidade = produto[1] - quantidade
        data_venda = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cursor.execute("INSERT INTO vendas (produto_id, quantidade, data, valor_total) VALUES (?, ?, ?, ?)",
                       (produto_id, quantidade, data_venda, valor_total))

        cursor.execute("UPDATE produtos SET estoque=? WHERE id=?", (nova_quantidade, produto_id))

        conn.commit()
        print(f"Venda registrada com sucesso! Total: R$ {valor_total}")
    else:
        print("Estoque insuficiente ou produto não encontrado.")

# Função para adicionar novos produtos
def adicionar_produto(nome, preco, estoque):
    cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)", (nome, preco, estoque))
    conn.commit()
    print(f"Produto {nome} adicionado com sucesso!")

# Exemplo de uso
adicionar_produto('Cerveja', 5.00, 100)
registrar_venda(1, 5)  # Venda de 5 unidades do produto com id 1 (Cerveja)

# Fechar conexão
conn.close()
