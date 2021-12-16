# -*- coding: utf-8 -*-

#Pour sauvegarder des données dans un fichier,
#on doit l'ouvrir en écriture avec l'option open
# et l'option "w"
# Si le fichier n'existe pas, il est automatiquement créé
# On utilise la syntaxe with open() as nomdevariable
# Pour ouvrir le fichier de manière plus sûre :
#   - Le fichier est automatiquement fermé à la fin du bloc
#   - Si une erreur arrive, le fichier est proprement fermé
#   - A l'interieur du bloc, on est sûr que le fichier a 
with open("fichier.txt","w") as fichier:
    # à l'intérieur de ce bloc with le fichier est ouvert
    # à  l'éxterieur on sort
    fichier.write("Bonjour\n")
    fichier.write("Ca va ?\n")

#L'option "w" écrase le contenu du fichier
#Pour ajouter du contenu à un fichier non vide,
#on utilie l'option "a"
with open("fichier.txt","a") as fichier:
    fichier.write("Belle journée n'est-ce pas ?\n")

'''
Pour lire dans un fichier, on utilise l'option "r"
'''
with open("fichier.txt","r") as fichier:
    contenu = fichier.read()
print(contenu)
print(len(contenu))

'''
Pour récupérer les données ligne par ligne
'''
with open("fichier.txt","r") as fichier:
    # lignes = fichier.readlines()
    contenu = fichier.read()
    # permet de découper une chaine de caractère au moment du retour à la ligne
    # et les retour à la ligne sont supprimé
    lignes = contenu.splitlines()
print(lignes)


'''
Pour à la fois lire et écrire dans un fichier, on peut 
utiliser l'option "w+" ou "a+" ou "r+"
'''

'''
Exercice
Ecrire 8 nombre aléatoire entre 0 et 10 dans un fichier
avec un nombre par ligne
Dans un deuxième temps, ouvrir le fichier en lecture et 
récupérer les nombres puis calculer leur somme
'''

import random

with open("fichier.txt", "a") as fichier:
    for i in range(8):
        nombre = random.randint(0,10)
        fichier.write(str(nombre)+'\n')
# print(fichier)

somme = 0
with open("fichier.txt","r") as fichier:
    contenu = fichier.read()
    nombre = contenu.splitlines()
    for i in nombre:    
        somme += int(i)
print(somme)


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 2
Ecrire dans un fichier les données suivantes 
avec un identifiant et un mot de passe par ligne
séparés par un espace
'''

identifiants = [
    "Thibaut",
    "Toto",
    "admin",
    "Zuckerberg",
    "Cartman",
    "Marie",
]

mdp = [
    "azerty",
    "0000",
    "password",
    "facebook",
    "Autorite",
    "radium"
]

with open("fichierEx2.txt","w") as fichier:
    for i in range(len(identifiants)):
        fichier.write(identifiants[i]+" "+mdp[i]+"\n")



'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 3
Lire les donnée du fichier et les stocker dans un dictionnaire
où les clés sont les identifiants et les valeurs sont les mots de passe
Indice : si phrase est une chaine de caractère 
on peut utiliser phrase.split() pour la découper en une list de str
là où il y a des espace
Exemple :  phrase='abc def gh'
phrase.split() renvoie la liste ["abc", "def", "gh"]
!!! Ceci est un exercice d'entrainement, pas de cybersécurité
!!! Ce n'est pas comme ça qu'on stocke des mots de passe
!!! dans la vraie vie !
'''

idmdp = {}
with open("fichierEx2.txt","r") as fichier:
    contenu = fichier.read()
    ligne = contenu.splitlines()
    for i in ligne:
        miniliste = i.split()
        for e in miniliste:
            idmdp[miniliste[0]] = miniliste[1]
print(idmdp)


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 4
Créer une fenêtre "Connexion" avec un champ "identifiant
un champs "mot de passe", un bouton "Connnexion" et un label
"Entrez vos identifiants"
Quand l'utilisateur clique sur le bouton, le label affiche:
    - Identifiant inconnu s'il n'apparait pas dans le dictionnaire
    - Mot de passe incorrect si le mdp ne correspond pas à associé
    à cet identifiant
    - Bonjour idenitifiant si le mdp est corrrect (en remplaçant identifiant par l'id de 
    l'utilisateur)
Indice :  pour tester si une clé est dans un dictionnaire,
on peut faire:
if cle in dictionnaire:
'''

import tkinter as tk

fenetre = tk.Tk()


identifiant = tk.StringVar()
entry1 = tk.Entry(fenetre, textvariable=identifiant)
entry1.grid()

mdp = tk.StringVar()
entry2 = tk.Entry(fenetre, textvariable=mdp)
entry2.grid()

label = tk.Label(fenetre, text="Entrez vos identifiants")
label.grid()

def display():
    id = identifiant.get()
    usermdp = mdp.get()
    if id in idmdp:
        if idmdp[id] != usermdp:
            label.config(text="Mot de passe incorrect")
        else:
            label.config(text="Bonjour "+id)
    else:
        label.config(text="Identifiant inconnu.")

button = tk.Button(fenetre,text="Connexion",command=display)
button.grid()

tk.mainloop()


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 5 
Ajouter un bouton pour créer un nouveau compte :
    -si l'identifiant existe déjà, indiquer
    "Identifiant déjà pris" sur le label
    - sinon, ajouter un nouveau couple id/mdp dans le dictionnaire 
    et sauvegarder le dictionnaire dans un fichier
'''

import tkinter as tk
import json

fenetre = tk.Tk()

identifiant = tk.StringVar()
entry1 = tk.Entry(fenetre, textvariable=identifiant)
entry1.grid()

mdp = tk.StringVar()
entry2 = tk.Entry(fenetre, textvariable=mdp)
entry2.grid()

def test_id():
    id = identifiant.get()
    usermdp = mdp.get()
    if id in idmdp:
        label.config(text="Identifiant déjà pris")
    else :
        label.config(text="Ajouter le nouveau compte")
        idmdp[id] = usermdp
        with open("dictionnaireAjout.txt","w") as fichier:
            fichier.write(json.dumps(idmdp))

bouton = tk.Button(fenetre, text="Créer un compte",command=test_id)
bouton.grid()

label = tk.Label(fenetre, text="Ajouter le nouveau compte")
label.grid()

tk.mainloop()



