import bcrypt

def hasher_mot_de_passe(mot_de_passe, sel):
    mot_de_passe_encode = mot_de_passe.encode('utf-8')
    sel_encode = sel.encode('utf-8')
    hashed = bcrypt.hashpw(mot_de_passe_encode, sel_encode)
    return hashed

def verifier_mot_de_passe(mot_de_passe, sel, hashed_mot_de_passe):
    mot_de_passe_encode = mot_de_passe.encode('utf-8')
    sel_encode = sel.encode('utf-8')
    hashed_a_verifier = bcrypt.hashpw(mot_de_passe_encode, sel_encode)

    return hashed_a_verifier == hashed_mot_de_passe

# Exemple d'utilisation
mot_de_passe_utilisateur = "motdepasse123"
sel_utilisateur = bcrypt.gensalt()

# Hachage du mot de passe avec le sel
mot_de_passe_hache = hasher_mot_de_passe(mot_de_passe_utilisateur, sel_utilisateur)

# Vérification du mot de passe
mot_de_passe_entre = "motdepasse123"
verification_reussie = verifier_mot_de_passe(mot_de_passe_entre, sel_utilisateur, mot_de_passe_hache)

if verification_reussie:
    print("Mot de passe correct.")
else:
    print("Mot de passe incorrect.")