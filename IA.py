import sorteio as srt

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

def fazer_tentativa(tentativa):
    global letras_eliminadas, letras_presentes, letras_com_posicao_correta

    if tentativa == 0:
        palavras_testadas.append("aureo")
        return "aureo"
    else:
        for i, simbolo in enumerate(ultimo_resultado):
            letra = ultima_palavra_usada[i]
            if simbolo == "#":
                if letra not in letras_eliminadas:
                    letras_eliminadas.append(letra)
            elif simbolo == "?":
                if (letra, i) not in letras_presentes:
                    letras_presentes.append((letra, i))
            elif simbolo == "!":
                if (letra, i) not in letras_com_posicao_correta:
                    letras_com_posicao_correta.append((letra, i))

        if tentativa < 2:
            eliminar_palavras(redundancia=False)
        else:
            eliminar_palavras(redundancia=True)

        if palavras_possiveis:
            print(palavras_possiveis)
            melhor = melhor_palavra_por_frequencia([p for p in palavras_possiveis if p not in palavras_testadas])
            palavras_testadas.append(melhor)
            return melhor

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

def eliminar_palavras(redundancia=False):
    global palavras_possiveis

    base = palavras_possiveis if redundancia else palavras

    nova_lista = []
    for palavra in base:
        if palavra_valida(palavra):
            nova_lista.append(palavra)

    if redundancia:
        palavras_possiveis = list(set(palavras_possiveis) & set(nova_lista))
    else:
        palavras_possiveis = nova_lista

        
def resetar_estado():
    global ultimo_resultado, ultima_palavra_usada
    global letras_eliminadas, letras_presentes, letras_com_posicao_correta
    global palavras_testadas, palavras_possiveis

    ultimo_resultado = ""
    ultima_palavra_usada = ""
    letras_eliminadas = []
    letras_presentes = []
    letras_com_posicao_correta = []
    palavras_testadas = []
    palavras_possiveis = palavras.copy()