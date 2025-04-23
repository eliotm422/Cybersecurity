

Beaucoup trop de fonctions, de lignes de code... Difficile de s'y retrouver.

Partons du main, on voit qu'il est beaucoup plus léger.

Restons sur cette ligne :  
``` Assembly 
b012 8644      call	#0x4486 <enc>
```

Cette ligne appelle une fonction appelée à <enc>, à l'emplacement mémoire 0x4486 de la mémoire, regardons ce qui est écrit : 

``` Assembly 
b012 8644      call	#0x4486 <enc>
```