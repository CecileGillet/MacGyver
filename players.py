from laby import Laby
from case import Case
from objets import Objets

class Players:
    '''Classe du joueur'''
    
    def __init__(self, labyrinthe: labyrinthe.Laby):
        self.position = labyrinthe.depart.position
        self.objets = []
        self.labyrinthe = labyrinthe
        self.labyrinthe.player = self

    def to_move(self, instruction):
        new_position = getattr(self.position, instruction)()
        new_case = Case(new_position)

        if new_case in self.labyrinthe.case:
            self.position = new_position
            self.recup_objet(new_case)
            return True
        else:
            return False

    def recup_objet(self, test_case):
        for case in self.labyrinthe.Case:
            if case == test_case and case.position == self.position and case.objet is not None:
                case.objets.recup_objet = True
                self.objets.append(case.objet)
                case.objets = None
                break

    def fin_partie(self):
        if self.position == self.labyrinthe.arriver.position:
            if len(self.objets) == len(self.labyrinthe.objets):
                return 'Victoire'
            else:
                return 'Défaite'
        else:
            return False

# Creer hero sur case de depart. Soit dans init self.position = positionjoueur. faire faire deplacement dans class hero
# donc creer un self.laby qui represente le labyrinthe laby.chemin est accessible
# creer un sac qui regroupe les objets. une fois sur la case d'arriver regarder dans le sac. si good stop jeu sinon on continue



# joueur = Players("MG")
# print(joueur.get_pseudo())
    # def get_pseudo(self):
    #     return self.pseudo

    # def catch_object(self, objet):
    #     objet.append()
    #     return self.inventaire

# mac = Players("MG")
# print(mac.get_pseudo())