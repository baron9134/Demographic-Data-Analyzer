# Demographic-Data-Analyzer
Demographic Data Analyzer
# 📊 Demographic Data Analyzer

Ce projet fait partie du cursus de certification **Data Analysis with Python** proposé par [freeCodeCamp](https://www.freecodecamp.org/).

## 🎯 Objectif

L’objectif est d’analyser un ensemble de données démographiques provenant du recensement américain de 1994, en utilisant la bibliothèque **Pandas**, afin d'en extraire des statistiques significatives sur les catégories socio-professionnelles, l'éducation, le revenu, et plus encore.

## 📁 Fichiers

- `demographic_data_analyzer.py` : contient la fonction principale `calculate_demographic_data()` qui effectue les calculs demandés.
- `main.py` : fichier pour tester localement la fonction.
- `test_module.py` : tests unitaires utilisés pour vérifier la validité des résultats.
- `adult.data.csv` : fichier de données utilisé pour l’analyse (à placer dans le même dossier).

## 🔍 Données analysées

Les données incluent des colonnes comme :
- âge
- niveau d'éducation
- heures de travail par semaine
- profession
- pays d'origine
- salaire (`<=50K` ou `>50K`)

## ✅ Statistiques calculées

- Nombre de personnes par race
- Âge moyen des hommes
- Pourcentage de personnes titulaires d’un baccalauréat
- Pourcentage de personnes ayant fait des études supérieures et gagnant >50K
- Pourcentage de personnes sans études avancées gagnant >50K
- Nombre minimal d’heures travaillées par semaine
- Pourcentage de personnes travaillant ces heures minimales et gagnant >50K
- Pays avec le pourcentage le plus élevé de personnes gagnant >50K
- Métier le plus fréquent chez les personnes gagnant >50K en Inde

## 🧪 Lancer les tests

Pour exécuter les tests unitaires :

```bash
python3 test_module.py
