
import csv
import hashlib




def ajouter_utilisateur(nom_utilisateur, mdp_utilisateur, nom_fichier='base_de_donnees.csv'):
    # Vérifie si l'utilisateur existe déjà
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            for line in fichier:
                # Vérifie si le nom d'utilisateur existe déjà dans le fichier
                if line.strip().split(',')[0] == nom_utilisateur:
                    print('Utilisateur déjà existant.')
                    return
    except FileNotFoundError:
        # Si le fichier n'existe pas, nous n'avons pas d'utilisateur pour le moment
        pass

    # Si l'utilisateur n'existe pas, ajoutons-le
    with open(nom_fichier, 'a', newline='', encoding='utf-8') as fichier:
        writer = csv.writer(fichier)
        writer.writerow([nom_utilisateur, mdp_utilisateur])
        print(f"Utilisateur {nom_utilisateur} ajouté avec succès.")


ajouter_utilisateur('user1', 'password1')



def mettre_a_jour_utilisateur(nom_utilisateur, nouveau_mdp, nom_fichier='base_de_donnees.csv'):
    utilisateurs = []
    utilisateur_trouve = False
    
    # Lire toutes les lignes du fichier CSV
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            lecteur = csv.reader(fichier)
            for ligne in lecteur:
                if ligne[0] == nom_utilisateur:
                    ligne[1] = nouveau_mdp  # Mise à jour du mot de passe
                    utilisateur_trouve = True
                utilisateurs.append(ligne)
    except FileNotFoundError:
        print("Le fichier n'existe pas.")
        return

    # Si l'utilisateur a été trouvé, réécrire le fichier avec les modifications
    if utilisateur_trouve:
        with open(nom_fichier, 'w', newline='', encoding='utf-8') as fichier:
            writer = csv.writer(fichier)
            writer.writerows(utilisateurs)
            print(f"Le mot de passe de {nom_utilisateur} a été mis à jour.")
    else:
        print("Utilisateur non trouvé.")

mettre_a_jour_utilisateur('user1', '123')









def supprimer_utilisateur(nom_utilisateur, nom_fichier='base_de_donnees.csv'):
    utilisateurs = []
    utilisateur_trouve = False
    
    # Lire toutes les lignes du fichier CSV
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            lecteur = csv.reader(fichier)
            for ligne in lecteur:
                if ligne[0] != nom_utilisateur:
                    utilisateurs.append(ligne)  # Conserver les utilisateurs qui ne sont pas à supprimer
                else:
                    utilisateur_trouve = True
    except FileNotFoundError:
        print("Le fichier n'existe pas.")
        return
    
    # Si l'utilisateur a été trouvé, réécrire le fichier sans cet utilisateur
    if utilisateur_trouve:
        with open(nom_fichier, 'w', newline='', encoding='utf-8') as fichier:
            writer = csv.writer(fichier)
            writer.writerows(utilisateurs)
            print(f"Utilisateur {nom_utilisateur} supprimé avec succès.")
    else:
        print("Utilisateur non trouvé.")







