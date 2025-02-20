class ObraMusical:
    def __init__(self, nome, periodo, compositor):
        self.nome = nome
        self.periodo = periodo
        self.compositor = compositor

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"Período: {self.periodo}\n"
                f"Compositor: {self.compositor}\n")

 
def ler_dataset_obras_musicais(ficheiro):
    with open(ficheiro, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    first_line = True
    i = 0
    line_break = True
    nome = []
    periodo = []
    compositor = []
    obras_musicais = []
    for c in conteudo:
        if first_line:
            if c == ';':
                i = i + 1
            if i == 6:
                first_line = False
                i = 1
            continue
        if i == 1:
            if (line_break):
                if (c == '\n'):
                    line_break = False
                continue
            if (c == ';'):
                i = i + 1
                continue
            nome.append(c)
            continue
        if (i == 2 or i == 3):
            if (c == ';'):
                i = i + 1
            continue
        if (i == 4 or i == 5):
            if (c == ';'):
                i = i + 1
                continue
            if (i == 4):
                periodo.append(c)
            else:
                compositor.append(c)
            continue
        if (i == 6):
            if (c == ';'):
                i = 1
                obras_musicais.append(ObraMusical(''.join(nome),''.join(periodo),''.join(compositor)))
                nome = []
                periodo = []
                compositor = []
                line_break = True
                
    return obras_musicais


def lista_compositores(obras):
    return sorted(set(obra.compositor for obra in obras))


def distribuicao_por_periodo(obras):
    distribuicao = {}
    for obra in obras:
        distribuicao[obra.periodo] = distribuicao.get(obra.periodo, 0) + 1
    return distribuicao


def obras_por_periodo(dados):
    periodos = {}
    for obra in obras:
        if obra.periodo not in periodos:
            periodos[obra.periodo] = []
        periodos[obra.periodo].append(obra.nome)
    
    for periodo in periodos:
        periodos[periodo].sort()
    
    return periodos


if __name__ == "__main__":
    ficheiro = "obras.csv"
    obras = ler_dataset_obras_musicais(ficheiro)

    print("Lista ordenada de compositores:")
    print(lista_compositores(obras))
    
    print("\nDistribuição das obras por período:")
    print(distribuicao_por_periodo(obras))
    
    print("\nDicionário de obras por período:")
    print(obras_por_periodo(obras))

