
# Révisions 

- Certification CSNA (Certified Stormshield Network Administrator) :
    
    - Utilisation du firewall Stormshield et produits associés comme Stormshield Data Security et Stormshield Endpoint Security.
- Étapes de configuration du firewall Stormshield :
    
    - Enregistrement du produit.
    - Configuration système.
    - Maintenance incluant sauvegardes et mises à jour.
    - Accès aux fonctionnalités avancées en mode admin.
- Fonctionnalités de translation d'adresse :
    
    - NAT (Network Address Translation).
    - PAT (Port Address Translation).
    - Publication ARP pour associer adresses publiques et adresses MAC.
- Filtrage avancé :
    
    - Filtrage stateful.
    - Filtrage global avec serveur d'administration centralisé SMC.
    - Protection applicative incluant filtrage URL, SSL, règles SMTP + antispam.
- Authentification des utilisateurs :
    
    - Portails captifs.
    - Annuaire utilisateur LDAPS.
    - Méthodes d'authentification comme Kerberos.
- Configuration des VPN :
    
    - VPN SSL et IPSec avec tunnels et profils de chiffrement spécifiés.
    - Utilisation de VTI pour simplifier la gestion des tunnels.
- Gestion des logs, objets réseau et règles de filtrage :
    
    - Visualisation en temps réel des logs.
    - Configuration des objets réseau comme VLAN.
    - Priorisation des règles de filtrage.
### Stormshield Data Security et Endpoint

- **Stormshield Data Security** :
    - Chiffrement en cloud ou local.
    - Coffre-fort sécurisé.
- **Stormshield Endpoint** :
    - Protection avancée pour les postes très sécurisés, incluant IDS/IPS.
### Gestion et Configuration

- **Serveur SMC** :
    - Administration centralisée des firewalls.
    - Les firewalls sont rattachés au serveur SMC.

### Fonctionnalités Avancées

- **NTP Horloge** :
    - Synchronisation de l'horloge.
- **SLS** :
    - Solution de gestion de traces.
- **Advanced Virus** :
    - Bitdefender, optionnel.
- **Extended Web Control (EWC)** :
    - Base de données Cloud, catégories d'URL payantes.
    - Filtrage URL web.

### Portail Actif

- **Portail d'authentification** :
    - URL : `https://@ip_firewall|nom_firewall)/auth`.
    - Durée maximale : 4 heures (14400 secondes).
    - Fonctionne avec la base embarquée, ne peut pas écrire sur l'AD.
    - Groupes et droits d'accès :
        - Les administrateurs peuvent modifier les mots de passe de tous, sauf ceux des autres administrateurs.

### Certificats et Base d'URL

- **Choix de la base d'URL EWC** :
    - Soit la base embarquée gratuite.
    - Soit Extended Web Control payant.
- **SNI (Server Name Indication)** :
    - Blocage par le nom du certificat d'un site web.
- **Certificat du Firewall** :
    - Peut empêcher l'accès à certains sites.

### Interfaces et Routage

- **VTI (Virtual Tunneling Interface)** :
    - Tunnel IPsec entre les interfaces du firewall.
    - Permet le routage via les interfaces du Firewall.
- **PBA (Policy-Based Routing)** :
    - Routage par politique pour sortir par une autre interface.

### Protocoles et Ports

- **Ports VPN IPsec** :
    - ISAKMP : 500
    - ESP : 4500
- **Ports LDAP** :
    - LDAP : 389
    - LDAPS : 636

### IPS/IDS

- **IPS (Intrusion Prevention System)** :
    - Détection et blocage des intrusions.
- **IDS (Intrusion Detection System)** :
    - Détection des intrusions seulement.

### Filtrage

- **Règles de filtrage** :
    - Filtrage implicite : Toutes les règles.
    - Filtrage global : Depuis le boîtier SMC.
    - Filtrage local : Depuis le boîtier actuel.
- **Connection Log** :
    - Tous les logs de connexion.

### VPN IPsec et SSL

