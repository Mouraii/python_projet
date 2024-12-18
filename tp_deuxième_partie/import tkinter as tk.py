import tkinter as tk
from tkinter import messagebox
from tp_1_fonctions import *  # Importation des fonctions externes
from hashage import *

def inscrire():
    """Affiche les champs pour l'inscription."""
    # Effacer les widgets existants
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Inscription", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Nom d'utilisateur:", font=("Arial", 12)).pack(pady=5)
    username_entry = tk.Entry(root, font=("Arial", 12))
    username_entry.pack(pady=5)

    tk.Label(root, text="Mot de passe:", font=("Arial", 12)).pack(pady=5)
    password_entry = tk.Entry(root, font=("Arial", 12), show="*")
    password_entry.pack(pady=5)

    def valider_inscription():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:
            register(username, password)
            messagebox.showinfo("Inscription", "Inscription réussie !")
            ouvrir_menu_principal()
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

    tk.Button(root, text="Valider", font=("Arial", 14), command=valider_inscription).pack(pady=10)
    tk.Button(root, text="Retour", font=("Arial", 14), command=ouvrir_menu_principal).pack(pady=5)

def se_connecter():
    """Affiche les champs pour la connexion."""
    # Effacer les widgets existants
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Connexion", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Nom d'utilisateur:", font=("Arial", 12)).pack(pady=5)
    username_entry = tk.Entry(root, font=("Arial", 12))
    username_entry.pack(pady=5)

    tk.Label(root, text="Mot de passe:", font=("Arial", 12)).pack(pady=5)
    password_entry = tk.Entry(root, font=("Arial", 12), show="*")
    password_entry.pack(pady=5)

    def valider_connexion():
        username = username_entry.get()
        password = password_entry.get()
        conn = login(username, password)
        if conn[0]:
            messagebox.showinfo("Connexion réussie", f"Bienvenue {conn[1]} !")
            creer_fichier(conn[1])
            ouvrir_menu_gestion(conn)
        else:
            messagebox.showerror("Erreur", "Connexion échouée. Vérifiez vos identifiants.")

    tk.Button(root, text="Valider", font=("Arial", 14), command=valider_connexion).pack(pady=10)
    tk.Button(root, text="Retour", font=("Arial", 14), command=ouvrir_menu_principal).pack(pady=5)

def connexionadmin():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Connexion Au pannel admin", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Nom d'utilisateur:", font=("Arial", 12)).pack(pady=5)
    username_entry = tk.Entry(root, font=("Arial", 12))
    username_entry.pack(pady=5)

    tk.Label(root, text="Mot de passe:", font=("Arial", 12)).pack(pady=5)
    password_entry = tk.Entry(root, font=("Arial", 12), show="*")
    password_entry.pack(pady=5)

    def valider_connexion():
        username = username_entry.get()
        password = password_entry.get()
        conn = loginadmin(username, password)
        if conn[0]:
            messagebox.showinfo("Connexion réussie", f"Bienvenue {conn[1]} !")
            creer_fichier(conn[1])
            ouvrir_menu_gestion(conn)
        else:
            messagebox.showerror("Erreur", "Connexion échouée. Vérifiez vos identifiants, votre tentative de connexion a été enregistré dans le cas d'une tentative d'infraction.")

    tk.Button(root, text="Valider", font=("Arial", 14), command=valider_connexion).pack(pady=10)
    tk.Button(root, text="Retour", font=("Arial", 14), command=ouvrir_menu_principal).pack(pady=5)



