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
            
# Teste Final

minha_carteira = Carteira()

t1 = Receita("Salário Mensal", 5000.00, "Trabalho")
t2 = Receita("Freelance Logo", 350.00, "Design")
t3 = Despesa("Mercado Semanal", 420.50, "Alimentação")
t4 = Despesa("Uber Shopping", 25.00, "Transporte")
t5 = Despesa("Ingresso Cinema", 45.00, "Lazer")

print("--- Processando Transações ---")
minha_carteira.adicionar_transacao(t1)
minha_carteira.adicionar_transacao(t2)
minha_carteira.adicionar_transacao(t3)
minha_carteira.adicionar_transacao(t4)
minha_carteira.adicionar_transacao(t5)

print("\n--- Extrato Detalhado ---")
minha_carteira.mostrar_transacoes()

print("\n--- Resumo Financeiro ---")
minha_carteira.mostrar_saldo()