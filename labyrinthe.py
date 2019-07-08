from position import Position 


class Labyrinthe :

    def __init__(self):
        self.height = None
        self.width = None
        self.depart = (0, 0)
        self.arriver = (3, 0)
        self.joueur = None
        self.chemin = []
        self.mur = []
        self.objets = []

mon_labyrinthe = {
    (0,0): 'd', (0,1): 'c', (0,2): 'm', (0,3): 'c', (0,4): 'c', (0,5): 'c',
    (1,0): 'm', (1,1): 'c', (1,2): 'c', (1,3): 'c', (1,4): 'm', (1,5): 'c',
    (2,0): 'm', (2,1): 'm', (2,2): 'm', (2,3): 'm', (2,4): 'c', (2,5): 'c',
    (3,0): 'a', (3,1): 'c', (3,2): 'm', (3,3): 'c', (3,4): 'c', (3,5): 'm',
    (4,0): 'm', (4,1): 'c', (4,2): 'm', (4,3): 'c', (4,4): 'm', (4,5): 'c',
    (5,0): 'm', (5,1): 'c', (5,2): 'c', (5,3): 'c', (5,4): 'm', (5,5): 'c',
    }

def test_deplacement(self):
    self.joueur = input('Choisir une direction. z : en haut, s : en bas, q : à gauche, d : à droite').upper()
    while self.joueur != "Z" and self.joueur != "S" and self.joueur != "Q" and self.joueur != "D":
        self.joueur = input('Choisir une direction. z : en haut, s : en bas, q : à gauche, d : à droite').upper()
        if self.joueur == "Z" and self.joueur == "S" and self.joueur == "Q" and self.joueur == "D":
            break
        else :
            print("Rentrer une direction valide")
    return self.joueur


def depart_joueur (self, depart):
    depart = self.depart

    if depart not in mon_labyrinthe.keys():
        print('Hors champs')
    else:
        print(mon_labyrinthe[0,0])
    return depart_joueur
    
def valeur_deplacement(self, mon_labyrinthe):
    coordonne_ligne = int(input('Entrer coordonnées ligne : '))
    coordonne_colonne = int(input('Entrer coordonnée colonne : '))
    coordonne = (coordonne_ligne, coordonne_colonne)

    for coordonne in mon_labyrinthe.keys:
        if coordonne == mon_labyrinthe.values('m'):
            print("C'est un mur !")
        elif coordonne == 'c':
            print("Cool ! C'est un chemin")
        else:
            print('Tu es hors champs')
    return valeur_deplacement