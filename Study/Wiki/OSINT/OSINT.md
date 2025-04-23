.Sup

https://osintfr.com/fr/outils/
# La recherche d'informations

* En générale on utilise : 
	* Traduction de langage 
		* Babel X
	* Git : 
		* Grep.app
	* Clear Deep / Dark web :
		* OWLINT
	* Les opérateurs / moteurs de recherches
		* Maltego (data mining)
		* Dorksearch (informations selon certaines recherches)
		* Global Scam Database (de tout)
		* Mikata (sur Opensearch for web)
		* SpiderFoot (sur les informatiosn web)
		* Intelligence X (data archive)
		* the harvester (outil complet site web)
	* Images
		* Yandex images / Googlees Images (Reverse Image search)
		* RevEye (Reverse Image search (add-on))
		* ExifData (exif viewer)
		* EXIF Viewer (exif viewer (add-on))
		* Forensically (Detection of Digital alterations )
		* DiffChecker (Compare two images)
		* Photo scissors (Remove background)
		* Let's Enhance (enahce image quality)
		* Findclone/ PIMEYES(Reconnaissance faciale)
		* Invid (extraire les images dans la vidéo)
	* Email 
		* Global Scam Database (de tout)
		* Epios (activité lié à l'adresse mail)
		* Hunter.io (email pro)
		* emailhippo
	* Mots de passe 
		* dehashed.com
		* Global Scam Database
		* Recon-ng
			* git clone https://github.com/lanmaster53/recon-ng.git
			* cd recon-ng
			* recon-ng --help
			* sudo recon-ng
				* on crée un workspace pour chaque reconnaissance
				- chaque workspace dispose de sa propre base de donnée pour stocker les resultats
				- on charge les modules dont on a besoin et on les paramètres en ligne de commande
				- on lance et on traite les résultats obtenus pour éliminer les faux positifs. Cela se fait grâce à des requêtes SQL à la mano.
- On génère le rapport au format que l ‘on veut
		* ihavebeenpwned (fuite mdp)
	* Personnes 
		* Hunter.io (email pro)
		* Maltego (très complet)
		* Lusha (info sur les comptes pro des personnes)
		* Pipl (Moteurs de recherche sur les personnes)
	* Noms d'utilisateurs
		* USERSEARCH
		* Namechck
		* Whatmyname
		* Maigret 
			* git clone https://github.com/soxoj/maigret.git
			* cd maigret
			* sudo pip install -r requirements.txt
			* ./maigret.py --help
			* ./maigret.py geeksforgeeks --tags photo,dating
			* ./maigret.py geeksforgeeks noms-a
		* Whatsmyname (recherche de nom sur sites web)
	* Réseaux sociaux 
		* Eagle Eye : (trouver comptes Facebook Twitter Insta à partir d'une photo)
		* Namecheck (trouve le profil en fonction des infos)
		* Sherlock (nom d'utilisateur sort des profils)
		* Accountanalysis (utilisé sur Twitter)
		* Trendsmap (permet de voir les hashtages)
	* Sites web
		* BuiltWith (technologie de site web)
		* Recon-ng (faiblesse de site web)
		* Central OPs (domaine)
	* Wifi / réseau
		*  Spyse (sécurité sur les réseaux informatiques)
	* GeoINT
		* GeoINT Localisator (distance entre deux lieux connus)
		* Overpass turbo (filtrage des données pour OpenStreetMap)
		* SunCalc (permet de voir l'ensoleillement la journée à un endroit donnée)
	* Phone number 
		* Truecaller (Reverse phone number)
		* Epieos Phone number (comtpes liés à un numéro de téléphone)
		* PhoneINfoga (outil de collecte de numéros de téléphone)
		* TrueCaller Identifier et bloquer les appels
	* SOCMINT (collecte d'informations sur tout ce qui est publiquement disponible )
		* Instalocktrack ( permet de trouver les géolocalisations Instagram)
		* SnapMap ( carte avec les dernières stories publiées sur Snap)
		* Tweets Analyzer / Twint ( Twitter)
	* OPSEC (Protection contre la collecte d'informations)
		* FakeNameGenerator (fausse identité en ligne)
		* Thispersondoesnotexist (générer des images de personne)
		* TinyCheck (analyse de réseau)
	* Entreprise
		* OCCRP Aleph (documents publiques et fuites de données)
		* wigle.net (cherche de connexion sur le lieu)
		* Offshore leak database (qui est derrière els sociétés offshore)
		* Opencorporate (la plus grande base de donnée ouverte d'entreprise)
		* Societe.ninja (info gratuite sur les sociétés françaises)
	* Threat Intelligence ( Renseignement sur les cyber-menaces et cyber-attaques)
		* Any.run (echantillons gratuits bac-à-sable) pour logiciels malveillants
		* CRT.sh (réalisation d'empreintes de certificats et d'indetifications d'autres, similaire en ligne)
		* Onyphe (connecte les données sur les IP et les services)
		* *Shodan* (adresse ip et port ouvert sur web)
		* Virus totale (téléchargement et recherche logiciels malveillants par Google)
	* Data 
		* Metagoofil (metadata des documents)
		* Maltego (data mining)
		* Intelligence X (data archive)
		* Global Scam Database (de tout)
	* Code 
		* Searchcode (informations)
	* Site malveillant
		* Virus total .com
	* Voir les anciennes informations du site web 
		* THe Visual ping / waybackmachine
	

# La méthodologie

Fonctionnement :
	* 1 : Fake Name Generator
	* 2 : This Person Does Not Exist
	* 3 : Privacy.com permet d'ouvrir un compte banquaire (généralement aux etats Unis)
	* 4 : VPN

# La VM Trace Labs

VM spécialisée dans l'OSINT
## Applications Included

#### **Category**

**Tools/Features**  

#### Domains

• Sublist3r

#### Downloaders

• Browse Mirrored Websites  
• Metagoofil  
• Spiderpig  
• WebHTTrack Website Copier  
• Youtube-DL

#### Browsers

• Chromium Web Browser  
• Firefox ESR  
• Tor Browser

#### Emails

• Buster  
• H8mail  
• Infoga  
• theHarvester

#### Data Analysis

• DumpsterDiver  
• Exifprobe  
• Exifscan  
• Photon  
• Stegosuite

#### Frameworks

• FinalRecon  
• Little Brother  
• recon-ng  
• sn0int  
• Spiderfoot  
• WikiLeaker

#### Phone Numbers

• OSINT-Search  
• PhoneInfoga

#### Social Media

• Instaloader  
• Twint

#### Usernames

• Sherlock  
• WhatsMyName

#### FireFox Configuration Settings  

• Delete cookies/history on shutdown  
• Privacy protection (block mic/camera/geo)  
• OSINT Bookmarks

#### Other tools  
(not listed in the menu)  

• checkdmarc  
• Photon  
• Carbon14  
• Sherlock  
• skiptracer  
• h8mail  
• Shodan