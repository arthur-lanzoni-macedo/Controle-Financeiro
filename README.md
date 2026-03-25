## 📊 Gerenciador Financeiro Pro — POO & JSON
Este projeto é uma aplicação de terminal robusta desenvolvida em Python, focada na gestão de finanças pessoais. Utilizando os pilares da Programação Orientada a Objetos (POO) e persistência de dados em JSON, o sistema oferece uma estrutura escalável para controle de receitas e despesas.

*🚀 Novidades da Versão 2.0*

💾 Persistência Automática: Integração com transacao.json para salvar e carregar dados entre sessões.

🧠 Inteligência de Negócio: Algoritmo para identificação automática da categoria com maior índice de gastos.
📈 Relatórios Analíticos: Separação lógica entre fluxos de entrada (Receitas) e saída (Despesas).

🎨 Terminal UX: Interface estilizada com emojis e divisores visuais para melhor legibilidade.

🏛️ Arquitetura e Conceitos de POO
O sistema foi desenhado seguindo padrões de engenharia de software para garantir código limpo e reutilizável:

- Classes e Objetos: Entidades bem definidas como Transacao, Receita, Despesa e Carteira.

- Herança: Receita e Despesa herdam atributos base de Transacao, reduzindo a duplicidade de código.

- Polimorfismo: O método impacto_saldo() comporta-se de forma distinta conforme o tipo do objeto, somando ou subtraindo valores do montante total.

- Encapsulamento: A classe Carteira atua como o núcleo do sistema, protegendo a lógica de cálculo e a manipulação direta do arquivo de dados.

## 🏗️ Estrutura do Código
- Transacao: Classe abstrata/base contendo descricao, valor e categoria. Inclui o método to_dict() para serialização.

- Receita / Despesa: Especializações que definem a natureza do impacto financeiro.

- Carteira: O motor do sistema. Gerencia a lista de objetos, realiza o parsing do JSON, filtra categorias e gera as estatísticas.

*📂 Fluxo de Persistência (JSON)*
O sistema opera com um ciclo de vida de dados seguro:

- Leitura (Startup): Busca o arquivo transacao.json. Caso não exista, inicia uma nova carteira vazia.

- Processamento: Transforma dicionários JSON em instâncias de objetos vivos na memória.

- Escrita (Shutdown): Converte os objetos de volta para JSON, garantindo a integridade da informação.

## 📋 Exemplo de Interface
```
==========================================
        📂 SISTEMA DE FINANÇAS
==========================================
🔄 Carregando dados anteriores...
✅ Dados carregados com sucesso!

========== 📜 EXTRATO DETALHADO ==========
➕ Salário Mensal   | R$ 5000.00 | 💼 Trabalho
➖ Mercado Semanal  | R$ 420.50  | 🛒 Alimentação

========== 💰 RESUMO DE SALDO ==========
Saldo atual: R$ 4579.50

========== 📊 ANÁLISE POR CATEGORIA ==========
🛒 Alimentação   → R$ 420.50
💼 Trabalho      → R$ 5000.00

========== 🔍 DESTAQUES DE CONSUMO ==========
🚨 Maior despesa: R$ 420.50
🏆 Categoria com maior gasto: Alimentação

******************************************
💾 Salvando transações em transacao.json...
✨ Operação finalizada com sucesso!`
******************************************
```
*⚙️ Como Executar*
Certifique-se de ter o Python 3.10+ instalado.

Clone o repositório ou salve o código em main.py.
Execute no terminal:
```
Bash
python main.py
```

Desenvolvido por Arthur Lanzoni
