# -*- coding: utf-8 -*-
# Ce module est un des plus utilisé en Python et permet d'ouvrir une fenêtre
import tkinter as tk

'''_________________________________________________________________________________________________________________________________________'''

#Crée une fenêtre
fenetre = tk.Tk()
fenetre.title("Mon programme")
fenetre.config(background="red")

'''_________________________________________________________________________________________________________________________________________'''


#les éléments placés sur une fenêtre s'appellent des widget

#premier widget : le label permet d'afficher du texte
label = tk.Label(fenetre,text="Nombre de clics : 0")
#on place le widget sur la fenêtre avec la méthod grid()
label.grid()

'''_________________________________________________________________________________________________________________________________________'''

nb_clics=0
def modifie_label():
    # signifique que l'on veut utiliser une variable global dans une fonction local
    #on iunforme python que cette fonction peut modifier
    #la variable nb_clics
    global nb_clics 
    #on incrémente le nombre de clics
    nb_clics += 1
    #on modifie le texte affiché sur le label
    nouveau_texte = "Nombre de clics : "+str(nb_clics)
    label.config(text=nouveau_texte)

'''_________________________________________________________________________________________________________________________________________'''

#deuxième widget : le bouton
bouton = tk.Button(fenetre,text="Clique moi", command=modifie_label)
bouton.grid()


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice
Créer un deuxième bouton "reset" qui remet le compteur à 0
'''

def bouton_reset():
    global nb_clics
    nb_clics = 0
    nouveau_texte = "Nombre de clics : "+str(nb_clics)
    label.config(text=nouveau_texte) 

bouton_reset_compteur = tk.Button(fenetre,text="Compteur à 0", command=bouton_reset)
bouton_reset_compteur.grid()

'''_________________________________________________________________________________________________________________________________________'''


#boucle principale
#qui traite les événements (clics, etc.)
#toujours à la fin
tk.mainloop()


