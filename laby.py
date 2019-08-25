'''
Mode d'ouverture: r (lecture seule)
                  w (écriture avec remplacement)
                  a (écriture avec ajout en fin de fichier)
                  x (lecture et écriture)
                  r+ (lecture/écriture dans un même fichier)

Lecture : read() (Lire tout le fichier, str)
          readline(), (Lire une ligne, str)
          readlines (Lire toutes les lignes qui n'ont pas encore été lu, str)

Ecriture : write()

Fermeture : close() (Pas besoin de fermer le fichier avec with)

Position du curseur : tell()

Curseur debut de ligne : seek()

Remplacer : replace()
'''

import random

from position import Position
from case import Case
from objets import Objets


class Laby:

    def __init__(self, placer_objets):
        self.recup_objets = Objets.recup_alea_obj
        self.cases = []
        self.chemin = []
        self.arriver = None
        self.depart = None
        self.player = None
        
    def lecture(self):
        #Ouvrir fichier
        with open("laby.txt", "r") as fichier_laby:
            for nb_ligne, ligne in enumerate(fichier_laby):
                for nb_colonne, caractere in enumerate(ligne.strip()):

                    new_position = Position(nb_ligne, nb_colonne)
                    new_case = Case(new_position)

                    if caractere == 'c':
                        self.chemin.append(new_case)
                    elif caractere == 'd':
                        self.depart = new_case
                        self.chemin.append(new_case)
                    elif caractere == 'a':
                        self.arriver = new_case
                        self.chemin.append(new_case)

    # Retirer départ et arriver de la liste des chemins
    #  def liste_chemin(self):
    #     case_libre = self.chemin

    #     if self.chemin == 'd':
    #         self.chemin.pop(case_libre)
    #     elif self.chemin == "a":
    #         self.chemin.pop(case_libre)
    #     return case_libre


    # Placer les objets 
    def placer_objets(self):
        random_position = self.case_vide_aleatoire()

        for x, objet in self.chemin:

            position = random_position[x]
            objet.position = position

            for case in self.cases:

                if case.position == objet.position:
                    case.objet = objet
                    break

    # Définir la position des cases libres en retirant les cases arriver et depart
    def case_vide_aleatoire(self):
        nombre_objets = len(self.recup_objets)
        cases = random.sample(set(self.cases) - {self.depart, self.arriver}, nombre_objets)
        positions = [case.position for case in cases]

        return positions

# pour garder l'approche obj avec inependence de classe
# automatique reconnaissance chemin
# deplacer logique dans class Laby. une fonction qui permet d'avoir la liste des chemins.
# technique : tranformer une focntion en attribut 
# fonction qui renvoit liste des endroits libre. property. ou retourner self.chemin
# enlever a ou d : prend chemin et qui enleve d et a et renvoit les valeur 
# ou renvoi case_vide_aleatoire : liste des cases libres sans a et d et renvoyer cette liste et choisir un emplacement.
# Attention : Indiquer ou son les objets et faire attention au doublon sur meme  case
