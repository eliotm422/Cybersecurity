
# Aaarg

Vous devez afficher le flag, quelque soit le moyen utilisé !

Solutions : 
```bash
xxd -C aaarg | tr -d '\n'
xxd  -C -seek 10 aaarg      
┌──(kali㉿kali)-[/mnt/hgfs/Partage kali]
└─$ xxd  -C -seek 10 aaarg | grep "F"              
0000200a: 0000 0000 0000 46e2 808d 43e2 808d 53e2  ......F...C...S.
# Afficher 10 lignes
┌──(kali㉿kali)-[/mnt/hgfs/Partage kali]
└─$ xxd  -C -seek 10 aaarg | grep "F" -A 10
0000200a: 0000 0000 0000 46e2 808d 43e2 808d 53e2  ......F...C...S.
0000201a: 808d 43e2 808d 7be2 808d 66e2 808d 39e2  ..C...{...f...9.
0000202a: 808d 61e2 808d 33e2 808d 38e2 808d 61e2  ..a...3...8...a.
0000203a: 808d 64e2 808d 61e2 808d 63e2 808d 65e2  ..d...a...c...e.
0000204a: 808d 39e2 808d 64e2 808d 64e2 808d 61e2  ..9...d...d...a.
0000205a: 808d 33e2 808d 61e2 808d 39e2 808d 61e2  ..3...a...9...a.
0000206a: 808d 65e2 808d 35e2 808d 33e2 808d 65e2  ..e...5...3...e.
0000207a: 808d 37e2 808d 61e2 808d 65e2 808d 63e2  ..7...a...e...c.
0000208a: 808d 31e2 808d 38e2 808d 30e2 808d 63e2  ..1...8...0...c.
0000209a: 808d 35e2 808d 61e2 808d 37e2 808d 33e2  ..5...a...7...3.
000020aa: 808d 64e2 808d 62e2 808d 62e2 808d 37e2  ..d...b...b...7.
```

##  Afficher 30 lignes et seulement la première occurence


```bash

┌──(kali㉿kali)-[/mnt/hgfs/Partage kali]
└─$ xxd  -C -seek 10 aaarg | grep "F" -A 20 -m 1
0000200a: 0000 0000 0000 46e2 808d 43e2 808d 53e2  ......F...C...S.
0000201a: 808d 43e2 808d 7be2 808d 66e2 808d 39e2  ..C...{...f...9.
0000202a: 808d 61e2 808d 33e2 808d 38e2 808d 61e2  ..a...3...8...a.
0000203a: 808d 64e2 808d 61e2 808d 63e2 808d 65e2  ..d...a...c...e.
0000204a: 808d 39e2 808d 64e2 808d 64e2 808d 61e2  ..9...d...d...a.
0000205a: 808d 33e2 808d 61e2 808d 39e2 808d 61e2  ..3...a...9...a.
0000206a: 808d 65e2 808d 35e2 808d 33e2 808d 65e2  ..e...5...3...e.
0000207a: 808d 37e2 808d 61e2 808d 65e2 808d 63e2  ..7...a...e...c.
0000208a: 808d 31e2 808d 38e2 808d 30e2 808d 63e2  ..1...8...0...c.
0000209a: 808d 35e2 808d 61e2 808d 37e2 808d 33e2  ..5...a...7...3.
000020aa: 808d 64e2 808d 62e2 808d 62e2 808d 37e2  ..d...b...b...7.
000020ba: 808d 63e2 808d 33e2 808d 36e2 808d 34e2  ..c...3...6...4.
000020ca: 808d 66e2 808d 65e2 808d 31e2 808d 33e2  ..f...e...1...3.
000020da: 808d 37e2 808d 66e2 808d 63e2 808d 36e2  ..7...f...c...6.
000020ea: 808d 37e2 808d 32e2 808d 31e2 808d 64e2  ..7...2...1...d.
000020fa: 808d 37e2 808d 39e2 808d 39e2 808d 37e2  ..7...9...9...7.
0000210a: 808d 63e2 808d 35e2 808d 34e2 808d 65e2  ..c...5...4...e.
0000211a: 808d 38e2 808d 64e2 808d 7d00 0000 011b  ..8...d...}.....

```

Enlever les . et afficher seulement à partir de .

## Récupérer uniquement ce qui nous intéresse

```bash
# awk dernière ligne, tr supprime le ".", et le tr -d `\n`supprime les sauts,
xxd -C -seek 10 aaarg | grep "F" -A 20 -m 1 | awk '{print $NF}' | tr -d '.' | tr -d '\n'
```t