# -*- coding: utf-8 -*-

import tkinter as tk

fenetre = tk.Tk()

label1 = tk.Label(fenetre, text="Au tour du rond")
label1.grid()


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

marge=10 #marge utilisée pour éviter que les croix
# et les ronds touchent le bord des cases

#desine une croix dans la cas indiquée
#ligne vaut 0,1 ou 2
#colonne vaut 0,1 ou 2
def dessine_croix(ligne,colonne):
    #coordonées du point en haut à gauche 
    #de la case voulu
    y=ligne*taille_case
    x=colonne*taille_case

    canvas.create_line(x+marge,y+marge,x+taille_case-marge,y+taille_case-marge,width=3,fill="blue")
    canvas.create_line(x+marge,y+taille_case-marge,x+taille_case-marge,y+marge,width=3,fill="blue")

dessine_croix(2,0)

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
# def case2(x,y):
#     # "//" prend la divison entière et ignore les virgule et ce qu'il y a après
#     return(y//taille_case,x//taille_case)
#fonction callback appelés à chaquer clic
# def clic(event):
#     ligne,colonne=case2(event.x,event.y)
#     dessine_croix(ligne,colonne)

# canvas.bind("<Button-1>",clic)



'''
Exercice
Faire en sorte qu'on alterne entre coix et rond
'''
choix=True 
#liste 2D qui représente l'état de la grille
#à un instant donné
# 0 représente une case vide
# 1 reprénsente une croix 
# 2 représente un rond
grille=[[0,0,0], [0,0,0], [0,0,0]]

def clic(event):
    global choix
    #on détermine dans quelle case le joueur a cliqué
    ligne,colonne=case(event.x,event.y)
    #on teste si la case est vide
    if grille[ligne][colonne] == 0:
        if choix:
            dessine_croix(ligne,colonne)
            # on indique que la grille est occupé
            # par une croix
            grille[ligne][colonne] = 1
            choix = False
            label1.config(text="Au tour du cercle")
        else:
            choix = dessine_cercle(ligne,colonne)
            # on indique que la grille est occupé
            # par une croix
            grille[ligne][colonne] = 2
            choix = True
            label1.config(text="Au tour de la croix")


canvas.bind("<Button-1>",clic)

'''
Exercice
Mettre à jour la grille à chaque tour en fonction des cases dans 
lesquelles les joueurs jouent

Faire en sorte qu'on ne puisse pas jouer sur une 
case déjà rempli
'''

'''
Exercice 
Créer un label sous le canvas
Qui indique si c'est au tour du joueur croix ou rond
'''



tk.mainloop()