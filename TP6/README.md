Título: TP6 - Lexer e Parser de Expressões Aritméticas
Autor: Jorge Costa, A104617

Resumo:
   Este programa em Python implementa um analisador léxico (lexer) e um analisador sintático (parser) para avaliar expressões matemáticas que envolvem adição, subtração, multiplicação, divisão e parênteses, seguindo regras de precedência. O lexer usa expressões regulares para converter a string da expressão numa lista de tokens (números, operadores e parênteses). O parser analisa esses tokens de forma recursiva, seguindo a estrutura da gramática definida, onde uma expressão é composta por termos, termos por fatores e fatores por números ou expressões entre parênteses. Finalmente, a expressão é avaliada respeitando a precedência dos operadores e retorna o resultado.

Detalhes de Implementação:
   A gramática utilizada nesse analisador sintático (parser) é uma gramática livre de contexto (CFG) que define expressões aritméticas com adição, subtração, multiplicação, divisão e parênteses.
      expressão -> termo (("+" | "-") termo)*
      termo -> fator (("*" | "/") fator)*
      fator -> NUMERO | "(" expressão ")"
   
   1. Uma expressão pode conter termos conectados por + ou -.
   Exemplo: 3 + 5, 10 - 2 + 4
   2. Um termo pode conter fatores conectados por * ou /.
   Exemplo: 2 * 3, 8 / 4 * 2
   3. Um fator pode ser:
   Um número (ex: 5, 10)
   Uma expressão entre parênteses (ex: (3 + 2))
   
   Ordem de prioridade:
   1. Trata dos parênteses primeiro.
   2. Depois, multiplicação e divisão.
   3. Por fim, soma e subtração.
   Exemplo: 2 * 4 - (1 * (2 * 2)) + 4
      Parênteses internos: (2 * 2) → 4
      Multiplicação interna: 1 * 4 → 4
      Multiplicações externas: 2 * 4 → 8
      Subtração: 8 - 4 → 4
      Soma final: 4 + 4 → 8