def modifier_ligne_ui(username):
    """Affiche l'interface pour modifier une ligne."""
    # Effacer les widgets existants
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Modifier une ligne", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Numéro de ligne:", font=("Arial", 12)).pack(pady=5)
    ligne_entry = tk.Entry(root, font=("Arial", 12))
    ligne_entry.pack(pady=5)

    tk.Label(root, text="Nom de l'article:", font=("Arial", 12)).pack(pady=5)
    nom_entry = tk.Entry(root, font=("Arial", 12))
    nom_entry.pack(pady=5)

    tk.Label(root, text="Prix de l'article:", font=("Arial", 12)).pack(pady=5)
    prix_entry = tk.Entry(root, font=("Arial", 12))
    prix_entry.pack(pady=5)

    tk.Label(root, text="Unité de stock:", font=("Arial", 12)).pack(pady=5)
    stock_entry = tk.Entry(root, font=("Arial", 12))
    stock_entry.pack(pady=5)

    def valider_modification():
        try:
            ligne = int(ligne_entry.get()) - 1
            nom = nom_entry.get()
            prix = float(prix_entry.get())
            stock = stock_entry.get()
            modifier_ligne(username, ligne, nom, prix, stock)
            messagebox.showinfo("Succès", "Ligne modifiée avec succès.")
            ouvrir_menu_gestion((True, username))
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

    tk.Button(root, text="Valider", font=("Arial", 14), command=valider_modification).pack(pady=10)
    tk.Button(root, text="Retour", font=("Arial", 14), command=lambda: ouvrir_menu_gestion((True, username))).pack(pady=5)

def supprimer_dans_fichier_ui(username):
    """Affiche l'interface pour supprimer des lignes."""
    """Affiche l'interface pour supprimer des lignes."""
    # Effacer les widgets existants
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Supprimer des lignes", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Numéros des lignes à supprimer (séparés par des virgules):", font=("Arial", 12)).pack(pady=5)
    lignes_entry = tk.Entry(root, font=("Arial", 12))
    lignes_entry.pack(pady=5)

    def valider_suppression():
        try:
            lignes = [int(x.strip()) for x in lignes_entry.get().split(",")]
            success, message = supprimer_dans_fichier(username, lignes)
            if success:
                messagebox.showinfo("Succès", message)
                ouvrir_menu_gestion((True, username))
            else:
                messagebox.showerror("Erreur", message)
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des numéros valides ou vérifier que les lignes existent.")

    tk.Button(root, text="Valider", font=("Arial", 14), command=valider_suppression).pack(pady=10)
    tk.Button(root, text="Retour", font=("Arial", 14), command=lambda: ouvrir_menu_gestion((True, username))).pack(pady=5)

def ecrire_a_la_fin_ui(username):
    """Affiche l'interface pour ajouter un produit au fichier."""
    # Effacer les widgets existants
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Ajouter un produit", font=("Arial", 20, "bold")).pack(pady=10)

    tk.Label(root, text="Nom de l'article:", font=("Arial", 12)).pack(pady=5)
    nom_entry = tk.Entry(root, font=("Arial", 12))
    nom_entry.pack(pady=5)

    tk.Label(root, text="Prix de l'article:", font=("Arial", 12)).pack(pady=5)
    prix_entry = tk.Entry(root, font=("Arial", 12))
    prix_entry.pack(pady=5)

    tk.Label(root, text="Unité de stock:", font=("Arial", 12)).pack(pady=5)
    stock_entry = tk.Entry(root, font=("Arial", 12))
    stock_entry.pack(pady=5)

    def valider_ajout():
        try:
            nom = nom_entry.get()
            prix = float(prix_entry.get())
            stock = stock_entry.get()
            ecrire_a_la_fin(username, nom, prix, stock)
            messagebox.showinfo("Succès", "Produit ajouté avec succès.")
            ouvrir_menu_gestion((True, username))
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

    tk.Button(root, text="Valider", font=("Arial", 14), command=valider_ajout).pack(pady=10)
    tk.Button(root, text="Retour", font=("Arial", 14), command=lambda: ouvrir_menu_gestion((True, username))).pack(pady=5)
    
