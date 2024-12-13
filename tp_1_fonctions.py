import os
import pandas
import csv
import hashlib
import bcrypt
### création de fichiers ###

def creer_fichier():
    nom_fichier = input("Entrez le nom du fichier (avec extension .txt) : ")

    # Vérification si le fichier existe déjà
    if os.path.exists(nom_fichier):
        print(f"Le fichier '{nom_fichier}' existe déjà.")
        choix = input("Voulez-vous le remplacer ? (oui/non) : ").strip().lower() 
        if choix != 'oui':
            print("Annulation de la création du fichier.")
            
            return
        else:
            print("Le fichier sera remplacé.")

    try:
        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            print(f"Fichier '{nom_fichier}' créé avec succès.")   # crée le fichier puis indique qu'il à été crée. Il le crée grace au parametre 'w' qui crée un fichier si celui-ci n'existe pas
    except Exception as e:
        print(f"Erreur lors de la création du fichier : {e}, faites attention à mettre le .txt à la fin")
    
    

### modifier une ligne précise ###



def modifier_ligne():
    nom_fichier = input("Entrez le nom du fichier à modifier : ")  # Demande du fichier
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()  # Préparation de l'énumération des lignes

        # Vérification si le fichier est vide
        if not lignes:
            print("Le fichier est vide. Impossible de modifier des lignes.")
            return

        # Affichage de toutes les lignes du fichier
        for i, ligne in enumerate(lignes):
            print(f"{i + 1}: {ligne.strip()}")

        # Demande à l'utilisateur de choisir la ligne à modifier
        ligne_a_modifier = int(input("Entrez le numéro de la ligne à modifier : ")) - 1  # Choix de la ligne à modifier
        if 0 <= ligne_a_modifier < len(lignes):
            # Demande du nom, prix et stock
            nom = input("Entrez le nom de l'article : ")
            try:
                prix = float(input("Entrez le prix de l'article : "))  # Convertir l'entrée en float pour le prix
            except ValueError:
                print("Le prix doit être un nombre valide.")
                return  # Arrête la fonction si l'entrée n'est pas un nombre valide

            stock = input("Entrez l'unité de stock (ex : 'pcs', 'kg') : ")

            # Formatage des données sous forme de ('nom','prix','unité')
            nouveau_contenu = f"('{nom}','{prix}','{stock}')"

            # Remplacement de la ligne
            lignes[ligne_a_modifier] = nouveau_contenu + "\n"

            # Réécriture du fichier avec la ligne modifiée
            with open(nom_fichier, "w", encoding="utf-8") as fichier:
                fichier.writelines(lignes)
            print("Ligne modifiée avec succès.")
        else:
            print("Numéro de ligne invalide.")  # Si le numéro est invalide, ce message s'affichera
    except Exception as e:
        print(f"Erreur lors de la modification : {e}")  # Message d'erreur général, suivi du message spécifique d'exception

### suppresion dans un fichier ###

def supprimer_dans_fichier():
    nom_fichier = input("Entrez le nom du fichier : ")
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            contenu = fichier.readlines()

        print("Contenu actuel du fichier :")
        for i, ligne in enumerate(contenu):
            print(f"{i + 1}: {ligne.strip()}")

        lignes_a_supprimer = input("Entrez les numéros des lignes à supprimer (séparés par des virgules) : ")
        indices_a_supprimer = [int(x.strip()) - 1 for x in lignes_a_supprimer.split(",")]

        contenu_modifie = [ligne for i, ligne in enumerate(contenu) if i not in indices_a_supprimer]

        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            fichier.writelines(contenu_modifie)
        print("Lignes supprimées avec succès.")
    except Exception as e:
        print(f"Erreur lors de la suppression : {e}")
    

### ecrire à la fin d'un fichier ###

def ecrire_a_la_fin():
    nom_fichier = input("Entrez le nom du fichier : ")
    try:
        with open(nom_fichier, "a", encoding="utf-8") as fichier:
            # Demander à l'utilisateur de saisir le nom, prix et unités
            nom = input("Entrez le nom de l'article : ")
            try:
                prix = float(input("Entrez le prix de l'article : "))  # Convertir l'entrée en float pour le prix
            except ValueError:
                print("Le prix doit être un nombre valide.")
                return  # Arrête la fonction si l'entrée n'est pas un nombre valide

            stock = input("Entrez l'unité de stock (ex : 'pcs', 'kg') : ")

            # Formatage des données sous forme de ('nom','prix','unité')
            nouveau_contenu = f"('{nom}','{prix}','{stock}')"

            # Ajouter le nouveau contenu à la fin du fichier
            fichier.write(nouveau_contenu + "\n")
        print("Texte ajouté avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout : {e}")



