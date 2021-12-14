# -*- coding: utf-8 -*-

'''
Exercice 1
Demander à l'utilisateur quel jour de la semaine on est 
(Lundi, mardi, etc..)
Si on est samedi ou dimanche, afficher "Bon weekend !"
Sinon, afficher "Vivement le weekend !"
'''

# jourSemaine = input("Quel est le jour de la semaine ? ")
 
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

# moisQ = input("Quel est le mois actuelle ? ")
# mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
# for i in mois:       
#     if mois.index(moisQ) >= 8 :
#         print("Fin d'année !")
#         exit()
#     else :
#         moisQ = input("Quel est le mois actuelle ? ")
# print()


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 3
Demander une note sur 20.
Si la note est <0 ou >20, afficher "impossible"
Si elle est entre 0 et 9, afficher "rattrapage"
Si elle est entre 10 et 15, afficher "passage"
Si elle est entre 16 et 20, afficher "Bravo !"
'''

# noteQ = int(input("Donner une note sur 20 :"))

# if noteQ < 0 or noteQ > 20 :
#     print('Impossible')
# elif noteQ >= 0 and noteQ <= 9 :
#     print('Rattrapage')
# elif noteQ >= 10 and noteQ <= 15 :
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

# mdpQ = input("Choisissez un mot de passe : ")

# while mdpQ != "azerty":
#     mdpQ = input("Choisissez un mot de passe : ")
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


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 6
Afficher les nombres 10, 100, 1000, 10000, etc. jusqu'à
1 000 000 000
'''

# for i in range(1, 10):
#     print(10**i)