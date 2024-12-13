import csv
import hashlib
import os
import tkinter as tk
from tkinter import messagebox


# Fonction pour générer un hachage sécurisé avec un sel
def hash_password_with_salt(password: str, salt: str) -> str:
    # Ajouter le sel au mot de passe et le hacher avec SHA-256
    return hashlib.sha256((password + salt).encode()).hexdigest()


# Fonction pour générer un sel aléatoire
def generate_salt(length: int = 16) -> str:
    # Générer un sel aléatoire de 16 octets
    return os.urandom(length).hex()


# Fonction pour ajouter un utilisateur à la base de données CSV
def ajouter_utilisateur(nom_utilisateur, mdp_utilisateur, nom_fichier='base_de_donnees.csv'):
    # Vérifie si l'utilisateur existe déjà
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            if ligne.strip().startswith(f"'{nom_utilisateur}'"):
                print('Utilisateur déjà existant.')
                return
    # Génération d'un sel unique pour l'utilisateur
    salt = generate_salt()
    # Hachage du mot de passe avec le sel
    hashed_password = hash_password_with_salt(mdp_utilisateur, salt)
    # Enregistrement de l'utilisateur dans le fichier CSV
    with open(nom_fichier, 'a', newline='', encoding='utf-8') as fichier:
        writer = csv.writer(fichier)
        writer.writerow([nom_utilisateur, hashed_password, salt])
        print(f'Utilisateur {nom_utilisateur} ajouté avec succès.')


# Fonction pour vérifier si le mot de passe est compromis
def check_password_compromised(password: str, salt: str) -> bool:
    # Liste des hachages compromis (exemples)
    compromised_hashes = [
        '5e884898da28047151d0e56f8dc6292773603d0d1e3b8b7d5023f20f1e11a7b4',  # "password"
        '6cb75f652a9b52798ee8f9c7d4c9d4015c4c44db92ec18a9c169a64e73e87d6c',  # "123456"
    ]
    hashed_password = hash_password_with_salt(password, salt)
    return hashed_password in compromised_hashes


# Fonction pour vérifier le mot de passe de l'utilisateur
def login_user(nom_utilisateur, mdp_utilisateur):
    with open('base_de_donnees.csv', 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            # Séparation des informations
            utilisateur, hashed_password, salt = ligne.strip().split(',')
            if utilisateur == nom_utilisateur:
                salt = salt.strip()
                if check_password_compromised(mdp_utilisateur, salt):
                    return False  # Mot de passe compromis
                hashed_password_input = hash_password_with_salt(mdp_utilisateur, salt)
                if hashed_password_input == hashed_password:
                    return True  # Connexion réussie
    return False  # Utilisateur ou mot de passe incorrect


# Interface graphique Tkinter pour l'enregistrement et la connexion
class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Page de Connexion")
        self.geometry("400x400")
        self.config(bg="#f5f5f5")  # Couleur de fond moderne

        # Ajout de la police et de styles
        self.title_font = ("Helvetica", 18, "bold")
        self.label_font = ("Helvetica", 12)
        self.entry_font = ("Helvetica", 12)
        self.button_font = ("Helvetica", 12, "bold")

        # Titre de la fenêtre
        self.title_label = tk.Label(self, text="Se connecter", font=self.title_font, bg="#f5f5f5", fg="#4a4a4a")
        self.title_label.pack(pady=20)

        # Champs de saisie pour le nom d'utilisateur
        self.username_label = tk.Label(self, text="Nom d'utilisateur:", font=self.label_font, bg="#f5f5f5", fg="#4a4a4a")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self, font=self.entry_font, width=30, bd=2, relief="solid")
        self.username_entry.pack(pady=10)

        # Champs de saisie pour le mot de passe
        self.password_label = tk.Label(self, text="Mot de passe:", font=self.label_font, bg="#f5f5f5", fg="#4a4a4a")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self, show="*", font=self.entry_font, width=30, bd=2, relief="solid")
        self.password_entry.pack(pady=10)

        # Boutons de connexion et d'inscription
        self.login_button = tk.Button(self, text="Se connecter", font=self.button_font, bg="#4CAF50", fg="white", width=20, height=2, command=self.login)
        self.login_button.pack(pady=10)

        self.register_button = tk.Button(self, text="S'inscrire", font=self.button_font, bg="#2196F3", fg="white", width=20, height=2, command=self.register)
        self.register_button.pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if login_user(username, password):
            messagebox.showinfo("Connexion", f"Bienvenue {username} !")
            self.show_main_menu()
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Vérification si l'utilisateur existe déjà
        with open('base_de_donnees.csv', 'r', encoding='utf-8') as fichier:
            for ligne in fichier:
                if ligne.strip().startswith(f"'{username}'"):
                    messagebox.showerror("Erreur", "Utilisateur déjà existant")
                    return

        # Ajouter l'utilisateur
        ajouter_utilisateur(username, password)
        messagebox.showinfo("Enregistrement", "Utilisateur enregistré avec succès")

    def show_main_menu(self):
        self.clear_window()

        # Menu principal après la connexion réussie
        tk.Label(self, text="### Menu de Gestion ###", font=("Helvetica", 14, "bold"), bg="#f5f5f5", fg="#4a4a4a").pack(pady=20)

        tk.Button(self, text="1. Création de fichiers", font=self.button_font, bg="#FF9800", fg="white", width=20, height=2, command=self.create_file).pack(pady=10)
        tk.Button(self, text="2. Modification de fichier", font=self.button_font, bg="#FF5722", fg="white", width=20, height=2, command=self.modify_file).pack(pady=10)
        tk.Button(self, text="3. Supprimer des données", font=self.button_font, bg="#f44336", fg="white", width=20, height=2, command=self.delete_data).pack(pady=10)
        tk.Button(self, text="4. Quitter", font=self.button_font, bg="#607d8b", fg="white", width=20, height=2, command=self.quit).pack(pady=10)

    def clear_window(self):
        # Efface les widgets de la fenêtre actuelle
        for widget in self.winfo_children():
            widget.destroy()

    def create_file(self):
        print("Création de fichiers")

    def modify_file(self):
        print("Modification de fichier")

    def delete_data(self):
        print("Suppression de données")


# Démarrer l'application Tkinter
if __name__ == "__main__":
    app = Application()
    app.mainloop()
