Beaucoup trop de fonctions, de lignes de code... Difficile de s'y retrouver.

Partons du main, on voit qu'il est beaucoup plus léger.

Restons sur cette ligne :  
```Assembly 
b012 8644      call	#0x4486 <enc>
```

Cette ligne appelle une fonction appelée à <enc>, à l'emplacement mémoire 0x4486 de la mémoire, regardons ce qui est écrit : 

```Assembly 
4480: 6768 743f 0000 0b12 0a12 0912 0812 0d43   ght?...........C
4490: cd4d 7c24 1d53 3d90 0001 fa23 3c40 7c24   .M|$.S=....#<@|$
44a0: 0d43 0b4d 684c 4a48 0d5a 0a4b 3af0 0f00   .C.MhLJH.Z.K:...
44b0: 5a4a 7244 8a11 0d5a 3df0 ff00 0a4d 3a50   ZJrD...Z=....M:P
44c0: 7c24 694a ca48 0000 cc49 0000 1b53 1c53   |$iJ.H...I...S.S
44d0: 3b90 0001 e723 0b43 0c4b 183c 1c53 3cf0   ;....#.C.K.<.S<.
44e0: ff00 0a4c 3a50 7c24 684a 4b58 4b4b 0d4b   ...L:P|$hJKXKK.K
44f0: 3d50 7c24 694d cd48 0000 ca49 0000 695d   =P|$iM.H...I..i]
4500: 4d49 dfed 7c24 0000 1f53 3e53 0e93 e623   MI..|$...S>S...#
4510: 3841 3941 3a41 3b41 3041 0e4f 0f4e 3041   8A9A:A;A0A.O.N0A
4520: 7768 6174 2773 2074 6865 2070 6173 7377   what's the passw
4530: 6f72 643f 0000 0013 4c85 1bc5 80df e9bf   ord?....L.......
4540: 3864 2bc6 4277 62b8 c3ca d965 a40a c1a3   8d+.Bwb....e....
4550: bbd1 a6ea b3eb 180f 78af ea7e 5c8e c695   ........x..~\...
4560: cb6f b8e9 333c 5aa1 5cee 906b d1aa a1c3   .o..3<Z.\..k....
4570: a986 8d14 08a5 a22c baa5 1957 192d abe1   .......,...W.-..
4580: 66b9 f4b9 4a08 e95c d919 8069 07a5 ef01   f...J..\...i....
4590: caa2 a30d f344 815e 3e10 e765 2bc8 2837   .....D.^>..e+.(7
45a0: abad ab3f 8cfa 754d 8ff0 b083 6b3e b3c7   ...?..uM....k>
```

Continuons, on voit un appel à une fonciton à 2400 :
```Assembly
b012 0024      call	#0x2400
```

