
# Enumération de port 
On fait un énumération des pages possibles sur la page web 
![[dirb_rick.png]]

On va aller sur robots.txt

Wubbalubbadubdub
ça sera un mot de passe

Rien d'intéressant, ni dans l'inspecteur de la page web

# Scan de ports 

![[Pasted image 20240129100527.png]]

On va regarder les CVE
https://www.exploit-db.com/exploits/40136

On va l'installer; et le lancer sur le service.


# Enumeration de compte sur le SSH

On install rockyou.txt
et on configure un fichier vim user.txt
```bash
hydra -L users.txt -p rockyou.txt 10.10.234.143 ssh
```

Le serveur limite le nombre d'authentification, idem si on réduit le vitesse d'attaque on n'arrive pas à attaquer le service...

