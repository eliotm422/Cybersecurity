
Debuger en system mode, utilisé sur une interface web de routeur.

Comment faire de l'émulation : Qiling, sur unicorn qui est sur QEMU.

Qiling : ça utilise un filesystem un exe et un profile (emplacement de la mémoire, taille...), à la différence que cela se base sur le process, un type de conteneur ???

RevenUnicorn : Enregistre le processeur à chaque instruction; on doit connaître les zones mémoire, donc à chaque instruction appel API (deux lignes de codes)

Donc Qilling appelle RevenUnicorn pour les fonctions, qui sotn développés (écriture, lecture mémoire...)

Petit problème : les libraires doivent être bien chargés 

Le ROP : utiliser du code déjà présent dans le binaire pour l'exploiter