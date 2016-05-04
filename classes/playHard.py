# -*-coding:UTF-8 -*
from Game   import *
from Neuron import *
from Player import *

game = Game(15)

humanPlayer = CPUPlayer('Sharky', 'hard', 15)
cpuPlayer   = CPUPlayer('Terminator', 'hard', 15)

game.start(humanPlayer, cpuPlayer, True)