- **Types de VPN** :
    - PPTP (obsolète).
    - SSL (pour clients nomades) : Ports TCP 443, UDP 1194.
    - IPsec : Tunnels site à site ou clients nomades.
- **Durée de connexion et renégociation** :
    - SSL : 14400 secondes.
    - IPsec : 3600 secondes.

#### Phases du VPN IPsec

- **Phase 1** :
    - Mise en place d'un canal chiffré pour négocier la phase 2.
    - Négociation des IP publiques et des extrémités de tunnels.
- **Phase 2** :
    - Négociation des paramètres de trafic.
    - Utilisation de PSK (clé pré-partagée) ou PKI (clé par certificat).
    - Chiffrement des communications avec IKEv1 ou IKEv2.
- **Charon Service** :
    - Service pour monter le tunnel.
- **SPI (Stateful Packet Inspection)** :
    - Garde en mémoire l'état des connexions pour une meilleure sécurité.

### Cas d'Usage et Modèles de Boîtiers

- **Types de boîtiers** :
    - **SN...** : Pour petites entreprises, agences et filiales.
    - **SN...W** : Avec carte WIFI intégrée pour connexions sans fil sécurisées.
    - **SN...I** : Adapté aux environnements industriels.
    - **SN510, SN-M-Series-720, SN-M-Series-920** : Pour organisations moyennes.
    - **SN...** : Pour grandes organisations et datacenters.
- **Exemples de cas d’usage** :
    - **SN160(W)** : Site distant connecté en VPN, sécurité unifiée pour petite structure.
    - **SN210(W)** : Site distant connecté en VPN, sécurité unifiée pour petite structure avec DMZ ou double accès WAN.
    - **SN310** : Sécurité unifiée pour petites structures avec haute disponibilité et zones de sécurité.

### Proxy ARP

- **Utilisation du proxy ARP** :
    - Si deux services identiques passent par la même interface OUT, création d'une adresse IP publique OUT et un alias.
    - Service proxy ARP pour associer la MAC adresse de l'interface avec l'IP publique.

### Certification et Maintenance

- **Certification CSNA** :
    - Certified Stormshield Network Administrator.
- **Label LTSB** :
    - Maintenance 12 mois avec mises à jour.


### Présentation de Stormshield

**Stormshield Data Security** : Chiffrement des données (documents, mails).

**Stormshield Endpoint Security** : Solution EDR, adaptée principalement pour les serveurs critiques, non recommandée pour les PME.

**Stormshield Network Security** :

- **Firewall**
- **IPS (Intrusion Prevention System)** : Détecte et bloque les intrusions.
- **IDS (Intrusion Detection System)** : Détecte et informe l’IPS des intrusions.

### Configuration et Réseau

**Ports** :

- Port 1 : Sortie (Out)
- Port 2 : Entrée (In)
- Port 3 : DMZ

**Adresses** :

- Adresse Bridge : 10.0.0.254/8
- Adresse DHCP : 10.0.0.10 – 10.0.0.10/8

