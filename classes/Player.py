# -*-coding:UTF-8 -*

from random import *
from Neuron import *

class Player:
    def __init__(self,name):
        self.name = name
        self.nbWin = 0

    def getName(self):
        return self.name

    def getNbWin(self):
        return self.nbWin

    def addWin(self):
        self.nbWin+=1

    def addLoss(self):
        pass

class HumanPlayer(Player):
    def play(self,sticks):
        if sticks==1: return 1
        else:
            correct = False
            while not correct:
                nb = input('Sticks?\n')
                try:
                    nb=int(nb)
                    if nb>=1 and nb<=3 and sticks-nb>=0:
                        correct=True
                except: pass
            return nb

class CPUPlayer(Player):
    def __init__(self,name,mode,nbSticks):
        super().__init__(name)
        self.mode = mode
        self.netw = NeuronNetwork(3,nbSticks)
        self.previousNeuron = None

    def play(self,sticks):
        if self.mode=='easy': return self.playEasy(sticks)
        elif self.mode=='hard': return self.playHard(sticks)
        else: return self.playMedium(sticks)

    def playMedium(self,sticks):
        if   sticks==1: return 1
        elif sticks<=4: return sticks-1
        else: return self.playRandom(sticks)

    def playEasy(self,sticks):
        return self.playRandom(sticks)

    def playRandom(self,sticks):
        if sticks < 4: return randint(1, sticks)
        else: return randint(1, 3)

    def playHard(self,sticks):
        # TODO utiliser le réseau neuronal pour choisir le nombre de bâtons à jouer
        # utiliser l'attribut self.previousNeuron pour avoir le neuron précédemment sollicité dans la partie
        # calculer un 'shift' qui correspond à la différence entre la valeur du précédent neurone et le nombre de bâtons encore en jeu
        # utiliser la méthode 'chooseConnectedNeuron' du self.previousNeuron puis retourner le nombre de bâtons à jouer
        # bien activer le réseau de neurones avec la méthode 'activateNeuronPath' après avoir choisi un neurone cible
        # attention à gérer les cas particuliers (premier tour ou sticks==1)
        if sticks == 1: return 1
        
        if self.previousNeuron == None:
            self.previousNeuron = self.netw.getNeuron(sticks)
            shift = 0
        else:
            shift = self.previousNeuron.index - sticks
            
        currentNeuron = self.previousNeuron.chooseConnectedNeuron(shift)
        
        # Cas ou sticks = 2 (normalement)
        if currentNeuron == None:
            nbSticksToPlay = 1
        else:
            nbSticksToPlay = sticks - currentNeuron.index
            self.netw.activateNeuronPath(self.previousNeuron, currentNeuron)
            self.previousNeuron = currentNeuron
            
        return nbSticksToPlay
        
        
    def getNeuronNetwork(self): return self.netw

    def addWin(self):
        super().addWin()
        self.netw.recompenseConnections()
        self.previousNeuron=None

    def addLoss(self):
        super().addLoss()
        self.previousNeuron=None
