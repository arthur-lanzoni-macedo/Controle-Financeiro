import json
import os
from datetime import datetime

# Classe base de qualquer transação (entrada ou saída)
class Transacao:
    def __init__(self, descricao, valor, categoria, data=None):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        
        if data is None:
            self.data = datetime.now().strftime("%d/%m/%Y")
        else:
            self.data = data

    # transforma a transação em dicionário pra salvar no JSON
    def to_dict(self):
        dicionario_json = {}
        
        dicionario_json['tipo'] = self.__class__.__name__  # Receita ou Despesa
        dicionario_json['descricao'] = self.descricao
        dicionario_json['valor'] = self.valor
        dicionario_json['categoria'] = self.categoria
        dicionario_json['data'] = self.data
        
        return dicionario_json
        
    # mostra a transação no terminal
    def mostrar_transacao(self):
        print(f'{self.data} | {self.descricao} | R$ {self.valor} | {self.categoria}')
 
# MENU INICIAL
 
class Menu_Inicial():
    def exibir_titulos(self, mensagem):
        print(mensagem)
    
    def menu(self):
           
        while True:
            try:    
                    self.limpar_tela()
                    
                    print('📂 SISTEMA DE FINANÇAS\n')
                    print('1 — Adicionar receita')
                    print('2 — Adicionar despesa')
                    print('3 — Ver extrato')
                    print('4 — Relatórios')
                    print('5 — Salvar e sair\n')
                    
                    opcao = int(input('Qual opção gostaria: '))
                    
                    if opcao == 1:
                        self.adicionar_receita()
                        self.voltar_menu()
                    elif opcao == 2:
                        self.adicionar_despesa()
                        self.voltar_menu()
                    elif opcao == 3:
                        self.ver_extrato()
                        self.voltar_menu()
                    elif opcao == 4:
                        self.relatorios()
                        self.voltar_menu()
                    elif opcao == 5:
                        
                        sair_ficar = input('Deseja realmente sair? (s/n)')
                        
                        if sair_ficar == 's':
                            self.salvar_sair()
                            print('Finanças salvas com sucesso!')
                            break
                        else:
                            self.voltar_menu()
                    else:
                        print('Opção inválida, tente novamente!')
                        self.voltar_menu()
            except ValueError:
                    print("💥 Entrada inválida!")
                    
    # 1- Adicionar receita              
    def adicionar_receita(self):     
        descricao = input("Digite a descrição do produto/serviço: ")
        valor = float(input("Digite o valor (ex: 1250.50): "))
        categoria = input("Digite a categoria: ")
        
        if valor <= 0:
            print("💥 Entrada inválida!")
        else:
            adicionar = Receita(descricao, valor, categoria)
            minha_carteira.adicionar_transacao(adicionar)
            print('✅ Receita cadastrada com sucesso')
            print(f'💰 Saldo atual: R${minha_carteira.saldo}')
        
    # 2- Adicionar despesa              
    def adicionar_despesa(self):     
        descricao = input("Digite a descrição do produto/serviço: ")
        valor = float(input("Digite o valor (ex: 1250.50): "))
        categoria = input("Digite a categoria: ")
        
        if valor <= 0:
            print("💥 Entrada inválida!")
        else:
            adicionar = Despesa(descricao, valor, categoria)
            minha_carteira.adicionar_transacao(adicionar)
            print('✅ Despesa cadastrada com sucesso')
            print(f'💰 Saldo atual: R${minha_carteira.saldo}')
    
    # 3- Ver extrato              
    def ver_extrato(self):
        if minha_carteira.transacoes:
            self.exibir_titulos("📜 EXTRATO DETALHADO")
            minha_carteira.mostrar_transacoes()
            print(f'💰 Saldo atual: R${minha_carteira.saldo}')
        else:
                print("\n🆕 Nenhuma transação encontrada.\nUse as opções 1 ou 2 para adicionar dados.")
            
    # 4 - Relatórios      
    def relatorios(self):
        
        self.exibir_titulos("💰 RESUMO DE SALDO")
        minha_carteira.mostrar_saldo()
        print()
        self.exibir_titulos("📊 ANÁLISE POR CATEGORIA")
        minha_carteira.gasto_por_categoria()
        print()
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
                tipo = item_json.get('tipo')
                descricao = item_json.get('descricao')
                valor = item_json.get('valor')
                categoria = item_json.get('categoria')
                data = item_json.get('data')
                              
                if tipo == 'Receita':
                    tipo_lista = Receita(descricao, valor, categoria, data)
                elif tipo == 'Despesa':
                    tipo_lista = Despesa(descricao, valor, categoria, data)
                
                self.adicionar_transacao(tipo_lista)
                
        except FileNotFoundError:
            print(f"Erro: O arquivo não foi encontrado.")            
               

# TESTE

def main():
    global minha_carteira

    # Cria os objetos principais
    minha_carteira = Carteira()
    menu = Menu_Inicial()

    print("🔄 Carregando dados anteriores...")

    # Tenta carregar dados salvos
    minha_carteira.carregar_json()

    print("✅ Sistema pronto para uso!\n")

    # Inicia o menu
    menu.menu()


# Executa apenas se o arquivo for rodado diretamente
if __name__ == "__main__":
    main()