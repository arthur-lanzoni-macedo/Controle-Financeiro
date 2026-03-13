## 📊 Gerenciador Financeiro — POO
Este projeto é uma aplicação de terminal desenvolvida em Python que utiliza os pilares da Programação Orientada a Objetos para gerenciar transações financeiras. O sistema permite o registro de receitas e despesas, calculando o saldo final e gerando um extrato detalhado.
## 🛠️ Tecnologias e Conceitos Utilizados
- Python 3.x: Linguagem principal.

## POO (Programação Orientada a Objetos):

- Classes e Objetos: Estruturação de Transacao, Carteira, etc.
- Herança: As classes Receita e Despesa herdam atributos e métodos da classe base Transacao.
- Polimorfismo: O método impacto_saldo() é implementado de formas diferentes para receitas e despesas.
- Encapsulamento: Gerenciamento do estado do saldo dentro da classe Carteira.

## 🏗️ Estrutura do Código
***O sistema é dividido em quatro classes principais:***

- Transacao: Classe base que armazena descrição, valor e categoria.
- Receita: Especialização que soma o valor ao saldo.
- Despesa: Especialização que subtrai o valor do saldo.
- Carteira: Atua como o "cérebro" do sistema, armazenando a lista de transações e atualizando o saldo total.

## 🚀 Como Executar
- Certifique-se de ter o Python instalado.
- Copie o código para um arquivo chamado main.py.

**Execute o comando:**
```
bash
Copy code
python main.py
```
## 📋 Exemplo de Saída
```
--- Processando Transações ---
✅ Sucesso: R$ +5000.00 adicionado ao saldo
✅ Sucesso: R$ +350.00 adicionado ao saldo
⚠️ Saída: R$ -420.50 debitado com sucesso
⚠️ Saída: R$ -25.00 debitado com sucesso
⚠️ Saída: R$ -45.00 debitado com sucesso

--- Extrato Detalhado ---
Salário Mensal | 5000.0 | Trabalho
Freelance Logo | 350.0 | Design
Mercado Semanal | 420.5 | Alimentação
Uber Shopping | 25.0 | Transporte
Ingresso Cinema | 45.0 | Lazer
--- Resumo Financeiro ---
Saldo atual: R$ 4859.5
```

***Feitopor Arthur Lanzoni***