### Lire les fichiers ###


def lire_fichier():
    nom_fichier = input("Entrez le nom du fichier à lire : ")
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            contenu = fichier.readlines()  # Lecture de toutes les lignes du fichier

        # Vérification si le fichier est vide
        if not contenu:
            print("Le fichier est vide.")
        else:
            print("Contenu du fichier :")
            for ligne in contenu:
                print(ligne.strip())  # Affiche chaque ligne sans les espaces ou sauts de ligne supplémentaires

    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")


### Recherche
def rechercher():
    # Demander à l'utilisateur d'entrer le nom du fichier et le nom du produit une seule fois
    nom_fichier = input("Entrez le nom du fichier à rechercher : ").strip()
    nom_recherche = input("Entrez le nom de l'article à rechercher : ").strip().lower()

    # Demander à l'utilisateur de choisir le type de recherche
    print("Choisissez le type de recherche :")
    print("1. Recherche par nom")
    print("2. Recherche dichotomique")
    choix = input("Entrez le numéro de votre choix (1 ou 2) : ")

    if choix not in ["1", "2"]:
        print("Choix invalide. Veuillez entrer 1 ou 2.")
        return

    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            contenu = fichier.readlines()  # Lire toutes les lignes du fichier

        # Transformer chaque ligne du fichier en tuple (nom, prix, quantité)
        donnees = []
        for ligne in contenu:
            # Chaque ligne devrait être formatée comme "nom, prix, quantité" (séparée par des virgules)
            elements = ligne.strip().split(", ")
            if len(elements) == 3:
                nom_produit = elements[0].strip().lower()  # Enlever les espaces et convertir en minuscule
                try:
                    prix = float(elements[1])
                    quantite = int(elements[2])
                    donnees.append((nom_produit, prix, quantite))  # Ajouter le tuple dans la liste
                except ValueError:
                    continue  # Ignore les lignes mal formatées

        if choix == "1":  # Recherche par nom (linéaire)
            article_trouve = False
            for i, ligne in enumerate(contenu):
                # Recherche insensible à la casse et espaces enlevés
                if nom_recherche in ligne.strip().lower():  
                    print(f"Ligne {i + 1}: {ligne.strip()}")  # Afficher le numéro et le contenu de la ligne
                    article_trouve = True

            if not article_trouve:
                print(f"Aucun article trouvé avec le nom '{nom_recherche}'.")

        elif choix == "2":  # Recherche dichotomique avec tri par sélection
            def lire_produits_depuis_fichier(nom_fichier):
                produits = []
                try:
                    with open(nom_fichier, 'r') as fichier:
                        for index, ligne in enumerate(fichier, start=1):  # Utilisation de enumerate pour obtenir l'index
                            ligne = ligne.strip()
                            if ligne:  # Vérifie que la ligne n'est pas vide
                                # Supprimer les parenthèses et couper la ligne en trois parties
                                ligne = ligne.strip('()')
                                parties = ligne.split(',')

                                # Extraire le nom, le prix et la quantité
                                nom = parties[0].strip().strip("'")  # Enlever les espaces et les guillemets autour du nom
                                prix = parties[1].strip().strip("'")  # Enlever les espaces et les guillemets autour du prix
                                quantite = int(parties[2].strip())  # Quantité est un entier

                                # Ajouter le produit à la liste avec son index
                                produits.append(((nom, prix, quantite), index))  # On garde une référence à l'index
                except FileNotFoundError:
                    print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
                return produits

            # Fonction de recherche dichotomique
            def recherche_dichotomique(liste, nom_recherche):
                # Trier la liste des produits par le nom en ignorant la casse et les espaces excédentaires
                liste.sort(key=lambda x: x[0][0].lower().strip())  # Tri des produits en fonction du nom

                # Initialiser les indices pour la recherche dichotomique
                bas = 0
                haut = len(liste) - 1

                # Boucle de recherche
                while bas <= haut:
                    milieu = (bas + haut) // 2
                    produit, index = liste[milieu]
                    nom_milieu = produit[0].lower().strip()  # Conversion en minuscules et suppression des espaces

                    # Comparaison insensible à la casse et nettoyée des espaces
                    if nom_milieu == nom_recherche.lower().strip():  
                        # Trouvé, retourner l'élément avec son index
                        return produit, index
                    elif nom_milieu < nom_recherche.lower().strip():
                        # Recherche dans la moitié droite
                        bas = milieu + 1
                    else:
                        # Recherche dans la moitié gauche
                        haut = milieu - 1

                # Si le produit n'est pas trouvé
                return None, None

            # Lecture des produits depuis le fichier
            produits = lire_produits_depuis_fichier(nom_fichier)

            # Si des produits ont été lus depuis le fichier, effectuer la recherche
            if produits:
                # Recherche du produit
                produit_trouve, ligne_trouvee = recherche_dichotomique(produits, nom_recherche)

                # Affichage du résultat sans apostrophes
                if produit_trouve:
                    # Affichage du résultat formaté sans apostrophes et ligne où il a été trouvé
                    nom, prix, quantite = produit_trouve
                    print(f"Produit trouvé : Nom: {nom}, Prix: {prix}, Quantité: {quantite}")
                    print(f"Ce produit a été trouvé à la ligne {ligne_trouvee} du fichier.")
                else:
                    print("Produit non trouvé")
            else:
                print("Aucun produit trouvé dans le fichier.")

    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")


