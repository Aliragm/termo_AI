import sorteio as srt

def receber_palavra(palavra=None):
    if palavra != None:
        return srt.remover_acentos(str(palavra))
    else:
        verificado = False
        while verificado == False:
            palavra_input = srt.remover_acentos(input("digite sua palavra: "))
            verificado = srt.verificador(palavra_input)
        return str(palavra_input)
