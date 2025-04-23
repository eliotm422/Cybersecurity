![[Pasted image 20240605000602.png]]PAGE 28
![[Pasted image 20240605000042.png]]

![[Pasted image 20240605000056.png]]

![[Pasted image 20240605000104.png]]


# Brouillon 

Usurpation : 3 types :
- Usurpation d'adresse IP du parefeu
- Usurpation d'un réseau connu
- Interface interne mal configurée


* Stormshield : Français 
* (Stormshield data security : chiffrement en cloud ou local, coffre-fort sécurisé) 
* Stormshield endpoint pour les postes très secure 
* Rotation des disques durs sur les logs 
* Sur les différents boitiers : comprendre les diffs interfaces, de débit, de co simultanées 
* Rester sur des firmwares LTSB et certifié ANSSI ! 
* Le serveur SMC permet de tout gérer, pratique pour l'administration 
* Pas d'antivirus Avancé : c'est bitdefender maintenant, optionnel Extended Web 
* Control, protocol industriel, inventaire d'app et détection de vul, ipsec VPN payant 
 * Haute dispo : pas sur le 160 et 210 (reprise en cas de panne) 
* Penser à prendre le premium : Advanced Antivirus et Extended URL Filtering 
* A prendre si nous avons pas de haute dispo : Garanti standart : Si problème on l'envoie et il nous le renvoie Garanti express : Ils envoient le boitier d'abord

FQDN : pas de groupe, résolution DNS 
Portail actif :  https://@ip_firewall|nom_firewall)/auth
 durée max : 4 heures
 marche que si c'est dans la base embarquée la modification du mot, ne peut pas écrire sur l'AD
on peut prendre un groupe
On peut donner des différents droits d'accès aux admins
admin peut modifier les mdp de tous
mais les administrateurs ne peuvent pas modifier les mdp entre eux, mais les utilisateurs



On passe SNS • CSNA (Certified Stormshield Network Administrator)

Label LTSB 12 mois, avec maj

(Stormshield data security : chiffrement en cloud ou local, coffre-fort sécurisé)

Les firewalls sont ratachés au serveur SMC.

