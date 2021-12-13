# # -*- coding: utf-8 -*-

# '''
# La boucle while permet de répéter des instructions temps qu'une condition est vérifiée
# '''

# #exemple: on demande à l'utilisateur d'entrer des mots
# #tant qu'il n'entre pas le mot stop

# entree = input("Entre un mot (stop pour arrêter) ")
# while entree != "stop":
#     entree = input("Entre un mot (stop pour arrêter) ")

# #même exemple, mais on compte le nombre de mots entrés ( à part stop )
# entree = input("Entre un mot (stop pour arrêter) ")
# compteur = 0
# while entree != "stop":
#     compteur = compteur + 1
#     entree = input("Entre un mot (stop pour arrêter) ")
# print("Tu as entré", compteur,"mots.")

# #Pour effectuer une action 8 fois d'affilée
# i = 0
# while i < 8:
#     print("i=", i)
#     i = i + 1
# print("Terminé.")


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice
Demander des nombres positifs à l'utilisateur
S'arreter dès qu'il entre un nombre négatif
Afficher le nombre de nombre entrés
'''

nombre = int(input("Entrer un nombre positif : "))
compteur = 0
while nombre >= 0:
    compteur += 1 #équivalent à compteur = compteur + 1
    nombre = int(input("Entrer un nombre positif : "))
print('Vous avez entré des nombre', compteur, 'fois')
    


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice
Demander des nombres positifs à l'utilisateur
S'arreter dès qu'il entre un nombre négatif
Affiche la somme des nombre positifs entrés
'''

nombre = int(input("Entrer un nombre positif : "))
compteur = 0
while nombre >= 0:
    compteur += nombre
    nombre = int(input("Entrer un nombre positif : "))
print('La sommes des nombre positif entrés est', compteur)


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice
Demander des nombres à l'utilisateur
S'arreter dès qu'il entre le mot 'stop'
Afficher la moyenne des nombres entrés
'''

nombre = input("Entrer un nombre : ")
compteur = 0
somme = 0
while nombre != "stop":
    compteur += 1
    somme  += int(nombre) 
    moyenne = somme / compteur
    nombre = input("Entrer un nombre : ")
if compteur == 0 :
    print('Vous avez quitter le programme !')
else :
    print('La moyenne des nombre entrée est : ', moyenne)
