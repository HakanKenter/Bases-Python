# -*- coding: utf-8 -*-

class Personne:
    #Le constructeur es tla fonction qui est appelée 
    #à chaque fois que l'on fait appel à une classe (instance de cette classe)
    #le premier paramètre, self, représente l'objet
    #qui vient d'être créé
    def __init__(self,nom):
        self.nom = nom
        self.argent = 0

    #méthode qui permet de représenter l'objet
    #à l'aide d'une str
    def __repr__(self):
        return "Je m'appelle "+self.nom
    
    def presente_toi(self):
        print("Bonjour, je m'appelle",self.nom,"et je possède",self.argent,"€")

    #méthode pour donner de l'argent à 
    #une autre personne
    def donne(self,autre,montant):
        self.argent -= montant
        autre.argent += montant
    
personne1 = Personne('hakan')
print(personne1.nom)

personne2 = Personne('Toto')
print(personne2.nom)

print(personne1) #appel automatiquement la méthode __repr__
print(personne2)

personne1.argent+=1000
personne1.presente_toi()
personne2.presente_toi()

personne1.donne(personne2,100)
personne1.presente_toi()
personne2.presente_toi()

#Héritage (dérivation)
class Salarie(Personne):
    def __init__(self, nom, employeur):
        #on appel le constructeur de la classe mère
        super().__init__(nom)
        #on définit les attributs spécifiques de la classe
        #fille
        self.employeur = employeur

    def __repr__(self):
        return "Salarie "+self.nom
    
    def salaire(self, montant):
        self.argent += montant


salarie1 = Salarie("hakan","Raphael")
print(salarie1.nom)
print(salarie1.employeur)
salarie1.presente_toi()
print()

salarie1.salaire(2000)
salarie1.presente_toi()

class Clone(Personne):
    def __init__(self):
        super().__init__("Toto")

clone1=Clone()
clone2=Clone()
clone1.presente_toi()
clone2.presente_toi()
print()

clone1.donne(clone2,10)
clone1.presente_toi()
clone2.presente_toi()
print()