(Stormshield data security : chiffrement en cloud ou local, coffre-fort sécurisé

Stormshield endpoint pour les postes très secure Il fait IDS/IPS

NTP horloge

SLS : Solution de gestion de trace

Phase 1 : extremité tunnel chiffrement et authentification,  durée de clef identiques pour monter un tunnel
Phase 2 : extremité traffic

VTI : tunnel IPsec entre les interfaces du firewall qui permettent de faire du routage. Il les fait passer par une interface du Firewall 

Si il y a une ligne : pas de route de retour. Si deux lignes : une route de retour spécifiant l'interface 	

Charon service pour monter le tunnel

Choix de la base d'uRL EWC :
* On choisit qu'une seule base :
	* Embedded URL database (soit embarqué gratuite)
	* Extended Web Control (soit payante)

SNI : 
* Bloquage par le nom du certificat d'un site web : OBJECT/URL /Certficate Name(CN)

Port : 
ISAKMP : 500
ESP : 4500

636 ldaps 
389 ldap

PBA : Le routage par politique c'est le fait de pouvoir sortir sur internet par un deuxièle endroit 

advanced virus : bitdenfender 

EWC : Base de donnée Cloud, c'est stormshield ui paye des catégories d'URL
Pour faire une requete EWC applique les r^gles puis consulte le cache 
Passer et bloquer sans déchiffrer; on utilisera cela.

Le certificat du Firewall empêche d'accèder à certains sites.
le parefeu proège jusqu'à la couche 7 du modèlde OSI
l'IPS fait pleins de trucs; il détecte et il bloque; 
l'IDS détecte juste,
Le FW ne fait rien


## Règle de filtrage:

Filtrage implicite :
toutes les regles
Filtrage global :
Fitrage depuis sur le boitier SMC (celui qui gère tout)
Fitlrage local : 
Filtrage depuis le boitier actuel

Connection log :
Tous les logs de connexion 


## Révision

Types boitiers :
* SN... (SN 3 chiffres) (pour les petites entreprises, les agences et les filiales)
* SN...W : intègrent une carte WIFI pour assurer des connexions sans fil sécurisées
* SN...I : adapté aux environnements industriels
* SN510, SN-M-Series-720 et SN-M-Series-920 : Organisations moyennes
* SN.... grandes organisations et les datacenters

Il y a la technologie IPS.

## VPN IPSEC

trois familles :
PPTP clients nomades mais obselète
SSL : poru clients nomades port(TCP443), UDP(1194)
IPSEC : tunnels site à site ou clients nomades
+ GRE/GRETAP

Durée de connexion avec de régociation du tunnel : 14400secondes POUR ssl, 3600 secondes IPSEC

3 phases :
Phase 1
C'est les extrémités de tunnels :
L'objectif principal de la phase 1 est la mise en place d'un canal chiffré sécurisé par l'intermédiaire duquel deux pairs peuvent négocier la phase 2. Lorsque la phase 1 se termine avec succès, les pairs passent rapidement aux négociations de phase 2. Si la phase 1 échoue, les périphériques ne peuvent entamer la phase 2. c'est la négociation des IP publiques, c'est les extrémités de tunnels
extrémité tunnel chiffrement et authentification,  durée de clef identiques pour monter un tunnel
Phase 2
Extrémité Traffic :
L 'objectif des négociations de phase 2 est que les deux pairs s'accordent sur un ensemble de paramètres qui définissent le type de trafic pouvant passer par le VPN et sur la manière de chiffrer et d'authentifier le trafic. Cet accord s'appelle une association de sécurité
PSK : clé pré partagée
PKI : clé partagé par certificat
IKEv1 IKEv2 : pour chiffrer la clef de phase 2
La clef de phase 2 permet de chiffrer les communications.
ESP : 500
keep alive :Tous les ... secondes pour envoyer un ping, pour voir s'il est en vie.
port ISAKMP autorisé explicitement 
Charon : deamon IPSEC
SPI : En informatique, un pare-feu à états est un pare-feu qui garde en mémoire l'état de connexions réseau qui le traversent. Le fait de garder en souvenir les états de connexions précédents permet de mieux détecter et écarter les intrusions et assurer une meilleure sécurité
En IKEv2, si on fait des groupes, les SPI sont identiques et uniquement là
VTI :Routage via la VTI (Virtual Tunneling Interface) distante dont l'adresse IP
appartient au même réseau que la VTI locale. Les interfaces VTI permettent de
définir des routes passant par le tunnel IPsec. Elles agissent comme passerelles
réciproques l’une de l’autre. Elles sont comme des points d’entrée et de sortie du
tunnel. Ce mode de fonctionnement est prioritaire sur la correspondance de
politique. *C'est une virtual interface sur nos routeurs*.

## VPN SSL :

* Le nombre de co VPN dépend du modèle du boitier
Exemple : 192.168.100.0/24 -> 62
Serveur : 192.168.100.0|.1|.2|.3]/30
Client 1 : 192.168.100.4(réseau)|.5(serveur)|.6(client)|.7(broadcast)]/30

	* Conifg :
Interne : boitier
externe : ldap


IPS : on détecte et on bloque
	* IPS 00 : entrant
	* IPS 01 : sortant
IDS : on détecte
FW : On laisse passer

Filtrage URL web : fait par l'extended web control
Cas d’usages
• SN160(W) : Site distant connecté en VPN, sécurité unifiée pour petite structure. Le SN160W permet la création de deux réseaux Wifi distincts.
• SN210(W) : Site distant connecté en VPN, sécurité unifiée pour petite structure avec DMZ ou double accès WAN. 
• SN310 : Sécurité unifiée pour petites structures avec besoin de continuité (haute disponibilité) et de zones de sécurité. 

Pour le proxy ARP 
* Si deux services identiques passent par la même interface out, il faut créer une adresse ip publique out et un alias, par exemples 10.0.0.1 (out) et 10.0.0.2 (alias) du moment que les adresses sont libres. Ainsi les deux passeront par le port 25, mais pas sur la même adresse IP.
* On peut sinon utiliser le service proxy ARP, ainsi les deux services utilisent cette même adresse. Ainsi on fait l'association entre la MAC adresse de l'interface et l'@ IP publique   

