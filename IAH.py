import sorteio as srt
from collections import Counter

with open('palavras_comuns.txt', 'r', encoding='utf-8') as arquivo:
    palavras = [srt.remover_acentos(linha.strip()) for linha in arquivo if linha.strip()]

ultimo_resultado = ""
ultima_palavra_usada = ""
letras_eliminadas = []
letras_presentes = []
letras_com_posicao_correta = []
palavras_testadas = []
palavras_possiveis = palavras.copy()

def captar_resultado(palavra, resultado):
    global ultimo_resultado, ultima_palavra_usada
    ultimo_resultado = resultado
    ultima_palavra_usada = palavra

def palavra_valida(palavra):
    for letra, pos in letras_com_posicao_correta:
        if palavra[pos] != letra:
            return False
    for letra, pos_errada in letras_presentes:
        if letra not in palavra or palavra[pos_errada] == letra:
            return False
    for letra in letras_eliminadas:
        if letra in palavra:
            if not any(l == letra for l, _ in letras_presentes + letras_com_posicao_correta):
                return False
    return True

def eliminar_palavras():
    global palavras_possiveis
    palavras_possiveis = [p for p in palavras_possiveis if palavra_valida(p)]

def heuristica():
    #HEURÍSTICA: Escolhe a melhor palavra para chutar com base na frequência
    #de letras nas palavras ainda possíveis.
    #O objetivo é maximizar a informação obtida.

    freq_letras = Counter()
    for palavra in palavras_possiveis:
        freq_letras.update(set(palavra))

    melhor_palavra = ""
    max_score = -1

    for palavra_candidata in palavras:
        if palavra_candidata in palavras_testadas:
            continue

        score_atual = sum(freq_letras[letra] for letra in set(palavra_candidata))

        if score_atual > max_score:
            max_score = score_atual
            melhor_palavra = palavra_candidata

    return melhor_palavra if melhor_palavra else palavras_possiveis[0]


def fazer_tentativa(tentativa):
    global letras_eliminadas, letras_presentes, letras_com_posicao_correta

    if tentativa == 0:
        proxima_palavra = "aureo"
        palavras_testadas.append(proxima_palavra)
        return proxima_palavra

    for i, simbolo in enumerate(ultimo_resultado):
        letra = ultima_palavra_usada[i]
        if simbolo == "#" and letra not in letras_eliminadas:
            letras_eliminadas.append(letra)
        elif simbolo == "?" and (letra, i) not in letras_presentes:
            letras_presentes.append((letra, i))
        elif simbolo == "!" and (letra, i) not in letras_com_posicao_correta:
            letras_com_posicao_correta.append((letra, i))

    eliminar_palavras()

    if len(palavras_possiveis) <= 2:
        proxima_palavra = next((p for p in palavras_possiveis if p not in palavras_testadas), palavras_possiveis[0])
    else:
        proxima_palavra = heuristica()

    palavras_testadas.append(proxima_palavra)
    print(palavras_possiveis)
    print(f"IA escolheu: {proxima_palavra}")
    return proxima_palavra

def resetar_estado():
    global ultimo_resultado, ultima_palavra_usada, letras_eliminadas
    global letras_presentes, letras_com_posicao_correta, palavras_testadas, palavras_possiveis

    ultimo_resultado = ""
    ultima_palavra_usada = ""
    letras_eliminadas = []
    letras_presentes = []
    letras_com_posicao_correta = []
    palavras_testadas = []
    palavras_possiveis = palavras.copy()