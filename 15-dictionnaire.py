#-*- coding: utf-8 -*-

#Un dictionnairee associe des clés à des valeurs 
repertoire = {
    "Thibaut":"0621154878",
    "Toto":"0506078465",
    "Bob":"0754321568",
    "Pompiers":"18",
}

# print(repertoire)

# #On accàde aux valeurs via les clés
# print(repertoire["Toto"])

# #On peut modifier un élément
# repertoire["Toto"] = "0717548652"
# print(repertoire["Toto"])

# #Si la clé n'existe pas, elle est créée
# #et la valeur donnée après le = lui est associée
# repertoire["Maman"] = "0535458752"
# print(repertoire)

#Pour parcourir un dictionnaire
# for cle in repertoire:
#     print(cle, repertoire[cle])


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 
Créer un dictionnaire dont les clés sont
des noms et les valeurs sont des notes (int)
Puis calculer et afficher la moyenne de la classe
'''

# notes = {
#     "Thibaut":20,
#     "Toto":15,
#     "Bob":2,
#     "Pompiers":13,
# }

# somme = 0
# for eleve in notes:
#     tour += 1
#     somme += notes[eleve]
# moyenne = somme / len(notes)
# print("moyenne :",moyenne)


'''_________________________________________________________________________________________________________________________________________'''


'''
Exerice
Créer un dictionnaire vide puis demander à l'utilisateur 
d'entrer des noms de pays et leurs capitales et stocker ces données
dans le dictionnaires (les clés seront les pays et les valeurs seront
les capitales)
On s'arrête au mot "stop"
'''

# pays_capitale = {}
# entree_pays = ""
# entree_ville = ""

# while entree_pays != "stop":
#     entree_pays = input("Entrer un Pays : ")
#     if entree_pays != "stop":
#         entree_ville = input("Entre une ville : ")
#         pays_capitale[entree_pays] = entree_ville

# print(pays_capitale)

#Alternative avec une seul comparaison
# entree_pays = input("Entrer un Pays : ")
# while entree_pays != "stop":
#     entree_ville = input("Entre une ville : ")
#     pays_capitale[entree_pays] = entree_ville
#     entree_pays = input("Entrer un Pays : ")

# print(pays_capitale)



'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice
Afficher la capitale du pays qui a le nom le plus long
Afficher le pays dont la capitale a le nom le plus court
'''

pays_capitale = {
    "France": "Paris",
    "Allemagne": "Berlin",
    "Turquie": "Istanbul",
    "Étas-Unis": "Washington",
}

maxpays = 0
for pays in pays_capitale:
    if len(pays) > maxpays:
        maxpays = len(pays)
        cap = pays_capitale[pays]
print("Plus long :",cap)


mincap = 1000000
for pays in pays_capitale:
    if len(pays_capitale[pays]) < mincap:
        mincap = len(pays_capitale[pays])
        p = pays_capitale[pays]
print("Plus court :",p)
