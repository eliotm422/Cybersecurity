.defense 
[[Threat and Hunting Fundamentals]]
[[Deobfuscation Javascript]]
*** 

# SIEM 

  

Le SIEM, ou Security Information and Event Management, est une technologie essentielle dans le domaine de la protection informatique. Il englobe l'utilisation de logiciels et de solutions pour gérer les données de sécurité et surveiller les événements de sécurité en temps réel. Ces outils permettent de détecter les cyberattaques au moment de leur déclenchement ou même avant, améliorant ainsi la réactivité face aux incidents de sécurité.

Le terme "SIEM" est né de la fusion de deux technologies antérieures : la gestion des informations de sécurité (SIM) et la gestion des événements de sécurité (SEM). Le SIEM collecte et traite les données provenant de différentes sources, telles que les appareils réseau, les serveurs et les applications, afin de les analyser et de détecter les menaces potentielles.

Les principales fonctionnalités d'un SIEM incluent la collecte et la gestion des journaux d'événements, l'analyse des données de différents systèmes, la prise en charge de la gestion des incidents, des résumés visuels et de la documentation.

Le SIEM offre des avantages considérables, notamment une visibilité accrue sur les menaces grâce à la consolidation des journaux, une détection rapide des attaques et une réponse plus efficace aux incidents de sécurité. Il joue également un rôle crucial dans la conformité aux réglementations de sécurité.

En résumé, le SIEM est un outil puissant qui permet aux entreprises de détecter, analyser et répondre aux menaces de sécurité de manière proactive, en centralisant et en corrélant les données de différents systèmes pour une meilleure prise de décision en matière de cybersécurité.

  
  
  
  

# Stack Elastic

  

Le Stack Elastic, créé par Elastic, est une collection de trois applications principales (Elasticsearch, Logstash et Kibana) en open-source qui fonctionnent ensemble pour offrir aux utilisateurs des capacités de recherche et de visualisation complètes pour l'analyse en temps réel et l'exploration de sources de fichiers journaux.

Elasticsearch est un moteur de recherche distribué basé sur JSON, conçu avec des API RESTful, qui gère l'indexation, le stockage et les requêtes des données. Logstash est responsable de la collecte, de la transformation et du transport des enregistrements de fichiers journaux, tandis que Kibana sert d'outil de visualisation pour les documents d'Elasticsearch.

Le Stack Elastic peut être utilisé comme une solution SIEM (Security Information and Event Management) pour collecter, stocker, analyser et visualiser des données de sécurité à partir de différentes sources, telles que les pare-feu, les IDS/IPS et les terminaux. En utilisant Kibana Query Language (KQL), les analystes SOC peuvent effectuer des recherches avancées et des corrélations pour détecter les incidents de sécurité et les menaces potentielles.

L'utilisation d'Elastic Common Schema (ECS) permet une approche unifiée et cohérente des données, ce qui facilite la création de requêtes et de visualisations. En utilisant ECS, les utilisateurs peuvent bénéficier d'une vue unifiée des données provenant de différentes sources et améliorer la corrélation des événements pour des enquêtes plus approfondies.

En résumé, le Stack Elastic est un ensemble d'outils puissants pour la gestion de données et l'analyse en temps réel, avec des fonctionnalités SIEM avancées pour la détection des menaces et la sécurité des systèmes informatiques.

  

## exemple :

  

event.code:4625

  

The KQL query event.code:4625 filters data in Kibana to show events that have the [Windows event code 4625](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=4625). This Windows event code is associated with failed login attempts in a Windows operating system.

  
  

"svc-sql1"

This query returns records containing the string "svc-sql1" in any indexed fiel

  
  

event.code:4625 AND winlog.event_data.SubStatus:0xC0000072

  

The KQL query event.code:4625 AND winlog.event_data.SubStatus:0xC0000072 filters data in Kibana to show events that have the Windows event code 4625 (failed login attempts) and the SubStatus value of 0xC0000072

  
  

event.code:4625 AND user.name: admin*

  

The Kibana KQL query event.code:4625 AND user.name: admin* filters data in Kibana to show events that have the Windows event code 4625 (failed login attempts) and where the username starts with "admin", such as "admin", "administrator", "admin123", etc.

  
  