**Connexion au portail Stormshield** : [https://10.0.0.254/admin](https://10.0.0.254/admin)

**Configuration** :

- Utiliser des firmwares LTSB validés ANSII en production.
- Changement de fuseau horaire nécessite un redémarrage.
- Changer le mot de passe par défaut (admin/admin).

### Modules

**Backup** :

- Cloud backup disponible.
- Restauration de modules au choix.
- Synchronisation entre modules actifs et passifs.
- Possibilité de désactiver les mises à jour automatiques des modules actifs.

**Traces & Supervision** :

- Logs standards (connexions TCP/UDP) et avancés (connexions + logs réseaux).
- Logpoint : Logiciel SIEM.
- Pas de stockage de logs sans carte SD, visualisation en temps réel uniquement.
- Personnalisation et accès temporaire aux logs possible.
- Configuration de 4 serveurs syslog.
- Notifications/Alerte par mails via SLS (Stormshield Log Supervisor).

**Objets** :

- Objets = @IP, URL, événement.
- Exportation de la base de données en fichier CSV.
- NAT et PAT pour la configuration des règles de translation d’adresses.

### Sécurité Réseau

**Usurpation d'adresse IP** :

- Usurpation du Firewall Stormshield.
- Usurpation d'un réseau connu.
- Interface/machine interne mal configurée.

**VLAN (802.1q)** :

- Communication entre VLANs par routage.
- Publication ARP pour l'association d'une adresse publique et l'adresse MAC du Firewall.

**Protocole & Ports** :

- ISAKMP (UDP Port 500)
- HTTP: 80
- HTTPS: 443 (TCP)
- LDAP: 389
- LDAPS: 636
- UDP: 1194
- ESP: 500

### Filtrage et Contrôle Web

**Base de contrôle d'accès aux sites web** :

- Stormshield : 16 catégories.
- EWC (External Web Control) : 65 catégories.
- FQDN et SNI pour le filtrage HTTPS.
- Antivirus de base : ClamAV, avancé : Bitdefender.
- Portail captif pour la création et approbation des comptes utilisateurs.

### VPN

**Module VPN IPSec** :

- Configuration des tunnels VPN IPsec pour sécuriser les connexions entre sites.
- Durée de vie des phases : Phase 1 (21 600 sec), Phase 2 (3 600 sec).
- "Keep alive" pour maintenir le tunnel actif.
- Charon : Service de tunnel/VPN IPsec.
- VTI (Virtual Tunneling Interface) pour définir des routes via un seul tunnel IPSEC.

**Module VPN SSL** :

- Configuration des VPN SSL pour les connexions sécurisées des utilisateurs distants.
- Durée de vie : 14 400 secondes.
- Réseau VPN SSL (TCP ou UDP) avec sous-réseaux en /30.


# Quizz bouquin 

## Prises en main du firewall
Q1 - Quel est le mot de passe et le compte administrateur par défaut du SNS ?
A. Login : admin, password : admin

Q2 - Quelle est l’adresse IP par défaut du SNS ?
A. 10.0.0.254/8

Q3 - En configuration usine, il est possible (si le matériel le supporte) de se connecter au firewall
grâce :
A. A un câble série
B. Un écran utilisant une connexion HDMI ou VGA
D. Une connexion HTTPS
C. Une connexion SSH(FAUX)
## Traces et supervision

Q1 – Quelles sont les assertions vraies :
C. 4 serveurs syslog peuvent être configurés, ainsi que 4 serveurs de
secours.
FAUX
A. Les pare-feux SNS ne peuvent pas stocker de logs en local.
B. Il est possible de stocker les logs sur une clef USB connectée au firewall.
Q2 - Par défaut, les logs n’affichent pas les adresses IP de destination à cause de la
RGPD.
B. Faux
Q3 - Tous les administrateurs peuvent avoir accès aux informations personnelles
dans les log à partir du moment où ils ont un mot de passe temporaire d’accès.
A. Vrai
Q4 - Le protocole syslog est utilisable uniquement chiffré avec TLS sur les firewalls
Stormshield 
B. Faux

## Objets

Q1 – Quelles sont les assertions vraies :
A. L’objet dynamique récupère son IP automatiquement depuis les serveurs DNS : Vrai
B. Un objet hôte peut être dynamique ou statique. Vrai
C. Un objet FQDN est toujours résolu automatiquement. : Vrai
FAUX :
D. Grâce au DHCP, le pare-feu peut découvrir automatiquement les adresses IP des autres machines du réseau et créer les objets correspondants. 

Q2 – Quelles sont les assertions vraies :
A. Il est impossible de créer manuellement l’objet Firewall_A. : Vrai
B. Il est possible de créer un groupe d’objets FQDN. : Faux
C. L’objet Network_external est géré automatiquement par le pare-feu. : Faux
D. Il est possible d’exporter les objets sous forme d’un fichier CSV : Vrai
E. L’iŵport d’un fichier CSV remplace systématiquement toute la base d’objets. Il faut donc être vigilant et ne pas oublier d’objet dans le fichier au risque de casser la configuration. : Faux

## Configuration réseau

Q1 – Les objets routeurs peuvent être utilisés comme route par défaut :
A. Vrai

Q2 – Une route de retour est obligatoire pour joindre l’Internet :
B. Faux

Q3 – Un bridge contenant les interfaces dmz1 et dmz2 permet aux machines
connectées sur ces deux interfaces de communiquer directement sans filtrage ni
analyse.
B. Faux


## Translation d'adresses

Q1 – La translation d’adresse permet à plusieurs serveurs web d’être accessibles sur
la même adresse IP publique et le même port.
B. Faux
Q2 – La translation dynamique nécessite une réécriture de port source :
Vrai seulement s’il y a plusieurs machines émettant des connexions à translater
A. Vrai dans tous les cas
Q3 – Combien de politique de filtrage et NAT sont disponibles sur les pare-feux
Stormshield :
D. 10
Q4 – Si deux règles de translation ont les mêmes critères de sélection de trafic, c’est
la dernière dans la liste qui s’appliquera :
B. Faux
Q5 – Le protocole ARP permet de déterminer automatiquement la passerelle à
utiliser pour joindre une machine :
B. Faux
Q6 – La publication ARP permet au pare-feu de répondre aux requêtes ARP sur des
adresses IP ne lui appartenant pas (non configurée sur une interface) :
A. Vrai

## Filtrage 

Q1 – Pour autoriser un trafic TCP à passer au travers du pare-feu, il faut
impérativement créer une seconde règle pour autoriser les paquets réponses, sinon
le client ne recevra jamais les données demandées au serveur.
B. Faux
Q2 – Les règles de filtrage implicites peuvent toute être désactivées :
A. Vrai
Q3 – L’action « block » sur une règle de filtrage permet de rejeter une connexion et
d’inforŵer le client que ce trafic n’est pas autorisé :
B. Faux
Q4 – Dans quels cas est-il intéressant d’utiliser le niveau de trace avancé ?
B. Si je souhaite avoir des log du trafic ICMP et ESP.
C. Si je souhaite avoir des log des paquets bloqués.
FAUX
A. Tout le temps si je souhaite avoir des log des connexions traversant le
pare-feu.
Q5 – Il n’est pas possible d’utiliser une liste d’objets dans la destination d’une règle
de filtrage si on y insère un objet FQDN.
A. Vrai
Q6 – Le pare-feu Stormshield permet d’autoriser spécifiquement un message ICMP
avec son type et son code.
A. Vrai

## Protection applicative

Q1 – Les analyses pour le filtrage URL sont effectuées par le module IPS ASQ :
B. Faux
Q2 – La base d’URL extended web control ne peut pas être utilisée sur les petits
modèles de pare-feu car l’espace disque est insuffisant :
B. Faux
Q3 – La catégories personnalisées sont prioritaires sur les catégories intégrées dans
le pare-feu :
A. Seulement si la règle de filtrage est située avant.
FAUX :
B. Toujours.
C. Jamais, c’est l’inverse.
Q4 – Il n’est pas possible de filtrer les sites web utilisant HTTPS avec le proxy HTTP
(filtrage URL) :
A. Vrai
Q5 – Le SNI est un champ dans le handshake TLS/SSL qui contient l’URL demandée
par le client :
B. Faux
Q6 – Quel flux le proxy SSL peut-il déchiffrer et analyser (regarder ssl_srv dans ssl insepction wizard)?
B. HTTPS
D. FTPS
E. SMTPS
FAUX :
A. SSH
C. SFTP


## Utilisateurs et authentification

Q1 – Une des limites de l’annuaire interne au pare-feu est qu’il ne supporte pas les groupes d’utilisateurs :
B. Faux
Q2 – Il n’est pas possible de rediriger vers le portail captif les utilisateurs visant un site web en HTTPS :
C. Vrai, mais on peut utiliser le proxy SSL pour cela.
FAUX
A. Faux, la règle de redirection permet de le faire de base.
B. Vrai, c’est impossible car HTTPS est chiffré.
Q3 – Tous les administrateurs du pare-feu peuvent gérer les droits des autres
administrateurs :
B. Faux, c'est les admins
Q4 – La création d’un utilisateur par enrôlement nécessite obligatoirement une
action de la part d’un administrateur :
A. Faux

## VPN

Q1 – IPsec utilise TCP pour négocier la connexion, puisse envoie les données
chiffrées grâce à UDP :
B. Faux
Q2 – SHA1 est un algorithme de hachage sûr pour les tunnel VPN :
B. Faux
Q3 – Les VTI font partie du standard IKEv2 est ne sont pas disponibles sur IKEv1 :
B. Faux
Q4 – Un tunnel IPsec garantit :
A. L’authentification
C. L’intégrité
D. La confidentialité
E. L’anti-rejeu
faux /
B. La qualité de service
F. La réception
Q5 – L’option keepalive permet au pare-feu de détecter des coupures de connexion :
B. Faux
Q6 – La négociation d’un tunnel IPsec est initiée seulement s’il y a des données à
envoyer dans le tunnel :
A. Vrai
Q7 – Sans VTI, il est impossible de faire fonctionner deux tunnels entre les mêmes
réseaux simultanément (pour un besoin de redondance par exemple) :
A. Vrai
Q8 – Une route statique est nécessaire pour que le firewall puisse envoyer les paquets dans un tunnel IPsec :
B. Vrai seulement avec des VTI
FAUX :
C. Vrai seulement avec de la correspondance de politique (tunnel IPsec
standard)
D. Faux dans tous les cas
A. Vrai dans tous les cas

## VPN SSL

Q1 – Les utilisateurs s’authentifient avec des certificats uniques sur le VPN SSL :
B. Faux
Q2 – Le pare-feu peut gérer simultanément des connexions UDP et TCP au VPN SSL :
A. Vrai
Q3 – Le VPN SSL est une implémentation non standard, spécifique Stormshield :
B. Faux
Q4 – Les utilisateurs connectés en VPN SSL sont automatiquement authentifiés sans
devoir passer par le portail captif :
A. Vrai
Q5 – Pour qu’un utilisateur puisse se connecter en VPN SSL, je dois :
A. Autoriser l’accès au VPN pour cet utilisateur
B. Lui fournir l’adresse IP publique de mon firewall
C. Activer le portail captif sur l’interface externe
D. Avoir un annuaire lié à mon pare-feu
FAUX : 
E. Créer une règle de filtrage pour autoriser spécifiquement cet utilisateur à
se connecter

# QUIZZ blanc  :
1. L'administrateur peut configurer le firewall via
Console série
navigateur
ssh

2: La restauration d'une configuration :
* Peut s'effectuer depuis une sauvegarde automatique
* S'effectue grâce à l'import d'un fichier au format ".na"

3: En configuration usine, le port d'administration du firewall est :
* 443 (TCP)


4:  Il est possible de désactiver les mises à jours automatiques "Active Update" par module : 
* Vrai

5: La mise à jour système est possible : 
* Peu importe la partition

6: Un firewall en configuration usine :
* Bloque l'ensemble des flux sauf les pings et les ports d'administrations

7: Sur les appliances PHYSIQUES SNS, il est possible de :
* Copier la partition active a la passive
* Saubvegarder la configuration complète vers une  fichier na (ficheir chiffré)

8 :Le service NTP (Network Time Protocol)
* A besoin de connaitre  le fuseau horaire du firewall

9: Parmi les affirmations suivantes, sélectionnez celles qui sont correctes
ADE
*  Les connexions autorisées par le filtrage implicite ne seront pas soumises à la politique de NAT active
* Les règles implicites peuvent être désactivées 
* Les règles de filtrage et de NAT globales sont accessibles depuis l'interface d'administration du firewall



10 : Le nombre de règles de filtrage que peut gérer le firewall est
Illimité 

11 : Quelles inspections de sécurité peuvent être activées dans la politique de filtrage
*  Filtrage SMTP 
* Analyse antivirale
* Analyse antispam 
* Filtrage URL
*FAUX : antiphishing

12 : Par défaut, quand l'action "passer" est sélectionnée, quel(s) protocole(s) est (sont) gérés de manière stateful par le module de prévention d'intrusion Stormshield Network ?
aucune réponse
* aucun réponse
*Faux :
* L2TP
* ESP
* GRE
* PIM*

13 :  Les paquets ICMP de type "echo reply" peuvent être tracés dans les logs de filtrage avec le niveau de trace standard sur une règle de filtrage
* Faux

14 : Mon accès Internet est assuré par une connexion modem ADSL. J'ai paramétré cet accès dans mon firewall. Il me suffit alors d'activer la politique de filtrage no 1 0, telle qu'elle est définie dans la configuration d'usine, pour que mes machines internes puissent accéder à Internet :
* Faux

15: Les firewalls Stormshield Network sont capables de limiter la taille de chaque paquet ping (ICMP echo) arrivant sur un serveur
* Faux 

16: Les règles de filtrage sont traitées
* Par ordre d'apparition

17: En fonction de quel(s) critère(s) le firewall est capable de filtrer les flux ?
* BCDE
* De l'adresse IP destination
* Du port
* Du protocole
* De l'adresse IP source

* Faux C) Du numéro de session*

 18 : Il est possible de créer une liste de ports destination dans une seule et même règle de filtrage
