# -*-coding:UTF-8 -*
from Game   import *
from Neuron import *
from Player import *

game = Game(15)

cpuPlayer = CPUPlayer('R2D2', 'hard', 15)
cpuPlayer2   = CPUPlayer('Terminator', 'hard', 15)

i = 0
while i < 10000:
    game.start(cpuPlayer, cpuPlayer2, False)
    i += 1

print("\nReseau neuronal de R2D2 :")
print(cpuPlayer.netw.printAllConnections())

print("\nReseau neuronal de Terminator :")
print(cpuPlayer2.netw.printAllConnections())
