from threading import Thread
from time import sleep
import random

class player:

    def __init__(self, name, hpRegen):
        self.name = name
        self.hpRegen = hpRegen
        self.hp = 0
        Thread(target=player.iniciarHpRegen, args=(self, 1)).start()

    def iniciarHpRegen(self, tempo):

        while(True):

            sleep(tempo)

            if self.hp + self.hpRegen > 100:
                self.hp = 100
            else:
                self.hp = self.hp + self.hpRegen

            print (self.name, self.hp)

player1 = player(name="Player1", hpRegen=10)
player2 = player(name="Player2", hpRegen=20)