# Pratique 



################# LAB CREER LE SERVEUR ##################################33

1 : 
Pour se connecter : https://10.0.0.254/admin : admin/admin

2: 
Jamais déco : admin : déoroulant : log out when idle : never

3 : 
Langue : configuration / general configuration language
Le temps : avec timezone europe/paris synchronize with your machine
Redémarrer : le petit serveur à côté du warning, ne reset pas le mdp
SSH : Système configuration / Firewall Administration : enable SSH Access password
Licence: Système/licence/advance/everyday automatic
MDP Admin : Système/administrator/administrator account
Stockage local log : LOG dans la barre de recherche, on change les pourcentages pour désactiver ou activer POP3 à 0% et network capture à 3%
BACKUP : backup dans la barre de recherche, systeme/maintenance/backup

################### LES OBJETS #####################################

Je suis sur le clone, ça sera ma machien A

Configuration/objects/network
add +
Firewall :
	ADD Fw_B /host 192.36.253.20
Réseau : 
	Lan_in_B /network 192.168.2.0/255.255.255.0

Port
TCP :
add / port : protocol : webmail TPC en port 808

Sur le A 2 :
host / pc_admin 192.168.x.2(x = 2) 
host / srv_web_priv 172.16.2.11
host / srv_ftp_priv 172.16.2.12	
host / srv_mail_priv 172.16.2.13

Pour le groupe : 
Add : group/ name : srv_priv
srv

supprimer : dns.google.1 et 2
créer host : gateway 192.23.253.1

Exporter CSV
à côté de add export, DL

Importer : DEUX nouveaux hosts
host,srv_ftp_pub,192.36.253.22,,static,,""
host,srv_mail_pub,192.36.253.23,,static,,""

new group : 
serv_pub : srv_ftp_pub srv_mail_pub
et serv : serv_priv serv_pub

#########################" CONFIG INTERFACES ############################"

Out:
Config / security/NAT : (10)PassAll
network /interface /out /general addr range ; dynamic/static bridge IPV4 : Fixed IP (static) 
192.36.253.20/24

In : 
idem mais en internal
192.168.2.254/24
CRASH
on redémarre SNS_EVA1 en admin et new pass
on relance le ficheir de conf, et on entre la lettre b
on réentre désormais sur le web avec https://192.168.2.254/admin


DMZ
OK en interne

NETWORK / ROUTING
STATIC ROUTES
Default Gateway : basic_route (host en 192.168.2.1)

##############################" Translation d'adresse #######################"""


NAT : translation d'adresse on a une adresse pub PAT : Translation de port on change les ports

Il faut une translation statique, cela permet de lier l'IP à la MAC.

Src network in dest ou des port any, firewall_out le range c'est epheremal_fw

Dans Filter NAT
1 : On désactive les route IP statiques

2 : On ajoute et on clique sur edit 

3 : Dans filter on clique sur la colonne NAT, en source : network_intrenals, en destination internet, en src port après translation : epheremal en cliquant sur le random, en ipsource c'est le firewall_out
Pas oublier que dans routing la route par défault c'est le routeur en .1
OK et cache proxy aussi


BITMAP : correspondre ftp priv à ftp pub
On créé deux hosts en 192.36.253.12 13 11(web)poru les serv pub mail.
nat : crée bit map, en source ftp priv et en dest ftp pub et arp connexion
depuis l'autre PC : 
telnet 192.36.253.12 21
telnet 192.36.253.13 25
http://192.36.253.11
OK


Ajoutez une règle de NAT afin que les machines de votre réseau interne puissent accéder à vos
serveurs en DMZ sans que leur adresse IP privée n’y soit vue.
On créé une règle NAT : network_internal, any interface dmz1, traffic translation : source : fIrewall_dmz

source : interface :  interface out,  dest srv_mail_pub/priv, port http

####################### Menu filtrage #############################"
action : decrypt : pour déchiffrer

