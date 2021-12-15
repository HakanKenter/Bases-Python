# -*- coding: utf-8 -*-

import tkinter as tk

fenetre = tk.Tk()

canvas = tk.Canvas(fenetre,width=400,height=300,background="white")

canvas.grid()

#fonction qui affiche des coordonnée x,y
#à leurs emplacement sur la canvas
def affiche_coordonnees(x,y):
    canvas.create_text(x,y,text=str(x)+","+str(y))

# affiche_coordonnees(200,150)
# affiche_coordonnees(50,220)
# affiche_coordonnees(20,10)
# affiche_coordonnees(380,290)

#fonction callback appelés à chaque fois qu'on clique sur 
#le canvas
#le paramètre eveenemtn est créé automatiquement par 
#tkinter et contient des information sur l'évènement
#qui a eu lieu
def on_left_click(event):
    #event.x et event.y sont les coordonnées
    #du curseur au moment où le clic a eu lieu
    affiche_coordonnees(event.x, event.y)

#demande à tkinter d'appeler la fonction on_clic
#à chaque fois que l'évènement "<Button-1>" a lieu
#Cet évènement représente un clic sur le bouton gauche
#de la souris
#bind dit si cette evenement est donner -> appeler cette fonction


'''_________________________________________________________________________________________________________________________________________'''

#on dessine un petit x à l'endroit où on a cliqué
def on_right_click(event):
    canvas.create_text(event.x,event.y,text="x")


canvas.bind("<Button-1>",on_left_click)
canvas.bind("<Button-3>", on_right_click)

#L'évènement <Button-3> reprénsente le clic droit


tk.mainloop()