Example: Identify failed login attempts against disabled accounts that took place between March 3rd 2023 and March 6th 2023 KQL:

event.code:4625 AND winlog.event_data.SubStatus:0xC0000072 AND @timestamp >= "2023-03-03T00:00:00.000Z" AND @timestamp <= "2023-03-06T23:59:59.999Z"

  

Data and field identification approach 1: Leverage KQL's free text search

  
  
  

http://10.129.99.85:5601

  

event.code:4625 AND winlog.event_data.SubStatus:0xC0000072

 Identify failed login attempts against disabled accounts that took place between March 3rd 2023 and March 6th 2023 KQL:

  
  

event.code:4625 AND user.name: admin*

  
  
  
  

# SOC

  

Un Centre Opérationnel de Sécurité (SOC) est une installation essentielle abritant une équipe d'experts en sécurité de l'information chargée de surveiller en permanence et d'évaluer le statut de sécurité d'une organisation. Le principal objectif d'une équipe SOC est d'identifier, d'examiner et de traiter les incidents de cybersécurité en utilisant un ensemble de solutions technologiques et de procédures.

Le SOC est composé généralement d'analystes, d'ingénieurs et de gestionnaires de sécurité compétents qui supervisent les opérations de sécurité. Ils collaborent étroitement avec les équipes d'intervention en cas d'incident pour garantir que les problèmes de sécurité sont rapidement détectés et résolus.

Pour surveiller et identifier les menaces de sécurité, le SOC utilise diverses solutions technologiques telles que les systèmes de gestion des informations de sécurité (SIEM), les systèmes de détection et de prévention des intrusions (IDS/IPS) et les outils de détection et de réponse aux points d'extrémité (EDR). Ils utilisent également des renseignements sur les menaces et mènent des initiatives de chasse aux menaces pour détecter de manière proactive les menaces potentielles et les vulnérabilités.

En plus des solutions technologiques, le SOC suit des processus bien définis pour traiter les incidents de sécurité, comprenant la gestion des incidents, l'isolement, l'élimination et la récupération. Le SOC travaille en étroite collaboration avec l'équipe d'intervention en cas d'incident pour assurer une gestion appropriée des incidents de sécurité, protégeant ainsi la sécurité de l'organisation.

Résumé : Un SOC est une installation essentielle qui abrite une équipe de professionnels de la sécurité de l'information chargée de surveiller en permanence et de répondre aux incidents de cybersécurité dans une organisation. Ils utilisent des technologies avancées pour détecter les menaces de sécurité et suivent des processus bien définis pour y faire face. Les rôles au sein d'un SOC varient, allant des analystes de base aux analystes de niveau avancé, aux ingénieurs de sécurité et aux spécialistes de la conformité. Le SOC évolue également avec le temps, passant par différentes étapes pour répondre aux menaces de plus en plus sophistiquées. La prochaine étape, le SOC cognitif, cherche à incorporer des systèmes d'apprentissage pour améliorer la prise de décision en matière de sécurité.

  
  
  

# MITRE ATT&CK & Security Operations

  

Le cadre MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) est une ressource exhaustive et régulièrement mise à jour qui répertorie les tactiques, techniques et procédures (TTP) utilisées par les cybercriminels. Il aide les experts en cybersécurité à mieux comprendre, identifier et réagir de manière proactive aux menaces.

Le cadre ATT&CK est composé de matrices adaptées à différents environnements informatiques, tels que les systèmes d'entreprise, mobiles ou cloud. Chaque matrice relie les tactiques (les objectifs que les attaquants cherchent à atteindre) et les techniques (les méthodes utilisées pour accomplir leurs objectifs) à des TTP distinctes. Cette association permet aux équipes de sécurité d'examiner de manière méthodique les activités des attaquants et de prédire leurs actions.

Utilisations du cadre MITRE ATT&CK dans les opérations de sécurité :

- Détection et réponse : Le cadre aide les équipes de sécurité à élaborer des plans de détection et de réponse basés sur les TTP des attaquants, leur permettant de repérer les dangers potentiels et de développer des contre-mesures proactives.
    
