# -*- coding: utf-8 -*-

# Affiche les nombre de 0 inclus à 5 exclus
for i in range(5):
    print(i)
print() #on saute une ligne

# équivalent à
i=0
while i<5:
    print(i)
    i+=1
print()

#deuxième variante de range : range(start, stop)
for i in range(3,10):
    print(i)
print()

#troisième variante : range(start, stop, step)
for i in range(2,13,3):
    print(i)
print()

#équivalent à
i=2
while i<13:
    print(i)
    i+=3
print() #on saute une ligne

#on peut compter à rebours
for i in range(5,0,-1):
    print(i)
print('Partez !')
print()

for i in range(3, -1, -1):
    print(i)
print()


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice
Afficher les nombres pairs de 0 à 10 inclus
'''

for i in range(0,11,2):
    print(i)
print()


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 
Demander 4 nombre à l'utilisateur et afficher leurs somme
'''

nombre = int(input("Saissisez 4 nombre pour avoir la somme :"))
compteur = 0
somme = 0
for i in range(1,4):
    somme += nombre
    compteur += 1
    nombre = int(input("Saissisez 4 nombre pour avoir la somme :"))
print(somme)
print()

'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice
Demander un nombre n à l'utilisateur 
Puis calculer et afficher la somme 1+2+3+....+n
Exemple : si n=6, afficher 21
'''

n = int(input("Saissisez un nombre :"))
somme = 0
for i in range(n+1):
    somme+=i
print(somme)
print()


