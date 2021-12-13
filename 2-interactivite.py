# -*- coding: utf-8 -*-

# La fonction input permet de demander à l'utilisateur d'entrer des infos
# Le résultat est renvoyé sous forme de str
entree = input()
print("Tu as voulu dire :", entree)

prenom = input("Comment tu t'appelles ?")
print("Bienvenue",prenom) 
# on utilise des virgules dans les print, c'est aussi une forme de concaténation

'''
Exercice :
Ecrire un programme qui demande à l'utilisateur d'entrer son annee de naissance
et qui affiche son âge en 2021
'''

annee = int(input("En quel anne est-tu née ?"))
print("Tu as",2021-annee, "ans en 2021.")