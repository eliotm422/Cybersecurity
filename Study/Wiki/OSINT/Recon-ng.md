
.Sup
[[Sup de Vinci/cours/OSINT]]
# Les Commandes

Recon-NG tire sa force de ses modules. Chaque module a sa fonctionnalité propre. Il faut donc savoir quel module utilisé et à quel moment.

|Module|Description|
|---|---|
|discovery/info_disclosure/interesting_files|Extrait des fichiers type robot.txt d'un domaine|
|recon/credentials-credentials/bozocrack|Tente de trouver dans Google le décryptage d un mot de passe|
|recon/domains-contacts/hunter_io|Recheche des contacts et E-mail à partir d'un nom de domaine|
|recon/domains-contacts/wikileaker|Recherche dans les Wikileak si une correspondance existe par rapport au domaine et rempli la table contact|
|recon/domains-domains/brute_suffix|Trouver toutes les extensions de domaines ayant une entrée DNS|
|recon/domains-hosts/brute_hosts|Brute-force pour trouver les sous domaines|
|recon/domains-hosts/builtwith|Permet d'afficher des informations relatives aux domaines, technologie, serveur s.... mais attention ne stocke rien en base de donnée.|
|recon/domains-hosts/censys_domain|API censys pour récupérer informations sur les ports et hosts d un domaine|
|recon/domains-hosts/certificate_transparency|Analyse un certificat SSL d'un domaine et en extrait s'il existe d'autres noms de domaines rattacher au certificat|
|recon/domains-hosts/hackertarget|Récupération IP et host via Hackertarget|
|recon/domains-hosts/mx_spf_ip|Recherche les serveurs MX du domaine et enregistre dans la table hosts|
|recon/domains-hosts/netcraft|Interroge Netcraft pour trouver des infos|
|recon/domains-hosts/ssl_san|Analyse le SAN d'un domaine pour en extraire tous les hosts|
|recon/hosts-hosts/censys_ip|Liste les ports via l'API de Censys|
|recon/hosts-hosts/ipinfodb|Géolocalisation des IP de la table hosts|
|recon/locations-locations/geocode|Géolocalisation des adresses postales|
|recon/hosts-hosts/resolve|Permet de compléter les IP de la tables hosts en résolvant le nom de domaine|
|recon/hosts-hosts/reverse_resolve|Permet de compléter la table host en trouvant les noms de domaine manquants des IP|
|recon/hosts-ports/shodan_ip|Met à jour la liste de port d une IP dans host à partir de Shodan|
|recon/locations-pushpins/flickr|Permet de trouver des photos autour d'une localisation|
|recon/locations-pushpins/shodan|Cherche autour d une coordonnée GPS des IOT dans Shodan|
|recon/locations-pushpins/twitter|Chercher des Tweets avec media autour de coordonnée GPS|
|recon/locations-pushpins/youtube|Recherche des vidéos Youtube autour de coordonnée GPS|
|recon/netblocks-companies/censys_netblock_company|Récupère les informations de Censys qui appartient un block d IP|
|recon/netblocks-companies/whois_orgs|Récupère les informations du Whois sur une IP|
|recon/netblocks-hosts/shodan_net|Trouve les hostnames des IPs d'un netblock à partir de Shodan|
|recon/netblocks-hosts/virustotal|Trouve les hostnames des Ips d'un netblock à partir de Virustotal|
|recon/netblocks-ports/census_2012|Trouve les ports d'un netblock via Exfiltrated.com|
|recon/netblocks-ports/censysio|Trouve les ports d un netblock via Censysio|
|recon/profiles-contacts/bing_linkedin_contacts|Complète la table compagnie et contact à partir de profiles Linkedin|
|recon/companies-contacts/bing_linkedin_cache|Complète les tables profiles et contact à partir de la table compagnie en faisant une recherche sur LinkedIn|
|recon/profiles-contacts/dev_diver|Recherche des repository de code a partir du Username de profil|
|recon/profiles-contacts/github_users|Remplit la table contact pour les profiiles dont le username n'est pas vide et la ressource est Github|
|recon/profiles-profiles/profiler|Recherche sur plusieurs siteq si des comptes existent pour les usernames dans la table profiles et rajoute les URLs des comptes dans la table profiles|
|recon/profiles-profiles/twitter_mentioned|Recherche le username provenant de Twitter dans la table profiles et listent les user qui parle de lui|
|recon/profiles-profiles/twitter_mentions|Recherche les username provenant de twitter de la table profiles et liste les users qu il mentionne dans ses posts|
|recon/profiles-repositories/github_repos|Recherche depuis les username de la table profile sur Github. Liste les repository pour les mettre dans la table repository|
|recon/repositories-profiles/github_commits|Recherche depuis la liste des repository la liste des user ayant effectué des commit sur le projet et update les profiles|
|recon/repositories-vulnerabilities/gists_search|Recherche depuis la liste des repository ciblant Github une liste de vulnérabilité|
|recon/repositories-vulnerabilities/github_dorks|Recherche deouis les repository une liste de vulnérabilité|
|reporting/html|Permet de faire un export HTML des résultats|
|reporting/csv|Permet de faire un export CSV des résultats|
|reporting/xml|Permet de faire un export XML des résultats|


# Guide

https://www.6ber-network.com/tutoriaux/recon-ng-part1/

* On remet à 0 le market place, ça permet de lister des modules *

```bash
marketplace refresh
```

* Permet de chercher des modules *
``` bash
marketplace search motclé
```

* Permet de voir les infos modules *
```bash
marketplace info bing_linkedin_cache
```

* Marketplace install et remove *
```bash
marketplace install censys_tls_subjects
```
	
	 * Si nous avons des erreurs, penser à mettre à jour pyp*
``` bash
pip install --upgrade censys 
ou
python -m pip install --upgrade pip
```


```bash
marketplace remove censys_tls_subjects
```
* Voir les clefs API qui sont enregistrés dans recon-ng*
```bash
keys list
```
* Ajouter des clefs ou les retirer*
```bash
keys add <name> <value>
```
