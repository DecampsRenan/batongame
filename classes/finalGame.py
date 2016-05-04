# -*-coding:UTF-8 -*
from Game   import *
from Neuron import *
from Player import *

game = Game(15)

chaine = str()
while chaine.lower() != "q":
    print("Tapez 'Q' pour quitter...")

    print("Tapez votre nom de joueur : ")
    chaine = input()
    if chaine.lower() != "q":
        player = HumanPlayer(chaine)
        print("Bienvenue ", chaine, " !")

        print("Tapez votre mode de jeu (easy, medium, ou hard) : ")
        chaine = input()
        if chaine.lower() in ("easy","medium","hard"):
            cpuPlayer   = CPUPlayer('Terminator', chaine.lower(), 15)

            game.start(player, cpuPlayer, True)