* Vrai

19 : Dans une connexion FTP, le mode de traces avancé dans une règle de filtrage est-il nécessaire pour journaliser le trafic FTP ?
Non

20 :  Le niveau de traces d'une règle de filtrage est défini à standard, je tente d'établir une connexion sans succès, je peux visualiser les traces correspondantes dans le journal des connexions réseau
Oui

21 : Si je réserve le réseau 10.8.0.0/24 aux clients se connectant par le biais du VPN SSL, les adresses IP obtenues à la connexion du premier client sont
* 10.8.0.4 pour adresse réseau, .5 pour l'IP de l'interface du tunnel côté serveur, .6 pour l'IP du client, et .7 pour l'adresse de diffusion

22 : Par défaut, la durée de vie d'un tunnel VPN SSL est de
* 14400 secondes

23 :Chaque utilisateur se connectant via un tunnel VPN SSL est automatiquement authentifié au niveau du firewall
* Vrai

24 : Le droit d'accès VPN SSL est global à tous les utilisateurs
* Faux

25 : Dans quel(s) module(s) du firewall la plage VPN SSL attribuée aux clients mobiles peut-elle être utilisée ?
* Nat 
* Filtrage
FAUX Le VPN IPsec

26 : Mon entreprise possède un serveur smtp et un serveur http. Ils sont situés dans une DMZ en adressage privé. Le firewall Stormshield Network permet de rendre joignable simultanément ces 2 services depuis Internet bien que mon fournisseur d'accès ne m'ait attribué qu'une seule IP publique
* Vrai

