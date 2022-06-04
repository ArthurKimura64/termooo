import json
import random
import numpy
import collections

respostasAceitas = json.load(open('Json/Respostas.json'))
respostasAceitas.sort()

termosAceitos = json.load(open('Json/TermosAceitos.json'))
termosAceitos.extend(respostasAceitas)
termosAceitos = list(set(list(termosAceitos)))
termosAceitos.sort()

def main():
    while True:
        resposta = "0"
        respostasMain = [1,2,3,4]
        print ("Bem vindo ao Dueto! O que deseja fazer?")
        print ("1 - Jogar Dueto (sozinho)(padrão)")
        print ("2 - Tentar identificar uma palavra")
        print ("3 - Jogar Dueto (dois Jogadores)")
        print ("4 - Sair")
        while (True):
            resposta = int(input("Digite o número do que deseja fazer!\n"))
            if (resposta in respostasMain):
                break
            else:
                print("Escolha inválida! Escolha uma opção válida!")
        if resposta == 1:
            duetoSozinho()
        elif resposta == 2:
            identificador()
        elif resposta == 3:
            duetoSozinho()
        else:
            print("Finalizando programa...")
            exit()

def duetoSozinho():
    print ("\n----------------------------------------\n")
    print ("\nVocê escolheu a opção de Jogar Dueto, no modo SinglePlayer:\n")
    respostaEscolhida = list(respostasAceitas[random.randint(0, len(respostasAceitas)-1)][0])
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
    respostasAceitas = json.load(open('Json/Respostas.json'))
    respostasAceitas.sort()

    termosAceitos = json.load(open('Json/TermosAceitos.json'))
    termosAceitos.extend(respostasAceitas)
    termosAceitos = list(set(list(termosAceitos)))
    termosAceitos.sort()

    possiveisTermos = termosAceitos
    possiveisRespostas = respostasAceitas
    print ("\n----------------------------------------\n")
    print ("\nVocê escolheu a opção de tentar identificar uma palavra no Dueto:\n")

    while len(possiveisTermos) > 1:
        possiveisTermos = elaboraTermos(possiveisRespostas, possiveisTermos)
        respostasFiltradas = []
        pontuacaoTermos = []
        for possibilidades in possiveisTermos:
            pontuacaoTermos.append(possibilidades[1])
        indexMaiorPontuacao = numpy.where(numpy.array(pontuacaoTermos) == max(pontuacaoTermos))[0]
        print("\nInsira o input que você inseriu:\n")
        print("Recomendados", end=": ")
        for index in indexMaiorPontuacao:
            if index == indexMaiorPontuacao[-1]:
                print("\033[;1m\033[1;95m" + possiveisTermos[index][0] + "\033[0;0m", end=". \n")
            elif index == indexMaiorPontuacao[-2]:
                print("\033[;1m\033[1;95m" + possiveisTermos[index][0] + "\033[0;0m", end=" ou ")
            else:
                print("\033[;1m\033[1;95m" + possiveisTermos[index][0] + "\033[0;0m", end=", ")

        tentativa = list(input())
        letrasNaoExistentes = list(set(tentativa))

        print("\nInsira as letras que estão na palavra \033[;1m\033[1;93mporém na posição errada.\033[0;0m Coloque as letras em ordem!")
        print("Se a letra estiver em mais de um lugar, você pode especificar a posição da letra na palavra")
        posicoesErradasPrototipo = list(input())
        posicoesErradas = []
        for index in range(len(posicoesErradasPrototipo)):
            letra = posicoesErradasPrototipo[index]
            if any(map(str.isdigit,letra)):
                posicoesErradas[-1] = [posicoesErradas[-1][0], int(letra)-1]
            else:
                if len(posicoesErradas) != 0:
                    posicoesErradas.append([letra, tentativa.index(letra,posicoesErradas[-1][1])])
                else:
                    posicoesErradas.append([letra,tentativa.index(letra)])
        print(posicoesErradas)
                    
        for letra in posicoesErradas:
            if letra[0] in letrasNaoExistentes:
                letrasNaoExistentes.remove(letra[0])
        
        print("\nInsira, separando com espaço as letras que estão na palavra e na \033[;1m\033[1;92mposição certa.\033[0;0m Coloque as letras em ordem!")
        print("Se a letra estiver em mais de um lugar, você pode especificar a posição da letra na palavra")
        posicoesCertasPrototipo = list(input())
        posicoesCertas = []
        for index in range(len(posicoesCertasPrototipo)):
            letra = posicoesCertasPrototipo[index]
            if any(map(str.isdigit,letra)):
                posicoesCertas[-1] = [posicoesCertas[-1][0], int(letra)-1]
            else:
                if len(posicoesCertas) != 0:
                    posicoesCertas.append([letra, tentativa.index(letra,posicoesCertas[-1][1])])
                else:
                    posicoesCertas.append([letra,tentativa.index(letra)])
        print(posicoesCertas)
        for letra in posicoesCertas:
            if letra[0] in letrasNaoExistentes:
                letrasNaoExistentes.remove(letra[0])
        
        letrasNaoExistentes = list(set(list(letrasNaoExistentes)))

        for index in range(len(possiveisTermos)):
            resposta = list(possiveisTermos[index][0])
            tudoCerto = True
        
            for letra in posicoesErradas:
                    if letra[0] in resposta:
                        if tentativa[letra[1]] == resposta[letra[1]]:
                            tudoCerto = False
                            break
                    else:
                        tudoCerto = False
                        break

            for letra in posicoesCertas:
                if letra[0] in resposta:
                    if tentativa[letra[1]] == resposta[letra[1]]:
                        continue
                    else:
                        tudoCerto = False
                        break
                else:
                    tudoCerto = False
                    break
            for letra in letrasNaoExistentes:
                if letra in resposta:
                    tudoCerto = False
                    break
            
            if tudoCerto:
                respostasFiltradas.append(possiveisTermos[index][0])
        
        possiveisTermos = respostasFiltradas

        possiveisRespostas = []
        for possibilidade in possiveisTermos:
            if possibilidade in respostasAceitas:
                possiveisRespostas.append(possibilidade)

        if len(possiveisRespostas) == 0:
            print("Não encontramos uma resposta. Verifique suas respostas e tentem novamente")
            break
        if len(possiveisRespostas) == 1:
            print("Encontramos uma resposta!! A resposta é " + possiveisRespostas[0] + "\n")
            break
        elif len(possiveisRespostas) < 10:
            print("Temos algumas respostas... As possibilidades são ", end="")
            for possibilidade in possiveisRespostas:
                if possibilidade == possiveisRespostas[-1]:
                    print("\033[;1m\033[1;96m" + possibilidade + "\033[0;0m", end =".")
                elif possibilidade == possiveisRespostas[-2]:
                    print ("\033[;1m\033[1;96m" + possibilidade + "\033[0;0m", end =" ou ")
                else:
                    print("\033[;1m\033[1;96m" + possibilidade + "\033[0;0m", end =", ")

        else:
            print("Ainda temos muitas respostas, por favor tente inserir mais resultados!")

