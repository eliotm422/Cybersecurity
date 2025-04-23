.microcorruption
[[Microcorruption]] [[New Orlean]] [[Sydney]] [[Cusco]] [[Whitehorse]]

Buffer overflow
Immunity debbuger 
# I :  Introduction à l'assembleur


* Langage d'assembleur : il communique directement avec le microprocesseur : c'est un langage de bas niveau, il est lié au fonctionnement de la machine
* C'est pour ça en le comprenant, on comprendra d'autres notions
* ![[Pasted image 20231121093542.jpg]]

## I.1 : Le compilateur 

* Il permet de traduire le code source, il indique si le code présente des erreurs*
![[Pasted image 20231121093442.png]]

## I.2 : L'assembleur

* Il permet de traduire le code source, la sortie est un langage compréhensible par l'ordinateur*
* C'est l'interface la plus proche entre la machine et l'humain, le langage est composé d'instructions, l'assembleur les traduira en code binaire
* Le langage est basé sur les microcontrôleurs
![[Pasted image 20231121093810.png]]


## I.3 : Interprète

![[Pasted image 20231121094449.png]]
* Il lit ligne par ligne le code source et le traduit en instruction, si le code source présente une erreur, l'interprète affichera la ligne qui présentera un problème 
## Registre

Pour travailler, le microprocesseur utilise de petites zones où il peut stocker des données. Ces zones portent le nom de registres et sont très rapides d'accès puisqu'elles sont implantées dans le microprocesseur lui-même et non dans la mémoire vive.

# II Comment lire l'assembleur sur Microcorruption

## II.1 Disassembly 

Avec Intel : 
https://defuse.ca/online-x86-assembler.htm
Git : 
https://yozan233.github.io/Online-Assembler-Disassembler/

* Il présente les instructions, c'est un ensemble d'octets, dont chaque octet est représenté par 2 caractères hexadécimaux
* Chaque octet représente un code en assembleur
* A gauche c'est l'emplacement de l'instruction dans la mémoire, à côté c'est le code en hexa des instructions, et à droite c'est le code mieux rédigé

## II.2 Live Memory Dump 

https://cdiese.fr/les-dumps-memoire-en-5-min/
* Copie du contenu de la mémoire virtuelle, on peut y voir l'instruction, la valeur de l'instruction

## II.3 Disassembly


Il y a l'adresse de l'instruction, le code de cette instruction.

## II.4 Register State 
https://www-igm.univ-mlv.fr/~dr/XPOSE2008/RCE_KG_IR3/pratique.html#1

Un registre est un emplacement de mémoire interne à un processeur. Les registres se situent au sommet de la hiérarchie mémoire : il s'agit de la mémoire la plus rapide d'un ordinateur, mais dont le coût de fabrication est le plus élevé, car la place dans un microprocesseur est limitée.
# III Pourquoi faire du microcorruption ?


* Permet de visualiser le fonctionnement en interne du processeur, très proche de la machine, mais très compliqué à comprendre.
* On peut contourner des mécanismes de sécurité au niveau applicatif, comme par exemple les protections contre les débordements de tampon.
* Une analyse plus complète et précise, certaines failles apparaitront dans le langage assembleur et n'apparaîtront pas des niveaux plus élevés 
* Performances et optimisation !!!

# Le reverse Engineering / rétro ingénierie


* Des outils :
	* Les désassembleurs (Ollybg), convertit le language machine en language plus ou moins compréhensible
	* Les décompilateurs 
	* Les débogueurs