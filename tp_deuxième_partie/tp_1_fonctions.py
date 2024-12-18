import os
import csv
import pandas as pd

### création de fichiers ###

def creer_fichier(username):
    # Créer le répertoire 'bdd' s'il n'existe pas
    dossier_bdd = 'bdd'
    os.makedirs(dossier_bdd, exist_ok=True)

    nom_fichier = os.path.join(dossier_bdd, f'produits_{username}.csv')
    
    # Vérification si le fichier existe déjà
    if os.path.exists(nom_fichier):
        print(f"Le fichier '{nom_fichier}' existe déjà.")
        return nom_fichier

    try:
        # Création du fichier CSV avec un en-tête
        with open(nom_fichier, "w", newline='', encoding="utf-8") as fichier:
            writer = csv.writer(fichier)
            writer.writerow(["nom", "prix", "stock"])  # Ajout des colonnes
            print(f"Fichier CSV '{nom_fichier}' créé avec succès.")
            return nom_fichier
    except Exception as e:
        print(f"Erreur lors de la création du fichier : {e}. Vérifiez que le fichier a une extension .csv")


### modifier une ligne précise ###



def modifier_ligne(username,ligne_a_modifier,nom,prix,stock):
    dossier_bdd = 'bdd'
    nom_fichier = os.path.join(dossier_bdd, f'produits_{username}.csv')
    try:
        # Lire le contenu du fichier CSV dans un DataFrame
        df = pd.read_csv(nom_fichier)

        # Vérification si le fichier est vide ou ne contient que l'en-tête
        if df.empty:
            print("Le fichier est vide ou ne contient que des en-têtes. Impossible de modifier des lignes.")
            return

        # Affichage des lignes existantes
        print("Contenu du fichier :")
        print(df)

        # Demande à l'utilisateur de choisir la ligne à modifier
        if ligne_a_modifier < 0 or ligne_a_modifier >= len(df):
            print("Numéro de ligne invalide.")
            return

        # Demande des nouvelles valeurs pour la ligne
        try:
            prix = float(prix)  # Validation pour prix
        except ValueError:
            print("Le prix doit être un nombre valide.")
            return

        # Modification de la ligne dans le DataFrame
        df.loc[ligne_a_modifier, 'nom'] = nom
        df.loc[ligne_a_modifier, 'prix'] = prix
        df.loc[ligne_a_modifier, 'stock'] = stock

        # Réécriture du fichier CSV avec les modifications
        df.to_csv(nom_fichier, index=False, encoding="utf-8")
        print("Ligne modifiée avec succès.")
    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de la modification : {e}")

### suppresion dans un fichier ###

def supprimer_dans_fichier(username, lignes_a_supprimer):
    dossier_bdd = 'bdd'
    nom_fichier = os.path.join(dossier_bdd, f'produits_{username}.csv')
    try:
        # Lecture du contenu du fichier CSV
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            reader = csv.reader(fichier)
            contenu = list(reader)  # Charger tout le contenu en mémoire

        # Vérification si le fichier est vide ou ne contient que des en-têtes
        if len(contenu) <= 1:
            print("Le fichier est vide ou ne contient que des en-têtes.")
            return False, "Le fichier est vide ou ne contient que des en-têtes."

        # Validation des indices à supprimer
        lignes_valides = range(len(contenu))
        lignes_a_supprimer = [int(x) for x in lignes_a_supprimer if int(x) in lignes_valides]

        if not lignes_a_supprimer:
            return False, "Aucune ligne valide à supprimer."

        # Supprimer les lignes spécifiées, mais conserver les en-têtes
        contenu_modifie = [ligne for i, ligne in enumerate(contenu) if i not in lignes_a_supprimer]

        # Réécriture du fichier avec les lignes restantes
        with open(nom_fichier, "w", newline='', encoding="utf-8") as fichier:
            writer = csv.writer(fichier)
            writer.writerows(contenu_modifie)

        return True, "Lignes supprimées avec succès."
    except FileNotFoundError:
        return False, f"Le fichier '{nom_fichier}' n'existe pas."
    except ValueError:
        return False, "Veuillez entrer des numéros valides pour les lignes à supprimer."
    except Exception as e:
        return False, f"Erreur lors de la suppression : {e}"

### ecrire à la fin d'un fichier ###