27: Le mécanisme de translation permet de
* Cacher les adresses internes vis-à-vis de l'extérieur

FAUX 
Translater les adresses réseau sur un serveur sécurisé
Filtrer l'accès de certaines IP
Chiffrer les adresses IP

28 : Si j'utilise une adresse IP secondaire (alias) d'une interface (nommé Firewall_out_l) dans les règles de NAT, est-il nécessaire d'activer la publication ARP ?
* non

29 : L'opération de NAT qui modifie l'adresse IP et le port source
* Est uniquement configurable dans la politique de NAT
FAUX  
*Doit impérativement être définie dans le filtrage
Peut être définie dans une règle de filtrage et sera analysée en priorité sur les règles définies dans l'onglet NAT de la politique active
Modifie le port destination dans tous les cas

30 : Sélectionnez les critères d'application d'une règle de NAT parmi la liste suivante
ABC  
* Une plage de ports destination
* Une adresse réseau
* L'interface d'entrée 
* 
Faux 
* La passerelle de sortie
* Un groupe d'utilisateurs
* Le numéro de protocole


31 : Quel type de translation nécessite la modification de l'adresse source et du port source sur les paquets translatés
* Translation dynamique : Masquage
* FAUX
* Translation par port : PAT
* Translation statique : NAT

32: L'analyse antivirale peut s'appliquer à des flux
* SMTP
* HTTP
* HTTPS
* FAUX
* ICMP
* SSH