def tri_csv_ui(username):
    """Interface graphique pour trier un fichier CSV avec rendu en temps réel."""
    # Effacer les widgets existants
    for widget in root.winfo_children():
        widget.destroy()

    # Titre
    tk.Label(root, text="Tri des Produits", font=("Arial", 20, "bold")).pack(pady=10)

    # Cadres pour organiser les widgets
    main_frame = tk.Frame(root)
    main_frame.pack(pady=20)

    options_frame = tk.Frame(main_frame)
    options_frame.grid(row=0, column=0, padx=10)

    result_frame = tk.Frame(main_frame)
    result_frame.grid(row=0, column=1, padx=10)

    action_frame = tk.Frame(root)
    action_frame.pack(pady=10)

    # Variables pour les critères et les types de tri
    critere_var = tk.StringVar(value="prix")
    type_tri_var = tk.StringVar(value="rapide")

    # Critères de tri (Radio boutons)
    tk.Label(options_frame, text="Critères de tri :", font=("Arial", 14)).pack(anchor="w", pady=5)
    tk.Radiobutton(options_frame, text="Prix", variable=critere_var, value="prix", font=("Arial", 12)).pack(anchor="w")
    tk.Radiobutton(options_frame, text="Stock", variable=critere_var, value="stock", font=("Arial", 12)).pack(anchor="w")

    # Types de tri (Radio boutons)
    tk.Label(options_frame, text="Types de tri :", font=("Arial", 14)).pack(anchor="w", pady=5)
    tk.Radiobutton(options_frame, text="QuickSort (Rapide)", variable=type_tri_var, value="rapide", font=("Arial", 12)).pack(anchor="w")
    tk.Radiobutton(options_frame, text="Bubble Sort (Bulle)", variable=type_tri_var, value="bulle", font=("Arial", 12)).pack(anchor="w")

    # Zone pour afficher le contenu trié
    tk.Label(result_frame, text="Contenu Trié :", font=("Arial", 14)).pack(anchor="w", pady=5)
    text_widget = tk.Text(result_frame, font=("Arial", 12), wrap="none", width=50, height=20)
    text_widget.pack()

    def afficher_contenu(df):
        """Met à jour le rendu en temps réel avec le contenu trié."""
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", df.to_string(index=False))

    def valider_tri():
        """Effectue le tri en fonction des choix sélectionnés et met à jour l'affichage."""
        critere = critere_var.get()
        type_tri = type_tri_var.get()
        try:
            df = tri_csv_logic(username, critere, type_tri)  # Appelle la fonction logique
            afficher_contenu(df)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du tri : {e}")

    # Boutons Submit et Retour
    tk.Button(action_frame, text="Submit", font=("Arial", 14), command=valider_tri).grid(row=0, column=0, padx=10)
    tk.Button(action_frame, text="Retour", font=("Arial", 14), command=lambda: ouvrir_menu_gestion((True, username))).grid(row=0, column=1, padx=10)

