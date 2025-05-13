# utils.py

import csv
import json

def lire_csv(chemin):
    with open(chemin, newline='', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier)
        return list(lecteur)

def sauvegarder_json(data, chemin):
    with open(chemin, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def ecrire_texte(contenu, chemin):
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write(contenu)
