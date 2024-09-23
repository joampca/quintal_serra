import sqlite3
from datetime import datetime

# Conectar ao banco de dados (ou criar, se não existir)
conn = sqlite3.connect('chacara.db')
cursor = conn.cursor()

# Criar tabela de agendamentos
cursor.execute('''
CREATE TABLE IF NOT EXISTS agendamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_time TEXT,
    data_jogo TEXT,
    hora_inicio TEXT,
    hora_fim TEXT
)
''')

# Função para agendar um jogo
def agendar_jogo(nome_time, data_jogo, hora_inicio, hora_fim):
    cursor.execute("SELECT * FROM agendamentos WHERE data_jogo=? AND hora_inicio<=? AND hora_fim>=?",
                   (data_jogo, hora_fim, hora_inicio))
    conflito = cursor.fetchone()

    if conflito:
        print("Conflito de agendamento. Tente outro horário.")
    else:
        cursor.execute("INSERT INTO agendamentos (nome_time, data_jogo, hora_inicio, hora_fim) VALUES (?, ?, ?, ?)",
                       (nome_time, data_jogo, hora_inicio, hora_fim))
        conn.commit()
        print(f"Jogo agendado com sucesso para {nome_time} em {data_jogo} das {hora_inicio} às {hora_fim}.")

# Exemplo de uso
agendar_jogo('Time A', '2024-09-25', '10:00', '12:00')

# Fechar conexão
conn.close()
