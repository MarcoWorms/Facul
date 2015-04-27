from threading import Thread
from time import sleep
import random

class player:
	
	def __init__(self, name, hpRegen):
		self.name = name
		self.hp = 100
		self.hpRegen = hpRegen
		Thread(target=player.gerarRecurso, args=(self, 5, self.hpRegen)).start()

	def gerarRecurso(self, tempo, quanto):

	    while(True):
	        sleep(tempo)
	        self.hp = self.hp + quanto
	        print (self.name, self.hp)

player1 = player(name="Player1", hpRegen=10)
player2 = player(name="Player2", hpRegen=20)

