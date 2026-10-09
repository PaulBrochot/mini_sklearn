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
