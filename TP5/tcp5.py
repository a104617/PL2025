import json
from datetime import datetime
import ply.lex as lex

tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR',
    'ADICIONAR'
)

def t_LISTAR(t):
    r'LISTAR'
    return t

def t_MOEDA(t):
    r'MOEDA\s+([\d]+[ec],?\s*)+\.'
    t.value = t.value[6:].strip(" .")
    return t

def t_SELECIONAR(t):
    r'SELECIONAR\s+[A-Za-z]\d{2}'
    return t

def t_SAIR(t):
    r'SAIR'
    return t

def t_ADICIONAR(t):
    r'ADICIONAR'
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Comando inválido: {t.value[0]}")
    t.lexer.skip(1)

class AutomatoMoedas:
    def __init__(self):
        self.saldo = 0
        self.moedas_validas = {'1e': 100, '2e': 200, '50c': 50, '20c': 20, '10c': 10, '5c': 5, '2c': 2, '1c': 1}

    def processar_moedas(self, moedas):
        for moeda in moedas.split(","):
            moeda = moeda.strip()
            if moeda in self.moedas_validas:
                self.saldo += self.moedas_validas[moeda]
            else:
                print(f"maq: Moeda inválida: {moeda}")
        return self.saldo

class MaquinaVending:
    def __init__(self):
        self.stock = carregar_stock()
        self.saldo = 0
        self.estado = "INICIO"
        self.lexer = lex.lex()
        self.automato_moedas = AutomatoMoedas()
        print(f"maq: {datetime.now().strftime('%Y-%m-%d')}, Stock carregado, Estado atualizado.")
        print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    def processar_comando(self, comando):
        self.lexer.input(comando)
        for token in self.lexer:
            if self.estado == "INICIO":
                if token.type == "LISTAR":
                    self.estado = "LISTAGEM"
                elif token.type == "MOEDA":
                    self.estado = "INSERCAO_MOEDAS"
                elif token.type == "SELECIONAR":
                    self.estado = "SELECAO_PRODUTO"
                elif token.type == "SAIR":
                    self.estado = "SAIDA"
                elif token.type == "ADICIONAR":
                    self.estado = "ADICAO_PRODUTO"
                else:
                    print("maq: Comando inválido.")

            if self.estado == "LISTAGEM":
                self.listar_produtos()
                self.estado = "INICIO"

            elif self.estado == "INSERCAO_MOEDAS":
                self.processar_moedas(token.value)
                self.estado = "INICIO"

            elif self.estado == "SELECAO_PRODUTO":
                self.selecionar_produto(token.value)
                self.estado = "INICIO"

            elif self.estado == "SAIDA":
                self.sair()
                break

            elif self.estado == "ADICAO_PRODUTO":
                self.adicionar_produto()
                self.estado = "INICIO"

    def listar_produtos(self):
        print(f"{'cod':<6} | {'nome':<14} | {'quantidade':>10} | {'preço':>6}")
        print("-" * 45)
        for produto in self.stock:
            cod = produto['cod'].ljust(6)
            nome = produto['nome'].ljust(14)
            quant = str(produto['quant']).rjust(10)
            preco = f"{produto['preco']:.2f}€".rjust(6)
            print(f"{cod} | {nome} | {quant} | {preco}")

    def processar_moedas(self, moedas):
        self.saldo = self.automato_moedas.processar_moedas(moedas)
        if self.saldo >= 100:
            print(f"maq: Saldo = {self.saldo//100}e{self.saldo%100}c")
        else:
            print(f"maq: Saldo = {self.saldo}c")

    def selecionar_produto(self, comando):
        cod = comando.split()[1]
        produto = next((p for p in self.stock if p["cod"] == cod), None)
        if produto:
            if produto["quant"] > 0:
                if self.saldo >= produto["preco"] * 100:
                    self.saldo -= int(produto["preco"] * 100)
                    produto["quant"] -= 1
                    print(f'maq: Pode retirar o produto dispensado "{produto["nome"]}"')
                    if self.saldo >= 100:
                        print(f"maq: Saldo = {self.saldo//100}e{self.saldo%100}c")
                    else:
                        print(f"maq: Saldo = {self.saldo}c")
                else:
                    print("maq: Saldo insuficiente para satisfazer o seu pedido")
                    if self.saldo >= 100:
                        print(f"maq: Saldo = {self.saldo//100}e{self.saldo%100}c; Pedido = {produto['preco']:.2f}€")
                    else:
                        print(f"maq: Saldo = {self.saldo}c; Pedido = {produto['preco']:.2f}€")
            else:
                print("maq: Produto esgotado")
        else:
            print("maq: Produto inexistente")

    def sair(self):
        troco = calcular_troco(self.saldo)
        if troco:
            print("maq: Pode retirar o troco:", end=" ")
            for moeda, quantidade in troco.items():
                if moeda >= 100:
                    print(f"{quantidade}x {moeda//100}e", end=", ")
                else:
                    print(f"{quantidade}x {moeda}c", end=", ")
            print("\b\b.")
        else:
            print("maq: Não há troco para retirar.")
        print("maq: Até à próxima")
        salvar_stock(self.stock)

    def adicionar_produto(self):
        try:
            cod = input("Código do produto: ").strip()
            nome = input("Nome do produto: ").strip()
            quant = int(input("Quantidade: ").strip())
            preco = float(input("Preço (em euros): ").strip())
            adicionar_produto(self.stock, cod, nome, quant, preco)
            print("maq: Produto adicionado com sucesso.")
        except ValueError:
            print("maq: Entrada inválida. Certifique-se de que a quantidade é um número inteiro e o preço é um número decimal.")

def carregar_stock():
    try:
        with open("stock.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("maq: Erro ao carregar o estoque. Criando um novo stock vazio.")
        return []

def salvar_stock(stock):
    with open("stock.json", "w") as f:
        json.dump(stock, f, indent=4)

def calcular_troco(saldo):
    moedas = [200, 100, 50, 20, 10, 5, 2, 1]
    troco = {}
    for moeda in moedas:
        if saldo >= moeda:
            troco[moeda] = saldo // moeda
            saldo %= moeda
    return troco

def adicionar_produto(stock, cod, nome, quant, preco):
    for produto in stock:
        if produto["cod"] == cod:
            produto["quant"] += quant
            return
    stock.append({"cod": cod, "nome": nome, "quant": quant, "preco": preco})

if __name__ == "__main__":
    maquina = MaquinaVending()
    while True:
        comando = input("> ").strip()
        maquina.processar_comando(comando)
        if maquina.estado == "SAIDA":
            break