Action : 
pour voir les logs de filtrage il faut mettre le mode verbose

PBA : Le routage par politique c'est le fait de pouvoir sortir sur internet par un deuxièle endroit 

0 : 
supprimer la règle annynynyn dans security policy filter NAT

1 :
réseau interne 192.168.1.0 doit accéder au serveur de dmz :
group port
	port_interne : dns,http,frp,smtz
network group :
	srv_priv_a : 172.16.1.10 .11 .12 .13 .14

on crée une nouvelle règle en pass
source : Network IN , 
dest : Serv_priv_a
Dest port : dns,http,frp,smtz

2 :
Votre réseau interne, doit pouvoir naviguer sur les sites web d'Internet en HTTP
et HTTPS, sauf sur les sites de la République de Corée (test avec
www.visitkorea.or.kr).

Première règle qui block : interne : network_in, dest : internet avec corée du sud, dest port gttp_group

pass, network_in, internet, http_group

3 : 
Bloquer CNN : aller sur object et FQDN, ping cnn, on a l'adresse ip en 151.101.3.1, on rajoute cnn et son ip, et fait un rgèle de blocage en prennant en dest CNN 

4 :
Votre réseau interne doit pouvoir joindre les serveurs FTP d’IŶterŶet

pass, network_in, internet, ftp
telnet ftp.adobe.com 21
OK mais le serveur est down

5 :
bloquer adresse 192.168.1.200 pour faire des requetes ftp
on crée pc_200
bloque pc_200 internet ftp

6 :
votre réseau ping doit emettre un ping vers n'importe qui
action pass, source network_in, dest any, port porcole : protocole type : ip protocol : icmp

7 : 
Votre réseau interne doit pouvoir se connecter en SSH aux firewalls des autres
sites
pass network_in any https

8 : 
Seul votre serveur DNS interne (172.16.y.10) peut envoyer des requêtes DNS
vers l'extérieur.
pass route_gateway internet srv_dns_priv_a dns

9 : 
Votre serveur de messagerie peut envoyer des mails vers Ŷ’iŵporte quel
serveur de mail externe.
pass srv_mail_priv_a internet smtp 

pour tester : 
stmp coo ok

10 :
Les réseaux externes peuvent joindre vos serveurs Web et FTP ; ces
événements doivent être tracés.

