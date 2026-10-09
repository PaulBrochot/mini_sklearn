import csv 
import random 

class Dataset :
    def __init__(self,chemin):
        self.X = []
        self.y= []
        with open (chemin, newline="",encoding="utf-8") as f: 
            for ligne in csv.DictReader(f):
                self.X.append(float(ligne["surface"]))
                self.y.append(float(ligne["prix"]))

    def separer (self,ratio):
        paires = list(zip(self.X,self.y))
        random.shuffle(paires)
        coupure = int(len(paires)*ratio)
        train = paires[:coupure]
        test = paires[coupure:]
        X_train = [p[0] for p in train]
        y_train =[p[1] for p in test]
        X_test = [p[0]for p in test]
        y_test = [p[1] for p in test]
        return X_train, y_train, X_test, y_test