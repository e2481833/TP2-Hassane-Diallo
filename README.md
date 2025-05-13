# Gestionnaire de Tournoi

## Membres de l'équipe

- Nom : Hassane
- Matricule : e2481833

## Description du projet

Ce projet est une application en Python permettant de gérer un tournoi de jeux vidéo. Il permet de :

- Créer un tournoi
- Charger des joueurs depuis un fichier CSV
- Charger des matchs depuis un fichier CSV
- Saisir les scores des matchs
- Afficher le classement
- Sauvegarder les résultats en JSON
- Générer un rapport texte

## Instructions d'exécution

1. Assurez-vous d'avoir Python installé.
2. Placez les fichiers `joueurs.csv` et `matchs.csv` dans un dossier `data/`.
3. Lancez le programme avec la commande suivante :

```bash
python main.py
Suivez les instructions à l'écran.

Format des fichiers
joueurs.csv
csv
Copier
Modifier
pseudo,age
PlayerOne,18
PlayerTwo,19
PlayerThree,18
PlayerFour,20
matchs.csv
csv
Copier
Modifier
joueur1,joueur2
PlayerOne,PlayerTwo
PlayerThree,PlayerFour
PlayerOne,PlayerThree
PlayerTwo,PlayerFour