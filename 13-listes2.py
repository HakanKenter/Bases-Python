# -*- coding: utf8 -*-

'''
Exercice
Écrire une fonction qui prend en paramètre une liste
et qui renvoie la somme des éléments
(renvoie 0 si la liste est vide)
Interdiction d'utiliser sum()
'''

def somme(liste):
    add = 0
    if len(liste) > 0:
        for i in liste:
            add += i
    return add

# Retourne la somme
print(somme([3,4,5,8]))
# Retourne 0
print(somme([]))


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice
Écrire une fonction qui prend en paramètre une liste
et qui renvoie le plus petit élément de la liste
(Renvoie None si la liste est vide)
Interdiction d'utiliser min() et max()
'''

import math

def minEl(liste):
    higher = math.inf
    if len(liste) > 0:
        # len(liste)
        for i in range(len(liste)):
            if liste[i] < higher:
                higher = liste[i]
        return higher
    else :
        return None

# Retourne la somme
print(minEl([-3,-4,-9,-8]))
# Retourne None
print(minEl([]))


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice
Écrire une fonction qui prend en paramètre une liste et
un élément et qui renvoie le nombre de fois que cet élément
apparaît dans la liste
Interdiction d'utiliser count()
'''

def displayNumber(liste, element):
    count = 0
    for i in range(len(liste)):
        if liste[i] == element:
            count += 1
    return count

print(displayNumber(['hk', 'nk', 'ih', 'hk', 'hk'], 'hk'))


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice
Écrire une fonction qui prend en paramètre une liste 
et un élément e et qui teste si l'élément est présent
dans la liste (renvoie un bool)
Sans faire le test "e in l"
'''

def present(liste, e):
    for i in range(len(liste)):
        if liste[i] == e:
            return True
    else :        
        return False

print(present(['er', 'hk', 'nk'], 'hk'))


'''_________________________________________________________________________________________________________________________________________'''


#Pour créer une liste dans laquelle on ajoute des valeur rapidement
# listec = [i**2 for i in range(5)]
# print(listec)

#La meme chose en plus long 
# liste = []
# for i in range(5):
#     liste.append(i)




