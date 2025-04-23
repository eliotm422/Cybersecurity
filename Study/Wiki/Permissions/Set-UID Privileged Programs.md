
### Programmes Set-UID Privilégiés : Résumé

**Aperçu du mécanisme Set-UID :**
- **Objectif** : Les programmes Set-UID octroient aux utilisateurs des privilèges supplémentaires qu'ils n'ont pas habituellement. Un exemple est le programme `passwd`, qui permet aux utilisateurs de modifier une entrée spécifique dans le fichier `/etc/shadow` pour changer leur mot de passe, sans leur accorder la permission de modifier directement ce fichier.
  
- **UID Effectif et Réel** :
  - **UID Réel** : Identifie l'utilisateur réel qui exécute le programme.
  - **UID Effectif** : Utilisé pour le contrôle d'accès, il est défini comme étant le propriétaire du programme Set-UID.

**Comment cela fonctionne :**
- Normalement, les UID réel et effectif sont identiques. Cependant, dans les programmes Set-UID, l'UID effectif est défini sur celui du propriétaire du programme, ce qui lui permet d'effectuer des tâches privilégiées pour le compte de l'utilisateur.

**Mécanisme Set-UID sous Windows vs UNIX :**
- **Windows** : Il n'existe pas de mécanisme Set-UID ; à la place, les services s'exécutent sous le compte "Local System" et gèrent les privilèges via des descripteurs de sécurité.

**Risques de sécurité et vulnérabilités dans les programmes Set-UID** :

1. **Variables d'environnement** :
   - Les programmes peuvent être indirectement influencés par des variables d'environnement comme `PATH`, `IFS`, `LD_LIBRARY_PATH` et `LD_PRELOAD`. Si ces dernières sont manipulées par un attaquant, cela peut entraîner un comportement inattendu ou l'exécution de code malveillant.

2. **Vulnérabilité liée à PATH** :
   - Les attaquants peuvent modifier la variable `PATH` pour exécuter leurs propres programmes malveillants au lieu des commandes système légitimes, en particulier si le programme Set-UID repose sur des appels système comme `system()` qui invoquent un shell.

3. **Vulnérabilité liée à IFS** :
   - Si la variable `IFS` est modifiée, des caractères spéciaux comme les barres obliques peuvent être mal interprétés, entraînant l'exécution de commandes non prévues.

4. **Vulnérabilités liées à LD_LIBRARY_PATH et LD_PRELOAD** :
   - Les attaquants peuvent exploiter ces variables pour charger des bibliothèques partagées malveillantes, remplaçant ainsi les bibliothèques standard et exécutant des fonctions nuisibles. Cependant, ces variables d'environnement sont ignorées par le système lorsqu'un programme Set-UID est exécuté.

5. **Appel d'autres programmes** :
   - Un appel imprudent à d'autres programmes, surtout via des commandes comme `system()` ou en utilisant des entrées fournies par l'utilisateur, peut entraîner des risques de sécurité, tels que des injections de commandes si les entrées ne sont pas correctement filtrées.

**Modèles de vulnérabilités courantes** :
- **Dépassements de tampon** : Un attaquant peut exploiter des erreurs de gestion de la mémoire pour exécuter du code arbitraire.
- **Conditions de concurrence (race conditions)** : Exploite le timing entre les opérations pour obtenir des privilèges.
- **Vulnérabilités de formatage de chaînes** : Se produit lorsque les entrées de l'utilisateur sont traitées comme faisant partie d'une chaîne de format, ce qui peut entraîner l'exécution de code.

**Améliorer la sécurité des programmes Set-UID** :
- Évitez d'utiliser des appels système qui invoquent un shell, comme `system()` ou `execvp()`. Privilégiez `execve()` pour exécuter des programmes de manière sécurisée.
- Soyez prudent avec les fonctions qui peuvent dépendre du comportement d'un shell (par exemple, la fonction `open()` en Perl).
- Assurez-vous de valider correctement les entrées et évitez de vous fier aux variables d'environnement contrôlées par l'utilisateur.

### Résumé des principales mesures défensives :

