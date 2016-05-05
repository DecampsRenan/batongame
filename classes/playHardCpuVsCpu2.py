# -*-coding:UTF-8 -*
from Game   import *
from Neuron import *
from Player import *

game = Game(15)

cpuPlayer  = CPUPlayer('R2D2', 'easy', 15)
cpuPlayer2 = CPUPlayer('Terminator', 'easy', 15)

i = 0
while i < 10000:
    game.start(cpuPlayer, cpuPlayer2, False)
    i += 1

print("\n- easy contre easy")
print("Nombre de parties gagnees de R2D2 : ", cpuPlayer.getNbWin())
print("Nombre de parties gagnees de Terminator : ", cpuPlayer2.getNbWin(),"\n")

cpuPlayer  = CPUPlayer('R2D2', 'easy', 15)
cpuPlayer2 = CPUPlayer('Terminator', 'medium', 15)

i = 0
while i < 10000:
    game.start(cpuPlayer, cpuPlayer2, False)
    i += 1

print("- easy contre medium")
print("Nombre de parties gagnees de R2D2 : ", cpuPlayer.getNbWin())
print("Nombre de parties gagnees de Terminator : ", cpuPlayer2.getNbWin(),"\n")

cpuPlayer = CPUPlayer('R2D2', 'easy', 15)
cpuPlayer2   = CPUPlayer('Terminator', 'hard', 15)

i = 0
while i < 10000:
    game.start(cpuPlayer, cpuPlayer2, False)
    i += 1

print("- easy contre hard")
print("Nombre de parties gagnees de R2D2 : ", cpuPlayer.getNbWin())
print("Nombre de parties gagnees de Terminator : ", cpuPlayer2.getNbWin(),"\n")

cpuPlayer = CPUPlayer('R2D2', 'medium', 15)
cpuPlayer2   = CPUPlayer('Terminator', 'hard', 15)

i = 0
while i < 10000:
    game.start(cpuPlayer, cpuPlayer2, False)
    i += 1

print("- medium contre hard")
print("Nombre de parties gagnees de R2D2 : ", cpuPlayer.getNbWin())
print("Nombre de parties gagnees de Terminator : ", cpuPlayer2.getNbWin(),"\n")

cpuPlayer = CPUPlayer('R2D2', 'medium', 15)
cpuPlayer2   = CPUPlayer('Terminator', 'medium', 15)

i = 0
while i < 10000:
    game.start(cpuPlayer, cpuPlayer2, False)
    i += 1

print("- medium contre medium")
print("Nombre de parties gagnees de R2D2 : ", cpuPlayer.getNbWin())
print("Nombre de parties gagnees de Terminator : ", cpuPlayer2.getNbWin(),"\n")

cpuPlayer = CPUPlayer('R2D2', 'hard', 15)
cpuPlayer2   = CPUPlayer('Terminator', 'hard', 15)

i = 0
while i < 10000:
    game.start(cpuPlayer, cpuPlayer2, False)
    i += 1

print("- hard contre hard")
print("Nombre de parties gagnees de R2D2 : ", cpuPlayer.getNbWin())
print("Nombre de parties gagnees de Terminator : ", cpuPlayer2.getNbWin(),"\n")
