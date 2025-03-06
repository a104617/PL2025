Título: TP4 - Analisador Léxico
Autor: Jorge Costa, A104617
Resumo:
   - Programa em Python que implementa um analisador léxico de uma linguagem de query;
   - Género de frases da linguagem que pode receber como input: 
   ''' # DBPedia: obras de Chuck Berry
   select ?nome ?desc where {
      ?s a dbo:MusicalArtist.
      ?s foaf:name "Chuck Berry"@en.
      ?w dbo:artist ?s.
      ?w foaf:name ?nome.
      ?w dbo:abstract ?desc
   } LIMIT 1000 '''
   - Neste analisador léxico, os tokens são as unidades básicas que representam os componentes da linguagem de query;
   - Os tokens SELECT, WHERE e LIMIT correspondem a palavras reservadas na linguagem, e cada um tem a sua expressão regular para captura;
   - Variáveis, representadas por VARIABLE, são identificadas pelo prefixo ? seguido de letras, numeros ou underscores (ex: ?nome);
   - Os recursos são representados por IRI, e seguem o formato prefixo:valor (ex: dbo:MusicalArtist);
   - Strings, como "Chuck Berry"@en, são capturadas pelo token STRING, e números inteiros são reconhecidos como NUMBER;
   - Símbolos especiais, como {, }, ., :, @, =, e ,, são representados pelos tokens LBRACE, RBRACE, DOT, COLON, AT, EQUALS, e COMMA, respectivamente;
   - A função t_newline conta as linhas do input, incrementando para cada uma o contador lineno do lexer;
   - A linha "# DBPedia: obras de Chuck Berry" é completamente ignorada pelo lexer, devido à função t_COMMENT;
   - O lexer relata erros para texto inválido, como a palavra "a" na linha 4 do exemplo, que não corresponde a nenhum token válido no contexto da query.