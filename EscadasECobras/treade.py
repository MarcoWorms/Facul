from threading import Thread
from time import sleep
import random

ouro = 0
madeira = 0

def gerarRecurso(recurso, tempo):

    global ouro
    global madeira

    while(True):

        #print("Gerando",recurso,"...")

        sleep(tempo)

        if recurso == "Madeira":
            madeira = madeira + 1
            print(madeira,"Madeiras")
        else:
            ouro = ouro + 1
            print(ouro,"ouros")


Thread(target=gerarRecurso, args=("Madeira", 3)).start()
Thread(target=gerarRecurso, args=("Ouro", 2)).start()
