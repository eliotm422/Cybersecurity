
# Schéma 

![[Pasted image 20241210100011.png]]

# OSPF sur ISP1 2 3 4 5


Ø  Configurer le protocole OSPF entre ISP1, ISP2 et ISP3 et entre ISP4 et ISP5 d’autre part

Ø  Ne pas annoncer les réseaux d’interconnexion avec les routeurs Customer (routeurs C1, C2, C3, C4) ni le réseau entre ISP2 et ISP4 : 8.8.7.0/24

Clique droit sur la machine -> custom console -> solar gns3

````bash
### Config ISP1 ###
ISP1# config terminal
ISP1# router ospf 1
	router-id 1.1.1.1 
	network 8.8.8.0 0.0.0.255 area 0
	network 8.8.10.0 0.0.0.255 area 0
exit
write memory

### Config ISP2 ###
ISP2# config terminal
ISP2# router ospf 1
	router-id 2.2.2.2
	network 8.8.8.0 0.0.0.255 area 0
	network 8.8.9.0 0.0.0.255 area 0
	network 8.8.7.0 0.0.0.255 area 0
write memory

### Config ISP3 ###
ISP3# config terminal
ISP3# router ospf 1
	router-id 3.3.3.3 
	network 8.8.9.0 0.0.0.255 area 0
	network 8.8.11.0 0.0.0.255 area 0
write memory

### Config ISP4 ###
ISP4# config terminal
ISP4# router ospf 1
	router-id 4.4.4.4
	network 8.8.7.0 0.0.0.255 area 0
	network 8.8.5.0 0.0.0.255 area 0
	network 8.8.3.0 0.0.0.255 area 0
write memory

### Config ISP5 ###
ISP5# config terminal
ISP5# router ospf 1
	router-id 5.5.5.5
	network 8.8.5.0 0.0.0.255 area 0
	network 8.8.6.0 0.0.0.255 area 0
write memory

# Check 
show ip ospf neighbor

# Route 
show ip route ospf

# Afficher process-id
show ip ospf

# Supprimer
no router ospf <process-id>
no router ospf 1

# ISP1
# Afficher les routes
show running-config
conf t
router ospf 1
	no network 8.8.10.0 0.0.0.255 area 0

# ISP2
# Afficher les routes
show running-config
conf t
router ospf 1
	no network 8.8.7.0 0.0.0.255 area 0

# ISP3
# Afficher les routes
show running-config
conf t
router ospf 1
	no network 8.8.11.0 0.0.0.255 area 0

# ISP4
# Afficher les routes
show running-config
conf t
router ospf 1
	no network 8.8.3.0 0.0.0.255 area 0

# ISP5
# Afficher les routes
show running-config
conf t
router ospf 1
	no network 8.8.6.0 0.0.0.255 area 0
````



# Configuration BGP :

Ø  Configurer iBGP entre ISP4 et ISP5 et entre ISP1, 2 et 3 (full mesh BGP)

Ø  Configurer eBGP entre ISP4 et ISP2 (ne pas utiliser les loopback)

Ø  Configurer la fonction BGP Next Hop Self sur ISP 2 et ISP4

## Ø  Configurer iBGP entre ISP4 et ISP5 et entre ISP1, 2 et 3 (full mesh BGP)

### Configurer iBGP entre ISP4 et ISP5

IBGP : internal BGP, même numéro de routeur pour les différentes  addresses

```bash
### Routeur ISP4 ###
conf t
router bgp 65001
 bgp log-neighbor-changes
 # Passserelle du ISP5 et même AS que le routeur BGP
 neighbor 8.8.5.2 remote-as 65001
!
exit
write memory

### Routeur ISP5 ###
router bgp 65001
 bgp log-neighbor-changes
 neighbor 8.8.5.1 remote-as 65001
!
exit
write memory
```


### Configurer iBGP entre SP1, 2 et 3 

