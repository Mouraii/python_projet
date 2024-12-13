
import csv
import bcrypt


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



def check_password_authentification(stored_hash, mdp_utilisateur):
    return bcrypt.checkpw(mdp_utilisateur.encode('utf-8'), stored_hash)  # Vérifie le mot de passe avec le hachage stocké

def verifier_hash_compromis(hachage_utilisateur, fichier_compromis='hash_compromis.csv'):
    try:
        with open(fichier_compromis, 'r', encoding='utf-8') as f:
            # Lire tous les hachages compromis dans le fichier
            hachages_compromis = f.read().splitlines()  # Chaque ligne correspond à un hachage
            if hachage_utilisateur in hachages_compromis:
                return True
    except FileNotFoundError:
        print(f"Le fichier {fichier_compromis} est introuvable.")
    return False

# Fonction d'authentification
def authenticate_user(nom_utilisateur, mdp_utilisateur, nom_fichier='base_de_donnees.csv'):
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        for line in fichier:
            user_info = line.strip().split(',')
            if user_info[0].strip("'") == nom_utilisateur:  # Vérifier le nom d'utilisateur
                stored_hash = user_info[1].encode('utf-8')  # Convertir le hachage stocké en bytes
                if bcrypt.checkpw(mdp_utilisateur.encode('utf-8'), stored_hash):  # Vérification du mot de passe
                    print(f"Authentification réussie pour {nom_utilisateur}.")
                    
                    # Vérification si le hachage est compromis
                    if verifier_hash_compromis(stored_hash.decode('utf-8')):  # Comparer avec la base de données de hachages compromis
                        print(f"Attention : Le mot de passe de l'utilisateur {nom_utilisateur} a été compromis !")
                    return True
                else:
                    print(f"Mot de passe incorrect pour {nom_utilisateur}.")
                    return False
    print(f"Utilisateur {nom_utilisateur} non trouvé.")
    return False
def check_csv_format(nom_fichier='base_de_donnees.csv'):
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        for line in fichier:
            print(line.strip())  # Affiche chaque ligne pour vérifier le format



password = [
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


ajouter_utilisateur('drg', 'drg')