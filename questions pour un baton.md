### Les bases et le mode simple 
> Q. En utilisant ce script, commencez à jouer contre l’ordinateur en faisant quelques parties. L’ordinateur peut faire des erreurs évidentes lors du dernier tour; à l’aide du code, expliquez pourquoi.

- L'ordinateur joue de manière totalement aléatoire du début à la fin, le nombre de batons joués n'est pas choisi de manière réfléchie; il peut donc faire des erreurs évidentes lors du dernier tour même si il a l'occasion de gagner durant ce tour.

### Mode intermédiaire
> Q. Mode "medium" : écrire quelques lignes de code dans la méthode de l’IA (playMedium) pour éviter que l’ordinateur ne commette une erreur au dernier tour lorsqu’il a toutes les chances de gagner (le nombre de bâtons restants est de 2, 3 ou 4). Est-ce de l’apprentissage? Expliquez.

- Non car il n'apprend pas par lui même, cette nouvelle règle pour le dernier tour est fixe, et ne dépend pas des parties jouées ou de la partie en cours.

### Apprentissage
> Q. Pour être plus efficace dans l’apprentissage, nous allons maintenant laisser l’ordinateur jouer contre lui-même en mode "hard". Comment s’appelle cette méthode et pourquoi l’utilise-t-on ?

- Cette méthode est appellée **Apprentissage par renforcement**. Elle est utilisée dans ce cas car elle permet
au programme d'apprendre par lui-meme; il suffit de le laisser jouer contre lui-meme pour qu'il puisse apprendre à travers le système de récompense.

> Q. En laissant l’ordinateur jouer contre lui-même, que constatez-vous à la ﬁn de N parties? 

L'ordinateur arrive à apprendre de lui-même à travers le système de poids entre neurones qui s'incrémente en fonction des victoires. On obtient donc des reseaux de neurones avec des résultats très proches entre eux au bout de N partie, avec un avantage pour le joueur qui commence. On peut voir des liaisons entre neurones qui ont des poids beaucoups plus élevés que ses congénères, ce sont les neurones où l'ordinateur est sûr de gagné à 100%.

> Q. Expliquez la différence de scores entre les 2 joueurs. 

- easy contre easy
Nombre de parties gagnees de R2D2 :  506
Nombre de parties gagnees de Terminator :  494

Score assez équilibré dans l'ensemble vu que chaque décision est totalement aléatoire et a la même probabilitée.

- easy contre medium
Nombre de parties gagnees de R2D2 :  174
Nombre de parties gagnees de Terminator :  826

Le joueur qui joue en medium ne fais pas d'erreur lors des derniers tours (lorsqu'il y a 4 batons ou moins) contrairement au mode easy qui peut en faire.

- easy contre hard
Nombre de parties gagnees de R2D2 :  262
Nombre de parties gagnees de Terminator :  738

Le mode hard permet au joueur d'apprendre via le réseau neuronal, plus il joue, plus il aura de chance de gagner.

- medium contre hard
Nombre de parties gagnees de R2D2 :  370
Nombre de parties gagnees de Terminator :  630

Le mode hard permet au joueur d'apprendre via le réseau neuronal, plus il joue, plus il aura de chance de gagner. Le medium a juste plus de victoire que le mode easy grâce au fait qu'il ne fais pas d'erreur lors des derniers tours.

- medium contre medium
Nombre de parties gagnees de R2D2 :  471
Nombre de parties gagnees de Terminator :  529

Score globalement équilibré due au même algorithme, les joueurs n'apprennent pas, les probabilités de gagner sont donc les même de chaque côté.

- hard contre hard
Nombre de parties gagnees de R2D2 :  832
Nombre de parties gagnees de Terminator :  168

Un joueur qui commence à jouer a plus de chance de gagner la partie dans ce jeu si les décisions sont réfléchis et non aléatoires.

#### Jeu ﬁnal 
> Q. Jouez en mode "hard" en se plaçant "Joueur 2" (joueur qui ne commence pas). Est-ce possible de gagner? Expliquer pourquoi

Oui, mais il faut que l'ordinateur fasse une erreur dans une de ses décisions, dont la probabilité est très faible, il faudra donc jouer un grand nombre de fois pour pouvoir avoir une chance de gagner contre l'ordinateur.


