# Propriété d'Eliot MUSSET, chaîne MINIMUSS
# Vous êtes libre de le réutiliser, mais n'hésitez pas à parler de moi :) 

# Permet d'utiliser les foncitons de hash
import hashlib
# 
import os
# Permet d'importer toutes les lettres 
import string 
# Permet de calculer le temps d'une fonction
import time

# En entrée rien, en sortie un dictionnaire contenant toutes les lettres chiffres, et les deux mots de passes avec hash
def definition_variable() : 
    # Récupérer toutes les lettres minuscules
    lettres_minuscules = string.ascii_lowercase
    # Récupérer toutes les lettres majuscules
    lettres_majuscules = string.ascii_uppercase
    # Récuprer tous les numéros
    chiffres = string.digits
    # Récupérer les caractères spéciaux
    speciaux = string.punctuation

    # Définition du dictionnaire contenant toutes les lettres chiffres possibles 
    dictionnaire_test = lettres_majuscules + lettres_minuscules + chiffres + speciaux
        
    password1 = 'Crocodile741!'    


    password2 = 'Tu es mauvais jack'    

    print("Mot de passe numéro 1 :", password1)
    print("Mot de passe numéro 2 :", password2)

    return dictionnaire_test, password1, password2


# En entrée un mot de passe, en sortie un hash sans le sel, le sel tout seul, le hash +sel
def hash_password(password):
    
    # Génère une serie de 16 chiffres aléatoires par l'OS
    salt = os.urandom(16)  

    # Génère un hash aléatoire
    hash_algorithm = hashlib.sha256()

    # Rajoute le sel et le mot de passe
    hash_algorithm.update(salt + password.encode())

    # Récupération de l'hexadécimal du hash et du sel pour le stockage
    hashed_password = hash_algorithm.hexdigest()

    # On renvoie le hash avant d'y rajouter le sel, le sel, et le hash + sel + mdp
    return hash_algorithm, salt, hashed_password

# en entrée nos données qu'on veut afficher, le programme s'occupe d'afficher les données des variables de d+ùd
def affichage_donnee(hash_algorithm, salt, hashed_password) :
    print ("\n Le hash du mot de passe :", hash_algorithm)
    print ("\n Le sel du mot de passe :", salt)
    print ("\n Le hash, le sel avec le mdp :", hashed_password)
    
# En entrée les données qu'on veut afficher
def affichage_cracker_mdp(nb_tentative, new_password1, temps_execution) : 
    print ("\n Le nombre de tentative :", nb_tentative)
    print ("\n Le mot de passe trouvé :", new_password1)
    print ("\n Le mot de passe trouvé :", temps_execution)
    

def cracker_mdp_lettre_par_lettre(password, dictionnaire_test):
    # Nouveau mdp
    new_password = ''
    
    # Tailles du mot de passe et du dictionnaire
    taille_mdp = len(password)
    taille_dico = len(dictionnaire_test)
    
    # Compteur de tentatives et de secondes
    nb_tentative = 0
    
    # Condition de sortie
    mdp_trouve = False
    max_tentative = 10000
    
    # Permet de se balader dans le mot de passe
    cmpt_mdp = 0
    
    temps_debut = time.time()
    
    while not mdp_trouve and nb_tentative < max_tentative and cmpt_mdp < taille_mdp:
        # Tant qu'on n'a pas trouvé la lettre actuelle avec la lettre du dico
        cmpt_dico = 0
        lettre_actuelle_trouve = False
        
        while not lettre_actuelle_trouve and cmpt_dico < taille_dico:
            
            # Si la lettre actuelle du mot de passe est égale à celle du dictionnaire
            if password[cmpt_mdp] == dictionnaire_test[cmpt_dico]:
                # On rajoute la lettre du nouveau mot de passe
                new_password += dictionnaire_test[cmpt_dico]
                # On sort de la boucle interne et on cherche la prochaine lettre du mot de passe rentré
                lettre_actuelle_trouve = True
                print (' La lettre numéro',cmpt_mdp+1,'est la lettre',dictionnaire_test[cmpt_dico])
                cmpt_mdp += 1
            else:
                cmpt_dico += 1
                nb_tentative += 1
    
    temps_final = time.time()
    temps = temps_final - temps_debut
    
    return nb_tentative, new_password, temps 


def main() :

    dictionnaire_test, password1, password2 = definition_variable()
    hash_algorithm1, salt1, hashed_password1 = hash_password(password1)
    affichage_donnee(hash_algorithm1, salt1, hashed_password1)
    
    '''
    nb_tentative1, new_password1, temps_execution1 = cracker_mdp_lettre_par_lettre(password1, dictionnaire_test)
    affichage_cracker_mdp(nb_tentative1, new_password1, temps_execution1)
    '''
    
    hash_nb_tentative1, hash_new_password1, hash_temps_execution1 = cracker_mdp_lettre_par_lettre(hashed_password1, dictionnaire_test)
    affichage_cracker_mdp(hash_nb_tentative1, hash_new_password1, hash_temps_execution1)
    
    
    '''
    hash_algorithm2, salt2, hashed_password2 = hash_password(password2)
    affichage_donnee(hash_algorithm2, salt2, hashed_password2)
    nb_tentative1, new_password1, temps_execution1 = cracker_mdp_lettre_par_lettre(password1, dictionnaire_test)
    #nb_tentative2, new_password2, temps_execution2 = cracker_mdp_lettre_par_lettre(password2, dictionnaire_test)
    #affichage_cracker_mdp(nb_tentative2, new_password2, temps_execution2)
    '''
    print ("Imaginons, maintenant on veut trouver le mdp avec sel plus hash...")
    #nb_tentative2, new_password2, temps_execution2 = cracker_mdp_lettre_par_lettre(hashed_password1, dictionnaire_test)
    #affichage_cracker_mdp(nb_tentative2, new_password2, temps_execution2)

if __name__ == "__main__" :
    main()