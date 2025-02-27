Título: TP3 - Conversor de MarkDown para HTML
Autor: Jorge Costa, A104617
Resumo:
   - Programa em Python que converte um pequeno texto em MarkDown para HTML;
   - Conversões implementadas:
   - Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
     Input: # Exemplo -> Output: <h1>Exemplo</h1>
     Input: ## Exemplo -> Output: <h2>Exemplo</h2>
     Input: ### Exemplo -> Output: <h3>Exemplo</h3>
   - Bold: pedaços de texto entre "**"
     Input: Este é um **exemplo** ... -> Output: Este é um <b>exemplo</b> ...
   - Itálico: pedaços de texto entre "*"
     Input: Este é um *exemplo* ... -> Output: Este é um <i>exemplo</i> ...
   - Lista numerada.
     Input:
       1. Primeiro item
       2. Segundo item
       3. Terceiro item
     Output:
       <ol>
       ‹li>Primeiro item</li>
       ‹li>Segundo item</li>
       ‹li>Terceiro item</li>
       </ol>
   - Link: [texto] (endereço URL)
     Input: Como pode ser consultado em [página da UC](http://www.uc.pt) -> Output: Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>
   - Imagem: ![texto alternativo] (path para a imagem)
     Input: Como se vê na imagem seguinte: ![imagem dum coelho] (http://www.coellho.comb... -> Output: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...
   - Implementação da solução: especificação dos grupos de captura com padroes em regex, e inserção da informação dos mesmos no formato de formatação em HTML.
   - A expressão regex de Link e de Imagem são bastante semelhantes. A maior diferença é que a expressão para a Imagem exige um '!' antes de '[texto alternativo]',
    enquanto que a expressão de link usa um negative lookbehind para evitar capturar imagens por engano.