tabMarque = ["audi", "mercedes", "bmw", "lamborghini" ,"porsche", "ferrari", "tesla"]
tabModele = ["R8","S5", "RS4","Q8","G63", "C63","SLS","M5", "X6", "aventador", "huracan", "urus", "macan", "911 GT3 RS", "458 italia", "F8 tributo", "model S", "model X"]
tabCouleur =  ["rouge", "bleu", "vert", "jaune", "noir", "gris", "blanc",]
tabNbPorte = [2, 4]

rouge_modele = ["S5", "SLS", "X6", "huracan", "911 GT3 RS", "458 italia", "F8 tributo", "model S"]
bleu_modele = ["huracan", "urus", "911 GT3 RS"]
vert_modele = ["aventador"]
jaune_modele = ["urus", "RS4", "G63", "F8 tributo"]
noir_modele = ["R8", "S5", "C63", "M5", "Macan", "model S", "model X"]
gris_modele = ["Q8", "C63", "G63", "Macan"]
blanc_modele = ["R8", "model X"]

class concess :
    def __init__(self, couleur, prix, marque, modele, puissance, nbPorte) :
        self.couleur = couleur
        self.prix = prix
        self.marque = marque
        self.modele = modele
        self.puissance = puissance
        self.nbPorte = nbPorte

if __name__ == "__main__":
    t = concess(couleur, prix, input("Choisissez une marque"),modele, puissance, nbporte)))
    if t.marque in tabMarque :
        t.couleur = input("Quelle couleur souhaitez vous ?")
    else :
        print("Nous n'avons pas de véhicule de cette marque dans la concession")
    if t.couleur in tabCouleur :
        t.nbPorte = int(input("Combien de porte vous faut-il")
    else :
        print("Nous n'avons pas de véhicule de cette couleur")
    if nbPorte in tabNbPorte :
        

