# -*- coding: utf-8 -*-

a = int(input("Entre un nombre : "))

'''
Les instructions à l'intérieur  d'un bloc if
ne sont exécutées que si la condition est remplie
'''
if a > 0 : 
    print("Le nombre est positif.")
    print("Oui, j'ai bien dit positif.")

# On sort d'un bloc if en revenu en arière dans l'indentation
print("Cette instruction est executée quoi qu'il arrive")
print()

# le bloc eslse sert à executer les instructions quand la condition if 
# n'est pas vérifier
if(a > 0): 
    print("positif")
else : 
    print("negatif ou nul")
print()

#les blocs elif servent à tester plusieurd conditions les une après les autres 
if a > 0 : 
    print("positif")
elif a < 0 :
    print("negatif")
else : 
    print('nul')

'''
Syntaxe générale des conditionnelles:
if condition1 :
    instructions1
    ...
elif condition2 : 
    instruction2
    ...
elif condition3 : 
    instructions3
    ...
else :
    instructions par défault
    ...

Les blocs elif sont facultatifs et ils peut y en avoir plusieurs
Le bloc else est facultatif mais toujours à la fin et il n'a pas de condition
'''

'''
Exercice 
Ecrire un programme qui demande à l'utlisateur son age 
Si l'age est négatif , afficher "impossible"
Si l'âge est entre 0 et 18 ans, afficher 'mineur'
Si l'âge est >= 18ans, afficher "majeur"
'''

age = int(input("Quel âge as-tu ?"))

if age < 0 :
    print('Impossible')
elif age >= 0 and age < 18 :
    print("mineur")
elif age >= 18 :
    print('majeur')