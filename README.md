# BML-Automate-Cellulaire

### Simulation d’une version modifiée du modèle BML – Automate Cellulaire pour la Modélisation du Trafic Routier

## 🎯 Objectif
L’objectif de ce projet est d’implémenter une simulation du modèle **BML (Biham-Middleton-Levine)**, un **automate cellulaire** qui modélise un système de trafic routier en tenant compte :
- Des priorités entre les véhicules.
- Des sorties possibles du réseau.

---

## 📌 Consignes

### 1️⃣ Définition de la grille
L'automate cellulaire est représenté par une **grille de cellules** où chaque cellule peut contenir une voiture :

- La grille est une matrice **N × N** où chaque case peut contenir :  
  - 🚗 **Voiture rouge (1)** : se déplace vers la **droite**.
  - 🚙 **Voiture bleue (2)** : se déplace vers le **bas**.
  - ⬜ **Case vide (0)** : représente une **route libre**.

🔹 **Règles de mouvement :**  
- Une voiture rouge qui atteint le **bord droit** quitte définitivement la grille.  
- Une voiture bleue qui atteint le **bord inférieur** quitte définitivement la grille.  

---

### 2️⃣ Initialisation de la grille
🛠️ Écrire une fonction qui initialise la grille avec :  
- Un **nombre égal** de voitures rouges et bleues.  
- Une **répartition aléatoire** des véhicules sur la grille.  
- Une **proportion de cases vides** pour permettre le mouvement des véhicules.  

---

### 3️⃣ Implémentation des règles de transition
⚙️ Les véhicules rouges sont **prioritaires** sur les bleus :  
- À chaque itération :  
  1. Les **voitures rouges** avancent en premier vers la **droite** si la case suivante est libre.  
  2. Ensuite, les **voitures bleues** avancent vers le **bas** si la case suivante est libre.  
- Lorsqu’un véhicule atteint le bord de la grille, il **quitte définitivement** le système.  

---

### 4️⃣ Exécution de la simulation
🖥️ **Écrire une fonction `main`** qui exécute la simulation avec :  
- Une **boucle d’itération** jusqu’à ce que toutes les voitures aient **quitté la grille**.  

---

### 5️⃣ Extraction des statistiques
📊 Après chaque itération, calculer :  
- 🚧 **Nombre de voitures bloquées** (véhicules ne pouvant pas avancer).  
- 🔄 **Nombre total d’itérations** nécessaires avant que la grille soit vide.  
- 📈 **Taux de sortie** des véhicules rouges et bleus à chaque itération.  
- 🚗 **Pourcentage de la grille** occupé par des véhicules restants.  

---

## 📌 TP Final
- **Module** : Python 🐍  
- **Filière** : GIGD  
- **Professeur** : EL BAKKAL Salma  
- **Année universitaire** : 2024/2025 🎓  

---

## 🚀 Installation et Exécution
### 1️⃣ Cloner le projet :
```bash
git clone https://github.com/elhassanemhd/BML-automate-cellulaire.git
cd BML-automate-cellulaire
