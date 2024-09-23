from vendas import banco_vendas
from agenda import agendamento
from analise import perfil_analise

def main():
    # Criar tabelas no banco de dados
    banco_vendas.criar_tabelas()
    agendamento.criar_tabela_agenda()

    # Adicionar produto e registrar venda
    banco_vendas.adicionar_produto('Refrigerante', 7.00, 50)
    banco_vendas.registrar_venda(1, 5)

    # Agendar um jogo
    agendamento.agendar_jogo('Time B', '2024-09-30', '14:00', '16:00')

    # Analisar perfil de frequentadores
    perfil_analise.analisar_perfil()

if __name__ == "__main__":
    main()
