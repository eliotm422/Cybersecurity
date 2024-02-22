
## 1. OSINT c'est quoi?  

Qu'est-ce que l'OSINT 

OSINT : Méthode consistant à collecter et à analyser de l'informations provenant de sources publiques 

Les différentes méthodes de renseignement :

* HUMINT : Human Intelligence 

	* Renseignement d'origine humaine 

* SIGINT : Signal Intelligence 

	* Renseignement d'origine électromagnétique 

* IMINT : Imagery Intelligence 

    * Renseignement d'origine humaine 

* OSINT : Open Source Intelligence 

    * Renseignement d'origine humaine 


Avantages et inconvénients :

  * L'OSINT c'est bien pour :  

	* Savoir à qui j'ai à faire 

    * Avoir une plus grande réactivité sur des actualités 

    * Pouvoir tester mon exposition et identifier mes vulnérabilités 

    * Être plus pertinent dans mes réponses 

    * Trouver des informations pertinentes connues de peu de personnes 

L'OSINT c'est moins bien pour :  

  * Des personnes malveillantes peuvent utiliser à mon encombre 

  * Les attaques contre ma personne/organisation/cercle proche sont plus difficilement identifiable 

  

L'OSINT ça sert à qui/quoi :

  * Journalistes 

  * Investigations (fact checking, …) 

  * Forces de l'ordre 

  * Lutte contre les trafics (armes, arts, contrefaçons, humains…) 

  * Identifications de criminels (reconnaissances faciales, idetnficiations de lieux de résidences, d'exécution…) 

  * Groupes malveillants 

  * Identifications de vecteurs d'attaque 

  * ONG 

  * Investigations (Phénomènes d'actualités, désinformations…) 

  * Entreprises 

  * Sécurité informatiques (CTI, pentest, redteam) 

  * Intelligences économique 

  * Criminels 


## 2. Etape red team

* Envoie mail malveillant
	* Fichier malveillant
	* Clic par cible

* Intrusion physique
	* Pénétration au sein du site cible 
	* Interactions avec les employés


* Spear-phishing 
	* Listing des employés de l'organisation
	* Récupérations des coordonnées professionnelles des cibles
	* Détections des mécanismes de sécurité présebts

* Intrusion physique 
	* Processus
	* Employés clés
	* Plans des bâtiments
	* Sécurité des postes 


## 3. Investigation sur une région


* OPSEC : permet de cacher son identité 
* SIGINT : permet d'intercepter des signaux radios 


* Objectifs 
	* Récupérer des informations intéressantes sur une région données
* Information visées
	* Connaissances en direct sur les évènements 


## 4. Actualités 

* Comptes telegram spécialisés
* Discord Project owl 
* Snapchat / Instagram (#) / tiktok (coupsure) / twitter benjamin pite? 
* twitter : geocode:Lat,Long,rayon,Km, near, until,since
* twitter : requête complexe, liste : site:twitter.com/*/list.iran, tweetdeck, tweeter build a query 




## 5. Investigation sur une organisation

* Objectif : avoir le plus d'informations
* Informations visées 
	* Organigrammes
	* Actionnaires
	* Employés
	* Partenaires
	* Vocabulaire

* Historique :
	* Archive.org, par exemple commande : web.archive.org/web/*/https://www.SITEWEB.com/* 
	* waybackmachine
* Rapidedns.io, connaître les dns 
* Amass : 
	* OWASP, permet de regarder la surface d'attaque d'un site web 
* Favicon to murmur hash
* Societe.ninja / pappers.fr 
* Opencorporates : recherche d'informations légales dans toutes les juridictions 
* Offshoreleaks.ciji : organisaiton leaks
* Aleph.occrp : contre la corruption


* Regarder les appels d'offres 
	* Monitoring des plateformes d'appels d'offres permet de récupérer :
		* Prestataires
		* Besoins
		* Environnement
		* contacts
* Liens utiles : 
	* Google : tenders entreprisecuble
	* globaltenders.com 

* Linkedin :
	* meetalfred.com
	* linkdedinhelper
	* ajouter /detail/recent-activity/ 
	* fec.gov : retrouver don chez personnes américaines
* Passer sur google dork si on ne sait jamais

* Instagram :
	* Google dork :
		* pseudo site:instagram.com site:instagram.com/pseudo

* Twitter : 
	* Accountanalysis : statistique sur un profil twitter 
* Adresse mail : regarder des google dork 


méthodologie : 
	Orgainisaiton :

* Méthodologie : 
	* Orgnasitation
		* A partir du site web
		* Acceder aux réseaux sociaux
		* Ou est basée l'orga?
	* Se mettre à la place de la cible, et chaque cible est unique

	## Ingénierie social

* Amorçage : 
	* Repose sur une mise en avant par le manipulateur d'avantages fictif dont le caractère illusoire est révélé in extremis
		* Exemple : vient m'aider à déménager , OK, je te préviens juste maintenant que tu as accepté que c'est au 8ème, c'est un avantage fictif.
* Pied dans la porte :
	* Demander une action peu couteuse avant de demander une action couteuse
		* On demande l'heure à une personne, puis on demande de l'argent.
* Porte au nez : 
	* Demander une action très couteuse qui sera refusée pour par la suite demander une action beaucoup moins couteuse qui elle sera acceptée.


### Intrusion physique

* intrusion physique
  * Dans les locaus d'une organisation cible afin de récupérer des informations ou déposer des dispositifs permettant de mener une attaque informatique interne 
* Réparage :
  * HO / HNO :
    * Repérage des entreprises prestataires et des horaires
    * Voir les différents accès 
    * Détecter la présence des systèmes de vidéos surveillance et de communciation radio
    * Essayer de rentrer au niveau de l'acceuil
    * Plan évacuation
    * Demander d'aller aux toilettes poru essayer d'aller plus loin
    * Détection des types d'entrées 
    * Fumer une cigarette devant les locaux


3 techniques d'intrusion :
	* Over tester 
    	* Faire comme si de rien n'était
    	* Avoir un scénario crédible
  	* Covert tester 
    	* Evite les interactions avec les gens
    	* Attaque la plus simple et moins risqué
  	* Unseen tester
    	* Veut être vu par personne
    	* Agit souvent en pleine nuit s 