### tri à bulle ###

def extraire_prix(ligne):
    """Fonction pour extraire le prix d'une ligne sous forme de tuple"""
    try:
        # Supposons que les lignes sont dans le format ('nom', 'prix', 'quantité')
        elements = ligne.strip().strip("()").split(", ")
        prix = float(elements[1].strip("'"))  # On extrait et nettoie le prix
        return prix
    except (IndexError, ValueError):
        # En cas d'erreur, retourner une valeur par défaut (par exemple 0.0)
        print(f"Erreur lors de l'extraction du prix pour la ligne : {ligne}")
        return 0.0


def extraire_quantite(ligne):
    """Extraire la quantité d'une ligne sous forme de tuple"""
    try:
        # On enlève les parenthèses et divise par les virgules
        elements = ligne.strip().strip("()").split(", ")
        quantite = int(elements[2].strip("'"))  # La quantité est le troisième élément
        return quantite
    except (IndexError, ValueError):
        print(f"Erreur lors de l'extraction de la quantité pour la ligne : {ligne}")
        return 0

def tri_a_bulle_par_prix(lignes):
    """Tri les lignes par prix (croissant) à l'aide du tri à bulle"""
    n = len(lignes)
    for i in range(n):
        for j in range(0, n - i - 1):
            prix_j = extraire_prix(lignes[j])
            prix_j1 = extraire_prix(lignes[j + 1])

            # Si le prix de j est supérieur à celui de j + 1, on échange les lignes
            if prix_j > prix_j1:
                lignes[j], lignes[j + 1] = lignes[j + 1], lignes[j]
    
    return lignes

def tri_a_bulle_par_quantite(lignes):
    """Tri les lignes par quantité à l'aide du tri à bulle"""
    n = len(lignes)
    for i in range(n):
        for j in range(0, n - i - 1):
            quantite_j = extraire_quantite(lignes[j])
            quantite_j1 = extraire_quantite(lignes[j + 1])

            if quantite_j > quantite_j1:
                lignes[j], lignes[j + 1] = lignes[j + 1], lignes[j]
    return lignes

def trier_fichier():
    """Fonction qui trie un fichier par prix ou quantité, en fonction de l'input de l'utilisateur"""
    nom_fichier = input("Entrez le nom du fichier à trier : ")

    # Demander à l'utilisateur de choisir le critère de tri
    critere = input("Entrez le critère de tri ('prix' ou 'quantite') : ").strip().lower()

    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()
        
        if critere == "prix":
            lignes_triees = tri_a_bulle_par_prix(lignes)
        elif critere == "quantite":
            lignes_triees = tri_a_bulle_par_quantite(lignes)
        else:
            print("Critère de tri invalide. Utilisation du tri par prix par défaut.")
            lignes_triees = tri_a_bulle_par_prix(lignes)

        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            fichier.writelines(lignes_triees)
        
        print(f"Fichier trié par {critere} avec succès.")
    except Exception as e:
        print(f"Erreur lors du tri du fichier : {e}")


### tri rapide ###


