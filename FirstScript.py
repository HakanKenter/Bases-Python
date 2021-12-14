# # -*- coding: utf-8 -*-

# '''
# Les triple guillements pour les commentaires sur plusieurs lignes
# En python, le caractère # sert à commencer un commentaire
# Le commentaire s'étend jusqu'en, bout de ligne
# '''

# # Déclaration d'une variable
# mavariable = 2

# # Affichage
# print(mavariable)

# # Le type str représente les chaine de caractères
# print('Bonjour')

# # L'opérateur + sert à concaténer des str
# print("Bonjour " + "ca va ?")

# # On crée des variables en donnant leurs nom de suivi d'un =
# mavariable2 = 5
# autrevariable = 3 
# print(mavariable + autrevariable)

# # La fonction print accepte plusieurs paramètres sparés par des virgules
# print("la calcul", mavariable2,"+",autrevariable,"donne", mavariable2+autrevariable)

# # Conversions de types
# texte = str(mavariable) # conversion en str
# print("a"+texte)
# a=int("32") # conversion en int
# print(a**2) # ** est l'opérateur de puissance: a**b vaut a puissance b


def salutation():
    return "Bonjour"
s=salutation()
print(s)
