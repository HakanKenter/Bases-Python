# -*- coding: utf-8 -*-

'''
Exercice
Créer une fenêtre avec un canvas carré
et diviser le canvas en une grille de 3x3 cases carée
'''

import tkinter as tk
from tkinter import font

fenetre = tk.Tk()


taille_case = 100 #taille d'une case de la grille
canvas = tk.Canvas(fenetre,width=3*taille_case,height=3*taille_case,background="white")

canvas.grid()
#premiere ligne verticale
canvas.create_line(taille_case,0,taille_case,3*taille_case,width=3)

#deuxième ligne verticale
canvas.create_line(2*taille_case,0,2*taille_case,3*taille_case,width=3)

#première ligne horizontale
canvas.create_line(0,taille_case,3*taille_case,taille_case,width=3)

#deuxième ligne horizontale
canvas.create_line(0,2*taille_case,3*taille_case,2*taille_case,width=3)

#mon code pas ergnonomique
# canvas = tk.Canvas(fenetre,width=600, height=600, background="green")
# canvas.grid()

# canvas.create_rectangle(0,0,200,200,fill="red",outline="blue",width=5)
# canvas.create_rectangle(200,0,400,200,fill="green",outline="blue",width=5)
# canvas.create_rectangle(400,0,600,200,fill="black",outline="blue",width=5)

# canvas.create_rectangle(0,200,200,400,fill="red",outline="blue",width=5)
# canvas.create_rectangle(200,200,400,400,fill="green",outline="blue",width=5)
# canvas.create_rectangle(400,200,600,400,fill="black",outline="blue",width=5)

# canvas.create_rectangle(0,400,200,600,fill="red",outline="blue",width=5)
# canvas.create_rectangle(200,400,400,600,fill="green",outline="blue",width=5)
# canvas.create_rectangle(400,400,600,600,fill="black",outline="blue",width=5)


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice
Ecrire une fonction qui prend en paramètre 
une ligne (entre 0 et 2) et une colonnes (entre 0 et 2) et qui dessine une croix de la taille
d'une case (ou légèrement plus petite) centrée sur la case située sur cette ligne et cette colonne 
'''
marge=10 #marge utilisée pour éviter que les croix
# et les ronds touchent le borrd des cases
def dessine_croix(ligne,colonne):
    #coordonées du point en haut à gauche 
    #de la case voulu
    y=ligne*taille_case
    x=colonne*taille_case

    canvas.create_line(x+marge,y+marge,x+taille_case-marge,y+taille_case-marge,width=3,fill="blue")
    canvas.create_line(x+marge,y+taille_case-marge,x+taille_case-marge,y+marge,width=3,fill="blue")

dessine_croix(2,0)

'''
Exercice
Même en dessinant un rond
'''

def dessine_cercle(ligne,colonne):
    #coordonées du point en haut à gauche 
    #de la case voulu
    y=ligne*taille_case
    x=colonne*taille_case

    canvas.create_oval(x+marge,y+marge,x+taille_case-marge,y+taille_case-marge,width=3,fill="blue")
    canvas.create_oval(x+marge,y+taille_case-marge,x+taille_case-marge,y+marge,width=3,fill="blue")

dessine_cercle(1,0)

#fonction qui prend en paramètre des coordonnées x,y
#qui représente le pixel où on a cliqué
#et qui renvoie la ligne et la colonne correspondant à 
#la case où se trouve ce pixel
def case(x,y):
    #on cherche la ligne
    if y<taille_case:
        ligne=0
    elif y<2*taille_case:
        ligne=1
    else:
        ligne=2
    #on cherche la colonne
    if x<taille_case:
        colonne=0
    elif x<2*taille_case:
        colonne=1
    else:
        colonne=2
    return (ligne, colonne)

#alternative plus courte
def case2(x,y):
    return(y//taille_case,x//taille_case)

#fonction callback appelés à chaquer clic
def clic(event):
    ligne,colonne=case(event.x,event.y)
    dessine_croix(ligne,colonne)

canvas.bind("<Button-1>",clic)
    
tk.mainloop()