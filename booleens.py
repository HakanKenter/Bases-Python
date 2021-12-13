# -*- coding: utf-8 -*-

'''
En python, le type bool (booléen) représente des valeurs de vérité
Il y a deux valeur possibles : True et False
Les opérateurs de comporaison <, <=, >, >=, == et != ont pour résultat
un bool
'''

# if True:
#     print("a")
# else: 
#     print("b")

# if 3<2:
#     print("a")
# else:
#     print("b")

#On crée une variable qui contient un bool
test = 5!=3
print(test)
if test:
    print("a")
else:
    print("b")

mdp="querty"
testmdp = mdp == "azerty"
if testmdp:
    print("mot de passe correct")
else:
    print("mot de passe incorrect")


'''_________________________________________________________________________________________________________________________________________'''


'''
Les opérateurs booléens permettent de manipuler les expressions booléennes
not inverse la valeur du booléen
x           not x
True        False
False       True
'''
print()#on saute une ligne 
print(not False)
print(not 2==2)



'''_________________________________________________________________________________________________________________________________________'''

'''
and teste si deux conditions sont vrai simultanément
x           y           x and y
True        True        True
True        False       False
False       False       False
False       True        False
'''

print() #on saute une ligne
print(False and True)
a=5
print(a>0 and a%2==0) #on teste si a est positif et divisible par 2


'''_________________________________________________________________________________________________________________________________________'''


'''
or teste si au moins une des deux condition est vraie
x           y           x and y
True        True        True
True        False       True
False       False       False
False       True        True
'''

print()#on saute une ligne
print(True or False)
print(5>3 or 2==4)

#exemple avec les années bissextiles:
annee = int(input("Entre une année "))
if annee%400==0 or (annee%4==0 and annee%100!=0):
    print("Bissextile")
else:
    print("Non bissextile")


'''_________________________________________________________________________________________________________________________________________'''


#tester si une str apparaît à l'intérieur d'une autre
mot = input("Entre un mot ")
if "e" in mot:
    print("Le mot contient la lettre e")
else:
    print("Le mot ne contient pas la lettre e") 

if "to" in "toto":
    print('gagné')
else: 
    print("perdu")


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice
Demander une lettre et afficher "voyelles" ou "consonne"
suivant la lettre entrée
'''

lettre = input('Saisissez une lettre : ')

if lettre in 'AEIOUYaeiouy' : 
    print('voyelle')
else :  
    print('consonne')