```bash
### Routeur ISP1 ###
conf t
router bgp 65002
 bgp log-neighbor-changes
 neighbor 8.8.0.1 remote-as 65002
 neighbor 8.8.9.2 remote-as 65002 
!
exit
write memory

### Routeur ISP2 ###
router bgp 65002
 bgp log-neighbor-changes
 neighbor 8.8.0.2 remote-as 65002
 neighbor 8.8.9.2 remote-as 65002
!
exit
write memory

### Routeur ISP3 ###
router bgp 65002
 bgp log-neighbor-changes
 neighbor 8.8.9.1 remote-as 65002
 neighbor 8.8.0.1 remote-as 65002
!
exit
write memory

# Afficher
show ip bgp summary
show ip route ospf
```


## Ø  Configurer eBGP entre ISP4 et ISP2 (ne pas utiliser les loopback)

``` bash
### Routeur ISP4 ###
conf t
router bgp 65001
 bgp log-neighbor-changes
 neighbor 8.8.7.2 remote-as 65002
!
exit
write memory


### Routeur ISP2 ###
router bgp 65002
 bgp log-neighbor-changes
 neighbor 8.8.7.1 remote-as 65001
!
exit
write memory
```

## Ø  Configurer la fonction BGP Next Hop Self sur ISP 2 et ISP4*

idée : uniquer l'ip des autres routeurs qu'on est soi même le routeur qui transite les paquets

``` bash
### Routeur ISP2 ###
enable
configure terminal
hostname ISP2
router bgp 65002
 neighbor 8.8.0.2 next-hop-self
 neighbor 8.8.9.2 next-hop-self
!
exit
write memory

```



``` bash
### Routeur ISP4 ###
enable
configure terminal
hostname ISP4
router bgp 65001
 neighbor 8.8.5.2 next-hop-self
!
exit
write memory

```


# Configuration du réseau Client

·        Configurer une route par défaut sur tous les routeurs C

·        Configurer une architecture DMVPN PHASE 2 full mesh avec C1 en HUB. Utiliser GRE : Utiliser le réseau 192.168.1.0/24 pour les tunnels

·        Configurer le protocole EIGRP sur les routeurs Customer pour annoncer les différents réseaux LAN dans l'infrastructure DMVPN

##  Configurer une route par défaut sur tous les routeurs C

``` bash
# POUR C1, route vers le prochain saut
ip route 0.0.0.0 0.0.0.0 8.8.3.1

# POUR C2 
ip route 0.0.0.0 0.0.0.0 8.8.6.1

# POUR C3
ip route 0.0.0.0 0.0.0.0 8.8.10.1

# POUR C4
ip route 0.0.0.0 0.0.0.0 8.8.11.1
```

## Configurer une architecture DMVPN PHASE 2 full mesh avec C1 en HUB. Utiliser GRE : Utiliser le réseau 192.168.1.0/24 pour les tunnels

### Phase 1
HUB :

``` bash
# Sur C1
interface Tunnel 0
ip address 192.168.1.1 255.255.255.0
tunnel mode gre multipoint
tunnel source FastEthernet0/0 
ip nhrp authentication DMVPN
ip nhrp map multicast dynamic
ip nhrp network-id 1
```

