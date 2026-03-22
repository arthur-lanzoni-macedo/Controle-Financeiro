## 📊 Gerenciador Financeiro Pro — POO & JSON
Este projeto é uma aplicação de terminal desenvolvida em Python que utiliza os pilares da Programação Orientada a Objetos (POO) para gerenciar finanças pessoais. O sistema agora conta com persistência de dados, permitindo salvar e carregar transações automaticamente.

*🚀 Novidades da Versão*
- Persistência em JSON: Seus dados não somem ao fechar o programa.
- Análise de Gastos: Identificação automática da categoria onde você mais gasta.
- Relatórios Detalhados: Soma de totais de receitas e despesas separadamente.

*🛠️ Tecnologias e Conceitos*
- 🐍 Python 3.x
- Utilização de manipulação de arquivos, dicionários e listas.

## 🏛️ Programação Orientada a Objetos:
- Classes e Objetos: Estruturação das entidades Transacao, Receita, Despesa e Carteira.
- Herança: Receita e Despesa herdam atributos de Transacao.
- Polimorfismo: O método impacto_saldo() executa comportamentos diferentes (soma ou subtração) dependendo do tipo do objeto.
- Encapsulamento: A classe Carteira centraliza a lógica de negócio e proteção do saldo.

## 🏗️ Estrutura do Código
- Transacao: Classe base com descricao, valor e categoria. Possui o método to_dict() para conversão de dados.
- Receita / Despesa: Classes especializadas que definem como cada valor afeta o saldo.
- Carteira: O motor do sistema. Gerencia a lista de transações, calcula totais, filtra categorias e manipula o arquivo transacao.json.

## 📂 Persistência de Dados
- O sistema utiliza um arquivo chamado transacao.json para armazenar as informações.
- Leitura: Ao iniciar, o sistema tenta carregar transações existentes.
- Escrita: Ao finalizar, todas as operações da sessão são salvas automaticamente.

## 📋 Exemplo de Saída
```
========== 📂 SISTEMA DE FINANÇAS ==========
🔄 Carregando dados anteriores...
📊 Dados existentes carregados com sucesso!

========== 📜 EXTRATO DETALHADO ==========
Salário Mensal | 5000.0 | Trabalho
Mercado Semanal | 420.5 | Alimentacao

========== 💰 RESUMO DE SALDO ==========
Saldo atual: R$ 4579.5

========== 📊 ANÁLISE POR CATEGORIA ==========
Gastos por categoria:
Alimentacao → R$ 420.50

========== 🔍 DESTAQUES DE CONSUMO ==========
Maior despesa: R$ 420.50
Categoria com maior gasto: Alimentacao — R$ 420.50

***********************************
💾 Salvando dados no banco JSON...
✅ Operação finalizada com sucesso!
***********************************
```
## ⚙️ Como Executar
- Certifique-se de ter o Python 3 instalado.
- Salve o código em um arquivo main.py.
- Execute no terminal:
```
python main.py
```
**Feito por Arthur Lanzoni**