def ecrire_a_la_fin(username,nom,prix,stock):
    dossier_bdd = 'bdd'
    nom_fichier = os.path.join(dossier_bdd, f'produits_{username}.csv')
    try:
        # Vérifier si le fichier existe déjà
        fichier_existe = os.path.exists(nom_fichier)

        # Si le fichier existe, charger son contenu, sinon créer une DataFrame vide
        if fichier_existe:
            df = pd.read_csv(nom_fichier)
        else:
            df = pd.DataFrame(columns=["nom", "prix", "stock"])

        # Demander les informations à ajouter

        try:
            prix = float(prix)
        except ValueError:
            print("Le prix doit être un nombre valide.")
            return

        # Ajouter les données dans la DataFrame
        nouvelle_ligne = pd.DataFrame([{"nom": nom, "prix": prix, "stock": stock}])
        df = pd.concat([df, nouvelle_ligne], ignore_index=True)

        # Sauvegarder dans le fichier CSV
        df.to_csv(nom_fichier, index=False)

        print("Données ajoutées avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout : {e}")




### Lire les fichiers ###


def lire_fichier(username):
    dossier_bdd = 'bdd'
    nom_fichier = os.path.join(dossier_bdd, f'produits_{username}.csv')
    try:
        # Lecture du fichier CSV avec pandas
        df = pd.read_csv(nom_fichier)

        # Vérification si le fichier est vide
        if df.empty:
            print("Le fichier est vide.")
        else:
            print("Contenu du fichier :")
            print(df.to_string(index=False))  # Affiche le contenu de manière lisible

    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")

### Recherche
def rechercher(username):
    # Demander à l'utilisateur d'entrer le nom du fichier et le produit à rechercher
    dossier_bdd = 'bdd'
    nom_fichier = os.path.join(dossier_bdd, f'produits_{username}.csv')
    nom_recherche = input("Entrez le nom de l'article à rechercher : ").strip().lower()

    # Demander à l'utilisateur de choisir le type de recherche
    print("Choisissez le type de recherche :")
    print("1. Recherche par nom (linéaire)")
    print("2. Recherche dichotomique")
    choix = input("Entrez le numéro de votre choix (1 ou 2) : ")

    if choix not in ["1", "2"]:
        print("Choix invalide. Veuillez entrer 1 ou 2.")
        return

    try:
        # Charger le fichier CSV dans un DataFrame
        df = pd.read_csv(nom_fichier)

        # Vérifier si le fichier contient des données
        if df.empty:
            print("Le fichier est vide.")
            return

        # Vérifier que la colonne "nom" existe
        if "nom" not in df.columns:
            print("Le fichier ne contient pas de colonne 'nom'.")
            return

        # Recherche par nom (linéaire)
        if choix == "1":
            # Filtrer les lignes qui contiennent le nom recherché
            resultats = df[df['nom'].str.lower().str.contains(nom_recherche, na=False)]
            if resultats.empty:
                print(f"Aucun article trouvé avec le nom '{nom_recherche}'.")
            else:
                print("Articles trouvés :")
                print(resultats)

        # Recherche dichotomique (nécessite tri préalable)
        elif choix == "2":
            # Vérifier que les données sont triées par nom
            df = df.sort_values(by="nom", key=lambda col: col.str.lower())

            # Effectuer une recherche dichotomique
            position = pd.Index(df['nom'].str.lower()).get_loc(nom_recherche, method='nearest')

            # Vérifier si le résultat trouvé correspond au nom recherché
            if nom_recherche in df.iloc[position]['nom'].lower():
                print("Article trouvé :")
                print(df.iloc[[position]])
            else:
                print(f"Aucun article trouvé avec le nom '{nom_recherche}'.")

    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de la recherche : {e}")
### tri à bulle ###

def tri_csv_logic(username, critere, type_tri):
    """Logique pour trier un fichier CSV et retourner le contenu trié."""
    dossier_bdd = 'bdd'
    nom_fichier = os.path.join(dossier_bdd, f'produits_{username}.csv')

    if not os.path.exists(nom_fichier):
        raise FileNotFoundError(f"Le fichier '{nom_fichier}' n'existe pas.")

    # Charger le fichier CSV
    df = pd.read_csv(nom_fichier)

    if df.empty:
        raise ValueError("Le fichier est vide, aucun tri à effectuer.")

    if critere not in ['prix', 'stock']:
        raise ValueError(f"Critère de tri invalide : '{critere}'.")

    if type_tri == 'rapide':
        # Utilisation du tri intégré de pandas
        df = df.sort_values(by=critere, ascending=True)
    elif type_tri == 'bulle':
        # Implémentation du tri à bulle
        n = len(df)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if df.iloc[j][critere] > df.iloc[j + 1][critere]:
                    df.iloc[j], df.iloc[j + 1] = df.iloc[j + 1], df.iloc[j]
    else:
        raise ValueError("Type de tri invalide. Choisissez 'rapide' ou 'bulle'.")

    # Sauvegarder le fichier trié
    df.to_csv(nom_fichier, index=False)

    return df  # Retourner le DataFrame trié