- **Vérification des entrées** : Assurez-vous que toutes les entrées utilisateur, y compris les variables d'environnement, sont validées afin d'empêcher tout comportement malveillant.
- **Limiter les invocations de shell** : Évitez d'invoquer des shells dans des programmes privilégiés pour réduire les risques d'injections de commandes.
- **Liens statiques** : Utilisez des liens statiques ou des bibliothèques de confiance pour éviter les vulnérabilités liées au chargement dynamique, comme `LD_LIBRARY_PATH`.
- **Protection contre les dépassements de tampon et les conditions de concurrence** : Implémentez des protections contre les vulnérabilités courantes comme les dépassements de tampon et les conditions de concurrence.

Les programmes Set-UID sont puissants mais introduisent des défis de sécurité significatifs. Une validation rigoureuse des entrées, une utilisation prudente des variables d'environnement et une limitation des invocations de shell sont essentielles pour sécuriser ces programmes.

### Pourquoi est-il important de limiter les privilèges ?
La principale raison de limiter les privilèges nécessaires pour exécuter un programme est de réduire les dommages qui pourraient être causés en cas d'exploitation d'une vulnérabilité par un utilisateur malveillant. Si un programme fonctionne avec des privilèges basiques, il est plus difficile pour un attaquant de causer des dommages importants. À l'inverse, si un programme nécessite des privilèges d'administrateur, une faille de sécurité pourrait entraîner des dommages beaucoup plus graves.

### Questions à se poser lors de l'écriture d'un programme privilégié :

1. **Le programme a-t-il besoin de privilèges ?**
   - Si un programme n'a pas besoin de privilèges particuliers pour fonctionner, il ne devrait pas en disposer.
  
2. **Le programme a-t-il besoin de tous les privilèges ?**
   - Il faut accorder au programme le minimum de privilèges nécessaire à l'accomplissement de sa tâche.
   - Dans certains systèmes d'exploitation (comme la plupart des systèmes Unix), les choix sont souvent limités : soit l'utilisateur dispose de tous les privilèges "root", soit de rien. Cependant, les systèmes Unix modernes et Windows permettent une granularité plus fine des privilèges, ce qui facilite l'application du principe du moindre privilège.

3. **Le programme a-t-il besoin des privilèges en ce moment ?**
   - Un programme n'a souvent besoin de certains privilèges qu'à certains moments. Il est donc conseillé de désactiver temporairement les privilèges inutiles pour minimiser les risques en cas d'erreur ou de faille.
   - Si les privilèges deviennent nécessaires à nouveau, ils peuvent être réactivés.

4. **Le programme aura-t-il besoin des privilèges à l'avenir ?**
   - Si un privilège ne sera plus utilisé, il devient inutile et doit être définitivement supprimé.

### Mécanismes Unix pour appliquer le principe du moindre privilège :
- **Appels systèmes utiles** : `setuid()`, `seteuid()`, `setgid()`, et `setegid()`.

1. **seteuid(uid)** : Cet appel définit l'ID utilisateur effectif du processus appelant. 
   - Si l'ID effectif est celui du super-utilisateur, l'argument `uid` peut être n'importe quel ID. Cela permet à un programme d'abandonner temporairement ses privilèges et de les récupérer plus tard. 
   - Si l'ID effectif n'est pas celui du super-utilisateur, `uid` ne peut être que l'ID effectif, réel, ou sauvegardé de l'utilisateur.

2. **setuid(uid)** : Définit l'ID utilisateur effectif du processus appelant, ainsi que les IDs utilisateur réels et sauvegardés si le processus est exécuté par le super-utilisateur. Cela permet de renoncer définitivement aux privilèges root.

### Exemples (Fedora Linux) :
- Un processus s'exécute avec un **ID utilisateur effectif = 0** et un **ID utilisateur réel = 500**. Voici ce que font les appels suivants :
  - `setuid(500); setuid(0);` → Réponse : 500/500 (le premier appel génère 500/500, et le second échoue).
  - `seteuid(500); setuid(0);` → Réponse : 0/500 (le premier appel génère 500/500, et le second génère 0/500).
  - `seteuid(600); setuid(500);` → Réponse : 500/500 (le premier appel génère 600/500, et le second génère 500/500).
  - `seteuid(600); setuid(500); setuid(0);` → Réponse : 0/500 (le premier appel génère 600/500, le second 500/500, et le troisième 0/500).