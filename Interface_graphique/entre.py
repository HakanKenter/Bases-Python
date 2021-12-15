# -*- coding: utf-8 -*-

import tkinter as tk

fenetre = tk.Tk()

#Un StringVar permet de communiquer des str 
#entre des widget
texte = tk.StringVar()

#Une entry permet d'écrire du texte.
#Ce texte est automatiquement stocké dans la StringVar
entry = tk.Entry(fenetre,textvariable=texte)
entry.grid(row=1,column=1)

label = tk.Label(fenetre,text="Entre ton nm")
label.grid(row=2,column=1)

#Fonction callback appelés à chaque clic
#sur le bouton
def clic():
    #on récupère la str stockés dans la StringVar
    nom = texte.get()
    #on l'affiche sur le label
    label.config(text=nom)

bouton = tk.Button(fenetre,text="OK",command=clic)
bouton.grid(row=1,column=2)

tk.mainloop()