# -*- coding: utf-8 -*-

import random

'''
Exercice 
Coder un jeu de "nombre mystère"
L'ordinateur tire au hazard un nombre entre 1 et 100
Puis il demande au joueur de deviner le nombre
Si le joueur donne un nombre plus grand que le nombre
à deviner, le programme répond "plus bas", 
Si le joueur donne un nombre plus petit, le programme répond "plus haut".
Le joueur redonne de nouveaux nombres jusqu'à ce qu'il tombe sur 
le nombre à deviner.
À la fin, le programme indique combien d'étapes il a fallu au joueur pour deviner 
le nombre.
'''

randomNumber = random.randint(1, 100)
testNumber = 0
compteur = 0
while testNumber != randomNumber :
    testNumber = int(input("Deviner le nombre : "))
    compteur += 1
    if testNumber > randomNumber :
        print("Plus petit")
    elif testNumber < randomNumber :
        print("Plus grand")
    else :
        print("Il ta fallu",compteur,"tentatives pour réussir !")

