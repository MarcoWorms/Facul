import random

def rolarDado():
    return random.randint(1,6)

def checarTabuleiro(tabuleiro, jogador):
    jogador.posicao = tabuleiro[jogador.posicao]

def criarTabuleiro():
    return list(range(100))
