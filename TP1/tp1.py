
import sys

try:
    print("Escreva o Texto de entrada (Ctrl+C para sair):")
    comp_ligado = True
    comp_desligado = False
    soma = 0
    valor_atual = 0
    fst = False
    snd = False
    for linha in sys.stdin:
        linha = linha.strip()
        for c in linha:
            if c.isdigit() and comp_ligado:
                valor_atual = (valor_atual * 10) + int(c)
                continue
            soma = soma + valor_atual
            valor_atual = 0
            if c.lower() not in 'onf=':
                fst, snd = False, False
                continue
            if c.lower() == 'o':
                    fst= True
            if c.lower() == 'n':
                if fst:
                    comp_ligado, comp_desligado = True, False
            if c.lower() == 'f':
                if fst:
                    if snd:
                        comp_desligado, comp_ligado = True, False
                    else:
                        snd = True
            if c == '=':
                print(f">> {soma}")
                
except KeyboardInterrupt:
    soma = soma + valor_atual
    print(f">> {soma}")