* ***Interface Tunnel 0** : Crée une interface tunnel logique sur le routeur C1. Cette interface est utilisée pour établir un tunnel GRE avec les autres routeurs, comme le Spoke C2.
* ***ip address 192.168.1.1 255.255.255.0** : Attribue l'adresse IP **192.168.1.1** avec le masque de sous-réseau **255.255.255.0** à l'interface Tunnel 0. Cette adresse est utilisée pour identifier le tunnel dans le réseau **DMVPN**.
* ***tunnel mode gre multipoint** : Configure le tunnel en mode **GRE multipoint**. Cela permet à plusieurs routeurs de se connecter via ce tunnel (c'est-à-dire qu'il peut s'agir d'un réseau **full-mesh**), avec le routeur HUB (C1) pouvant établir des connexions avec tous les SPOKES (C2, C3, etc.).
*  **tunnel source FastEthernet0/0** : Définit l'interface physique utilisée pour le tunnel GRE. Ici, c'est l'interface **FastEthernet0/0** qui sera utilisée comme source du tunnel pour atteindre le Spoke (C2).
* **ip nhrp authentication DMVPN** : Active l'authentification pour le protocole **NHRP** (Next Hop Resolution Protocol) et définit un mot de passe pour l'authentification des voisins **NHRP**. Dans ce cas, le mot de passe est **DMVPN**. Cela sécurise la communication entre les routeurs via DMVPN.
* **ip nhrp map multicast dynamic** : Permet la **résolution dynamique des adresses multicast**. Cela permet aux SPOKES d'envoyer des messages multicast via le HUB, ce qui est essentiel pour le protocole de routage dynamique comme **EIGRP**.
* **ip nhrp network-id 1** : Déclare l'identifiant du réseau **NHRP**. Tous les routeurs DMVPN doivent utiliser le même `network-id` pour s'identifier dans le même réseau **NHRP**. Ici, l'ID est **1**.


Spoke : 

``` bash
# Sur C2
conf t
interface Tunnel 0
ip address 192.168.1.2 255.255.255.0
ip nhrp authentication DMVPN
ip nhrp map 192.168.1.1 8.8.3.1
ip nhrp map multicast 192.168.1.1
ip nhrp network-id 1
ip nhrp authentication DMVPN
ip nhrp map multicast dynamic
tunnel source FastEthernet0/0 
tunnel destination 192.168.1.1


# Sur C3
conf t
interface Tunnel 0
ip address 192.168.1.3 255.255.255.0
ip nhrp authentication DMVPN
ip nhrp map 192.168.1.1 8.8.3.1
ip nhrp map multicast 192.168.1.1
ip nhrp network-id 1
ip nhrp authentication DMVPN
ip nhrp map multicast dynamic
tunnel source FastEthernet0/0 
tunnel destination 192.168.1.1

# Sur C4 
conf t
interface Tunnel 0
ip address 192.168.1.4 255.255.255.0
ip nhrp authentication DMVPN
ip nhrp map 192.168.1.1 8.8.3.1
ip nhrp map multicast 192.168.1.1
ip nhrp network-id 1
ip nhrp authentication DMVPN
ip nhrp map multicast dynamic
tunnel source FastEthernet0/0 
tunnel destination 192.168.1.1

```


* **interface Tunnel 0** : Crée l'interface tunnel sur le Spoke **C2**. Cette interface est utilisée pour se connecter au tunnel GRE configuré sur le **HUB** (C1).
* **ip address 192.168.1.2 255.255.255.0** : Attribue l'adresse IP **192.168.1.2** à l'interface Tunnel 0 sur le Spoke **C2**. Cela permet à ce Spoke de se connecter au réseau DMVPN et au HUB **C1** via cette adresse.
* **ip nhrp authentication DMVPN** : Active l'authentification NHRP et définit le mot de passe pour l'authentification **DMVPN** entre le Spoke et le HUB. Le mot de passe est **DMVPN** ici également.
* **ip nhrp map 192.168.1.1 8.8.3.1** : Cette ligne configure le mappage **NHRP** pour le **HUB (C1)**. Le Spoke (C2) associe l'adresse **192.168.1.1** (adresse du HUB dans le tunnel) à l'adresse IP **8.8.3.1** (adresse physique de la passerelle du HUB ou une autre adresse pertinente). Cela permet au Spoke de savoir comment résoudre l'adresse du HUB dans le tunnel.
* **ip nhrp map multicast 192.168.1.1** : Ce mappage permet au Spoke **C2** de résoudre l'adresse multicast **192.168.1.1** pour communiquer avec le HUB. C'est essentiel pour les protocoles comme **EIGRP** utilisant le multicast pour annoncer des routes.
* **ip nhrp network-id 1** : Configure le même **network-id** que celui du HUB (C1). Tous les routeurs dans le réseau DMVPN doivent avoir le même **NHRP network-id** pour qu'ils fassent partie du même réseau logique.
* **ip nhrp authentication DMVPN** : Répétition de l'authentification **NHRP** pour le Spoke, en utilisant le mot de passe **DMVPN**.
* **ip nhrp map multicast dynamic** : Permet au Spoke **C2** d'accepter des mappages **multicast** dynamiques pour l'acheminement du trafic multicast. Cela permet au Spoke de s'adapter aux changements dans le réseau DMVPN, notamment pour la gestion des sessions multicast.
* **tunnel source FastEthernet0/0** : Définit l'interface physique sur **C2** à utiliser comme source pour le tunnel GRE. Ici, l'interface est **FastEthernet0/0**.
* **tunnel destination 192.168.1.1** : Indique l'adresse IP de destination du tunnel GRE, c'est-à-dire l'adresse **192.168.1.1** de l'interface tunnel sur le **HUB (C1)**.
### Phase 2

