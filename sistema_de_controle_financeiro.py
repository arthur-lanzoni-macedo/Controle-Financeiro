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
 
    def gasto_por_categoria(self):
        gasto_categoria = {}
        
        for transacao_por_categoria in self.transacoes:
            if isinstance(transacao_por_categoria, Despesa):
                categoria_atual = transacao_por_categoria.categoria
                valor_atual = transacao_por_categoria.valor
                
                if categoria_atual in gasto_categoria:
                    gasto_categoria[categoria_atual] += valor_atual
                else:
                    gasto_categoria[categoria_atual] = valor_atual
        
        print("📋 Gastos por Categoria")
        print("-" * 23)
        
        for categoria, total in gasto_categoria.items():
            print(f"{categoria} → R$ {total:.2f}")
            
    def categoria_maior_gasto(self):
        gasto_por_categoria = {}
        
        for transacao_por_categoria in self.transacoes:
            if isinstance(transacao_por_categoria, Despesa):
                categoria_atual = transacao_por_categoria.categoria
                valor_atual = transacao_por_categoria.valor
                
                if categoria_atual in gasto_por_categoria:
                    gasto_por_categoria[categoria_atual] += valor_atual
                else:
                    gasto_por_categoria[categoria_atual] = valor_atual
                      
        categoria_com_maior_gasto = None
        maior_valor = 0
                
        for categoria, valor in gasto_por_categoria.items():
                        
            if valor > maior_valor:
                maior_valor = valor
                categoria_com_maior_gasto = categoria
            
        print("\n🏆 Destaque de Gastos")
        print("-" * 23)

        if categoria_com_maior_gasto:
            print(f"Maior Gasto: {categoria_com_maior_gasto}")
            print(f"Valor Total: R$ {maior_valor:.2f}")
        else:
            print("❌ Nenhuma despesa encontrada para análise.")
        
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

print("\n--- Análise por Categoria ---")
minha_carteira.gasto_por_categoria()

print("\n--- Maior Despesa Individual ---")
minha_carteira.maior_gasto()

print("\n--- Categoria com Maior Gasto ---")
minha_carteira.categoria_maior_gasto()