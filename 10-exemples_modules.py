# -*- coding: utf-8 -*-


'''_________________________________________________________________________________________________________________________________________'''


#pour importer un module et utiliser ses fonctions et variables
import math

#racine carrée
print(math.sqrt(49))

#cosinus
print(math.cos(1.5))

print(math.pi)


'''_________________________________________________________________________________________________________________________________________'''


#time serrt à mesurer et manipuler le temps 
import time

#sleep met en pause le programme pendant un certain temps
print("a")
time.sleep(3)
print("b")

#time sert à mesurer la durer
t1=time.time()
entre = input("Entre un mot : ")
t2=time.time()
print("Il ta fallu",t2-t1,"secondes pour répondre")


'''_________________________________________________________________________________________________________________________________________'''


#Pour générer des nombres aléatoires
import random

#tire au hasard un int entre les deux bornes en paramètres incluses
print(random.randint(3,8))

#tire un foalt au hasard entre 0 et 1
print(random.random())