def elaboraTermos(possiveisRespostas, possiveisTermos):
    resposta0 = []
    resposta1 = []
    resposta2 = []
    resposta3 = []
    resposta4 = []
    
  #Cria pontuacao
    for possivelResposta in possiveisRespostas:
        resposta0.append(possivelResposta[0])
        resposta1.append(possivelResposta[1])
        resposta2.append(possivelResposta[2])
        resposta3.append(possivelResposta[3])
        resposta4.append(possivelResposta[4])
    resposta0 = dict((collections.Counter(resposta0)))
    resposta1 = dict((collections.Counter(resposta1)))
    resposta2 = dict((collections.Counter(resposta2)))
    resposta3 = dict((collections.Counter(resposta3)))
    resposta4 = dict((collections.Counter(resposta4)))
    caractereRespostas = {}
    for chave in resposta0.keys():
        if chave in caractereRespostas.keys():
            caractereRespostas[chave] += resposta0[chave]
        else:
            caractereRespostas[chave] = resposta0[chave]
    for chave in resposta1.keys():
        if chave in caractereRespostas.keys():
            caractereRespostas[chave] += resposta1[chave]
        else:
            caractereRespostas[chave] = resposta1[chave]
    for chave in resposta2.keys():
        if chave in caractereRespostas.keys():
            caractereRespostas[chave] += resposta2[chave]
        else:
            caractereRespostas[chave] = resposta2[chave]
    for chave in resposta3.keys():
        if chave in caractereRespostas.keys():
            caractereRespostas[chave] += resposta3[chave]
        else:
            caractereRespostas[chave] = resposta3[chave]
    for chave in resposta4.keys():
        if chave in caractereRespostas.keys():
            caractereRespostas[chave] += resposta4[chave]
        else:
            caractereRespostas[chave] = resposta4[chave]
  #Estabelece Pontuação
    for index in range(len(possiveisTermos)):
        letras = []
        pontuacao = 0
        for letra in possiveisTermos[index]:
            if letra in letras:
                pontuacao += 0
            else:
                if letra in caractereRespostas.keys():
                    pontuacao += caractereRespostas[letra]
                else:
                    pontuacao += 0
                letras.append(letra)
        possiveisTermos[index] = [possiveisTermos[index], pontuacao]

    return possiveisTermos
main()