- Évaluation de la sécurité et analyse des lacunes : Les organisations peuvent utiliser le cadre ATT&CK pour identifier les forces et faiblesses de leur posture de sécurité, en priorisant les investissements dans les contrôles de sécurité pour se défendre efficacement contre les menaces pertinentes.
    
- Évaluation de la maturité du SOC : Le cadre ATT&CK permet aux organisations d'évaluer la maturité de leur Centre Opérationnel de Sécurité (SOC) en mesurant leur capacité à détecter, répondre et atténuer différentes TTP. Cela permet d'identifier les domaines à améliorer et de prioriser les ressources pour renforcer la posture de sécurité globale.
    
- Intelligence sur les menaces : Le cadre offre un langage et un format unifiés pour décrire les actions adverses, permettant aux organisations d'améliorer leur intelligence sur les menaces et de favoriser la collaboration entre les équipes internes ou avec des parties prenantes externes.
    
- Enrichissement de l'intelligence sur les menaces cybernétiques : En utilisant le cadre ATT&CK, les organisations peuvent enrichir leur intelligence sur les menaces en fournissant des informations sur les TTP des attaquants, ainsi que des indices sur les cibles potentielles et les indicateurs de compromission (IOC). Cela permet de prendre des décisions plus éclairées et de développer des stratégies efficaces pour contrer les menaces.
    
- Développement de l'analyse comportementale : En cartographiant les TTP décrites dans le cadre ATT&CK à des comportements spécifiques des utilisateurs et des systèmes, les organisations peuvent développer des modèles d'analyse comportementale pour identifier des activités anormales indiquant des menaces potentielles.
    
- Exercices de Red Teaming et de tests de pénétration : Le cadre ATT&CK permet de reproduire de manière systématique les techniques des attaquants lors d'exercices de Red Teaming et de tests de pénétration, évaluant ainsi les capacités de défense d'une organisation.
    
- Formation et éducation : La nature complète et bien organisée du cadre ATT&CK en fait une ressource exceptionnelle pour la formation et l'éducation des professionnels de la sécurité sur les dernières tactiques et méthodes adverses.
    

En résumé, le cadre MITRE ATT&CK est un atout indispensable pour les opérations de sécurité, offrant un langage partagé et une structure pour décrire et comprendre les comportements adverses. Il est essentiel pour améliorer divers aspects des opérations de sécurité, de l'intelligence sur les menaces et l'analyse comportementale à l'évaluation de la maturité du SOC et l'enrichissement de l'intelligence sur les menaces cybernétiques.

  

---

# What Is A SIEM Use Case?

  
  

Un cas d'utilisation SIEM (Security Information and Event Management) est un scénario spécifique dans lequel un produit ou un service de cybersécurité peut être appliqué. Ces cas d'utilisation permettent d'identifier et de détecter efficacement les incidents de sécurité potentiels. Ils peuvent couvrir des situations simples, comme des tentatives de connexion échouées, jusqu'à des scénarios plus complexes comme la détection d'une attaque de ransomware.

Par exemple, un cas d'utilisation SIEM peut consister à détecter 10 tentatives de connexion échouées consécutives pour un utilisateur nommé "Rob". Ces événements peuvent provenir d'un utilisateur légitime ayant oublié ses identifiants ou d'un acteur malveillant tentant de forcer l'accès au compte. Dans ce cas, le SIEM regroupe ces 10 événements en un seul et déclenche une alerte à l'équipe de sécurité ("brute force" use case).

Le développement d'un cas d'utilisation SIEM suit plusieurs étapes :

- Définir les besoins : Comprendre le scénario spécifique pour lequel une alerte ou une notification est nécessaire.
    
- Identifier les sources de données : Trouver les sources de données générant des journaux d'événements pertinents pour le cas d'utilisation, tels que les journaux d'événements de système d'exploitation, les journaux de pare-feu, etc.
    
- Valider les journaux : Vérifier que les journaux contiennent toutes les informations nécessaires pour détecter les événements d'intérêt.
    
- Concevoir et mettre en œuvre le cas d'utilisation : Définir les conditions pour déclencher une alerte, l'agrégation des événements, et établir la priorité de l'alerte.
    
- Documenter les procédures : Rédiger des procédures standard pour gérer les alertes, y compris les conditions, l'agrégation, la priorité et les rapports aux autres équipes.
    
