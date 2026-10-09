import donnees

# data = Dataset("appartements.csv")
# X_train, y_train, X_test, y_test = data.separer(0.8)

# modeles = [ModeleMoyenne(), RegressionLineaire(), KPlusProchesVoisins(k=3)]

# for m in modeles:
#     m.fit(X_train, y_train)
#     print(type(m).__name__, "→ erreur moyenne :", round(m.score(X_test, y_test), 1))

# print(modeles[1].predict([75]))   # prix estimé pour 75 m²

from donnees import Dataset

data = Dataset("appartements.csv")
X_train, y_train, X_test, y_test = data.separer(0.8)
print(len(data.X), data.y)
print(len(y_train), y_train)
#print(X_test, y_test)

from modeles import ModeleMoyenne

m = ModeleMoyenne()
m.fit(X_train, y_train)
print(m.moyenne)
print(m.predict([30, 75, 120]))
print(m.score(X_test, y_test))