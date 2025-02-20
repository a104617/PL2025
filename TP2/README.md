Título: TP2 - Análise de um dataset de obras musicais
Autor: Jorge Costa, A104617
Resumo:
   - Programa em Python que lê e processa um dataset de obras musicais;
   - Não é permitida a utilização do módulo CSV do Python;
   - Estrutura do dataset: nome;desc;anoCriacao;periodo;compositor;duracao;_id;
   - A primeira linha do dataset que identifica os parâmetros é descartada;
   - Uma obra musical pode ocupar mais do que uma linha no ficheiro CSV;
   - Apenas a informação referente ao nome da obra musical, compositor musical, e período é armazenada em memória;
   - O programa cria uma lista ordenada alfabeticamente dos compositores musicais; 
   - O programa indica o número de obras por período; 
   - O programa cria um dicionário onde cada período corresponde a uma chave, e para cada chave existe um valor que corresponde a uma lista alfabética dos títulos das obras desse período;
   - Das 174 obras do dataset, 18 são classificadas de forma equivocada (10%) em relação aos parâmetros nome, compositor musical e período, devido à existência de caracteres ";" entre os delimitadores de parâmetros do ficheiro CSV;
   - Não são utilizadas expressões regulares na identificação dos parâmetros, mas a sua utilização resultaria num output análogo.