```Assembly
2400: 0b12 0412 0441 2452 3150 e0ff 3b40 2045   .....A$R1P..;@ E
2410: 073c 1b53 8f11 0f12 0312 b012 6424 2152   .<.S........d$!R
2420: 6f4b 4f93 f623 3012 0a00 0312 b012 6424   oKO..#0.......d$
2430: 2152 3012 1f00 3f40 dcff 0f54 0f12 2312   !R0...?@...T..#.
2440: b012 6424 3150 0600 b490 9357 dcff 0520   ..d$1P.....W... 
2450: 3012 7f00 b012 6424 2153 3150 2000 3441   0....d$!S1P .4A
2460: 3b41 3041 1e41 0200 0212 0f4e 8f10 024f   ;A0A.A.....N...O
2470: 32d0 0080 b012 1000 3241 3041 d21a 189a   2.......2A0A....
2480: 22dc 45b9 4279 2d55 858e a4a2 67d7 14ae   ".E.By-U....g...
2490: a119 76f6 42cb 1c04 0efa a61b 74a7 416b   ..v.B.......t.Ak
24a0: d237 a253 22e4 66af c1a5 938b 8971 9b88   .7.S".f......q..
24b0: fa9b 6674 4e21 2a6b b143 9151 3dcc a6f5   ..ftN!*k.C.Q=...
24c0: daa7 db3f 8d3c 4d18 4736 dfa6 459a 2461   ...?.<M.G6..E.$a
24d0: 921d 3291 14e6 8157 b0fe 2ddd 400b 8688   ..2....W..-.@...
24e0: 6310 3ab3 612b 0bd9 483f 4e04 5870 4c38   c.:.a+..H?N.XpL8
24f0: c93c ff36 0e01 7f3e fa55 aeef 051c 242c   .<.6..>.U....$,
2500: 3c56 13af e57b 8abf 3040 c537 656e 8278   <V...{..0@.7en.x
2510: 9af9 9d02 be83 b38c e181 3ad8 395a fce3   ..........:.9Z..
2520: 4f03 8ec9 9395 4a15 ce3b fd1e 7779 c9c3   O.....J..;..wy..
2530: 5ff2 3dc7 5953 8826 d0b5 d9f8 639e e970   _.=.YS.&....c..p
2540: 01cd 2119 ca6a d12c 97e2 7538 96c5 8f28   ..!..j.,..u8...(
2550: d682 1be5 ab20 7389 48aa 1fa3 472f a564   ..... s.H...G/.d
2560: de2d b710 9081 5205 8d44 cff4 bc2e 577a   .-....R..D....Wz
2570: d5f4 a851 c243 277d a4ca 1e6b 0000 0000   ...Q.C'}...k....
2580: 0000 0000 0000 0000 0000 0000 0000 0000   ................
```


Rien de bien compréhensible, on va désasembler le code pour comprendre
```Dissasembly
0b12           push	r11
0412           push	r4
0441           mov	sp, r4
2452           add	#0x4, r4
3150 e0ff      add	#0xffe0, sp
3b40 2045      mov	#0x4520, r11
073c           jmp	$+0x10
1b53           inc	r11
8f11           sxt	r15
0f12           push	r15
0312           push	#0x0
b012 6424      call	#0x2464
2152           add	#0x4, sp
6f4b           mov.b	@r11, r15
4f93           tst.b	r15
f623           jnz	$-0x12
3012 0a00      push	#0xa
0312           push	#0x0
b012 6424      call	#0x2464
2152           add	#0x4, sp
3012 1f00      push	#0x1f
3f40 dcff      mov	#0xffdc, r15
0f54           add	r4, r15
0f12           push	r15
2312           push	#0x2
b012 6424      call	#0x2464
3150 0600      add	#0x6, sp
b490 9357 dcff cmp	#0x5793, -0x24(r4)
0520           jnz	$+0xc
3012 7f00      push	#0x7f
b012 6424      call	#0x2464
2153           incd	sp
3150 2000      add	#0x20, sp
3441           pop	r4
3b41           pop	r11
3041           ret
1e41 0200      mov	0x2(sp), r14
0212           push	sr
0f4e           mov	r14, r15
8f10           swpb	r15
024f           mov	r15, sr
32d0 0080      bis	#0x8000, sr
b012 1000      call	#0x10
3241           pop	sr
3041           ret
```

On remarque une instruction compare qui est très intéressante, elle compare la valeur stocké dans le registre r4 à l'adresse 24.
Il y a quoi à l'adresse r4? Sans savoir cela, on sait qu'après la comparaison, il y a un test qui nous permet de sauter ou non l'instruction si la comparaison est réussie... Et si on essayait de louper ce test?

Et ba le programme termine après...

Et si on le réussie? On récupère la ligne 
```Dissassembly
b490 9357 dcff cmp	#0x5793, -0x24(r4)
````
On compare la valeur 5793 avec ce qui est stocké dans r4 (peut être notre mot de passe), pour vérifier cela on va rentrer la valeur 9357 (MP430 Promuiscuité oninverse les octets entre eux).


