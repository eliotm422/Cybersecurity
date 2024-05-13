Le principe fondamental derrière l'exécution de code dans la mémoire grâce à une vulnérabilité de débordement de tampon (Buffer Overflow) repose sur la manipulation des données stockées dans la mémoire d'un programme pour altérer son comportement prévu.

Lorsqu'un programme s'exécute, il utilise la mémoire pour stocker des données, telles que des variables, des instructions et d'autres informations nécessaires pour son fonctionnement. Cette mémoire est organisée de manière spécifique, avec différentes zones pour les variables locales, les données statiques, le code du programme lui-même, etc.

Un débordement de tampon se produit lorsqu'une quantité de données supérieure à celle prévue est écrite dans une zone de la mémoire, souvent un tableau ou une mémoire tampon. Si cette opération n'est pas correctement contrôlée par le programme, elle peut écraser d'autres parties de la mémoire, y compris des adresses de retour, des variables, voire des instructions.

L'exploitation d'une telle faille implique souvent la manipulation de la pile d'exécution du programme. La pile est une structure de données utilisée par les programmes pour stocker des informations temporaires, y compris les adresses de retour des fonctions et des variables locales.

En exploitant une faille de débordement de tampon, un attaquant peut délibérément écrire plus de données que ce qui est attendu dans une zone tampon, et ainsi déborder dans des zones adjacentes de la mémoire, notamment la pile. En écrivant délibérément des données spécifiques dans la pile, un attaquant peut modifier les adresses de retour stockées lors des appels de fonction.

Lorsque le programme atteint un point où il doit retourner à l'adresse stockée sur la pile pour continuer son exécution (par exemple, retour d'une fonction), il saute à cette adresse. Si un attaquant a réussi à écrire une adresse de son choix dans la zone de la pile qui stocke l'adresse de retour, il peut forcer le programme à sauter à cette adresse spécifique.

C'est à ce stade que l'attaquant peut contrôler le flux d'exécution du programme en lui faisant sauter à une zone de la mémoire où il a injecté son propre code malveillant, souvent appelé "shellcode". Ce shellcode est généralement du code machine spécifique à la plateforme cible (par exemple, assembleur pour x86), conçu pour exécuter des actions spécifiques, telles que lancer un shell ou donner un accès à distance à l'attaquant.

En résumé, l'exécution de code dans la mémoire grâce à une vulnérabilité de débordement de tampon implique la manipulation des données stockées pour contrôler le flux d'exécution du programme et lui faire exécuter du code malveillant injecté par l'attaquant.