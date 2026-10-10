import random

from donnees import Dataset
from modeles import ModeleMoyenne, RegressionLineaire, KPlusProchesVoisins

# Fixe le hasard 
random.seed(42)

# 1. Charger et séparer les données
data = Dataset("appartements.csv")
X_train, y_train, X_test, y_test = data.separer(0.8)

# 2. Créer les modèles
modeles = [ModeleMoyenne(), RegressionLineaire(), KPlusProchesVoisins(k=3)]

# 3. Entraîner et évaluer chaque modèle
print("=== Erreur moyenne sur le jeu de test ===")
for m in modeles:
    m.fit(X_train, y_train)
    print(type(m).__name__, "→", round(m.score(X_test, y_test), 1), "k€")

# 4. Prédire le prix d'un appartement de 75 m² avec chaque modèle
print("\n=== Prix estimé pour 75 m² ===")
for m in modeles:
    print(type(m).__name__, "→", round(m.predict([75])[0], 1), "k€")