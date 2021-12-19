# -*- coding: utf-8 -*-
'''
Exercice
Faire en sorte qu'on puisse rejouer une partie tant qu'on
en a envie
'''

'''
Exercice
Donnez 1000 jetons au joueur au début du programme
Ensuite, à chaque début de partie, le joueur indique
combien il veut miser.
Vérifiez qu'il a assez de jetons et, à la fin de la partie,
rendez-lui sa mise s'il a fait égalité et doublez sa mise
s'il a gagné.
'''

import random as rd

def tirage(paquet):
    #on tire au hasard un indice dans la liste des cartes
    i = rd.randint(0,len(paquet)-1)
    #on retire cette carte du paquet et on la renvoie
    return paquet.pop(i)

def score(main):
    resultat=0
    for carte in main:
        if carte in "VDR":
            resultat += 10
        elif carte == "A":
            #par défaut, tous les as sont comptés comme 1
            resultat += 1
        else:
            resultat += int(carte)
    #Si j'ai un as et que je peux me permettre de le compter
    #comme 11 sans dépasser 21, je le fais
    if "A" in main and resultat<=11:
        resultat += 10
    return resultat

#joue une partie de blackjack
#renvoie un booléen : True si le joueur veut rejouer
#False sinon
def partie():
    global jetons
    print("Vous avez",jetons,"jetons.")
    mise=0
    while mise<=0 or mise>jetons:
        mise = int(input("Combien voulez-vous miser ? "))
    jetons-=mise
    
    paquet = 4*([str(j) for j in range(2,11)]+["V","D","R","A"])
    main_casino = [tirage(paquet),tirage(paquet)]
    main_joueur = [tirage(paquet),tirage(paquet)]
    print("Casino :",main_casino[0],"*")
    print("Votre main :",main_joueur)
    score_casino = score(main_casino)
    score_joueur = score(main_joueur)
    print("Votre score :",score_joueur)
    
    #Au tour du joueur
    reponse = input("Voulez-vous tirer une carte (hit) ou arrêter (stand) ? ")
    while reponse != "stand":
        if reponse != "hit":
            print("Commande invalide.")
        else:
            #on tire une nouvelle carte
            main_joueur.append(tirage(paquet))
            print("Votre main :",main_joueur)
            #on calcule le nouveau score
            score_joueur = score(main_joueur)
            print("Votre score :",score_joueur)
            if score_joueur > 21:
                print("Vous avez perdu !")
                break #quitter immédiatment la boucle
        #on demande à nouveau ce que le joueur veut faire
        reponse = input("Voulez-vous tirer une carte (hit) ou arrêter (stand) ? ")
    if score_joueur <= 21:
        #Au tour du casino
        #On dévoile la deuxième carte du casino
        print("Casino :",main_casino)
        print("Score du casino :",score_casino)
        if score_casino == 21:#natural blackjack
            if score_joueur == 21 and len(main_joueur)==2:#natural blackjack
                print("Egalité")
                jetons+=mise
            else:
                print("Vous avez perdu !")
        elif score_joueur == 21 and len(main_joueur)==2:#natural blackjack
            print("Vous avez gagné !")
            jetons+=2*mise
        else:#aucun natural blackjack
            while score_casino < 17:
                #on tire une nouvelle carte
                main_casino.append(tirage(paquet))
                #on calcule le nouveau score
                score_casino=score(main_casino)
            print("Casino :",main_casino)
            print("Score du casino :",score_casino)
            if score_casino > 21 or score_joueur > score_casino:
                print("Vous avez gagné !")
                jetons+=2*mise
            elif score_joueur == score_casino:
                print("égalité")
                jetons+=mise
            else:
                print("Vous avez perdu !")
    print()
    reponse = input("Voulez-vous rejouer ? (o/n) ")
    return reponse in "Ouioui"
    
jetons=1000
while jetons>0 and partie():
    #mot-clé servant à indiquer qu'on n'a rien
    #à faire dans la boucle
    pass

if jetons==0:
    print("Vous êtes à sec !")
    
    