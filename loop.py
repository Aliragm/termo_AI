import sorteio as srt
import palavra as pl
import IA

def jogo(ia=False):
    palavra = srt.sorteio()
    print(palavra)
    tentativas = 0
    acertou = False

    print("LEGENDA:")
    print("# = LETRA ERRADA")
    print("? = LETRA CERTA NO LUGAR ERRADO")
    print("! = LETRA CERTA NO LUGAR CERTO")
    while acertou == False and tentativas < 6:
        if ia == False:
            palavra_user = pl.receber_palavra()
        elif ia == True:
           palavra_user = pl.receber_palavra(IA.fazer_tentativa(tentativa=tentativas))
        resultado = ""

        print(f"a palavra escrita foi: {palavra_user}")
        for i in range(0,5):
            if palavra[i] == palavra_user[i]:
                resultado += "!"
            elif palavra_user[i] in palavra and palavra[i] != palavra_user[i]:
                resultado += "?"
            else:
                resultado += "#"
        
        if ia == True:
            IA.captar_resultado(resultado=resultado, palavra=palavra_user)

        print(resultado)
        if palavra_user == palavra:
            acertou = True
            print(f"Ganhou! a palavra é {palavra}")
            return
        else:
            tentativas += 1
            print(f"tentativas restantes: {6-tentativas}")
    print(f"Perdeu! a palavra é {palavra}")

jogo(ia=True)
