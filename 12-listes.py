# -*- coding: utf-8 -*-

#une liste contient des objets indexés par leurs position
#dans la liste

liste1 = [45, -3.1, "abc", True]
print(liste1)

# Le nombre d'éléments est donné par la fonction len()
print(len(liste1))

#On accède aux éléments via les crochets
# les indices (positions) commencent à zéro
print(liste1[0])

#On peut aussi compter à partir de la fin avec des indices négatifs
print(liste1[-1])

#On peut changer un élément
liste1[2] = "def"
print(liste1)

#On peut ajouter des éléments

#à la fin 
liste1.append(0)
print(liste1)

# à une position donnée
liste1.insert(1,"toto")
print(liste1)

#on peut retirer des éléments 

#par indice
liste1.pop(3)
print(liste1)

#par valeur
liste1.remove(-3.1)
print(liste1)

#On peut concaténér deux listes
liste2 = ["a","b","c"]
print(liste1+liste2)

#Pour parcourir une list, on va souvent utiliser une boucle for
#len() renvoi la longueur d'une liste donnée
for i in range(len(liste2)):
    print("Élement d'indice",i,":",liste2[i])

#Si on n'a pas besoin des indices mais seulement des 
#valeurs, on peut parcourir directement les éléments eux-mêmes
for e in liste2:
    print(e)

#Pour construire une liste petit à petit 
liste3 = [] # liste vide
for i in range(5):
    liste3.append(2**i)
print(liste3)

'''
Exercice
Demander 4 nombres à l'utilisateur et construire 
une liste contenant tous ces nombres puis afficher la somme
'''

liste4 = []
somme = 0
for i in range(4):
    number = int(input("Saisissez un nombres : "))
    liste4.append(number)
    somme += number 
print("Le sommes des 4 nombres que vous avez saisie est :", somme)
print(sum(liste4))
print()


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice
Demander des nombres et construire une liste avec tout ces 
nombres jusqu'au mot 'stop'
Puis afficher le plus grand nombre de la liste
'''

nombre = input("Saisissez des nombres :")
liste5 = []
entree = input("Saisissez des nombres (stop pour arrêter) :")
while entree != "stop":
    liste5.append(int(entree))
    entree = input("Saisissez des nombres (stop pour arrêter) :")
print(max(liste5))


'''_________________________________________________________________________________________________________________________________________'''



'''
Exercice
Demander 5 des mots et en faire une liste puis afficher le mot le plus long
de la liste
'''

liste6 = []
motlepluslong="" # stocke le record du mot le plus long
for i in range(5):
    mot = input("Ecrivez des mot : ")
    liste6.append(mot)
    # Si on trouve un mot plus long que le record actuel
    # ce mot devient le nouveau record
    if len(mot) > len(motlepluslong):
        motlepluslong=mot
print(motlepluslong)


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice
Créer une liste de 20 nombres entier aléatoires compris entre 1 et 6 
et afficher le premier et le dernier element de cette liste
'''
import random

liste7 = []
for i in range(20):
    liste7.append(random.randint(1,6))

print(liste7)
print(liste7[0])
#dernier élément
print(liste7[19])
#dernier élément
print(liste7[-1])