33 : Le filtrage par SNI (nom de certificat) permet de bloquer l'accès à des sites web. Il est utilisable sur les protocoles
* HTTPS
FAUX
* HTTP

34 : Dans le module "objets WEB", il est possible d'éditer les catégories d'URL de la base embarquée afin de lire leur contenu
* Faux

35: Breach Fighter peut analyser les fichiers transitant via le(s) protocole(s)
* HTTPS
Faux 
* FTP
* GRE
* ICMP

36 : Un flux HTTPS dépend de l'action "Passer sans déchiffrer". Le certificat présenté au le navigateur est celui du proxy SSL
* Faux

37 : Lorsque le filtrage URL se base sur le fournisseur "Extended Web Control", toutes les requêtes HTTP sont transmises à un des serveurs du Cloud pour obtenir la catégorisation du site visité
* Vrai si l'url n'est pas présente dans le cache local du proxy
*FAUX
*Vrai dans tous les cas
*Faux dans tous les cas


38 : Il est possible de visualiser les journaux (logs) ou une portion des journaux via
* L'interface d'administration du firewall
* wireshark

39 : La mise en œuvre du Règlement Général sur la Protection des Données (RGPD) restreint l'accès aux logs
A B
* Pour tous les administrateurs
* Depuis l'interface dadministration du firewall
*Faux :
Pour tous les administrateurs sauf le super administrateur admin

