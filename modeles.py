class Modele :
    def __init__(self):
        self.entraine = False 

    def fit(self, X, y):
        raise NotImplementedError("fit doit être definie dans la classe enfant")
    
    def predict(self, X) :
        raise NotImplementedError("predict doit être definie dans la classe enfant")

    def score(self, X, y): 
        predictions = self.predict(X)

        ecarts = []
        for p,vrai in zip(predictions,y) :
            ecarts.append(abs(p - vrai))

        return sum(ecarts) / len(ecarts)

class ModeleMoyenne(Modele) : 
    def fit(self, X, y):
        self.moyenne = sum(y)/len(y)
        self.entraine = True

    def predict(self, X): 
        return [self.moyenne for x in X ]

class RegressionLineaire(Modele):
    def fit(self,X,y):
        moy_x = sum(X) / len(X)
        moy_y = sum(y) / len(y)
        numerateur = sum((x - moy_x) * (yi - moy_y) for x, yi in zip(X,y))
        denominateur = sum((x - moy_x)**2 for x in X)

        self.a = numerateur / denominateur
        self.b = moy_y - self.a * moy_x

        self.entraine = True

    def predict(self, X): 
        return [self.a * x + self.b for x in X]

class KPlusProchesVoisins(Modele):
    def __init__(self,k=3):
        super().__init__()
        self.k = k

    def fit(self, X, y): 
        self.donnees = list(zip(X,y))
        self.entraine = True 

    def predict(self, X):
        predictions = []
        for x in X :
            tries = sorted(self.donnees, key=lambda p : abs(p[0]-x))
            voisins = tries[:self.k]
            moyenne = sum(p[1] for p in voisins) / len(voisins)
            predictions.append(moyenne)
        return predictions