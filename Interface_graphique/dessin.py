# -*- coding: utf-8 -*-
import tkinter as tk

fenetre = tk.Tk()

#le canvas permet de dessiner des formes à l'écran
#et d'intéragir avec l'utilisateur

#Quand on a un canva (toile) il faut mettre la largeur et la hauteur
canvas = tk.Canvas(fenetre,width=400,height=300,background="#002379")
canvas.grid()

#create_line(x1,y1,x2,y2) -> dessine un segement du point
# (x1,y1) au point (x2, y2)
# on peut choisir l'épaisseur du trait avec width
#et la couleur avec fill
#Attention ! Dans une canvas, l'axe y (des ordonnées)
#est dirigé vers le bas : y=0 en haut du canvas
#et y augmente quand on descend
# canvas.create_line(20,50,200,140,width=5,fill='red')

#ligne verticale qui coupe le canvas en deux
#dans son milieu
# canvas.create_line(200, 0, 200, 300)


'''
Exercice
Tracer les deux diagonales du canvas
C'est à dire la ligne qui part du coin 
en haut à gauche et qui va jusqu'au coin en bas
à droite
Et celle qui part du bas à gauche et qui va en 
haut à droite
'''

#diagonales
canvas.create_line(0,0,400,300,width=30,fill="white")
canvas.create_line(0,300,400,0,width=30,fill="white")

#rectangle 
#Pour un rectangl, on donne les coordonées 
#des deux sommets opposés
canvas.create_rectangle(100,200,180,250,fill="red",outline="blue",width=5)

#Pour un ovale, on donne les coordonées du rectangle
#qui contient l'ovale
canvas.create_oval(300,20,350,60,fill="blue",outline="black",width=5)

#Pour affihcer du texte à une position donnée
canvas.create_text(150,50,text="Quel beau dessin !",fill="white")

tk.mainloop()
