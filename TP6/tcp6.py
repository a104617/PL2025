import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, expressao):
        self.scanner = re.Scanner([
            (r"\d+", lambda scanner, token: Token("NUMERO", int(token))),
            (r"[+\-*/]", lambda scanner, token: Token("OP", token)),
            (r"[()]", lambda scanner, token: Token("PAREN", token)),
            (r"\s+", None),
        ])
        self.tokens, _ = self.scanner.scan(expressao)
        self.pos = 0

    def proximo_token(self):
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            self.pos += 1
            return token
        return None

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.token_atual = self.lexer.proximo_token()

    def consumir(self):
        self.token_atual = self.lexer.proximo_token()
    
    def parse(self):
        return self.expressao()
    
    def expressao(self):
        resultado = self.termo()
        while self.token_atual and self.token_atual.value in ('+', '-'):
            op = self.token_atual.value
            self.consumir()
            resultado = resultado + self.termo() if op == '+' else resultado - self.termo()
        return resultado

    def termo(self):
        resultado = self.fator()
        while self.token_atual and self.token_atual.value in ('*', '/'):
            op = self.token_atual.value
            self.consumir()
            resultado = resultado * self.fator() if op == '*' else resultado / self.fator()
        return resultado

    def fator(self):
        if self.token_atual.type == 'NUMERO':
            valor = self.token_atual.value
            self.consumir()
            return valor
        elif self.token_atual.value == '(':
            self.consumir()
            resultado = self.expressao()
            if self.token_atual.value != ')':
                raise SyntaxError("Falta um ')'")
            self.consumir()
            return resultado
        else:
            raise SyntaxError("Token inesperado!")

expressao = "2 * 4 - (1 * (2 * 2)) + 4"
lexer = Lexer(expressao)
parser = Parser(lexer)
resultado = parser.parse()
print(f"Resultado da expressão '{expressao}': {resultado}")
