# Hachage

## Propriétés
- Fonction unidirectionnelle : impossible de retrouver l'original à partir du hash.

## Usages
- Stockage des mots de passe
- Vérification de l'intégrité des données
- Signatures numériques
- Contrôle d'intégrité
- Indexation des données
- Proof of Work (preuve de travail)

# Échange de Données

## Chiffrement Symétrique
- Utilisé pour échanger des données de manière sécurisée.

# Chiffrement Asymétrique

## Clé Privée et Clé Publique
- **Clé privée** : utilisée pour chiffrer.
- **Clé publique** : utilisée pour déchiffrer.

# Signature Numérique

## Objectif
- Prouver que la donnée a bien été créée par sa source et n'a pas été altérée lors de l'échange.

## Processus
1. On chiffre les données avec un hash et on ajoute une clé privée : cela constitue la signature.
2. On envoie le document + clé privée.

## Vérification
1. Récupérer la signature et utiliser la clé privée pour déchiffrer.
2. Récupérer le texte et le chiffrer.
3. Si les résultats des deux étapes sont identiques, la signature est valide.

# Infrastructure à Clé Publique (PKI)

## Fonctionnement
- Vérifier la date d'expiration.
- Validation de la signature par le certificat racine.

## Catalogue de Certificats
- Les machines possèdent par défaut un catalogue de certificats racines.

# Création d'un Certificat

## Étapes
1. Garder la clé privée (elle certifie que c'est bien moi qui envoie les données).
2. Envoyer la clé publique + renseignements.
    - L'autorité de certification fait un hachage de la clé publique + renseignements.
    - Cela constitue le certificat.

## Illustration
![Image](image.webp)

# Révocation d'un Certificat

## Méthodes
- **Expiration** : le certificat expire ou n'est pas renouvelé.
- **Révocation** :
  - **CTL** : Liste de révocation de certificats.
  - **OCSP** : Interrogation de la PKI à chaque authentification via OCSP.


C'este une chaine de vérification :
* Pour vérifier un certificat, cela fonction comme une chaîne :
	* Une autorité de certification racine vérifier le certificat
	* Qui sera vérifier par l'autorité de certification subordonnée
	* Qui sera vérifier l'autorité de certification subordonnée...


# SSL/TLS


outil tuffin : outil de pour regrouper toutes les sécurités de firewall