40 : Est-il possible de modifier le pourcentage d'espace disque réservé qu'occupe une famille de traces ?
* oui

41 : Par défaut, seul le super administrateur "admin" peut accéder aux logs complets en cliquant sur "Accès restreint aux logs"
* faux

42 : Un administrateur différent de "admin" peut accéder aux logs complets via un code d'accès
* Qu'un autre administrateur ayant des droits doit générer
* Temporaire
*FAUX
Qu'il peut générer lui-même
Non limité dans le temps

43 :  Les extrémités de trafic d'un tunnel IPsec représentent les machines/réseaux qui pourront communiquer au travers du tunnel
Vrai

44 : Les règles implicites générées lors de l'activation d'une politique IPsec permettent
D'autoriser le trafic au sein du tunnel
* La réception de paquets 4500/UDP
La négociation d'un tunnel nomade
* La négociation ISAKMP et la réception des paquets ESP dun tunnel site à site
*Faux 
D'autoriser le trafic au sein du tunnel
La négociation d'un tunnel nomade

45 : Quels types de VPN puis-je établir entre deux firewalls Stormshield Network ?
* VPN IPsec
*FAUX
VPN SSL
VPN pp-rp
OpenVPN
 
46 : Pour des tunnels négociés en IKEv1, les extrémités de trafic doivent être rigoureusement identiques sur les deux sites participant au tunnel IPsec pour que les tunnels puissent fonctionner
* Vrai

47 : Sélectionnez la configuration cryptographique offrant la meilleure sécurité
* DES de la merde; 
* SHa-1 aussi, choisir le plus de bit !

48 : Combien de phases sont nécessaires à l'établissement d'un tunnel VPN IPsec ?
* 2

49 : Lors de la création d'un VPN IPsec, si je paramètre une authentification par PSK, cela signifie
* Par clé partagé

50 : La clé ISAKMP négociée lors de la phase 1 d'un VPN IPsec permet
* De chiffrer les échanges recus lors de la phase 2
*FAUX 
De chiffrer le trafic à envoyer par le protocole ESP
De déchiffrer le trafic ESP reçu

 
51 :Une politique d'authentification peut se baser sur
* La machine source
* L'utilisateur ou le groupe
*FAUX
La machine destination
Le port destination


