# BML-automate-cellulaire
TP Final
Module : Python
Filière : GIGD
Pr : EL BAKKAL Salma
Année universitaire 2024/2025
TP : Simulation d’une version modifiée modèle BML – Automate Cellulaire pour la 
Modélisation du Trafic Routier
Objectif
L’objectif de ce TP est d’implémenter une simulation du modèle BML (Biham-Middleton￾Levine), un automate cellulaire qui modélise un système de trafic routier en tenant compte 
des priorités entre les véhicules et des sorties possibles du réseau.
Consignes
1. Définition de la grille : automate cellulaire est une grille de cellule tel que chaque 
cellule est supposé de contenir une voiture
• La grille est une matrice N × N où chaque case peut contenir : 
o Une voiture rouge (1) : se déplace vers la droite.
o Une voiture bleue (2) : se déplace vers le bas.
o Une case vide (0) : représente une route libre.
• Pour le mouvement du véhicule nous avons les règles suivantes :
o Une voiture rouge qui atteint le bord droit quitte définitivement la grille.
o Une voiture bleue qui atteint le bord inférieur quitte définitivement la grille.
2. Initialisation de la grille
• Écrire une fonction qui initialise la grille avec : 
o Un nombre égal de voitures rouges et bleues.
o Une répartition aléatoire des véhicules sur la grille.
o Une proportion de cases vides pour permettre le mouvement des véhicules.
3. Implémentation des règles de transition
• Les véhicules rouges sont prioritaires sur les bleus : 
o À chaque itération, les voitures rouges avancent en premier vers la droite si 
la case suivante est libre.
o Ensuite, les voitures bleues avancent vers le bas si la case suivante est libre.
• Lorsqu’un véhicule atteint le bord de la grille, il quitte définitivement le système.
4. Exécution de la simulation
TP Final
Module : Python
Filière : GIGD
Pr : EL BAKKAL Salma
Année universitaire 2024/2025
• Écrire la fonction main qui exécute la simulation avec : 
o Une boucle d’itération jusqu’à ce que toutes les voitures aient quitté la 
grille.
5. Extraction des statistiques
Après chaque itération, calculer :
• Le nombre de voitures bloquées (véhicules ne pouvant pas avancer).
• Le nombre total d’itérations nécessaires avant que la grille soit vide.
• Le taux de sortie des véhicules rouges et bleus à chaque itération.
• Le pourcentage de la grille occupé par des véhicules restants.
