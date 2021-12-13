# -*- coding: utf-8 -*-

'''
Exercice
Demander une année à l'utilisateur.
Afficher 'Bissextile' ou 'Non bissextile' suivant les cas.
Une année est bissextile si elle est divisible par 4.
Cependant, si elle est divisible par 100, elle n'est pas bissextile.
Dernière exception : si elle est divisile par 400, alors elle est bissextile.
L'Opérateur % (modulo) permet de savoir si un nombre a est divisible par un autre nombre b en testant :
a % b == 0

Exemples 
2001 n'est pas bissextile
2020 est bissextile
1900 n'est pas bissextile
2000 est bissextile
'''

annee = int(input("Choissisez une année."))

if (annee % 400) == 0: #Si l'année est divisible par 400
    print('Bissextile')
elif (annee % 100) == 0 : #Si l'année est divisible par 100
    print('Non bissextile')    
elif (annee % 4) == 0: #Si l'année est divisible par 4
    print('Bissextile')
else :
    print('Non Bissextile')