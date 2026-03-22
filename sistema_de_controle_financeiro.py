import json  # salvar os dados em arquivo JSON
import os

# Classe base de qualquer transação (entrada ou saída)
class Transacao:
    def __init__(self, descricao, valor, categoria):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria

    # transforma a transação em dicionário pra salvar no JSON
    def to_dict(self):
        dicionario_json = {}
        
        dicionario_json['tipo'] = self.__class__.__name__  # Receita ou Despesa
        dicionario_json['descricao'] = self.descricao
        dicionario_json['valor'] = self.valor
        dicionario_json['categoria'] = self.categoria
        
        return dicionario_json
        
    # mostra a transação no terminal
    def mostrar_transacao(self):
        print(f'{self.descricao} | {self.valor} | {self.categoria}')
 
 # MENU INICIAL
 
    def exibir_titulos(self, mensagem):
        print(mensagem)

class Menu_Inicial():
    def menu(self):
        try:    
            while True:
                self.exibir_titulos('📂 SISTEMA DE FINANÇAS\n')
                print('1 — Adicionar receita')
                print('2 — Adicionar despesa')
                print('3 — Ver extrato')
                print('4 — Relatórios')
                print('5 — Salvar e sair\n')
                
                opcao = int(input('Qual opção gostaria'))
                
            
                if opcao == 1:
                    ...
                    self.voltar_menu()
                elif opcao == 2:
                    ...
                    self.voltar_menu()
                elif opcao == 3:
                    self.ver_extrato()
                    self.voltar_menu()
                elif opcao == 4:
                    self.relatorios()
                    self.voltar_menu()
                elif opcao == 5:
                    self.salvar_sair()
                    print('Finanças salvas com sucesso!')
                    break
                else:
                    print('Opção inválida, tente novamente!')
        except ValueError:
                print("💥 ERRO CRÍTICO: O programa encontrou um valor inválido!")
                
    # 3- Ver extrato              
    def ver_extrato(self):

        if len(minha_carteira.transacoes) == 0:

            print("\n🆕 Nenhum dado encontrado. Criando dados iniciais...")

            novas_transacoes = [
                Receita("Salário Mensal", 5000.00, "Trabalho"),
                Receita("Freelance Logo", 350.00, "Design"),
                Despesa("Mercado Semanal", 420.50, "Alimentacao"),
                Despesa("Uber Shopping", 25.00, "Transporte"),
                Despesa("Ingresso Cinema", 45.00, "Lazer")
            ]

            for t in novas_transacoes:
                minha_carteira.adicionar_transacao(t)

        else:
            print("📊 Dados existentes carregados com sucesso!")
            
    # 4 - Relatórios      
    def relatorios(self):
        
        self.exibir_titulos("📜 EXTRATO DETALHADO")
        minha_carteira.mostrar_transacoes()

        self.exibir_titulos("💰 RESUMO DE SALDO")
        minha_carteira.mostrar_saldo()

        self.exibir_titulos("📊 ANÁLISE POR CATEGORIA")
        minha_carteira.gasto_por_categoria()

        self.exibir_titulos("🔍 DESTAQUES DE CONSUMO")
        minha_carteira.maior_gasto()
        minha_carteira.categoria_maior_gasto() 
        
    # 5 - Salvar e sair
    def salvar_sair(self):
        print(f"\n{'*'*35}")
        print("💾 Salvando dados no banco JSON...")
        minha_carteira.salvar_json()
        print("✅ Operação finalizada com sucesso!")
        print(f"{'*'*35}")
    
    # Controle de menu
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def voltar_menu(self):
        input("\nPressione Enter para voltar ao menu...")
        self.limpar_tela()

# Classe de dinheiro que entra
class Receita(Transacao):
    def impacto_saldo(self):
        print(f'✅ Entrada: R$ +{self.valor:.2f} adicionado ao saldo')
        return +self.valor  # soma no saldo


# Classe de dinheiro que sai
class Despesa(Transacao):
    def impacto_saldo(self):
        print(f'⚠️ Saída: R$ -{self.valor:.2f} debitado com sucesso')
        return -self.valor  # subtrai do saldo


