from labyrinthe import Labyrinthe
from hero import Hero

class Position :
    '''Classe qui gére toutes les positions dans le labyrinthe x étant le numéro de ligne et y le numéro de colonne'''

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def en_bas(self, laby):
        self.x = self.x + 1
        print("G")
        if self.verif_laby(laby) == False:
            self.x = self.x - 1

    def en_haut(self, laby):
        self.x = self.x - 1
        print("G")
        if self.verif_laby(laby) == False:
            self.x = self.x +  1

    def a_droite(self, laby):
        self.y = self.y + 1
        print("G")
        if self.verif_laby(laby) == False:
            self.y = self.y - 1
    
    def a_gauche(self, laby):
        self.y = self.y - 1
        print("G")
        if self.verif_laby(laby) == False:
            self.y = self.y + 1

    def verif_laby(self,lab):
        case = (self.x, self.y)
        if case in lab.keys():
            print(lab[case])
            if lab[case] == 'c':
                return True
            else:
                return False
        else:
            print('Hors champs')
            return False
    
    def deplacement(self, direction, laby):
        if direction == 'Z':
            return self.en_haut(laby)
        elif direction == 'S':
            return self.en_bas(laby)
        elif direction == 'Q':
            return self.a_gauche(laby)
        elif direction == 'D':
            return self.a_droite(laby)