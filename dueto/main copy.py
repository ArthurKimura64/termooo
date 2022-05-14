import json
import random

with open('Json/Respostas.json') as file:
    possiveisRespostas = json.load(file)

with open('Json/TermosAceitos.json') as file:
    termosAceitos = json.load(file)

def main():
    possiveisRespostas = ["1","2","3","4"]
    resposta = "0"
    print ("Bem vindo ao Dueto! O que deseja fazer?")
    print ("1 - Jogar Dueto (sozinho)(Padrão)")
    print ("2 - Tentar identificar uma palavra")
    print ("3 - Jogar Dueto (dois Jogadores)")
    print ("4 - Sair")
    while (True):
        resposta = input("Digite o número do que deseja fazer!\n")
        if (resposta in possiveisRespostas):
            break
        else:
            print("Escolha inválida! Escolha uma opção válida!")
    if resposta == "1":
        duetoSozinho()
    elif resposta == "2":
        identificador()
    elif resposta == "3":
        duetoSozinho()
    else:
        exit()
def duetoSozinho():
    print ("\n----------------------------------------\n")
    print ("\nVocê escolheu a opção de Jogar Dueto, no modo SinglePlayer:\n")
    respostaEscolhida = list(possiveisRespostas[random.randint(0, len(possiveisRespostas)-1)])
    print ("A resposta foi selecionada! Você terá 6 chances para descobrir qual palavra será!\n")
    for i in range(6):
        checarAlgo = []
        letras = []
        tentativa = list(input("Descubra a palavra. Você tem mais %d chance(s)\n" %(6-i)))
        for letra in tentativa:
            if letra in respostaEscolhida:
                if respostaEscolhida.count(letra) == 1:
                    if tentativa.index(letra) == respostaEscolhida.index(letra):
                        tentativa[tentativa.index(letra)] = "\033[1;92m" + letra + "\033[0;0m"
                        checarAlgo.append(False)
                    else:
                        tentativa[tentativa.index(letra)] = "\033[1;33m" + letra + "\033[0;0m"
                        checarAlgo.append(False)
                else:
                    if tentativa.index(letra) == respostaEscolhida.index(letra):
                        tentativa[tentativa.index(letra)] = "\033[1;92m" + letra + "\033[0;0m"
                    else:
                        checarAlgo = True
                        letras.append(letra)

        if checarAlgo:
            for letra in letras:
                pass
                
    pass
def identificador():
    print ("\n----------------------------------------\n")
    print ("\nVocê escolheu a opção de tentar identificar uma palavra no Dueto:\n")
    letrasNaoExistentes = []
    respostasLetras = []
    respostasAceitas = ["teste1","teste2"]

    #separa as letras em caracteres
    for resposta in possiveisRespostas:
        respostasLetras.append(list(resposta))

    while len(respostasAceitas) > 1:
        respostasAceitas = []
        tentativa = input("Insira o input que você inseriu:\n")
        letrasTentativasNaoExistem = list(set(list(tentativa)))
        
        #cuida dos jogadores cujas letras estão na posicao errada
        print("\nInsira, separando com espaço as letras que estão na palavra \033[;1m\033[1;93mporém na posição errada.\033[0;0m\nSe a letra estiver em mais de um lugar, especifique a posição da letra na palavra")
        posicoesErradas = input("Ex: e2 f4(e na 2o posição e f na 4 posição)\n")
        posicoesErradas = posicoesErradas.split(" ")
        for letras in posicoesErradas:
            posicoesErradas[posicoesErradas.index(letras)] = list(letras)
        contador = -1
        for letras in posicoesErradas:
            contador +=1
            if len(letras) == 1:
                posicoesErradas[contador] = [letras[0], tentativa.index(letras[0])]
            elif len(letras) == 2:
                posicoesErradas[contador] = [letras[0], int(letras[1]) - 1]
        if len(posicoesErradas) == 1 and posicoesErradas[0] == []:
            posicoesErradas[0] = None
        posicoesErradas = list(filter(None, posicoesErradas))

        for letras in posicoesErradas:
            if letras[0] in letrasTentativasNaoExistem:
                letrasTentativasNaoExistem.remove(letras[0])
        print (posicoesErradas)

        #cuida dos jogadores cujas letras estão na posicao certas
        print("\nInsira, separando com espaço as letras que estão na palavra e na \033[;1m\033[1;92mposição certa.\033[0;0m\nSe a letra estiver em mais de um lugar, especifique a posição da letra na palavra")
        posicoesCertas = input("Ex: e2 f4(e na 2o posição e f na 4 posição)\n")
        posicoesCertas = posicoesCertas.split(" ")
        for letras in posicoesCertas:
            posicoesCertas[posicoesCertas.index(letras)] = list(letras)
        contador = -1
        for letras in posicoesCertas:
            contador +=1
            if len(letras) == 1:
                posicoesCertas[contador] = [letras[0], tentativa.index(letras[0])]
            elif len(letras) == 2:
                posicoesCertas[contador] = [letras[0], int(letras[1]) - 1]
        if len(posicoesCertas) == 1 and posicoesCertas[0] == []:
            posicoesCertas[0] = None
        posicoesCertas = list(filter(None, posicoesCertas))

        for letras in posicoesCertas:
            if letras[0] in letrasTentativasNaoExistem:
                letrasTentativasNaoExistem.remove(letras[0])
        

        for letras in letrasTentativasNaoExistem:
            if letras in letrasNaoExistentes:
                continue
            else:
                letrasNaoExistentes.append(letras)
        

        for resposta in respostasLetras:
            tudoCerto = True

            for letras in posicoesErradas:
                if letras[0] in resposta:
                    if tentativa[letras[1]] == resposta[letras[1]]:
                        tudoCerto = False
                        break
                else:
                    tudoCerto = False
                    break

            for letras in posicoesCertas:
                if letras[0] in resposta:
                    if tentativa[letras[1]] == resposta[letras[1]]:
                        continue
                    else:
                        tudoCerto = False
                        break
                else:
                    tudoCerto = False
                    break
            for letras in letrasNaoExistentes:
                if letras in resposta:
                    tudoCerto = False
                    break
            
            if tudoCerto:
                respostasAceitas.append(resposta)
        
        respostasLetras = respostasAceitas
        for resposta in respostasAceitas:
            respostasAceitas[respostasAceitas.index(resposta)] = "".join(resposta)
            
        print(respostasAceitas)
    
    main()
     
def duetoDuplo():
    pass

main()