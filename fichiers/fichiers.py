# -*- coding: utf-8 -*-

#Pour sauvegarder des données dans un fichier,
#on doit l'ouvrir en écriture avec l'option open
# et l'option "w"
# Si le fichier n'existe pas, il est automatiquement créé
# On utilise la syntaxe with open() as nomdevariable
# Pour ouvrir le fichier de manière plus sûre :
#   - Le fichier est automatiquement fermé à la fin du bloc
#   - Si une erreur arrive, le fichier est proprement fermé
#   - A l'interieur du bloc, on est sûr que le fichier a 
with open("fichier.txt","w") as fichier:
    # à l'intérieur de ce bloc with le fichier est ouvert
    # à  l'éxterieur on sort
    fichier.write("Bonjour\n")
    fichier.write("Ca va ?\n")

#L'option "w" écrase le contenu du fichier
#Pour ajouter du contenu à un fichier non vide,
#on utilie l'option "a"
with open("fichier.txt","a") as fichier:
    fichier.write("Belle journée n'est-ce pas ?\n")

'''
Pour lire dans un fichier, on utilise l'option "r"
'''
with open("fichier.txt","r") as fichier:
    contenu = fichier.read()
print(contenu)
print(len(contenu))

'''
Pour récupérer les données ligne par ligne
'''
with open("fichier.txt","r") as fichier:
    # lignes = fichier.readlines()
    contenu = fichier.read()
    # permet de découper une chaine de caractère au moment du retour à la ligne
    # et les retour à la ligne sont supprimé
    lignes = contenu.splitlines()
print(lignes)