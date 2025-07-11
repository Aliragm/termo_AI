import random
import unicodedata

def remover_acentos(palavra):
    return ''.join(
        c for c in unicodedata.normalize('NFD', palavra)
        if unicodedata.category(c) != 'Mn'
    )

def sorteio():
    with open('palavras_comuns.txt', 'r', encoding='utf-8') as arquivo:
        palavras = [remover_acentos(linha.strip()) for linha in arquivo if linha.strip()]
    return random.choice(palavras)

def verificador(verificado):
    with open('palavras_comuns.txt', 'r', encoding='utf-8') as arquivo:
        palavras = [linha.strip() for linha in arquivo if linha.strip()]
    if verificado in palavras:
        return True
    else:
        print("palavra não consta.")
        return False