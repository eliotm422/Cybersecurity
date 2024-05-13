
Intro : 

Ok je vais vous expliquer en 5 minutes c'est quoi une attaque buffer overflow en assembleur 
## Comprendre c'est quoi l'assembleur


![[Pasted image 20240113154832.png]]
L'assembleur est un langage de bas niveau, il est compilé depuis un langage de haut niveau, puis par la suite il est "assemblé" pour être compris par les composants de l'ordinateur.
Ainsi les instructions sont bien plus décomposées que des commandes en langage de haut niveau  , on comprendrait donc plus en détail le fonctionnement de chaque opérations, dans la mémoire, et aussi le processeur.
On peut donc décomposer certaines opérations, et le fonctionnement de certains matériels.


## Fonctionnement de la mémoire et du (micro)processeur

![[Pasted image 20240111133949.png]]

Le langage assembleur comporte les instructions, qui pointent "dans un lieu de la mémoire", plus précisément, une adresse. Chaque adresse est "unique", permettant d'associer une seule adresse à une informations. On peut cependant associer plusieurs informations à plusieurs adresses.
Il est donc important de comprendre que notre mémoire contient les valeurs qu'on va lire, écrire, modifier... 
Ces valeurs seront nos données, et c'est le processeur ou microprocesseur (un processeur qui n'a pas besoin de composants externes pour fonctionner).
Cependant il est important de noter que certaines données peuvent être lues dans le microprocesseur, à son sommet, on appelle cela des registres.
On y reviendra après.

### Fonctionnement 

* Bref, le code d'assembleur (soit le code avant d'être traduit) lit l'instruction à l'adresse mémoire 4404 (c'est de l'hexadécimal : soit 2 chiffre en octet, soit 8 chiffre en binaire : soit 2 bits x 8 octets: 16 bits (hexa)).
	On lit dans la mémoire les valeurs stockées dans l'adresse, en octet 1012 3215.

* C'est valeurs signifient des instructions à effectuer:
	* calcul, transfert de données, opérations logiques....
	* On appelle cela des opérandes

* Si une instruction à donc besoin de données, elle regardera dans la mémoire, dans des variables, des registres....

* Il y aussi le flux de contrôle permet de cependant de sauter certaines instructions, c'est à dire que le code lu dans la mémoire par le microprocesseur aura un impact sur le code assembleur.

### On résume avec un exemple : 

Thierry clique sur son programme, qui lance des instructions de langage de haut niveau (python, C, des langages de programmation faciles à écrire), qui est lui même traduit en langage assembleur, qui sera par la suite traduit en langage machine compréhensible par la machine.
Le code assembleur est une suite d'instructions qui seront exécutés par la processeur, qui lira les données : 
	* dans des registres
	* dans la mémoire
	* dans des variables 
Ces données sont, une fois lues par le processeur, comprises comme des opérations à exécuter, ce sont des opérandes.
Ces données peuvent elles même agirent sur le code assembleur, et donc par la suite sur le fonctionnement de notre ordinateur, et c'est là le point important à comprendre ! 

## Le buffer overflow 

### Comprendre 

Le principe de l'attaque est simple : 

Rappelons nous que la mémoire, les registre, les registres, contiennent des instructions qui seront comprises et lues par notre processeur.
Ces différentes instructions, effectueront diverses opérations sur notre ordinateur (par exemple lancer un programme), mais que se passe-t-il si on modifie ces données?

### Les risques 

Deux conséquences qu'on verra dans cette vidéo : 
* Exécution de programme malveillant 
* Contournement de certains principes de sécurité  
Mais aussi pleins d'autres : 
* Elévations de privilèges 
* Déni de services...
* Accès à des zones de la mémoire interdites
### Comment on modifie les données?

A vrai dire, il y a des termes comprendre :
- Memory buffer : c'est la mémoire destinées à une variable, autrement dit, c'est l'espace de stockage destiné à une variable, données... A titre de comparaison, c'est notre gourde 1 Litre d'eau, si on met 1,5 d'eau on déborde sur l'espace à côté, le principe est le même sur la mémoire.
- La mémoire, possèdes des informations stockées "côte à côte", cela dépend de l'organisation de la mémoire, mais que se passe t-il si, dans notre espace qui nous est réservé, on écrit plus de données qu'il nous est destiné? 

### Exemples 1 : contourner des principes de sécurités en modifiant une adresse de retour 

![[Pasted image 20240111122051.png]]

On décompose en trois étapes : 
où on écrit dans notre mémoire?
* Dans le programme, on demande à une personne de rentrer des informations, qui seront stockées à l'emplacement 43c9 dans le mémoire.
* Il décide de rentrer plus de données que ce lui est réservé, comme si vous mettiez un litre d'eau dans 500 ml d'eau, cela déborde sur les autres données de la mémoire.
* Par la suite dans ce programme, on remarque que l'instruction à l'adresse de la mémoire 453e, contient la valeur 3041 (traduit par le microprocesseur en return)

où cela présenterai des failles?
* Implicitement, on remarque que pendant cette instructions,  on lit la pile SP, soit l'adresse 43fe, ça sera la destination de notre adresse return
* On rappelle qu'on peut rentrer des données à l'emplacement 43c9, si on écrit trop de données, on dépasse sur l'emplacement 43fe
* Si on écrit trop gros volume de données, on dépasse donc sur les données qui seront lues pour l'instruction return (cette instruction permet de se déplacer dans la mémoire), que se passe-t-il si on écrit une adresse vers laquelle on voudrait aller ? 
* Imaginons que si on va à l'adresse 2845, on déverouille le niveau, mais pour accéder il faut trouver un mot de passe de 24 caractères... c'est dur.

Comment exploiter ces failles? 
* On rentrera à l'adresse 43fe la valeur 2845 jusqu'à l'adresse 43fe, là où le processeur lira 4528 (ça s'appelle l'Endianess on inverse les octets 2 par deux), qui est l'emplacement qu'on souhaite atteindre.
* Ainsi on contourne pleins d'instruction et on atteint l'instruction "on déverrouille la porte"
* TADAM : démo 

### Exemples 2 : contourner des principes de sécurités en rentrant les valeurs demandées 

![[Pasted image 20240111140935.png]]


* On remarque qu'on cherche la valeur 8e écrite à l'adresse mémoire 2410
* On écrit notre mdp à l'emplacement 2400
* On écrit donc 8e8e8e8e8e8e8e8e en boucle, jusqu'à atteindre l'emplacement 2410
* Ainsi le registre d'instruction compara la valeur qu'il veut trouver, à savoir 8e, avec ce qui est écrit à l'emplacement mémoire 2410, là où nous avons écrit 8e
* TADAM
