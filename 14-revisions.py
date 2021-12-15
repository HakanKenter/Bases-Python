# -*- coding: utf-8 -*-

'''
Exercice 1
Ecrire une fonction qui prend en paramètre une liste
et qui teste si elle est triée dans l'ordre croissant
(elle renvoi un booléen)
Indice :
'''

def test_triee(liste):
    # une liste vide ou à un élément est toujours triée
    if len(liste)<2:
        return True
        #pour les listes plus grandes,
        # on va comparer chaque élément à son précédent
    for i in range(1, len(liste)):
        if liste[i-1] > liste[i]:
            #si le précédent est plus grand 
            # alors liste liste n'est pas triées
            return False
    return True

print(test_triee([0,3,6,8,9,3]))
print(test_triee([10,8,6,5,4]))
        


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 2
Ecrire un fonction qui prend en paramètre une liste et 
deux indices i et j et qui échange les éléments situés
aux positions i et j
Exemple : avec la liste [5,7,0,1,3,6] et i=1 et j=3,
la liste devient [5,1,0,7,3,6]
La fonction ne renvoie rien
'''

def pos(liste, i, j):
    # il faut que ça soit fait en même temps
    #soit ça
    # aux = liste[i] # sert à rappeler la valeur de la liste[i]
    # liste[i] = liste[j]
    # liste[j] = aux
    # soit ça
    liste[i], liste[j] = liste[j], liste[i] 
    return liste

print(pos([5,7,0,1,3,6],1,3))

'''_________________________________________________________________________________________________________________________________________'''


'''
Exerice3
Ecrire un fonction qui prend en paramètre deux listes
de même taille et qui renvoie une troisième liste dont
les éléments sont la somme des éléments correspondants
des deux premières listes
Exemple : [3,4,1,8] et [1,0,2,2] donne [4,4,3,10]
'''

def sommedesListes(liste1, liste2):
    resultat = []
    for i in range(len(liste1)):
        resultat.append(liste1[i]+liste2[i])
    return resultat

print(sommedesListes([3,4,1,8], [1,0,2,2]))