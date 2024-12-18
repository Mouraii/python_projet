from tp_1_fonctions import *  # Importation des fonctions externes
from hashage import *


def menu_selectif():
    """Affiche le menu de gestion après une connexion ou une inscription réussie."""
    while True:
        print("### MENU PRINCIPAL ###")
        print("Choisissez une option :")
        print("1. S'inscrire (Créer un nouveau compte)")
        print("2. Se connecter")
        print("3. Quitter")

        try:
            selection = int(input('Votre sélection : '))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if selection == 1:
            register()  # Appelle la fonction d'inscription
            continue  # Retourne au menu principal après l'inscription

        elif selection == 2:
            # Tentative de connexion
            conn = login()
            if conn[0]:
                print(f"Bienvenue dans le menu de gestion {conn[1]}.")
                # Une fois connecté, on entre dans le menu de gestion
                creer_fichier(conn[1])
                gestion_menu(conn)
                
                return conn  # Sort de la boucle une fois connecté et dans le menu de gestion

        elif selection == 3:
            print("Au revoir !")
            break  # Quitter le programme

        else:
            print("Choix invalide. Veuillez choisir une option valide.")

def gestion_menu(conn):
    while True:
        # Affichage du menu
        print('###  MENU DE GESTION  ###\n Choix possibles :\n        1. Création de fiche de stock\n        2. Modification de fiche de stock\n        3. Supprimer un produit de la fiche de stock\n        4. ajouter un produit au stock\n        5. Lire une fiche de stock \n        6. Trier une fiche de stock \n        7. Rechercher un produit dans un stock\n        8. Quitter le programme')

        try:
            selection = int(input('Votre sélection :   '))  # Demande de choix
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue  # Retourner au début de la boucle si l'entrée est invalide

        # Vérification de la validité du choix
        if selection not in [1, 2, 3, 4, 5, 6, 7, 8]:
            print('Votre choix doit se situer entre 1 et 8')
            continue  # Retourne au début de la boucle en cas de choix invalide

        # Exécution de l'action en fonction du choix de l'utilisateur
        if selection == 1:
            creer_fichier()
        elif selection == 2:
            modifier_ligne(conn[1])
        elif selection == 3:
            supprimer_dans_fichier(conn[1])

        elif selection == 4:
            ecrire_a_la_fin(conn[1])
        elif selection == 5:
            lire_fichier(conn[1])
        elif selection == 6:
            tri_csv_logic(conn[1])

        elif selection == 7:
            rechercher(conn[1])
            

        elif selection == 8:
            print("Très bien, bonne journée")
            break  # Sortie de la boucle, donc fin du programme


menu_selectif()