HUB :

``` bash
# Sur C1
conf t
interface Tunnel 10
ip address 192.168.1.1 255.255.255.0
ip nhrp map multicast dynamic
ip nhrp authentication DMVPN
ip nhrp network-id 1
tunnel source FastEthernet0/0 
tunnel mode gre multipoint
end
```

SPOKE :

``` bash
# Sur C2
conf t
interface Tunnel 10
ip address 192.168.1.2 255.255.255.0
ip nhrp authentication DMVPN
ip nhrp map 192.168.1.1 8.8.3.1
ip nhrp map multicast 192.168.1.1
ip nhrp network-id 1
ip nhrp nhs 192.168.1.1
tunnel source FastEthernet0/0 
tunnel mode gre multipoint

# Sur C3
conf t
interface Tunnel 10
ip address 192.168.1.3 255.255.255.0
ip nhrp authentication DMVPN
ip nhrp map 192.168.1.1 8.8.3.1
ip nhrp map multicast 192.168.1.1
ip nhrp network-id 1
ip nhrp nhs 192.168.1.1
tunnel source FastEthernet0/0 
tunnel mode gre multipoint

# Sur C4 
conf t
interface Tunnel 10
ip address 192.168.1.4 255.255.255.0
ip nhrp authentication DMVPN
ip nhrp map 192.168.1.1 8.8.3.1
ip nhrp map multicast 192.168.1.1
ip nhrp network-id 1
ip nhrp nhs 192.168.1.1
tunnel source FastEthernet0/0 
tunnel mode gre multipoint

```

La diff : on met tunnel mode gre multipoint pour dire qu'on parle à tous

## Configurer le protocole EIGRP sur les routeurs Customer pour annoncer les différents réseaux LAN dans l'infrastructure DMVPN

conf t
no router eigrp 100 
HUB (C1) :

```bash
conf t
router eigrp 100
 no auto-summary
 network 192.168.1.0  
 network 10.1.1.0 0.0.0.255    
 exit

interface Tunnel 10
 ip nhrp authentication DMVPN
 ip nhrp map multicast dynamic
 ip nhrp network-id 1
 no ip split-horizon eigrp 100

```


C2 :

```bash
conf t
router eigrp 100
 no auto-summary
 network 192.168.1.0 0.0.0.255   
 network 10.1.2.0 0.0.0.255    
 exit

interface Tunnel 10
 ip nhrp authentication DMVPN
 ip nhrp map multicast 192.168.1.1   
 ip nhrp network-id 1
 ip nhrp shortcut                   
 tunnel source FastEthernet0/0
 tunnel destination 192.168.1.1
```

C3 :

```bash
conf t
router eigrp 100
 no auto-summary
 network 192.168.1.0 0.0.0.255   
 network 10.1.3.0 0.0.0.255    
 exit

interface Tunnel 10
 ip nhrp authentication DMVPN
 ip nhrp map multicast 192.168.1.1  
 ip nhrp network-id 1
 ip nhrp shortcut                    
 tunnel source FastEthernet0/0
 tunnel destination 192.168.1.1

```

