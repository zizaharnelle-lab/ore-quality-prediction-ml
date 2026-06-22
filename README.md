# Ore Quality Prediction — Machine Learning

## Contexte
Projet de Data Science appliqué à la métallurgie extractive.
Ce modèle prédit automatiquement la qualité d'échantillons de minerai
de manganèse à partir de données d'analyse XRF (fluorescence X),
en s'appuyant sur des critères réels utilisés en laboratoire minier.

## Problématique
La classification manuelle de la qualité des minerais est chronophage
et dépend de l'interprétation humaine. Ce projet automatise cette
décision grâce au Machine Learning.

## Classification de qualité
- **Haute qualité** : Mn >= 43%
- **Moyenne qualité** : 38% <= Mn < 43%
- **Basse qualité** : Mn < 38%

## Dataset
- 800 échantillons simulés basés sur des paramètres XRF réels
- Variables : Mn_pct (manganèse %), Fe_pct (fer %)
- Outil de génération : src/generate_data.py

## Structure du projet
- data/raw/ : dataset brut (raw_data.csv)
- src/ : scripts Python
- notebooks/ : exploration et modélisation
- models/ : modèles entraînés
- requirements.txt : dépendances Python

## Installation
git clone https://github.com/zizaharnelle-lab/ore-quality-prediction-ml.git
cd ore-quality-prediction-ml
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

## Statut
En cours — Semaine 1 : génération du dataset terminée

## Auteur
Yeno Ziza Harnelle Layis
Ingénieure Métallurgiste | Superviseure Laboratoire | IA & Data Science
Franceville, Gabon
