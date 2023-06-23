# README - Projet IA

Ce fichier README fournit des instructions simples pour exécuter notre projet IA. Suivez ces étapes pour démarrer rapidement avec le projet.

## Installation

1. **Clonez** le référentiel du projet sur votre machine locale.
   ```
   git clone <lien_vers_le_référentiel>
   ```

2. **Accédez** au répertoire du projet.
   ```
   cd <nom_du_répertoire>
   ```

## Exécution

1. Les étapes à suivre pour exécuter le projet :
  - Accéder au fichier `scriptApprentissageSuperviseKnn.py`
  - Lancer le script de la manière suivante : `py knn_script.py [chemin_fichier_csv_entrainement] [chemin fichier_csv_donnee_a_predire]` (le second fichier peut contenir une liste des accidents à prédire.)
  - Le script va renvoyer en sortie dictionnaire qui contiendra la prédiction obtenu à travers le modèle.
---
  - Lancer le script de la manière suivante : `py kmeans_script.py [latitude] [longitude] [centroides.csv]` (latitude et longitude doivent être des float. centroides.csv est un fichier csv regroupant les latitudes et longitudes de différents centroïdes)
  - Le script va renvoyer en sortie un objet JSON qui contient la latitudes et la longitudes de l'accident initial et la latitude et la longitude du cluster prédit auquel il appartient
---
   - Lancer le script de la manière suivante : `py script_classification_haut_niveau.py [chemin_fichier_csv_repertoriant_un_accident] [methode_utilisee]` (la méthode utilisée est, au choix, SVM, RF, ou MLP.)
   - Le script va renvoyer en sortie un objet JSON contenant la gravité de l'accident prédite ainsi que les informations de l'accident.
   - ATTENTION ! Assurez-vous d'avoir dans votre répertoire courant les différents modèles entraînés.
---
C'est tout ! Vous devriez maintenant pouvoir exécuter notre projet IA en suivant les étapes mentionnées ci-dessus. Bonne utilisation !
