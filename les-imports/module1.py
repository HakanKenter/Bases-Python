# -*- coding: utf-8 -*-
def carre(x): 
    return x**2

def aire(x,y):
    return x*y

prenom = "hakan"

'''
La variable __name__ vaut "__main__" s'il est executer directement 
et vaut "module1" s'il est importé depuis un autre module
'''


print("__name__ depuis le module1 :", __name__)

# Ne vais être executer que si j'execute ce script "module1.py"
# Car __name__ renvoi toujours "__main__" si elle est appelé dans 
# le même fichier
# Si en revanche elle est importer dans un autre module
# Sa valeur sera le nom du module
# Donc si je l'appel depuis le module2 sa valeur ne sera pas 
# "__main__" mais "module1"
if __name__ == "__main__":
    print(carre(6))