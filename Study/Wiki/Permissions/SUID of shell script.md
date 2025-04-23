.pentest


L'article "Dangers of SUID Shell Scripts" de Thomas Akin, publié dans le *Sys Admin Magazine* en juin 2001, explique les risques liés à l'utilisation des scripts SUID (Set User ID) dans les environnements UNIX et propose des solutions pour éviter les failles de sécurité courantes. Les programmes SUID permettent à un script ou programme d’être exécuté avec les droits de son propriétaire, souvent "root", plutôt que ceux de l’utilisateur qui l’exécute, ce qui peut poser de sérieux problèmes de sécurité.

### Principales failles et leçons :

1. **Utilisation des scripts C-shell** : Les scripts écrits en C-shell sont vulnérables à la manipulation des variables d'environnement. Solution : éviter les scripts C-shell pour les programmes SUID et utiliser Korn shell (ksh) ou d'autres alternatives plus sûres.
   
2. **Chemins relatifs et variables PATH** : Un attaquant peut modifier la variable d'environnement `PATH` pour exécuter son propre programme à la place de celui attendu (comme le programme `passwd`). Solution : utiliser des chemins absolus pour toutes les commandes exécutées.

3. **Mauvaise gestion des arguments** : Si aucun argument n’est fourni, certains programmes comme `passwd` peuvent par défaut modifier le mot de passe de l'utilisateur courant (dans le cas d’un script SUID root, cela serait root lui-même). Solution : vérifier et valider les arguments fournis.

4. **Utilisation de fichiers temporaires** : L'usage de fichiers temporaires dans des répertoires accessibles par tous (comme `/tmp`) est dangereux car ils peuvent être manipulés par un attaquant via une attaque de type "race condition". Solution : éviter les fichiers temporaires ou les placer dans des répertoires sécurisés.

5. **Meta-caractères dans les arguments** : Les caractères spéciaux comme `;`, `|`, ou `&` permettent à un attaquant d'exécuter des commandes arbitraires. Solution : nettoyer et vérifier les entrées utilisateur pour éliminer ces caractères.

6. **Manipulation du séparateur de champs interne (IFS)** : En modifiant l'IFS (Internal Field Separator), un attaquant peut perturber l’interprétation des chemins par le script. Solution : définir explicitement l'IFS dans le script.

7. **Race condition dans l'exécution des scripts SUID** : Les scripts shell SUID sont intrinsèquement vulnérables aux attaques "race condition" car le shell doit lire le script après l'avoir ouvert. Solution : éviter complètement les scripts shell SUID, car ils sont quasiment impossibles à sécuriser.

### Conclusion :
L'article recommande de ne pas utiliser de scripts shell SUID, car ils sont trop difficiles à sécuriser. À la place, il suggère des alternatives plus sûres, comme l’utilisation de programmes écrits en C, de scripts Perl (qui ont des protections intégrées), ou d’outils comme `sudo` pour gérer les privilèges.