# -*- coding: utf-8 -*-

import tkinter as tk

fenetre = tk.Tk()

label1 = tk.Label(fenetre, text="Au tour du rond")
label1.grid()

taille_case = 100 #taille d'une case de la grille
canvas = tk.Canvas(fenetre,width=3*taille_case,height=3*taille_case,background="white")

canvas.grid()
#premiere ligne verticale
# canvas.create_line(taille_case,0,taille_case,3*taille_case,width=3)

# #deuxième ligne verticale
# canvas.create_line(2*taille_case,0,2*taille_case,3*taille_case,width=3)

# #première ligne horizontale
# canvas.create_line(0,taille_case,3*taille_case,taille_case,width=3)

# #deuxième ligne horizontale
# canvas.create_line(0,2*taille_case,3*taille_case,2*taille_case,width=3)

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

    canvas.create_line(x+marge,y+marge,x+taille_case-marge,y+taille_case-marge,width=3,fill="blue",tag="cross")
    canvas.create_line(x+marge,y+taille_case-marge,x+taille_case-marge,y+marge,width=3,fill="blue",tag="cross")

# dessine_croix(2,0)

def dessine_cercle(ligne,colonne):
    #coordonées du point en haut à gauche 
    #de la case voulu
    y=ligne*taille_case
    x=colonne*taille_case

    canvas.create_oval(x+marge,y+marge,x+taille_case-marge,y+taille_case-marge,width=3,fill="blue",tag="circl")
    canvas.create_oval(x+marge,y+taille_case-marge,x+taille_case-marge,y+marge,width=3,fill="blue",tag="circl")

# dessine_cercle(1,0)

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
nb_tour=0
#liste 2D qui représente l'état de la grille
#à un instant donné
# 0 représente une case vide
# 1 reprénsente une croix 
# 2 représente un rond
grille=[[0,0,0], [0,0,0], [0,0,0]]

'''
fonction qui prend en paramètre la case où le 
joueur actuel vient de jouer et qui teste si ce
joueur a aligné trois symboles
'''
def alignement(ligne, colonne):
    #On teste s'il y a un alignement horizontal

    if grille[ligne][0] == grille[ligne][1] == grille[ligne][2]:
        return True

    if grille[0][colonne] == grille[1][colonne] == grille[2][colonne]:
        return True
    
    if grille[0][0] == grille[1][1] == grille[2][2] != 0:
        return True
    
    if grille[2][0] == grille[1][1] == grille[0][2] != 0:
        return True
    

    #On test s'il y a un alignement vertical
    #On test s'il y a un alignement diagonal
    # else :
    return False

def clic(event):
    global choix, nb_tour
    #on détermine dans quelle case le joueur a cliqué
    ligne,colonne=case(event.x,event.y)
    #on teste si la case est vide
    if grille[ligne][colonne] == 0:
        nb_tour+=1
        if choix:
            dessine_croix(ligne,colonne)
            # on indique que la grille est occupé
            # par une croix
            grille[ligne][colonne] = 1
            if alignement(ligne,colonne):
                #le joueur croix a gagné
                label1.config(text="Bravo ! Le joueur croix a gagné !")
                canvas.unbind("<Button-1>")
            elif nb_tour == 9:
                label1.config(text="Math nul !")
                canvas.unbind("<Button-1>")
            else :
                choix = False
                label1.config(text="Au tour du cercle")
        else:
            choix = dessine_cercle(ligne,colonne)
            # on indique que la grille est occupé
            # par une croix
            grille[ligne][colonne] = 2
            if alignement(ligne,colonne):
                #le joueur croix a gagné
                label1.config(text="Bravo ! Le joueur rond a gagné !")
                canvas.unbind("<Button-1>")
            else :
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

'''
Exercice 
Ajouter un bouton "Nouvelle partie"
Qui permet de relancer un nouvelle partie
Indice : pour effacer le contenu d'un canva,
on peut utiliser l'instruction canva.delete("all")
'''

def nouveau():
    global grille
    global choix
    global nb_tour
    canvas.delete("all")
    #premiere ligne verticale
    canvas.create_line(taille_case,0,taille_case,3*taille_case,width=3)
    #deuxième ligne verticale
    canvas.create_line(2*taille_case,0,2*taille_case,3*taille_case,width=3)
    #première ligne horizontale
    canvas.create_line(0,taille_case,3*taille_case,taille_case,width=3)
    #deuxième ligne horizontale
    canvas.create_line(0,2*taille_case,3*taille_case,2*taille_case,width=3)
    #réinitialisation de toutes laes variables concernées
    choix=True 
    nb_tour=0

    #liste 2D qui représente l'état de la grille
    #à un instant donné
    # 0 représente une case vide
    # 1 reprénsente une croix 
    # 2 représente un rond
    grille=[[0,0,0], [0,0,0], [0,0,0]]
    #re-permission du clic
    canvas.bind("<Button-1>",clic)



nouvelle_partie = tk.Button(fenetre, text="Nouvelle Partie",command=nouveau)
nouvelle_partie.grid()




tk.mainloop()