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
    pass