
# Installation

* Installation : 
````bash
sudo apt install suricata

suricata --build-info

sudo suricata -c /etc/suricata/suricata.yaml -q 0
````

# Règle

--- 
Empêcher le scan de nmap :

```bash
alert tcp any any -> any any (msg:"Nmap Scan Detected"; flow:stateless; flags:S; threshold:type both, track by_src, count 20, seconds 3; sid:1000001; rev:1;)

alert tcp any any -> any any (msg:"Nmap Scan Detected"; flow:stateless; flags:S; threshold:type both, track by_src, count 20, seconds 3; sid:1000001; rev:1;)
```


Explication :

    alert tcp any any -> any any : Déclenche une alerte pour tout trafic TCP.

    msg:"Nmap Scan Detected" : Message associé à l’alerte.

    flow:stateless : Ne prend pas en compte l’état de la connexion (utile pour la détection de scan).

    flags:S : Détecte les paquets TCP SYN (souvent utilisés par Nmap).

    threshold:type both, track by_src, count 20, seconds 3 :

        Déclenche l’alerte si 20 paquets SYN sont envoyés en 3 secondes depuis une même source.

    sid:1000001 : Identifiant unique de la règle.

    rev:1 : Version de la règle.