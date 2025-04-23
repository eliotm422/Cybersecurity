
.microcorruption

# La solution :

* On remarque que dans la fonction <create_password>le registre r15 stocke des données
	* Ces données sont stockés dans le registre r15 (#0x2d, 0x0(r15)) à l'octet 0, puis 1 (#0x2b, 0x1(r15)), puis 2...
	* ![[Capture d'écran 2023-11-30 171636.png]]
	* Attention, la première instruction signifie qu'on va définir le registre r15 à l'emplacement de la mémoire 0x2400
	* Cela signifie avec l'instruction mov.b, qu'on déplace la valeur après (#0x) à l'emplacement de l'octet
		* N'oublions pas qu'on octet ce sont deux chiffres en hexadécimal, ce qui signifie qu'on déplace deux chiffres en hexadécimal (soit un octet) dans 1 octet (ou deux chiffres en hexadécimal)

* Ainsi on remarque que le mot de passe est stocké dans le registre r15, lui stocké dans l'emplacement de la mémoire 0x2400; et que la fonction <create_password> permet de d'écrire en dur des valeurs en hexadécimal dans le mot de passe.
![[Capture d'écran 2023-11-30 172319.png]] 
*  Par la suite on remarque que le registre *r15* est appelé dans la fonction *check_password*
, est déplacé dans le registre r13, qui sera comparé avec le registre de notre mot de passe le r13...

# La solution 

* La solution est donc pour ma part : 
	* 2d2b787867576900 
	* *Car oui un 0 en octet signifie 00 en hexadécimal

# (pour aller plus loin) Comprendre cela avec luks et dm-crypt 


* La clef ne sera jamais stocké crypté sur la mémoire, il faut que le processeur puis lire la clef en dur dans la mémoire, il n'y a pas d'autres opération entre lui et la mémoire
	* dm-crypt propose par exemple de *split-key*, c'est à dire séparer les octets de la clefs, où rajouter des octets entre les données
	* La clef à une taille définie, elle est donc facile à lire dans la mémoire, idem dm-crypt à une taille de clef définie, (dans le header par exemple avec LUKS)
	* Cependant c'est la clef crypté qu'il faut trouver avec vm-crypt :
		* C'est à dire que si on trouve le mot de passe, il nous faudra malgré trouvé la fonction qui à codé le mot de passe, pour qu'il corresponde à celui qui à été stocké
		* Autrement dit, le mot de passe stocké à lui aussi été crypté, donc il faut découvrir quels ont été les calculs qui l'ont crypté


²
16:35 : cryptage de disque dur*
18:10: La fonction de cryptage est PBKD2
18:20: la clef aléatoire est une dérivation mathématique du mdp crypté
18:30 évidemment il y a d'autres opérations, j'ai juste voulu tracer, mais je peux faire un vidéo dessus :) 