# Classe que controla tudo (saldo + lista de transações)
class Carteira:
    def __init__(self):
        self.saldo = 0
        self.transacoes = []  # lista onde ficam todas as transações
        
    # adiciona uma transação e atualiza o saldo
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
        self.saldo += transacao.impacto_saldo()
        
    # mostra o saldo atual
    def mostrar_saldo(self):
        print(f'Saldo atual: R$ {self.saldo}')
        
    # mostra todas as transações cadastradas
    def mostrar_transacoes(self):
        for transacao in self.transacoes:
            transacao.mostrar_transacao()
            
    # soma todas as receitas
    def total_receitas(self):
        total = 0
        
        for transacao in self.transacoes:
            if isinstance(transacao, Receita):
                total += transacao.valor
        
        print(f'Total de receitas: R$ {total:.2f}')
        
    # soma todas as despesas
    def total_despesas(self):
        total = 0
        
        for transacao in self.transacoes:
            if isinstance(transacao, Despesa):
                total += transacao.valor
        
        print(f'Total de despesas: R$ {total:.2f}')
        
    # pega a maior despesa individual
    def maior_gasto(self):
        maior_valor = 0
        
        for transacao in self.transacoes:
            if isinstance(transacao, Despesa):
                if transacao.valor > maior_valor:
                    maior_valor = transacao.valor
            
        print(f"Maior despesa: R$ {maior_valor:.2f}")
 
    # mostra quanto foi gasto por categoria
    def gasto_por_categoria(self):
        gasto_categoria = {}
        
        for transacao in self.transacoes:
            if isinstance(transacao, Despesa):
                categoria = transacao.categoria
                valor = transacao.valor
                
                if categoria in gasto_categoria:
                    gasto_categoria[categoria] += valor
                else:
                    gasto_categoria[categoria] = valor
        
        print("Gastos por categoria:")
        
        for categoria, total in gasto_categoria.items():
            print(f"{categoria} → R$ {total:.2f}")
            
    # mostra qual categoria teve mais gasto
    def categoria_maior_gasto(self):
        gasto_por_categoria = {}
        
        for transacao in self.transacoes:
            if isinstance(transacao, Despesa):
                categoria = transacao.categoria
                valor = transacao.valor
                
                if categoria in gasto_por_categoria:
                    gasto_por_categoria[categoria] += valor
                else:
                    gasto_por_categoria[categoria] = valor
                      
        categoria_com_maior_gasto = None
        maior_valor = 0
                
        for categoria, valor in gasto_por_categoria.items():
            if valor > maior_valor:
                maior_valor = valor
                categoria_com_maior_gasto = categoria
            
        if categoria_com_maior_gasto:
            print(f"Categoria com maior gasto: {categoria_com_maior_gasto} — R$ {maior_valor:.2f}")
        else:
            print("Nenhuma despesa encontrada")
            
    # salva tudo num arquivo JSON
    def salvar_json(self):
        lista_json = []
        
        for transacao in self.transacoes:
            lista_json.append(transacao.to_dict())
            
        with open('transacao.json', 'w') as arquivo_transacao:
            json.dump(lista_json, arquivo_transacao, indent=4)
            
    # carregar arquivo JSON
    def carregar_json(self):
        
        try:
            with open('transacao.json', 'r') as arquivo_transacao:
                dados = json.load(arquivo_transacao)
                        
            for item_json in dados:
                tipo = item_json['tipo']
                descricao = item_json['descricao']
                valor = item_json['valor']
                categoria = item_json['categoria'] 
                              
                if tipo == 'Receita':
                    tipo_lista = Receita(descricao, valor, categoria)
                elif tipo == 'Despesa':
                    tipo_lista = Despesa(descricao, valor, categoria)
                
                self.adicionar_transacao(tipo_lista)
                
        except FileNotFoundError:
            print(f"Erro: O arquivo não foi encontrado.")            
               

# ===== TESTE =====

minha_carteira = Carteira()

# --- Inicialização ---
Menu_Inicial.menu()
Menu_Inicial.escolha_opcao()

print("🔄 Carregando dados anteriores...")
minha_carteira.carregar_json()