def rechercher_ui(username):
    """Affiche l'interface pour rechercher un produit et affiche le résultat avec son index."""
    # Effacer les widgets existants
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Rechercher un produit", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Nom du produit à rechercher:", font=("Arial", 12)).pack(pady=5)
    produit_entry = tk.Entry(root, font=("Arial", 12))
    produit_entry.pack(pady=5)

    # Zone pour afficher les résultats
    result_text = tk.Text(root, height=10, width=50, font=("Arial", 12))
    result_text.pack(pady=10)

    def valider_recherche():
        produit = produit_entry.get().strip().lower()
        if not produit:
            messagebox.showerror("Erreur", "Veuillez entrer un nom de produit.")
            return

        dossier_bdd = 'bdd'
        nom_fichier = os.path.join(dossier_bdd, f'produits_{username}.csv')
        try:
            # Charger le fichier CSV
            df = pd.read_csv(nom_fichier)

            if df.empty or "nom" not in df.columns:
                messagebox.showerror("Erreur", "Le fichier est vide ou mal formaté.")
                return

            # Recherche des correspondances
            resultats = df[df['nom'].str.lower() == produit]
            if resultats.empty:
                result_text.delete("1.0", tk.END)
                result_text.insert(tk.END, f"Aucun article trouvé pour '{produit}'.")
            else:
                # Afficher les résultats et l'index des lignes
                result_text.delete("1.0", tk.END)
                result_text.insert(tk.END, f"Articles trouvés pour '{produit}':\n\n")
                for index, row in resultats.iterrows():
                    # Format du message sans guillemets et accolades
                    ligne = f"Ligne {index + 1} - Nom: {row['nom']}, Prix: {row['prix']}, Stock: {row['stock']}\n"
                    result_text.insert(tk.END, ligne)
        except FileNotFoundError:
            messagebox.showerror("Erreur", f"Fichier '{nom_fichier}' introuvable.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la recherche : {e}")

    # Boutons pour valider ou retourner au menu principal
    tk.Button(root, text="Rechercher", font=("Arial", 14), command=valider_recherche).pack(pady=10)
    tk.Button(root, text="Retour", font=("Arial", 14), command=lambda: ouvrir_menu_gestion((True, username))).pack(pady=5)


def quitter():
    """Quitte l'application."""
    if messagebox.askyesno("Quitter", "Êtes-vous sûr de vouloir quitter ?"):
        root.destroy()

def ouvrir_menu_principal():
    """Affiche le menu principal."""
    # Effacer les widgets existants
    for widget in root.winfo_children():
        widget.destroy()

    # Afficher les options du menu principal
    tk.Label(root, text="### MENU PRINCIPAL ###", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="1. S'inscrire", font=("Arial", 14), command=inscrire).pack(pady=5)
    tk.Button(root, text="2. Se connecter", font=("Arial", 14), command=se_connecter).pack(pady=5)
    tk.Button(root, text="3. Pannel Admin", font=("Arial", 14), command=connexionadmin).pack(pady=5)
    tk.Button(root, text="4. Quitter", font=("Arial", 14), command=quitter).pack(pady=5)
    

def ouvrir_menu_gestion(conn):
    """Affiche le menu de gestion après connexion."""
    # Effacer les widgets existants
    for widget in root.winfo_children():
        widget.destroy()

    username = conn[1]

    def executer_action(selection):
        if selection == 1:
            creer_fichier(username)
            messagebox.showinfo("Création", "Fiche de stock créée.")
        elif selection == 2:
            modifier_ligne_ui(username)
        elif selection == 3:
            supprimer_dans_fichier_ui(username)
        elif selection == 4:
            ecrire_a_la_fin_ui(username)
        elif selection == 5:
            lire_fichier(username)
            messagebox.showinfo("Lecture", "Contenu affiché dans la console.")
        elif selection == 6:
            tri_csv_ui(username)
            messagebox.showinfo("Tri", "Fichier trié avec succès.")
        elif selection == 7:
            rechercher_ui()
        elif selection == 8:
            ouvrir_menu_principal()
        else:
            messagebox.showerror("Erreur", "Choix invalide.")

    # Afficher les options du menu de gestion
    tk.Label(root, text="### MENU DE GESTION ###", font=("Arial", 16)).pack(pady=10)

    options = [
        "1. Création de fiche de stock",
        "2. Modification de fiche de stock",
        "3. Supprimer un produit de la fiche de stock",
        "4. Ajouter un produit au stock",
        "5. Lire une fiche de stock",
        "6. Trier une fiche de stock",
        "7. Rechercher un produit dans un stock",
        "8. Quitter le menu de gestion",
    ]

    for i, option in enumerate(options, start=1):
        tk.Button(
            root, text=option, font=("Arial", 14), command=lambda i=i: executer_action(i)
        ).pack(pady=5)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Gestion de Stock")
root.geometry("600x400")

# Lancer le menu principal
ouvrir_menu_principal()

# Boucle principale Tkinter
root.mainloop()
