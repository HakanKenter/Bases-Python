# -*- coding: utf-8 -*-

#on définit une fonction avec le mot-clé def
#suivi du nom de la fonction et des éventuels paramètres

#Exemples : fonction qui prend en paramètre un nombre
#et qui renvoie son carré

def carre(a):
    #le mot clé return termine la fonction
    #et renvoi la valeur à sa droite
    return a**2

#on appelle la fonction carre
c = carre(5)
print(c)


'''_________________________________________________________________________________________________________________________________________'''


#Une fonction peut avoir un ou plusieurs paramètres, ou aucun

#Renvoie l'aire du rectangle de cotés a et b
def aire(a,b):
    return a*b
print(aire(4,3))


'''_________________________________________________________________________________________________________________________________________'''


def salutation():
    return "Bonjour"
s=salutation()
print(s)

#Le return est optionnel, par défaut une fonction renvoie
#une valeur spéciale appelée None
def dit_bonjour():
    print("Bonjour à tous !")

resultat = dit_bonjour()
print(resultat)


'''_________________________________________________________________________________________________________________________________________'''


def f(x):
    return x**2 - 2*x + 3

print(f(0))
print(f(2))
print(f(3))


'''_________________________________________________________________________________________________________________________________________'''


'''
Exemple de fonction qui renvoie un bool
fonctions qui teste si la lettre passée en paramètre
est une voyelle
'''
def voyelle(lettre):
    return lettre in "AEIOUYaeiouy"

# print(voyelle("a"))
# print(voyelle("b"))

#on peut utiliser cette fonction en guise de condition 
lettre = input("Entre une lettre : ")
if voyelle(lettre):
    print("C'est une voyelle")
else:
    print("C'est une consonne")


'''_________________________________________________________________________________________________________________________________________'''


'''
Exerice 
Coder votre propre fontion max:
Ecrire une fonction maximum qui prend deux paramètres
et qui renvoie la plus grande des deux
'''

def max(a,b):
    if a > b:
        return a
    else:
        return b

plusgrand = max(9,3)
print(plusgrand)


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 
Ecrire une fonction max3 qui prend trois paramètre 
et qui renvoie la plus grande des trois
Sans utiliser max, min, ni la fonction maximum défini
plus haut
'''

def max3(a,b,c):
    if b < a > c:
        return a
    elif b > c:
        return b
    else:
        return c

plusgrand = max3(11,-10,8)
print(plusgrand)


