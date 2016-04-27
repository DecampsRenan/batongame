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