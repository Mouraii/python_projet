import hashlib
import os
import pandas as pd

def hash_password(password, salt):
    """Hash le mot de passe avec un salt en utilisant SHA-256."""
    salted_password = password + salt
    return hashlib.sha256(salted_password.encode('utf-8')).hexdigest()

def save_to_csv(username, hashed_password, salt, filename='users.csv'):
    dossier_bdd = 'users_bdd'
    os.makedirs(dossier_bdd, exist_ok=True)
    filepath = os.path.join(dossier_bdd, filename)
    """Sauvegarde l'utilisateur, le mot de passe hashé et le salt dans un fichier CSV."""
    df = pd.DataFrame({'username': [username], 'hashed_password': [hashed_password], 'salt': [salt]})
    
    # Si le fichier existe déjà, on l'ajoute sans écraser les données existantes
    df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filepath), index=False)

def register(username, password, filename='users.csv'):
    """Fonction d'enregistrement d'un nouvel utilisateur."""
    print("### ENREGISTREMENT D'UN NOUVEL UTILISATEUR ###")
    
    # Demander le nom d'utilisateur et le mot de passe
    dossier_bdd = 'users_bdd'
    os.makedirs(dossier_bdd, exist_ok=True)
    filepath = os.path.join(dossier_bdd, filename)
    # Vérification si le fichier existe et s'il est lisible
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['username', 'hashed_password', 'salt'])  # Si le fichier n'existe pas encore
    
    # Vérification des colonnes
    print("Colonnes actuelles du fichier CSV : ", df.columns.tolist())  # Affiche les colonnes du fichier CSV pour vérifier
    
    # Si le fichier ne contient pas les colonnes attendues, on les crée manuellement
    if 'username' not in df.columns or 'hashed_password' not in df.columns or 'salt' not in df.columns:
        print("Le fichier CSV ne contient pas les colonnes nécessaires. Création de nouvelles colonnes.")
        df = pd.DataFrame(columns=['username', 'hashed_password', 'salt'])

    # Vérification si l'utilisateur existe déjà
    if username in df['username'].values:
        print("Le nom d'utilisateur existe déjà. Choisissez-en un autre.")
        return  # L'utilisateur existe déjà, sortir de la fonction

    # Générer un salt aléatoire (16 octets)
    salt = os.urandom(16).hex()

    # Hash du mot de passe avec le salt
    hashed_password = hash_password(password, salt)

    # Ajouter l'utilisateur dans le DataFrame
    new_user = pd.DataFrame({'username': [username], 'hashed_password': [hashed_password], 'salt': [salt]})

    # Vérifier si le fichier existe pour ajouter ou créer le header
    file_exists = os.path.exists(filepath)

    # Sauvegarder le DataFrame dans le fichier CSV
    new_user.to_csv(filepath, mode='a', header=not file_exists, index=False)
    
    print(f"Utilisateur {username} enregistré avec succès !")


def login(username, password,filename='users.csv'):
    """Fonction de connexion pour vérifier les informations d'un utilisateur."""
    while True:
        # Demander le nom d'utilisateur et le mot de passe
        dossier_bdd = 'users_bdd'
        os.makedirs(dossier_bdd, exist_ok=True)
        filepath = os.path.join(dossier_bdd, filename)
        
        # Charger le fichier CSV avec les utilisateurs enregistrés
        try:
            df = pd.read_csv(filepath)
        except FileNotFoundError:
            print("Le fichier des utilisateurs n'existe pas.")
            return False
        
        # Vérifier si l'utilisateur existe dans le fichier CSV
        if username in df['username'].values:
            # Récupérer les données de l'utilisateur (hash et salt)
            user_data = df[df['username'] == username].iloc[0]
            stored_hashed_password = user_data['hashed_password']
            salt = user_data['salt']
            
            # Hash du mot de passe fourni avec le salt
            hashed_password = hash_password(password, salt)
            
            # Vérifier si le mot de passe fourni correspond au hash stocké
            if hashed_password == stored_hashed_password:
                print("Connexion réussie !")
                dataconn = [True, username]
                return dataconn  # Connexion réussie
            else:
                print("Mot de passe incorrect.")
                continue  # Redemander les informations de connexion
        else:
            print("Nom d'utilisateur non trouvé.")
            continue  # Redemander les informations de connexion



def loginadmin(username, password,filename='base_admin.csv'):
    """Fonction de connexion pour vérifier les informations d'un utilisateur."""
    while True:
        # Demander le nom d'utilisateur et le mot de passe
        dossier_bdd = 'users_bdd'
        os.makedirs(dossier_bdd, exist_ok=True)
        filepath = os.path.join(dossier_bdd, filename)
        
        # Charger le fichier CSV avec les utilisateurs enregistrés
        try:
            df = pd.read_csv(filepath)
        except FileNotFoundError:
            print("Le fichier des utilisateurs n'existe pas.")
            return False
        
        # Vérifier si l'utilisateur existe dans le fichier CSV
        if username in df['username'].values:
            # Récupérer les données de l'utilisateur (hash et salt)
            user_data = df[df['username'] == username].iloc[0]
            stored_hashed_password = user_data['hashed_password']
            salt = user_data['salt']
            
            # Hash du mot de passe fourni avec le salt
            hashed_password = hash_password(password, salt)
            
            # Vérifier si le mot de passe fourni correspond au hash stocké
            if hashed_password == stored_hashed_password:
                print("Connexion réussie !")
                dataconn = [True, username]
                return dataconn  # Connexion réussie
            else:
                print("Mot de passe incorrect.")
                continue  # Redemander les informations de connexion
        else:
            print("Nom d'utilisateur non trouvé.")
            continue  # Redemander les informations de connexion