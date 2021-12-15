# -*- coding: utf-8 -*-

'''
Exercice 
Créer une fenêtre appelés "connexion" avec 
un label "Identifiant" suivi d'une Entry
un label "Mot de passe" suivi d'une entry
Un bouton "OK" et un label "Connexion"
Quand l'utilisateur clic sur le bouton OK, 
le dernier label doit afficher:
    - Identifiant inconnu si l'identifiant n'est pas "Thibaut"
    - "Mot de passe incorrect" si l'identifiant est bon mais le 
    mot de passe n'est pas "azerty
    - "Bienvenue Thibaut" si l'identifiant et le mot de passe
    sont corrects
'''

import tkinter as tk

# Créer une fenêtre appelés "connexion"
fenetre = tk.Tk()
fenetre.title("Connexion")

'''_________________________________________________________________________________________________________________________________________'''

#un label "Identifiant" suivi d'une Entry
label1 = tk.Label(fenetre,text="Identifiant")  
label1.grid(row=1,column=1)

identifiant = tk.StringVar()
entry1 = tk.Entry(fenetre,textvariable=identifiant)
entry1.grid(row=1,column=2)

'''_________________________________________________________________________________________________________________________________________'''


# un label "Mot de passe" suivi d'une entry
label2 = tk.Label(fenetre,text="Mot de passe")
label2.grid(row=2,column=1)

mdp = tk.StringVar()
entry2 = tk.Entry(fenetre,textvariable=mdp)
entry2.grid(row=2,column=2)

'''_________________________________________________________________________________________________________________________________________'''

# Quand l'utilisateur clic sur le bouton OK, 
# le dernier label doit afficher:
#     - Identifiant inconnu si l'identifiant n'est pas "Thibaut"
#     - "Mot de passe incorrect" si l'identifiant est bon mais le 
#     mot de passe n'est pas "azerty"
#     - "Bienvenue Thibaut" si l'identifiant et le mot de passe
#     sont corrects

def display():
    if identifiant.get() != "Thibaut":
        nouveau_message = "Identifiant inconnu"
    elif mdp.get() != "azerty":
        nouveau_message = "Mot de passe incorrect"
    else : 
        nouveau_message = "Bienvenue Thibaut"
    label3.config(text=nouveau_message)

'''_________________________________________________________________________________________________________________________________________'''


# Un bouton "OK" et un label "Connexion"
button = tk.Button(fenetre,text="OK",command=display)
button.grid(row=3,column=1,columnspan=2)

label3 = tk.Label(fenetre,text="Connexion")
label3.grid(row=4,column=1)

'''_________________________________________________________________________________________________________________________________________'''

tk.mainloop()