action pass log level : advanced (connection log and filter, internet, srv_web_priv_a srv_ftp_priv_a http/ftp

11 :
Les serveurs mail externes sont autorisés à transmettre des e-mails à votre
serveur de messagerie.
pass internet  srv_mail_priv_a smtp 

12 :
Les réseaux externes sont autorisés à pinger l'interface « out » de votre
firewall; ce type d’évéŶeŵeŶt doit lever une alarme mineure.
pass minor alrme source internet firewall_out port ip_ICMP

13 : 
Les réseaux externes peuvent se connecter à votre firewall : via l’iŶterface web et
en SSH. Ce type d’évéŶeŵeŶt doit lever une alarme majeure.
pass alarme, internet, srv_web_pub_a, ssh

14 :
OK 

######################### Proxy #############
advanced virus : bitdenfender 
EWC : Base de donnée Cloud, c'est stormshield ui paye des catégories d'URL
Pour faire une requete EWC applique les r^gles puis consulte le cache 
Passer et bloquer sans déchiffrer; on utilisera cela.
Le certificat du Firewall empêche d'accèder à certains sites.
le parefeu proège jusqu'à la couche 7 du modèlde OSI
l'IPS fait pleins de trucs; il détecte et il bloque; 
l'IDS détecte juste,
Le FW ne fait rien

1 :1. Sélectionnez la base d’URL embarquée.
objects url database

2 :Trouvez les catégories dans lesquelles sont classées les URL twitter.com,
www.netbsd.org, www.mozilla.org, neverssl.com.
online, it, it, rien

3 : Configurez une politique de filtrage URL, et une politique de filtrage SSL,
permettant l'accès à tous les sites Web sauf les sites listés au point 2, les sites
des catégories « shopping » et « news ». Cependant, assurez-vous que le site
bbc.com reste joignable.
URL filtrering deux règles, news shopping

On va dans object url, dans url c'est les http, et dans certificat name c'est les https.
On fait nos groupes. lES http ils sont dans url filtering, dans ssl filtering c'est les https. on va dans filter nat et on rajoute une ssl route

1 : on créé un objet CNI
2 : On applique un filtrage URL : HTTP / SSL : HTTPS
3 : Filtrage : S : Reseau IN D : Internet P : HTTP I : IPS + Filtrage URL
	       S : Reseau IN D : Internet P : HTTPS I : IPS + Filtrage SSL

####################### Utilsiateur et authentification "########################

Portail captif : Il nous authentifie
LDAP S 836

Lancez l’assistaŶt LDAP et créez une base LDAP interne :
▪ Le nom d’orgaŶisatioŶ est x, et le domaine est « net ».
▪ Activez le profil d’autheŶtificatioŶ 0 (internal) sur l’iŶterface « IN »,
ainsi que l'enrôlement des utilisateurs.
▪ Testez l’accğs au portail captif : https://192.168.x.254/auth

On va dans user directories configuration
Connect to Internal Active directory
x
net
puis on coche le premier
https://192.168.1.254/auth OK

users / users and group
new user : 
jsmith
password
jsmith@x.net


créer peter wood avec mdp password avec enrolement
Users/authentification/captive protal/user enrollement/allow web enreollment for users
Sur la page d'auth : new user


4 : OK

5 : 
Modifiez la politique de filtrage pour que l'envoi de pings depuis votre
réseau interne ne soit autorisé Ƌu’à John Smith. Cette règle devra
systématiquement lever une alarme mineure.

Regle : 
new regle
pass alarm minor source network_in avec jhon smith dest int et ipc6 icmp

6 :  Adaptez la politique de filtrage afin que tous les utilisateurs non
authentifiés soient redirigés vers le portail captif lorsqu'ils tentent
d'accéder à des sites WEB en HTTP, sauf les sites présents dans la catégorie
« it » 

authentification_rule
: source : Network_Internals  

7 :
test

8 :
system administrators add a administrator
john smith

7 : 


################################### VPN IPSEC ####################################
Phase 1

L'objectif principal de la phase 1 est la mise en place d'un canal chiffré sécurisé par l'intermédiaire duquel deux pairs peuvent négocier la phase 2. Lorsque la phase 1 se termine avec succès, les pairs passent rapidement aux négociations de phase 2. Si la phase 1 échoue, les périphériques ne peuvent entamer la phase 2.
extremité tunnel chiffrement et authentification,  durée de clef identiques pour monter un tunnel
Phase 2
extremité traffic
L'objectif des négociations de phase 2 est que les deux pairs s'accordent sur un ensemble de paramètres qui définissent le type de trafic pouvant passer par le VPN et sur la manière de chiffrer et d'authentifier le trafic. Cet accord s'appelle une association de sécurité.


VTI : tunnel IPsec entre les interfaces du firewall qui permettent de faire du routage. Il les fait passer par une interface du Firewall 

1. Ajoutez une règle de filtrage Pass any any any en tête de cette politique.

Ajouter une règle any any nay

2. Configurez un tunnel IPsec avec une authentification par PSK pour relier votre
réseau interne « 192.168.x.0/24 » à celui de l’autre entreprise en utilisant les
profils de chiffrement par défaut (StrongEncryption).
GO to VPN / IPsec VPN 
Créer le tunnel : En local ressource : Network IN, en peer selection : Fw_B Site_Fw_B IKEv2, Net_In_B
Clef PSK : adminadmin
OK
keep_alive : 30
On fait la même l'autre côté

3. Générez du trafic correspondant aux extrémités de trafic et suivez les étapes de
négociation des tunnels et l'activité dans les tunnels depuis les journaux et le
menu de supervision correspondants.
filtrage : source Network_in LAN_in8B any
LAN_in_B Network_in any


4. Modifiez vos politiques IPSec pour relier cette fois vos deux réseaux Internes (IN
+ DM)) aux réseaux internes ;IN + DM)) de l’autre entreprise.
▪ Activez la fonction keep-alive sur votre tunnel.
▪ Regardez le nombre de tunnels négociés dans la supervision.
Filter NAT : Graphical_client : 
Network_in LAN_IN_B
LAN_in_B Network_ins
IPsec VPN :
Network_internals Site_F_B LAN_in_B
OK On fait des groups des deux côtées

