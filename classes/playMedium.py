# -*-coding:UTF-8 -*
from Game   import *
from Neuron import *
from Player import *

game = Game(15)

humanPlayer = HumanPlayer('Spixe')
cpuPlayer   = CPUPlayer('Terminator2', 'medium', 15)

game.start(humanPlayer, cpuPlayer, True)
