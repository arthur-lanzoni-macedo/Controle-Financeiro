class Transacao:
    def __init__(self, descricao, valor, categoria):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        
    def mostrar_transacao(self):
        print(f'{self.descricao} | {self.valor} | {self.categoria}')
        
class Receita(Transacao):
    def impacto_saldo(self):
        print(f'✅ Sucesso: R$ +{self.valor:.2f} adicionado ao saldo')
        return +self.valor

class Despesa(Transacao):
    def impacto_saldo(self):
        print(f'⚠️ Saída: R$ -{self.valor:.2f} debitado com sucesso')
        return -self.valor

class Carteira:
    def __init__(self):
        self.saldo = 0
        self.transacoes = []
        
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
        
        self.saldo += transacao.impacto_saldo()
        
    def mostrar_saldo(self):
        print(f'Saldo atual: R$ {self.saldo}')
        
    def mostrar_transacoes(self):
        for transacao in self.transacoes:
            transacao.mostrar_transacao()
            
    def total_receitas(self):
        total = 0
        
        for transacao in self.transacoes:
            if isinstance(transacao, Receita):
                total += transacao.valor
        
        print(f'📈 [SUCESSO] Cálculo de Receitas finalizado! Total: R$ {total:.2f} ✅')
        
    def total_despesas(self):
        total = 0
        
        for transacao in self.transacoes:
            if isinstance(transacao, Despesa):
                total += transacao.valor
        
        print(f'📉 [SUCESSO] Cálculo de Despesas finalizado! Total: R$ {total:.2f} ✅')
        
    def maior_gasto(self):
        maior_valor = 0
        
        for transacao in self.transacoes:
            if isinstance(transacao, Despesa):
                
                if maior_valor == 0 or transacao.valor > maior_valor:
                    if maior_valor < transacao.valor:
                        maior_valor = transacao.valor
            
        print(f"📉 [SUCESSO] Busca finalizada! Maior despesa encontrada: R$ {maior_valor:.2f} ✅")


# CLASSE EM ANDAMENTO
 
    def gasto_por_categoria(self):
        gasto_categoria = {}
        
        for transacao_por_categoria in self.transacoes:
            if isinstance(transacao_por_categoria, Despesa):
                
                if transacao_por_categoria in self.transacoes:
                    sum(transacao_por_categoria.valor)
                else:
                    gasto_categoria = {'transacao_por_categoria.categoria', transacao_por_categoria.valor}
                    
                    print('📋 Listagem de Despesas:')
                    print('-' * 25)
                    print(f'{transacao_por_categoria.categoria} → {transacao_por_categoria.valor:.2f}')
                
            
# Teste Final

minha_carteira = Carteira()

t1 = Receita('Salário Mensal', 5000.00, 'Trabalho')
t2 = Receita('Freelance Logo', 350.00, 'Design')
t3 = Despesa('Mercado Semanal', 420.50, 'Alimentação')
t4 = Despesa('Uber Shopping', 25.00, 'Transporte')
t5 = Despesa('Ingresso Cinema', 45.00, 'Lazer')

print('--- Processando Transações ---')
minha_carteira.adicionar_transacao(t1)
minha_carteira.adicionar_transacao(t2)
minha_carteira.adicionar_transacao(t3)
minha_carteira.adicionar_transacao(t4)
minha_carteira.adicionar_transacao(t5)

print('\n--- Extrato Detalhado ---')
minha_carteira.mostrar_transacoes()

print('\n--- Resumo Financeiro ---')
minha_carteira.mostrar_saldo()

print('\n--- Estatísticas Financeiras ---')
minha_carteira.total_receitas()
minha_carteira.total_despesas()
minha_carteira.maior_gasto()