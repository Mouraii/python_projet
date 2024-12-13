
import csv



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




import hashlib
import os

# Fonction pour générer un hachage sécurisé avec un sel
def hash_password_with_salt(password: str, salt: str) -> str:
    # Ajouter le sel au mot de passe et le hacher avec SHA-256
    return hashlib.sha256((password + salt).encode()).hexdigest()

# Fonction pour générer un sel aléatoire
def generate_salt(length: int = 16) -> str:
    # Générer un sel aléatoire de 16 octets
    return os.urandom(length).hex()

# Exemple de base de données de hachages compromis (avec sel)
compromised_hashes = [
    '5e884898da28047151d0e56f8dc6292773603d0d1e3b8b7d5023f20f1e11a7b4',  # "password"
    '6cb75f652a9b52798ee8f9c7d4c9d4015c4c44db92ec18a9c169a64e73e87d6c',  # "123456"
    # Ajoutez d'autres hachages compromis ici
]

# Exemple d'utilisation
password_to_check = input("Entrez le mot de passe à vérifier : ")

# Génération d'un sel unique pour chaque mot de passe
salt = generate_salt()

# Vérification du mot de passe avec le sel
if check_password_compromised(password_to_check, salt):
    print("Ce mot de passe est compromis.")
else:
    print("Ce mot de passe n'est pas compromis.")


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


ajouter_utilisateur('ok', '123456')



