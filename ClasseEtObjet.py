### Classes et Objets ###

class carre :
    def __init__(self, cote, perimeter,facteur, count) :
        self.cote = cote
        self.perimeter = self.cote * 4
        self.area = self.area()
        self.facteur = self.area * facteur
        
    
    def area(self):
        return self.cote * self.cote
        

if __name__ == "__main__":
    t = carre(5,0,2,0)
    print(t.perimeter)
    print(t.area)
    print("Le carré à un côté d'une longueur de", t.cote,", une aire de", t.area,", et un périmètre de,",t.perimeter,".")
    print(t.facteur)

class carre2 :
    def __init__(self, cote2, perimeter2,facteur2) :
        self.cote2 = cote2
        self.perimeter2 = self.cote2 * 4
        self.area2 = self.area2()
        self.facteur2 = self.area2 * facteur2
    
    def area2(self):
        return self.cote2 * self.cote2
if __name__ == "__main__":

    r = carre2(1,0,2)
    print(r.perimeter2)
    print(r.area2)
    print("Le carré à un côté d'une longueur de", r.cote2,", une aire de", r.area2,", et un périmètre de,",r.perimeter2,".")
    print(r.facteur2)
    print("le périmètre des 2 carrés est de :",t.perimeter + r.perimeter2)
    print("la soustraction des périmètres des 2 carrés est de :",t.perimeter - r.perimeter2)


if (t.perimeter < r.perimeter2) == True :
    print("Le carré 2 est plus grand que le 1")
else :
    print("Le carré 1 est >= que le carré 2")

class count :
  
