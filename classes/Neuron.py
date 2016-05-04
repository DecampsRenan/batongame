# -*-coding:UTF-8 -*

import random

BASE_WEIGHT = 10
RECOMPENSE  = 8

class NeuronNetwork:
<<<<<<< HEAD
  # maxDist correspond au nombre maximum de batons que l'on peut retirer.
  # nbSticks correspond au nombre de batons en jeu au début de la partie.
  def __init__(self,maxDist,nbSticks):
    self.neurons = [] # Liste des Neurons du réseau.

    # On crée autant de Neuron qu'il y a de sticks
    for i in range(1,nbSticks+1):
      self.neurons.append(Neuron(self,i))

    # Pour chaque Neuron, on crée les connexions
    for neuron in self.neurons:
      neuron.makeConnections(maxDist,nbSticks,BASE_WEIGHT)

    self.initPath()
  
  def initPath(self):
    # Path correspond au 'chemin que le réseau de neurone va emprunter'
    self.path = {}

  def getNeuron(self,index):
    if index-1>=0 and index<=len(self.neurons): return self.neurons[index-1]
    else: return None

  def activateNeuronPath(self,neuron1,neuron2):
    self.path[neuron1]=neuron2

  def recompenseConnections(self):
    for neuron1,neuron2 in self.path.items():
      neuron1.recompenseConnection(neuron2)
    self.initPath()

  def printAllConnections(self):
    for neuron in self.neurons: neuron.printConnections()

  def printScores(self):
    scores = {}
    for neuron in self.neurons:
      for n,s in neuron.connections.items():
        if n not in scores: scores[n]=s
        else: scores[n] = scores[n] + s
    for neuron,score in scores.items():
      print(neuron.asString(),score)


class Neuron:
    
  # Constructeur permettant d'initialiser un neurone
  def __init__(self,network,index):
    self.network = network # Référence vers le réseau de neurones
    self.index   = index   # Valeur du neurone actuel (correspond aux nombre de batons à jouer)
    self.connections = {}  # Dictionnaire des connexions

  # Méthode permettant de définir les connexions entre les Neurons
  # Chaque Neuron aura maxDist*2+1 connexions (ici, 7-1=6 :: cf.range); sauf le dernier
  # qui en aura maxDist+1 (4-1=3 :: cf.range).
  # Cette valeur est utilisée afin de construire les connexions entre les neurons
  # et leur associer 
  def makeConnections(self,maxDist,nbSticks,baseWeight):
    if self.index!=nbSticks: nb=maxDist*2 +1
    else: nb=maxDist+1
    for i in range(1,nb): # range(1, nb) =>  [1, 2, 3, 4, 5, ..., nb-1]
      neuron = self.network.getNeuron(self.index-i)
      if neuron!=None: self.connections[neuron] = baseWeight
  
  # Méthode qui retourne un neurone connecté au neurone actuel
  # en fonction du 'shift' (cf. CPUPlayer).
  def chooseConnectedNeuron(self,shift):
    # Méthode qui retourne un neurone connecté au neurone actuel
    # en fonction du 'shift' (cf. CPUPlayer).
    # On devra utiliser la méthode self.weighted_choice pour choisir
    # au hasard dans une liste de connexions disponibles en fonction de leurs poids
    connectionsCopy = dict(self.connections)
    isDone  = False
    choosen = None
    while not isDone:
      if len(connectionsCopy) == 0: isDone = True
      else:
        choosen = self.weighted_choice(connectionsCopy)
        if choosen.testNeuron(self.index - shift): isDone = True
        else: connectionsCopy.pop(choosen)
      
    return choosen

  # TODO: savoir à quoi sert cette fonction...
  def testNeuron(self,inValue):
    # Renvoie un booléen : True si la différence entre la 'inValue' et
    # la valeur du neurone actuel est comprise entre 1 et 3 inclus
    dif =  inValue - self.index
    return (dif >= 1 and dif <= 3) 

  # Méthode permettant de récompenser la connexion entre le neurone actuel et 'neuron'
  def recompenseConnection(self,neuron):
    self.connections[neuron] += RECOMPENSE

  # Affiche les connexions du noeud courant
  def printConnections(self):
    print("Connections of", self.asString() + ":")
    for neuron in self.connections:
      print(neuron.asString(),self.connections[neuron])
  
  
  # Affiche le nom du nom
  def asString(self):
    return "N"+str(self.index)
    