- Intégration : Tester et déployer le cas d'utilisation dans l'environnement de production.
    
- Mise à jour et optimisation : Affiner le cas d'utilisation en fonction des retours d'analystes et des nouvelles menaces.
    

Exemples de cas d'utilisation SIEM :

Exemple 1 : Détection d'un MSBuild initié par une application Office

- Identifier les tentatives de connexion échouées pour un utilisateur spécifique.
    
- Vérifier que les journaux d'événements contiennent les informations nécessaires.
    
- Concevoir une alerte pour 10 tentatives de connexion échouées en 4 minutes.
    
- Documenter les procédures pour l'analyse des alertes et les actions à prendre.
    

Exemple 2 : MSBuild établissant des connexions réseau

- Surveiller les instances où MSBuild.exe établit des connexions sortantes.
    
- Définir une alerte pour détecter des connexions sortantes suspectes initiées par MSBuild.
    
- Mettre en place un processus d'analyse et de réponse spécifique à cette alerte.
    

En résumé, les cas d'utilisation SIEM sont des scénarios spécifiques qui permettent aux organisations de détecter et de réagir efficacement aux menaces de sécurité. Ils nécessitent une planification et une documentation soignées pour assurer leur succès et leur adaptation aux besoins spécifiques de chaque organisation.

  

# The Triaging Process

  

Le triage des alertes, effectué par un analyste d'un Centre des Opérations de Sécurité (SOC), est le processus d'évaluation et de priorisation des alertes de sécurité générées par différents systèmes de surveillance et de détection, afin de déterminer leur niveau de menace et leur impact potentiel sur les systèmes et les données d'une organisation. Cela implique de passer en revue de manière systématique et de catégoriser les alertes pour allouer efficacement les ressources et répondre aux incidents de sécurité.

L'escalade est un aspect important du triage des alertes dans un environnement SOC. Le processus d'escalade implique généralement de notifier les superviseurs, les équipes d'intervention en cas d'incident ou des personnes désignées au sein de l'organisation qui ont l'autorité de prendre des décisions et de coordonner les efforts de réponse. L'analyste du SOC fournit des informations détaillées sur l'alerte, y compris sa gravité, son impact potentiel et toutes les découvertes pertinentes de l'enquête initiale. Cela permet aux décideurs d'évaluer la situation et de déterminer le plan d'action approprié, comme impliquer des équipes spécialisées, déclencher des procédures d'intervention plus étendues ou faire appel à des ressources externes si nécessaire.

L'escalade garantit que les alertes critiques reçoivent une attention immédiate et facilite la coordination efficace entre les différentes parties prenantes, permettant une réponse rapide et efficace aux incidents de sécurité potentiels. Cela permet de tirer parti de l'expertise et des capacités de prise de décision des personnes chargées de gérer et d'atténuer les menaces ou incidents de niveau supérieur au sein de l'organisation.

Processus idéal de triage des alertes :

- Examen initial de l'alerte :
    

- Examiner minutieusement l'alerte initiale, y compris les métadonnées, l'horodatage, l'adresse IP source, l'adresse IP de destination, les systèmes affectés et la règle/signature déclenchante.
    
- Analyser les journaux associés (trafic réseau, système, application) pour comprendre le contexte de l'alerte.
    

- Classification de l'alerte :
    

- Classer l'alerte en fonction de sa gravité, de son impact et de son urgence à l'aide du système de classification prédéfini de l'organisation.
    

- Corrélation des alertes :
    

- Faire des recoupements avec des alertes, des événements ou des incidents connexes pour identifier des motifs, des similitudes ou des indicateurs potentiels de compromission (IOC).
    
- Interroger le SIEM ou le système de gestion des journaux pour recueillir des données de journal pertinentes.
    
- Utiliser des flux de renseignements sur les menaces pour vérifier les modèles d'attaque connus ou les signatures de logiciels malveillants.
    

- Enrichissement des données d'alerte :
    

- Rassembler des informations supplémentaires pour enrichir les données de l'alerte et obtenir du contexte :
    
- Collecter les captures de paquets réseau, les vidages mémoire ou les échantillons de fichiers associés à l'alerte.
    
