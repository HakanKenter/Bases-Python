# -*- coding: utf-8 -*-

'''
Exercice 1
Demander à l'utilisateur quel jour de la semaine on est 
(Lundi, mardi, etc..)
Si on est samedi ou dimanche, afficher "Bon weekend !"
Sinon, afficher "Vivement le weekend !"
'''

# jourSemaine = input("Quel est le jour de la semaine ? ").lower()
 
# if jourSemaine == "Samedi" or jourSemaine == "Dimanche":
#     print("Bon weekend !")
# else :
#     print("Vivement le weekend !")
# print()


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 2
Demander quel mois on est. Si on est entre 
septembre et décembre, afficher "fin d'année"
'''

# mois = input("Quel est le mois actuelle ? ").lower()
# if "bre" in mois:
#     print("fin d'année")


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 3
Demander une note sur 20.
Si la note est <0 ou >20, afficher "impossible"
Si elle est entre 0 et 9, afficher "rattrapage"
Si elle est entre 10 et 15, afficher "passage"
Si elle est entre 16 et 20, afficher "Bravo !"
'''

# note = int(input("Donner une note sur 20 :"))

# if note < 0 or note > 20 :
#     print('Impossible')
# elif note < 10:
#     print('Rattrapage')
# elif note < 16 :
#     print('Passage')
# else :
#     print('Bravo !')


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 4
Demander un mot de passe. Tant que le mot entré n'est pas
azerty, redemander le mot de passe.
Une fois que le mot de passe est bon, afficher "Bienvenue"
'''

# mdp = ""
# while mdp != "azerty":
#     mdp = input("Choisissez un mot de passe : ")
# print('Bienvenue')
# print()


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 5
Même exercice mais l'utilisateur n'a que 3 tentatives.
S'il n'a pas entré le bon mot de passe, afficher 
"Votre compte est bloqué"
'''

# mdpQ = input("Choisissez un mot de passe : ")

# for i in range(2) :
#     if mdpQ != "azerty" :
#         mdpQ = input("Choisissez un mot de passe : ")
#     elif mdpQ == "azerty" :
#         print('Bienvenue !')
#         break 
# print('Votre compte est bloqué')
# print()

# mdp=""
# i=0
# while mdp != "azerty" and i<3:
#     mdp = input("Mot de passe ?")
#     i+=1
# if mdp == "azerty":
#     print("Bienvenue")
# else:
#     print("Votre compte est bloqué")


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 6
Afficher les nombres 10, 100, 1000, 10000, etc. jusqu'à
1 000 000 000
'''

# for i in range(1, 10):
#     print(10**i)

# alternative
nombre="1"
for i in range(10):
    nombre+="0"
    print(nombre)

