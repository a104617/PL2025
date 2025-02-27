import re

def converter_markdown_para_html(exemplo_markdown):
    output_html = ""
    dentro_lista = False
    padrao_cabeçalho = re.compile(r'^(#{1,3})\s+(.*)')
    padrao_bold = re.compile(r'\*\*(.*?)\*\*')
    padrao_italico = re.compile(r'\*(.*?)\*')
    padrao_lista = re.compile(r'^\d+\.\s+(.*)')
    padrao_link = re.compile(r'(?<!!)\[(.*?)\]\((.*?)\)')
    padrao_imagem = re.compile(r'!\[(.*?)\]\((.*?)\)')

    for linha in exemplo_markdown.split("\n"):
        # cabeçalhos
        cabeçalho = padrao_cabeçalho.match(linha)
        if cabeçalho:
            if dentro_lista:
                output_html += "</ol>\n"
                dentro_lista = False
            num_cabeçalho = len(cabeçalho.group(1))
            header = cabeçalho.group(2)
            match = f"<h{num_cabeçalho}>{header}</h{num_cabeçalho}>"
        
        # bold
        match = padrao_bold.sub(r'<b>\1</b>', linha)
        
        # itálico
        match = padrao_italico.sub(r'<i>\1</i>', linha)

        # lista numerada
        lista = padrao_lista.match(linha)
        if lista:
            if not dentro_lista:
                output_html += "<ol>\n"
                dentro_lista = True
            texto_item_lista = lista.group(1)
            linha = f"<li>{texto_item_lista}</li>"
        else:
            if dentro_lista:
                output_html += "</ol>\n"
                dentro_lista = False

        # imagem
        match = padrao_imagem.sub(r'<img src="\2" alt="\1"/>', linha)
        
        # link
        match = padrao_link.sub(r'<a href="\2">\1</a>', linha)

        output_html = output_html + match + "\n"
    
    if dentro_lista:
        output_html += "</ol>\n"

    return output_html


def main():
    exemplo_markdown = """# Exemplo
## Outro Exemplo
### Mais um Exemplo
Este é um **exemplo** de texto em *Markdown*.
1. Primeiro item
2. Segundo item
3. Terceiro item
Como pode ser consultado em [página da UC](http://www.uc.pt)
Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)
"""
    output_html = converter_markdown_para_html(exemplo_markdown)
    print(output_html)


if __name__ == "__main__":
    main()
