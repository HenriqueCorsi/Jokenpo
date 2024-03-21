import random
import os
import time

def menu():
    os.system('cls')
    print('=======================')
    print(' WELCOME TO JOKENPÔÔÔ ')
    print('=======================')
    list_menu = ['[1] Pedra', '[2] Papel', '[3] Tesoura', '[4] SAIR\n']
    for x in list_menu:
        print(x) 

cont = True
placar_user = 0
placar_cpu = 0