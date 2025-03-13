Título: TP5 - Máquina de Vending
Autor: Jorge Costa, A104617

Resumo:
   1. Programa em Python que simula uma Máquina de Vending.
   2. A máquina tem um stock de produtos num ficheiro JSON que é carregado no início do programa e atualizado no final.
   3. Operações implementadas:
      - Listar produtos: Mostra os produtos disponíveis, respectivas quantidades e preços.
      - Inserir moedas: Aceita moedas válidas e soma ao saldo do utilizador.
      - Selecionar produto: Permite comprar um produto se houver saldo suficiente e stock disponível.
      - Adicionar produto: Permite a inserção de novos produtos no stock.
      - Sair: Finaliza a operação e retorna o troco, se houver.

Detalhes de Implementação:
   1. Classe AutomatoMoedas:
      - Usa um autómato finito para processar as moedas inseridas, verificando se são válidas e atualizando o saldo.
   2. Classe MaquinaVending:
      - Utiliza ply.lex para tokenização e um autómato finito (AF) para gerir os estados possíveis, tornando o programa modular e fácil de expandir.
      - O ply.lex é utilizado para identificar, validar e processar os comandos de forma eficiente.
      - Processa os comandos do utilizador, como LISTAR, MOEDA, SELECIONAR, SAIR e ADICIONAR.
      - O AF mantém o estado da máquina (ex: INICIO, LISTAGEM, INSERCAO_MOEDAS, etc.).
      - Faz a gestão do stock, carregando e guardando num ficheiro JSON (stock.json).
      - Calcula o troco e mostra as mensagens adequadas.

Exemplo de Interação:
   1. LISTAR:
      cod    | nome           | quantidade | preço
      -------------------------------------------------
      A23    | água 0.5L      |          8 |  0.70€
      B12    | chocolate      |          5 |  1.20€
      C45    | bolacha        |          3 |  0.50€
   2. MOEDA 1e, 20c, 5c, 5c .:
      maq: Saldo = 1e30c
   3. SELECIONAR A23:
      maq: Pode retirar o produto dispensado "água 0.5L"
      maq: Saldo = 60c
   4. SAIR:
      maq: Pode retirar o troco: 1x 50c, 1x 10c.
      maq: Até à próxima