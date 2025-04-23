Le Buffer Overflow se produit lorsque l'on écrit plus de données que ce que peut contenir un tampon mémoire. Dans ce cas précis, cela mène à l'écrasement du "Program Counter" (compteur programme), également connu sous le nom de "Instruction Pointer" (pointeur d'instruction). Cela se produit car la zone mémoire où résident nos données d'entrée est trop proche des instructions du programme, ce qui permet de les écraser.

L'explication repose sur le fait que la pile de mémoire grandit vers des adresses mémoire inférieures, alors que les écritures en mémoire se font vers des adresses mémoire supérieures. À chaque ajout d'élément dans la pile, celui-ci se place vers des adresses mémoire plus basses. Ainsi, la pile grandit vers des adresses mémoire inférieures, en direction du tas (heap).

Chaque fois qu'une fonction est appelée, le pointeur d'instruction (Program Counter) saute vers une autre partie de la mémoire. Pour retourner au bon endroit après cette exécution, il doit savoir où revenir. C'est ce qu'on appelle le "Function prologue" (prologue de fonction). Pendant ce prologue, l'adresse de l'instruction suivant le saut est sauvegardée, c'est-à-dire l'adresse où le pointeur d'instruction doit revenir, parmi d'autres informations. Cette adresse est généralement appelée RETADDR, adresse de retour ou @ret.

Imaginons maintenant qu'une fonction qui vient d'être appelée possède un tampon mémoire. Comme la pile grandit vers des adresses mémoire inférieures, ce tampon sera "situé sous" l'adresse de retour. Si ce tampon n'a pas de vérification de limites, c'est-à-dire qu'il peut être écrit sans limite, alors même s'il est censé contenir 16 octets, on peut écrire 200 octets et ainsi écraser ce qui se trouve à 200 octets "au-dessus" de l'adresse de départ de notre tampon.

Cela explique comment une manipulation non sécurisée de tampons peut conduire à écraser des zones mémoire critiques, ce qui est souvent exploité pour des attaques malveillantes.

453a
  
Ce passage explique pourquoi l'adresse de retour (retaddr) que nous voulons écraser est celle de la fonction `login`. Cela se rapporte à la façon dont les écritures en mémoire se font vers des adresses mémoire supérieures et comment la pile grandit vers des adresses mémoire inférieures.

Dans ce scénario, nous ne pouvons pas écraser la valeur de retour d'une fonction qui a été déclarée après notre tampon mémoire. En effet, la pile (où réside notre tampon) grandit vers des adresses mémoire supérieures, et les adresses de retour des fonctions appelées ultérieurement se trouveront donc au-dessus de notre tampon.

La fonction `main` est celle qui appelle `login` et à un moment donné, le pointeur d'instruction (Instruction Pointer) doit retourner à `main`. À l'intérieur de `login`, notre tampon est déclaré, et après cette déclaration, viennent les autres appels de fonctions. Étant donné que l'écriture dans le tampon se fera vers des adresses mémoire plus élevées, la seule adresse de retour que nous pouvons écraser est celle de `login`.

En résumé, étant donné que le tampon où nous écrivons se situe avant les autres adresses de retour des fonctions ultérieures dans la pile (du fait de la manière dont la pile grandit), la seule adresse de retour que nous pouvons affecter est celle de la fonction `login`. Cela donne à l'attaquant la possibilité de contrôler où le programme exécutera le code après l'exécution de `login`, ce qui est une des méthodes courantes d'exploitation de débordement de tampon.