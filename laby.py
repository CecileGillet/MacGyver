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
from position import Position
from case import Case

class Laby:

    def __init__(self):
        self.mur = []
        self.chemin = []
        self.arriver = None
        self.depart = None
        # self.height = None
        # self.width = None

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
                
                # nb_ligne = self.width
                # nb_colonne = self.height
                
        # for position in self.depart:
        #     print(position.x, position.y)

    # def controle_deplacement(self):
    #     case = Position
    #     if case == 'c':
    #         print(Position(nb_ligne, num_colonne))
