# -*-coding:UTF-8 -*
import pickle
from Game   import *
from Neuron import *
from Player import *

NB_STICKS = 15

game = Game(NB_STICKS)

cpuPlayer  = CPUPlayer('R2D2', 'hard', NB_STICKS)
cpuPlayer2 = CPUPlayer('Terminator', 'hard', NB_STICKS)

i = 0
while i < 100000:
    game.start(cpuPlayer, cpuPlayer2, False)
    i += 1

print("\nReseau neuronal de R2D2 :")

with open('reseau_neuronal','wb') as output: pickle.dump(cpuPlayer.getNeuronNetwork(),output,pickle.HIGHEST_PROTOCOL)

print("\nReseau neuronal de Terminator :")
