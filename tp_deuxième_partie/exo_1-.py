import csv

data = [
    ["Nom", "Age", "Note", "Adresse"],  # En-têtes de colonnes
    ["Alice", 22, 85, "Paris"],
    ["Bob", 23, 90, "Nantes"],
    ["Charlie", 21, 78, "Sarcelle"],
    ["Diane", 24, 92, "Tours"],
    ["Eve", 22, 88, "Nanterre"]
]

fichier_csv = 'fichier.csv' 

with open(fichier_csv,'w',newline='', encoding="utf-8") as fichier :
    writer = csv.writer(fichier)
    writer.writerows(data)

