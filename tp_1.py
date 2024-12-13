from tp_1_fonctions import *  # Importation des fonctions externes
import tkinter as tk

def menu_selectif():
    while True:
        # Affichage du menu
        print('###  MENU DE GESTION  ###\n Choix possibles :\n        1. Création de fichiers\n        2. Modification de fichier\n        3. Supprimer des données\n        4. Ecriture dans un fichier\n        5. Lire un fichier txt\n        6. Trier un fichier \n        7. Rechercher une information\n        8. Quitter le programme')

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
            modifier_ligne()
        elif selection == 3:
            supprimer_dans_fichier()

        elif selection == 4:
            ecrire_a_la_fin()
        elif selection == 5:
            lire_fichier()
        elif selection == 6:
            choix_tri_1 = int(input('quel type de tri souhaitez vous ?\n          1.Tri rapide\n          2.tri à bulle\n    votre choix : '))
            if choix_tri_1 == 2:
                trier_fichier()
            elif choix_tri_1 == 1:
                trier_fichier_rapide()

        elif selection == 7:
            rechercher()
            

        elif selection == 8:
            print("Très bien, bonne journée")
            break  # Sortie de la boucle, donc fin du programme


menu_selectif()