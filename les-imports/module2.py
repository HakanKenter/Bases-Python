# # -*- coding: utf-8 -*-

# #si le module à importer est dans un autre dossier
# # import sys
# # sys.path.append("chemin")
# #Le double antislash en python représente un antislash

# # Voila un exemple
# import sys
# chemin = sys.path.append("F:\\ecole+entreprise\\Could-Campus\\Deuxieme Année\\Semaine 2 - Python\\Base-Python\\")
# import FirstScript as ff

# #On importe un module en utilisant le nom du script
# #sans son extension .py
# #on peut importer un module et utiliser un alias pour
# #raccourcir les noms de fonctions
import module1 as m1
# print(m1.carre(3))

# #on peut aussi importer des fonctions ou variables spécifiques
# from module1 import carre, aire
# print(carre(3))
# print(aire(2,4))

# # ! Un peu dangereux
# # On peux importer tout ce qui est dans le module
# # sans avoir besoin de préfixe
# from module1 import *
# print(prenom)

#test des noms des variables __main__
print("__name__ de m1 depuis le module2 :",m1.__name__)
print("__name__ du module2 :", __name__)
