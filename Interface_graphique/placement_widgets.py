# -*- coding: utf-8 -*-
import tkinter as tk

#ouvre une fenetre
fenetre = tk.Tk()

label1 = tk.Label(fenetre, text="Label 1 qui a un long texte")
label2 = tk.Label(fenetre, text="Label 2")
label3 = tk.Label(fenetre, text="Label 3")
label4 = tk.Label(fenetre, text="Label 4")
label5 = tk.Label(fenetre, text="Label 5")

#row et column spécifient la ligne et la colonne où
#placer un widget
label1.grid(row=1,column=1)
label2.grid(row=1,column=2)
label3.grid(row=1,column=3)
label4.grid(row=1,column=1)

#columnspan permet de placer un widget à cheval
#c'est à dire sur plusieurs colonnes
label5.grid(row=2,column=1,columnspan=2)

tk.mainloop()