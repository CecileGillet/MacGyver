from position import Position

class Labyrinthe:

    def __init__(self, x, y):
        self.height = None
        self.width = None
        self.depart = (0, 0)
        self.arriver = (3, 0)
        self.joueur = None
        self.chemin = 'c'
        self.mur = 'm'
        # self.objets = []
        self.x = int(x)
        self.y = int(y)

    mon_labyrinthe = {
        (0,0): 'd', (0,1): 'c', (0,2): 'm', (0,3): 'c', (0,4): 'c', (0,5): 'c',
        (1,0): 'm', (1,1): 'o', (1,2): 'c', (1,3): 'c', (1,4): 'm', (1,5): 'c',
        (2,0): 'm', (2,1): 'm', (2,2): 'm', (2,3): 'm', (2,4): 'c', (2,5): 'c',
        (3,0): 'a', (3,1): 'c', (3,2): 'm', (3,3): 'c', (3,4): 'c', (3,5): 'm',
        (4,0): 'm', (4,1): 'c', (4,2): 'm', (4,3): 'c', (4,4): 'm', (4,5): 'c',
        (5,0): 'm', (5,1): 'c', (5,2): 'c', (5,3): 'c', (5,4): 'm', (5,5): 'c',
        }

    def depart_joueur(self):
        depart = self.depart
        if depart in self.mon_labyrinthe.keys():
            print(self.mon_labyrinthe[0,0])
        else:
            print('Tu n\'est pas sur le départ')
        
    # def partie(self):
    #     self.action = True
    #     while self.action:
    #         if self.joueur == 'G':
    #             self.action = False
    #             print('Fin de la partie')
    #         else:
    #             self

    def limite_laby(self, x, y):
        self.x = self.width
        self.y = self.height
        if x and y <= 5 in self.mon_labyrinthe.keys():
            print('Tu est dans le labyrinthe')
            return True
        else:
            print('Tu est hors jeu')
            return False
            
    def deplacement_joueur(self):
        self.joueur = input('Choisir une direction. z : en haut, s : en bas, q : à gauche, d : à droite').upper()
        while self.joueur != 'Z' and self.joueur != 'S' and self.joueur != 'Q' and self.joueur != 'D':
            self.joueur = input('Choisir une direction. z : en haut, s : en bas, q : à gauche, d : à droite').upper()
            if self.joueur == 'Z' and self.joueur != 'S' and self.joueur != 'Q' and self.joueur != 'D':
                break
            else:
                print('Tu dois sélectionner une direction valide')
            return self.joueur