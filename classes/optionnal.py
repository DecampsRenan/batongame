# -*-coding:UTF-8 -*
import pickle
from Game   import *
from Neuron import *
from Player import *

NB_STICKS = 15
NB_GAMES  = 10

game = Game(NB_STICKS)

cpuPlayer  = CPUPlayer('R2D2', 'hard', NB_STICKS)
cpuPlayer2 = CPUPlayer('Terminator', 'hard', NB_STICKS)

for i in range(1, NB_GAMES+1):
    game.start(cpuPlayer, cpuPlayer2, False)
    if i%10000 == 0: print(i)

# Calcul du taux de victoire du joueur qui commence
wins = cpuPlayer.getNbWin()
taux = (NB_GAMES / wins) * 100

# Affichage du résultat
print('Sur ', NB_GAMES, ' parties, le joueur qui commence a gagné ', wins, '.')
print('Soit un taux de ', taux, '% de victoires sur le nombre de match disputés.')