- Utiliser des sources de renseignements externes sur les menaces, des outils open source ou des environnements sécurisés pour analyser les fichiers suspects, les URL ou les adresses IP.
    
- Effectuer une reconnaissance des systèmes affectés pour repérer les anomalies (connexions réseau, processus, modifications de fichiers).
    

- Évaluation des risques :
    

- Évaluer le risque potentiel et l'impact sur les actifs critiques, les données ou l'infrastructure :
    
- Tenir compte de la valeur des systèmes affectés, de la sensibilité des données, des exigences de conformité et des implications réglementaires.
    
- Déterminer la probabilité d'une attaque réussie ou d'un mouvement latéral potentiel.
    

- Analyse contextuelle :
    

- L'analyste prend en compte le contexte entourant l'alerte, y compris les actifs affectés, leur importance critique et la sensibilité des données qu'ils traitent.
    
- Il évalue les contrôles de sécurité en place, tels que les pare-feux, les systèmes de détection/prévention d'intrusions et les solutions de protection des points d'extrémité, pour déterminer si l'alerte indique une défaillance potentielle du contrôle ou une technique d'évasion.
    
- L'analyste évalue les exigences de conformité, les réglementations de l'industrie et les obligations contractuelles pertinentes pour comprendre les implications de l'alerte sur la conformité légale et réglementaire de l'organisation.
    

- Planification de l'intervention en cas d'incident :
    

- Lancer un plan d'intervention en cas d'incident si l'alerte est significative :
    
- Documenter les détails de l'alerte, les systèmes affectés, les comportements observés, les IOC potentiels et les données enrichies.
    
- Attribuer des membres de l'équipe d'intervention en cas d'incident avec des rôles et des responsabilités définis.
    
- Coordonner avec d'autres équipes (opérations réseau, administrateurs système, fournisseurs) si nécessaire.
    

- Consultation avec les opérations informatiques :
    

- Évaluer le besoin de contexte supplémentaire ou d'informations manquantes en consultant les opérations informatiques ou les services pertinents :
    
- Participer à des discussions ou des réunions pour recueillir des informations sur les systèmes affectés, les changements récents ou les activités de maintenance en cours.
    
- Collaborer pour comprendre les problèmes connus, les mauvaises configurations ou les changements réseau qui pourraient potentiellement générer des alertes faussement positives.
    
- Obtenir une compréhension globale de l'environnement et de toute activité non malveillante qui aurait pu déclencher l'alerte.
    

- Documenter les informations et les connaissances obtenues lors de la consultation.
    
- Exécution de la réponse :
    

- En fonction de l'examen de l'alerte, de l'évaluation des risques et de la consultation, déterminer les actions de réponse appropriées.
    
- Si le contexte supplémentaire résout l'alerte ou l'identifie comme un événement non malveillant, prendre les mesures nécessaires sans
    

  
  
  

- Visualization 1: Failed logon attempts (All users)  
    Such a visualization might reveal potential brute force attacks. It's important to identify any single user with numerous failed attempts or perhaps, various users connecting to (or from) the same endpoint device. However, the current data does not point towards any such scenario. One anomaly is noticeable though. Hint: It is related to the "sql-svc1" account.
    
- Visualization 2: Failed logon attempts (Disabled user)  
    It seems that there is one incident where the user "Anni" has tried to authenticate, despite the account being disabled.
    
- Visualization 3: Failed logon attempts (Admin users only)  
    Hint: Check if all events took place on either Privileged Access Workstations (PAWs) or Domain Controllers.
    
- Visualization 4: RDP logon for service account  
    Service accounts in this environment serve a very specialized function. Do you notice anything that warrants suspicion?
    
- Visualization 5: User added or removed from a local group  
    An administrator has incorporated an individual (who is only represented by the SID value) into the "Administrators" group. Should you escalate to a Tier 2/3 analyst or consult with the IT Operations department first?
    
- Visualization 6: Admin logon not from PAW  
    Administrators should exclusively utilize PAWs for server remote connections. Should you escalate to a Tier 2/3 analyst or consult with the IT Operations department first?
    
- Visualization 7: SSH Logins  
    Be reminded that the root user account is not typically in use.
    

  
**