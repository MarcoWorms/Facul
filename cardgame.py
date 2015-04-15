# Cores:
# 1 = verde
# 2 = vermelho
# 3 = azul
#
# Raridades:
# 1 = Comum
#
# Tipos:
# 1 = Criatura
#
# Subtipos:
# 1 = Pedra
#
#
#

class Card:

	def __init__(self, 
				 cardid,
				 name,
				 manacost,
				 color, 
				 rarity,
				 maintype,
				 subtype,
				 power,
				 defense,
				 effect,
				 text):

		self.cardid = cardid
		self.name = name
		self.manacost = manacost
		self.color = color
		self.rarity = rarity
		self.maintype = maintype
		self.subtype = subtype
		self.power = power
		self.defense = defense
		self.effect = effect
		self.text = text

	def __str__(self):
		return str(self.name)


carta = Card(cardid=0,
			 name="Weed Wizard",
			 manacost=4,
			 color=1,
			 rarity=1,
			 maintype=1,
			 subtype=1,
			 power=2,
			 defense=0,
			 effect="all creatures but stone status confuse 4",
			 text='''Todas as criaturas do campo que não sejam do tipo "Pedra" ganham o status "Confusão" durante 3 etapas de combate do controlador delas.

			 Confusão: Criaturas com status "Confusão" não podem atacar''')
print (carta)