from eventos import *

class Jogador():
    posicao = 0

tabuleiro = criarTabuleiro()

tabuleiro[5] = 12
tabuleiro[7] = 14
tabuleiro[10] = 2


jogador1 = Jogador()
jogador2 = Jogador()

jogador_da_vez = 1

while (True):

    if jogador_da_vez == 1:
        jogador = jogador1
    else:
        jogador = jogador2


    input("Aperte Enter para rolar o dado")
    dado = rolarDado()
    jogador.posicao = jogador.posicao + dado

    if jogador.posicao > 98:
        ganhador = jogador_da_vez
        break

    checarTabuleiro(tabuleiro, jogador)


    print("Jog: " + str(jogador_da_vez))

    if jogador_da_vez == 1:
        jogador1.posicao = jogador.posicao
        jogador_da_vez = 2
    else:
        jogador2.posicao = jogador.posicao
        jogador_da_vez = 1

    print("Dado: " + str(dado))
    print("Jog1: " + str(jogador1.posicao))
    print("Jog2: " + str(jogador2.posicao))
    print("==========")

print("Jog: " + str(jogador_da_vez))
print("Dado: " + str(dado))
print("Jog1: " + str(jogador1.posicao))
print("Jog2: " + str(jogador2.posicao))
print("")
print ("Ganhador: Jogador " + str(ganhador))