5. Après avoir vérifié que vos tunnels sont fonctionnels, désactivez la règle de
filtrage Pass any any any et ajoutez les règles autorisant les réseaux du site
distant à joindre à pinger vos réseaux locaux et à joindre vos serveurs FTP et
WEB.
OK

6. Créez les profils de chiffrement suivants :
▪ IKE Phase 1 : Diffie-Hellman (DH15 MODP), Durée de vie
ŵaxiŵuŵ ;ϮϭϲϬϬs), algorithŵe d’authentification ;shaϮ_ϱϭϮ) et
algorithme de chiffrement (AES 256bits).
▪ IPSEC Phase 2 : PFS (DH15 MODP), durée de vie (3600s),
algorithŵe d’authentification ;hŵac_shaϱϭϮ) et algorithŵe de
chiffrement (AES 256bits).


7. Appliquez vos nouveaux profils de chiffrement sur votre VPN. Puis vérifiez que
tout fonctionne correctement.
8. Réalisez l’interconnexion de ces ŵêŵes réseaux, ŵais en configurant des tunnels
basés sur des VTI. Avec au choix du routage statique ou par politique (PBR).


############################## Filtrage et NAT #############################
Cela permet de sortir sur l'exterieur avec le tunnel VPN, et de filtrer.
11 81 14
443


1. Le client OpenVPN est installé sur la VM graphique fournie par Stormshield.
Configurez le firewall pour permettre aux utilisateurs qui se connecteront
depuis le réseau externe d’accéder à vos réseaux internes IN et DMZ :
• Les réseaux distribués aux utilisateurs VPN SSL seront :
• Pour TCP : Net-SSLVPN_TCP 172.31.x.0/24
• Pour UDP : Net-SSLVPN_UDP 172.30.x.0/24
• Le serveur DNS annoncé au client correspond à la machine srv-dns.
OK

VPN SSL VPN 
ON
192.36.253.10
NETwork_Internal
Net-SSLVPN_UDP
Net-SSLVPN-TCP
126

USERS / Authentification / Captive Portal / Interface ; out / External

2. Donnez le droit VPN SSL à l'utilisateur John Smith.
Configuration / Utilisateurs / Access privileges
detailled access


3. Pour le filtrage :
• Autorisez votre réseau à accéder aux firewalls de vos voisins sur les
ports SSLVPN et UDPVPN pour tous les utilisateurs (authentifiés et non
authentifiés).
• Autorisez aux réseaux Net-SSLVPN_TCP et Net-SSLVPN_UDP l’accès aux
réseaux internes.
4. Récupérez le fichier « Profil VPN SSL pour clients mobiles OpenVPN
Connect (fichier unique .ovpn) » via le portal captif sur l’adresse IP publique de
l’autre entreprise, il est téléchargé par défaut dans /home/user/Downloads,
ouvrez un terminal puis tapez les commandes suivantes :
su –
#Mot de passe root par défaut : toor
cd /home/user/Downloads
openvpn openvpn_mobile_client.ovpn
Il est possible d'avoir une erreur d'ajout de route si la route poussée est déjà
présente. Cela n'empêche pas l'établissement du tunnel.
Dans un second terminal, consultez votre table de routage pour visualiser les
routes ajoutées sur le client, avec la commande ip route show.
5. Consultez la liste des utilisateurs authentifiés dans l'ASQ ainsi que les logs
relatifs au VPN SSL côté firewall.
6. Validez l’accès aux différents serveurs de la DMZ et par ping sur l’IP interne du
firewall sur le réseau LAN.
7. Enfin, fermez le tunnel via le premier terminal avec la combinaison de touches
[CTRL+C].
**