C4 :

```bash
conf t
router eigrp 100
 no auto-summary
 network 192.168.1.0 0.0.0.255   
 network 10.1.4.0 0.0.0.255     
 exit

interface Tunnel 10
 ip nhrp authentication DMVPN
 ip nhrp map multicast 192.168.1.1  
 ip nhrp network-id 1
 ip nhrp shortcut                   
 tunnel source FastEthernet0/0
 tunnel destination 192.168.1.1

```



```bash
show ip eigrp neighbors
show ip route eigrp
```
# Sécurisation des échanges de données

·        Configurer IPSEC sur tous les routeurs C pour chiffrer les échanges de données au sein du tunnel (choisissez les paramètres Phase 1, Phase 2 que vous souhaitez)

·        Utiliser le mode transport

```bash
crypto isakmp

```
##  Configurer IPSEC sur tous les routeurs C pour chiffrer les échanges de données au sein du tunnel (choisissez les paramètres Phase 1, Phase 2 que vous souhaitez)


Sur les 4 routeurs : 

```bash
crypto isakmp policy 1
encryption aes
authentication pre-share
hash md5
group 5

crypto isakmp key 0 DMVPN_IPSEC address 0.0.0.0

crypto ipsec transform-set DMVPN_policy esp-aes esp-sha-hmac
mode transport
crypto ipsec profile IPSEC_DMVPN
set transform-set DMVPN_policy

int tunnel 0
tunnel protection ipsec profile IPSEC_DMVPN
```
## Utiliser le mode transport


```bash
```


# Configuration fortigate

## Webterm3

```bash
file:///etc/network/interfaces
auto eth0
iface eth0 inet static
	address 10.0.0.1
	netmask 255.255.255.0
	gateway 10.0.0.254
	up echi nameserver 10.0.0.1 > /etc/resolv.conf
```

## Webterm2

```bash
file:///etc/network/interfaces
nano /etc/network/interfaces
auto eth0
iface eth0 inet static
	address 10.2.0.1
	netmask 255.255.255.0
	gateway 10.2.0.254
	up echi nameserver 10.0.0.1 > /etc/resolv.conf
```

## Webterm1

```bash
file:///etc/network/interfaces
nano /etc/network/interfaces
auto eth0
iface eth0 inet static
	address 10.1.0.1
	netmask 255.255.255.0
	gateway 10.1.0.254
	up echi nameserver 10.0.0.1 > /etc/resolv.conf
```

## Fortigate 3 


```bash
config system interface
edit "port1"
set mode static
set ip 10.0.0.254 255.255.255.0
set allowaccess ping https ssh http fgfm
next
edit "port2"
set ip 8.8.0.1 255.255.255.0
set allowaccess ping https ssh http fgfm
next
edit "port3"
set ip 160.160.0.1 255.255.255.0
set allowaccess ping https ssh http fgfm
next
end
```

## Fortigate 2

```bash
config system interface
edit "port1"
set mode static
set ip 10.2.0.254 255.255.255.0
set allowaccess ping https ssh http fgfm
next
edit "port2"
set ip 8.8.2.1 255.255.255.0
set allowaccess ping https ssh http fgfm
next
edit "port3"
set ip 160.160.2.1 255.255.255.0
set allowaccess ping https ssh http fgfm
next
end
```

## Fortigate 1

```bash
config system interface
edit "port1"
set mode static
set ip 10.1.0.254 255.255.255.0
set allowaccess ping https ssh http fgfm
next
edit "port2"
set ip 8.8.1.0 255.255.255.0
set allowaccess ping https ssh http fgfm
next
edit "port3"
set ip 160.160.1.1 255.255.255.0
set allowaccess ping https ssh http fgfm
next
end
```


# VPN


* Aller sur SDWAN
* Create VPN sd-WAN member
* Remote IP adress
* Gateway 0.0.0.0
* 

```bash
```