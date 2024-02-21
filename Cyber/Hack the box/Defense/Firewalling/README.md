.Sup
[[Security Monitoring]]
eval sur table /20 + certif storm shield /20 
On va passer la certif CSNA QCM 70% de bonnes réponses
Stormshield : Français
(Stormshield data security : chiffrement en cloud ou local, coffre-fort sécurisé)
Stormshield endpoint pour les postes très secure
IPS IDS 
Rotation des disques durs sur les logs

Sur les différents boitiers : comprendre les diffs interfaces, de débit, de co simultanées

Rester sur des firmwares LTSB et certifié ANSSI !


Le serveur SMC permet de tout gérer, pratique pour l'administration

Pas d'antivirus Avancé : c'est bitdefender maintenant, optionnel
Extended Web Control, protocol industriel, inventaire d'app et détection de vul, ipsec VPN payant

Haute dispo : pas sur le 160 et 210 (reprise en cas de panne)

Penser à prendre le premium : Advanced Antivirus et Extended URL Filtering 

A prendre si nous avons pas de haute dispo :
Garanti standart : Si problème on l'envoie et il nous le renvoie
Garanti express : Ils envoient le boitier d'abord 


###################### MSP BOITIER ##################

On enregistre le boitier sur ke http://mystormshield
On retrouve tous nos produits au même endroit, on récupère une licence avec toutes les fonctionnalités
TOUJOURS AVOIR UNE MAINTENANCE
On peut restaurer stocker les logs par les ports USB, Port 1 : OUT, Port 2 : IN
L'IPS ne sera pas le même en IN et en OUT
Bridge :L'IP du boitier 10.0.0.254/8
DHCP : [10.0.0.10-10.0.0.100]/8

Regarder si on est en lecture sur l'interface D'admin, et pour l'accès aux logs.
On peut faire sur l'interface Graphique, et l'infterface console.
Pas besoin de cochre la case de l'ANSSI
Pour les NTP : on peut faire sur l'active Directory
Le port c'est l'https 443 et ssh 22 c'est modifiable
On peut autoriser des réseaux dans ACCESS To Firewall
Il y a les proxy et les dns 
Partition passive : partition de backup, partition active : partition actuelle
On peut envoyer les backups à stormshield, et restaurer la conf qu'on veut 
On utilisera logpoint, ou SLS pour que les produits STORMSHIELD 
ACTIVE UPDATE : MAJ Automatique sur les Firewalls

Proxy permet d'analyser les protocoles
Connexion : l'ensemble des co qui traversent le boitier 
VPN : Les logs VPN SSL/IPSec
Système : Admin/Evènements
Sécurité et usage : statistiques et alarmes 
PAS de trace en verbose 
Les protocoles IPSec envoient les paquets de données en toute sécurité.


Le lab est en page 98

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

## Révisions 

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


636 ldap 

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

Phase 1

L'objectif principal de la phase 1 est la mise en place d'un canal chiffré sécurisé par l'intermédiaire duquel deux pairs peuvent négocier la phase 2. Lorsque la phase 1 se termine avec succès, les pairs passent rapidement aux négociations de phase 2. Si la phase 1 échoue, les périphériques ne peuvent entamer la phase 2.
extremité tunnel chiffrement et authentification,  durée de clef identiques pour monter un tunnel
Phase 2
extremité traffic
L'objectif des négociations de phase 2 est que les deux pairs s'accordent sur un ensemble de paramètres qui définissent le type de trafic pouvant passer par le VPN et sur la manière de chiffrer et d'authentifier le trafic. Cet accord s'appelle une association de sécurité.