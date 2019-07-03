mon_labyrinthe = {
    (0,0): 'd', (0,1): 'c', (0,2): 'm', (0,3): 'c', (0,4): 'c', (0,5): 'c',
    (1,0): 'm', (1,1): 'c', (1,2): 'c', (1,3): 'c', (1,4): 'm', (1,5): 'c',
    (2,0): 'm', (2,1): 'm', (2,2): 'm', (2,3): 'm', (2,4): 'c', (2,5): 'c',
    (3,0): 'a', (3,1): 'c', (3,2): 'm', (3,3): 'c', (3,4): 'c', (3,5): 'm',
    (4,0): 'm', (4,1): 'c', (4,2): 'm', (4,3): 'c', (4,4): 'm', (4,5): 'c',
    (5,0): 'm', (5,1): 'c', (5,2): 'c', (5,3): 'c', (5,4): 'm', (5,5): 'c',
    } 

items = mon_labyrinthe.items()
print(items)

# def dictionnaire():
#     for position in enumerate(mon_labyrinthe):
#         print(position)
#         for cle in mon_labyrinthe.keys():
#             print(cle)
#         for valeur in mon_labyrinthe.values():
#             print(valeur)
#     return position + valeur
# dictionnaire()

# for position, cle in enumerate(mon_labyrinthe):
#     print(position, cle)


# list_labyrinthe = (
#     'd', 'c', 'm', 'c', 'c', 'c',
#     'm', 'c', 'c', 'c', 'm', 'c',
#     'm', 'm', 'm', 'm', 'c', 'c',
#     'a', 'c', 'm', 'c', 'c', 'm',
#     'm', 'c', 'm', 'c', 'm', 'c',
#     'm', 'c', 'c', 'c', 'm', 'c'
#     )

# nb_ligne = ''
# nb_colonne =  ''

# def lire_liste():
#     liste = []
#     while liste in list_labyrinthe:
#         for nb_ligne, ligne in enumerate(list_labyrinthe):
#             ajout_ligne = []
#             for nb_colonne, colonne in enumerate(ligne.strip()):
#                 ajout_ligne.append(colonne)
#         liste.append(ajout_ligne)
#     return liste
# print(lire_liste())
# # liste = lire_liste()

# def afficher_case(labyrinthe):
#     print