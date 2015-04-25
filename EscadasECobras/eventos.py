import random

def rolarDado():
    return random.randint(1,6)

def checarTabuleiro(tabuleiro, jogador):
    goto = tabuleiro[jogador.posicao]
    jogador.posicao = goto

def criarTabuleiro():
    tabuleiro = [0] * 100
    i = 0
    for casa in tabuleiro:
        tabuleiro[i] = i
        i = i + 1
    return tabuleiro
