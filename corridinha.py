from threading import Thread
import random
from time import sleep

class Corredor:
    chegada = 50
    colocado = 0

    def __init__(self, numero):
        self.numero = numero
        self.posicao = 0

    def correr(self):
        while self.posicao < Corredor.chegada:
            distancia = random.randint(2, 5)
            sleep(random.randint(1,2))
            self.posicao += distancia
            print(self.numero, 'percorreu', distancia, 'metros e alcancou a posição', self.posicao)

        Corredor.colocado += 1
        print(self.numero, 'chegou em', Corredor.colocado, 'lugar')

for i in range(10):
    Thread(target=Corredor(i).correr).start()
