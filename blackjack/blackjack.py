# -*- coding: utf-8 -*-

'''
On va représenter les cartes sous forme de str
"8" représente un 8
"D" représente une dame, etc.
'''

'''
Créer une liste de 52 cartes contenant 4 as, 4 deux, etc.
jusqu'à 4 rois
'''

# paquet = []
# for i in range(4):
#     for j in range(2,10):
#         paquet.append(str(j))
#     paquet.append("V")
#     paquet.append("D")
#     paquet.append("R")
#     paquet.append("A")

#alternative avec des compréhensions de listes
# les compréhension de lsite permettent de fabriquer des liste facilement
paquet = 4*([str(j) for j in range(2,11)] + ["V","D","R","A"])

'''
Exercice 
Le casino commence par se distribuer deux cartes et en distribue deux autres
au joueur
Tirer 2 cartes au hazard pour le casino et 2 pour le joueur et afficher les cartes
'''

import random as rd

def tirage():
    i = rd.randint(0,len(paquet)-1)
    #on retire cette carte du paquet et on la renvoie
    return paquet.pop(i)

main_casino = [tirage(), tirage()]
main_joueur = [tirage(), tirage()]

# print('Casino :', main_casino)
# print("Joueur :",main_joueur)

'''
Le score d'une main correspond à la somme des points des cartes
Les cartes de 2 à 10 valent leurs chiffre 
Les figures (V, D et R) valent 10 points 
Pour le moment, on considère que l'as vaut 11 points
'''


'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice:
Ecrire une fonction qui prend en paramètre une main,
c'est à dire une liste de cartes 
et qui renvoie le score correspondant
'''

# somme = 0 
# def score(main):
#     global somme
#     for i in main:
#         if i == 'V' or i == 'D' or i == 'R':
#             i = 10
#         if i == 'A':
#             i = 11
#         somme += int(i)
#     return somme

# print(score([1,5,4,'V','D','R','A']))

def score(main):
    resultat=0
    for carte in main:
        if carte in 'VDR':
            resultat += 10
        elif carte == "A":
            #par défault tout les as sont comptés comme 1
            resultat += 1 
        else: resultat += int(carte)
    #Si j'ai un as et que je peux me permettre de le compte
    #comme 11 sans dépasser 21, je le fais,
    if "A" in main and resultat<=11:
        resultat+=10
    return resultat
# print(main_casino)
# print(score(main_casino))

'''
Exercice
Calculer le score du casino et celui du joueur.
Si le casino a 21 points avec ses deux cartes, 
(on parle de natural blackjack)
le joueur a perdu.
Sinon, le joueur a 21 points (natural blackjack),
il a gagné.
Sinon, la partie continue
'''




def jeu():
    score_casino=score(main_casino)
    score_joueur=score(main_joueur)
    print(main_casino)
    print(score(main_casino))
    print("La première carte du casino est :",main_casino[0])

    if score_casino == 21 and score_joueur == 21:
        print("Égalité !")
    elif score_casino == 21:
        print("Vous avez a perdu !")
    elif score_joueur == 21:
        print("natural blackjack ! Le casino a perdu !")
    else:
        reponse = input('Voulez-vous tirer un autre carte (hit) ou arrêter (stand) ?')
        while reponse != "stand":
            if reponse != "hit":
                print("Commande invalide.")
            else:
                main_joueur.append(tirage())
                print("Joueur :",main_joueur)
                score_joueur = score(main_joueur)
                print("Votre score :",score_joueur)
                if score_joueur > 21:
                        print('Vous avez perdu !')
                        break #quitter immédiatement la boucle
            reponse = input('Voulez-vous tirer un autre carte (hit) ou arrêter (stand) ?')
        if score_joueur <= 21:
            #le casino joue
            print("Score du casino :",main_casino)
            if score_casino == 21:
                if score_joueur == 21 and len(main_joueur) == 2:
                    print("Égalité")
                else:
                    print("Vous avez perdu")
            elif score_joueur == 21 and len(main_joueur)==2:
                print('Vous avez gagné')
            while score_casino < 17:
                main_casino.append(tirage())
                score_casino=score(main_casino)
                print("Casino :",main_casino)
            if score_casino > 21 or score_joueur > score_casino:
                print("Vous avez gagné !")
            elif score_joueur == score_casino:
                print("Égalité")
            else:
                print("Vous avez perdu !")

#Les jetons du joueur
jeton_joueur = 1000
mise_joueur = ""
def mise():
    global jeton_joueur, mise_joueur, rejouer
    mise_joueur = int(input("Combien voulez-vous miser ?"))
    while jeton_joueur > mise_joueur:
        jeu()
    else: 
        print("Vos jetons sont insuffisants..")    
    
# if jeton_joueur > mise_joueur:
#     jeu()
# else :
#     print("Vous n'avez pas assez de jetons")
#     mise_joueur = int(input(" vCombien voulez-vous miser ?"))

mise()
rejouer = ""
while rejouer != "non":
    if rejouer == "oui":
        jeu()
    else :
        print('Commande inconnu !')
    rejouer = input("Voulez-vous rejouer ?")

'''
Sinon, on demande au joueur s'il veut tirer une autre carte 
ou s'arrêter là. 
Tant que le joueur veut tirer de nouvelles 
cartes et tant qu'il ne dépasse pas 21, on lui redemande
et on les tire une par une.
S'il dépasse 21, il a perdu.
Sinon, une fois qu'il a décidé de s'arrêter, c'est au tour du casino.
Le casino va aussi tirer des cartes jusqu'à atteindre 17.
Si le casino dépasse 21, le joueur a gagné.
Sinon, le joueur gagne s'il a strictement plus que 
le casino, et perd s'il a moin ou autant.
'''

'''_________________________________________________________________________________________________________________________________________'''


'''
Exercice 
En réalité, au début de la partie, la première carte du casino est visible
mais la deuxième est cachée.
Le joueur joue sa partie et seulement après le casino
dévoile sa deuxième carte puis joue.
Modifier le programme pour prendre en compte cette règle
'''



'''
Exercice 
En réalité, l'as ne vaut pas toujours 11.
Il peut valoir 11 ou 1, suivant ce qui arrange le joueur.
En pratique, le premier as vaut 11 tant que le score est 
inférieur à 21. Si le score dépasse 21, la valeur de l'as
est réduite à 1 pour rester dans la partie.
Modifier la fonction score pour prendre en compte cette
règle.
'''

'''_________________________________________________________________________________________________________________________________________'''

'''
Exercice 
Faire en sorte qu'on puisse rejouer une partie temps qu'on en a envie
'''

'''_________________________________________________________________________________________________________________________________________'''

'''
Exercice
Donnez 1000 jetons au joueur au début du programme 
Ensuite, à chaque début de partie, le joueur indique
combien il veut miser.
Vérifier qu'il a assez de jetons et, à la fin de la partie, rendez-lui sa mise
s'il a fait égalité et doublez sa mise
s'il a gagné.
'''

