# Exercices MEDADOM 

## Description du Projet

Ce répertoire est composé de deux exercices.

- Une analyse exploratoire approfondie d'un jeu de données portant sur le revenu d'une population d'adultes. L'objectif est de découvrir des insights intéressants sur les facteurs socio-économiques qui influencent le revenu, ainsi que d'explorer les relations et corrélations entre différentes caractéristiques démographiques.
- Une fonction python qui consiste à transformer un fichier excel d'horaires en une matrice de 0 et 1 dans les heures travaillées.

## Structure du Projet
- **assets :** Le dossier contenant les fichiers du sujet sur lesquels les exercices sont basés.
    - **adult.csv :** Le dataset à analyser lors de la partie 1 au format csv.
    - **algo_test.xlsx :** Le fichier d'entrée de la fonction python de la partie 2.
- **part1_exercise :** Le dossier contenant le rendu de l'exercice 1 : l'analyse exploratoire du jeu de données.
    - **MEDADOM_exercises_part1.ipynb :** Le fichier du premier exercice. Il contient toutes les analyses, visualisations et interprétations.
    - **MEDADOM_exercises_part1.html :** Le fichier du premier exercice. Il s'agit du même que le précédent au format html. Il n'est utile que dans le cas où le fichier au format `.ipynb` est inaccessible.
- **part2_exercise :** Le dossier contenant le rendu de l'exercice 2 : la fonction python au format `.py`.
    - **MEDADOM_exercises_part2.py :** Le fichier du deuxième exercice. Il contient tout le code commenté.
- **requirements :** Dossier contenant les fichiers listants toutes les dépendances nécessaires pour exécuter chaque partie.
    - **part1_requirements :** Fichier contenant toutes les dépendances nécessaires à la partie 1 : l'analyse exploratoire
    -**part2_requirements :** Fichier contenant toutes les dépendances nécessaires à la partie 2 : la fonction python

## Installation et Configuration
Pour exécuter le notebook, vous devez avoir Python installé sur votre machine ainsi que Jupyter Notebook ou JupyterLab. Assurez-vous également d'avoir les paquets nécessaires installés. Pour installer les dépendances, exécutez la commande suivante dans votre terminal à la racine du projet :

```bash
pip install -r requirements/part1_requirements.txt
```

Cette commande installera tous les paquets requis pour l'exécution du notebook, tels que définis dans le fichier `part1_requirements.txt`.

De même, pour exécuter le fichier python du deuxième exercice, vous aurez besoin des pacquets nécessaires. Pour les installer, exécutez la commande suivante dans votre terminal à la racine du projet :
```bash
pip install -r requirements/part2_requirements.txt
```

## Exécution du Notebook
Après avoir installé les dépendances, ouvrez Jupyter Notebook ou JupyterLab et naviguez jusqu'au fichier `MEDADOM_exercices_part1.ipynb` pour lancer l'analyse. Le fichier devrait déjà être compilé et prêt à être lu.

## Exécution du fichier Python (Exercice 2)
Après avoir installé les dépendances, vous pourrez exécuter ce fichier avec la commande suivante :
```bash
python part_2_exercise/MEDADOM_exercises_part2.py path_to_your_input_file
```

Par exemple, pour exécuter le code avec le fichier donné dans le sujet, placez-vous à la racine et entrez la commande suivante :
```bash
python part_2_exercise/MEDADOM_exercises_part2.py assets/algo_test.xlsx
```

Une fois le programme exécuté, un fichier `Output.xlsx` se créera dans votre répértoire. Il s'agira de la matrice créée par le programme exportée au format Excel.

Attention, conformément aux consignes que j'ai reçu, le programme ne se lancera que si la feuille de l'excel qui contient l'input est nommée `Input`.

## Remarques

L'output que j'ai pour l'exercice 2 est légèrement différent de l'output cible défini dans la feuille `Output` du fichier Excel. Selon moi, on y trouve une erreur. On y voit un 1 dans la case de lundi à horaire = 18 (de 18h à 19h) pour Robert. Hors, les horaires de travail de Robert lundi doivent être 8h-18h (et non 8h-19h).