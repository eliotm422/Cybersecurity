  
* Bonjour, la vidéo m'a pris beaucoup plus de temps que prévu, elle n'était censé pas moins de 15 min, mais en réalité elle va faire le triple car j'essaie à chaque fois de peaufinner. J'ai décidé 
* Cette vidéo est à but préventif et éducatif,
* En 10 minutes je vais vous expliquer comment craquer, c'est à dire "deviner" un mot de passe Windows. Je vous rassure, si vous n'y connaissez rien, ne vous en faites pas je vais tout expliquer étape par étape
* Je pourrai utiliser un outil déjà développé pour trouver le mot de passe, mais il n'y aura rien d'instructif à cela

# Comprendre c'est quoi un mot de passe

Ca va être tout simplement une série de caractère qui vont nous permettre de nous authentifier et de prouver donc notre identité pour accéder à des ressources.	 On va donc comparer ce que rentre l'utilisateur, avec le mot de passe qui est stocké.
# Comprendre : c'est quoi Windows 


* C'est un système d'exploitation (OS), il permet d'exploiter les ressources matérielles d'un ordinateur, c'est à dire votre mémoire, votre disque dur, votre processeur...  Il permet d'agir comme interface entre le matériel d'un ordinateur, et les programmes applicatifs. Il permet de communiquer entre les ressources matérielles de l'ordinateurs et les ressources logicielles, qui sont par exemple word, chrome, du code en quelque sorte, puisque quand on clique sur un programme on lance du code.
* ![[Pasted image 20240120164649.png]]
* Il y trois OS connus, 2 qui sont propriétaires, Windows et MacOS, à savoir que le code est réservé à l'entreprise, donc seuls eux peuvent travailler dessus. Il y a sinon Linux en open source, tous le monde peut travailler dessus.
* ![[Pasted image 20240120164715.png]]
* Pour comprendre les OS un exemple de ma tête :
* On donne une feuille et un crayon à 20 personnes dans une salle, on leur demande d'écrire "mais c'est ça le rock". Ici, 
	* les ressources matérielles vont être, les mains, les yeux que vont utiliser les élèves (leur ressources qui leurs appartiennent).
	* Les stylos et les feuilles seront les ressources logicielles (ressources qu'on leur a donné), propre à chacun.
	* Leo cerveau propre à chacun permettront de coordonner les deux (ressource qui fera le lien entre les deux, et qui est spécifique à chacun, ça va être le rôle de l'OS).
	* Le résultat de notre exercice sera le même, ils écriront "mais c'est ça le rock", ça ne sera pas écrit exactement de la même manière, ni à la même vitesse, mais le résultat sera identique.
	* Les OS c'est pareil, ils veulent accomplir une même tâche, mais certains y arriveront plus rapidement que d'autres, d'autres plus facilement que d'autres...
	* ![[Pasted image 20240120164741.png]]
* Bon maintenant parlons un tout petit peu du fonctionnement d'un OS (2min pas plus)

* ## Pour la culture, petit aparté :
	* Les pilotes, ils permettent la traduction entre les instructions générées périphérique avec les programmes de votre système d'exploitation et le langage matériel, ils communiquent directement avec le noyau du système d'exploitation, c'est là où passent les appels systèmes lors de l'utilisation d'une instruction, si un pilote n'est pas à jour, certaines instructions pourraient être mal comprises par votre ordinateur, d'où la fameuse solution à vos problèmes :  "Il faut mettre les pilotes à jour !"
		*cf schéma pilote
		![[Pasted image 20240111142001.png]]
	*  Les appels systèmes fournissent une interface entre les applications et le noyau, permettant aux applications d'effectuer des opérations complexes tout en maintenant la sécurité et l'intégrité du système d'exploitation. Ils jouent un rôle essentiel dans la gestion des ressources et des services du système.
		*cf schéma appels systèmes
		![[Pasted image 20240111142031.png]]
	* En résumé, les appels systèmes sont des interfaces générales pour interagir avec le système d'exploitation, tandis que les pilotes sont des logiciels spécifiques qui facilitent la communication entre le système d'exploitation et le matériel. Les appels système permettent aux applications de demander des services au noyau, tandis que les pilotes fournissent une interface entre le noyau et le matériel pour des opérations spécifiques.


* ## Comment le système d'exploitation fonctionne : 
	* Brièvement, la carte mère permet la communication entre les différents composants de l'ordinateur, elle possède en elle un BIOS (UEFI récemment). Ce firmware (microprogramme, un programme indépendant pour fonctionner) initialise les composants matériels, effectue des vérifications et prépare le système pour le démarrage.
	* Il cherche ensuite un (ou plusieurs) périphériques de démarrage qui contient le système d'exploitation
	* Il sera chargé en mémoire pour prendre le contrôle du système 
	* Ensuite, le système d'exploitation enverra ses instructions à la carte mère qui traduira ces informations entre les différents composants des systèmes 
		 *cf schéma fonctionnement matériel
	![[Pasted image 20240111141902.png]]

* Pour résumer : Maintenant qu'on a compris les principes d'un système d'exploitation, on comprend mieux pourquoi lorsqu'on installe une application on nous demande quel est le système d'exploitation qu'on utilise  :
	* L'application reste la même cependant la façon dont sont exploitées les ressources dépendent donc du système d'exploitation ( rappelez vous l'exemple)
	* C'est pour cela que craquer un mot de passe dépendra du système d'exploitation, la manière de stocker un mot de passe ne sera pas identique ! 

# Le scénario : 

## Mot de passe stocké en clair 

* Mon ordinateur Windows est verrouillé et je n'arrive pas à retrouver le mot de passe, combien il y a t'il de possibilités ? Essayer de deviner... 
* Si on rentre un mot de passe de 1 caractère, parmi 26 possibilités, on est à 26^1 possibilités
* Pour 4 caractères, parmi 26 possibilités : 26^4 possibilités : 456 796 possibilités
* On remarque que le nombre de possibilité augmente très vite, c'est pour cela qu'on vous demande un mot de passe de minimum 8 caractères... Cela augmente grandement la robustesse d'un mot de passe
* Pour vérifier le robustesse d'un mot de passe, regarder ce lien : *ANSSI MDP

* J'ai programmé (bon je ne suis pas un expert), un petit programme qui permet de vite décoder cela. On teste pour chaque lettre, si le mot de passe stocké correspond avec une lettre du clavier (on teste cela 1 par 1), si oui on la garde en mémoire et on passe à la seconde lettre, plutôt simple non? 
* ![[Pasted image 20240120174614.png]]
* *Démo crackage mdp* 
* On remarque cependant qu'on décode très vite cela pourquoi? Puisque nos ressources matérielles sont de plus en plus puissantes avec le temps, donc plus de calculs, plus d'efficacité. Si on stocke un mdp en clair, cela s'avère très peu efficace 
Comment pallier cela? 
## Mot de passe hasher et sel 

* A vrai dire, aucune source sur internent évoque toutes les possibilités, mais comprenons le problème :
	* Pour accéder au mot de passe windows, voici les étapes : 
	* ![[Pasted image 20240120175440.png]]
		* Michel rentre le mot de passe ("Jack")
		* On Ajoute du sel à la suite du mot de passe : c'est une générée valeur aléatoirement ajouté au hash (on y viendra après), cela permet d'éviter qu'en précalculant le hash on trouve le mot de passe, puisque le mot de passe dépend du sel et du hash
		* On ajoute ensuite un hash, c'est à dire mathématiquement transformé en suite de caractères aléatoires, uniques, qui ne peuvent être reproduits qu'avec la même chaine de base et le même hashage (démontré mathématiquement, c'est ce qu'on appelle de la cryptologie)
		* Stockage sécurisé dans un registre sécurisé 
* Essayons de cracker le mot de passe avec le hash: 
	* Pour bien comprendre, on va essayer sur un mot de passe stocké en clair : 
		*cf code python mdp en dur , on remarque que j'ai mis un nombre de caulculs max pour éviter d'y passer la journée
		* En remarque qu'on ne trouve pas le mot de passe, et si on l'affichait?
		* Ok, le mot de passe est clairement plus long, et si on réessayait avec le mot de passe? 
		* Totalement différent, il faut donc comprendre comment trouver le mot de passe ? 
		* Le moyen le plus simple serait de trouver donc le hash, pourquoi ? 
			* Si on trouve le hash (le plus dur), on trouvera donc plus facile le mot de passe et le sel, je vous rappelle qu'on en cherche pas le mot de passe crocodile, mais le mot de passe final.
			* Comment faire cela? Et ba beaucoup de logiciels représentes des points communs, je vous rappelle que ce sont des programmes qui sortent oui des valeurs aléatoires, mais certains logiciel de hashage se caractérisent par :
				* - Leur longueur
				* - Certains caractères spéciaux au début à la fin
			* Avec cela on pourrait identifier le hash  *demo* https://www.dcode.fr/hash-identifier
			* Ok maintenant qu'on a trouvé le type de hash, comment trouver la clef de cryptage sachant que c'est censé être mathématiquement introuvable? 
			* Et baaaaaaaa bonne question, c'est impossible, c'est le but justement du procédé : qu'on ne puisse pas décrypter. Enfaite on peut pas y trouver le mot de passe, 1c70088b4b9c650d49fd3ee04349dfb9, imaginons ce mdp stocké de 33 caractères, il faudrait donc 26^33, soit beaucoup trop de possibilités…
			* Il existe cependant deux types d'attaques possibles : 
				* les attaques par dictionnaires, on essaie des possibilités connues déjà connues du hash la chance de trouver est faible mais au moins l'attaque est rapide, le but n'est pas de trouver le hash, mais des résultats de mdp et de hash. Il faudra qu'on connaisse cependant le hash
				* ou alors une attaque par "table arc en ciel", enfaite il faut récupérer le mot de passe 1c70088b4b9c650d49fd3ee04349dfb9 déjà stocké,  et enfaite en pa²rtant de cela, on va essayer de faire le chemin inverse avec toutes les possibilités de hash. 
			* On va utiliser des outils déjà développés sur kali Linux. 

# Crackage de mdp avec kali linux 

* Je rappelle deux principes : 
	* Déchiffrer un mot de passe consiste à le décoder avec une clef (donc celle de chiffrement)
	* 

reprendre le schéma sur les pilotes 
reprendre sur les appels systèmes 

0 min : Vidéos en deux parties ! 
0 min : Comprendre c'est quoi un os 
3 min pile : Mais c'est ça le rock
4 min : mais c'est ça le rock 
4:50 : Le fonctionnement des pilotes