def trier_fichier_rapide():
    # Fonction pour partitionner les éléments autour d'un pivot
    def partitionner(tableau, bas, haut, indice_tri):
        pivot = tableau[haut][indice_tri]  # Le pivot est l'élément à l'index 'haut' du critère choisi
        i = bas - 1  # Index pour le plus petit élément
        for j in range(bas, haut):
            # Si l'élément courant est inférieur ou égal au pivot, échangez-le avec l'élément à l'index 'i'
            if tableau[j][indice_tri] <= pivot:
                i += 1
                tableau[i], tableau[j] = tableau[j], tableau[i]
        # Place le pivot à la bonne position
        tableau[i + 1], tableau[haut] = tableau[haut], tableau[i + 1]
        return i + 1

    # Fonction de tri rapide (QuickSort)
    def tri_rapide(tableau, bas, haut, indice_tri):
        if bas < haut:
            # Partitionne le tableau et obtient la position du pivot
            pi = partitionner(tableau, bas, haut, indice_tri)
            # Trie récursivement les sous-tableaux
            tri_rapide(tableau, bas, pi - 1, indice_tri)
            tri_rapide(tableau, pi + 1, haut, indice_tri)

    # Demande à l'utilisateur le fichier à trier
    nom_fichier = input("Entrez le nom du fichier à trier : ")
    try:
        # Lit le contenu du fichier
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            contenu = fichier.readlines()

        produits = []
        for ligne in contenu:
            # Nettoie la ligne et extrait les données
            ligne = ligne.strip().strip("()")
            elements = ligne.split(", ")
            nom = elements[0].strip("'")
            try:
                prix = float(elements[1].strip("'"))  # Convertit le prix en float
                stock = int(elements[2].strip("'").strip())  # Convertit la quantité en entier
            except ValueError:
                print(f"Ligne ignorée : {ligne}")
                continue
            produits.append((nom, prix, stock))  # Ajoute le produit comme un tuple

        # Demande le critère de tri à l'utilisateur avec validation
        while True:
            critere = input("Souhaitez-vous trier par prix (1) ou par quantité (2) ? : ").strip()
            if critere in ("1", "2"):
                indice_tri = 1 if critere == "1" else 2
                break  # Quitte la boucle si l'entrée est valide
            else:
                print("Choix invalide. Veuillez entrer 1 pour le prix ou 2 pour la quantité.")

        # Effectue le tri rapide
        tri_rapide(produits, 0, len(produits) - 1, indice_tri)

        # Écrit les produits triés dans le fichier
        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            for produit in produits:
                fichier.write(f"('{produit[0]}', '{produit[1]:.2f}', {produit[2]})\n")

        print("Fichier trié avec succès.")

    except Exception as e:
        print(f"Erreur : {e}")





def ajouter_utilisateur(nom_utilisateur, mdp_utilisateur, nom_fichier='base_de_donnees.csv'):
    # Vérifie si l'utilisateur existe déjà
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            if ligne.strip().startswith(f"'{nom_utilisateur}'"):
                print('Utilisateur déjà existant.')
                return
    with open(nom_fichier, 'a', newline='', encoding='utf-8') as fichier:
            writer = csv.writer(fichier)
            writer.writerow([nom_utilisateur, mdp_utilisateur])
            print(f'Utilisateur {nom_utilisateur} ajouté avec succès.')





mots_de_passe = [
"123456",
"password",
"123456789",
"12345",
"12345678",
"qwerty",
"abc123",
"password123",
"123123",
"welcome",
"letmein",
"monkey",
"1234",
"1q2w3e4r",
"iloveyou",
"123321",
"qwertyuiop",
"sunshine",
"princess",
"123qwe",
"qazwsx",
"trustno1",
"admin",
"welcome123",
"123abc",
"football",
"123abc123",
"qwerty123",
"letmein123",
"shadow",
"1234qwer",
"password1",
"1qaz2wsx",
"qwerty1",
"superman",
"12345qwerty",
"starwars",
"123qaz",
"football123",
"1q2w3e4r5t",
"freedom",
"iloveyou123",
"dragon",
"abcdef",
"monkey123",
]


def hash_password(password):
    salt = bcrypt.gensalt()  # Génère un sel aléatoire
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)  # Hache le mot de passe avec le sel
    return hashed


def check_password_authentification(stored_hash, password):
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash)  # Vérifie le mot de passe avec le hachage stocké


def authenticate_user(nom_utilisateur, mdp_utilisateur, nom_fichier='base_de_donnees.csv'):
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        for line in fichier:
            user_info = line.strip().split(',')
            if user_info[0] == f"'{nom_utilisateur}'":
                stored_hash = user_info[1]
                if check_password_authentification(stored_hash, mdp_utilisateur):
                    print('Authentification réussie.')
                    return True
    print('Authentification échouée.')
    return False