52 : L'accès au portail captif s'effectue via l'URL
* https://<adresse_lP_firewall>/auth

53 : Le portail d'authentification peut être accessible
* Depuis toutes les auth qu'on définit nous même

54 : Les objets routeurs
* Permettent de configurer une répartition de charge sur plusieurs passerelles
* Permettent de tester la disponibilité des passerelles
*Faux
Sont utililisés par les routes statiques
Ne peuvent avoir qu'une seule passerelle de secours

55 :  Les objets commençant par Network_ peuvent être modifiés dans la base d'objets par l'utilisateur
* Faux 

56 : Le nom d'un objet que je crée manuellement peut
* Commencer par un chiffre
* Être un nom de domaine 
*FAUX
Contenir un nombre illimité de caractères
Commencer par Network
Commencer par Firewall_

57 : L'objet Network_internals contient (2 bonnes réponses)
BF
* Les réseaux de toutes les interfaces protégées
* Les réseaux déclarés dans une route statique et joignables depuis une interface protégée
*FAUX
Les réseaux privés définis par l'IETF dans la RFC 1918
Les réseaux des interfaces "dmz"
Les réseaux de toutes les interfaces du firewall
(O Le réseau de l'interface "in"

58 : Si elle n'est pas utilisée, une route statique peut être désactivée depuis I'IHM
Vrai

59 : Parmi les affirmations suivantes, sélectionnez celles qui sont correctes
* La passerelle par défaut est la route la moins prioritaire
* Par défaut, le routage par politique est plus prioritaire que le routage statique en version 3 et 4 du firmware
* La route de retour est la plus prioritaire
*Faux 
Seul le routage par politique est plus prioritaire que le routage dynamique
La passerelle par défaut est la route la plus prioritaire

![[attachments.png]]


60 : Les modems de la configuration réseau peuvent être de type
* PPTP
* PPPoE
*FAUX
pppoA 
pp-rp 
HTTp 
L2TP

61 : Pour une meilleure sécurité, on placera les serveurs publics (mail, Web, FTP,etc...)
* Dans une zone DMZ

62 : Une interface peut disposer de deux adresses IP faisant partie du même réseau
* Vrai

63 : 172.30.0.1 est une adresse
* Privée
*FAUX     
Multicast
Publique


64 : Les routes statiques
* N'ont pas d'utilité sur les firewalls Stormshield Network
*FAUX
Permettent de faire du routage en fonction de l'adresse IP source

65 : La définition d'une route statique nécessite la configuration d'une interface de sortie
* Vrai

66 : Le firewall Stormshield Network peut jouer le rôle de serveur DHCP pour les machines du réseau local
* Vrai

67 : En utilisant un objet routeur dans le routage par défaut, est-il possible de bloquer (ne pas router) les paquets si aucune passerelle n'est disponible ?
* Vrai

68 : Nous souhaitons effectuer un routage par défaut avec une répartition de charge sur 3 passerelles. Une passerelle doit recevoir la moitié du trafic et les deux autres passerelles doivent se partager la moitié restante. Parmi les propositions suivantes, choisissez la (ou les) configuration(s) correctes) pour les poids des passerelles
* GWI : 4, GW2: 2, GW3: 2
* GWI : 2, GW2: 1, GW3: 1
*FAUX
C) GWI : 8, GW2: 1, GW3: 1
C) GWI        GW2: 2, GW3: 1

69 : Lors d'un routage sans NAT, quels champs de la trame sont modifiés à chaque passage par un routeur ?
* MAC source
* MAC dest
*FAUX
Adresse IP de destination
Port source
Adresse IP source
Port de destination



70 : Pour l'adresse IP 194.12.27.33 et le masque 255.255.255.240, l'adresse réseau et l'adresse de diffusion sont respectivement
* 194.12.27.32et 194.12.27.47