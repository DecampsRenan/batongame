# -*-coding:UTF-8 -*
from Game   import *
from Neuron import *
from Player import *

game = Game(15)

cpuPlayer = CPUPlayer('R2D2', 'hard', 15)
cpuPlayer2   = CPUPlayer('Terminator', 'hard', 15)

i = 0
while i < 100:
    game.start(cpuPlayer, cpuPlayer2, False)
    i += 1
